import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssignmentLists:
    """
    Process Assignment Lists
    """
    def __init__(self, ) -> None: ...
    AssignedLists: list[Teamcenter.Soa.Client.Model.Strong.EPMAssignmentList]
    """assignedLists"""
    OwnedLists: list[Teamcenter.Soa.Client.Model.Strong.EPMAssignmentList]
    """ownedLists"""
    GroupLists: list[Teamcenter.Soa.Client.Model.Strong.EPMAssignmentList]
    """groupLists"""
    OtherLists: list[Teamcenter.Soa.Client.Model.Strong.EPMAssignmentList]
    """otherLists"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data - returns index of the input vector if call on that fails"""

class AttachmentInfo:
    """
    Structure containing list of attachments and the attachment types
    """
    def __init__(self, ) -> None: ...
    Attachment: list[Teamcenter.Soa.Client.Model.ModelObject]
    """attachment"""
    AttachmentType: list[int]
    """attachmentType"""

class AuditFile:
    """
    Audit files
    """
    def __init__(self, ) -> None: ...
    AuditFiles: list[str]
    """auditFiles"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class ChangeStateInputInfo:
    """
    Input to changeState operation
    """
    def __init__(self, ) -> None: ...
    State: str
    """state"""
    RemoteProcessID: str
    """remoteProcessID"""

class ChangeStateOutput:
    """
    ChangeState operation output
    """
    def __init__(self, ) -> None: ...
    State: str
    """state"""
    RemoteProcessID: str
    """remoteProcessID"""
    ParentProcessID: str
    """parentProcessID"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class ContextData:
    """
    
Context-specific data required to create a process or a sub process at a local
or
a remote site.  Except the process template, the rest of the elements in the
context
data is optional. The optional elements        that are currently supported are
attachmentCount,attachments,attachmentTypes
and processAssignmentList.  The rest of the optional elements are defined to
support
future workflow enhancements.
    """
    def __init__(self, ) -> None: ...
    ProcessTemplate: str
    """Name of the process template.  must be a valid, existing process template"""
    ProcessOwner: str
    """Login id of the process owner. supported in future"""
    AttachmentCount: int
    """
            Count of attachment objects consisting of including both target        and reference
            attachments. If count is less than 1, no attachments are added
            """
    Attachments: list[str]
    """
            List of atachments representing either target or reference objects that will be added
            at process creation time. List may consist of target attachments or reference attachments
            or a mixture of both. If NULL, no attachments are added
            """
    AttachmentTypes: list[int]
    """
            Identifies the types of attachments listed in attachment.  Valid types include EPM_target_attachment
            (target attachment) and EPM_reference_attachment (reference attachment). There is
            a one-to-one correspondence between the attachment types on this list and the list
            of attachments.
            """
    DeadlineDate: System.DateTime
    """
            A date in the form of yyyy-mm-dd hh-mm-ss GMT that will be applied as a due date
            for the processes. If GMT is not specified then the time will be interpreted as based
            on the local time zone of the server. If NULL or invalid date, no due date is applied.
            supported in future
            """
    Container: str
    """
            Identifies the object to which the processes should be attached using the relation_type
            specified. supported in future
            """
    RelationType: str
    """
            The name of the relation. If NULL, the default relation type for the container object
            will be used. supported in future
            """
    ProcessAssignmentList: str
    """Name of the process assignment list"""
    ProcessResources: list[str]
    """
            A list of comma-separated user login IDs that will be used to satisfy signoff profiles
            for each individual task. Any users that do not match a signoff profile within a
            task will be added as an adhoc user. supported in future
            """
    DependencyTask: str
    """
            The path to the dependency task. This will be used to determine the dependency tasks
            in the processes that need to be returned in response.   The full path to the task
            in the template needs to be specified, e.g.       CMII Change Notice: Change Admin
            II (CN). supported in future
            """
    SubscribeToEvents: bool
    """
            The flag to indicate if the observer needs to be notified about events that occur
            on the processes and the dependency tasks in the processes. supported in future
            """
    SubscriptionEventCount: int
    """Number of events to subscribe to"""
    SubscriptionEventList: list[str]
    """
            List of events for which subscription objects will be created so that the observer
            is notified when these events occur on the process and /or process dependency task.
            supported in future
            """
    RemoteParent: str
    """URI of the observer in the remote application. supported in future"""
    RemoteParentAppguid: str
    """
            The Application ID of the application in which the observer resides. supported in
            future
            """
    RemoteParentUrl: str
    """The URL to the observer. supported in future"""

