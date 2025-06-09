import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Attribute:
    """
    Structure that contains weld feature attribute name and list of attribute
values.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Attribute name of weld feature."""
    Values: list[str]
    """List of values for the weld feature attribute."""

class CreateWeldInput:
    """
    
Structure that represents weld components and weld features input. Client
application
should retrieve all weld components and weld features under parent node.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    ParentBvr: Teamcenter.Soa.Client.Model.ModelObject
    """
            Parent node BVR. Parent node must be provided so that the created bom window contains
            weld components as well as connection parts.
            """
    WeldComps: list[WeldCompWithFeatData]
    """List of weld component (with feature data) to be created or updated."""

class CreateWeldOut:
    """
    Structure that represents create weld output. It lists weld component data.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    Welds: list[WeldComp]
    """List of weld components."""

class CreateWeldResp:
    """
    Structure that represents create weld response.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data."""
    Weldouts: list[CreateWeldOut]
    """List of create weld outputs."""

class DeleteWeldInput:
    """
    Structure that represents delete weld component input.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    ParentBvr: Teamcenter.Soa.Client.Model.ModelObject
    """
            Parent node BVR. Parent node should be the work part that when weld component was
            created in NX.
            """
    Comps: list[WeldComp]
    """List of weld components to be deleted."""
    RelType: str
    """
            Type of relation from weld feature object to connection parts. This is needed to
            clean up those relation objects.
            """
    Destroy: bool
    """
            The logical mark to decide if destroy weld components and weld features.True - destroy
            weld components and feature objects from Teamcenter completely; False - remove weld
            components from assembly only.
            """

class DeleteWeldOut:
    """
    Structure that represents delete weld output.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    Message: list[str]
    """
            List of message show weld component id and status of deletion. Format is id - OK
            if component is deleted successfully. Otherwise, it is id - Failed.
            """

class DeleteWeldResp:
    """
    Structure that represents delete weld component response.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data."""
    Results: list[DeleteWeldOut]
    """List of delete weld outputs."""

class FindWeldInput:
    """
    Structure that represents find weld component input.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    AsmWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """
            Assembly bom window. It is not needed when parent BVR is provided. Weld components
            are searched within the bomlines by looking at connection relationships with provided
            connection components. Weld type may be used to further filter out unwanted weld
            components.
            """
    ParentBvr: Teamcenter.Soa.Client.Model.ModelObject
    """Weld component parent BVR."""
    ConnectionParts: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            Connection part PS Occurrences. Connection parts must fall in the bom window that
            created by parent BVR.
            """
    Relation: str
    """
            Connection relation type. For example, weld component and features occurrence are
            related to connection part APN by TC_CONNECT_TO relation.
            """
    WeldTypes: list[str]
    """Weld component types as a filter."""
    ReturnUid: bool
    """
            The logical mark to decide the return data. true - return the uids for occurrence,
            revision and BVR only. false - return objects only.
            """

class FindWeldOut:
    """
    Structure that represents find weld component output.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    Welds: list[WeldComp]
    """List of weld components returned."""

class FindWeldResp:
    """
    Structure that represents find weld component response.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data."""
    Results: list[FindWeldOut]
    """List of find weld component outputs."""

class FormAttributes:
    """
    
Structure that represents form and attributes. Data to create a form and attach
the
form to parent object.
    """
    def __init__(self, ) -> None: ...
    FormType: str
    """Form type."""
    FormName: str
    """Form name."""
    FormRel: str
    """Relation name from parent object to form."""
    Attributes: list[Attribute]
    """List of form attribute name and values."""

class WeldComp:
    """
    Structure that represents weld component data.
    """
    def __init__(self, ) -> None: ...
    CompOcc: Teamcenter.Soa.Client.Model.ModelObject
    """Weld component PS occurrence."""
    CompRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Weld component revision."""
    CompBvr: Teamcenter.Soa.Client.Model.ModelObject
    """Weld component BVR."""
    OccUid: str
    """component Occurrence uid string."""
    RevUid: str
    """Component revision uid."""
    BvrUid: str
    """Component BVR uid."""

class WeldCompWithFeatData:
    """
    
Structure that represents weld component with feature data. The component
occurrence
information must be specified in this call.
    """
    def __init__(self, ) -> None: ...
    UgEntHandle: str
    """Weld component (NX part that contains weld features) UG Entity Handle."""
    CompRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Weld component revision."""
    CompOcc: Teamcenter.Soa.Client.Model.ModelObject
    """Weld component PS Occurrence. The PS occurence must be specified."""
    CompBvr: Teamcenter.Soa.Client.Model.ModelObject
    """Weld component BVR."""
    Features: list[WeldFeature]
    """List of weld features that current weld component defines."""
    RelType: str
    """Type of relation from weld feature object to connection parts."""
    Revise: bool
    """
            The logical mark to decide if revise the weld component.True - current weld component
            is revised or to be revised. False - update weld component.
            """

class WeldFeature:
    """
    
