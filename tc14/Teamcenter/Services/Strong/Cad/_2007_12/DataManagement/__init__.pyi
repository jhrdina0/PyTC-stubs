import System
import Teamcenter.Services.Strong.Cad._2007_01.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdatePartsPref:
    """
    Input structure for CreateOrUpdatePartsPref
    """
    def __init__(self, ) -> None: ...
    OverwriteForLastModDate: bool
    """
            Flag to check whether dataset needs to be modified, if input last modified date is
            different from actual.
            """

class DatasetInfo2:
    """
    
            The DatasetInfo2 struct represents all of the data necessary to construct the dataset
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
    NamedReferencePreference: str
    """
            Preference name which holds the list of named references to delete from one Dataset
            version to the next
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
    NamedReferenceObjectInfos: list[NamedReferenceObjectInfo2]
    """List of NamedReferenceObjectInfos"""

class NamedReferenceObjectInfo2:
    """
    Contains information for object named references to apply to the Dataset.
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
    NamedReferenceType: str
    """
            The reference type name from the dataset to this object, must be either AE_ASSOCIATION
            or AE_PART_OF.
            """
    TypeName: str
    """Type of the object to be created. Required for object creation only."""
    AttrNameValuePairs: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.AttributeInfo]
    """List of AttributeInfos."""

class PartInfo2:
    """
    
            The PartInfo2 struct is the main input to the createOrUpdateParts service. This structure
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
    DatasetInput: list[DatasetInfo2]
    """List of DatasetInfo2"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateParts(self, Info: list[PartInfo2], Pref: CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2007_01.DataManagement.CreateOrUpdatePartsResponse:
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
                         A list of PartInfo2 structures
             
        :param Pref: 
                         A Struct which contains information whether dataset needs to be modified, if input
                         last modified date is different from actual.
             
        :return: contains a list of CreateOrUpdatePartsOutput structures (which contain information
             about the item, itemrevisions. datasets and extra objects ). Failure will be with
             client id and error message in the ServiceData.
        """
        ...

