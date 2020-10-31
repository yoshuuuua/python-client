import json
import intuneClient
from uuid import UUID

DEFAULT_SERVICE_VERSION = "2018-02-20";
VALIDATION_SERVICE_NAME = "ScepRequestValidationFEService";
VALIDATION_URL = "ScepActions/validateRequest";
NOTIFY_SUCCESS_URL = "ScepActions/successNotification";
NOTIFY_FAILURE_URL = "ScepActions/failureNotification"

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def ValidateRequestAsync(transactionId, certificateRequest):
    if not transactionId:
        raise Exception("TransactionId may not be null")

    with open('PARAMETERS.json') as f:
        parameters = json.load(f)

    dict_body = {
        "request": 
        {
            "transactionId":transactionId,
            "certificateRequest": certificateRequest,
            "callerInfo": parameters["providerNameAndVersion"]
        }
    }
    json_body = json.dumps(dict_body, cls=UUIDEncoder)
    PostAsync(json_body, VALIDATION_URL, transactionId, parameters)

def PostAsync(body, url_Suffix, transactionId, parameters):
    intuneClient.PostAsync(VALIDATION_SERVICE_NAME, url_Suffix, DEFAULT_SERVICE_VERSION, body, transactionId)


