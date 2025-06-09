import System
import Teamcenter.Services.Strong.Workflow._2007_06.Workflow
import Teamcenter.Services.Strong.Workflow._2008_06.Workflow
import Teamcenter.Services.Strong.Workflow._2010_09.Workflow
import Teamcenter.Services.Strong.Workflow._2013_05.Workflow
import Teamcenter.Services.Strong.Workflow._2014_06.Workflow
import Teamcenter.Services.Strong.Workflow._2014_10.Workflow
import Teamcenter.Services.Strong.Workflow._2015_07.Workflow
import Teamcenter.Services.Strong.Workflow._2019_06.Workflow
import Teamcenter.Services.Strong.Workflow._2020_01.Workflow
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class WorkflowRestBindingStub(WorkflowService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def SetReleaseStatus(self, Input: list[Teamcenter.Services.Strong.Workflow._2007_06.Workflow.ReleaseStatusInput]) -> Teamcenter.Services.Strong.Workflow._2007_06.Workflow.SetReleaseStatusResponse: ...
    @typing.overload
    def AddSignoffs(self, Signoffs: list[Teamcenter.Services.Strong.Workflow._2008_06.Workflow.CreateSignoffs]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def AddSignoffs(self, Signoffs: list[Teamcenter.Services.Strong.Workflow._2015_07.Workflow.CreateSignoffs]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ChangeState(self, StateInput: Teamcenter.Services.Strong.Workflow._2008_06.Workflow.ChangeStateInputInfo) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.ChangeStateOutput: ...
    def CreateInstance(self, StartImmediately: bool, ObserverKey: str, Name: str, Subject: str, Description: str, ContextData: Teamcenter.Services.Strong.Workflow._2008_06.Workflow.ContextData) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.InstanceInfo: ...
    def GetAssignmentLists(self, Names: list[str]) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.AssignmentLists: ...
    def GetResourcePool(self, GroupRoleRef: list[Teamcenter.Services.Strong.Workflow._2008_06.Workflow.GroupRoleRef]) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.GetResourcePoolOutput: ...
    def ListDefinitions(self, Name: str, Templatestatus: int) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.ProcessTemplates: ...
    def RemoveSignoffs(self, Signoffs: list[Teamcenter.Services.Strong.Workflow._2008_06.Workflow.RemoveSignoffsInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ViewAuditFile(self, AuditedObject: Teamcenter.Soa.Client.Model.ModelObject, IsSignoffReport: bool) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.AuditFile: ...
    def AddAttachments(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Attachments: Teamcenter.Services.Strong.Workflow._2008_06.Workflow.AttachmentInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AssignAllTasks(self, Process: Teamcenter.Soa.Client.Model.Strong.EPMJob, AssignmentList: Teamcenter.Soa.Client.Model.Strong.EPMAssignmentList, Resources: list[Teamcenter.Services.Strong.Workflow._2008_06.Workflow.Resources]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DelegateSignoff(self, Delegatee: Teamcenter.Soa.Client.Model.ModelObject, Signoff: Teamcenter.Soa.Client.Model.Strong.Signoff) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetAllTasks(self, Process: Teamcenter.Soa.Client.Model.Strong.EPMJob, State: int) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.Tasks: ...
    @typing.overload
    def GetWorkflowTemplates(self, Targets: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject], AllOrAssignedCriteria: str) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.Templates: ...
    @typing.overload
    def GetWorkflowTemplates(self, Input: list[Teamcenter.Services.Strong.Workflow._2013_05.Workflow.GetWorkflowTemplatesInputInfo]) -> Teamcenter.Services.Strong.Workflow._2013_05.Workflow.GetWorkflowTemplatesResponse: ...
    def PerformAction(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Action: str, Comments: str, Password: str, SupportingValue: str, SupportingObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveAttachments(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Attachments: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ApplyTemplateToProcesses(self, ApplyTemplateInput: list[Teamcenter.Services.Strong.Workflow._2010_09.Workflow.ApplyTemplateInput], ProcessingMode: int) -> Teamcenter.Services.Strong.Workflow._2010_09.Workflow.ApplyTemplateResponse: ...
    def PerformAction2(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Action: str, Comments: str, Password: str, SupportingValue: str, SupportingObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def PerformAction3(self, Input: list[Teamcenter.Services.Strong.Workflow._2014_06.Workflow.PerformActionInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetActiveSurrogate(self, Input: list[Teamcenter.Services.Strong.Workflow._2014_06.Workflow.SetActiveSurrogateInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetSurrogate(self, Requests: list[Teamcenter.Services.Strong.Workflow._2014_06.Workflow.SurrogateInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def PerformActionWithSignature(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Action: str, Comments: str, Password: str, SupportingValue: str, SupportingObject: Teamcenter.Soa.Client.Model.ModelObject, Signatures: list[Teamcenter.Services.Strong.Workflow._2014_06.Workflow.ApplySignatureInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetOutOfOffice(self, FromResource: Teamcenter.Soa.Client.Model.Strong.User, ToResource: Teamcenter.Soa.Client.Model.ModelObject, StartDate: System.DateTime, EndDate: System.DateTime) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateWorkflow(self, Input: Teamcenter.Services.Strong.Workflow._2014_10.Workflow.CreateWkfInput) -> Teamcenter.Services.Strong.Workflow._2014_10.Workflow.CreateWkfOutput: ...
    def CreateOrUpdateHandler(self, Input: list[Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateUpdateHandlerInput]) -> Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateOrUpdateHandlerResponse: ...
    def CreateOrUpdatePAL(self, Input: list[Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateUpdatePALInput]) -> Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateOrUpdatePALResponse: ...
    def CreateOrUpdateTemplate(self, Input: list[Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateUpdateTemplateInput]) -> Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateOrUpdateTemplateResponse: ...
    def GetRegisteredHandlers(self) -> Teamcenter.Services.Strong.Workflow._2019_06.Workflow.GetRegisteredHandlerResponse: ...
    def GetSupportedHandlerArguments(self, Input: list[Teamcenter.Services.Strong.Workflow._2020_01.Workflow.SupportedHandlerArgumentsInput]) -> Teamcenter.Services.Strong.Workflow._2020_01.Workflow.SupportedHandlerArgumentsReponse: ...

class WorkflowService:
    """
    
            Workflow Service exposes operations to create and manage workflow
processes in an
            organization.  The service provides operations that can be used in
the following
            use cases:

Query for the workflow templates designed based on the business process
            requirements.

Create workflow processes using the Workflow Templates.

Add Reviewers to the workflow process to review and signoff on the
            tasks assigned to them.

Add additional target /reference attachments to the tasks during
            the lifecycle of the workflow process.

Reassign the task to a different reviewer.

View the workflow process history and signoff history.

Apply the changes made to the workflow templates after the workflow
            processes are created to the active processes.

Assign all the tasks in the workflow process using a process assignment
            list -- a predefined list of reviewers to be assigned to each task
in a process.

Library Reference:

TcSoaWorkflowStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> WorkflowService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def SetReleaseStatus(self, Input: list[Teamcenter.Services.Strong.Workflow._2007_06.Workflow.ReleaseStatusInput]) -> Teamcenter.Services.Strong.Workflow._2007_06.Workflow.SetReleaseStatusResponse:
        """    
             Manages the release status status of an object  The permitted operations are Append,
             Delete, Rename and Replace Currently Append and Delete are supported With the delete
             operation if an empty string is passed in instead of the status name all statuses
             will be cleared for that set of workspace objects.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Input: 
                         A vector of ReleaseStatusInput structures that control operations performed on the
                         objects
             
        :return: Failure will be with error messages in the ServiceData.
        """
        ...
    @typing.overload
    def AddSignoffs(self, Signoffs: list[Teamcenter.Services.Strong.Workflow._2008_06.Workflow.CreateSignoffs]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def AddSignoffs(self, Signoffs: list[Teamcenter.Services.Strong.Workflow._2015_07.Workflow.CreateSignoffs]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ChangeState(self, StateInput: Teamcenter.Services.Strong.Workflow._2008_06.Workflow.ChangeStateInputInfo) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.ChangeStateOutput:
        """    
             changeState - Change the state of a process or a task at a remote site.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param StateInput: 
                         ChangeStateInputInfo
             
        :return: the structure consisting of the changed state of the process or sub process or a
             task at the remote site, the unique ID of the remote process or task whose state
             was changed, the uniqueID of the process or task who initiated the state change and
             the serviceData containing the URI of the modified remote process or task.
        """
        ...
    def CreateInstance(self, StartImmediately: bool, ObserverKey: str, Name: str, Subject: str, Description: str, ContextData: Teamcenter.Services.Strong.Workflow._2008_06.Workflow.ContextData) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.InstanceInfo:
        """    
             Workflow processes are the instantiations from workflow templates. This operation
             can be used to create a workflow process or sub process at a local or a remote site
             from a given workflow template.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param StartImmediately: 
                         Boolean value to say whether the instance created should be immediately started or
                         should be put into initial state for later starting by use of the "Start" operation.
                         No value implies true. (This argument is currently not supported).
             
        :param ObserverKey: 
                         URI of the observer that initiated the workflow process or sub process at a remote
                         site. The observer is to be notified of events impacting the execution of this process
                         instance such as state changes, and most notably the completion of the instance.
                         If not specified, the observer will not receive completed notification from the sub
                         process. (This argument is currently not supported)
             
        :param Name: 
                         Name of the remote process or sub process instance.
             
        :param Subject: 
                         A shorter description of the purpose of the remote process or sub process.
             
        :param Description: 
                         A longer description of the purpose of the remote process or sub process.
             
        :param ContextData: 
                         Context-specific data required to create a process or sub process at a local or a
                         remote site in Teamcenter.
             
        :return: InstanceInfo structure containing the URI of the new process or sub process that
             has been created at the remote site ServiceData -  contains the URI of the newly
             created process or sub process at the remote site.
        """
        ...
    def GetAssignmentLists(self, Names: list[str]) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.AssignmentLists:
        """    
             Gets the process assignment list given the process assignment list names.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Names: 
                         A set of process assignment list names
             
        :return: AssignmentList - with list of process assignment lists and ServiceData
        """
        ...
    def GetResourcePool(self, GroupRoleRef: list[Teamcenter.Services.Strong.Workflow._2008_06.Workflow.GroupRoleRef]) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.GetResourcePoolOutput:
        """    
             getResourcePool - Returns regular or all member ResourcePools corresponding to the
             list of GroupRoleRef (group and role).
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param GroupRoleRef: 
                         list of GroupRoleRef  structure containing info about the Resource Pool being asked
                         for
             
        :return: list of ResourcePoolInfo - structure containing the Resource Pool matching the GroupRoleRef
             and the Service Data
        """
        ...
    def ListDefinitions(self, Name: str, Templatestatus: int) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.ProcessTemplates:
        """    
             Gets a list of process templates based on the criteria passed.  Description if name
             and status are specified, all the templates matching the name and the status are
             returned. If only name is specified, only the available templates matching the name
             will be returned If only status is specified, all the templates with the specified
             status is returned. If both are not specified, all the available templates will be
             returned for a non-Dba
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Name: 
                         name of the template to retrieve. This argument is optional.  Provide the value null
                         to make it optional.
             
        :param Templatestatus: 
                         TODO
             
        :return: ProcessTemplates
        """
        ...
    def RemoveSignoffs(self, Signoffs: list[Teamcenter.Services.Strong.Workflow._2008_06.Workflow.RemoveSignoffsInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             addSignoffs - Add/remove and update signoffs on a task.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Signoffs: 
                         list of Signoffs - structure containing the select signoff task tag, groupmembers
                         or
             
        :return: serviceData.
        """
        ...
    def ViewAuditFile(self, AuditedObject: Teamcenter.Soa.Client.Model.ModelObject, IsSignoffReport: bool) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.AuditFile:
        """    
             viewAuditFile - get audit information on the selected object when stored in a file.
             By default, audit info is stored in a file in teamcenter.  This operation cannot
             be used to get audit info when audit manager is turned on.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param AuditedObject: 
                         the object to get audit info on. E.g. workspace object in process or
                         process itself..
             
        :param IsSignoffReport: 
                         Boolean to indicate if the request is for a audit file or a signoff report. true
                         for a signoff report, false for a audit file
             
        :return: structure containing the audit file and the service data.
        """
        ...
    def AddAttachments(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Attachments: Teamcenter.Services.Strong.Workflow._2008_06.Workflow.AttachmentInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             addAttachments - Add attachments to a task.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Task: 
                         task to add attachments to.
             
        :param Attachments: 
                         structure containing the list of attachments and the attachment types. The attachments
                         can be target_objects, reference_objects,release status etc The attachment types
                         can be EPM_target_attachment, EPM_reference_attachment, EPM_release_status_attachment
                         and EPM_signoff_attachment
             
        :return: containing the updated task.
        """
        ...
    def AssignAllTasks(self, Process: Teamcenter.Soa.Client.Model.Strong.EPMJob, AssignmentList: Teamcenter.Soa.Client.Model.Strong.EPMAssignmentList, Resources: list[Teamcenter.Services.Strong.Workflow._2008_06.Workflow.Resources]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Assign a process assignment list to a process. Description: If the assignment list
             is given, it will use it to apply the assignment list to the process.  If the assignment
             is not given, it will loop through the Resources structure and create the list of
             task templates and list of resources, profiles and other information to apply the
             resources to the process. Thus at a given time either assignmentList and resources
             both cannot be null. either one of them can be null
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Process: 
                         the process to which the process assignment list has to be assigned.
             
        :param AssignmentList: 
                         assignment list to be applied to the process
             
        :param Resources: 
                         list of structures containing resource info (for eg. Task template, Group member
                         or resource pool, signoff profiles, quorum etc).
             
        :return: - Service data contains any partial errors.
        """
        ...
    def DelegateSignoff(self, Delegatee: Teamcenter.Soa.Client.Model.ModelObject, Signoff: Teamcenter.Soa.Client.Model.Strong.Signoff) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Delegate a signoff to a different groupmember or a resourcepool.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Delegatee: 
                         The group memebr or a resource pool tag to be delegated to.
             
        :param Signoff: 
                         signoff object.
             
        :return: serviceData.
        """
        ...
    def GetAllTasks(self, Process: Teamcenter.Soa.Client.Model.Strong.EPMJob, State: int) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.Tasks:
        """    
             Gets all the tasks in a process.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Process: 
                         workflow process object
             
        :param State: 
                         TODO
             
        :return: Tasks
        """
        ...
    @typing.overload
    def GetWorkflowTemplates(self, Targets: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject], AllOrAssignedCriteria: str) -> Teamcenter.Services.Strong.Workflow._2008_06.Workflow.Templates: ...
    @typing.overload
    def GetWorkflowTemplates(self, Input: list[Teamcenter.Services.Strong.Workflow._2013_05.Workflow.GetWorkflowTemplatesInputInfo]) -> Teamcenter.Services.Strong.Workflow._2013_05.Workflow.GetWorkflowTemplatesResponse: ...
    def PerformAction(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Action: str, Comments: str, Password: str, SupportingValue: str, SupportingObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Performs workflow actions on a task. The actions that can be performed using this
             operation are : assign, start, complete, skip, suspend, resume, undo, perform, approve,
             reject, promote and demote. Note: Special case This operation can be used to set
             only comments without changing the decision for perform signoff task. To do that,
             use the 'EPM_no_action' as input for action argument and use the current decision
             for the supportingValue argument.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Task: 
                         The task
             
        :param Action: 
                         the action to be performed on the task required. The possible values for action are
                         defined in enum SoaEPMAction.  They are SOA_EPM_assign_action, SOA_EPM_start_action,
                         SOA_EPM_complete_action,  SOA_EPM_skip_action, SOA_EPM_suspend_action,  SOA_EPM_resume_action,
                         SOA_EPM_undo_action, SOA_EPM_abort_action, SOA_EPM_perform_action,
                         SOA_EPM_add_attachment_action, SOA_EPM_remove_attachment_action, SOA_EPM_approve_action,
                         SOA_EPM_reject_action, SOA_EPM_promote_action, SOA_EPM_demote_action, SOA_EPM_refuse_action,
                         SOA_EPM_assign_approver_action, SOA_EPM_notify_action and SOA_EPM_no_action
             
        :param Comments: 
                         user comments. This argument is optional.  Provide the value null to make it optional.
             
        :param Password: 
                         password for secure signoff action required for secure signoff.        This argument
                         is optional.  Provide the value null to make it optional(non secure).
             
        :param SupportingValue: 
                         this argument can be used to send in decision value or result.  If the task is perform
                         signoff task, provide the decision using this argument.  The possible values for
                         decision are SOA_EPM_no_decision, SOA_EPM_approve, SOA_EPM_reject.  For all the other
                         tasks, provide the result value using this argument.  Following are the result values
                         applicable for different tasks..   SOA_EPM_unset - Do,Review,Route,Ack,EPMTask,Cond(Auto/Manual),SST
                         and Validate  SOA_EPM_completed - Do,EPMTask and SST  SOA_EPM_unable_to_complete
                         -Do,EPMTtask,Cond (Manual)  SOA_EPM_true -Cond (Auto/Manual)  SOA_EPM_false -Cond
                         (Auto/Manual)  SOA_EPM_no_error - Validate
             
        :param SupportingObject: 
                         If the action is assign, provide a user tag or a resource pool tag to assign the
                         task to. If the task is perform signoff task, provide the signoff tag to set the
                         decision on.
             
        :return: Service data - returns index of the input vector if call on that fails
        """
        ...
    def RemoveAttachments(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Attachments: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             removeAttachments - Remove attachments to a task.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Task: 
                         task to remove attachments from.
             
        :param Attachments: 
                         the list of attachments to remove The attachments can be target_objects, reference_objects,release
                         status etc
             
        :return: containing the updated task.
        """
        ...
    def ApplyTemplateToProcesses(self, ApplyTemplateInput: list[Teamcenter.Services.Strong.Workflow._2010_09.Workflow.ApplyTemplateInput], ProcessingMode: int) -> Teamcenter.Services.Strong.Workflow._2010_09.Workflow.ApplyTemplateResponse:
        """    
             Apply the specified templates to all active workflow processes that are based on
             earlier versions of the templates.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param ApplyTemplateInput: 
                         Templates to be applied to active processes
             
        :param ProcessingMode: 
                         Indicates if request needs to be processed asynchronously.  0 - Indicates synchronous
                         processing. 1 - Indicates asynchronous processing.
             
        :return: List of active processes that were updated successfully and list of failures
        """
        ...
    def PerformAction2(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Action: str, Comments: str, Password: str, SupportingValue: str, SupportingObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation performs an action on a workflow task. The following actions are supported:
             

Assign
             
Start
             
Complete
             
Skip
             
Suspend
             
Resume
             
Undo
             
Perform
             
Approve
             
Reject
             
Promote
             
Demote
             
Claim
             



Use Cases:

             User can perform a workflow task from worklist folder in rich or thin client. Similarly,
             workflow tasks can be performed or signed-off using office client as well. This operation
             can be used to perform or sign-off the workflow tasks.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Task: 
                         Workflow task on which the action needs to be performed
             
        :param Action: 
                         "SOA_EPM_claim_action"                            Claim the task
             
        :param Comments: 
                         A comment assigned to this task action. This may be an empty string.
             
        :param Password: 
                         The password for a secure task. The value of this parameter is ignored for non-secure
                         tasks.
             
        :param SupportingValue: 
                         Following are the result values applicable for different tasks: "SOA_EPM_unset" -
                         Do Task, Review Task, Route Task, Ackowledge Task, EPMTask, Condition Task (Auto/Manual),
                         select-signoff-team task, Validate Task "SOA_EPM_completed" - Do Task, EPMTask, select-signoff-team
                         task "SOA_EPM_unable_to_complete" - Do Task, EPMTtask, Condition Task (Manual) "SOA_EPM_true"
                         - Condition Task (Auto/Manual)  "SOA_EPM_false" - Condition Task (Auto/Manual)  "SOA_EPM_no_error"
                         - Validate Task
             
        :param SupportingObject: 
                         If the action is <i>assign</i>, provide a user or resource pool to assign the task.
                         If the task is perform-signoff task, provide the Signoff object to set the decision.
                         If the task is a perform-signoff task and the action is <i>claim</i>, provide the
                         signoff object to be claimed.
             
        :return: 
        """
        ...
    def PerformAction3(self, Input: list[Teamcenter.Services.Strong.Workflow._2014_06.Workflow.PerformActionInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation performs an action on an EPMTask or Signoff. This operation
             also allows user to digitally sign the target objects in a workflow.
             


             Note:

             The Teamcenter session should be configured with HTTPS as the password in the input
             structure is not encrypted.
             

             Following actions are supported on EPMTask.
             


Assign
             
Start
             
Complete
             
Skip
             
Suspend
             
Resume
             
Undo
             
Perform
             
Approve
             
Reject
             
Promote
             
Demote
             
Claim
             



             Following action is supported on Signoff.
             


Assign
             


             This action will delegate a Signoff to a different GroupMember or ResourcePool
             and records the comments supplied while performing delegate operation in the audit
             log. User may use workflowService.getResourcePool method To get the ResourcePool
             business object from only group or only role or both.
             

Use Cases:

Use Case 1: User can perform a workflow task.

Description: User can perform an EPMTask from worklist folder in rich
             or thin client. Similarly EPMTask can be performed or signed-off using office
             client as well. This operation can be used to perform or signoff the workflow tasks.
             

Use Case 2: User can assign or delegate a Signoff to a different GroupMember or
             ResourcePool and provide optional comments while performing delegate operation.

Description: When a user delegates a Signoff to a different GroupMember
             or ResourcePool,  the comments provided while performing delegate operation
             gets recorded in the audit log.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Input: 
                         A list of PerformActionInputInfo structure which contains clientId, the <b>EPMTask</b>
                         or <b>Signoff</b> business object, action to be performed on an <b>EPMTask</b> or
                         <b>Signoff</b>, the password for a secure Task, supportingValue which can be used
                         to send in decision value or result, supporting object which can be a <b>User</b>
                         or a <b>ResourcePool</b> business object and the NameValuePair which is a map of
                         property name and values that will contain all property names and corresponding string
                         values that needs to be saved  on an input business object.
             
        :return: 330001(error)Â Â Â Â : Internal error occurred during this operation.
        """
        ...
    def SetActiveSurrogate(self, Input: list[Teamcenter.Services.Strong.Workflow._2014_06.Workflow.SetActiveSurrogateInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets/unsets the logged in user as an active surrogate on a given EPMTask
             or Signoff. It transfers checkout of the target object(s) to/from the logged
             in user from/to the original user.
             

Use Cases:

Use Case 1: User can Stand In for an EPMTask or Signoff with
             Transfer Check-Out(s).
             
Description: When a user is set as a surrogate and wants to perform received
             task in the original user's inbox while allowing the original user to retain control,
             user can Stand-In for the EPMTask or Signoff. The transfer of checkout
             of the target object(s) from the original user is done when the boolean input parameter
             transferCheckouts is set to true.
             

Use Case 2: User is released from EPMTask or Signoff with Transfer
             Check-Out(s).
             
Description: Releases current user as an active surrogate for a EPMTask
             or Signoff. The transfer of checkout of the target object(s) from the current
             user to the original user is done when the boolean input parameter transferCheckouts
             is set to true.
             

Use Case 3: User can Stand-In for an EPMTask or Signoff without
             Transfer Check-Out(s).
             
Description: When a user is set as a surrogate and wants to perform the task
             in the original user's inbox while allowing the original user to retain control,
             user can Stand-In for the EPMTask or Signoff. The target object(s)
             will remain checked out to the original user if they were checked out before the
             Stand-In operation was performed.
             

Use Case 4: User is released for EPMTask or Signoff without
             Transfer Check-Out(s).
             
Description: Releases current user as an active surrogate for an EPMTask
             or Signoff. The target object(s) will remain checked out to the current user
             if the transfer of checkout(s) was done while Stand-In operation was performed.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Input: 
                         A list of SetActiveSurrogateInputInfo structure which contains the <b>EPMTask</b>
                         or <b>Signoff</b> business object, boolean to indicate the Stand-In or Release operation
                         and the boolean to indicate if the checkout of the target objects(s) should be transferred
                         or not.
             
        :return: 
        """
        ...
    def SetSurrogate(self, Requests: list[Teamcenter.Services.Strong.Workflow._2014_06.Workflow.SurrogateInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets or unsets the surrogate resource for a given User effective for
             a given date range.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Requests: 
                         A list of SurrogateInput structures which contain the original User, the surrogate
                         User, effective start date, and the end date.
             
        :return: 219021: Start date cannot be later than end date. Please set start date again.
        """
        ...
    def PerformActionWithSignature(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Action: str, Comments: str, Password: str, SupportingValue: str, SupportingObject: Teamcenter.Soa.Client.Model.ModelObject, Signatures: list[Teamcenter.Services.Strong.Workflow._2014_06.Workflow.ApplySignatureInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation performs an action on workflow task. The following actions are supported.
             


Assign
             
Start
             
Complete
             
Skip
             
Suspend
             
Resume
             
Undo
             
Perform
             
Approve
             
Reject
             
Promote
             
Demote
             
Claim
             



Use Cases:

             User can perform a workflow task from worklist folder in rich or thin client. Similarly,
             workflow tasks
             
             can be performed or signed-off using office client as well.This operation can be
             used to perfrom or sign-off the workflow tasks.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Task: 
                         Workflow task on which the action needs to be performed
             
        :param Action: 
                         Â Â Â Â 
             
        :param Comments: 
                         A comment assigned to this task action. This may be an empty string.
             
        :param Password: 
                         The password for secure task. The value of this parameter is ignored for non-secured
                         tasks.
             
        :param SupportingValue: 
                         Â Â Â Â 
             
        :param SupportingObject: 
                         If the action is assign, provide a user or resource pool to assign the task. If the
                         task is perform-signoff task, provide the Signoff object to set the decision. If
                         the task is a perform-signoff task and the action is claim, provide the signoff object
                         to be claimed.
             
        :param Signatures: 
                         List of ApplySignatureInput objects, each representing target object and its corresponding
                         Base64 string.
             
        :return: 
        """
        ...
    def SetOutOfOffice(self, FromResource: Teamcenter.Soa.Client.Model.Strong.User, ToResource: Teamcenter.Soa.Client.Model.ModelObject, StartDate: System.DateTime, EndDate: System.DateTime) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets/unsets Out of Office resource for a given user. The Out of Office
             resource can be a User or a ResourcePool. The Out of Office setting
             is effective for the specified date range.
             

Use Cases:

Use Case 1: User sets Out of Office
             
Description: When a user is going to be out of the office and wants to have
             someone receive the tasks during his/her absence then user sets Out of Office. If
             the end date is not provided then all the future tasks will be delegated indefinitely.
             

Use Case 2: System Administrator sets Out of Office for another user
             
Description: When a user is out of the office but does not have Out of Office
             setting then System Administrator can set Out of Office for the user. Also, group
             administrators will only be able to set the Out of Office for users within their
             group.
             

Use Case 3:  User modifies Out of Office settings
             
Description: When a user has set Out of Office and during this period if the
             Out of Office resource is also going to be out of the office then System Administrator
             can modify the Out of Office settings of the user
             

Use Case 4:  User unsets Out of Office settings
             
Description: When a user who has set Out of Office is back before the specified
             end date then he/she can unset the current Out of Office setting. The startDate and
             endDate parameters will be set to null and the toResource paramenter will be set
             to an empty object.
             


Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param FromResource: 
                         The <b>User</b> for whom the Out of Office will be set/unset.
             
        :param ToResource: 

        :param StartDate: 
                         The effective start date of the Out of Office setting.
             
        :param EndDate: 
                         The effective end date of the Out of Office setting.  Set to null (for C++ use DateTime::getNullDate())
                         to set the Out of Office to be indefinite (no end).
             
        :return: 219027: The user is out of the office starting from date. Please select another user
             for these dates.
        """
        ...
    def CreateWorkflow(self, Input: Teamcenter.Services.Strong.Workflow._2014_10.Workflow.CreateWkfInput) -> Teamcenter.Services.Strong.Workflow._2014_10.Workflow.CreateWkfOutput:
        """    
             This operation creates a workflow process given the  process template name, workflow
             owner, responsible party, attachments and attachment types.
             

Use Cases:

             Any client can use this operation to create a workflow process in Teamcenter given
             the process template name, workflow owner and the responsible party.  It can also
             provide the attachments to attach to the workflow process. For Example:  Teamcenter
             Integration Framework can call this operation by providing the process template name,
             workflow owner, responsible party, attachments, attachment types.  Workflow process
             will be created using the given workflow template. The responsibly party and the
             workflow owner will be assigned to the root task. The attachments will be attached
             using the given attachment relation types.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Input: 
                         The process name, process template name, workflow process owner, responsible party,
                         assignees, due date, attachments, and attachment relations.
             
        :return: Structure of type CreateWkfOutput containing the UID of a Workflow root task, a NameValuePairs
             data type that holds root task property names and values, and service data.
        """
        ...
    def CreateOrUpdateHandler(self, Input: list[Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateUpdateHandlerInput]) -> Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateOrUpdateHandlerResponse: ...
    def CreateOrUpdatePAL(self, Input: list[Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateUpdatePALInput]) -> Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateOrUpdatePALResponse: ...
    def CreateOrUpdateTemplate(self, Input: list[Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateUpdateTemplateInput]) -> Teamcenter.Services.Strong.Workflow._2019_06.Workflow.CreateOrUpdateTemplateResponse: ...
    def GetRegisteredHandlers(self) -> Teamcenter.Services.Strong.Workflow._2019_06.Workflow.GetRegisteredHandlerResponse:
        """    
             This operation returns the list of names of registered workflow handlers. The names
             returned by this operation  are used as an input for creating the handler instance(s).
             

Use Cases:

             In Active Workspace Client, this operation will be used in a Workflow Designer sub-location
             for following cases:
             

             1.    Creating a new workflow handler instance (EPMHandler) for
             specified workflow template (EPMTaskTemplate). Here user will use the name of the
             handler (shown as the dropdown list) returned from this service operation.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :return: 
        """
        ...
    def GetSupportedHandlerArguments(self, Input: list[Teamcenter.Services.Strong.Workflow._2020_01.Workflow.SupportedHandlerArgumentsInput]) -> Teamcenter.Services.Strong.Workflow._2020_01.Workflow.SupportedHandlerArgumentsReponse: ...

