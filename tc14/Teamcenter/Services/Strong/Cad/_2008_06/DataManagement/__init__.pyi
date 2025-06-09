import System
import Teamcenter.Services.Strong.Cad._2007_01.DataManagement
import Teamcenter.Services.Strong.Cad._2007_12.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeInfo:
    """
    
            This structure allows the caller define or update named attributes. The name member
            represents the property name for the related object and the value is the value to
            set.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Text for attribute name"""
    Values: list[str]
    """Text for attribute value"""

class BoundingBox:
    """
    Holds the boundingbox co-ordinates  information.
    """
    def __init__(self, ) -> None: ...
    Xmin: float
    """BoundingBox x-coordinate min value in double"""
    Ymin: float
    """BoundingBox y-coordinate min value in double"""
    Zmin: float
    """BoundingBox z-coordinate min value in double"""
    Xmax: float
    """BoundingBox x-coordinate max value in double"""
    Ymax: float
    """BoundingBox y-coordinate max value in double"""
    Zmax: float
    """BoundingBox z-coordinate max value in double"""

class CommitDatasetFileInfo:
    """
    Holds the basic info for a file to be uploaded to a dataset.
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference."""
    CreateNewVersion: bool
    """Flag to create new version ( TRUE ) or not ( FALSE )."""
    DatasetFileTicketInfos: list[DatasetFileTicketInfo]
    """
            A list of DatasetFileTicketInfos which contains
            file ticket information for the dataset file.
            """

class CreateOrUpdatePartsOutput:
    """
    Contains the output response structure for createOrUpdateParts operation.
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
    ExtraItemObjs: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExtraObjectOutput]
    """List of ExtraObjectOutputs for the item extra objects"""
    ExtraItemRevObjs: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExtraObjectOutput]
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
    BoundingBoxesAvailable: bool
    """Flag to indicate BoundingBoxes are available."""
    BoundingBoxes: list[BoundingBox]
    """List of BoundingBoxes."""

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
    Contains created/updated dataset.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by user to track the related object."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference of the created/updated dataset"""
    CommitInfo: list[CommitDatasetFileInfo]
    """List of CommitDatasetFileInfos"""
    ExtraObjs: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExtraObjectOutput]
    """
            List of ExtraObjectOutputs for the extra
            objects
            """
    NamedRefObjs: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExtraObjectOutput]
    """
            List of ExtraObjectOutputs for the named
            references
            """

class ExpandFolderForCADPref2:
    """
    
            Contains a list of RelationAndTypesFilter,
            number of latest revisions for further filtering and a flag to check whether item
            revision needs to be expanded and list of other object types to return from the folder
            contents.
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """
            Flag to specify if the datasets attached to the item revisions are to be returned.
            If set to TRUE then all datasets owned by each item revision will be returned with
            the item revision.
            """
    LatestNRevs: int
    """
            The number of revisions under an item that should be considered for further filtering.
            If there are 5 versions of an item and this option is set to 2 then versions 4 and
            5 will be processed. 0 = do not return any item revisions. minus 1 = return all item
            revisions.
            """
    Info: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.RelationAndTypesFilter2]
    """
            A list of RelationAndTypesFilter2 structures
            to select the datasets under an item revision to return. If empty then all dataset
            will be returned.
            """
    ContentTypesFilter: list[str]
    """
            A list of object types. Any objects in any input folder that are of the type in this
            list will also be returned.
            """

class ExpandFoldersForCADOutput2:
    """
    
            Contains the folder expanded and the results of expanding the folder based on the
            input preference.
            
    """
    def __init__(self, ) -> None: ...
    InputFolder: Teamcenter.Soa.Client.Model.Strong.Folder
    """The folder that was expanded."""
    FstlvlFolders: list[Teamcenter.Soa.Client.Model.Strong.Folder]
    """A list of folders contained by the input folder."""
    ItemsOutput: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandFoldersForCADItemOutput]
    """
            A list of ExpandFolderForCADItemOutput which
            has information about the items in the folder.
            """
    ItemRevsOutput: list[Teamcenter.Services.Strong.Cad._2007_01.DataManagement.ExpandFoldersForCADItemRevOutput]
    """
            A list of ExpandFolderForCADItemRevOutput
            which has information about the item revisions in the folder.
            """
    Contents: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            A list of objects in the folder that are a type listed in the contentTypesFilter input.
            """

