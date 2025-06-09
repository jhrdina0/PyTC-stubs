import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddMembershipResponse:
    """
    The response when schedule members are added.
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""
    AddedMembers: list[Teamcenter.Soa.Client.Model.Strong.ScheduleMember]
    """The added members."""

class BillRateContainer:
    """
    The container for a BillRate.
    """
    def __init__(self, ) -> None: ...
    Type: int
    """The type: (0-Multiplier, 1-Custom Rate)."""
    Name: str
    """The name of the bill rate."""
    Rate: str
    """The new hourly rate or multiplier in the format *n.nnn (15.3  max)."""
    Currency: str
    """The ISO 4217 currency rate."""

class CreateBillRateResponse:
    """
    The response when BillRates are created.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""
    Rates: list[Teamcenter.Soa.Client.Model.Strong.BillRate]
    """The added BillRates."""

class CreateScheduleResponse:
    """
    The response when new Schedule is created
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData"""
    Schedules: list[Teamcenter.Soa.Client.Model.Strong.Schedule]
    """The created Schedules"""

class FixedCostContainer:
    """
    The information need to create/update a Fixed Cost.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of fixed cost."""
    Estimate: str
    """The estimated cost. Valid value can be empty string"""
    Actual: str
    """The actual cost. Valid value can be empty string."""
    Currency: str
    """ISO-4217 code for currency of the costs."""
    UseActual: bool
    """Should accrual calculations use the "actual" cost?"""
    BillCode: str
    """
            The billing code. Valid values are determined by the LOV  {unassigned, General, Management,
            ProjectMgmt, Sales, Training, Travel, ProductDev, SoftwareDev}
            """
    SubCode: str
    """
            The billing subcode. Valid values are determined by the LOV. Values are following
            groups depending upon billcode.eg. If billcode is General then you can mentioned
            subcode as either of following set (unassigned, Accounting, Clerical, CorpAdmin,
            IT, Meetings, Other)                                             Following are the
            list of billcode and corresponsing valid values for sub code.  For BillCode 'unassigned'
            = { unassigned } For BillCode 'General' ={ unassigned, Accounting, Clerical, CorpAdmin,
            IT, Meetings, Other }, For Bill code Management = { unassigned, Executive, ProjMgmt,
            Design/Plan, Meetings, Training, Other} For BillCode 'ProiectMgmt' ={ unassigned,
            Management, Meetings, Design/Plan, Training, Teaching, Clerical, Email, Other } For
            BillCode 'Sales' ={ unassigned, MajorAccts, General, Admin, Training, Other } For
            BillCode 'Training' ={ unassigned, Billable, Customer1, Customer2, Customer3, Region1,
            Region2, Region3, Other } For BillCode 'Travel' ={ unassigned, Billable, Region1,
            Region2, Region3, Other } For BillCode 'ProductDev' ={ unassigned, Planning, Design,
            Development, ProcessMgt, Validation, Other } For BillCode 'SoftwareDev' ={unassigned,
            Concept, Defination, Development, Introduction, Training, Other }
            """
    BillingType: str
    """The billing type. Valid value are { unassigned, Billable, Billed, Standard, Unbillable}"""
    AccrualType: int
    """The cost accrual type (0=start, 1=prorated, 2=end)."""
    FixedCost: Teamcenter.Soa.Client.Model.Strong.SchedulingFixedCost
    """A reference to the cost being updated (or null when newCost)."""

class MembershipData:
    """
    The information needed to create a new member in a schedule.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule for the new membership. Valid value- tag of the schedule."""
    Resource: Teamcenter.Soa.Client.Model.ModelObject
    """
            The resource to add.  (This can be a User, Group, or Discipline).valid value- tag
            of the resource
            """
    MembershipLevel: int
    """The membership level in that schedule. Valid values are-{0-observer,1-participant,2-coordinator}"""
    Cost: str
    """The cost value (n.nnn (15.3 max))"""
    Currency: str
    """The ISO-4217 currency code."""

class NewScheduleContainer:
    """
    The container for a new schedule.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name. Valid value can not be null"""
    Description: str
    """The description. Valid value can be empty string"""
    Id: str
    """id. Valid value can not be null"""
    RevID: str
    """revID. Valid value can not be null"""
    CustomerName: str
    """The customer's name. Valid value can be empty string"""
    CustomerNumber: str
    """The customer's ID. Valid value can be empty string"""
    StartDate: System.DateTime
    """The start Date. Valid value can not be null"""
    FinishDate: System.DateTime
    """The finishDate. Valid value can not be null"""
    Priority: int
    """The priority. Valid values are {0-lowest,1-low,2-MediumLow,3-Medium,4-High,5-VeryHigh,6-Highest}"""
    Status: int
    """The status. Valid values are  {0-Not started,1-In Progress,2-Needs Attention,3-Complete,4-Abandoned,5-Late}"""
    TaskFixedType: int
    """Task fixed type. Valid values - FIXED_WORK = 0, FIXED_DURATION = 1, FIXED_RESOURCES=2"""
    Published: bool
    """Indicates whether the schedule is published. Valid values - true or false"""
    NotificationsEnabled: bool
    """
            notificationsEnabled. Indicates whether notifications should be enabled. Valid values
            - true or false
            """
    PercentLinked: bool
    """
            isPercentLinked? Indicates whether percentage complete should be linked to work complete.
            Valid values - true, false
            """
    IsTemplate: bool
    """isTemplate? Indicates whether the schedule is a template. Valid values - true, false"""
    IsPublic: bool
    """Indicates whether the schedule is public. Valid values - true, false""""
    Type: str
    """
            type. This is the object_type of the schedule being created. It could be "Schedule"
            or any of the custom types created by the customer.
            """
    BillCode: str
    """The billCode. Valid value can be empty string"""
    BillSubCode: str
    """The bill sub code. Valid value can be empty string"""
    BillType: str
    """The bill type. Valid value can be empty string"""
    BillRate: Teamcenter.Soa.Client.Model.ModelObject
    """The bill rate. Valid value can be NULLTAG"""
    StringValueContainer: list[StringValContainer]
    """A collection of additional attributes (Optional)"""
    TypedAttributesContainer: list[TypedAttributeContainer]
    """typedAttributesContainer. A container with type attribute -(optional)"""

