import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeInfo:
    """
    
            This structure allows the caller to define or update named attributes. The name member
            represents the property name for the related object and the value is the value to
            set.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Text for Attribute Name"""
    Value: str
    """Text for Attribute Value"""

class PropDescriptor:
    """
    The PropDescriptor struct describes information about the Teamcenter property
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Name of the property"""
    DisplayName: str
    """Display name of the property"""
    DefaultValue: str
    """Default value for the property"""
    PropValueType: int
    """
            Value type for the property in integer form: PROP_untyped (0) No Value PROP_char
            (1) Value is a single character PROP_date (2) Value is a date PROP_double (3) Value
            is a double PROP_float (4) Value is a float PROP_int (5) Value is an integer PROP_logical
            (6) Value is a logical PROP_short (7) Value is a short PROP_string (8) Value is a
            character string PROP_typed_reference (9) Value is a typed reference PROP_untyped_reference
            (10) Value is an untyped reference PROP_external_reference (11) Value is an external
            reference PROP_note (12) Value is a note PROP_typed_relation (13) Value is a typed
            relation PROP_untyped_relation (14) Value is an untyped relation
            """
    PropType: int
    """
            Type for the property in integer form: PROP_unknown (0) Property type is Unknown
            PROP_attribute (1)  Based on a POM Attribute (int, string, ...) PROP_reference (2)
            Based on a POM Reference PROP_relation (3) Based on an ImanRelation PROP_compound
            (4) Based on a property from another Type PROP_runtime (5) Based on a computed value
            """
    IsDisplayable: bool
    """isDisplayable"""
    IsArray: bool
    """Specifies whether the property is an array or single value"""
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    """ListOfValues object attached to the property (if any)"""
    IsRequired: bool
    """Specifies whether the property is required"""
    IsEnabled: bool
    """Specifies whether the property is enabled"""
    IsModifiable: bool
    """Specifies whether the property is modifiable"""
    AttachedSpecifier: int
    """attachedSpecifier"""
    MaxLength: int
    """maxLength"""
    InterdependentProps: list[str]
    """interdependentProps"""

class AttrMappingInfo:
    """
    
            Contains CadAttrMappingDefinition object reference and the PropDescriptor structure
            used in the response of get attribute mapping operations.
            
    """
    def __init__(self, ) -> None: ...
    CadAttrMappingDefinition: Teamcenter.Soa.Client.Model.Strong.CadAttrMappingDefinition
    """CadAttrMappingDefinition object reference"""
    PropDesc: PropDescriptor
    """PropDescriptor structure containing property information for mapping definition property."""

class CommitDatasetFileInfo:
    """
    Holds the basic info for a file to be uploaded to a dataset.
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dateset object reference."""
    CreateNewVersion: bool
    """Flag to create new version ( TRUE ) or not ( FALSE )."""
    DatasetFileTicketInfos: list[DatasetFileTicketInfo]
    """A list of DatasetFileTicketInfos."""

class CreateOrUpdatePartsOutput:
    """
    Intermediate level output structure for createOrUpdateParts operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """Item object reference of the created/updated item"""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference of the created/updated item revision"""
    DatasetOutput: list[DatasetOutput]
    """List of DatasetOutputs"""
    ExtraItemObjs: list[ExtraObjectOutput]
    """List of ExtraObjectOutputs for the item extra objects"""
    ExtraItemRevObjs: list[ExtraObjectOutput]
    """List of ExtraObjectOutputs for the item revision extra objects"""

class CreateOrUpdatePartsResponse:
    """
    Holds the response for createOrUpdateParts
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateOrUpdatePartsOutput]
    """List of CreateOrUpdatePartsOutputs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information.
            """

class CreateOrUpdateRelationsInfo:
    """
    
            Contains input information for createdOrUpdateRelations
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    RelationType: str
    """Realtion of interest, required for create or update"""
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """object reference of primary object of interest, required for create or update"""
    SecondaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """object reference of secondary object of interest, required for create or update"""
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    """ImanRelation object reference of existing relation, used for update if provided"""
    UserData: Teamcenter.Soa.Client.Model.ModelObject
    """object reference to an object that can be attached to the relation (optional)"""

