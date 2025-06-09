import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetManagedRelationInput:
    """
    GetManagedRelationInput
    """
    def __init__(self, ) -> None: ...
    PrimaryTags: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of primaryTags"""
    SecondaryTags: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of secondaryTags"""
    PrimaryType: str
    """// primaryType of Managed relation"""
    Subtype: str
    """// subtype of primary type"""

class GetManagedRelationResponse:
    """
    GetManagedRelation Response
    """
    def __init__(self, ) -> None: ...
    ManagedRelations: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """Tracelink relations"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The successful Object ids, partial errors and failures"""

class ManagedRelations:
    """
    Interface ManagedRelations
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetManagedRelations(self, Inputdata: GetManagedRelationInput) -> GetManagedRelationResponse:
        """    
             This operation will return tracelinks between primary and secondary objects.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputdata: 
                         information required to get tracelink relations
             
        :return: will return tracelink relations between primary and secondary objects and error message
             in the ServiceData.
        """
        ...

