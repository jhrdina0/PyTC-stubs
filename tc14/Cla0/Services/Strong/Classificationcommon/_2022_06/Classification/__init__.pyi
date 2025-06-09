import typing

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
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

