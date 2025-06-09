import Teamcenter.Soa.Client.Model
import typing

class ClassificationObjectResponse:
    """
    Holds information on created, updated or deleted classification objects.
    """
    def __init__(self, ) -> None: ...
    JsonResponse: str
    """
            This is a JSON string containing information about the created, updated, retrieved
            or deleted classification objects.
            
            Any failures occurred during the operation will be specified in the JSON string under
            the 'ErrorDetails' container. The response structure will follow the JSON schema
            defined in the file: TC_DATA\classification\json\cla\1.0.0\schema\Response.schema.json.
            
            Refer the following sample responses for operations on classification objects:
            
            Save and Retrieve:- TC_DATA\classification\json\cla\1.0.0\samples\GetClassificationObjects_Response_sample.json
            
            Delete:- TC_DATA\classification\json\cla\1.0.0\samples\DeleteClassificationObjects_Response_sample.json
            
            Error:- TC_DATA\classification\json\cla\1.0.0\samples\SaveClassificationObjects_Error_Response_sample.json
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a placeholder for future use. All information about the created, updated
            and deleted classification objects and any errors, occurred during the operation,
            will be returned in the JSON response string.
            """

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteClassificationObjects(self, JsonRequest: str) -> ClassificationObjectResponse: ...
    def GetClassificationObjects(self, JsonRequest: str) -> ClassificationObjectResponse: ...
    def SaveClassificationObjects(self, JsonRequest: str) -> ClassificationObjectResponse: ...

