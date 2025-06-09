import Cla0.Services.Strong.Classificationcommon._2020_01.Classification
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class ClassificationRestBindingStub(ClassificationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def DeleteClassificationObjects(self, JsonRequest: str) -> Cla0.Services.Strong.Classificationcommon._2020_01.Classification.ClassificationObjectResponse: ...
    def GetClassificationObjects(self, JsonRequest: str) -> Cla0.Services.Strong.Classificationcommon._2020_01.Classification.ClassificationObjectResponse: ...
    def SaveClassificationObjects(self, JsonRequest: str) -> Cla0.Services.Strong.Classificationcommon._2020_01.Classification.ClassificationObjectResponse: ...
    def GetClassDescriptor(self, JsonRequest: str) -> str: ...
    def ImportClassificationDefinitions(self, FileTicket: str, DryRun: bool) -> str: ...
    def SearchClassificationDefinitions(self, JsonRequest: str) -> str: ...
    def SearchClassificationObjects(self, JsonRequest: str) -> str: ...
    def ImportClassificationData(self, FileTicket: str, RelativePathToClsDataFile: str, ProcessAsAsync: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteClassificationDefinitions(self, Request: str) -> str: ...
    def SaveClassificationDefinitions(self, Request: str) -> str: ...

class ClassificationService:
    """
    
            The Classification service serves as a common entry point for interacting with all
            the underlying classification systems. The service allows users to create classification
            objects and associate them to workspace objects in order to classify the workspace
            objects. It can also be used to perform add, update, or delete operations on classification
            objects and retrieve information about them.
            

            The Classification service contains operations to achieve the following:
            

Create classification objects and optionally attach them to workspace
            objects.
            
Update existing classification objects.
            
Delete existing classification objects.
            
Get information on classification objects.
            
Create graphics based on part family templates or based on template
            parts
            




Library Reference:

Cla0SoaClassificationCommonStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ClassificationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def DeleteClassificationObjects(self, JsonRequest: str) -> Cla0.Services.Strong.Classificationcommon._2020_01.Classification.ClassificationObjectResponse: ...
    def GetClassificationObjects(self, JsonRequest: str) -> Cla0.Services.Strong.Classificationcommon._2020_01.Classification.ClassificationObjectResponse: ...
    def SaveClassificationObjects(self, JsonRequest: str) -> Cla0.Services.Strong.Classificationcommon._2020_01.Classification.ClassificationObjectResponse: ...
    def GetClassDescriptor(self, JsonRequest: str) -> str:
        """    
             Gets detailed information about a classification class based on classification node
             ID. This information includes class type, parent, name, description, unit system
             and user data associated with the class. It also includes a count of children, number
             of classification views and number of instances of classification objects associated
             with the classification class. Information can also be obtained on any documents
             such as images and icons attached to the classification class.
             

Use Cases:

             When user need details of classification classes. These details can help user decide
             whether to classify a workspace object into particular classification classes.
             

Teamcenter Component:

             Classification Interface - Component for the template - cla0classification
             
        :param JsonRequest: 
                         A JSON string containing information about the classification objects to be retrieved.
                         The structure of the JSON string must follow the JSON schema specified in the file:
                         TC_DATA\classification\json\cla\1.0.0\schema\Classification_Get_ClassDescriptor_Request.schema.json.
             
        :return: 
        """
        ...
    def ImportClassificationDefinitions(self, FileTicket: str, DryRun: bool) -> str: ...
    def SearchClassificationDefinitions(self, JsonRequest: str) -> str: ...
    def SearchClassificationObjects(self, JsonRequest: str) -> str: ...
    def ImportClassificationData(self, FileTicket: str, RelativePathToClsDataFile: str, ProcessAsAsync: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteClassificationDefinitions(self, Request: str) -> str:
        """    
             Deletes one or multiple classification definitions permanently. This can be used
             for basic and also advanced Classification.
             

Use Cases:

             User needs to delete classification definitions. It is typically called when after
             creating or searching the classification definitions, user decides that the returned
             objects are not needed anymore.
             

Teamcenter Component:

             Classification Interface - Component for the template - cla0classification
             
        :param Request: 
                         A sample input for deleting classification objects is provided in the file: TC_DATA\classification\json\cla\1.0.0\samples\DeleteClassificationDefinitions_Request_sample.json.
             
        :return: 
        """
        ...
    def SaveClassificationDefinitions(self, Request: str) -> str: ...

