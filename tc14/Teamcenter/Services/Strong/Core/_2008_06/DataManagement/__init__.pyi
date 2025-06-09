import System
import System.Collections
import Teamcenter.Services.Strong.Core._2006_03.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddParticipantInfo:
    """
    
AddParticipantInfo structure is an input
            for the addParticipants operation.
            
    """
    def __init__(self, ) -> None: ...
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """An item revision to add participants to."""
    ParticipantInfo: list[ParticipantInfo]
    """Contains information to create a new participant or find an existing one."""

class AddParticipantOutput:
    """
    
AddParticipantOutput structure contains Item
            Revision and the added participants along with Service Data.
            
    """
    def __init__(self, ) -> None: ...
    ParticipantOutput: list[Participants]
    """
            List of structures containing the participants and the object to which participants
            are added.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class AttrInfo:
    """
    This structure contains information for specifying name value pairs.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the attribute."""
    Value: str
    """The value of the attribute."""

class BOHierarchy:
    """
    
            This structure contains information for a bottom up hierarchy starting with a Business
            Object name and going up the hierarchy of parents up to the primary Business
            Object.
            
    """
    def __init__(self, ) -> None: ...
    BOName: str
    """Business Object Name"""
    BOParents: list[str]
    """Ordered list of Business Object parents from bottom up"""

class BOWithExclusionIn:
    """
    Structure to hold the information about Business Object name and its exclusion list.
    """
    def __init__(self, ) -> None: ...
    BoTypeName: str
    """
            Primary Business Object name for which hierarchies of displayable Business Objects
            are returned.
            """
    ExclusionBOTypeNames: list[str]
    """List of Business Object names to be excluded from the returned list."""

class BVROutput:
    """
    This structure contains bom view revision information.
    """
    def __init__(self, ) -> None: ...
    Bvr: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    """The BVR associated with the ItemRevision if requested."""
    ViewTypeName: str
    """The bvr view type."""

class ConnectionOutput:
    """
    
            This structure contains information for createConnections
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifying string from the source ConnectionProperties."""
    Connection: Teamcenter.Soa.Client.Model.Strong.PSConnection
    """The newly created Connection object"""
    ConnectionRev: Teamcenter.Soa.Client.Model.Strong.PSConnectionRevision
    """The initial revision for the newly created ConnectionRevision"""

class ConnectionProperties:
    """
    
            Input structure for createConnections operation.  Specifies attributes for the new
            Connection or ConnectionRevision.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller for each ConnectionProperties. This ID is
            used to identify returned ConnectionOutput elements and Partial Errors associated
            with the input ConnectionProperties, optional
            """
    ConnId: str
    """The ID of the Connection to be created, optional"""
    Name: str
    """The name of the Connection to be created, optional"""
    Type: str
    """The type of the Connection to be created. The default type is Connection"""
    RevId: str
    """The ID of the initial revision of the Connection to be created, optional"""
    Description: str
    """The description text for the Connection to be created, optional"""
    ExtendedAttributes: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.ExtendedAttributes]
    """
            Any additional attribute values to be set on the created Connection, ConnectionRevision
            or coresponding Master Forms, optional
            """

class CreateConnectionsResponse:
    """
    Return structure for createConnections operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""
    Output: list[ConnectionOutput]
    """
            A list of created Connection objects and associate ConnectionRevision
            in the form of ConnectionsOutput structure.
            """

