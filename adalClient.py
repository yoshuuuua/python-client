import json
import logging
import os
import sys
import adal

def get_token():
    with open('PARAMETERS.json') as f:
        parameters = json.load(f)

    authority_url = (parameters['authorityHostUrl'] + '/' + parameters['tenant'])
    GRAPH_RESOURCE = '00000002-0000-0000-c000-000000000000'
    RESOURCE = parameters.get('resource', GRAPH_RESOURCE)

    context = adal.AuthenticationContext(
        authority_url, validate_authority=parameters['tenant'] != 'adfs',
        )

    return context.acquire_token_with_client_credentials(
        RESOURCE,
        parameters['clientId'],
        parameters['clientSecret'])

    # print('Here is the token:')
    # print(json.dumps(token, indent=2))
