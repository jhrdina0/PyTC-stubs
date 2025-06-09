import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2007_12.DataManagement
import Teamcenter.Services.Strong.Cad._2008_06.DataManagement
import Teamcenter.Services.Strong.Cad._2010_09.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateInput:
    """
    
            The CreateOrUpdateInput structure represents
            all of the data necessary to construct a business object. All attributes are passed
            in as name/value pairs for the corresponding value type map.
            
            The compoundCreateOrUpdateInput field allows
            for the creation of a secondary object(s) for the newly created primary object.
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business Object type name. This field must be specified for create."""
    BoReference: Teamcenter.Soa.Client.Model.ModelObject
    """Existing object reference. This field must be specified for update."""
    StringProps: System.Collections.Hashtable
    """A map (string/string) of property names to a single value."""
    StringArrayProps: System.Collections.Hashtable
    """A map (string/list of strings) of property names to a list of values."""
    DoubleProps: System.Collections.Hashtable
    """A map (string/double) of property names to a single value."""
    DoubleArrayProps: System.Collections.Hashtable
    """A map (string/list of doubles) of property names to a list of values."""
    FloatProps: System.Collections.Hashtable
    """A map (string/float) of property names to a single value."""
    FloatArrayProps: System.Collections.Hashtable
    """A map (string/list of floats) of property names to a list of values."""
    IntProps: System.Collections.Hashtable
    """A map (string/integer) of property names to a single value."""
    IntArrayProps: System.Collections.Hashtable
    """A map (string/list of integers) of property names to a list of values."""
    BoolProps: System.Collections.Hashtable
    """A map (string/boolean) of property names to a single value."""
    BoolArrayProps: System.Collections.Hashtable
    """A map (string/list of booleans) of property names to a list of values."""
    DateProps: System.Collections.Hashtable
    """A map (string/datetime) of property names to a single value."""
    DateArrayProps: System.Collections.Hashtable
    """A map (string/list of datetimes) of property names to a list of values."""
    TagProps: System.Collections.Hashtable
    """A map (string/business object) of property names to a single value."""
    TagArrayProps: System.Collections.Hashtable
    """A map (string/list of business objects) of property names to a list of values."""
    CompoundCreateOrUpdateInput: System.Collections.Hashtable
    """
CreateOrUpdateInput for secondary (compounded)
            objects
            """

class DatasetInfo:
    """
    
            The DatasetInfo struct represents all of
            the data necessary to construct the Dataset object. The basic attributes that
            are required are passed as named elements in the structure. All other attributes
            are passed as name/value pairs in the AttributeInfo
            structure: attrList. The extraObject field
            allows for the creation of an object(s) that will be related to this newly created
            Dataset.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    CreateOrUpdateInput: CreateOrUpdateInput
    """
CreateOrUpdateInput object which contains
            attributes to create a Dataset. createOrUpdateInput
            can be null for update.
            """
    BasisName: str
    """
            Basis name attribute value. When the dataset name is blank, the basis name is used
            to call USER_new_dataset_name to generate a new name.
            """
    LastModifiedOfDataset: System.DateTime
    """
            If not null, the date and time that the Dataset was last modified. If the
            actual modified date and time is later, then an error is thrown.
            """
    ItemRevRelationName: str
    """
            The relation name for the Dataset to ItemRevision relation. Can be
            null, but is required if an ItemRevision is specified.
            """
    CreateNewVersion: bool
    """Flag to create new version ( TRUE ) or not (FALSE )."""
    MapAttributesWithoutDataset: bool
    """
            Flag to indicate whether DatasetInfo should
            be used for mapping attributes or for create.
            """
    NamedReferencePreference: str
    """
            Preference name which holds the list of named references to delete from one Dataset
            version to the next.
            """
    MappingAttributes: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.AttributeInfo]
    """
            List of AttributeInfos for mapped attributes.
            Mapped attributes are attributes that are applied to other objects. Refer to the
            ITK manual for a definition of attribute mapping.
            """
    ExtraObject: list[ExtraObjectInfo]
    """
            List of ExtraObjectInfos, the extra objects
            to be created and related to the Dataset.
            """
    DatasetFileInfos: list[Teamcenter.Services.Strong.Cad._2010_09.DataManagement.DatasetFileInfo]
    """
            List of DatasetFileInfos, which holds the
            basic information for a file to be uploaded to a Dataset.
            """
    NamedReferenceObjectInfos: list[NamedReferenceObjectInfo]
    """
            List of NamedReferenceObjectInfos, contains
            information regarding named reference type value, object reference, object type name
            and list of attribute information to set on the object.
            """

class ExtraObjectInfo:
    """
    
            Form objects that can be created or updated and related to an item, item revision
            or dataset.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    CreateOrUpdateInput: CreateOrUpdateInput
    """
            CreateOrUpdateInput object which contains attributes to create an extra object. createOrUpdateInput
            can be null for update.
            """
    RelationTypeName: str
    """Name of the relation type to the parent object"""

