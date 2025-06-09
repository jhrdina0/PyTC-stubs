import System
import Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeferredSaveOption:
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    DeferredOption: int

class DeferredSaveResponse:
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    ScheduleUpdates: Teamcenter.Services.Internal.Strong.Projectmanagement._2008_06.ScheduleManagement.GenericAttributesContainer
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
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PasteTaskContainer:
    def __init__(self, ) -> None: ...
    SourceTask: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    PrevSibling: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    NewParent: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    Flag: int

class ScheduleManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def DeferredSave(self, DeferredOption: DeferredSaveOption) -> DeferredSaveResponse: ...
    def PasteTasks(self, Inputs: list[PasteTaskContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

