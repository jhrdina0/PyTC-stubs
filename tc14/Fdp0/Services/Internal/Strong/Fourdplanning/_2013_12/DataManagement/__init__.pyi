import System
import Teamcenter.Soa.Client.Model
import typing

class CompareProcessWithScheduleTaskInfo:
    def __init__(self, ) -> None: ...
    InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    ConsiderHierarchy: bool

class CompareProcessWithScheduleTaskResponse:
    def __init__(self, ) -> None: ...
    Output: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PropagateScheduleChangesInfo:
    def __init__(self, ) -> None: ...
    InputObject: list[Teamcenter.Soa.Client.Model.ModelObject]
    ConsiderHierarchy: bool

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CompareProcessWithScheduleTask(self, Input: CompareProcessWithScheduleTaskInfo) -> CompareProcessWithScheduleTaskResponse: ...
    def PropagateScheduleChanges(self, Input: PropagateScheduleChangesInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...