class ScheduleCopyOptionsContainer:
    """
    The input information necessary to copy a schedule.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """
            The name of the new Schedule to be created.The name cannot be NULL

"""
    Description: str
    """The description text for the new Schedule to be created."""
    Id: str
    """The id of the new Schedule to be created. The id value cannot be NULL."""
    RevId: str
    """
            The revID of the new ScheduleRevision
            that will be created along with the new schedule.
            
            The revID value cannot be NULL.
            
"""
    ScheduleToCopy: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The tag to the schedule to copy."""
    ResetWork: bool
    """
            This is the flag to indicate whether or not to reset the tasks' execution data (%,
            status, work complete, etc)
            """
    CopyBaselines: bool
    """Flag to indicate whether or not to copy baselines."""
    LoadOnResponse: bool
    """Flag to indicate whether or not to load the schedule in the response."""
    IDeepCopyCount: int
    """This parameter stores the number of deep copied objects."""
    StringValueContainer: list[StringValContainer]
    """
            This parameter is  to collect additional attributes for the new schedule. The container
            represents a single attribute's value.
            """
    TypedAttributesContainer: list[TypedAttributeContainer]
    """
            This parameter specifies  any additional attribute values to be set on the newly
            created Schedule,scheduleRevision.
            """
    Copyinfo: list[ScheduleDeepCopyinfo]
    """
            This parameter specifies any additional metadata for the copy of the schedule. This
            DeepCopyData data structure holds the relevant
            information regarding applicable deep copy rules.
            """

class ScheduleCopyResponse:
    """
    
The response from a schedule copy call.  It includes all the data necessary to
load
that schedule.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule."""
    ScheduleTask: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """The schedule tasks."""
    ResourceAssignment: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]
    """The task assignments."""
    TaskDependency: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    """The task dependencies."""
    Calendar: list[Teamcenter.Soa.Client.Model.Strong.TCCalendar]
    """The calendars asssociated with the schedule and its members."""
    CalendarEvent: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    """The calendar events associated with the calendars."""

class ScheduleCopyResponses:
    """
    Container to hold multiple ScheduleCopyResponse objects.
    """
    def __init__(self, ) -> None: ...
    ScheduleResponse: list[ScheduleCopyResponse]
    """A collection of ScheduleCopyResponses."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class ScheduleDeepCopyinfo:
    """
    
The DeepCopyData data structure holds the relevant information regarding
applicable
deep copy rules.
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
    DeliverableReference: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """A reference to the deliverable.(optional)"""

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
    """
            An integer to help determine the data type of the attribute. Valid values- { 1=String_type,2=Integer_type,3=Long_type,4=Double_type,5=Float_type,6=Boolean_type,7=Date_type,8=Cal_type
            }
            """

