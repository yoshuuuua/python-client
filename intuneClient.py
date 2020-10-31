import requests
import adalClient
import json
from locationProvider import LocationProvider

def PostAsync(service_name, url_suffix, service_version, body, activityId, parameters):
    auth_token = adalClient.get_token(parameters)

    location_provider = LocationProvider(parameters)

    intune_service_endpoint = location_provider.GetServiceEndpointAsync(service_name)

    print(intune_service_endpoint)
    # print(json.dumps(auth_token, indent=2))

