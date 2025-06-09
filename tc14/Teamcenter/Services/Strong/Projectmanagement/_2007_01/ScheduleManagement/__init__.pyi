import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateBaselineContainer:
    """
    The information to create a baseline.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the baseline. If empty, uses the schedule ID of the baseline."""
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The Schedule to baseline."""
    ParentBaseline: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The Schedule baseline to copy from."""
    IsActive: bool
    """
            If true, then set the newly created baseline
            as the active baseline.
            """
    IncludeNewTasks: bool
    """If true, then baseline the newly created tasks."""
    UpdateScheduleBaselineCost: bool
    """
            If true, update the baselined Schedule
            cost. (Not currently used)
            """
    TaskRebaseOption: int
    """A bitmask of types of task to rebaseline (0=none, 1=non-started, 2=non-complete)."""

class CreateScheduleContainer:
    """
    The container for a new schedule.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name. Valid value- can not be null."""
    Description: str
    """The description. Valid value- can be empty string."""
    CustomerName: str
    """The customer's name. Valid value- can be empty string."""
    CustomerNumber: str
    """The customer's ID. Valid value- can be empty string."""
    StartDate: System.DateTime
    """The start date."""
    FinishDate: System.DateTime
    """The finish date."""
    Priority: int
    """The priority. Valid values are {0-lowest,1-low,2-MediumLow,3-Medium,4-High,5-VeryHigh,6-Highest}"""
    Status: str
    """The status. Valid values are { 0-Not started,1-InProgress,2-NeedsAttention,3-Complete,4-Abandoned,5-Late}"""
    Published: bool
    """isPubished?"""
    LinksAllowed: bool
    """areLinksAllowed?"""
    DatesLinked: bool
    """areDatesLinked?"""
    PercentLinked: bool
    """isPercentLinked?"""
    IsTemplate: bool
    """isTemplate?"""
    ScheduleType: int
    """The schedule type. Valid value (0-Standard)"""
    IsPublic: bool
    """isPublic?"""
    StringValueContainer: list[StringValContainer]
    """A collection of additional attributes.(optional)"""

class MembershipData:
    """
    The information needed to create a new member in a schedule.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule for the new membership."""
    Resource: Teamcenter.Soa.Client.Model.ModelObject
    """The resource to add.  (This can be a UserLogin, Group, or Discipline)."""
    MembershipLevel: int
    """The membership level in that schedule."""

class ScheduleCopyContainer:
    """
    The information need to copy a schedule.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the new schedule."""
    ScheduleToCopy: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The tag of the schedule to copy."""
    ResetWork: bool
    """
            Flag to indicate whether or not to reset the tasks' execution data (%, status,
            work complete, etc).
            """
    CopyBaselines: bool
    """Flag to indicate whether or not to copy baselines."""

class ScheduleDeliverableData:
    """
    A container for a new Schedule Deliverable.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule to contain this deliverable."""
    DeliverableType: str
    """The type of the deliverable."""
    DeliverableName: str
    """The name of the deliverable."""

class ScheduleObjDeleteContainer:
    """
    An object to delete.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """A tag to the object to be deleted."""

class StringValContainer:
    """
    
The container represents a single attribute's value.  The name of the attribute
is
represented by the key field.  The data type of the attribute is represented by
the
type field. The type field can be one of the following; char = 0; date = 1;
double
= 2; float = 3; int = 4; bool = 5; short = 6; string = 7; ModelObject = 8;
    """
    def __init__(self, ) -> None: ...
    Key: str
    """A string key identifying the attribute."""
    Value: str
    """A string representation of the value of the attribute."""
    Type: int
    """An integer to help determine the type of object represented by the value."""

class TaskDeliverableData:
    """
    The input information for a single task deliverable.
    """
    def __init__(self, ) -> None: ...
    ScheduleTask: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The task which will contain this delievable."""
    ScheduleDeliverable: Teamcenter.Soa.Client.Model.Strong.SchDeliverable
    """The ScheduleDeliverable to reference."""
    SubmitType: int
    """The submit type  (3=Don't submit, 0=submit as target, 1=submit as reference)."""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddMemberships(self, MembershipData: list[MembershipData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Add resources to the schedule with given membership levels.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param MembershipData: 
                         A collection of MembershipData structures to be added.
             
        :return: The references to the created membership objects, partial errors and failures are
             updated and returned through this object.
        """
        ...
    def CopySchedules(self, ScheduleCopyContainer: list[ScheduleCopyContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Makes a deep copy of the schedule with options to reset work and copy existing baselines.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleCopyContainer: 
                         A collection of ScheduleCopyContainer structures.
             
        :return: POMRefs to the new schedules, partial errors and failures are updated and returned
             through this object.
        """
        ...
    def CreateNewBaselines(self, CreateBaselineContainer: list[CreateBaselineContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates a new schedule baselines possibly based on a previous baseline.
             
             The created objects are returned back in the ServiceData
             of the response.The information required to create new baseline is passed as input
             parameter to the operation through CreateBaselineContainer
             data structure.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param CreateBaselineContainer: 
                         A collection of <font face="courier" height="10">CreateBaselineContainer</font> structures.
                         This structure contains the information to create new schedule baseline.
             
        :return: 
        """
        ...
    def CreateSchedule(self, NewSchedules: list[CreateScheduleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Create new scheduling object based on the initial user's request to the Application
             Interface.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param NewSchedules: 
                         A collection of CreateScheduleContainer structures.
             
        :return: The references to the updated object.
        """
        ...
    def CreateScheduleDeliverableTemplates(self, ScheduleDeliverableData: list[ScheduleDeliverableData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Creates new schedule deliverable templates and relates them to the schedule.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleDeliverableData: 
                         A collection of ScheduleDeliverableData structures.
             
        :return: The references to the created ScheduleDeliverable objects, partial errors and failures
             are updated and returned through this object.
        """
        ...
    def CreateTaskDeliverableTemplates(self, TaskDeliverableData: list[TaskDeliverableData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Creates new task deliverable templates and relates them to the task.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param TaskDeliverableData: 
                         A collection of TaskDeliverableData structures.
             
        :return: The references to the created TaskDeliverable objects, partial errors and failures
             are updated and returned through this object.
        """
        ...
    def DeleteSchedulingObjects(self, ScheduleObjDeleteContainer: list[ScheduleObjDeleteContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation is used to delete a scheduling object which cannot be deleted by deleteObjects operation. After the operation is
             called, the business logic determines whether to delete the scheduling objects by
             examining the schedule preservation rule, SM_PREVENT_DELETE_STATE. The SM_PREVENT_DELETE_STATE
             rule is optional and the system admin can remove the rule from the system or set
             its value to an empty list. But if the rule is in the system and set to any status
             or statuses then the value of the rule would be applied.
             
             The scheduling objects are Schedule, ScheduleTask, TaskDependency
             and ResourceAssignment.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleObjDeleteContainer: 
                         A collection of ScheduleObjDeleteContainer structures.
             
        :return: 
        """
        ...
    def BaselineTasks(self, ScheduleTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask], ScheduleBaseline: Teamcenter.Soa.Client.Model.Strong.Schedule) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation baselines or re-baselines a task's data in the context of an existing
             schedule baseline. The updated objects or added task baselines are returned back
             in the service data of the response. This operation throws a ServiceException in case of failure. The service exception will
             contain the error message of the failure. Additional errors will be returned in the
             list of partial errors in the ServiceData.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleTasks: 
                         A list of tasks to rebaseline.
             
        :param ScheduleBaseline: 
                         The schedule baseline to update.
             
        :return: 
        """
        ...

