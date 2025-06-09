import System
import Teamcenter.Services.Internal.Strong.Core._2018_06.LogicalObject
import Teamcenter.Soa.Client.Model
import typing

class AddIncludedLogicalObjectsResponse:
    def __init__(self, ) -> None: ...
    IncludedLogicalObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AddIncludedLOInput:
    def __init__(self, ) -> None: ...
    LogicalObjectType: Teamcenter.Soa.Client.Model.ModelObject
    IncludedLODefinitions: list[IncludedLogicalObjectDefinition]

class IncludedLogicalObjectDefinition:
    def __init__(self, ) -> None: ...
    IncludedLogicalObjectID: str
    DisplayName: str
    Description: str
    TraversalPath: list[Teamcenter.Services.Internal.Strong.Core._2018_06.LogicalObject.TraversalHop2]
    ApplyConfigurationContext: bool

class LogicalObject:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddIncludedLogicalObjects(self, AddIncludedLOInput: AddIncludedLOInput) -> AddIncludedLogicalObjectsResponse: ...

