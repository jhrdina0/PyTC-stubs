import System
import Teamcenter.Services.Internal.Strong.Projectmanagement._2007_06.ScheduleManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GenericAttributesContainer:
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    KeyValContainer: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2007_06.ScheduleManagement.KeyValContainer]
    StringValContainer: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2007_06.ScheduleManagement.StringValContainer]
    TypedAttributesContainer: list[TypedAttributesContainer]

class MasterMetaData:
    def __init__(self, ) -> None: ...
    Uid: str
    Start: System.DateTime
    Finish: System.DateTime

class MultipleScheduleLoadResponses:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ScheduleData: list[ScheduleLoadResponse]

class ScheduleLoadResponse:
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    ScheduleTask: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    ResourceAssignment: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]
    TaskDependency: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    Calendar: list[Teamcenter.Soa.Client.Model.Strong.TCCalendar]
    CalendarEvent: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    Submasterdata: list[SubMasterMetaData]

class ScheduleModifyContainer:
    def __init__(self, ) -> None: ...
    ScheduleUpdates: GenericAttributesContainer
    DeleteAllTasks: bool
    NewTasks: list[GenericAttributesContainer]
    NewDependencies: list[GenericAttributesContainer]
    NewAssignments: list[GenericAttributesContainer]
    TaskUpdates: list[GenericAttributesContainer]
    DependencyUpdates: list[GenericAttributesContainer]
    AssignmentUpdates: list[GenericAttributesContainer]
    DeletedTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    DeletedDependencies: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    DeletedAssignments: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]

class ScheduleModifyResponse:
    def __init__(self, ) -> None: ...
    NewTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    NewDependencies: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    NewAssignments: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]

class ScheduleModifyResponses:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Responses: list[ScheduleModifyResponse]

class SubMasterMetaData:
    def __init__(self, ) -> None: ...
    Subschedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    Masterdata: list[MasterMetaData]

class TypedAttributesContainer:
    def __init__(self, ) -> None: ...
    Type: str
    Attributes: list[Teamcenter.Services.Internal.Strong.Projectmanagement._2007_06.ScheduleManagement.StringValContainer]

class ScheduleManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def LoadSchedules(self, Schedule: list[str]) -> MultipleScheduleLoadResponses: ...
    def ModifySchedule(self, ScheduleModifyContainers: list[ScheduleModifyContainer]) -> ScheduleModifyResponses: ...
    def GetSchedulesToinsert(self, MasterSchedule: Teamcenter.Soa.Client.Model.Strong.Schedule) -> Teamcenter.Soa.Client.Model.ServiceData: ...

