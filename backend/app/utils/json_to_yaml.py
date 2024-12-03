import json
import yaml

"""
run the following command inside `./app` after activating fatAPI 
```
curl http://localhost:8000/openapi.json -o openapi.json
```
"""

with open("../openapi.json", "r") as json_file:
    openapi_json = json.load(json_file)
 
with open("../APIspecification.yaml", "w") as yaml_file:
    yaml.dump(openapi_json, yaml_file, default_flow_style=False)