class TaskCostUpdate:
    """
    The request container for fixed cost and costing meta data updates.
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The task which contains or will contain the fixed costs."""
    NewCosts: list[FixedCostContainer]
    """The information needed to create new fixed costs."""
    UpdatedCosts: list[FixedCostContainer]
    """The information needed to update existing fixed costs."""
    DeletedCosts: list[Teamcenter.Soa.Client.Model.Strong.SchedulingFixedCost]
    """A list of fixed costs to delete."""
    BillCode: str
    """
            The bill code for the task. Valid values are determined by the LOV. Valid values
            are {unassigned, General, Management, ProjectMgmt, Sales, Training, Travel, ProductDev,
            SoftwareDev}
            """
    SubCode: str
    """
            The bill subcode for the task. Valid values are determined by the LOV. Valid value
            are following groups depending upon billcode.eg. If billcode is General then you
            can mentioned subcode as either of following set (unassigned, Accounting, Clerical,
            CorpAdmin, IT, Meetings, Other)                    Following are the list of billcode
            and corresponsing valid values for sub code. For BillCode 'unassigned' = { unassigned
            } For BillCode 'General' ={ unassigned, Accounting, Clerical, CorpAdmin, IT, Meetings,
            Other }, For Bill code Management = { unassigned, Executive, ProjMgmt, Design/Plan,
            Meetings, Training, Other} For BillCode 'ProiectMgmt' ={ unassigned, Management,
            Meetings, Design/Plan, Training, Teaching, Clerical, Email, Other } For BillCode
            'Sales' ={ unassigned, MajorAccts, General, Admin, Training, Other } For BillCode
            'Training' ={ unassigned, Billable, Customer1, Customer2, Customer3, Region1, Region2,
            Region3, Other } For BillCode 'Travel' ={ unassigned, Billable, Region1, Region2,
            Region3, Other }                                       For BillCode 'ProductDev'
            ={ unassigned, Planning, Design, Development, ProcessMgt, Validation,Other}
            For BillCode 'SoftwareDev' ={unassigned,
            Concept, Defination, Development, Introduction, Training, Other }
            """
    BillingType: str
    """
            The billing type of the task. Valid values are determined by the LOV. Valid value
            are { unassigned, Billable, Billed, Standard, Unbillable}
            """
    BillRate: str
    """The name of the bill rate associated with the task. Valid value can be empty string"""
    Rate: Teamcenter.Soa.Client.Model.Strong.BillRate
    """A tag to the bill rate to associate with this task. Valid value can be NULLTAG"""

class TaskCostUpdateResponse:
    """
    The response container for fixed cost update.
    """
    def __init__(self, ) -> None: ...
    UpdatedTask: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The updated task."""
    NewCosts: list[Teamcenter.Soa.Client.Model.Strong.SchedulingFixedCost]
    """The list of new fixed costs."""

class TypedAttributeContainer:
    """
    A container which is used to update custom properties.
    """
    def __init__(self, ) -> None: ...
    Type: str
    """The object type. Valid values are {  ScheduleType,ScheduleRevisionType,ScheduleTaskType,ScheduleTaskRevisionType}"""
    Attributes: list[StringValContainer]
    """A collection of updates.(optional)"""

class UpdateTaskCostDataResponse:
    """
    The response to the cost update.
    """
    def __init__(self, ) -> None: ...
    Responses: list[TaskCostUpdateResponse]
    """The collection of individual task cost changes."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddMemberships(self, MembershipData: list[MembershipData]) -> AddMembershipResponse:
        """    
             This operation adds resources to the schedule with given membership levels.
             

             The information required to add  new resource  to the schedule is passed to the function
             through MembershipData structure.
             

             The operation saves the references to the newly created membership objects and errors
             if any in the ServiceData of the MembershipDataResponse data structure.
             

             When a resource that needs to be added doesnot exist,the operation returns and  the
             error is saved in the ServiceData of the
             response.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param MembershipData: 

        :return: 
        """
        ...
    def CopySchedules(self, ScheduleCopyContainer: list[ScheduleCopyOptionsContainer]) -> ScheduleCopyResponses:
        """    
             This operation makes a deep copy of the schedule with options to reset work and copy
             existing baselines. The information needed to copy schedule is specified in the ScheduleCopyOptionsContainer structure. It returns
             ScheduleCopyResponses which will have information
             of copied  schedules and ServiceData. Errors
             will be returned in the list of partial errors in the ServiceData.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleCopyContainer: 
</font>

        :return: 
        """
        ...
    def CreateBillRates(self, Rates: list[BillRateContainer]) -> CreateBillRateResponse:
        """    
             This operation creates a new BillRates. BillRate is a business object
             that is used to represent Rate Modifiers,which are used  with resource costing
             information to calculate schedule and task costs and are defined by billing types,
             rates and currency. This operation throws exceptions that are system and database
             exceptions . There are no specific business logic errors. The created objects are
             returned back in the service data of the response.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Rates: 

        :return: The created bill rate objects, Partial errors and failures are returned through this
             object.
        """
        ...
    def CreateSchedule(self, NewSchedules: list[NewScheduleContainer]) -> CreateScheduleResponse:
        """    
             This operation creates new schedule based on the initial user's request to the application
             interface. The information needed to create Schedule is specified in the NewScheduleContainer structure. It returns CreateScheduleResponse which will have information
             of created schedules and ServiceData. Errors
             will be returned in the list of partial errors in the ServiceData.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param NewSchedules: 

        :return: 
        """
        ...
    def CreateScheduleDeliverableTemplates(self, ScheduleDeliverableData: list[ScheduleDeliverableData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates new schedule deliverable. The created objects are returned
             back in the ServiceData of the response.
             ServiceData will contain partial errors in
             case of operation failure.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleDeliverableData: 
                         Vector of ScheduleDeliverableData structures. This structure will have all information
                         necessory to create a schedule deliverable
             
        :return: 
        """
        ...
    def UpdateTaskCostData(self, Updates: list[TaskCostUpdate]) -> UpdateTaskCostDataResponse:
        """    
             This operation creates, updates and deletes fixed cost entries and task costing metadata
             such as bill code, sub code etc. This operation throws exceptions that are system
             and database exceptions. There are no specific business logic errors. The created
             objects are returned back in the service data of the response.
             



Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Updates: 

        :return: 
        """
        ...