class CreateOrUpdateRelationsOutput:
    """
    
            Contains the output response structure for createdOrUpdateRelations
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    """ImanRelation object reference of relation created or updated"""

class CreateOrUpdateRelationsPref:
    """
    Contains a list of RelationAndTypesFilter structures for other side object filtering.
    """
    def __init__(self, ) -> None: ...
    Info: list[RelationAndTypesFilter2]
    """A list of RelationAndTypesFilter2"""

class CreateOrUpdateRelationsResponse:
    """
    Contains the response for createOrUpdateRelations
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateOrUpdateRelationsOutput]
    """A list of CreateOrUpdateRelationsOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created or updated by the service
            and error information. Errors are identified by the clientID
            which is supplied in the input data.
            """

class DatasetFileInfo:
    """
    Holds the basic info for a file to be uploaded to a dataset.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    FileName: str
    """Name of file to be uploaded.  Filename only, should not contain path to filename."""
    NamedReferencedName: str
    """Named Reference relation to file."""
    IsText: bool
    """Flag to indicate if file is text ( TRUE ) or binary (FALSE )."""
    AllowReplace: bool
    """Flag to indicate if file can be overwritten ( TRUE ) or not ( FALSE )."""

class DatasetFileTicketInfo:
    """
    Holds the basic info for a file to be uploaded to a dataset.
    """
    def __init__(self, ) -> None: ...
    DatasetFileInfo: DatasetFileInfo
    """Member of type DatasetFileInfo."""
    Ticket: str
    """ID of ticket."""

class DatasetInfo:
    """
    
            Contains all of the data necessary to construct the dataset object. The basic attributes
            that are required are passed as named elements in the structure. All other attributes
            are passed as name/value pairs in the AttributeInfo structure. The extraObject field
            allows for the creation of an object(s) that will be related to this newly created
            Dataset.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference for update, null for creation"""
    Name: str
    """Name attribute value"""
    Description: str
    """Description attribute value"""
    Type: str
    """Type attribute value"""
    Id: str
    """ID attribute value"""
    DatasetRev: str
    """Revision attribute value"""
    ItemRevRelationName: str
    """Required input, may not be null, not defaulted"""
    CreateNewVersion: bool
    """Flag to create new version ( TRUE ) or not (FALSE )"""
    NamedReferencePreference: str
    """
            Preference name which holds the list of named references to delete from one Dataset
            version to the next.
            """
    AttrList: list[AttributeInfo]
    """List of AttributeInfos for attributes"""
    MappingAttributes: list[AttributeInfo]
    """
            List of AttributeInfos for mapped attributes. Mapped atributes are attributes that
            are applied to other objects. Refere to the ITK manual for a definition of attribute
            mapping.
            """
    ExtraObject: list[ExtraObjectInfo]
    """List of ExtraObjectInfos"""
    DatasetFileInfos: list[DatasetFileInfo]
    """List of DatasetFileInfos"""
    NamedReferenceObjectInfos: list[NamedReferenceObjectInfo]
    """List of NamedReferenceObjectInfos"""

class DatasetOutput:
    """
    Structure contains created/updated dataset objects.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference of the created/updated dataset"""
    CommitInfo: list[CommitDatasetFileInfo]
    """List of CommitDatasetFileInfos"""
    ExtraObjs: list[ExtraObjectOutput]
    """List of ExtraObjectOutputs for the extra objects"""
    NamedRefObjs: list[ExtraObjectOutput]
    """List of ExtraObjectOutputs for the named references"""

class ExpandFolderForCADPref:
    """
    
            Contains list of RelationAndTypesFilter, number of latest revisions for further filtering
            and a flag to check whether item revision needs to be expanded.
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """
            Flag to specify if item revisions are to be expanded ( TRUE ) or not ( FALSE ) if
            found as other side objects.
            """
    LatestNRevs: int
    """
            The number of latest revisions under an Item that should be considered for further
            filtering
            """
    Info: list[RelationAndTypesFilter2]
    """A list of RelationAndTypesFilter2"""

