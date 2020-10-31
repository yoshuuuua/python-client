import requests
import adalClient
import json

def PostAsync(service_name, url_suffix, service_version, body, activityId):
    auth_token = adalClient.get_token()
    print('Here is the token:')
    print(json.dumps(auth_token, indent=2))