class ExpandFoldersForCADResponse2:
    """
    
            Contains the response for ExpandFoldersForCAD
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandFoldersForCADOutput2]
    """
            A list of ExpandFoldersForCADOutput2 which
            has information about the input folder and folders, items and item revisions output
            found under this folder
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the folders, items, items revisions, datasets, and other object types in
            the list of plain objects.
            
            Error information returned is identified by the folder tag sent to the service and
            will include system errors plus errors generated by this service :
            
            7007 : Input folder is invalid.
            
            215121 : Object passed in is not a folder.
            
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

class ItemInfo:
    """
    
            the ItemInfo structure represents all of the data necessary to construct the item
            object. The basic attributes that are required are passed as named elements in the
            structure. All other attributes are passed as name/value pairs in the AttributeInfo
            structure. The extraObject field allows for the creation of an object(s) that will
            be related to this newly created Item.
            
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
    
            the ItemRevInfo structure represents all of the data necessary to construct the item
            revision object. The basic attributes that are required are passed as named elements
            in the struct. All other attributes are passed as name/value pairs in the AttributeInfo
            structure. The extraObject field allows for the creation of an object(s) that will
            be related to this newly created Item Revision.
            
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

class NamedReferenceObjectInfo:
    """
    
            Contains information regarding named reference type value, object reference, object
            type name and list of attribute information to set on the object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier defined by client to track the related object."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Object reference of the object for update, null for create."""
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
    AttrNameValuePairs: list[AttributeInfo]
    """List of attribute information."""

class PartInfo:
    """
    
            The PartInfo struct is the main input to the createOrUpdateParts service for boundingbox.
            This structure refers to the Item, ItemRevision, and one or more Dataset structures
            used to create those objects.
            
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

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateParts(self, PartInput: list[PartInfo], Pref: Teamcenter.Services.Strong.Cad._2007_12.DataManagement.CreateOrUpdatePartsPref) -> CreateOrUpdatePartsResponse:
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
    def ExpandFoldersForCAD(self, Folders: list[Teamcenter.Soa.Client.Model.Strong.Folder], Pref: ExpandFolderForCADPref2) -> ExpandFoldersForCADResponse2:
        """    
             The purpose of this service is to provide the contents of a folder that a CAD integration
             typically needs in one service call as opposed to multiple expand calls. This service
             is specifically for folder expansion and will only return items, item revisions and
             folders that are contained in the input folder. Other types of objects ( forms, datasets,
             etc.. ) that are contained directly under the input folder can be returned if their
             type is specified in the preference. The service will also return the item revisions
             and datasets for the items found in the folder and datasets found for the item revisions
             found directly under the folder. The item revisions returned, are controlled thru
             an input latestNRevs specifying how many
             latest revisions should be sent to output. The items, item revisions and datasets
             returned can be filtered thru an input preference of a list of relation names and
             dataset types filter.
             

Use Cases:

             A CAD application needs to know what objects in the database are relative to the
             cad application. The CAD application can get the contents of the home folder and
             display to the user. If the user then selects a subfolder of home then the application
             can expand that folder to get to the desired data. This service will return objects
             that the cad application understands such as subfolders, items, item revisions and
             datasets and other objects of the type the application specifies in the input filter.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Folders: 
                         A list of folders to expand.
             
        :param Pref: 
                         Filter and expand preferences
             
        :return: .
        """
        ...