class ItemInfo:
    """
    
            The ItemInfo structure represents all of
            the data necessary to construct the item object. The basic attributes that are required
            are passed as named elements in the structure. All other attributes are passed as
            name/value pairs in the AttributeInfo structures:
            attrList and formAttrList.
            The extraObject field allows for the creation
            of an object(s) that will be related to this newly created Item.
            
    """
    def __init__(self, ) -> None: ...
    CreateOrUpdateInput: CreateOrUpdateInput
    """
CreateOrUpdateInput object which contains
            attributes to create an Item. createOrUpdateInput
            can be null for update.
            """
    ItemExtraObject: list[ExtraObjectInfo]
    """List of extra objects to be used or created and related to the Item."""
    ItemRevisionExtraObject: list[ExtraObjectInfo]
    """List of extra objects to be used or created and related to the Item Revision."""
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """
            Folder to attach the Item to. If null, then the Teamcenter preference WsoInsertNoSelectionsPref
            is used to get the default location.
            """

class NamedReferenceObjectInfo:
    """
    
            Contains information regarding named reference type value, object reference, object
            type name and list of attribute information to set on the object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by client to track the related object."""
    CreateOrUpdateInput: CreateOrUpdateInput
    """
            Object that contains attributes to create
            a named reference object. createOrUpdateInput
            can be null for update.
            """
    NamedReferenceName: str
    """
            The named reference from the dataset to this object and a required input. Named reference
            name values  are defined for each dataset type. The customer can add more values
            as needed. To get a current list of valid named reference name values the programmer
            can either use the Business Modeler IDE or can call the Core service getDatasetTypeInfo.
            """
    NamedReferenceType: str
    """
            The reference type name from the dataset to this object, must be either AE_ASSOCIATION
            or AE_PART_OF.
            """

class PartInfo:
    """
    
            The PartInfo struct is the main input to
            the createOrUpdateParts service for boundingbox.
            This structure refers to the item and one or more dataset structures used to create
            those objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by the user to track the related object."""
    ItemInput: ItemInfo
    """Member of type ItemInfo."""
    DatasetInput: list[DatasetInfo]
    """List of DatasetInfos."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateParts(self, PartInput: list[PartInfo], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.CreateOrUpdatePartsResponse:
        """    
CreateOrUpdateParts allows the user to create
             or update a set of Items, ItemRevisions, and Datasets (CAD concept
             of a Part includes these Teamcenter objects). The service first attempts to validate
             the existence of the Item, ItemRevision, and Dataset. If the
             Item already exist,s but the ItemRevision does not, then a new initial
             ItemRevision is created-any existing ItemRevisions are not revised.
             If the Item and ItemRevision already exist, but the Dataset
             does not, then only the Dataset is created. If the Dataset exists,
             a new version will be added to the existing series. If any of the objects exist but
             the input attribute values that differ from those already set, attempts are made
             to update the values if possible. If no Item object reference or ItemRevision
             object references are specified then a new Item and ItemRevision and
             related objects will be created. All objects created and updated will be returned
             in the ServiceData. All partial errors will
             contain the clientIDs for all items related
             to the error message, i.e. if a dataset encounters an error, then the ID for that
             error will be the item client ID concatenated with the item revision id concatenated
             with the dataset client ID, all separated by semi-colons ( ; ).
             

Use Cases:

             User wants to create a new CAD Part (item, item revision, and dataset). User fills
             in the CreateOrUpdateInput structure with
             the information for the item and item ievision.
             

             User wants to create an item and item revision with one or more datasets. Client
             fills in the CreateOrUpdateInput structure
             with the information for the item and item revision from the user. Client also fills
             in one or more DatasetInfos with the information
             about the datasets to create from the user. Upon return from the service, the client
             will extract the FileTickets from the DatasetOutputs and upload the data files for the
             datasets using FMS. Once the uploads have completed, then the client will use the
             DatasetCommitInfos to attach the upload files
             to the datasets using the Core Services commitDatasetFiles.
             

             User wants to modify properties on an item, item revision or dataset. Client fills
             in the CreateOrUpdateInput structure with
             the new information for the item or item revision. Client fills in the new information
             in a DatasetInfo structure then invokes the
             service using an existing item or item revision or dataset.
             

User wants to create or update an existing item and/or item revision with
             User created Form object. The client fills in the necessary data to create or update
             an item and/or item revision. The client also specifies itemExtraObjectInfo
             and/or itemRevisionExtraObjectInfo containing
             the form and relation to be used to attach the form to another object.
             

User wants to add objects to a dataset. This can be done as Extra Objects
             or using the NamedReference feature. The user fills in the information necessary
             to create or update a dataset. The user can then specify ExtraObjectInfo
             data for attaching forms or NamedReferenceObjectInfo
             for other objects.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param PartInput: 
                         A list of <font face="courier" height="10">PartInfo</font> structures
             
        :param Pref: 
                         A Struct which contains information whether dataset needs to be modified, if input
                         last modified date is different from actual
             
        :return: .
        """
        ...

