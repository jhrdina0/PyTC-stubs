import System
import Teamcenter.Services.Strong.Cad._2007_12.DataManagement
import Teamcenter.Services.Strong.Cad._2008_06.DataManagement
import Teamcenter.Soa.Client.Model.Strong
import typing

class DatasetFileInfo:
    """
    Holds the basic info for a file to be uploaded to a Dataset.
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
    BoundingBoxesAvailable: bool
    """Flag to indicate BoundingBoxes are available."""
    DestinationVolume: Teamcenter.Soa.Client.Model.Strong.ImanVolume
    """
            Destination volume into which the file will be uploaded. If null tag the current
            default volume of the user will be used.
            """
    BoundingBoxes: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.BoundingBox]
    """List of BoundingBoxes."""

class DatasetInfo:
    """
    
            The DatasetInfo struct represents all of the data necessary to construct the dataset
            object. The basic attributes that are required are passed as named elements in the
            structure. All other attributes are passed as name/value pairs in the AttributeInfo
            structure. The extraObject field allows for the creation of an object(s) that will
            be related to this newly created Dataset.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference for update, null for creation"""
    Name: str
    """Name attribute value"""
    BasisName: str
    """basisName"""
    Description: str
    """Description attribute value"""
    Type: str
    """Type attribute value"""
    LastModifiedOfDataset: System.DateTime
    """lastModifiedOfDataset"""
    Id: str
    """ID attribute value"""
    DatasetRev: str
    """Revision attribute value"""
    ItemRevRelationName: str
    """Can be null, defaulted"""
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
            version to the next
            """
    AttrList: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.AttributeInfo]
    """List of AttributeInfos for attributes"""
    MappingAttributes: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.AttributeInfo]
    """
            List of AttributeInfos for mapped attributes. Mapped atributes are attributes that
            are applied to other objects. Refere to the ITK manual for a definition of attribute
            mapping.
            """
    ExtraObject: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.ExtraObjectInfo]
    """List of ExtraObjectInfos"""
    DatasetFileInfos: list[DatasetFileInfo]
    """List of DatasetFileInfos"""
    NamedReferenceObjectInfos: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.NamedReferenceObjectInfo]
    """List of NamedReferenceObjectInfos"""
    DatasetTool: str
    """
            The dataset tool for the dataset. If not specified then the default tool will be
            used.
            """

class PartInfo:
    """
    
            The PartInfo struct is the main input to the createOrUpdateParts service for boundingbox.
            This structure refers to the Item, ItemRevision, and one or more Dataset structures
            used to create those objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    ItemInput: Teamcenter.Services.Strong.Cad._2008_06.DataManagement.ItemInfo
    """Member of type ItemInfo"""
    ItemRevInput: Teamcenter.Services.Strong.Cad._2008_06.DataManagement.ItemRevInfo
    """Member of type ItemRevInfo"""
    DatasetInput: list[DatasetInfo]
    """List of DatasetInfos"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateParts(self, PartInput: list[PartInfo], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> Teamcenter.Services.Strong.Cad._2008_06.DataManagement.CreateOrUpdatePartsResponse:
        """    
             CreateOrUpdateParts allows the user to update or create a set of parts using Items,
             Item Revisions, and Datasets and save the boudingbox information related to these
             objects. The service first attempts to validate the existence of the Item, Item Revision,
             and Dataset. If the Item and Item Revision already exist, but the Dataset does not,
             then only the Dataset is created. If the Dataset exists, a new version will be added
             to the existing series. If any of the objects exist but the input attribute values
             that differ from those already set, attempts are made to update the values if possible.
             If the boundingbox information exists it saves that information on that particular
             dataset else it willnot save the boudingbox information. If no item object reference
             or item revision object references are specified then a new item and item revision
             and related objects will be created. All objects created and updated will be returned
             in the ServiceData. All partial errors will contain the clientIDs for all items related
             to the error message, i.e. if a dataset encounters an error, then the ID for that
             erro will be the item client ID concantentated with the item revision id contantenated
             with the dataset client ID, all separated by semi-colons ( ; ).
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param PartInput: 
                         A list of PartInfo structures
             
        :param Pref: 
                         A Struct which contains information whether dataset needs to be modified, if input
                         last modified date is different from actual
             
        :return: contains a list of CreateOrUpdatePartsOutput structures (which contain information
             about the item, itemrevisions. datasets and extra objects ). Failure will be with
             client id and error message in the ServiceData.
        """
        ...

