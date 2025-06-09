import System
import System.Collections
import Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2012_09.ScheduleManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AnalyticsMultipleResourceAssignmentStacks:
    """
    Reponse container for resource graph data request that contains one or more
resources.
    """
    def __init__(self, ) -> None: ...
    StacksVector: list[AnalyticsResourceAssignmentStacks]
    """Multiple resource stacks container."""

class AnalyticsResourceAssignmentDayStack:
    """
    Holds data for all the assigned tasks for the day.
    """
    def __init__(self, ) -> None: ...
    NumElements: int
    """Number of elements that makeup the stack for the day."""
    Stack: list[AnalyticsResourceAssignmentSingleTask]
    """Stack/pile of assigned tasks for the day."""

class AnalyticsResourceAssignmentSingleTask:
    """
    Information on single task assignment for the day.
    """
    def __init__(self, ) -> None: ...
    Day: System.DateTime
    """Date of assignments."""
    UserUid: str
    """Uid of the business object"""
    CalUid: str
    """Uid of user calendar"""
    SchUid: str
    """Uid of Schedule to which task assignment belongs."""
    SchTaskUid: str
    """The scheduleTask from which the assignment is assigned."""
    SchName: str
    """Name of the schedule"""
    SchStartDate: System.DateTime
    """Schedule start date"""
    SchEndDate: System.DateTime
    """Schedule end/finish date."""
    TaskName: str
    """Name of the scheduleTask from which the assignment was made."""
    TaskstartDate: System.DateTime
    """ScheduleTask start date."""
    TaskEndDate: System.DateTime
    """ScheduleTask end date."""
    TaskMinutes: float
    """Amount of work on the task."""
    ResourceMinutes: float
    """Day's work performed on the task."""
    StackBase: float
    """Where to place the next element in the day's stack of work."""
    TaskMinutesOverLoad: float
    """Amount of day's work over and above what the user's calendar indicates."""
    UserData: str
    """Descriiption of the data to provide tooltip information."""

class AnalyticsResourceAssignmentStacks:
    """
    Holds stack of tasks for each day and for all days between the start and finish
dates.
    """
    def __init__(self, ) -> None: ...
    UserName: str
    """Name of the reesource"""
    NumDays: int
    """
            Numebr of days between the start and finish range.The range represent when the graph
            starts and ends.
            """
    Stacks: list[AnalyticsResourceAssignmentDayStack]
    """Holds data for all the days that falls between start and finish dates."""

class CostDetailContainer:
    """
    The container that has the details of the cost attributes of schedule or task
    """
    def __init__(self, ) -> None: ...
    TotalEstimatedMinutes: int
    """
            The total estimated minutes of schedule or collection of selected schedule tasks
            or individual task
            """
    TotalAccruedMinutes: int
    """
            The total accrued minutes of schedule or collection of selected schedule tasks or
            individual task .
            """
    TotalEstimatedCost: float
    """The total estimated cost of schedule task"""
    TotalAccruedCost: float
    """The total estimated cost of schedule task"""
    BillCode: str
    """
            The bill code for task. Valid values are determined by the LOV. Valid values are
            {unassigned, General, Management, ProjectMgmt, Sales, Training, Travel, ProductDev,
            SoftwareDev}.
            """
    BillSubCode: str
    """
            The bill subcode for the task. Valid values are determined by the LOV. Valid value
            are following groups depending upon billcode.eg. If billcode is General then you
            can mentioned subcode as either of following set (unassigned, Billable, Billed, Standard,
            Unbillable}
            """
    BillingType: str
    """
            The billing type of the task. Valid values are determined by the LOV. Valid value
            are { unassigned, Billable, Billed, Standard, Unbillable}.
            """
    BillRate: Teamcenter.Soa.Client.Model.Strong.BillRate
    """
            The name of the bill rate associated with the task. Valid value can be empty string
            

"""
    Currency: str
    """The currency used in the cost for schedule or task."""
    Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The task which contains the total costs (sum of fixed costs and variable costs)"""
    Numchildren: int
    """the number of children associated with the summary tasks or schedule"""
    FixedCostData: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.FixedCostContainer]
    """Fixed cost container"""
    TaskCostDetails: list[CostDetailContainer]
    """the cost details of each sub-task"""

class CostDetailResponse:
    """
    The response of the get cost roll up data
    """
    def __init__(self, ) -> None: ...
    CostDetails: list[CostDetailContainer]
    """The response of the get cost roll up data"""
    CostServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data"""

class DetachScheduleContainer:
    """
    
DetachScheduleContainerÂ Â Â Â Contains the information of the schedule
being detached, the master schedule.
    """
    def __init__(self, ) -> None: ...
    SubSchedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule that is being detached from the master schedule."""
    MasterSchedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The master schedule from which the subSchedule is being detached."""