class CreateInput:
    """
    
            This structure captures the inputs required for creation of a business object. This
            is a recursive structure containing the CreateInput(s)
            for any secondary(compounded) objects that might be created (e.g Item also
            creates ItemRevision and ItemMaster Form, etc.)
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business object type name"""
    StringProps: System.Collections.Hashtable
    """
            Map of string property names to values (string,
            string)
            """
    StringArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type string array. A map of property names to values
            (string/list of strings).
            """
    DoubleProps: System.Collections.Hashtable
    """
            Map of double property names to values (string,
            double)
            """
    DoubleArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type double array. A map of property names to values
            (string/list of doubles).
            """
    FloatProps: System.Collections.Hashtable
    """Map of float property names to values (string, float)"""
    FloatArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type float array. A map of property names to values
            (string/list of floats).
            """
    IntProps: System.Collections.Hashtable
    """Map of int property names to values (string, int)"""
    IntArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type int array. A map of property names to values
            (string/list of ints).
            """
    BoolProps: System.Collections.Hashtable
    """Map of boolean property names to values (string, bool)"""
    BoolArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type bool array. A map of property names to values
            (string/list of bools).
            """
    DateProps: System.Collections.Hashtable
    """
            Map of DateTime property names to values (string,
            date)
            """
    DateArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type DateTime array. A map of property names to values
            (string/list of DateTimes).
            """
    TagProps: System.Collections.Hashtable
    """
            Map of BusinessObject property names to values (string,
            BusinessObject)
            """
    TagArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type BusinessObject array. A map of property
            names to values (string/list of BusinessObjects)
            """
    CompoundCreateInput: System.Collections.Hashtable

class CreateIn:
    """
    
            The data structure contains data for creation
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Unique client identifier. If there is an error in create, the client id in the ServiceData
            PartialError list can be used to associate to the clientId in the input to detect
            which object creation failed.
            """
    Data: CreateInput
    """
            Input data for create operation. This is essentially a map of property name-value
            pairs representing the input data for creation. It also is recursive referencing
            secondary input data (e.g For Item creation, the primary input data is for Item and
            secondary input data is for Item Master and ItemRevision).
            """

class CreateOrUpdateGDELinksResponse:
    """
    Create Or Update GDE Links Response
    """
    def __init__(self, ) -> None: ...
    SuccessfullyProcessedGDELinks: System.Collections.Hashtable
    """
            A map containing the clientIds and the successfully created/updated GeneralDesignElementLink
            objects
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data to report partial errors."""

class CreateOrUpdateItemElementsResponse:
    """
    Return structure for createOrUpdateItemElements operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData member containing created/updated objects and partial errors
            if any
            """
    Output: list[ItemElementsOutput]
    """A list of createItemElementsOutput"""

class CreateOrUpdateRelationsInfo:
    """
    
            The required parameters to create the relation between the primary and secondary
            object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    RelationType: str
    """Realtion of interest, required for create or update."""
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The primary object of interest, required for create or update."""
    SecondaryData: list[SecondaryData]
    """
            List of secondary objects per primaryObject via relation of type relationType.
            """
    Relations: list[Teamcenter.Soa.Client.Model.Strong.ImanRelation]
    """
            Instead of secondary business object in secondaryData
            and primaryObject, this can be used, if such
            an object is available. This is only used if the primaryObject
            is not specified. If relations is specified,
            the primaries for all of them must be the same and the relations
            must have the same relationType.
            """

class CreateOrUpdateRelationsOutput:
    """
    This structure contains information for CreateOrUpdateRelationsOutput.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the CreateOrUpdateRelationsInfo.clientId.
            This can be used by the caller to indentify this data structure with the source input
            data
            """
    Relations: list[Teamcenter.Soa.Client.Model.Strong.ImanRelation]
    """The newly created relation."""

class CreateOrUpdateRelationsResponse:
    """
    
            The relations created based on the input primary, secondary and relation type information
            and the errors that might have been encountered while creating, updating the relations.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateOrUpdateRelationsOutput]
    """A list of CreateOrUpdateRelationsOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData object to hold the partial
            errors that the operation encounters.
            """

class CreateOut:
    """
    This structure contains information or create operation including unique client identifier.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that were created"""

class CreateResponse:
    """
    
            Response object for create operation containing vector of objects that were created
            and partial errors.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateOut]
    """Vector of output objects representing objects that were created."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data including partial errors that are mapped to the client id from the input.
            Created objects are also added to the created objects list in the Service Data.
            """

class DatasetFilter:
    """
    The structure contains information for determining which datasets to return.
    """
    def __init__(self, ) -> None: ...
    UseNameFirst: bool
    """Filter with the datasetName first."""
    Processing: str
    """
            Specifies which version or versions of the Dataset are returned.
            
            Legal values are:
            

All - All versions of the dataset are returned.
            
Min - The version 0 of the dataset is returned.
            
None - No dataset is returned.
            

"""
    NrFilters: list[NamedReferenceFilter]
    """
            Filter to select datasets with a particular named reference to a specific uid. If
            empty then not used in filtering.
            """
    Name: str
    """The name of the Dataset objects to return. If empty then not used in filtering."""
    RelationFilters: list[DatasetRelationFilter]
    """The relation filters to use."""

class DatasetInfo:
    """
    
            Input structure that the information for determining which datasets to return. If
            the datasetUid is specified, then only that
            dataset will be returned. If the dataset does not exist then a null dataset is returned.
            If the datasetUid is not specified then the
            dataset filter determines the datasets to return. For each dataset to be returned,
            the NamedRef will determine the named reference
            information to return. For each named reference returned that is a reference to a
            file, an FMS read ticket will be returned if ticket
            is set.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string used to identify return data elements and partial errors associated
            with this input structure.
            """
    Uid: str
    """The uid of the only Dataset to return."""
    Filter: DatasetFilter
    """If a UID is not specified, determines the Dataset objects to return."""
    NamedRefs: list[NamedReferenceList]
    """Information about named references to return for each Dataset."""

class DatasetOutput:
    """
    Output structure for Dataset information
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string used to identify return data elements and partial errors associated
            with this input structure.
            """
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object ."""
    RelationTypeName: str
    """Relationship type to the dataset."""
    NamedReferenceOutput: list[NROutput]
    """The list of NROutput for the dataset if requested."""

