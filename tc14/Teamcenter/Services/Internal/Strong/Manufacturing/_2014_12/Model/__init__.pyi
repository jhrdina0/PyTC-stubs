import System
import Teamcenter.Soa.Client.Model
import typing

class ExternalNodeInfo:
    def __init__(self, ) -> None: ...
    ExternalNode: Teamcenter.Soa.Client.Model.ModelObject
    UiLocation: str
    ConnectedNodes: list[Teamcenter.Soa.Client.Model.ModelObject]

class LABatchDetails:
    def __init__(self, ) -> None: ...
    Identifier: str
    Mode: str
    Site: int
    Priority: int
    StartTime: System.DateTime
    EndTime: System.DateTime
    DaysOfWeek: list[bool]
    EndAfterOccurrences: int
    PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]

class LAResolveAsyncData:
    def __init__(self, ) -> None: ...
    ScopeLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    Products: list[Teamcenter.Soa.Client.Model.ModelObject]
    ResolveRecursively: bool

class ScopeFlowInfo:
    def __init__(self, ) -> None: ...
    Predecessor: Teamcenter.Soa.Client.Model.ModelObject
    Successor: Teamcenter.Soa.Client.Model.ModelObject

class UILocationInfo:
    def __init__(self, ) -> None: ...
    ContextLine: Teamcenter.Soa.Client.Model.ModelObject
    ExternalNodesInfo: list[ExternalNodeInfo]

class UILocationsInfoResponse:
    def __init__(self, ) -> None: ...
    UiLocationsInfo: list[UILocationInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Model:
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteScopeFlows(self, ScopeFlowsInfo: list[ScopeFlowInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetUILocations(self, ContextLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> UILocationsInfoResponse: ...
    def SaveUILocations(self, UiLocationsInfo: list[UILocationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ScheduleLAResolve(self, LaResolveData: LAResolveAsyncData, BatchDetails: LABatchDetails) -> Teamcenter.Soa.Client.Model.ServiceData: ...