Structure that represents weld feature data. Client application must collect all
features per weld component in current NX session. Server implementation
compares
the features list from input with the one retrieved from weld component
occurrence
in Teamcenter. The features that are missing from input will be removed from
weld
component occurrence children. The features that do not exist in weld component
occurrence
will be created and added as children. Client application should only provide
feature
UG Entity Handle for the features that have not been modified in current NX
session.
Client application should mark the features that are to be revised. Rest of the
features
are assumed to be updated.
    """
    def __init__(self, ) -> None: ...
    UgEntHandle: str
    """
            Feature UG Entity Handle. Weld feature Entity handle must be specified if feature
            exists.
            """
    FeatOcc: Teamcenter.Soa.Client.Model.ModelObject
    """Feature occurrence node in PS. Optional."""
    FeatRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Feature revision object. Optional."""
    RevAttributes: list[Attribute]
    """Feature revision attributes. New value overwrite existing value."""
    RevForms: list[FormAttributes]
    """
            Forms to be created or updated and attached to feature revision. Existing form is
            updated by overwritting attribute values.
            """
    Comps: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of connection parts PS occurrence for current feature."""
    Revise: bool
    """
            The logical mark to decide if revise. True - revise this feature; false - do not
            revise this feature.
            """
    Type: str
    """Feature item type."""
    Name: str
    """Feature item name."""
    Desc: str
    """Feature item description."""
    JtFile: str
    """Feature JT file name."""
    JtTicket: str
    """Feature JT file ticket for uploading."""
    NxFile: str
    """Feature NX file name."""
    NxTicket: str
    """Feature NX file ticket for uploading."""

class WeldManagement:
    """
    Interface WeldManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateUpdateWelds(self, Inputs: list[CreateWeldInput]) -> CreateWeldResp:
        """    
             This operation creates or modifies weld feature business objects for the CreateWeldInput
             supplied.The CreateWeldInput contains information for properties client Id,
             parent bvr that is used to create bom window contains weld components as well as
             connection parts, WeldCompWithFeatData. WeldCompWithFeatData contains
             weld component information and Weld feature data properties of UG Entity Handle,
             attriubtes, forms, JT file, JT ticket, connected part information, weld feature type,revise
             mark.
             

             Server implementation compares the features list from input with the one retrieved
             from weld component occurrence in Teamcenter. if the weld feature does not exist,
             then the features  will be created in weld component occurrence and added as children.
             If the weld feature exists, then the features  will be updated based on the input
             information.  If the features is missing from input, the features will be removed
             from weld component occurrence children.
             

             Client application should mark the features that are to be revised. by default the
             revise mark is false, if the revise mark set to true, the new weld feature revison
             will be created and attached to the weld component.Rest of the features are assumed
             to be updated.
             

Use Cases:

             when you enable weld publish option and  save the assembly part that including weld
             feature, the SOA createUpdateWeld will be called and weld feature will be created
             in teamcenter.
             

Teamcenter Component:

             Weld Management - Weld Management SOA service.
             
        :param Inputs: 
                         List of create/update weld component inputs.
             
        :return: The created/updated weld feature business objects are returned via CreateWeldResp
             in Created/Updated lists
        """
        ...
    def DeleteWelds(self, Inputs: list[DeleteWeldInput]) -> DeleteWeldResp:
        """    
             This operation deletes weld components and weld feature business objects for the
             DeleteWeldInput supplied.The DeleteWeldInput contains information for
             properties client Id, parent bvr that is used to create bom window contains weld
             components as well as connection parts, List of weld components to be deleted, Type
             of relation from weld feature object to connection parts,and logical destroy mark.
             The destory mark will determine destroy object or just remove from the structure,
             if it is true, weld component and feature objects will be destroyed  from TC; if
             it is false, the weld component will be removed from assembly structure.
             

Use Cases:

             You can delete weld components or weld features(destroy or remove it from structure
             based on the destroy mark argument)  using deleteWelds operation by providing
             a list of DeleteWeldInput.
             

Teamcenter Component:

             Weld Management - Weld Management SOA service.
             
        :param Inputs: 
                         List of delete weld component inputs.
             
        :return: List of message on eached weld component showing whether is deleted or failed to
             be deleted.
        """
        ...
    def FindWelds(self, Inputs: list[FindWeldInput]) -> FindWeldResp:
        """    
             This operation find weld components by the FindWeldInput supplied. The FindWeldInput
             contains information for properties client Id, parent bvr that is used to create
             bom window contains weld components as well as connection parts, Connection part
             PS Occurrences, which must fall in the bom window that created by parent BVR, Connection
             relation type, Weld component types as a filter, for example, weld component and
             features occurrence are related to connection part APN by TC_CONNECT_TO relation.
             

Use Cases:

             You can find weld components using findWelds operation by providing a list
             of  FindWeldInput structure.
             

Teamcenter Component:

             Weld Management - Weld Management SOA service.
             
        :param Inputs: 
                         List of find weld component inputs.
             
        :return: List of weld components.
        """
        ...