class DatasetProperties2:
    """
    Input structure for createDatasets operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Identifier that helps the client to track the object(s) created, required; should
            be unique for the input set
            """
    Type: str
    """Type of the Dataset to be created"""
    Name: str
    """Name of the Dataset to be created"""
    Description: str
    """Description of the Dataset to be created, may be an empty string."""
    ToolUsed: str
    """
            Name of the Tool used to open the created Dataset, may be an empty
            string.  If it is an empty string no Tool will be associated to the Dataset
            to be created.
            """
    DatasetId: str
    """
            Unique identifier for the Dataset, may be an empty string. If the preference
            AE_datase_id_usage is ON, the id will be generated through user exit mechanism.
            """
    DatasetRev: str
    """
            The revision of this Dataset, may be an empty string.  If the preference AE_datase_id_usage
            is ON, the rev will be generated through user exit mechanism.
            """
    Container: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of the container used to hold the created dataset, optional"""
    RelationType: str
    """Name of the relation type for the Dataset to be created, may be an empty string."""

class DatasetRelationFilter:
    """
    
            This structure contains information for determining which datasets to consider to
            return. The relation type and Dataset type will be used to produce a set of
            datasets.
            
    """
    def __init__(self, ) -> None: ...
    RelationTypeName: str
    """
            The relation type name specifies the relation that relates the ItemRevision
            to the Dataset. If not specified then all.
            """
    DatasetTypeName: str
    """The type name of Dataset to return. If empty then all."""

class DeepCopyData:
    """
    The data structure holds information required to apply deep copy rules.
    """
    def __init__(self, ) -> None: ...
    OtherSideObjectTag: Teamcenter.Soa.Client.Model.ModelObject
    """Object on which the deep copy should be performed."""
    RelationTypeName: str
    """Name of the relation that need to be deep copied."""
    NewName: str
    """
            New name for the new copy of the object represented by the otherSideObject.
            The value for the newName will be null if
            'action' is not CopyAsObject or ReviseAndRelateToLatest.
            """
    Action: int
    """
            Integer representing the action to be performed on the object represented by 'otherSideObjectTag'.
            
            The values for action are:
            

CopyAsObjectType = 0
            
CopyAsRefType = 1
            
DontCopyType =2
            
RelateToLatest = 3
            
ReviseAndRelateToLatest = 4
            

"""
    IsTargetPrimary: bool
    """
            Indicates whether the given ItemRrevision is a primary object in the relation
            to be deep copied.
            """
    IsRequired: bool
    """Indicates whether the deep information is from a mandatory deepcopy rule"""
    CopyRelations: bool
    """Indicates whether the properties on the relation should be copied"""

class DisplayableBOsOut:
    """
    
            This structure contains a list of displayable business(BO) object under a given BO
            (displayable sub-BO hierarchy).
            
    """
    def __init__(self, ) -> None: ...
    BoTypeName: str
    """Business object name for which displayable hierarchy is returned"""
    DisplayableBOTypeNames: list[BOHierarchy]
    """Hierarchy of displayable business Objects"""

class DisplayableSubBOsResponse:
    """
    Response for getDisplayableBusinessObjects
    """
    def __init__(self, ) -> None: ...
    Output: list[DisplayableBOsOut]
    """Vector of output objects representing displayable types during create of a BO"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data including partial errors that are mapped to the input BO type name"""

class GDELinkInfo:
    """
    GDE Link Information
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string identifier supplied by the caller for each GDELinkInfo. This ID is
            used to identify returned GDELink objects and Partial Errors associated with the
            input properties.
            """
    Name: str
    """Name of the GDELink to be created."""
    Description: str
    """The description text for the GDELink to be created."""
    Type: str
    """Type of the GDELink that needs to be created. The default type is GeneralDesignElementInfoLink."""
    GdeLink: Teamcenter.Soa.Client.Model.Strong.GeneralDesignElementLink
    """Existing GDELink to update (will be null in case of creation)"""
    Attributes: list[NameValueStruct]
    """Any additional attribute values to be set on the created GDELink."""

class ItemInfo:
    """
    
            This structure contains either an item id or uid. Has a flag that indicates if the
            id is to be used first. If set then the id will be used. If the id does not resolve
            to an item then the uid will be used. If the flag is not set then the uid will be
            used first. If the uid does not resolve to an item then the id will be used. If no
            matching item is found then a null entry is placed in the output list and an error
            is returned.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Identifier generated by client to identify output"""
    UseIdFirst: bool
    """A flag to indicate if the id is to be used before the uid."""
    Uid: str
    """Item uid string for Item to retrieve."""
    Ids: list[AttrInfo]
    """
            List of attributes and values for selecting the item. For pre TC8.1 versions only
            one entry is supported. This entry has the name item_id.
            """

class RevInfo:
    """
    This structure contains information to determine the revisions to return.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Identifier generated by client to identify output."""
    Processing: str
    """
            Specifies what data to use to determine the revisions to return.
            
            The legal values are:
            

All - All the revisions of the input Item are returned
            
None - No revisions are returned.
            
Nrev - Number of revisions based on the RevInfo::nRevs
            input.
            
Min - The latest revision.
            
Rule - The revision as configured by the RevInfo::revisionRule
            input.
            
Ids - The revision based on the RevInfo::Id
            input.
            

"""
    UseIdFirst: bool
    """A flag to indicate if the id is to be used before the uid."""
    Uid: str
    """Revision uid for revision to retrieve."""
    Id: str
    """Revision id for revision to retrieve."""
    NRevs: int
    """
            The number of revisions to retrieve, or the number of existing revisions, whichever
            is smaller. The revisions returned will be the latest ones. The first one returned
            is the oldest of the group. The last the latest.
            """
    RevisionRule: str
    """The revision rule to be used."""

