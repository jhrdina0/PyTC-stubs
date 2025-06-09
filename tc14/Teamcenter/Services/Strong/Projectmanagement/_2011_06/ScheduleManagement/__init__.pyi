import System
import Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SchMgtOptions:
    """
    Schedule Management Options
    """
    def __init__(self, ) -> None: ...
    LogicalOptions: list[SchMgtLogicalOption]
    """Logical options"""
    IntegerOptions: list[SchMgtIntegerOption]
    """Integer Options"""
    StringOptions: list[SchMgtStringOption]
    """String Options"""

class LoadScheduleContainer:
    """
    Contain the schedule uids and options for loading schedules
    """
    def __init__(self, ) -> None: ...
    ScheduleUids: list[str]
    """The UIDs of the schedules."""
    SchmgtOptions: SchMgtOptions
    """
            The options for loading. Integer Option: "SM_Structure_Partial_Context" Values: 0
            =  load the full schedule including all sub schedules and their children . 1 =
            load only schedule summaries partially     Integer Option:  "SM_Structure_Load_Context"
            Values:  0 = loading schedule  1 = loading sub-schedule   4 = inserting sub schedule
            by reference Integer Option: "SM_Structure_Client_Context" Values: 0 = RAC client
            1 = Server client (for Synchronous dispatcher) 2 = MSP plugin client
            """

class LockRequest:
    """
    A request structure to lock the schedule.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule for which the lock request is"""
    RequestLock: bool
    """The request to lock (true) or unlock (false)"""

class LockResponse:
    """
    
A Response for SOA "ManageScheduleLocks". This will indicate whether the lock
request
is successful or not.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule locked or unlocked"""
    LockState: bool
    """The state of the lock (true=locked, false=not locked)"""
    RequestSuccess: bool
    """Was the request successful. True if the request was a success."""

class LockResponses:
    """
    List of multiple "LockResponses".
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""
    Responses: list[LockResponse]
    """The individual responses"""

class MasterMetaData:
    """
    A container for the SubMasterMetaData.
    """
    def __init__(self, ) -> None: ...
    Uid: str
    """The uid of a master schedule."""
    Start: System.DateTime
    """The Start Date of that master schedule."""
    Finish: System.DateTime
    """The Finish Date of that master schedule."""

class MultipleScheduleLoadResponses:
    """
    A container for load schedule responses
    """
    def __init__(self, ) -> None: ...
    ScheduleData: list[ScheduleLoadResponse]
    """Collection of the schedule load responses."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class ProxyTaskContainer:
    """
    Container for Proxy Task
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule were the proxy is being created"""
    Sublevels: int
    """
            Number of sublevels (if this should be mirrored in the sub schedules (-1 =  all,
            0 = only this schedule, 1= first level, 2 = 1st and 2nd level, etc)
            """
    TaskTag: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The real task being proxied."""
    RefTag: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The reference task in the schedule"""

class ProxyTaskResponse:
    """
    Response for createProxyTasks call.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule of the proxy task."""
    ProxyTask: Teamcenter.Soa.Client.Model.Strong.Fnd0ProxyTask
    """The proxy task"""
    SubScheduleAdditions: list[ProxyTaskResponse]
    """A collection containing a ProxyTaskResponse for each sub schedules addition"""