class CreateSignoffInfo:
    """
    Structure containing information to add adhoc signoff or add signoff based on a
profile
    """
    def __init__(self, ) -> None: ...
    SignoffMember: Teamcenter.Soa.Client.Model.ModelObject
    """signoffMember"""
    Origin: Teamcenter.Soa.Client.Model.ModelObject
    """origin"""
    SignoffAction: str
    """signoffAction"""
    OriginType: str
    """originType"""

class CreateSignoffs:
    """
    Structure containing information to add adhoc signoff or add signoff based on a
profile
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.EPMTask
    """task"""
    SignoffInfo: list[CreateSignoffInfo]
    """signoffInfo"""

class DefinitionInfo:
    """
    Structure containing process template information
    """
    def __init__(self, ) -> None: ...
    Definitionkey: str
    """unique identifier of the process template"""
    Name: str
    """name of the process template"""
    Description: str
    """description of the process template"""
    Version: str
    """version of the process template"""
    Status: int
    """
            status of the process template. The values are 0 -obsolete,1 - under construction,
            2- ready for use
            """

class GetResourcePoolOutput:
    """
    Structure containing the Resource Pool matching the GroupRoleRef and the
ServiceData
    """
    def __init__(self, ) -> None: ...
    ResourcePoolInfo: list[ResourcePoolInfo]
    """resourcePoolInfo"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class GroupRoleRef:
    """
    Structure containing the group and role info
    """
    def __init__(self, ) -> None: ...
    GroupTag: Teamcenter.Soa.Client.Model.Strong.Group
    """groupTag"""
    RoleTag: Teamcenter.Soa.Client.Model.Strong.Role
    """roleTag"""
    AllowSubGroup: int
    """allowSubGroup"""
    IsAllMembers: int
    """isAllMembers"""

class InstanceInfo:
    """
    Structure containing information related to the new process
    """
    def __init__(self, ) -> None: ...
    InstanceKey: str
    """instanceKey. supported in future"""
    NewProcessDepTask: str
    """newProcessDepTask. supported in future"""
    NewProcessUrl: str
    """newProcessUrl. supported in future"""
    NewProcessDepTaskUrl: str
    """newProcessDepTaskUrl. supported in future"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData containing the created process and errors if any"""

class ProcessTemplates:
    """
    Process templates
    """
    def __init__(self, ) -> None: ...
    Output: list[DefinitionInfo]
    """vector of DefinitionInfo objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data contains any partial errors."""

class RemoveSignoffsInfo:
    """
    Structure containing signoffs to be removed
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.EPMTask
    """task"""
    RemoveSignoffObjs: list[Teamcenter.Soa.Client.Model.Strong.Signoff]
    """removeSignoffObjs"""

class ResourcePoolInfo:
    """
    Structure containing resource pool , group and role info
    """
    def __init__(self, ) -> None: ...
    GroupRoleRef: GroupRoleRef
    """groupRoleRef"""
    ResourcePoolTag: Teamcenter.Soa.Client.Model.Strong.ResourcePool
    """resourcePoolTag"""

class Resources:
    """
    Structure containing the task template and the resources to be applied to the
