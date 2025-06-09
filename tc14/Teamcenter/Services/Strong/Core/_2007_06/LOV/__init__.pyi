import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttachedLOVsResponse:
    """
    AttachedLOVsResponse
    """
    def __init__(self, ) -> None: ...
    InputTypeNameToLOVOutput: System.Collections.Hashtable
    """Map of input type name to LOVOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData which has output tags as plain objects and errors in partialError"""

class LOVInfo:
    """
    LOVInfo
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """The name of the Teamcenter Engineering type to which property belongs"""
    PropNames: list[str]
    """List of Property names to which the LOV is attached"""

class LOVOutput:
    """
    LOVOutput
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Input Property name to which the LOV is attached"""
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    """The attached LOV tag found for the input type and property name"""

class LOV:
    """
    Interface LOV
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAttachedLOVs(self, Inputs: list[LOVInfo]) -> AttachedLOVsResponse:
        """    
             Get attached LOV based on input type name and property names structure. The LOV Tag
             is returned in the response and service data.
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param Inputs: 
                         - vector of structure of LOVInfo with type name and property names vector.
             
        :return: AttachedLOVsResponse - Response structure with Map of input Index to LOV tag and
             serviceData
        """
        ...