class GetItemAndRelatedObjectsInfo:
    """
    
            Input structure for GetItemAndRelatedObjects.
            Must have a clientId, must contain an itemInfo that is valid, may contain a list of information
            about revisions to return. If any bvr names are given then the tags for the BVRs
            will be returned.
            
            If itemInfo and revInfo
            are not provided, then the input structure for GetItemAndRelatedObjects
            expects the value "ProcessingNone" for both datasetInfo.filter.processing and revInfo.filter.processing.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Identifier generated by client to identify output"""
    ItemInfo: ItemInfo
    """
Item specifications, the itemInfo input is valid when one of the following
            is true:
            
            - has the uid field set to the UID of an existing Item,
            
            - has the ids filed set to key attribute values which identify a single existing
            Item,
            
            - it may be blank if the RevInfo uid field is set to the UID of an existing ItemRevision.
            """
    RevInfo: RevInfo
    """Revision specifications"""
    DatasetInfo: DatasetInfo
    """Filter used to select datasets to return."""
    BvrTypeNames: list[str]
    """A list of a BVRs to return. optional."""

class GetItemAndRelatedObjectsItemOutput:
    """
    This structure contains item information.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier of input data used to generate output."""
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """Item object."""
    ItemRevOutput: list[RevisionOutput]
    """
            List of RevisionOutputs. When multiple are
            returned, the order will be oldest first to latest last.
            """

class GetItemAndRelatedObjectsResponse:
    """
    
            Return structure for GetItemAndRelatedObjects
            operation
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetItemAndRelatedObjectsItemOutput]
    """List of GetItemAndRelatedObjectsItemOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class GetNextIdsResponse:
    """
    
            Response structure for getNextIds service
            operation.
            
    """
    def __init__(self, ) -> None: ...
    NextIds: list[str]
    """List containing next Id strings generated as per the pattern."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData structure. It contains
            partial errors and failures along with the clientIds.
            """

class GetNRPatternsWithCountersResponse:
    """
    Response structure for getNRPatternsWithCounters service operation.
    """
    def __init__(self, ) -> None: ...
    Patterns: list[PatternsWithCounters]
    """List of structs which contain Patterns which has counters."""
    PreferredPattern: list[str]
    """List of preferred patterns."""
    Condition: list[str]
    """List of conditions."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData structure. It contains partial errors and failures along with
            the clientIds.
            """

class GetRevNRAttachResponse:
    """
    Response structure for getRevNRAttachDetails service operation.
    """
    def __init__(self, ) -> None: ...
    InitRevDetails: list[RevOptionDetails]
    """List containing information about Initial Revision Type."""
    SecRevDetails: list[RevOptionDetails]
    """List containing information about Secondary Revision Type."""
    SupplRevDetails: list[RevOptionDetails]
    """List containing information about Supplemental Revision Type."""
    ExcludedLetters: list[str]
    """List of exluded letters."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData structure. It contains partial errors and failures along with
            the clientIds.
            """

class InfoForNextId:
    """
    
            Input structure for getNextIds operation.
            It contains information about the object type, property name and pattern to be used
            for id generation.
            
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """Type Name"""
    PropName: str
    """Property Name"""
    Pattern: str
    """Pattern String"""

class ItemElementProperties:
    """
    Input structure for createOrUpdateItemElements operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Identifier that helps the client to track the object(s) created should be unique
            for the input set
            """
    Name: str
    """Name of the ItemElement to be created"""
    Type: str
    """
            Type of the ItemElement to be created. If it is not passed, operation takes default
            type.
            """
    Description: str
    """Description of the ItemElement to be created"""
    ItemElemAttributes: System.Collections.Hashtable
    """
            Map<String,String> containing the attributes to be modified and its values. Required
            in case of updating an existing GDE.
            """
    ItemElement: Teamcenter.Soa.Client.Model.ModelObject
    """ItemElement to be updated."""

class ItemElementsOutput:
    """
    
            This structure contains information for createOrUpdateItemElements
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created."""
    ItemElem: Teamcenter.Soa.Client.Model.Strong.GeneralDesignElement
    """ItemElement object that was created"""

class MasterFormPropertiesInfo:
    """
    
            The data structure holds information for specifying property values to be set on
            a Form.
            
    """
    def __init__(self, ) -> None: ...
    Form: Teamcenter.Soa.Client.Model.Strong.Form
    """Reference to Form object"""
    PropertyValueInfo: list[PropertyNameValueInfo]
    """A list of propertie names and values"""

class NamedReferenceFilter:
    """
    
            This structure contains information for determining which datasets to consider to
            return. This specifies a list of named references and the UID referenced by the named
            reference.
            
    """
    def __init__(self, ) -> None: ...
    NamedReference: str
    """The name of the named reference."""
    UidReferenced: str
    """The unique identifier referenced."""

class NamedReferenceList:
    """
    
            This structure contains information determining which named reference information
            to return. This specifies a named reference to return and a flag to specify, if the
            named reference is to a file, to return an FMS read ticket.
            
    """
    def __init__(self, ) -> None: ...
    NamedReference: str
    """Named Reference to return."""
    Ticket: bool
    """If this Named Reference is to a file, include an FMS read ticket if set."""

class NameValueStruct:
    """
    This structure contains property name and value pairs for each property.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Title of the attribute like time, act_location that needs to be set"""
    Values: list[str]
    """Values of the attribute to be set"""

class NRAttachInfo:
    """
    
            NRAttachInfo structure contains information about the object type and property name
            for which Naming Rule information needs to be obtained.
            
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """Type Name"""
    PropName: str
    """Property Name"""

class NROutput:
    """
    This structure contains named reference information.
    """
    def __init__(self, ) -> None: ...
    NamedReference: Teamcenter.Soa.Client.Model.ModelObject
    """Object referenced"""
    NamedReferenceName: str
    """Named Reference name"""
    Ticket: str
    """Read ticket if referenced file and if requested."""