class ProxyTaskResponses:
    """
    A collection of ProxyTaskResponses returned for createProxyTasks call.
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""
    Responses: list[ProxyTaskResponse]
    """A collection of ProxyTaskResponse"""

class SchmgtClientCache:
    """
    The list of names lists.
    """
    def __init__(self, ) -> None: ...
    NamedStringLists: list[SchmgtNamedStringList]
    """Array of named string lists of components uid"""

class RefreshScheduleContainer:
    """
    Container for refreshing schedule
    """
    def __init__(self, ) -> None: ...
    MasterScheduleUid: str
    """The UID of the master schedule."""
    ComponentUid: str
    """The UID of the object to refresh"""
    RefreshOptions: SchMgtOptions
    """
            The options for refresh. Integer Option: "SM_Structure_Partial_Context" Values: 0
            =  load the full schedule including all sub schedules and their children . 1 =
            load only schedule summaries partially     Integer Option:  "SM_Structure_Load_Context"
            Values:  6 = refresh the schedule 7 = load all objects currently not in the client;
            compliment  Integer Option: "SM_Structure_Client_Context" Values: 0 = RAC client
            1 = Server client (for Synchronous dispatcher) 2 = MSP plugin client
            """
    ClientCache: SchmgtClientCache
    """List of currently loaded components for the object being refreshed."""
    LastModifiedDate: System.DateTime
    """The last modified date for the component represented by componentUID."""

class ScheduleCopyOptionsContainer:
    """
    Container for schedule copy options
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the new schedule"""
    Description: str
    """The description of the new schedule. Valid value -can be empty string."""
    Id: str
    """The ID of the new schedule."""
    RevId: str
    """The revId of the new schedule."""
    ScheduleToCopy: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The tag to the schedule to copy."""
    Options: SchMgtOptions
    """
            Copy schedule options 1) logical options  -{bool copyBaselines,bool loadOnResponse,bool
            resetWork,bool copyProxyTasks,bool  copycrossScheduleDependencies } 2) integerOptions
            -{ int ideepCopyCount } 3) stringOptions -{bool deepcopyrequired }
            """
    StringValueContainer: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.StringValContainer]
    """Additional attributes for the new schedule.(optional)"""
    TypedAttributesContainer: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.TypedAttributeContainer]
    """Additional  attributes for the new schedule.(optional)"""
    CopyInfo: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleDeepCopyinfo]
    """Additional metadata for the copy.(optional)"""

class SchMgtOptionsAsync:
    """
    SchMgtOptions for Async operation
    """
    def __init__(self, ) -> None: ...
    LogicalOptions: list[SchMgtLogicalOptionAsync]
    """Logical options"""
    IntegerOptions: list[SchMgtIntegerOptionAsync]
    """Integer Options"""
    StringOptions: list[SchMgtStringOptionAsync]
    """String Options"""

class ScheduleCopyOptionsContainerAsync:
    """
    ScheduleCopyOptionsContainer for copySchedule
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the new schedule"""
    Description: str
    """The description of the new schedule. Valid value -can be empty string."""
    Id: str
    """The ID of the new schedule."""
    RevId: str
    """The revId of the new schedule."""
    ScheduleToCopy: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The tag to the schedule to copy."""
    Options: SchMgtOptionsAsync
    """
            Copy schedule options 1) logical options  -{bool copyBaselines,bool loadOnResponse,bool
            resetWork,bool copyProxyTasks,bool  copycrossScheduleDependencies } 2) integerOptions
            -{ int ideepCopyCount } 3) stringOptions -{bool deepcopyrequired }
            """
    StringValueContainer: list[StringValContainerAsync]
    """Additional  attributes for the new schedule.(optional)"""
    TypedAttributesContainer: list[TypedAttributeContainerAsync]
    """Additional  attributes for the new schedule.(optional)"""
    CopyInfo: list[ScheduleDeepCopyinfoAsync]
    """
            This parameter specifies any additional metadata for the copy of the schedule. This
            ScheduleDeepCopyinfoAsync data structure
            holds the relevant information regarding applicable deep copy rules. This is optional
            parameter.
            """

class ScheduleDeepCopyinfoAsync:
    """
    ScheduleDeepCopyinfoAsync container
    """
    def __init__(self, ) -> None: ...
    ObjectComp: Teamcenter.Soa.Client.Model.ModelObject
    """A tag representing object on which the deep copy action need to be performed."""
    Relation: str
    """
            A string representing the name the relation  that need to be deep copied. Valid value
            can be IMANRelation.
            """
    ObjName: str
    """
            A string representing the new name for the new copy. of the object represented by
            otherSideObjectTag. The value for the newName will be null if the 'action' is not
            CopyAsObject or ReviseAndRelateToLatest.
            """
    OperationType: int
    """
            An integer representing the action to be performed on the object represented by 'otherSideObjectTag'.
            The values for action are: CopyAsObjectType = 0, CopyAsRefType = 1, DontCopyType
            =2, RelateToLatest = 3, ReviseAndRelateToLatest = 4
            """
    IsTargetPrimary: bool
    """
            A Boolean representing whether the given item revision is a primary object in the
            relation that need to be deep copied.
            """
    IsRequired: bool
    """
            A Boolean representing whether the deep information is from a mandatory deep copy
            rule configured by the administrator or not.
            """

class ScheduleLoadResponse:
    """
    Container for the load schedules response.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule"""
    ScheduleTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """All the tasks in this schedule."""
    ResourceAssignments: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]
    """All the resource assignments in this schedule."""
    TaskDependencies: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    """All the task dependencies in this schedule."""
    Calendars: list[Teamcenter.Soa.Client.Model.Strong.TCCalendar]
    """All the calendars referenced in this schedule."""
    CalendarEvents: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    """All the calendar events referenced in the calendars."""
    Submasterdata: list[SubMasterMetaData]
    """The metadata for master-schedules of this schedule and all sub-schedules."""
    NamedStringLists: list[SchmgtNamedStringList]
    """Currently used by refresh to return deleted objects to the client."""

class SchMgtIntegerOption:
    """
    Schedule Manager Integer Option
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the option"""
    Value: int
    """The value of the option"""

class SchMgtIntegerOptionAsync:
    """
    SchMgtIntegerOptions for Async operation
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the option"""
    Value: int
    """The value of the option"""

class SchMgtLogicalOption:
    """
    Schedule Manager Logical Option
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the option"""
    Value: bool
    """The value of the option (True or False)"""

class SchMgtLogicalOptionAsync:
    """
    SchMgtLogicalOptions for Async operation
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the option"""
    Value: bool
    """The value of the option (True or False)"""

class SchmgtNamedStringList:
    """
    A vector of lists.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """A unique identifier for this list (possibly UID)."""
    List: list[str]
    """The list of  UIDs contained by this object."""
    Aggregate: float
    """Not Used"""