class ExpandFoldersForCADItemOutput:
    """
    Contains the item expanded and the list of item revisions for the item.
    """
    def __init__(self, ) -> None: ...
    OutputItem: Teamcenter.Soa.Client.Model.Strong.Item
    """An item that is in the input folder."""
    ItemRevsOutput: list[ExpandFoldersForCADItemRevOutput]
    """
            A list of ExpandFolderForCADItemRevOutput
            which contains information about any item revisions that belong to item as specified
            by latestNRevs.
            """

class ExpandFoldersForCADItemRevOutput:
    """
    Contains the item revision expanded and the results of expanding the item revision.
    """
    def __init__(self, ) -> None: ...
    OutputItemRevs: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """An item revision that is in the input folder."""
    OutputDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """A list of datasets related to the item revision as specified by the input filter."""

class ExpandFoldersForCADOutput:
    """
    Contains the output data for ExpandFoldersForCAD operation.
    """
    def __init__(self, ) -> None: ...
    InputFolder: Teamcenter.Soa.Client.Model.Strong.Folder
    """Folder object reference of the folder of interest"""
    FstlvlFolders: list[Teamcenter.Soa.Client.Model.Strong.Folder]
    """A list of Folder object references in the input folder"""
    ItemsOutput: list[ExpandFoldersForCADItemOutput]
    """A list of ExpandFoldersForCADItemOutput for the item"""
    ItemRevsOutput: list[ExpandFoldersForCADItemRevOutput]
    """A list of ExpandFoldersForCADItemRevOutput for the item revision"""

class ExpandFoldersForCADResponse:
    """
    Contains the response for ExpandFoldersForCAD operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandFoldersForCADOutput]
    """
            A list of ExpandFoldersForCADOutput which has information about the input folder
            and folders, items and itemRevs output found under this folder
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            SOA framework object containing objects that were created, deleted, or updated by
            the Service, plain objects, and service errors/failure information
            """

class ExpandGRMRelationsData:
    """
    
            Contains a list of related objects and the relation name used to relate to the input
            object.
            
    """
    def __init__(self, ) -> None: ...
    OtherSideObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of object references of objects the object of interest is related to."""
    RelationName: str
    """The name of the relation used to relate the object of interest to the other otherSideObjects"""

class ExpandGRMRelationsOutput:
    """
    Contains the output data for ExpandGRMRelations operation.
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object reference of the object of interest"""
    OtherSideObjData: list[ExpandGRMRelationsData]
    """List of ExpandGRMRelationsData"""

class ExpandGRMRelationsPref:
    """
    
            Contains a list of RelationAndTypesFilter and a flag to check whether item revision
            needs to be expanded.
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """
            Flag to specify if item revisions are to be expanded ( TRUE ) or not ( FALSE ) if
            found as other side objects.
            """
    Info: list[RelationAndTypesFilter2]
    """List of RelationAndTypesFilter2"""

class ExpandGRMRelationsResponse:
    """
    Top level response structure for ExpandGRMRelations operations.
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandGRMRelationsOutput]
    """
            A list of ExpandGRMRelationsOutput which has information about the input object and
            it's filtered related object list
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            SOA framework object containing objects that were created, deleted, or updated by
            the Service, plain objects, and service errors/failure information
            """