class EVMDataRequest:
    """
    Earned Value Data Request of schedule or task
    """
    def __init__(self, ) -> None: ...
    TaskVector: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """The tag of a task"""
    CalcBasisSelected: bool
    """
            To view the earned value data of schedule or task by cost , use the boolean value
            as false . To view the earned value data of schedule or task by duration , use the
            boolean value as true and the default option .
            """
    CalcWorkComplete: bool
    """
            To view the earned value data based on work complete of schedule's or tasks's percentage
            complete used, use the boolean value as true and the default option .To view the
            earned value data based on the work complete of schedule's task's actual hours used
            , use the boolean value as false .
            """
    SelectedLabel: bool
    """
            To view the earned value data based on the schedule's or task's earned value management
            labels , use the boolean value as true and the default option . To view the earned
            value data based on the schedule's or task's Cost/Schedule control systems criteria
            labels , use the boolean value as false.
            """

class EVMResultsContainer:
    """
    The container that contains the task's or schedule's earned value data.
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The tag of a task"""
    EvmResults: System.Collections.Hashtable
    """The evm results that holds the earned value calculations of schedule or task"""

class EVMResultsResponse:
    """
    The response that contains the evm results
    """
    def __init__(self, ) -> None: ...
    EvmData: EVMResultsContainer
    """The container that holds the earned value data of the schedule or task"""
    EvmServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""

class FailedObjectContainer:
    """
    
FailedObjectContainer will hold the Schedule Task and an error message of
            the operation that failed.
    """
    def __init__(self, ) -> None: ...
    Tasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """A vector of Schedule Tasks"""
    ErrorMsgs: list[str]
    """A vector of strings that have the error messages."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""

class InsertScheduleContainer:
    """
    
Contains the information of the schedule being inserted, the master schedule,
the
task in the master schedule below which the sub-schedule is inserted and the
Boolean
to adjust the master dates
    """
    def __init__(self, ) -> None: ...
    SubSchedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule that is being inserted in the master schedule."""
    MasterSchedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule in which the subSchedule is being inserted."""
    MasterScheduleTask: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The task in the master schedule below which the subSchedule is being inserted."""
    AdjustMasterDates: bool
    """
            Boolean value of true will allow the master start and/or end date to automatically
            adjust if the sub schedule start and/or finish date do not lie between the master
            dates.
            """

class LoadResourceGraphContainer:
    """
    A container representing the Query input for the resource load.
    """
    def __init__(self, ) -> None: ...
    Resources: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The user Tags."""
    StartDate: System.DateTime
    """An optional Start Date to filter with requires endDate."""
    EndDate: System.DateTime
    """An optional Finish Date to filter with requires startDate."""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreatePhaseGateTask(self, TaskInputContainer: Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.TaskCreateContainer) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer:
        """    
             This operation creates a phase gate structure inside a Schedule. A phase gate
             structure comprises of a phase task, two milestones, a gate task and a finish to
             start TaskDependency between the phase and the gate tasks. The operation takes
             the start date,  finish date, work estimate of the phase task as input and computes
             the start and finish dates of the milestones and the gate task. The name sent in
             the input will be used for the names of the phase and gate tasks with the string
             "Phase" and "Gate" appended.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param TaskInputContainer: 
<ul>
<li type="disc">name                    The name which is used for the phase and
                         gate tasks. The string "Phase"is appended to the name of the phase task and the string
                         "Gate" is appended to the name of the gate task.
                         </li>
<li type="disc">desc                      The description for the phase task
                         </li>
<li type="disc">objectType              A string representing the object type of
                         the phase and the gate tasks (typically "ScheduleTask").
                         </li>
<li type="disc">start                       The start date and time of the phase
                         task.
                         </li>
<li type="disc">finish                       The finish date and time of the phase
                         task.
                         </li>
<li type="disc">workEstimate            The work estimate in minutes of the phase
                         task.
                         </li>
<li type="disc">parent                     The <b>ScheduleTask</b> under which the
                         new phase task will be created.
                         </li>
<li type="disc">prevSibling                The <b>ScheduleTask</b> after which the
                         new phase task will be positioned after create.  If specified as null, the new phase
                         task will be positioned at the end of the <b>Schedule</b>.
                         </li>
<li type="disc">otherAttributes           List of other <b>ScheduleTask</b> properties
                         that can be optionally specified. Eg., Priority
                         </li>
<li type="disc">typedOtherAttributes   List of optional custom properties on the
                         <b>ScheduleTask</b>
