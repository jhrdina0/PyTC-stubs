import System
import Teamcenter.Soa.Client.Model
import typing

class AutomaticMFGFeaturesAssignmentInputInfo:
    def __init__(self, ) -> None: ...
    SourceContexts: list[Teamcenter.Soa.Client.Model.ModelObject]
    TargetContexts: list[Teamcenter.Soa.Client.Model.ModelObject]
    ConsiderCycleTime: bool
    MatchType: str

class AutomaticMFGFeaturesAssignmentResponse:
    def __init__(self, ) -> None: ...
    AssignmentList: list[StationAssignmentStruct]
    LogFileTicket: str
    LogFileName: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FeatureAssignmentStruct:
    def __init__(self, ) -> None: ...
    FeatureObject: Teamcenter.Soa.Client.Model.ModelObject
    OccChain: str
    Operation: Teamcenter.Soa.Client.Model.ModelObject
    AssignedType: str

class StationAssignmentStruct:
    def __init__(self, ) -> None: ...
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    FeatureAssignmentList: list[FeatureAssignmentStruct]

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AutomaticMFGFeaturesAssignment(self, Input: AutomaticMFGFeaturesAssignmentInputInfo) -> AutomaticMFGFeaturesAssignmentResponse: ...

