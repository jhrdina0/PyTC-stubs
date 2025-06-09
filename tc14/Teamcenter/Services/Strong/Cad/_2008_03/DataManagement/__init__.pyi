import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2007_01.DataManagement
import Teamcenter.Services.Strong.Cad._2007_12.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CadAttrMappingDefinitionInfo:
    """
    
            Contains unique clientId and CadAttributeMappingDefinition object reference associated with
            the resolved property object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Unique client side identifier. This is a required input parameter If the ClientId is not provided or not unique a partial error is reported
            and the property for the particular CADAttrMappingDefinition
            will not resolved.
            """
    CadAttrMappingDefinition: Teamcenter.Soa.Client.Model.Strong.CadAttrMappingDefinition
    """
CadAttributeMappingDefinition object reference associated with the resolved
            property object
            """

class DatasetInfo3:
    """
    
            The DatasetInfo3 struct represents all of the data necessary to construct the dataset
            object. The basic attributes that are required are passed as named elements in the
            struct. All other attributes are passed as name/value pairs in the AttributeInfo
            struct. The extraObject field allows for the creation of an object(s) that will be
            related to this newly created Dataset.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference for update, null for creation"""
    Name: str
    """Name attribute value"""
    BasisName: str
    """Basis Name attribute value, used when the name is null or blank"""
    Description: str
    """Description attribute value"""
    Type: str
    """Type attribute value"""
    LastModifiedOfDataset: System.DateTime
    """Last Modified Date of dataset"""
    Id: str
    """ID attribute value"""
    DatasetRev: str
    """Revision attribute value"""
    ItemRevRelationName: str
    """Required input, may not be null, not defaulted"""
    CreateNewVersion: bool
    """Flag to create new version ( TRUE ) or not (FALSE )"""
    MapAttributesWithoutDataset: bool
    """
            Flag to indicate whether DatasetInfo should be used for mapping attributes or for
            create.
            """
    NamedReferencePreference: str
    """
            Preference name which holds the list of named references to delete from one Dataset
            version to the next.
            """
    AttrList: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.AttributeInfo]
    """List of AttributeInfos for attributes"""
    MappingAttributes: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.AttributeInfo]
    """
            List of AttributeInfos for mapped attributes. Mapped atributes are attributes that
            are applied to other objects. Refere to the ITK manual for a definition of attribute
            mapping.
            """
    ExtraObject: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExtraObjectInfo]
    """List of ExtraObjectInfos"""
    DatasetFileInfos: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.DatasetFileInfo]
    """List of DatasetFileInfos"""
    NamedReferenceObjectInfos: list[Teamcenter.Services.Strong.Cad._2007_12.DataManagement.NamedReferenceObjectInfo2]
    """List of NamedReferenceObjectInfos"""

class MappedDatasetAttrPropertyInfo:
    """
    
            Contains resolved object and property name along with CadAttrMappingDefinition
            object reference associated with the resolved property object.
            
    """
    def __init__(self, ) -> None: ...
    CadAttrMappingDefinition: Teamcenter.Soa.Client.Model.Strong.CadAttrMappingDefinition
    """
CadAttrMappingDefinition object reference associated with the resolved property
            Object.
            """
    ResolvedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of object holding mapped attribute value"""
    ResolvedPropertyName: str
    """
            The property name of the mapped object holding the attribute value of interest resulting
            from evaluation of a dataset CAD attribute mapping definition.
            """

class PartInfo3:
    """
    
            The PartInfo3 struct is the main input to the createOrUpdateParts service. This structure
            refers to the Item, ItemRevision, and one or more Dataset structures used to create
            those objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    ItemInput: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ItemInfo
    """Member of type ItemInfo"""
    ItemRevInput: Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ItemRevInfo
    """Member of type ItemRevInfo"""
    DatasetInput: list[DatasetInfo3]
    """List of DatasetInfo3"""

