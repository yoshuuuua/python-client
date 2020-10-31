import json
import logging
import os
import sys
import adal

def get_token(parameters, resource = ""):
    authority_url = (parameters['authorityHostUrl'] + '/' + parameters['tenant'])
    GRAPH_RESOURCE = '00000002-0000-0000-c000-000000000000'
    if not resource:
        resource = parameters.get('resource', GRAPH_RESOURCE)

    context = adal.AuthenticationContext(
        authority_url, validate_authority=parameters['tenant'] != 'adfs',
        )

    print(resource)
    return context.acquire_token_with_client_credentials(
        resource,
        parameters['clientId'],
        parameters['clientSecret'])

    # print('Here is the token:')
    # print(json.dumps(token, indent=2))