class ParticipantInfo:
    """
    
            This structure contains information about new participant to be created or to find
            an existing one.
            
    """
    def __init__(self, ) -> None: ...
    Assignee: Teamcenter.Soa.Client.Model.ModelObject
    """The participant which can be a User, GroupMember or a ResourcePool"""
    ParticipantType: str
    """
            Participant type to be assigned or added.  List of Participant types provided
            are:
            

ProposedResponsibleParty
            
ProposedReviewer
            
ChangeImplementationBoard
            
ChangeReviewBoard
            
ChangeSpecialist1
            
ChangeSpecialist2
            
ChangeSpecialist3
            
Analyst
            
Requestor
            



            Custom participant types are also allowed.
            """
    ClientId: str
    """A unique string supplied by the caller"""

class Participants:
    """
    
Participants structure contains the participants
            to be added / removed and object to which participants are to be added or removed.
            
    """
    def __init__(self, ) -> None: ...
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Item Revision to which the Participant objects are added/removed."""
    Participant: list[Teamcenter.Soa.Client.Model.Strong.Participant]
    """List of Participant objects to be added/removed."""

class PatternsWithCounters:
    """
    This structure holds patterns with counters.
    """
    def __init__(self, ) -> None: ...
    PatternStrings: list[str]
    """A list of pattern strings with counters"""

class PropertyNameValueInfo:
    """
    This structure contains information for specifying property name value pairs.
    """
    def __init__(self, ) -> None: ...
    PropertyName: str
    """Name of the property"""
    PropertyValues: list[str]
    """A list of value(s) of the property"""

class RelatedObjectInfo:
    """
    The data structure for specifying related object information.
    """
    def __init__(self, ) -> None: ...
    RelatedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Object related to the new Item or IitemRevision."""
    Action: int
    """
            An integer representing the action that specifies the why the relatedObject as the
            other side object while applying the deep copy rules. Valid values are : CopyAsObjectType
            = 0, (A new copy of the object represented by otherSideObjectTag will be created
            and while propagatring the relations) CopyAsRefType = 1, (The same object represented
            by otherSideObjectTag will be used to propagate the relations) DontCopyType =2, (The
            relation will not be propagated.) RelateToLatest = 3, (If the other side object is
            an ItemRevision, then the latest version of the revision will be used while propagating
            the relation) ReviseAndRelateToLatest = 4 (If the other side object is an Item Revision,
            it will be revised and the newly created revision will be used while propagating
            the relations)
            """
    IsSecondary: bool
    """
            Flag indicating whether the relatedObject
            is participating as a secondary object in the relation.
            """

class ReviseInfo:
    """
    
            The data structure contains the information required to create the new revision.
            If DeepCopyInfo is supplied it overrides
            the existing relations on the existing ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier to uniquely identify the input"""
    BaseItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Original ItemRevision object to be used for the revise operation"""
    NewRevId: str
    """ItemRevision id string for creating new ItemRevision object"""
    Name: str
    """Name string for creating new Item/ItemRevision"""
    Description: str
    """Description string for creating new Item/ItemRevision"""
    DeepCopyInfo: list[DeepCopyData]
    """
            List of DeepCopyData objects to be used for
            propagating the relations of the ItemRevision. If this list is supplied, then
            only the relations listed in this list will be carried forward to the new ItemRevision.
            No other Deep Copy Rules defined in the system will get applied. Thus the DeepCopyData in this list overrides everything defined in the
            system to carry forward the relations of the ItemRevision.
            """
    NewItemRevisionMasterProperties: MasterFormPropertiesInfo
    """The information for the new ItemRevisionMaster Form property values"""

class ReviseOutput:
    """
    This structure contains newly created ItemRevision object and related objects.
    """
    def __init__(self, ) -> None: ...
    NewItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Newly created ItemRevision object."""
    RelatedObjects: list[RelatedObjectInfo]
    """
            A list of RelatedObjectInfo which represents
            the new objects created or the existing the objects used to propagate the relations
            during the deep copy.
            """

class ReviseResponse2:
    """
    Return structure for revise operation.
    """
    def __init__(self, ) -> None: ...
    ReviseOutputMap: System.Collections.Hashtable
    """
            Map whose keys are the input clientIds and output values pairs (string, ReviseOutput).
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This contains the status of the operation."""

class RevisionOutput:
    """
    Output structure containing revision information
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier of input data used to generate output."""
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object."""
    Bvrs: list[BVROutput]
    """The BVRs associated with the item revision if requested."""
    DatasetOutput: list[DatasetOutput]
    """List of DatasetOutput."""

class RevOptionDetails:
    """
    This structure contain revision option details.
    """
    def __init__(self, ) -> None: ...
    RevOption: str
    """The next available revision option"""
    RevFormat: int
    """Format specified for revision type."""

class SaveAsNewItemInfo:
    """
    
            This data structure contain existing and new object info for save as new Item
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier to uniquely identify the input"""
    BaseItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Original ItemRevision to be used for the ItemRevisionSaveAs
            operation
            """
    NewItemId: str
    """Item id string for creating new Item"""
    NewRevId: str
    """ItemRevision id string for creating new ItemRevision"""
    Name: str
    """Name string for creating new Item/ItemRevision."""
    Description: str
    """Description string for creating new Item/ItemRevision"""
    DeepCopyInfo: list[DeepCopyData]
    """
            List of deep copy data to be used for propagating the relations of the ItemRevision.
            If this list is supplied, then only the relations listed in this list will be carried
            forward to the new ItemRevision. No other Deep Copy Rules defined in the system
            will get applied. Thus the DeepCopyData in
            this list overrides everything defined in the system to carry forward the relations
            of the ItemRevision.
            """
    NewItemMasterProperties: MasterFormPropertiesInfo
    """The properties to be set for the newly created master form of the new Item"""
    NewItemRevisionMasterProperties: MasterFormPropertiesInfo
    """The properties to be set for the newly created master form of the new ItemRevision"""

