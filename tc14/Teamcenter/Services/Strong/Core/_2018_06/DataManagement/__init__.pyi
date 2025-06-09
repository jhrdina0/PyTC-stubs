import Teamcenter.Services.Strong.Core._2008_06.DataManagement
import Teamcenter.Services.Strong.Core._2015_07.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class CreateIn3:
    """
    
            This is an input structure for create operation of a single object including unique
            client identifier.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier."""
    CreateData: Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreateInput2
    """Input data for create operation."""
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """Target to which the created object will be related."""
    PasteProp: str
    """
            Property to be used to relate the created object to the targetObject. This
            can be something similar to the illustrations below:
            
(1)      A reference property on the targetObject Type. For example,
            "contents" on targetObject of Type Folder.
            
(2)      A relation property on the targetObject Type. For example,
            "IMAN_reference" on targetObject of Type Item or "IMAN_specification"
            on targetObject of Type ItemRevision.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateObjectsInBulkAndRelate(self, CreateInputs: list[CreateIn3]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...