</li>
</ul>

        :return: 
        """
        ...
    def DetachSchedule(self, DetachScheduleContainer: list[DetachScheduleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetEVMResults(self, InputEVMData: EVMDataRequest) -> EVMResultsResponse:
        """    
             The operation calculates the earned valued results for Schedule or ScheduleTask.
             The operation takes in input the Schedule or ScheduleTask  on which
             the earned value calculated data is sought and the criteria for the calculations.
             The earned value is calculated for the following labels -
             
             Planned Value (PV), Earned Value (EV), Actual Cost (AC) or Actual Cost of Work Performed,
             (ACWP) (Actual Effort), Cost Variance (CV), Budget at Completion (BAC), Forecast
             at Completion (FAC), Estimate at Completion (EAC), Schedule Variance (SV), Schedule
             Performance Index (SPI),Cost Performance Index (CPI)
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param InputEVMData: 
                         selectedLabel                    If true  the operation uses the earned value management
                         labels for the  earned value data of the <b>Schedule</b> or <b>ScheduleTask</b>.
                         If false the operation uses the the Cost Schedule Control Systems Criteria labels
                         for the earned value data of the <b>Schedule</b> or <b>ScheduleTask</b>. Default
                         value is true.
             
        :return: 
        """
        ...
    def GetResourceGraphData(self, LoadResourceGraphContainer: LoadResourceGraphContainer) -> AnalyticsMultipleResourceAssignmentStacks:
        """    
             The operation calculates the resource load information of one or more users assigned
             to ScheduleTask. The operation takes in a list of User objects as the
             input for whom the resource graph data is generated. You can specify the start date
             and end date to get the resource loading over the period of time specified by the
             start and end dates. The operation takes into account all the ScheduleTask
             objects in the system where the User is assigned to compute the resource load.
             

Use Cases:

             Create resource assignments histogram in Schedule Manager and Teamcenter Organization.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param LoadResourceGraphContainer: 

        :return: 
        """
        ...
    def InsertSchedule(self, InsertScheduleContainer: list[InsertScheduleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation inserts one or more Schedule specified in the input in a master
             Schedule.
             
             You can specify in the input an optional parameter which if true, the operation will
             adjust the master Schedule start date and end date to be the same as the sub
             Schedule start date and end date. By default, the operation does not adjust
             the dates of the master Schedule to be the same as the sub Schedule
             dates.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param InsertScheduleContainer: 
<b>adjustMasterDates</b>              If true the operation adjusts the start date
                         and the end date of the master <b>Schedule</b> to match the start date and the end
                         date of the sub <b>Schedule</b>. If false the operation  does not adjust the dates
                         of the master<b> Schedule</b>

        :return: 
        """
        ...
    def GetCostRollupData(self, CostDetailRequest: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]) -> CostDetailResponse:
        """    
             The operation calculates the total cost associated with either a Schedule
             or ScheduleTask. The total cost of a Schedule or ScheduleTask
             is calculated as below
             
             1) The total of the fixed costs specified on the Schedule or ScheduleTask

             2) The total of the costs of each ResourceAssignment based on the work hours
             and resource rate reported against the ScheduleTask.
             
             If there are any child ScheduleTask below the input ScheduleTask, the costs
             of the child ScheduleTask are accumulated into the costs of the parent ScheduleTask.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param CostDetailRequest: 

        :return: 
        """
        ...
    def ReplaceAssignment(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewAssignments: list[Teamcenter.Services.Strong.Projectmanagement._2012_09.ScheduleManagement.AssignmentCreateContainer], AssignmentDeletes: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer:
        """    
             This operation replaces a specified list of existing ResourceAssignment objects
             on a ScheduleTask with a specified list of new ResourceAssignment.
             The orginal ResourceAssignment specified in the input are deleted and new
             ResourceAssignment specified in the input are created on the ScheduleTask



Use Cases:

             In Schedule Manager, right click tasks and select Assignments->Replace Assignments.
             
             A dialogue will appear with current resources on the left hand side and the list
             of resources on the right hand side to replace the existing ones with. Select the
             resources on both the sides and click OK.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The <b>Schedule</b> containing the <b>ScheduleTask</b> whose assignments are to be
                         replaced.
             
        :param NewAssignments: 
                         assignedPercent      The resource loading of the <b>User</b> on the <b>ScheduleTask</b>

        :param AssignmentDeletes: 
                         List of ResourceAssignment objects which are to be deleted from a given <b>ScheduleTask</b>
                         in a <b>Schedule</b>.
             
        :return: 
        """
        ...
    def VerifySchedule(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule) -> FailedObjectContainer:
        """    
             This operation will verify the input Schedule for integrity of the scheduling
             data. The operation validates all the ScheduleTask, ResourceAssignment
             objects, TaskDependency, constraints in the Schedule for their effort
             driven scheduling values. It is recommended to use this operation to verify the integrity
             and data correctness of the Schedule before publishing the Schedule
             for execution.
             

Use Cases:



Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The <b>Schedule</b> whose integrity and correctness needs to be verified.
             
        :return: 
        """
        ...