class SchMgtStringOption:
    """
    Schedule Manager String Option
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the option"""
    Value: str
    """The value of the option."""

class SchMgtStringOptionAsync:
    """
    SchMgtStringOptions for Async operation
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the option"""
    Value: str
    """The value of the option."""

class StringValContainerAsync:
    """
    string value container for Async operation
    """
    def __init__(self, ) -> None: ...
    Key: str
    """A string key identifying the attribute."""
    Value: str
    """A string representation of the value of the attribute."""
    Type: int
    """
            An integer to help determine the data type of the attribute. Valid values- { 1=String_type,2=Integer_type,3=Long_type,4=Double_type,5=Float_type,6=Boolean_type,7=Date_type,8=Cal_type
            }
            """

class SubMasterMetaData:
    """
    A container for the sub-schedule master MetaData.
    """
    def __init__(self, ) -> None: ...
    Subschedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The tag of the sub schedule."""
    Masterdata: list[MasterMetaData]
    """Collection of metadata for all master schedules of this schedule and it's sub-schedules."""

class TaskExecUpdate:
    """
    
The structure which would be used to send back and forth the data for execution
view
for tasks.
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The task being updated."""
    UpdateAS: bool
    """Must be true when updating the Actual Start Date."""
    NewAS: System.DateTime
    """
            The new Actual Start Date to set (null is allowed). updateAS must also be to true
            to update this value.
            """
    UpdateAF: bool
    """Must be true when updating the Actual Finish Date."""
    NewAF: System.DateTime
    """
            The new Actual Finish Date to set (null is allowed). updateAF must also be to true
            to update this value.
            """
    NewPC: float
    """The new percent complete for the task (0-100) (-1 for no  update)"""
    NewStatus: str
    """
            The new status for the task. Valid values are the status strings listed in the status
            LOV. ("" or null for no update)
            """
    NewWC: int
    """The new work complete to set (-1 means no update)"""
    NewWR: int
    """The new work remaining to set (-1 means no update)"""

