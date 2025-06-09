import System
import Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssignmentCreateContainer:
    """
    The information needed to create a new assignment to a task.
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The task to assign the resource."""
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The user being assigned (or null if discipline assignment)."""
    Discipline: Teamcenter.Soa.Client.Model.Strong.Discipline
    """The discipline of the assignee or the discipline for the assignment."""
    AssignedPercent: float
    """The percentage effort being assigned (I.E. 50.0 == 50%)"""

class AssignmentUpdateContainer:
    """
    Container for assignment updates.
    """
    def __init__(self, ) -> None: ...
    Assignment: Teamcenter.Soa.Client.Model.Strong.ResourceAssignment
    """The assignment to update"""
    NewEffort: float
    """The new % effort of that assignee."""

class AttributeUpdateContainer:
    """
    Holds the name and value of an attribute.
    """
    def __init__(self, ) -> None: ...
    AttrName: str
    """The name of the attribute."""
    AttrValue: str
    """The value of the attribute."""
    AttrType: int
    """
            An integer to help determine the data type of the attribute. Valid values- { 1=String_type,2=Integer_type,3=Long_type,4=Double_type,5=Float_type,6=Boolean_type,7=Date_type,8=Cal_type
            }
            """

class CreatedDependenciesContainer:
    """
    New  dependencies container
    """
    def __init__(self, ) -> None: ...
    CreatedDependencies: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    """The dependencies created"""
    CreatedProxyTasks: list[Teamcenter.Soa.Client.Model.Strong.Fnd0ProxyTask]
    """The created proxy tasks"""
    UpdatedTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """The tasks which were updated due to"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The SOA service data"""

class CreatedObjectsContainer:
    """
    The container of created objects
    """
    def __init__(self, ) -> None: ...
    CreatedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """The objects which were created."""
    UpdatedTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """The tasks affected by the creation."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class CriticalTasksContainer:
    """
    The tasks on the critical path.
    """
    def __init__(self, ) -> None: ...
    Tasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """The tasks on the critical path."""
    ProxyTasks: list[Teamcenter.Soa.Client.Model.Strong.Fnd0ProxyTask]
    """The proxy tasks on the critical path."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class DeleteTaskContainer:
    """
    Information about the deleted tasks.
    """
    def __init__(self, ) -> None: ...
    Orphaned: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """Tasks which were orphaned(as they could not be deleted)."""
    Updated: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """Tasks updated due to the delete."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class DependencyCreateContainer:
    """
    
Creates Dependencies between tasks in the same schedule, between a task and a
proxy
task in the same schedule, or between a tasks in different schedules (but in the
same master schedule).  It returns the created dependencies, created proxy tasks
(if any), and the objects affected by this change
    """
    def __init__(self, ) -> None: ...
    PredTask: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The predecessor task for the dependency."""
    SuccTask: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The successor task for the dependency."""
    DepType: int
    """The type of dependency: 0-FS, 1-FF, 2-SS, 3-SF"""
    LagTime: int
    """The lag time in minutes (480 ~ 1 day)"""

class DependencyUpdateContainer:
    """
    Update dependency container
    """
    def __init__(self, ) -> None: ...
    Dependency: Teamcenter.Soa.Client.Model.Strong.TaskDependency
    """The dependency to update."""
    NewType: int
    """The new type for the dependency."""
    NewLag: int
    """The new lag for the dependnecy."""

class LaunchedWorkflowContainer:
    """
    Information about the launched workflows.
    """
    def __init__(self, ) -> None: ...
    LaunchedWorkflows: list[Teamcenter.Soa.Client.Model.Strong.EPMJob]
    """The launched workflow processes."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class MoveRequest:
    """
    The information required to move a task.
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The task or proxy task to move."""
    NewParent: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The new parent for the task."""
    PrevSibling: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The new previous sibling for the task (or the reference task in the case of a proxy)."""

class ObjectUpdateContainer:
    """
    Information to update an object.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The object being updated."""
    Updates: list[AttributeUpdateContainer]
    """The updates to the main type."""
    TypedUpdates: list[TypedAttributeUpdateContainer]
    """Updates for a custom type."""

