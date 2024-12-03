from dotenv import main
import os 

_ = main.load_dotenv(main.find_dotenv())
github_token = os.getenv("GITHUB_TOKEN")

class GitHubBase : 
    def get_header(self) : 
        return {"Authorization": f"Bearer {github_token}"}