class TypedAttributeContainerAsync:
    """
    TypedAttributeContainerAsync conatiner for Async operation
    """
    def __init__(self, ) -> None: ...
    Type: str
    """The object type"""
    Attributes: list[StringValContainerAsync]
    """A collection of updates"""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CopySchedules(self, Containers: list[ScheduleCopyOptionsContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleCopyResponses:
        """    
             This operation makes a deep copy of the schedule with options to reset work and copy
             existing baselines.
             
             The following  are the options:  resetWork
             (false if not provided),
             
copyBaselines (false if not provided),
             
copyProxyTasks (false if not provided),
             
copyCrossScheduleDependencies (false if not
             provided )
             

             The information needed to copy the schedule is specified in the ScheduleCopyOptionsContainer structure. It returns ScheduleCopyResponses which will have information of copied  schedules
             and ServiceData. Errors will be returned
             in the list of partial errors in the ServiceData.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Containers: 

        :return: 
        """
        ...
    def CopySchedulesAsyncClient(self, SchToCopy: list[ScheduleCopyOptionsContainerAsync]) -> bool:
        """    
             This operation copies schedule asynchronously. The information required to copy the
             schedule asynchronously is passed as parameter to the operation as ScheduleCopyOptionsContainerAsync data structure.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param SchToCopy: 
                         A vector of <font face="courier" height="10">ScheduleCopyOptionsContainerAsync</font>
                         structures to copy schedule asynchronously.
             
        :return: 
        """
        ...
    def CreateProxyTasks(self, NewProxyTasks: list[ProxyTaskContainer]) -> ProxyTaskResponses:
        """    
             This operation creates proxy tasks. The information needed to create proxy tasks
             are specified in the ProxyTaskContainer structure.
             It returns ProxyTaskResponses which will
             have information of created proxy tasks and ServiceData.
             Errors will be returned in the list of partial errors in the ServiceData if operation fails to create proxy task.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param NewProxyTasks: 
                         Vector of <font face="courier" height="10">ProxyTaskContainer</font> structures to
                         create proxy Â Â Â Â tasks. This structure will contain all necessory
                         information to create new proxy task.
             
        :return: 
        """
        ...
    def LoadSchedules(self, LoadScheduleContainers: list[LoadScheduleContainer]) -> MultipleScheduleLoadResponses:
        """    
             The operation loads into memory all the objects belonging to a schedule. The objects
             are those needed to manage and validate the schedule. The objects are can be  instances
             of Schedule, ScheduleTask, ResourceAssignment, TaskDependency,
             TCCalendar TCCalendarEvents and SubMasterMetaData
             .
             
             This operation requires a load option which defines how it behaves, such as loading
             sections of a structured schedule on demand or loading the full schedule if system
             resources are available to accomplish request. The load option is defined by the
             preference "SM_Structure_Partial_Context" which can be set to one of the following
             values:
             
             1)    0 -> load all the schedule objects
             
             2)    1 -> load the schedule objects on demand.
             
             The default load option is 0 (load all objects).
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param LoadScheduleContainers: 
                         Containers for information required to load schedules. A container has the schedule
                         UID and load options.
             
        :return: 
        """
        ...
    def ManageScheduleLocks(self, Requests: list[LockRequest]) -> LockResponses:
        """    
             This is an operation that is used to manage concurrent access to schedule data. The
             server concurrent access capability allows schedule data to be accessed simultaneously
             from different sessions. To ensure data integrity, the server enforces a first-in-first-out
             execution logic by locking out access to the same data from other sessions until
             the lock is removed. During the lock period the session that owns the lock is allowed
             to add and update the schedule data. For deferred save or bulk update, the operation
             is used to purposely lock the schedule data until an unlock request is received.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Requests: 
                         The LockRequests
             
        :return: 
        """
        ...
    def RefreshScheduleObject(self, RefreshScheduleContainer: RefreshScheduleContainer) -> MultipleScheduleLoadResponses:
        """    
             The server allows concurrent access to a schedule data and because of this capability
             updates and additions can be added to the schedule data from other sessions apart
             from a client session. This operation loads all the objects in a schedule since the
             last modified date in the client session. The client can also specify the date from
             which to begin the load. The operation would then return all schedule objects that
             were modified from the specified date. It may also include objects modified in the
             client's session. The objects are Schedule, ScheduleTask, ResourceAssignment,
             TaskDependency, TCCalendar TCCalendarEvents and SubMasterMetaData.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param RefreshScheduleContainer: 
                         A container of schedule object, refresh operation options and last modified date
             
        :return: 
        """
        ...
    def UpdateTaskExecution(self, TaskUpdateExec: list[TaskExecUpdate]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Updates the execution data attributes of Schedule Tasks. The updates are specified
             through TaskExecUpdate  structures. actual
             start date, actual finish date, percent complete, status, work complete and work
             remaining attributes on schedule task can be updated through this operation.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param TaskUpdateExec: 
                         Vector of structures used to pass the new values to execution data attributes like
                         actual start date, actual finish date, percent complete, status, work complete and
                         work remaining.
             
        :return: 
        """
        ...
    def DeleteScheduleAsyncClient(self, SchToDelete: Teamcenter.Soa.Client.Model.Strong.Schedule) -> bool:
        """    
             Deletes the specified schedule asynchronously but will check that there is a connection
             between client and server before performing the delete action. After the check is
             performed successfully a call to deleteScheduleAsync
             operation is made to finalize the deletion of the schedule. See operation deleteScheduleAsync for more details.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param SchToDelete: 
                         The schedule to delete.
             
        :return: 
        """
        ...