class ExpandPrimaryObjectsData:
    """
    
            Contains a list of related objects and the relation name or property used to relate
            to the input object.
            
    """
    def __init__(self, ) -> None: ...
    OtherSideObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of object references of objects the object of interest is related to."""
    RelationName: str
    """The name of the relation used to relate the object of interest to the other otherSideObjects"""

class ExpandPrimaryObjectsOutput:
    """
    Contains the output data for ExpandPrimaryObjects operation.
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object reference of the object of interest"""
    OtherSideObjData: list[ExpandPrimaryObjectsData]
    """List of ExpandPrimaryObjectsData"""

class ExpandPrimaryObjectsPref:
    """
    
            Contains list of RelationAndTypesFilter and a flag to check whether item revision
            needs to be expanded .
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """
            Flag to specify if item revisions are to be expanded ( TRUE ) or not ( FALSE ) if
            found as other side objects.
            """
    Info: list[RelationAndTypesFilter2]
    """List of RelationAndTypesFilter2"""

class ExpandPrimaryObjectsResponse:
    """
    Contains the response structure for ExpandPrimaryObjects operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandPrimaryObjectsOutput]
    """A list of ExpandPrimaryObjectsOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            SOA framework object containing objects that were found by the service and service
            errors/failure information
            """

class ExtraObjectInfo:
    """
    
            Form objects that can be created or updated and related to an item, item revision
            or dataset.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference for existing object"""
    ClientId: str
    """Identifier defined by user to track the related object."""
    RelationTypeName: str
    """Name of the relation type to the parent object"""
    TypeName: str
    """Object Type name"""
    AttrNameValuePairs: list[AttributeInfo]
    """List of AttributeInfos."""

class ExtraObjectOutput:
    """
    
Form objects that can be created or updated and related to an item, item revision
            or dataset.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of the created/updated object"""

class GenerateAlternateIdsProperties:
    """
    Holds the input structure of GenerateAlternateIdsProperties
    """
    def __init__(self, ) -> None: ...
    IdContext: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of the id context used to generate the alternate id of that context"""
    Pattern: str
    """Pattern type used to generate the alternate id of that pattern"""
    AltIdType: str
    """Type of the alternate id to generate"""
    ParentAltId: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of the parent alternate id"""
    Count: int
    """Number of the alternate id to be generated."""

class GenerateAlternateIdsResponse:
    """
    Holds the response for generateAlternateIds
    """
    def __init__(self, ) -> None: ...
    InputIndexToAltId: System.Collections.Hashtable
    """Key is the index of the input, data is a list of alternate IDs generated."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains any partial errors and exceptions. No objects are created,
            deleted, modified or returned by this service.
            """

class GetAllAttrMappingsResponse:
    """
    Contains the response for getAllAttrMappings operation.
    """
    def __init__(self, ) -> None: ...
    AttrMappingInfos: list[AttrMappingInfo]
    """A list of AttrMappingInfo"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information. CadAttrMappingDefinition objects
            are returned as plain objects.
            """

class GetAttrMappingsForDatasetTypeCriteria:
    """
    
            Input criteria for the data returned from the getAttrMappingsForDatasetType
            operation.
            
    """
    def __init__(self, ) -> None: ...
    DatasetTypeName: str
    """The type name of a dataset.  This input is required."""
    ItemTypeName: str
    """The type name of an item.  This input is optional."""
    Exact: bool
    """
            The input flag indicating that the mappings to be returned are for a specific dataset
            type and item type combination when the value is true.
            """

class GetAttrMappingsForDatasetTypeOutput:
    """
    
            Contains the output data for the getAttrMappingsForDatasetType
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Criteria: GetAttrMappingsForDatasetTypeCriteria
    """The dataset and item type criteria used to find the attribute mapping definitions."""
    AttrMappingInfos: list[AttrMappingInfo]
    """The list of attribute mapping information that matches the criteria."""

