import adalClient
import json
import uuid
import requests

class LocationProvider:

    service_map = dict()
    DEFAULT_GRAPH_VERSION = "1.6"
    DEFAULT_INTUNE_APP_ID = "0000000a-0000-0000-c000-000000000000"

    def __init__(self, parameters):
        self.parameters = parameters
        self.resource = parameters['resource']
        self.tenantId = parameters['tenantId']
        self.client_id = parameters['clientId']

    def GetServiceEndpointAsync(self, service_name):
        service_name_lower = service_name.lower()

        if not(self.service_map):
            self.RefreshServiceNameAsync()

        if service_name_lower in self.service_map:
            return self.service_map[service_name_lower]

        return ""

    def RefreshServiceNameAsync(self):
        auth_token = adalClient.get_token(self.parameters)

        graph_request = self.resource + self.tenantId + "/servicePrincipalsByAppId/" + self.DEFAULT_INTUNE_APP_ID + "/serviceEndpoints?api-version=" + self.DEFAULT_GRAPH_VERSION;
        activityId = str(uuid.uuid4())

        headers = {
            "client-request-id": activityId,
            "Authorization": "Bearer " + auth_token['accessToken']
        }

        response = requests.get(graph_request, headers=headers).json()
        service_endpoints = response['value']

        for service in service_endpoints:
            self.service_map[service['serviceName'].lower()] = service['uri']

