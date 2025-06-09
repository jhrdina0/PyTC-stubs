import System
import Teamcenter.Services.Internal.Strong.Projectmanagement._2007_06.ScheduleManagement
import Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class LoadProgramViewContainer:
    def __init__(self, ) -> None: ...
    Schedules: list[str]
    LoadProgramViewSets: list[LoadProgramViewSet]

class LoadProgramViewFilter:
    def __init__(self, ) -> None: ...
    Field: str
    Value: str
    Condition: int

class LoadProgramViewSet:
    def __init__(self, ) -> None: ...
    LoadProgramViewFilters: list[LoadProgramViewFilter]

class ScheduleModifyContainer:
    def __init__(self, ) -> None: ...
    ScheduleUid: str
    ScheduleUpdates: Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer
    Options: Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.SchMgtOptions
    NewTasks: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    NewDependencies: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    NewAssignments: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    TaskUpdates: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    DependencyUpdates: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    AssignmentUpdates: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    DeletedTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    DeletedDependencies: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    DeletedAssignments: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]
    NewProxyTasks: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    ProxyTaskUpdates: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    DeletedProxyTasks: list[Teamcenter.Soa.Client.Model.ModelObject]
    InsertedSubSchedules: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer]
    DetachedSubSchedules: list[Teamcenter.Soa.Client.Model.ModelObject]

class ScheduleModifyResponse:
    def __init__(self, ) -> None: ...
    NewTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    NewProxyTasks: list[Teamcenter.Soa.Client.Model.Strong.Fnd0ProxyTask]
    NewDependencies: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    NewAssignments: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]

class ScheduleModifyResponses:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Responses: list[ScheduleModifyResponse]

class ScheduleManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def LoadProgramView(self, LoadProgramViewContainer: LoadProgramViewContainer) -> Teamcenter.Services.Internal.Strong.Projectmanagement._2007_06.ScheduleManagement.LoadProgramViewResponse: ...
    def ModifySchedules(self, ScheduleModifyContainers: list[ScheduleModifyContainer]) -> ScheduleModifyResponses: ...