class GetAttrMappingsForDatasetTypeResponse:
    """
    
            The response from the getAttrMappingsForDatasetType
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetAttrMappingsForDatasetTypeOutput]
    """A list of input dataset and item type criteria and the found attribute mapping definitions."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData.  This operation will populate
            the ServiceData plain objects with CadAttrMappingDefinition objects and property descriptor
            LOV objects.
            """

class GetAvailableTypesResponse:
    """
    
            Holds the response for getAvailableTypes,
            which the map of input objects (class names) and for each input object, the object
            references of found Types (NULL, if none found), along with the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    InputClassToTypes: System.Collections.Hashtable
    """
            Map where the key is the class type and the value is a list of strings representing
            the types available for the class.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains objects that are returned by the service, and error information. The actual
            type objects are returned as PlainObjects.
            This service does not define any of its own errors, but will return any errors from
            the subsystem in the list of partial errors.
            """

class ItemInfo:
    """
    
            The ItemInfo struct represents all of the data necessary to construct the item object.
            The basic attributes that are required are passed as named elements in the struct.
            All other attributes are passed as name/value pairs in the AttributeInfo struct.
            The extraObject field allows for the creation of an object(s) that will be related
            to this newly created Item.
            
    """
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """Item object reference for update, can be null for creation"""
    ItemId: str
    """ID for create, generated if null"""
    ItemType: str
    """Type, default is Item if null"""
    Name: str
    """Name, defaulted to id if null"""
    Description: str
    """Description, can be null"""
    AttrList: list[AttributeInfo]
    """List of AttributeInfos"""
    ExtraObject: list[ExtraObjectInfo]
    """List of ExtraObjectInfos"""
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """Folder to attach Item to, if null then default used"""

class ItemRevInfo:
    """
    
            The ItemRevInfo structure represents all of the data necessary to construct the item
            revision object. The basic attributes that are required are passed as named elements
            in the struct. All other attributes are passed as name/value pairs in the AttributeInfo
            struct. The extraObject field allows for the creation of an object(s) that will be
            related to this newly created Item Revision.
            
    """
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference, null for creation, otherwise update"""
    RevId: str
    """ID, if null then generated"""
    AttrList: list[AttributeInfo]
    """List of AttributeInfos"""
    ExtraObject: list[ExtraObjectInfo]
    """List ofr ExtraObjectInfos"""

class MappedDatasetAttrProperty:
    """
    Contains the found resolved object and property name mapped to specific input values.
    """
    def __init__(self, ) -> None: ...
    AttrTitle: str
    """
            The CadAttrMappingDefinition object title. This is generally the client application
            attribute display name.
            """
    DatasetTypeName: str
    """The Teamcenter defined type name of a dataset."""
    ItemTypeName: str
    """The Teamcenter defined type name of an item"""
    ResolvedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of object holding mapped attribute value"""
    ResolvedPropertyName: str
    """
            The property name of the mapped object holding the attribute value of interest resulting
            from evaluation of a dataset CAD attribute mapping definition.
            """

class NamedReferenceObjectInfo:
    """
    
            Contains information regarding named refernce type value, Object reference, Object
            type name and list of Attribute infos.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of the object for update, null for create"""
    NamedReferenceName: str
    """
            The Named Reference from the dataset to this object, required. NamedReference values
            are defined for each Dataset type. The customer can add more values as needed. To
            get a current list of valid Named Reference values the programmer can either use
            BMIDE or can call the SOA Core service getDatasetTypeIno.
            """
    TypeName: str
    """Type of the object to be created. Required for object creation only."""
    AttrNameValuePairs: list[AttributeInfo]
    """List of AttributeInfos."""

