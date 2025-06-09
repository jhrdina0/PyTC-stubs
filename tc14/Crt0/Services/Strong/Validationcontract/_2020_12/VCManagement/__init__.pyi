import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddObjectInput:
    """
    
            Structure representing the objects to add and its parameters to the Verification
            Request.
            
    """
    def __init__(self, ) -> None: ...
    ObjectToBeAdded: Teamcenter.Soa.Client.Model.ModelObject
    """The object  (BOMLine or WorkspaceObject) that is to be added."""
    ChildPathObjectToBeAdded: str
    """
            PS Occurrence Thread child path. If objectToBeAdded is empty, object determined
            from childPathObjectToBeAdded will be added to Verification Request. System
            considers either objectToBeAdded or childPathObjectToBeAdded to add
            to Verification Request. childPathObjectToBeAdded works on existing BOM window
            in system. The BOM window must be available in system to determine and add object
            to Verification Request.
            """
    ContextForObjectToBeAdded: Teamcenter.Soa.Client.Model.ModelObject
    """
            The context (BOMLine) in which Tracelink is to be created. This is
            required when objectToBeAdded is of type BOMLine, and ignored when
            objectToBeAdded is of type WorkspaceObject.
            """
    ChildPathContextToBeAdded: str
    """
            PS Occurrence Thread child path. If contextForObjectToBeAdded is empty, context
            of objectToBeAdded will be determined from childPathContextToBeAdded.
            System considers either contextForObjectToBeAdded or childPathContextToBeAdded
            as context. childPathContextToBeAdded works on existing BOM window in system.
            The BOM window must be available in system to determine and add object to Verification
            Request.
            """
    AdditionalProps: System.Collections.Hashtable
    """Additional properties for objectToBeAdded."""
    Parameters: list[ParameterInfo]
    """
            A list of ParameterInfo structure. Represents parameter and parameter direction
            of content to be set to Verification Request object. If empty, system adds all associated
            parameters of content to Verification Request object.
            """

class CreateVerificationRequestData:
    """
    Structure represents created Verification Request object and related data.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            This unique Id is used to identify return data elements and partial errors associated
            with this input structure.
            """
    VerificationRequest: Teamcenter.Soa.Client.Model.Strong.Crt0VldnContractRevision
    """Created Verification Request Object."""
    Elements: list[ElementData]
    """
            A List of ElementData structure. Represents details of elements of Verification
            Request Object.
            """

class RecipeData:
    """
    Structure represents Information about recipe to be executed on the given content.
    """
    def __init__(self, ) -> None: ...
    RecipeName: str
    """Name of the Fnd0Recipe object to be executed for the given content."""
    RecipeUid: str
    """The Fnd0Recipe object UID to be executed for the given content."""
    BomWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]
    """
            A list of optional BOMWindow objects to which qualified business objects are
            resolved.
            """

class CreateVerificationRequestInputData:
    """
    
            Structure required to create Verification Request with given Verification Request
            content.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    VerificationRequestName: str
    """
            Verification Request object name. It is mandatory input to create Crt0VldnContractRevision
            object.
            """
    VerificationRequestType: str
    """
            Verification Request object type. Valid types are Crt0VldnContractRevision
            and its sub-types
            """
    VerificationRequestDefinition: Teamcenter.Soa.Client.Model.Strong.Crt0VldnContractRevision
    """
            Optional Crt0VCDefnRevision object. If not empty , system sets given Verification
            Definition Revision to created  Verification Request object. If empty, Verification
            Definition Revision information will be empty for created  Verification Request object.
            """
    ReviseVerificationRequestRevision: Teamcenter.Soa.Client.Model.Strong.Crt0VldnContractRevision
    """
            Existing Crt0VldnContractRevision Verification Request Object. If not empty,
            system performs Revise operation on existing Verification Request and adds given
            input objects to revised Verification Request object.  If empty, system creates new
            Verification Request object and adds given input objects.
            """
    VerificationRequestContent: list[AddObjectInput]
    """
            A list of AddObjectInput structure. Represents content and parameters details
            to add to Verification Request Object.
            """
    CreateParameterCopyOptions: str
    VerificationRequestProps: System.Collections.Hashtable
    """Additional properties to set on Verification Request object."""
    RecipeData: RecipeData
    """
            The recipe to be executed on given verificationRequestContent content . The
            results are added to the Verification Request.
            """
    Participants: list[ParticipantInfo]
    WorkflowNameToInitiate: str
    PopulateFromParent: bool
    """
            If true, created Verification Request is populated from given parentVerificationRequest
            parent  content. If false, content of parentVerificationRequest parent will
            not be populated to created Verification Request.
            """
    ParentVRObject: Teamcenter.Soa.Client.Model.Strong.Crt0VldnContractRevision
    """
            Parent Verification Request Object for creating sub-type of Verification Request
            object. It is mandatory only for creation of sub-types of Verification Request object.
            """

class CreateVerificationRequestResponse:
    """
    Structure represents created Verification Request object details.
    """
    def __init__(self, ) -> None: ...
    VerificationRequestData: list[CreateVerificationRequestData]
    """A list of CreateVerificationRequestData structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data with partial errors for createVerificationRequest operation."""

class ElementData:
    """
    Details of Verification Request content object.
    """
    def __init__(self, ) -> None: ...
    Element: Teamcenter.Soa.Client.Model.ModelObject
    """Verification Reequest content object."""
    Parameters: list[ParameterData]
    """
            A list of ParameterData structure. Represents details of parameters of Verification
            Request Object.
            """

class ParameterData:
    """
    Structure represents parameter data of created Verification Request object.
    """
    def __init__(self, ) -> None: ...
    Parameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """Att0MeasurableAttribute object associated with Verification Request."""
    Direction: str

class ParameterInfo:
    """
    
            Structure representing the Parameter to add to the Verification Request for the given
            object.
            
    """
    def __init__(self, ) -> None: ...
    Parameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """
            This Att0MeasurableAttribute object to be added to Verification Request as
            Input or Output for the objectToBeAdded in AddObjectInput.
            """
    Direction: str

class ParticipantInfo:
    """
    Structure representing the Participant to add to Verification Request object.
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The User object to be added as Participant to Verification Request."""
    Role: str

class VCManagement:
    """
    Interface VCManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateVerificationRequest(self, Input: list[CreateVerificationRequestInputData]) -> CreateVerificationRequestResponse: ...

