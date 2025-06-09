import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateResourceAssignmentContainer:
    def __init__(self, ) -> None: ...
    TaskID: str
    Resource: str
    Percentage: float
    Discipline: str
    StringValueContainer: list[StringValueContainer]

class CreateTaskContainer:
    def __init__(self, ) -> None: ...
    Id: str
    Name: str
    Description: str
    ParentTaskID: str
    PrevSiblingID: str
    Priority: int
    FixedType: int
    AutoComplete: bool
    TaskType: int
    Constraint: int
    StartDate: System.DateTime
    FinishDate: System.DateTime
    StartDateOffset: int
    FinishDateOffset: int
    WorkEstimate: int
    WorkComplete: int
    PercentComplete: float
    Duration: int
    StringValueContainer: list[StringValueContainer]

class CreateTaskDependencyContainer:
    def __init__(self, ) -> None: ...
    PredecessorTaskID: str
    SuccessorTaskID: str
    Type: int
    Lag: int
    StringValueContainer: list[StringValueContainer]

class KeyValueContainer:
    def __init__(self, ) -> None: ...
    Key: int
    Value: str
    Type: int

class MultipleScheduleLoadResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ScheduleData: list[ScheduleLoadResponse]

class UpdateContainer:
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    KeyValueContainer: list[KeyValueContainer]
    StringValueContainer: list[StringValueContainer]

class ScheduleChangeContainer:
    def __init__(self, ) -> None: ...
    ScheduleUpdates: UpdateContainer
    NewTasks: list[CreateTaskContainer]
    NewDependencies: list[CreateTaskDependencyContainer]
    NewAssignments: list[CreateResourceAssignmentContainer]
    TaskUpdates: list[UpdateContainer]
    DependencyUpdates: list[UpdateContainer]
    AssignmentUpdates: list[UpdateContainer]
    DeletedTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    DeletedDependencies: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    DeletedAssignments: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]

class ScheduleLoadResponse:
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    ScheduleTask: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    ResourceAssignment: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]
    TaskDependency: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    Calendar: list[Teamcenter.Soa.Client.Model.Strong.TCCalendar]
    CalendarEvent: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]

class StringValueContainer:
    def __init__(self, ) -> None: ...
    Key: str
    Value: str
    Type: int

class ScheduleManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def LoadSchedule(self, Schedule: list[str]) -> MultipleScheduleLoadResponse: ...
    def ModifySchedule(self, ScheduleChangeContainer: ScheduleChangeContainer) -> Teamcenter.Soa.Client.Model.ServiceData: ...