class ResolveAttrMappingsInfo:
    """
    
            Contains dataset, item revision and list of CadAttrMappingDefinition
            object references to use to resolve the mapping.
            
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
Dataset object reference to use as starting point to get mapped attribute
            values.
            """
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
ItemRevision object reference helps resolve ambiguity in the mapping traversal
            for the dataset or can be the starting point for the traversal as well.
            """
    MappingDefinitionInfos: list[CadAttrMappingDefinitionInfo]
    """List of CadAttrMappingDefinitionInfo objects"""

class ResolveAttrMappingsResponse:
    """
    
            Holds the response for resolveAttrMappings. The processing of the input is as follows
            :
            
            1.Â Â Â Â Process the ResolveAttrMappingsInfo first. This will validate
            the dataset and item revision inputs are valid. If this validation fails, then an
            error will be returned with the index of the ResolveMappinsInfo being the identifier
            with the error.
            
            2.Â Â Â Â Process the list of CadAttrMappingDefinitionInfo. If this
            results in an error then the identifier for the error will be the clientId specified
            in the CadAttributeMappingDefinition.
            
            When processing the output, if a key with thte clientId is not found, the application
            should first look for an error with an identifier of the cleintId. If no error is
            found then the index of the input that contained the clientId should be found.
            

    """
    def __init__(self, ) -> None: ...
    ResolvedMappingsMap: System.Collections.Hashtable
    """
            Member of type ResolveAttrMappingsOutputMap.
            This is a map containing the successfully mapped property information. The keys are
            the input clientIds and the values are the
            output MappedDatasetAttrPropertyInfo structures.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains any partial errors and exceptions. The objects holding the
            mapped attributes, resulting from successfully resolved mappings, are returned as
            plain objects. The mapped attribute properties are returned as ServiceData properties.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateParts(self, Info: list[PartInfo3], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdatePartsResponse:
        """    
             CreateOrUpdateParts allows the user to create or update a set of parts using Items,
             Item Revisions, Datasets and ExtraObjects and also changes the ownership of the newly
             created object to the user/group supplied. If the user supplies a valid Item object
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
                         A list of PartInfo3 structures
             
        :param Pref: 
                         A Struct which contains information whether dataset needs to be modified, if input
                         last modified date is different from actual.
             
        :return: contains a list of CreateOrUpdatePartsOutput structures (which contain information
             about the item, itemrevisions. datasets and extra objects ). Failure will be with
             client id and error message in the ServiceData.
        """
        ...
    def ResolveAttrMappings(self, Info: list[ResolveAttrMappingsInfo]) -> ResolveAttrMappingsResponse:
        """    
             Retrieves CAD attribute mapped properties for item revisions or datasets.  Attribute
             Mapping is a scheme whereby Teamcenter attributes can be retrieved or set via a defined
             path to the attribute from the starting object, usually a dataset.  For example,
             a mapped attribute can be defined in the client integration with a particular name
             ATTR1.  Using Teamcenter attribute mapping, the customizer can define a path named
             ATTR1 from a starting point item revision type or dataset type to the actual attribute
             that holds the value for ATTR1. The client integration then can access the attribute
             using the attribute mapping title ATTR1 and the starting point object.
             
             For more information about Attribute Mapping including examples with syntax, please
             consult the "Configuring attribute mapping section" of the Application Administration
             Guide in Teamcenter Online Help.
             

Use Cases:

             A user performs a File Open operation on an existing Teamcenter dataset.  The client
             integration has defined an attribute mapping in Teamcenter for that Dataset type.
             The resolveAttrMappings call performed as a part of the File Open, sends the mapping
             definition, defined by the mapping title, and the Dataset as input.  The operation
             traverses from the input Dataset to the mapped property which in this case resides
             on the Datasets parent Item Revision.  The operation will return the item revision
             and the mapped property name such that the client integration can retrieve the property
             value from the item revision.  The value is then displayed in the attribute data
             for the dataset in the client integration.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         An array of ResolveAttrMappingsInfo structures each containing a <b>Dataset</b> object
                         reference, an optional item revision, and a list of corresponding CAD Attribute Mapping
                         Definitions to be resolved for the dataset.
             
        :return: 
        """
        ...

