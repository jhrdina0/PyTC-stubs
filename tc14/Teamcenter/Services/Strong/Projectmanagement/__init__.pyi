import System
import Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2007_12.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2011_02.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2011_12.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2012_09.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2014_06.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2015_07.ScheduleManagement
import Teamcenter.Services.Strong.Projectmanagement._2022_06.ScheduleManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ScheduleManagementRestBindingStub(ScheduleManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def AddMemberships(self, MembershipData: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.MembershipData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def AddMemberships(self, MembershipData: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.MembershipData]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.AddMembershipResponse: ...
    @typing.overload
    def CopySchedules(self, ScheduleCopyContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.ScheduleCopyContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CopySchedules(self, ScheduleCopyContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.ScheduleCopyOptionsContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.MultiScheduleCopyResponse: ...
    @typing.overload
    def CopySchedules(self, ScheduleCopyContainer: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleCopyOptionsContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleCopyResponses: ...
    @typing.overload
    def CopySchedules(self, Containers: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.ScheduleCopyOptionsContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleCopyResponses: ...
    @typing.overload
    def CreateNewBaselines(self, CreateBaselineContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.CreateBaselineContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateNewBaselines(self, CreateBaselineContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.CreateBaselineContainer], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateSchedule(self, NewSchedules: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.CreateScheduleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateSchedule(self, NewSchedules: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.NewScheduleContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.CreateScheduleResponse: ...
    @typing.overload
    def CreateScheduleDeliverableTemplates(self, ScheduleDeliverableData: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.ScheduleDeliverableData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateScheduleDeliverableTemplates(self, ScheduleDeliverableData: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleDeliverableData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateTaskDeliverableTemplates(self, TaskDeliverableData: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.TaskDeliverableData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateTaskDeliverableTemplates(self, TaskDeliverableData: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.TaskDeliverableContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteSchedulingObjects(self, ScheduleObjDeleteContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.ScheduleObjDeleteContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def BaselineTasks(self, ScheduleTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask], ScheduleBaseline: Teamcenter.Soa.Client.Model.Strong.Schedule) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateOrUpdateNotificationRules(self, NotificationsContainers: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.NotificationRuleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateOrUpdateNotificationRules(self, NotificationRuleInfos: list[Teamcenter.Services.Strong.Projectmanagement._2022_06.ScheduleManagement.NotificationRuleInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteNotificationRules(self, NotificationRuleContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.DeleteNotificationRuleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetNotificationRules(self, NotificationRuleContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.GetNotificationRuleContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.NotificationRulesList: ...
    def GetDemandProfile(self, Requests: list[Teamcenter.Services.Strong.Projectmanagement._2007_12.ScheduleManagement.DemandProfileRequest]) -> Teamcenter.Services.Strong.Projectmanagement._2007_12.ScheduleManagement.DemandProfileResponses: ...
    def CreateBillRates(self, Rates: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.BillRateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.CreateBillRateResponse: ...
    def UpdateTaskCostData(self, Updates: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.TaskCostUpdate]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.UpdateTaskCostDataResponse: ...
    def ModifySchedules(self, ScheduleModifyContainers: list[Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement.ScheduleModifyContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def UpdateTasks(self, Updates: list[Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement.GenericAttributesContainer], ScheduleUid: list[str]) -> Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement.GenericResponseContainer: ...
    @typing.overload
    def UpdateTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, Updates: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.ObjectUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SpecialPasteScheduleTasks(self, CopyContainer: Teamcenter.Services.Strong.Projectmanagement._2011_02.ScheduleManagement.SpecialCopyContainer) -> Teamcenter.Services.Strong.Projectmanagement._2011_02.ScheduleManagement.MultiSchSpecialCopyResponse: ...
    def CopySchedulesAsyncClient(self, SchToCopy: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.ScheduleCopyOptionsContainerAsync]) -> bool: ...
    def CreateProxyTasks(self, NewProxyTasks: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.ProxyTaskContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.ProxyTaskResponses: ...
    def LoadSchedules(self, LoadScheduleContainers: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.LoadScheduleContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.MultipleScheduleLoadResponses: ...
    def ManageScheduleLocks(self, Requests: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.LockRequest]) -> Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.LockResponses: ...
    def RefreshScheduleObject(self, RefreshScheduleContainer: Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.RefreshScheduleContainer) -> Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.MultipleScheduleLoadResponses: ...
    def UpdateTaskExecution(self, TaskUpdateExec: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.TaskExecUpdate]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteScheduleAsyncClient(self, SchToDelete: Teamcenter.Soa.Client.Model.Strong.Schedule) -> bool: ...
    @typing.overload
    def CreateDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDependencies: list[Teamcenter.Services.Strong.Projectmanagement._2011_12.ScheduleManagement.DependencyCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2011_12.ScheduleManagement.CreatedDependenciesContainer: ...
    @typing.overload
    def CreateDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDependencies: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.DependencyCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedDependenciesContainer: ...
    def UpdateSchedules(self, ScheduleUpdates: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.ObjectUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def AssignResources(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateAssignments: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.AssignmentCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    @typing.overload
    def AssignResources(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateAssignments: list[Teamcenter.Services.Strong.Projectmanagement._2012_09.ScheduleManagement.AssignmentCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    @typing.overload
    def AssignResources(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateAssignments: list[Teamcenter.Services.Strong.Projectmanagement._2015_07.ScheduleManagement.AssignmentCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    def CreateTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateContainers: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.TaskCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    def DeleteAssignments(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, AssignmentDeletes: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, DependencyDeletes: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, DeleteTasks: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.DeleteTaskContainer: ...
    def FindCriticalPathTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CriticalTasksContainer: ...
    def LaunchScheduledWorkflow(self, Tasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.LaunchedWorkflowContainer: ...
    def MoveTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, MoveRequests: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.MoveRequest]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RecalculateScheduleNonInteractive(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, RecalcType: int, RunAsync: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ScaleScheduleNonInteractive(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, ScaleFactor: float, Options: Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.SchMgtOptions) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ShiftScheduleNonInteractive(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDate: System.DateTime, NewFinish: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UpdateAssignments(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, AssignmentUpdates: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.AssignmentUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UpdateDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, DependencyUpdates: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.DependencyUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ClaimAssignment(self, Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask, Assignment: Teamcenter.Soa.Client.Model.Strong.ResourceAssignment) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    def FilterUsers(self, Filteringcriteria: Teamcenter.Services.Strong.Projectmanagement._2014_06.ScheduleManagement.FilterCriteria) -> Teamcenter.Services.Strong.Projectmanagement._2014_06.ScheduleManagement.FilteredUsersInfo: ...
    def CreatePhaseGateTask(self, TaskInputContainer: Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.TaskCreateContainer) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    def DetachSchedule(self, DetachScheduleContainer: list[Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.DetachScheduleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetEVMResults(self, InputEVMData: Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.EVMDataRequest) -> Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.EVMResultsResponse: ...
    def GetResourceGraphData(self, LoadResourceGraphContainer: Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.LoadResourceGraphContainer) -> Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.AnalyticsMultipleResourceAssignmentStacks: ...
    def InsertSchedule(self, InsertScheduleContainer: list[Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.InsertScheduleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetCostRollupData(self, CostDetailRequest: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]) -> Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.CostDetailResponse: ...
    def ReplaceAssignment(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewAssignments: list[Teamcenter.Services.Strong.Projectmanagement._2012_09.ScheduleManagement.AssignmentCreateContainer], AssignmentDeletes: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    def VerifySchedule(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule) -> Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.FailedObjectContainer: ...
    def ShiftSchedule(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDate: System.DateTime, IsNewFinishDate: bool, RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def WhatIfAnalysis(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, WhatIfOption: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SubmitTimesheetEntries(self, TimesheetEntries: list[Teamcenter.Soa.Client.Model.Strong.TimeSheetEntry], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def LoadBaselines(self, LoadBaselinesInfo: Teamcenter.Services.Strong.Projectmanagement._2022_06.ScheduleManagement.LoadBaselinesInfo) -> Teamcenter.Services.Strong.Projectmanagement._2022_06.ScheduleManagement.LoadBaselineResponse: ...

class ScheduleManagementService:
    """
    
            The ScheduleManagement service provides a
            wide variety of operations to for schedule management.  There are
operations to support
            managing schedule, tasks, assignments, dependencies, notification
rules, and more.
            There are also various operations to support the most common
functionalities needed
            in schedule management.

            The ScheduleManagement service can be used
            for supporting following use-cases:

Adding memberships to schedule

Baselining to tasks

Copying schedules

Create new baselines

Creating schedule deliverable templates

Creating task deliverable templates

Creating, updating, deleting and retrieving schedules

Creating, updating, deleting, and retrieving notification rules

Updating task cost data

Creating, updating, and deleting tasks

Special paste schedule tasks

Creating proxy tasks

Loading specified schedules

Managing schedule locks

Refreshing a schedule

Creating, updating, and deleting dependencies

Assigning, updating, and deleting resources

Finding critical path tasks

Launching schedule workflow

Moving tasks within a schedule

Shifting the schedule backward or forward

Claiming an assignment

Library Reference:

TcSoaProjectManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ScheduleManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def AddMemberships(self, MembershipData: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.MembershipData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def AddMemberships(self, MembershipData: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.MembershipData]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.AddMembershipResponse: ...
    @typing.overload
    def CopySchedules(self, ScheduleCopyContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.ScheduleCopyContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CopySchedules(self, ScheduleCopyContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.ScheduleCopyOptionsContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.MultiScheduleCopyResponse: ...
    @typing.overload
    def CopySchedules(self, ScheduleCopyContainer: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleCopyOptionsContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleCopyResponses: ...
    @typing.overload
    def CopySchedules(self, Containers: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.ScheduleCopyOptionsContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleCopyResponses: ...
    @typing.overload
    def CreateNewBaselines(self, CreateBaselineContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.CreateBaselineContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateNewBaselines(self, CreateBaselineContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.CreateBaselineContainer], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateSchedule(self, NewSchedules: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.CreateScheduleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateSchedule(self, NewSchedules: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.NewScheduleContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.CreateScheduleResponse: ...
    @typing.overload
    def CreateScheduleDeliverableTemplates(self, ScheduleDeliverableData: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.ScheduleDeliverableData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateScheduleDeliverableTemplates(self, ScheduleDeliverableData: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.ScheduleDeliverableData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateTaskDeliverableTemplates(self, TaskDeliverableData: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.TaskDeliverableData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateTaskDeliverableTemplates(self, TaskDeliverableData: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.TaskDeliverableContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteSchedulingObjects(self, ScheduleObjDeleteContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.ScheduleObjDeleteContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    @typing.overload
    def CreateOrUpdateNotificationRules(self, NotificationsContainers: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.NotificationRuleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateOrUpdateNotificationRules(self, NotificationRuleInfos: list[Teamcenter.Services.Strong.Projectmanagement._2022_06.ScheduleManagement.NotificationRuleInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteNotificationRules(self, NotificationRuleContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.DeleteNotificationRuleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Delete notification rules for Schedule or ScheduleTask based on the
             contents of the delete notifications container. After deleting the notification will
             rule, the users attached to that rule will not receive any more notifications for
             that specific action.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param NotificationRuleContainer: 
                         A collection of DeleteNotificationRuleContainers.
             
        :return: The reference to the tag of the deleted objects.
        """
        ...
    def GetNotificationRules(self, NotificationRuleContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.GetNotificationRuleContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2007_06.ScheduleManagement.NotificationRulesList:
        """    
             Get a list of notification rules for Schedule or ScheduleTask based
             on the notifications container. Use notifications to notify individuals, including
             yourself, of important events associated with selected objects. Notifications utilize
             Teamcenter mail and the Subscription Manager. To receive notifications and
             subscriptions, a system administrator must set the value of the Mail_server_name
             preference to a name of a valid mail server (this task needs only to be performed
             once). The e-mail address in the Person object for every user that's expected
             to receive a notification.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param NotificationRuleContainer: 

        :return: 
        """
        ...
    def GetDemandProfile(self, Requests: list[Teamcenter.Services.Strong.Projectmanagement._2007_12.ScheduleManagement.DemandProfileRequest]) -> Teamcenter.Services.Strong.Projectmanagement._2007_12.ScheduleManagement.DemandProfileResponses:
        """    
             Calculates the demand profile data for a schedule based on the initial input request
             to the Application Interface..
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Requests: 

        :return: The demand profile information and errors. The information includes the schedule,
             start period, end period, and months in period.
        """
        ...
    def CreateBillRates(self, Rates: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.BillRateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.CreateBillRateResponse:
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
    def UpdateTaskCostData(self, Updates: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.TaskCostUpdate]) -> Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.UpdateTaskCostDataResponse:
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
    def ModifySchedules(self, ScheduleModifyContainers: list[Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement.ScheduleModifyContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Not Implemented.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleModifyContainers: 
                         Not Implemented
             
        :return: Not Implemented
        """
        ...
    @typing.overload
    def UpdateTasks(self, Updates: list[Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement.GenericAttributesContainer], ScheduleUid: list[str]) -> Teamcenter.Services.Strong.Projectmanagement._2009_10.ScheduleManagement.GenericResponseContainer: ...
    @typing.overload
    def UpdateTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, Updates: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.ObjectUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SpecialPasteScheduleTasks(self, CopyContainer: Teamcenter.Services.Strong.Projectmanagement._2011_02.ScheduleManagement.SpecialCopyContainer) -> Teamcenter.Services.Strong.Projectmanagement._2011_02.ScheduleManagement.MultiSchSpecialCopyResponse:
        """    
             Gets the selected Schedule and their tasks and paste it to target task as specified
             by the options.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param CopyContainer: 
                         Container which consists of list of <font face="courier" height="10">FromSchedule</font>
                         and a <font face="courier" height="10">ToSchedule</font>

        :return: 
        """
        ...
    def CopySchedulesAsyncClient(self, SchToCopy: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.ScheduleCopyOptionsContainerAsync]) -> bool:
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
    def CreateProxyTasks(self, NewProxyTasks: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.ProxyTaskContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.ProxyTaskResponses:
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
    def LoadSchedules(self, LoadScheduleContainers: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.LoadScheduleContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.MultipleScheduleLoadResponses:
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
    def ManageScheduleLocks(self, Requests: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.LockRequest]) -> Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.LockResponses:
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
    def RefreshScheduleObject(self, RefreshScheduleContainer: Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.RefreshScheduleContainer) -> Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.MultipleScheduleLoadResponses:
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
    def UpdateTaskExecution(self, TaskUpdateExec: list[Teamcenter.Services.Strong.Projectmanagement._2011_06.ScheduleManagement.TaskExecUpdate]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    @typing.overload
    def CreateDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDependencies: list[Teamcenter.Services.Strong.Projectmanagement._2011_12.ScheduleManagement.DependencyCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2011_12.ScheduleManagement.CreatedDependenciesContainer: ...
    @typing.overload
    def CreateDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDependencies: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.DependencyCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedDependenciesContainer: ...
    def UpdateSchedules(self, ScheduleUpdates: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.ObjectUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    @typing.overload
    def AssignResources(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateAssignments: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.AssignmentCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    @typing.overload
    def AssignResources(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateAssignments: list[Teamcenter.Services.Strong.Projectmanagement._2012_09.ScheduleManagement.AssignmentCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    @typing.overload
    def AssignResources(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateAssignments: list[Teamcenter.Services.Strong.Projectmanagement._2015_07.ScheduleManagement.AssignmentCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer: ...
    def CreateTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateContainers: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.TaskCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer:
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
    def DeleteTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, DeleteTasks: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.DeleteTaskContainer:
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
    def FindCriticalPathTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CriticalTasksContainer:
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
    def LaunchScheduledWorkflow(self, Tasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.LaunchedWorkflowContainer:
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
    def MoveTasks(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, MoveRequests: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.MoveRequest]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def UpdateAssignments(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, AssignmentUpdates: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.AssignmentUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def UpdateDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, DependencyUpdates: list[Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.DependencyUpdateContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def ClaimAssignment(self, Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask, Assignment: Teamcenter.Soa.Client.Model.Strong.ResourceAssignment) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer:
        """    
             Claims an assignment.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Task: 
                         The task containing the assignment.
             
        :param Assignment: 
                         The assignment to claim.
             
        :return: The new assignment and any cascading updates.
        """
        ...
    def FilterUsers(self, Filteringcriteria: Teamcenter.Services.Strong.Projectmanagement._2014_06.ScheduleManagement.FilterCriteria) -> Teamcenter.Services.Strong.Projectmanagement._2014_06.ScheduleManagement.FilteredUsersInfo:
        """    
             In Schedule Manager, Discipline, Group, Role and Fnd0Qualification
             can be assigned to the ScheduleTask as placeholder assignments. These placeholder
             assignments can then be assigned to specific users who are a part of the placeholder
             assignment.
             

             The operation returns a list of Users which match the input filter criteria of Discipline,
             Group, Role and Fnd0Qualification.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Filteringcriteria: 
                         The filter criteria for retrieving the list of matching <b>Users</b>.
             
        :return: 
        """
        ...
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
    def DetachSchedule(self, DetachScheduleContainer: list[Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.DetachScheduleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetEVMResults(self, InputEVMData: Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.EVMDataRequest) -> Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.EVMResultsResponse:
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
    def GetResourceGraphData(self, LoadResourceGraphContainer: Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.LoadResourceGraphContainer) -> Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.AnalyticsMultipleResourceAssignmentStacks:
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
    def InsertSchedule(self, InsertScheduleContainer: list[Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.InsertScheduleContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def GetCostRollupData(self, CostDetailRequest: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]) -> Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.CostDetailResponse:
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
    def VerifySchedule(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule) -> Teamcenter.Services.Strong.Projectmanagement._2014_10.ScheduleManagement.FailedObjectContainer:
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
    def ShiftSchedule(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDate: System.DateTime, IsNewFinishDate: bool, RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def WhatIfAnalysis(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, WhatIfOption: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation allows the user to perform What-If analysis on a Schedule by
             making scheduling changes locally without affecting other users and save or cancel
             the changes made during the What-If analysis.
             

             Only the following operations can be performed by the user who has started the What-If
             analysis:
             
             1. Modify all properties of the Schedule.
             
             2. Modify all properties of the ScheduleTask other than the following execution
             proeprties : status, work complete, complete percent, actual start date, actual finish
             date, work remaining.
             
             3. Create, delete and update ScheduleTask, ResourceAssignment, TaskDependency,
             and Fnd0ProxyTask objects.
             

             The following operations cannot be performed by the user who has started the What-If
             analysis:
             
             1. Modify the following execution properties of the ScheduleTask : status,
             work complete, complete percent, actual start date, actual finish date, work remaining.
             
             2. Insert Schedule and detach Schedule operations.
             

             Only the following operations can be performed by other users when a Schedule is
             in What-If analysis mode:
             
             1. Modify the following execution properties of the ScheduleTask : status,
             work complete, complete percent, actual start date, actual finish date, work remaining.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The Schedule to set the What-If analysis mode.
             
        :param WhatIfOption: 
                         Specifies the What-If analysis option. The valid options are Start, SaveAndContinue,
                         SaveAndExit and CancelAndExit.
             
        :return: 230086 : The Schedule cannot be unlocked, because it is locked by the user.
        """
        ...
    def SubmitTimesheetEntries(self, TimesheetEntries: list[Teamcenter.Soa.Client.Model.Strong.TimeSheetEntry], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation submits the list of TimeSheetEntry to workflow. The preference SM_TIMESHEET_APPROVE_WORKFLOW
             will be used to determine the workflow template. If not specified, TimeSheetApproval
             template will be used.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param TimesheetEntries: 
                         A list of TimeSheetEntry objects to to submit to workflow.
             
        :param RunInBackground: 
                         If true perform the operation in background mode in a separate asynchronous server
                         session. False to perform the operation synchronously
             
        :return: 230141 : The privileged user assigned to the Schedule Task is invalid. Please assign
             either a user or a resource pool of any type.
        """
        ...
    def LoadBaselines(self, LoadBaselinesInfo: Teamcenter.Services.Strong.Projectmanagement._2022_06.ScheduleManagement.LoadBaselinesInfo) -> Teamcenter.Services.Strong.Projectmanagement._2022_06.ScheduleManagement.LoadBaselineResponse:
        """    
             Loads the information about the baseline tasks of the given ScheduleTask objects
             based on the source Schedule and the baseline Schedule objects.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param LoadBaselinesInfo: 
                         Information about the <b>Schedule</b> baseline to load.
             
        :return: 230504: The schedule baseline to load is invaliddoes not belong to the source schedule.
        """
        ...