class TaskCreateContainer:
    """
    The information needed to create a task.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name."""
    Desc: str
    """The description."""
    ObjectType: str
    """The type to create (typically "ScheduleTask")."""
    Start: System.DateTime
    """The start date and time."""
    Finish: System.DateTime
    """The finish date and time."""
    WorkEstimate: int
    """The work estimate in minutes."""
    Parent: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The summary task to create the new task under."""
    PrevSibling: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """
            The task to create this new task after.  Must currently exist under the parent.
            Can be null.
            """
    OtherAttributes: list[AttributeUpdateContainer]
    """Additional optional attributes: priority"""
    TypedOtherAttributes: list[TypedAttributeUpdateContainer]
    """Other attributes required to create the objectType specified."""

class TypedAttributeUpdateContainer:
    """
    Updates for a certain type of object.
    """
    def __init__(self, ) -> None: ...
    ObjectType: str
    """The object type containing the attributes."""
    Updates: list[AttributeUpdateContainer]
    """The list of attributes and their values."""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateSchedules(self, ScheduleUpdates: list[ObjectUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Updates all the affected scheduling objects based on the initial users request to
             the application interface.  Properties on the Schedule object like object
             name, description, start date, finish date, status, is schedule template, wbsformat,
             customer name, customer number , published, is public and priority etc can be
             updated with  this operation.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleUpdates: 
                         The schedules to update and the updates to make. Vector of <font face="courier" height="10">ObjectUpdateContainer</font>
                         structures. Each Â Â Â Â <font face="courier" height="10">ObjectUpdateContainer</font>
                         structure holds a scheduleÂ Â Â Â object,   <font face="courier" height="10">AttributeUpdateContainer</font> structure andÂ Â Â Â <font face="courier" height="10">TypedAttributeUpdateContainer</font> structure. Each <font face="courier" height="10">AttributeUpdateContainer</font> structure holds Â Â Â Â attribute
                         name, value and type.
             
        :return: 
        """
        ...
    def AssignResources(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateAssignments: list[AssignmentCreateContainer]) -> CreatedObjectsContainer:
        """    
             This operation assigns resources (Users and Disciplines) to tasks in
             a given schedule. The operation returns the CreatedObjectsContainer
             which will have information of created assignments, updated tasks and service data.The
             operation throws a ServiceException in case
             of failure. The service exception will contain the error message of the failure.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule containing the tasks to be assigned.
             
        :param CreateAssignments: 

        :return: It returns the created assignments as well as objects affected by the change.
        """
        ...
    def CreateDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDependencies: list[DependencyCreateContainer]) -> CreatedDependenciesContainer:
        """    
             Creates Dependencies between tasks in the
             same schedule, between a task and a proxy task in the same schedule, or between a
             tasks in different schedules (but in the same master schedule).  It returns the created
             dependencies, created proxy tasks (if any), and the objects affected by this change.
             This operation throws a ServiceException
             in case of failure. The service exception will contain the error message of the failure.
             Additional errors will be returned in the list of partial errors in the ServiceData.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule containing both the predecessor and successor tasks
             
        :param NewDependencies: 

        :return: 
        """
        ...
    def CreateTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateContainers: list[TaskCreateContainer]) -> CreatedObjectsContainer:
        """    
             Creates the specified tasks in a given schedule. The information needed to create
             task are specified in the TaskCreateContainer
             structure. It returns CreatedObjectsContainer
             which will have information of created tasks, updated tasks and ServiceData. Throws a ServiceException
             in case of failure. The service exception will contain the error message of the failure.
             Additional errors will be returned in the list of partial errors in the ServiceData.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule in which to create the tasks.
             
        :param CreateContainers: 

        :return: 
        """
        ...
    def DeleteAssignments(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, AssignmentDeletes: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes resource assignments from the tasks in the given schedule.
             It takes schedule from which assignments is to be deleted and array of resource assignments
             to be deleted as input.
             
             The deleted resource assignment objects are returned in the deletedObjects of the ServiceData.
             Operation throws a ServiceException in case
             of failure. The service exception will contain the error message of the failure.
             Additional errors will be returned in the list of partial errors in the ServiceData.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule containing the assignments to be deleted.
             
        :param AssignmentDeletes: 
                         Vector of <b>ResourceAssignment</b>. Each object in the vector represents a <b>ResourceAssignment</b>
                         type object which is to be deleted from a given schedule (required input)
             
        :return: 
        """
        ...
    def DeleteDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, DependencyDeletes: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the dependencies between the tasks in a given Schedule.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule containing the assignments to be deleted.
             
        :param DependencyDeletes: 
                         The dependencies to be deleted.
             
        :return: 
        """
        ...
    def DeleteTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, DeleteTasks: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> DeleteTaskContainer:
        """    
             Deletes the requested tasks along with the sub tasks, assignments, dependencies,
             and task deliverables.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule containing the tasks to delete.
             
        :param DeleteTasks: 
                         The tasks or proxy tasks to be deleted.
             
        :return: 
        """
        ...
    def FindCriticalPathTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule) -> CriticalTasksContainer:
        """    
             This operation finds and returns the tasks on the critical path of the schedule.
             The critical path is the task or tasks that would likely affect the last task in
             the schedule if they were completed late. The critical path is calculated by determining
             the last task in the project (time wise). Any task where a slip would delay the last
             task in the project is on the critical path. Tasks linked by dependencies have a
             longer critical path (chain of tasks). The tasks on the critical path with the longest
             sequence of dependent tasks merit the most attention to on-time completion in order
             to avoid delays.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule where the critical path is being calculated.
             
        :return: 
        """
        ...
    def LaunchScheduledWorkflow(self, Tasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]) -> LaunchedWorkflowContainer:
        """    
             A Teamcenter schedule  task can be configured in such a way that when certain
             conditions are
             
             met the associated workflow can be initiated. The triggering rules or conditions
             
             create a workflow process. If there are updates to the workflow process tasks, a
             
             notification is sent to the Teamcenter schedule task so that the schedule
             task can be
             
             updated. This operation launches workflows associated with the tasks .
             



Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Tasks: 
                         The tasks associated with the workflows to launch.
             
        :return: 
        """
        ...
    def MoveTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, MoveRequests: list[MoveRequest]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Allow schedule tasks and proxy tasks to be moved to a different location in the task
             hierarchy.
             
             The schedule task move requests are specified in the MoveRequest
             structure, which store information about schedule task object, its new parent and
             its new previous sibling. Additional errors during this operation will be returned
             in the list of partial errors in the ServiceData.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule containing the tasks to move.
             
        :param MoveRequests: 

        :return: 
        """
        ...
    def RecalculateScheduleNonInteractive(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, RecalcType: int, RunAsync: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation performs the revalidation/rerunning of the business logic on the properties
             of the schedule and its child objects based on the requested properties flag or ALL.
             Interactive use of this operation is not recommended.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule to be recalculated.
             
        :param RecalcType: 
                         The recalculation type:<font face="courier" height="10"> 0-All, 1-Execution Data,
                         2-Scheduling Data</font>

        :param RunAsync: 
                         Schedule a <b>DispatcherServices</b> job for the recalcuation? <font face="courier" height="10">TRUE</font>-schedule a job and return.  <font face="courier" height="10">FALSE</font>-run
                         full recalculation and return.
             
        :return: 
        """
        ...
    def ScaleScheduleNonInteractive(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, ScaleFactor: float, Options: Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.SchMgtOptions) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The scale schedule operation allows for the user to scale the schedule based on specified
             lag time.
             
             This operation throws a ServiceException
             in case of failure. The service exception will contain the error message of the failure.
             Additional errors will be returned in the list of partial errors in the ServiceData.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule to scale.
             
        :param ScaleFactor: 
                         The scaling factor.
             
        :param Options: 
                         The scaling options: <font face="courier" height="10">scaleType-integer (1-scale
                         work(default), 2-scale duration), checkState-boolean (true-check task state(default),
                         false-ignore state)</font>

        :return: 
        """
        ...
    def ShiftScheduleNonInteractive(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDate: System.DateTime, NewFinish: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Shifts the schedule forward or backwards to the new provided start/finish date.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule to shift.
             
        :param NewDate: 
                         The new date/time to shift to.
             
        :param NewFinish: 
                         Is the <font face="courier" height="10">newDate</font> a new finish date?  <font face="courier" height="10">True</font> if it is a new finish date.  <font face="courier" height="10">False</font> if it is a new start date.
             
        :return: 
        """
        ...
    def UpdateAssignments(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, AssignmentUpdates: list[AssignmentUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation updates the resource assignments in a given schedule. Only the resource
             load of the assignment can be updated with this operation. It returns the ServiceData which will have information of updated assignment
             objects. This operation throws a ServiceException
             in case of failure. The service exception will contain the error message of the failure.
             Additional errors will be returned in the list of partial errors in the ServiceData.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule in which the assignments are to be updated (Required input).
             
        :param AssignmentUpdates: 
                         Vector of <font face="courier" height="10">AssignmentUpdateContainer</font> structures.
                         Each <font face="courier" height="10">AssignmentUpdateContainer</font> structure
                         holds the assignment which is to be updated along with resource load of the assignment
                         to be updated (required input).
             
        :return: 
        """
        ...
    def UpdateDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, DependencyUpdates: list[DependencyUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation  updates the dependencies in a given schedule. It takes an array of
             DependencyUpdateContainer objects in which
             the type of the dependency,  and lag time updates can be specified per dependency
             object.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule containing the dependencies to be updated.
             
        :param DependencyUpdates: 
                         The dependencies to update.
             
        :return: 
        """
        ...
    def UpdateTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, Updates: list[ObjectUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Updates the specified tasks in a given schedule. Task updates are specified in the
             ObjectUpdateContainer  structure. All the
             scheduling data properties and execution data properties on the schedule task can
             be updated. Updates on the summary tasks are not allowed. This operation supports
             updating the custom attributes of OOTB schedule tasks  as well as custom schedule
             tasks. The updated objects are returned back in the service data of the response.
             This operation throws a ServiceException
             in case of failure. The service exception will contain the error message of the failure.
             Additional errors will be returned in the list of partial errors in the ServiceData.
             



Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule containing the tasks to be updated.
             
        :param Updates: 

        :return: 
        """
        ...