class PartInfo:
    """
    
            The PartInfo struct is the main input to the createOrUpdateParts service. This struct
            refers to the Item, ItemRevision, and one or more Dataset structures used to create
            those objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    ItemInput: ItemInfo
    """Member of type ItemInfo"""
    ItemRevInput: ItemRevInfo
    """Member of type ItemRevInfo"""
    DatasetInput: list[DatasetInfo]
    """List of DatasetInfos"""

class RelationAndTypesFilter2:
    """
    
            Structure contains relation name and vector of related object types of interest,
            which will used for filtering purpose.
            
    """
    def __init__(self, ) -> None: ...
    RelationName: str
    """The name of the relation of interest."""
    ObjectTypeNames: list[str]
    """A list of related object types of interest."""

class ResolveAttrMappingsForDatasetInfo:
    """
    
            Contains dataset, item revision and list of CadAttrMappingDefinition
            object references to be used in the resolve.
            
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference for which to get mapped attribute values."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference, helps resolve ambiguity in the mapping traversal."""
    CadAttrMappingDefinitions: list[Teamcenter.Soa.Client.Model.Strong.CadAttrMappingDefinition]
    """List of CadAttrMappingDefinition object references"""

class ResolveAttrMappingsForDatasetOutput:
    """
    Contains the output data for resolveAttrMappingsForDataset.
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference for which mapped attribute property information is desired."""
    MappedProperties: list[MappedDatasetAttrProperty]
    """A list of MappedDatasetAttrProperty"""

class ResolveAttrMappingsForDatasetResponse:
    """
    Contains the response for resolveAttrMappingsForDataset.
    """
    def __init__(self, ) -> None: ...
    Output: list[ResolveAttrMappingsForDatasetOutput]
    """A list of ResolveAttrMappingsForDatasetOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData contains any partial errors and
            exceptions.
            
            The objects holding the mapped attributes, resulting from successfully resolved mappings,
            are returned as plain objects.
            
            The mapped attribute properties are returned as ServiceData
            properties.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateParts(self, Info: list[PartInfo]) -> CreateOrUpdatePartsResponse:
        """    
             CreateOrUpdateParts allows the user to create or update a set of parts using Items,
             Item Revisions, Datasets and ExtraObjects. If the user supplies a valid Item object
             reference without specifying a valid item revision object reference or id, then only
             the item will be updated. If the user specifies a valid item object reference with
             a null item revision object reference and a non-null revision id, then a new item
             revision will be created and attached to the item with no relations from the new
             item revision to the previous item revision. If the user specifies a valid item object
             reference and a valid item revision object reference, then the item and item revision
             and related objects will be updated. If no item object reference or item revision
             object references are specified then a new item and item revision and related objects
             will be created. All objects created and updated will be returned in the ServiceData.
             All partial errors will contain the clientIDs for all items related to the error
             message, i.e. if a dataset encounters an error, then the ID for that erro will be
             the item client ID concantentated with the item revision id contantenated with the
             dataset client ID, all separated by semi-colons ( ; ).
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         A list of PartInfo structures
             
        :return: contains a list of CreateOrUpdatePartsOutput structures (which contain information
             about the item, itemrevisions. datasets and extra objects ). Failure will be with
             client id and error message in the ServiceData.
        """
        ...
    def CreateOrUpdateRelations(self, Info: list[CreateOrUpdateRelationsInfo], Complete: bool, Pref: CreateOrUpdateRelationsPref) -> CreateOrUpdateRelationsResponse:
        """    
createOrUpdateRelations creates or updates
             GRM relations between existing objects in Teamcenter. If the complete flag is set and a filter is supplied, then any relation
             types that exist for primary objects in the info that are listed in the filter, but
             the relations are not sent in the input, those relations will be deleted.
             

