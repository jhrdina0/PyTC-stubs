import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetWorkflowTemplatesInputInfo:
    """
    Structure to define input for workflow Templates
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    IncludeUnderConstruction: bool
    """
            If set to true, the operation will return Under construction templates for administrative
            users only.  Otherwise only available workflow templates are returned.
            """
    GetFiltered: bool
    """
            If set to true, the operation will return assigned or filtered list of workflow templates
            based on Target Objects and Object Types.
            """
    TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """List of target objects to be used for getting the filtered list of workflow templates."""
    ObjectTypes: list[str]
    """
            List of target object types to be used for getting the filtered list of workflow
            templates. This argument is not required if targetObjects are specified.
            """
    Group: str
    """User group to get the filtered list of  workflow templates."""

class GetWorkflowTemplatesOutput:
    """
    Structure to define output for workflow Templates
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    WorkflowTemplates: list[Teamcenter.Soa.Client.Model.Strong.EPMTaskTemplate]
    """A list of output workflow Templates."""

class GetWorkflowTemplatesResponse:
    """
    Structure to define response for workflow Templates
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData contains any partial errors."""
    TemplatesOutput: list[GetWorkflowTemplatesOutput]
    """Complete list of workflow Templates Output."""

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetWorkflowTemplates(self, Input: list[GetWorkflowTemplatesInputInfo]) -> GetWorkflowTemplatesResponse:
        """    
             This operation gets the list of workflow templates based on input criteria. The criteria
             includes the target objects for the workflow or the types of the target objects.
             User can also specify if the under construction templates should to be returned and
             if the filtered list of templates is required. The filtered list of templates are
             returned based on the users group and the target objects. The filter rules can also
             be customized using the user exits.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Input: 
                         Structure to define input for workflow Templates.
             
        :return: This operation returns the list of workflow templates based on the input criteria
             and ServiceData structure containing errors if any.
        """
        ...