template
    """
    def __init__(self, ) -> None: ...
    TaskTemplate: Teamcenter.Soa.Client.Model.Strong.EPMTaskTemplate
    """taskTemplate"""
    TemplateResources: list[Teamcenter.Soa.Client.Model.ModelObject]
    """templateResources"""
    Profiles: list[Teamcenter.Soa.Client.Model.Strong.EPMSignoffProfile]
    """profiles"""
    Actions: list[int]
    """actions"""
    RevQuorum: int
    """revQuorum"""
    AckQuorum: int
    """ackQuorum"""

class Tasks:
    """
    Structure containing all the tasks in a process
    """
    def __init__(self, ) -> None: ...
    AllTasks: list[Teamcenter.Soa.Client.Model.Strong.EPMTask]
    """allTasks"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data contains any partial errors."""

class Templates:
    """
    structure containing workflow templates
    """
    def __init__(self, ) -> None: ...
    WorkflowTemplates: list[Teamcenter.Soa.Client.Model.Strong.EPMTaskTemplate]
    """workflowTemplates"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data contains any partial errors."""

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddSignoffs(self, Signoffs: list[CreateSignoffs]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             addSignoffs : Add signoffs on a task.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Signoffs: 
                         vector of CreateSignoffs - structure containing the task tag and vector of CreateSignoffInfo
                         Description: CreateSignoffInfo structure contains information to add adhoc signoff
                         or add signoff based on a profile Case of Adhoc signoff:this is used for the case
                         of adhoc signoff : Provide signoffMember can be group member(user), resource pool
                         or address list(complete address list) tags : In this profile /subset of addresslist
                         will be empty. So there is no need to provide origin and origintype. Can pass a null
                         and 0 respectively. : Provide the signoffAction. Case of profile :this is used when
                         a signoff member is being added to satisfy a signoff profile : Provide the signoff
                         member : Provide the origin which will be the signoff profile object associated with
                         the signoff member : Provide the originType as SOA_EPM_SIGNOFF_ORIGIN_PROFILE Case
                         of subset of address list : this is used when only a particular member of an addresslist
                         needs to be added as a signoff. : Provide the signoff member : Provide the origin
                         which will be the address list object associated with the signoff member : Provide
                         the originType as SOA_EPM_SIGNOFF_ORIGIN_ADDRESSLIST
             
        :return: 
        """
        ...
    def ChangeState(self, StateInput: ChangeStateInputInfo) -> ChangeStateOutput:
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
    def CreateInstance(self, StartImmediately: bool, ObserverKey: str, Name: str, Subject: str, Description: str, ContextData: ContextData) -> InstanceInfo:
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
    def GetAssignmentLists(self, Names: list[str]) -> AssignmentLists:
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
    def GetResourcePool(self, GroupRoleRef: list[GroupRoleRef]) -> GetResourcePoolOutput:
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
    def ListDefinitions(self, Name: str, Templatestatus: int) -> ProcessTemplates:
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
    def RemoveSignoffs(self, Signoffs: list[RemoveSignoffsInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def ViewAuditFile(self, AuditedObject: Teamcenter.Soa.Client.Model.ModelObject, IsSignoffReport: bool) -> AuditFile:
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
    def AddAttachments(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Attachments: AttachmentInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def AssignAllTasks(self, Process: Teamcenter.Soa.Client.Model.Strong.EPMJob, AssignmentList: Teamcenter.Soa.Client.Model.Strong.EPMAssignmentList, Resources: list[Resources]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def GetAllTasks(self, Process: Teamcenter.Soa.Client.Model.Strong.EPMJob, State: int) -> Tasks:
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
    def GetWorkflowTemplates(self, Targets: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject], AllOrAssignedCriteria: str) -> Templates:
        """    
             Get the list of workflow templates given the list of target workspace objects and
             the All or Assigned criteria.  Description This SOA will return all the ready to
             use and under construction templates if the allorAssined criteria is SOA_EPM_ALL.
             If the allOrAssignedCriteria is set to SOA_EPM_Assigned, this SOA will get the group
             information and the configured filtering criteria from the session and using the
             list of target objects, return the filtered list of workflow templates.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Targets: 
                         list of target objects to get the workflow templates for
             
        :param AllOrAssignedCriteria: 
                         criteria to get all the templates or assigned templates.
             
        :return: Templates
        """
        ...
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

