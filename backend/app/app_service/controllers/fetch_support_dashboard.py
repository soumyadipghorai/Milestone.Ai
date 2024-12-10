from models.db_models import SupportTeam
from models.database import get_db
from _temp.config import INFO_LOG_FILE_PATH, DEBUG_LOG_FILE_PATH
from collections import deque

class DBOps : 
    def __init__(self) : 
        self.db = get_db()

class DashboardGenerator(DBOps) : 
    def __init__(self, support_id: str = "") -> None : 
        self.support_id = support_id  
        super().__init__()  

    def __find_metric(self) : 
        output = {
            "info" : 0, "warning" : 0, "critical" : 0, 
            "error" : 0
        }
        with open(DEBUG_LOG_FILE_PATH, "r") as file:
            for line in file : 
                if "WARNING" in line : 
                    output["warning"] += 1 
                elif "ERROR" in line : 
                    output["error"] += 1
                elif "CRITICAL" in line : 
                    output["critical"] += 1
                elif "INFO" in line : 
                    output["info"] += 1

        return {
                "labels": ['WARNING', 'ERROR', 'CRITICAL', 'INFO'],  
                "datasets": [
                    {
                        "label": 'Log type',
                        "data": [output["warning"], output["error"], output["critical"], output["info"]],   
                        "backgroundColor": ['#007BFF', 'rgba(0, 123, 255, 0.8)', 'rgba(0, 123, 255, 0.65)', 'rgba(0, 123, 255, 0.25)'],
                        "borderColor": '#ffffff',  
                        "borderWidth": 2,
                    },
                ],
                **output
            }

            

    def __fetch_logs(self, file_type: str = 'info') : 
        output, file_path = [], INFO_LOG_FILE_PATH if file_type == 'info' else DEBUG_LOG_FILE_PATH
        with open(file_path, "r") as file:
            last_100_lines = deque(file, maxlen=100)

        for line in last_100_lines:   
            try :
                time_stamp, source, log_type, log_message = line.split(' - ')
                output.append({
                    "time_stamp" : time_stamp.strip(), "source" : source.strip(), 
                    "log_type" : log_type.strip(), "log_message" : log_message.strip()
                })
            except : 
                pass 

        return output        

    def get_dashboard(self) : 
        user_details = self.db.query(SupportTeam).filter(SupportTeam.id == self.support_id).first()  
        if user_details :
            return {
                "registered" : True,
                "info" : self.__fetch_logs(file_type="info"),
                "debug" : self.__fetch_logs(file_type="debug"),
                "metric" : self.__find_metric()
            } 
        else : 
            return {
                "registered" : False,
            } 