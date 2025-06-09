import System
import System.Collections
import Teamcenter.Services.Strong.Workflow._2008_06.Workflow
import Teamcenter.Soa.Client.Model
import typing

class CreateOrUpdateHandlerResponse:
    """
    Response of createOrUpdateHandler operation.
    """
    def __init__(self, ) -> None: ...
    CreatedorUpdatedObjects: list[CreateUpdateHandlerOutput]
    """A list of CreateUpdateHandlerOutput structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class CreateOrUpdatePALResponse:
    """
    Response structure returned by createOrUpdatePAL operation.
    """
    def __init__(self, ) -> None: ...
    CreatedorUpdatedObjects: list[CreateUpdatePALOutput]
    """A list of CreateUpdatePALOutput structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class CreateOrUpdateTemplateResponse:
    """
    Response of createOrupdate operation.
    """
    def __init__(self, ) -> None: ...
    CreatedorUpdatedObjects: list[CreateUpdateTemplateOutput]
    """A list of CreateUpdateTemplateOutput structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class CreateUpdateHandlerInput:
    """
    Input structure to pass requried data for create or update handler.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    HandlerName: str
    TaskTemplate: str
    """UID of EPMTaskTemplate object on which handler is to be created or updated."""
    BusinessRule: str
    HandlerType: str
    HandlerToUpdate: str
    """
            UID of the EPMHandler object to be updated. If this  input is provided then it will
            be considered as update case.
            """
    Action: int
    """
            The action of the workflow task on which new handler will be added. Required for
            create.
            
            Supported values are:
            
            Action    Value
            
            Assign          1
            
            Start              2
            
            Complete  4
            
            Promote      5
            
            Suspend      6
            
            Resume      7
            
            Undo          8
            
            Abort          9
            
            Perform     100
            """
    RuleQuorum: int
    """
            The rule quorum value to specify whether one rule, all rules, or a number of rules
            must be satisfied for the task to progress. Below are the accepted values :
            
            -1 :  means all. In this case, every rule must pass to meet the quorum.
            
            A number greater than 1, but less than the number of already added Rule handler in
            the Rule container. Any invalid input will be ignored.
            """
    ChangeExecutionOrder: int
    """
            The position of the handler in added handler(s) array on particularaction of the
            EPMTaskTemplate. For example specifying the -1 position moves the given handler (handlerToUpdate
            input) up in a handler array. Similarly specifying the 1 position moves the given
            handler down in a handler array. Any invalid input will be ignored.
            """
    AdditionalData: System.Collections.Hashtable

class CreateUpdateHandlerOutput:
    """
    Structure represents the output of createOrUpdateHandler operation.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify  return data
            elements and partial errors associated with the input  structure.
            """
    HandlerObject: Teamcenter.Soa.Client.Model.ModelObject
    """Updated or created EPMHandler object."""
    RuleObject: Teamcenter.Soa.Client.Model.ModelObject
    """Updated or created EPMBusinessRule object."""

class CreateUpdatePALInput:
    """
    
Input stucture used to update or copy EPMAssignmentList or to create a new
EPMAssignmentList.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PalName: str
    """
            Name of the EPMAssignmentList to be updated or newly created . In case of
            copy operation, this is the name of new EPMAssignmentList to be created.
            """
    WorkflowTemplate: str
    """
            UID of EPMTaskTemplate object for which process assignment list is to be created
            or updated or copied.
            """
    PalDescription: list[str]
    """Description of process assignment list."""
    ResourceLists: list[Teamcenter.Services.Strong.Workflow._2008_06.Workflow.Resources]
    """A list of Resources to be assigned."""
    AdditionalData: System.Collections.Hashtable

class CreateUpdatePALOutput:
    """
    CreateUpdatePALOutput structure.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PalObject: Teamcenter.Soa.Client.Model.ModelObject
    """Updated or created EPMAssignmentList object."""

class CreateUpdateTemplateInput:
    """
    Input structure used for passing requried data for create or update template
object.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    TemplateName: str
    """Name of the task template to be created or updated."""
    TemplateDesc: str
    """Description of the task template to be created or updated."""
    BaseTemplate: str
    """
            UID of EPMTaskTemplate object which will be used as a base template.Basically new
            template to be created will be a exact copy of this template. This is requried for
            create operation.
            """
    ParentTemplate: str
    """
            UID of EPMTaskTemplate object represents the parent object. New template will be
            created as a child or sub template of this parent template input. This is requried
            for create operation.
            """
    TemplateToUpdate: str
    """
            UID of the EPMTaskTemplate object to be updated. If this input is provided then this
            operation will be considered as update case.
            """
    AdditionalData: System.Collections.Hashtable
    """
            A map (string, list of strings) to send additional data. This input is reserverd
            for future use.
            """

class CreateUpdateTemplateOutput:
    """
    Struture holds the created or updated template object.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with the input structure.
            """
    TemplateObject: Teamcenter.Soa.Client.Model.ModelObject
    """Updated or created EPMTaskTemplate object."""

class GetRegisteredHandlerResponse:
    """
    Returns list of registered action and rule handler names.
    """
    def __init__(self, ) -> None: ...
    ActionHandlers: list[str]
    """A list of names of registered action handlers."""
    RuleHandlers: list[str]
    """A list of names of registered rule handlers."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateHandler(self, Input: list[CreateUpdateHandlerInput]) -> CreateOrUpdateHandlerResponse: ...
    def CreateOrUpdatePAL(self, Input: list[CreateUpdatePALInput]) -> CreateOrUpdatePALResponse: ...
    def CreateOrUpdateTemplate(self, Input: list[CreateUpdateTemplateInput]) -> CreateOrUpdateTemplateResponse: ...
    def GetRegisteredHandlers(self) -> GetRegisteredHandlerResponse:
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