Use Cases:

             The user wishes to relate two objects in Teamcenter. The user specifies the primary
             and secondary objects, the type of relation to be created and any optional data the
             user wants added to the relation.
             
             The user wishes to modify the user data on the relationship between two objects.
             The user specifies the primary and secondary objects and the existing relationship.
             The user also specifies the new user data to be placed on the relationship.
             
             The user wishes to relate two objects in Teamcenter and remove any existing relationships
             between the objects. The user specifies the primary and secondary objects, the type
             of relation to be created and any optional data the user wants added to the relation.
             The user also sets the complete option to
             true to delete the existing relationships that pass the supplied filter, but does
             not send those existing relationships in the input.  For example, there is an item
             revision and a dataset related with an IMAN_specification relationship in Teamcenter
             and the user wants to change this to an IMAN_Rendering relationship. The user can
             specify the item revision and the dataset, specify the new relationship is IMAN_Rendering
             and set the complete flag. With the filter
             specifying the relation type of IMAN_specification and the object type as dataset.
             This will delete the current relationship and create the new one.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         A list of <font face="courier" height="10">CreateOrUpdateRelationsInfo</font>

        :param Complete: 
                         A flag to check whether any existing relations that pass the filter needs to be deleted.
             
        :param Pref: 
                         A list of <font face="courier" height="10">RelationAndTypesFilter2</font> structure.
             
        :return: .
        """
        ...
    def ExpandGRMRelations(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: ExpandGRMRelationsPref) -> ExpandGRMRelationsResponse:
        """    
             Returns the secondary objects related to the input object for the given list of relation
             names and other side object types filter. If no relation names or other side objects
             types are provided in the input, then all related objects will be returned. In addition,
             for performance, if an Item is the output of the expansion, then its associated Item
             Revisions and the Datasets for those Item Revisions will be returned. Similarly,
             if an Item Revision is the output of the expansion, then its associated Datasets
             will be returned. However this additional expansion is controlled through the expItemRev
             flag.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Objects: 
                         A list of object references of objects of interest
             
        :param Pref: 
                         A ExpandGRMRelationsPref structure
             
        :return: contains a list of ExpandGRMRelationsOutput structures (which contain information
             about the input TcEng Object, filtered Otherside related objects and the relationName
             they are related). Failures and error message are in the ServiceData.
        """
        ...
    def ExpandPrimaryObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: ExpandPrimaryObjectsPref) -> ExpandPrimaryObjectsResponse:
        """    
             Returns the secondary objects related to the input object for the given list of relation
             names and other side object types filter. If no relation names or other side objects
             types are provided in the input, then all related objects will be returned. In addition,
             for performance, if an Item is the output of the expansion, then its associated Item
             Revisions and the Datasets for those Item Revisions will be returned. Similarly,
             if an Item Revision is the output of the expansion, then its associated Datasets
             will be returned. However this additional expansion is controlled through the expItemRev
             flag.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Objects: 
                         A list of input TcEng object references and filter and expand preferences
             
        :param Pref: 
                         A ExpandPrimaryObjectsPref structure
             
        :return: contains a list of ExpandPrimaryObjectsOutput structures (which contain information
             about the input TcEng Object, filtered Otherside related objects and the relation/property
             Name they are related). Failures and error message are in the ServiceData.
        """
        ...
    def GenerateAlternateIds(self, Input: list[GenerateAlternateIdsProperties]) -> GenerateAlternateIdsResponse:
        """    
             Generate a list of alternate ids. An alternate id is a displayable id for an Item
             or ItemRevision that is controlled by the user via display rules. The client
             creates Identifiers that contain the various alternate ids to be displayed.
             Each Identifier is controlled by a display rule. When a display rule is active
             then the appropriate alternate id is displayed.
             

Use Cases:

             The client defines several alternate ids for a part. One alternate id is for the
             manufacturer of the part( this would be their part number ), another would be for
             a customer ( their part number ) and maybe one for a second customer ( again, another
             part number ). This service allows the client to invoke the user exit USER_new_alt_id.
             This exit will be called once for each count specified in the input using the data
             passed in as parameters.
             

