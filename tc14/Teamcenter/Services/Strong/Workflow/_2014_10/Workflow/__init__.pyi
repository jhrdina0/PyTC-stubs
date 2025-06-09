import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateRemoteWkfInput:
    """
    
A structure containing information used for workflow replication (e.g. the name
of
the process template, workflow owner, responsible party, export site,
attachments,
and attachment relations).
    """
    def __init__(self, ) -> None: ...
    ProcessName: str
    """Workflow process name."""
    ProcessDescription: str
    """Workflow process description."""
    ProcessTemplate: str
    """
            Name of the workflow process template used for creating the workflow process. This
            template should exist at the site where the workflow is created.
            """
    WorkflowOwner: Teamcenter.Soa.Client.Model.Strong.User
    """Owner of the workflow process."""
    ResponsibleParty: Teamcenter.Soa.Client.Model.ModelObject
    """Responsible party (Users or ResourcePool) of the root task."""
    AssignedUserList: list[str]
    """Users or ResourcePool objects to be used for task assignment."""
    DueDate: System.DateTime
    """The due date of the source object (e.g. Schedule Task)."""
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    """Source object (e.g. ScheduleTask)."""
    Site: Teamcenter.Soa.Client.Model.Strong.POM_imc
    """The site where the workflow needs to be created."""
    Attachments: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of attachments to the workflow process (e.g. ItemRevision, Dataset)."""
    AttachmentRelationTypes: list[str]
    """
            A list of relation type names to use while attaching the attachments to the workflow
            process (e.g. CMHasProblemItem, CMHasSolutionItem, Fnd0EPMTarget).
            """

class CreateWkfInput:
    """
    
A structure containing the process template name ,workflow process owner,
responsible
party, attachments, and attachment relations. Intent of structure is to hold
input
data that is required to create a workflow process.
    """
    def __init__(self, ) -> None: ...
    ProcessName: str
    """Workflow process name."""
    ProcessDescription: str
    """Workflow process description (Optional)."""
    ProcessTemplate: str
    """Name of the workflow process template used for creating the workflow process."""
    WorkflowOwner: Teamcenter.Soa.Client.Model.Strong.User
    """User assigned as the owner of the workflow process."""
    ResponsibleParty: Teamcenter.Soa.Client.Model.ModelObject
    """
            Responsible party of the workflow process root task. Responsible party can be a User
            or a ResourcePool.
            """
    AssignedUserList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of Users or ResourcePool objects  to be used for task assignment (Optional)."""
    DueDate: System.DateTime
    """Task due date (Optional)."""
    Attachments: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of attachments to the workflow process (e.g. ItemRevision, Dataset) (Optional)."""
    AttachmentRelationTypes: list[str]
    """
            A list of relation type names to use while attaching the attachment objects to the
            workflow process (e.g. CMHasProblemItem, CMHasSolutionItem, Fnd0EPMTarget) (Optional).
            """

class CreateWkfOutput:
    """
    
A structure containing the UID of the workflow root task, a NameValuePairs data
type
that holds root task property names and values, and service data. Intent of
structure
is to be an output parameter used to hold data pertaining to a newly created
workflow
process following the creation of the workflow process.
    """
    def __init__(self, ) -> None: ...
    WorkflowTask: Teamcenter.Soa.Client.Model.ModelObject
    """Workflow root task."""
    Attributes: System.Collections.Hashtable
    """
            A map (string/string) of workflow root task property names and values. (e.g. status,
            process instructions, task_result).
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data."""

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateWorkflow(self, Input: CreateWkfInput) -> CreateWkfOutput:
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

