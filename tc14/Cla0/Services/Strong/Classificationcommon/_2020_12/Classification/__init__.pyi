import typing

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
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