Dependencies:

             getContextsAndIdentifierTypes
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         A list of <font face="courier" height="10">GenerateAlternateIdsProperties</font>.
             
        :return: Contains the map of index to list of ids generated. The index refers to the input
             data in the input list.
        """
        ...
    def GetAllAttrMappings(self) -> GetAllAttrMappingsResponse:
        """    
             Retrieves all CAD attribute mapping definitions. Additionally, if a CadAttributeMappingDefinition
             object has a path that includes a GRM or NR part, the associated PropertyDescriptor
             and any attached ListOfValues objects will be returned.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :return: 
        """
        ...
    def GetAttrMappingsForDatasetType(self, Info: list[GetAttrMappingsForDatasetTypeCriteria]) -> GetAttrMappingsForDatasetTypeResponse:
        """    
             This operation retrieves the CAD attribute mapping definitions for one or more dataset
             type and item type combinations.  If a CadAttributeMappingDefinition
             object has a path that includes a Generic Relationship Manager (GRM) or named reference
             part, the associated property descriptor and any attached ListOfValues
             (LOV) objects will be returned.
             

             Since this operation returns existing Teamcenter attribute mappings, please reference
             the Teamcenter help section on creating attribute mappings.
             


Use Cases:

             User needs to have attribute mappings defined in Teamcenter.
             

             For this operation, the dataset object type is passed as input. The client application
             uses the list of returned attribute mapping definitions to present the CAD attributes
             to the user that correspond to the correct Teamcenter attributes.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         A list of dataset and item types used to get a specific set of attribute mapping
                         definitions from the all of the attribute mapping definitions in Teamcenter.
             
        :return: 
        """
        ...
    def GetAvailableTypes(self, Classes: list[str]) -> GetAvailableTypesResponse:
        """    
             Finds types implemented by the given input class name.
             

Use Cases:

             User selects File New Item and is presented with a list of creatable item types.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Classes: 
                         A list of the classes to return subtypes for
             
        :return: with original input class string mapped to error message.
        """
        ...
    def ResolveAttrMappingsForDataset(self, Info: list[ResolveAttrMappingsForDatasetInfo]) -> ResolveAttrMappingsForDatasetResponse:
        """    
             Retrieves CAD attribute mapped properties for one or more datasets.
             

Use Cases:

             User does a FileOpen of Teamcenter Item or Dataset (CAD Part).  CAD properties mapped
             to Teamcenter attribute values are shown in the Part attribute display.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         An array of <font face="courier" height="10">ResolveAttrMappingsForDatasetInfo</font>
                         structures each containing a <b>Dataset</b> object reference, an optional item revision,
                         and a list of corresponding CAD Attribute Mapping Definitions to be resolved for
                         the dataset. The optional item revision is recommended for improved performance in
                         cases where resolution of the mapping string would otherwise require a relation query
                         to find the item revision.
             
        :return: 
        """
        ...
    def ExpandFoldersForCAD(self, Folders: list[Teamcenter.Soa.Client.Model.Strong.Folder], Pref: ExpandFolderForCADPref) -> ExpandFoldersForCADResponse:
        """    
             The purpose of this service is to provide the contents of a folder that a CAD integration
             typically needs in one service call as opposed to multiple expand calls. This service
             is specifically for Folder expansion and will only return Items, Item Revisions and
             Folders that are contained in the input Folder. Other types of objects (Forms, Datasets,
             etc...) that are contained directly under the input folder will not be returned.
             The service will also return the Item Revisions and Datasets for the Items found
             in the folder and Datasets found for the Item Revisions found directly under the
             folder. The Item Revisions returned, are controlled thru an input latestNRevs specifying
             how many latest revisions should be sent to output. The Items, Item Revisions and
             Datasets returned can be filtered thru an input preference of a list of relation
             names and dataset types filter.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Folders: 
                         A list of input TcEng folders
             
        :param Pref: 
                         Filter and expand preferences
             
        :return: contains a list of ExpandFoldersForCADOutput structures (which contain information
             about the input TcEng folder, and filtered folder contents viz. folders, items and
             itemRevs). Failures and error message are in the ServiceData.
        """
        ...

