import System
import Teamcenter.Soa.Client.Model
import typing

class ObjectCoverageInput:
    """
    Structure contains input parameters for verifyObjectCoverageByRule operation
    """
    def __init__(self, ) -> None: ...
    Contexts: list[Teamcenter.Soa.Client.Model.ModelObject]
    """scoped lines in the target window"""
    ObjectsToCheck: list[Teamcenter.Soa.Client.Model.ModelObject]
    """the list of lines,that will be checked against the supplied closure rule"""
    ClosureRule: str
    """the closure rule selected by the user"""
    Depth: int
    """the traversal depth entered by the user"""
    OtherStructure: Teamcenter.Soa.Client.Model.ModelObject
    """context of another structure (can be window or any line in it)"""

class ObjectCoverageResponse:
    """
    Structure contains output parameters for verifyObjectCoverageByRule operation
    """
    def __init__(self, ) -> None: ...
    Covered: list[bool]
    """return vector (corresponds to the input objects vector) - with true or false"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """contains any errors received during the execution"""

class TraversedObjectsInput:
    """
    structure contains input parameters for getTraversedObjectsByRule operation
    """
    def __init__(self, ) -> None: ...
    ScopeObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """the scope lines selected by the user"""
    ClosureRule: str
    """the closure rule selected by the user"""
    Depth: int
    """the traversal depth entered by the user"""
    OtherStructure: Teamcenter.Soa.Client.Model.ModelObject
    """target context (can be window or any line in it)"""

class TraversedObjectsResponse:
    """
    structure contains output parameters for getTraversedObjectsByRule operation
    """
    def __init__(self, ) -> None: ...
    ResultObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """return vector of the the auto-expanded/filtered lines"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """return errors if verifacation was failed or illegal"""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTraversedObjectsByRule(self, Input: TraversedObjectsInput) -> TraversedObjectsResponse:
        """    
             This SOA traverses the structure according to supplied filtering rule and returns
             the full list of resulting lines.
             

Teamcenter Component:

             BOM Expand - Set of core services that allow to efficiently solve a product structure
             based on revision rules; effectivities etc.
             
        :param Input: 
                         TraversedObjectsInput structure
             
        :return: return the filtered and expanded lines for a structure
        """
        ...
    def VerifyObjectCoverageByRule(self, Input: ObjectCoverageInput) -> ObjectCoverageResponse:
        """    
             This SOA verifies whether the received lines fit the supplied filtering rule.
             

Teamcenter Component:

             BOM Expand - Set of core services that allow to efficiently solve a product structure
             based on revision rules; effectivities etc.
             
        :param Input: 
                         ObjectCoverageInput structure
             
        :return: for each received line returns whether it fits the supplied closure rule
        """
        ...

