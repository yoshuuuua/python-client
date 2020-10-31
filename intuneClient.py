import requests
import adalClient
import json
import requests
from locationProvider import LocationProvider

DEFAULT_INTUNE_RESOURCE_URL = "https://api.manage.microsoft.com/"

def PostAsync(service_name, url_suffix, service_version, body, activityId, parameters):
    location_provider = LocationProvider(parameters)
    intune_service_endpoint = location_provider.GetServiceEndpointAsync(service_name)
    auth_token = adalClient.get_token(parameters, DEFAULT_INTUNE_RESOURCE_URL)
    intune_request_url = intune_service_endpoint + "/" + url_suffix;

    headers = {
            "client-request-id": str(activityId),
            "Authorization": "Bearer " + auth_token['accessToken'],
            "api-version": service_version
        }
    print(intune_request_url)
    print(body)
    print(headers)

    response = requests.post(intune_request_url, data=body, headers=headers).json()
    print(response)
