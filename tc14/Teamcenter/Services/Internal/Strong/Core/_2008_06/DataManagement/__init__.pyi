import System
import Teamcenter.Services.Strong.Core._2008_06.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateRelationsOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation

class CreateRelationsResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreateRelationsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MultiRelationMultiLevelExpandRelationship:
    def __init__(self, ) -> None: ...
    RelationName: str
    IsPrimaryObject: bool

class MultiRelationMultiLevelExpandChildNodes:
    def __init__(self, ) -> None: ...
    Relationship: MultiRelationMultiLevelExpandRelationship
    Children: list[MultiRelationMultiLevelExpandOutputNode]

class MultiRelationMultiLevelExpandOutputNode:
    def __init__(self, ) -> None: ...
    CurrentObject: Teamcenter.Soa.Client.Model.ModelObject
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    RelAndChildNodes: list[MultiRelationMultiLevelExpandChildNodes]

class MultiRelationMultiLevelExpandResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    FoundObjects: MultiRelationMultiLevelExpandOutputNode

class MultiRelMultiLevelExpandInput:
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    Relationships: list[MultiRelationMultiLevelExpandRelationship]

class Relationship:
    def __init__(self, ) -> None: ...
    ClientId: str
    RelationType: str
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    SecondaryObject: Teamcenter.Soa.Client.Model.ModelObject
    UserData: Teamcenter.Soa.Client.Model.ModelObject

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ReviseObject(self, Info: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.ReviseInfo], DeepCopyRequired: bool) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.ReviseResponse2: ...
    def SaveAsNewItemObject(self, Info: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.SaveAsNewItemInfo], DeepCopyRequired: bool) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.SaveAsNewItemResponse2: ...
    def CreateCachedRelations(self, Input: list[Relationship]) -> CreateRelationsResponse: ...
    def MultiRelationMultiLevelExpand(self, Input: MultiRelMultiLevelExpandInput) -> MultiRelationMultiLevelExpandResponse: ...
    def SetDefaultProjectForProjectMembers(self, Project: Teamcenter.Soa.Client.Model.ModelObject, ProjectMembers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

