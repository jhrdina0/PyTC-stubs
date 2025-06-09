import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GenericAttributesContainer:
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    KeyValueContainer: list[KeyValContainer]
    StringValueContainer: list[StringValContainer]

class KeyValContainer:
    def __init__(self, ) -> None: ...
    Key: int
    Value: str
    Type: int

class LoadProgramViewContainer:
    def __init__(self, ) -> None: ...
    Schedules: list[str]
    LoadProgramViewSets: list[LoadProgramViewSet]

class LoadProgramViewFilter:
    def __init__(self, ) -> None: ...
    Field: int
    Value: str
    Condition: int

class LoadProgramViewResponse:
    def __init__(self, ) -> None: ...
    Schedules: list[Teamcenter.Soa.Client.Model.Strong.Schedule]
    ScheduleTask: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    ResourceAssignment: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]
    TaskDependency: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    Calendar: list[Teamcenter.Soa.Client.Model.Strong.TCCalendar]
    CalendarEvent: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LoadProgramViewSet:
    def __init__(self, ) -> None: ...
    LoadProgramViewFilters: list[LoadProgramViewFilter]

class LoadResourceAssignmentContainer:
    def __init__(self, ) -> None: ...
    Resource: list[Teamcenter.Soa.Client.Model.ModelObject]
    SchedulesToAlwaysInclude: list[Teamcenter.Soa.Client.Model.Strong.Schedule]
    StartDate: System.DateTime
    EndDate: System.DateTime

class ResourceAssignmentLoadResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ResourceData: list[SingleAssignmentLoadResponse]

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

class SingleAssignmentLoadResponse:
    def __init__(self, ) -> None: ...
    Resource: Teamcenter.Soa.Client.Model.ModelObject
    ResourceAssignment: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]
    Schedules: list[Teamcenter.Soa.Client.Model.Strong.Schedule]
    Tasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    Calendars: list[Teamcenter.Soa.Client.Model.Strong.TCCalendar]
    CalendarEvents: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]

class StringValContainer:
    def __init__(self, ) -> None: ...
    Key: str
    Value: str
    Type: int

class ScheduleManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def LoadProgramView(self, LoadProgramViewContainer: LoadProgramViewContainer) -> LoadProgramViewResponse: ...
    def LoadResourceAssignments(self, LoadResourceAssignmentContainer: LoadResourceAssignmentContainer) -> ResourceAssignmentLoadResponse: ...
    def ModifySchedule(self, ScheduleModifyContainer: ScheduleModifyContainer) -> Teamcenter.Soa.Client.Model.ServiceData: ...