class SaveAsNewItemOutput2:
    """
    The data strucutre contains newly created object inforamtiobn.
    """
    def __init__(self, ) -> None: ...
    NewItem: Teamcenter.Soa.Client.Model.Strong.Item
    """Newly created Item object"""
    NewItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Newly created ItemRevision object"""
    RelatedObjects: list[RelatedObjectInfo]
    """List of newly created related objects"""

class SaveAsNewItemResponse2:
    """
    The data structure contains return information for the operation.
    """
    def __init__(self, ) -> None: ...
    SaveAsOutputMap: System.Collections.Hashtable
    """
            Map whose keys are the input clientIds and output values pairs(string, SaveAsNewItemOutput2)
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data"""

class SecondaryData:
    """
    This structure contains information for secondary object data.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """identifier defined by user to track the related object."""
    Secondary: Teamcenter.Soa.Client.Model.ModelObject
    """the secondary object pointed to by the relation"""
    UserData: Teamcenter.Soa.Client.Model.ModelObject
    """Object associated with the relation to the above secondary object"""
    Properties: list[NameValueStruct]
    """
            Additional attributes to be set on the relation. These are meant for any derived
            classes of TCRelation with additional attributes.
            """

class TypeAndItemRevInfo:
    """
    
TypeAndItemRevInfo structure contains information
            about the object type and revision for which Revision Naming Rule information needs
            to be obtained.
            
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """Type name of Item or ItemRevision."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object selected."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindDisplayableSubBusinessObjects(self, Input: list[BOWithExclusionIn]) -> DisplayableSubBOsResponse:
        """    
             Operation to retrieve sub Business Object Names for a Business Object that are displayable
             to the login user in the object creation dialog. e.g File-new, select Item, what
             types to be displayed for Item
             
        :param Input: 
                         - a list of input objects representing the BO type names for which the displayable
                         types are to be retrieved
             
        :return: contains a list of BO type names to be displayed for input
        """
        ...
    def CreateDatasets2(self, Input: list[DatasetProperties2]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateDatasetsResponse:
        """    
             This operation creates a list of Dataset objects and creates the specified
             relation type between created Dataset and input container object.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param Input: 
                         The information needed to create  <b>Dataset</b>

        :return: 
        """
        ...
    def GetItemAndRelatedObjects(self, Infos: list[GetItemAndRelatedObjectsInfo]) -> GetItemAndRelatedObjectsResponse:
        """    
             This operation returns Items, ItemRevisions, Dataset and NamedReference
             information based on the input. Input is a list of GetItemAndRelatedObjectsInfo
             structures each of which contains item uid or id, revison information and optionally
             a list of filters to determine the datasets to be returned. For the Datasets
             the client can request information about the NamedReferences. NamedReferences
             are how Data files are attached to Datasets. The Data file is what
             a CAD client is really interested in. The return is a GetItemAndRelatedObjectsResponse
             which contains a list of GetItemAndRelatedObjectsItemOutput
             and a ServiceData.
             

Use Cases:

             The client has an item of ItemRevision and needs to know what CAD data is
             attached to the ItemRevision. The client fills in either the Item or
             ItemRevision information along with the information about the types of Dataset
             and NamedReferences the client is interested in. For the NamedReferences
             the user can get the tickets which will allow the client retrieve the files attached
             to the Datasets. The results of the query will give the client all the information
             about the Datasets and NamedReferences and optional tickets.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Infos: 
                         list of <font face="courier" height="10">GetItemAndRelatedObjectsInfo</font> structures.
             
        :return: Contains found items, revisions and the datasets attached to the revision. Partial
             Errors will be returned as a map of input client id to error message.
        """
        ...
    def Revise2(self, Info: list[ReviseInfo]) -> ReviseResponse2:
        """    
             This operation provides the ability to revise the ItemRevision objects given
             in the input list and carries forward relations to existing objects. When applying
             deep copy rules, if user overridden deep copy information is provided in the input,
             relations are propagated to the new ItemRevision based on that input. If no
             deep copy information is provided in the input, the deep copy rules in the database
             are used to propagate relations to the new ItemRevision.  If the input contains
             property values for the master form, those values are set on the new ItemRevision
             master form.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Info: 
                         The necessary information to create the new revision
             
        :return: 
        """
        ...
    def SaveAsNewItem2(self, Info: list[SaveAsNewItemInfo]) -> SaveAsNewItemResponse2:
        """    
             This operation provides the capability to create one or more new Item objects
             based on a list of existing ItemRevision objects. It optionally carries forward
             ItemRevision relations based on the deepCopyRequired
             flag. When applying deep copy rules, if user overridden deep copy information is
             provided in the input, then old ItemRevision relations are propagated to the
             new ItemRevision based on the input. If no deep copy rule information is provided
             in the input, the deep rules in the database will be applied. If user provides new
             property values for the Item and ItemRevision master forms in the input,
             then these will be copied to the master forms of the newly created Item and
             ItemRevision.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Info: 
                         The necessary information to create the new <b>Iitem</b> and <b>ItemRevision</b>

        :return: 
        """
        ...
    def GetNextIds(self, VInfoForNextId: list[InfoForNextId]) -> GetNextIdsResponse: ...
    def GetNRPatternsWithCounters(self, VAttachInfo: list[NRAttachInfo]) -> GetNRPatternsWithCountersResponse:
        """    
             This operation gives the list of Patterns which has counters along with preferred
             patterns and conditions for the Naming Rule attached to the property of an object
             Type. The Type name and the Property name are passed in the input structure. The
             input for this operation contains a list of this structure. The return structure
             contains the vector of patterns with counters, preferredPattern and condition, along
             with the service data member.
             

Use Cases:

             This operation is used in create, revise or save-as dialogs to receive list of applicable
             patterns for item and revision ids. The list of patterns returned is displayed in
             these dialogs for user selection. After user selects a pattern and clicks "Assign"
             button, an id is generated matching the pattern selected and populated in the corresponding
             field's box.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param VAttachInfo: 
                         Struct that contains Type Name and Property Name
             
        :return: (This list may be incomplete, and is subject to change without notice.)
        """
        ...
    def GetRevNRAttachDetails(self, TypeAndItemRevInfos: list[TypeAndItemRevInfo]) -> GetRevNRAttachResponse:
        """    
             This operation gets all the possible initial, secondary and supplemental revision
             next Ids for an ItemRevision along with the available formats and the set
             of excluded letters for revision. The Revision Type Name and the current revision
             are passed in the input typeAndItemRevInfos structure. The input for this operation
             contains a list of this structure. The return structure contains list of Initial
             Revision details, Secondary Revision details, Supplemental Revision details and exclude
             Skip letters along with the service data member.
             

Use Cases:

             This operation is used to get the next available options for revision id for a new
             or existing object. User can select one of the values returned by this operation
             and use as revision id input value for create, revise or save-as operation.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param TypeAndItemRevInfos: 
                         List of <font face="courier" height="10">TypeAndItemRevInfo</font> structs which
                         contains <b>Item</b> and <b>ItemRevision</b> type name and the revision object.
             
        :return: (This list may be incomplete, and is subject to change without notice.)
        """
        ...
    def CreateOrUpdateRelations(self, Infos: list[CreateOrUpdateRelationsInfo], Sync: bool) -> CreateOrUpdateRelationsResponse:
        """    
             Creates the specified relation between the input objects (primary and secondary objects)
             for each input structure. If the sync flag
             is specified, then if any Generic Relationship Management (GRM) relations exist between
             the primary and secondary objects and they are not specified in the input they will
             be deleted. If sync flag is provided, the
             relations member of CreateOrUpdateRelationsInfo
             is ignored.
             

Use Cases:

             Use Case 1: Create a relation based on the GRM rule definition.
             

             One can create a relation specified by name of the relation in the input structure
             between the primary and secondary object, when there exists a GRM rule between the
             primary and secondary object with the given relation type.
             

             Use Case 2: Update a relation based on the GRM rule definition.
             

             One can update a relation specified by name of the relation in the input structure
             between the primary and secondary object, when there exists a GRM rule between the
             primary and secondary object with the given relation type.
             

             Use Case 3: Remove a relation based on the GRM rule definition.
             

             One can remove a relation by setting the sync to true and do not provide any relation
             between the primary and secondary object in the input structure. When there exists
             a GRM rule between the primary and secondary object with the given relation type,
             and the sync flag is set to true, then if any GRM relations exist between the primary
             and secondary objects and they are not specified in the input they will be deleted.
             


Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param Infos: 
                         A list of <font face="courier" height="10">CreateOrUpdateRelationsInfo</font> structures
                         containing details of relationships to be created between primary and secondary objects
                         with the given relation.
             
        :param Sync: 
                         If true then GRM relations in db and the number of secondary objects specified in
                         the <font face="courier" height="10">input</font> will be synchronized. Note that
                         in this case the <font face="courier" height="10">secondaryData</font> member of
                         the <font face="courier" height="10">input</font> structure is used and not the <font face="courier" height="10">relations</font> member.
             
        :return: list of partial errors.
        """
        ...
    def CreateConnections(self, Properties: list[ConnectionProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> CreateConnectionsResponse:
        """    
             Creates a list of Connection objects and any associated data (ConnectionRevision,
             ConnectionMaster Form and ConnectionRevision Master Form) based on
             the input properties structure. It also creates the specified relation type between
             newly created Connection object and input container object. If container and
             relation type are not supplied, none of the Connection objects will be related
             to a container. If any destination to paste the newly created objects is desired
             then it must be supplied as input.
             

Use Cases:

             This operation supports creation of single or multiple Connection objects.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Properties: 
                         A <b>Connection</b> object is created for each ConnectionProperties in the list.
                         The data on the ConnectionProperties is used to create initial values on the <b>Connection</b>
                         and related objects
             
        :param Container: 
                         Object to which all the <b>Connection</b> objects created will be related to via
                         the input relationType (Folder instance and contents relationType). If not specified
                         the <b>Connection</b> will be created, but without a relation to a container object.
             
        :param RelationType: 
                         The name of the relation used to attach the created <b>Connection</b> objects to
                         input container. This argument is used only when the container argument is present,
                         optional.
             
        :return: object will still be created, but will not be placed in any container.
        """
        ...
    def CreateOrUpdateGDELinks(self, GdeLinkInfos: list[GDELinkInfo]) -> CreateOrUpdateGDELinksResponse:
        """    
             Create and/or update GeneralDesignElementLink(GDELink) objects based
             on the input properties structure. If the given GDELink object exists in Teamcenter
             then the operation will be treated as an update based on the input properties structure
             

Use Cases:

             This operation supports creation or updation of GDELink objects
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param GdeLinkInfos: 
                         An input of vector of structures containing values necessary to create or update
                         the Teamcenter Model Data representing the <i>GDELink</i>. If a reference to an existing
                         <i>GDELink</i> is supplied then an update is assumed, otherwise a new <i>GDELink</i>
                         is created. On update the <i>GDELink</i> name and description may be changed but
                         not the type. After the <i>GDELink</i> is created, and if for an update the property
                         values are supplied, the <i>GDELink</i> created will be updated with the properties.
             
        :return: with the error message mapped
             to input client id
        """
        ...
    def CreateOrUpdateItemElements(self, Properties: list[ItemElementProperties]) -> CreateOrUpdateItemElementsResponse:
        """    
             Allows the user to create a new GeneralDesignElement (GDE) or its subtype
             and set its properties. In the case of existing GDE, user can update the properties.
             

Use Cases:

             This operation can be used when user wants to create a GDE in a product structure
             or wants to update the properties of an existing GDE. User has to pass unique
             client Id, name and type when a new element has to be created. Whenever properties
             of an existing GDE have to be updated the itemElement business object
             and itemElemAttributes should be passed
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Properties: 
                         This is a vector of <i>ItemElementProperties</i>. While creating a new element it
                         shall contain a unique clientId, name and type. In the case of an existing <i>GDE</i>,
                         this structure must contain <i>itemElemAttributes</i> to be modified and the <i>itemElement</i>
                         whose properties have to be modified.
             
        :return: 
        """
        ...
    def CreateObjects(self, Input: list[CreateIn]) -> CreateResponse:
        """    
             Generic operation for creation of Business Objects. This will also create any secondary(compounded)
             objects that need to be created, assuming the CreateInput for the secondary object
             is represented in the recursive CreateInput object e.g. Item is Primary Object
             that also creates Item Master and ItemRevision. ItemRevision
             in turn creates ItemRevision Master. The input for all these levels is passed
             in through the recursive CreateInput object.
             

Use Cases:

             This operation to create an object is invoked after obtaining user input on the fields
             of the create dialog. This call is typically preceded by a call to Teamcenter::Soa::Core::_2008_06::PropDescriptor::getCreateDesc
             or to the SOA Client Metamodel layer to retrieve Create Descriptor for a Business
             Object.
             

             For example, to create an Item, client will get the Create Descriptor associated
             with the Item from the client metamodel (The associated descriptor type can be found
             by looking at the constant value for the CreateInput constant that is attached to
             Item). Alternatively, for clients that do not use the SOA client metamodel, the Descriptor
             for Item can be obtained by invoking getCreateDesc operation. The descriptor information
             can then be used to populate the Create dialog for the Business Object. Once the
             Create dialog is populated the createObjects operation can be called to create the
             object.
             


Dependencies:

             getCreateDesc
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param Input: 
                         This is a vector of CreateIn objects each one of which represents the CreateInput
                         information used to create an object. Each CreateIn object has a client id and a
                         CreateInput object which contains the information to create the object. The client
                         id can be used to map to any partial errors in the ServiceData information returned
                         in the output.
             
        :return: 
        """
        ...
    def AddParticipants(self, AddParticipantInfo: list[AddParticipantInfo]) -> AddParticipantOutput:
        """    
             This operation creates the Participant objects and adds them to the input
             Item Revision. If a Participant object with specified attributes already exists,
             it is added to the Item Revision.
             

Use Cases:

             For Change Management use cases, user may need to add different participants to the
             change objects like analyst, change specialist etc. The creator of the change object
             will assign the analyst for the change where this operation can be used.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param AddParticipantInfo: 
                         Contains a list of <font face="courier" height="10">ParticipantInfo</font> structures
                         with information about participants to be added and an Item Revision to add the participants
                         to.
             
        :return: If the service fails to create the participant, it returns "SOACORE_failed_to_create_participant"
             error code.
        """
        ...
    def RemoveParticipants(self, Participants: list[Participants]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation allows the user to remove Participant objects associated with
             specified Item Revision. If a participant being removed is no longer associated with
             any other objects, it gets deleted.
             

Use Cases:

             This operation can be used to remove the assigned Participant objects like
             Analyst, Proposed Reviewers etc. from the change objects. Change creator can use
             addParticipants service operation to assign
             an analyst or use this operation to remove an assigned analyst.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Participants: 
                         List of participants structures each containing a list of <b>Participant</b> objects
                         to be removed and an Item Revision to remove the <b>Participant</b> objects from.
             
        :return: 
        """
        ...

