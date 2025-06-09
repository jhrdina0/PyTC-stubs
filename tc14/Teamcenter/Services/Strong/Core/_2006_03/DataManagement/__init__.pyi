import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateDatasetsOutput:
    """
    This structure contains information for createDatasets operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created."""
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference that was created"""

class CreateDatasetsResponse:
    """
    Return structure for createDatasets operation
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateDatasetsOutput]
    """A list of created Dataset output"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class CreateFolderInput:
    """
    Input structure for createFolders operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object created, optional."""
    Name: str
    """
            Name of the folder to be created, optional, if null, uses value from USER_new_folder_name
            user exit
            """
    Desc: str
    """Description of the folder to be created, optional"""

class CreateFoldersOutput:
    """
    
            This structure contains information for createFolders
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object created."""
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """Folder object reference that was created"""

class CreateFoldersResponse:
    """
    Return structure for createFolders operation
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateFoldersOutput]
    """
            Each element in the list contains a client Id and the related Folder object
            created.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class CreateItemsOutput:
    """
    The data structure contains a list of created items and item revisions.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created."""
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """The created Item object"""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The created ItemRevision object"""

class CreateItemsResponse:
    """
    Return structure for createItems operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateItemsOutput]
    """A list of the created Item and ItemRevision"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data"""

class CreateRelationsOutput:
    """
    The relations created between the primary and secondary object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the Relationship.clientId.
            This can be used by the caller to indentify this data structure with the source input
            data.
            """
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    """The newly created relation."""

class CreateRelationsResponse:
    """
    
CreateRelationsResponse structure represents
            the relations created between the primary and secondary object and errors occurred.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateRelationsOutput]
    """A list of created relations."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData object to hold the partial
            errors that the operation encounters.
            """

class DatasetProperties:
    """
    Input structure for createDatasets operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Identifier that helps the client to track the object(s) created, required, should
            be unique for the input set
            """
    Type: str
    """Type of the Dataset to be created"""
    Name: str
    """Name of the Dataset to be created"""
    Description: str
    """Description of the Dataset to be created, may be an empty string"""
    ToolUsed: str
    """
            Name of the Tool used to open the created Dataset, may be an empty
            string.
            """
    Container: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object reference of the container used to hold the created Dataset, may be
            an empty string
            """
    RelationType: str
    """Name of the relation type for the Dataset to be created, may be an empty string."""

class ExtendedAttributes:
    """
    
            This structure contains information for createItems
            operation to support setting attribute values on the created Item, ItemRevision,
            or corresponding master forms that may be created with the objects.
            
    """
    def __init__(self, ) -> None: ...
    ObjectType: str
    """The type of object to set these properties on i.e. Connection, ConnectionRevision"""
    Attributes: System.Collections.Hashtable
    """
            A map of  attributes names and initial values pairs (string/string).
            Multi-valued properties are represented with a comma separated string
            """

class GenerateItemIdsAndInitialRevisionIdsProperties:
    """
    
            The input information for generateItemIdsAndInitialRevisionIds
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.ModelObject
    """
Item object reference to use as a basis for the next Item ID. This
            value is optional.
            """
    ItemType: str
    """
            Type of the Item for which the IDs will be generated.  This value is optional.
            The default is Item.
            """
    Count: int
    """Total number of IDs to be generated"""

class GenerateItemIdsAndInitialRevisionIdsResponse:
    """
    
            Return structure for generateItemIdsAndInitialRevisionIds
            operation
            
    """
    def __init__(self, ) -> None: ...
    OutputItemIdsAndInitialRevisionIds: System.Collections.Hashtable
    """
            A list of the new Item and ItemRevision IDs and flags indicating if
            the system is configured to allow modification of the id values after they have been
            generated.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data"""

class GenerateRevisionIdsProperties:
    """
    
            The data structure contains information for generateRevisionIds
            operation
            
    """
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.ModelObject
    """Item object reference to get the next revision id, optional"""
    ItemType: str
    """Type of the ids to generate, optional"""

class GenerateRevisionIdsResponse:
    """
    
            The data structure contains returned information for generateRevisionIds
            operation
            
    """
    def __init__(self, ) -> None: ...
    OutputRevisionIds: System.Collections.Hashtable
    """A list of the new generated id values"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data"""

class ItemIdsAndInitialRevisionIds:
    """
    
            This structure contain output information for generateItemIdsAndInitialRevisionIds
            operation indicating the new item id, new revision id, and a flag for each that indicates
            if the caller should be able to override the generated values.
            
    """
    def __init__(self, ) -> None: ...
    NewItemId: str
    """Newly generated Item Id"""
    NewRevId: str
    """Newly generated ItemRevision Id"""
    IsItemModify: bool
    """Flag to specify whether Item id is modifiable"""
    IsRevModify: bool
    """Flag to specify whether ItemRevision id is modifiable"""

class ItemProperties:
    """
    
            Input structure for createItems operation.  Specifies attributes for the new Item
            or ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created, optional."""
    ItemId: str
    """Id of the Item to be created, optional"""
    Name: str
    """Name of the Item to be created, optional"""
    Type: str
    """Type of the Item to be created, optional, default is Item"""
    RevId: str
    """Id of the initail revision of the Item to be created, optional"""
    Uom: str
    """Unit of measure(UOM) of the Item to be created, optional"""
    Description: str
    """Description of the Item to be created, optional"""
    ExtendedAttributes: list[ExtendedAttributes]
    """Name/value pairs for additional attributes to set, optional"""

class ObjectOwner:
    """
    
            This structure contains the business object whose owner needs to be changed, new
            owning user of the object and new owning group of the object.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Teamcenter Business object."""
    Owner: Teamcenter.Soa.Client.Model.Strong.User
    """New owning user of the business object."""
    Group: Teamcenter.Soa.Client.Model.Strong.Group
    """New owning group of the business object."""

class Relationship:
    """
    
Relationship structure represents all required
            parameters to create the relation between the primary and secondary object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this Relationship
            structure.
            """
    RelationType: str
    """
            Name of the relation type to create, required. This could be an empty string, in
            which case the relation name will be searched in the preference, ParentTypeName_ChildTypeName_default_relation
            or ParentTypeName_default_relation.
            """
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The primary object to create the relation from"""
    SecondaryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The secondary object to create the relation to."""
    UserData: Teamcenter.Soa.Client.Model.ModelObject
    """The user data object used to create the relation. This parameter is optional."""

class ReviseProperties:
    """
    
            This structure contains information about new revision id, name, description and
            extended attributes.
            
    """
    def __init__(self, ) -> None: ...
    RevId: str
    """New revision id of the Item to be revised, optional"""
    Name: str
    """Name of the new ItemRevision, optional"""
    Description: str
    """Description of the new ItemRevision, optional"""
    ExtendedAttributes: System.Collections.Hashtable
    """Name/value pairs for additional attributes to set, optional"""

class ReviseResponse:
    """
    Return structure for revise operation
    """
    def __init__(self, ) -> None: ...
    OldItemRevToNewItemRev: System.Collections.Hashtable
    """
            A Map whose keys are the input old item revisions and values are the newly created
            revisions
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class RevisionIds:
    """
    
            This structure contains information for generateRevisionIds
            operation
            
    """
    def __init__(self, ) -> None: ...
    NewRevId: str
    """Revision id that was generated"""
    IsModify: bool
    """Flag to specify whether revision id is modifiable"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetDisplayProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is provided to update the Teamcenter objects for the given name/display
             value pairs. This operation works for all supported property value types to set display
             values. When setting this operation it invokes the server PROP_UIF_set_value
             extensions. For updating an array property, display values need to be comma (,) separated
             which server parses them into individual values before assigning.
             
             Note:  Since LOVs support the display as feature where internal values of
             the LOV can be different from displayable values, this operation expects that internal
             value of the selection to be passed and not the display value.
             

        :param Objects: 
                         A list of objects for which property values need to be set
             
        :param Attributes: 
                         A map of attribute names and display values of a property  (string/string)
             
        :return: Objects that successfully have properties set are returned in the ServiceData list
             of updated objects.  Any failures will be returned with the input object mapped to
             the error message in the ServiceData list of partial errors.
        """
        ...
    def CreateDatasets(self, Input: list[DatasetProperties]) -> CreateDatasetsResponse:
        """    
             This operation creates a list of Datasets and creates the specified relation
             between created Dataset and input container object.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param Input: 

        :return: 
        """
        ...
    def CreateFolders(self, Folders: list[CreateFolderInput], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> CreateFoldersResponse:
        """    
             This operation creates a list of new Folder objects with the given names,
             descriptions and attaches them to the parent container. If attaching a created Folder
             to its parent container fails, the Folder will not be deleted.
             

Teamcenter Component:

             Core Model Folder - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component covers Folders.
             
        :param Folders: 
                         Input struture to create <b>Folder</b> Objects
             
        :param Container: 
                         The object to which all the created <b>Folder</b> objects will be related to via
                         the input relation type, may be null.
             
        :param RelationType: 
                         The name of relation type that all created <b>Folder</b> objects will be related
                         to the container, may be an empty string.
             
        :return: 
        """
        ...
    def ChangeOwnership(self, Input: list[ObjectOwner]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation can be used to change the ownership on a given business object to
             the given user and group.  Owning user attribute on the business object will be changed
             to the given user and owning group attribute is changed to the given group.  The
             user needs CHANGE_OWNER privilege and WRITE privilege on the business
             object to be able to change its ownership.  If user does not have the required privileges
             then this operation will return error code 515001. If the given user is invalid
             or given group is invalid then this operation will return error code 515024.
             

Use Cases:

             Change owner menu action calls this operation.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param Input: 
                         Input object to the operation that holds the business object, new owning user and
                         new owning group.
             
        :return: This operation returns ServiceData object.  If the object's ownership is changed
             successfully then the object is returned in the updated objects list in the ServiceData.
             Any failure will be returned with the input object mapped to the error message in
             the list of partial errors in the ServiceData.
        """
        ...
    def GetProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation is provided to get property values of instances outside of
             the current object property policy for a particular business object.  Net
             result of this operation includes the properties expressly defined in the input attributes
             as well as the properties defined in the current Object Property Policy.
             

             This operation takes care of following:
             

Since all relations are stored as properties on the primary object,
             this operation supports the expanding of relations.
             
Properties in the input attribute argument that reference other objects
             (relations) will have the properties for those referenced objects returned as defined
             by the Object Property Policy.
             


Limitation:


Classification objects attached to WorkspaceObjects using "IMAN_classification"
             relation are not returned by this operation. User need to use findClassificationObjects
             operation from Classification service to retrieve properties of such objects. For
             more information about findClassificationObjects operation please refer classification
             service guide.
             



Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param Objects: 
                         List of attribute/property name strings for which values are needed
             
        :param Attributes: 
                         List of object references for which property values are requested
             
        :return: Objects that successfully have properties added are returned in the ServiceData list
             of plain objects.  Any failures will be returned with the input object mapped to
             the error message in the ServiceData list of partial errors.
        """
        ...
    def CreateItems(self, Properties: list[ItemProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> CreateItemsResponse:
        """    
             This operation creates a list of Items and associated data (ItemRevision/ItemMasterForm/ItemRevisionMasterForm)
             based on the input attribute structures and the specified relation type between created
             Item and input object.  If container and relation type are not input, none
             of the Items will be related to a container. (There is no default, if any
             destination is desired, it must be provided as input). Note: createItems are for
             items creation, if a compound object such as ItemRevision adds a required
             property in BMIDE, createItems will fail since it only accepts required properties
             for item types, not for its associated data such as ItemRevision. Also, if
             any other properties including object description and custom properties are
             added as required on Item, createItems will fail. In this case, user
             should use createObjects instead.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Properties: 
                         A list of properties to create new <b>Item</b> objects
             
        :param Container: 
                         The container object to which all the items will be related to via the input relation
                         type, optional.
             
        :param RelationType: 
                         The relation type that will be used to relate the newly created <b>Item</b>s to the
                         container, optional.
             
        :return: list of partial errors.
        """
        ...
    def GenerateItemIdsAndInitialRevisionIds(self, Input: list[GenerateItemIdsAndInitialRevisionIdsProperties]) -> GenerateItemIdsAndInitialRevisionIdsResponse:
        """    
             This operation generates a list of Item IDs and initial ItemRevision
             IDs.  The initial revision ID is defined as the first revision ID for the given type.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Input: 
                         A list of the <b>Item</b>, <b>Item</b> type, and the number of IDs to generate.
             
        :return: IDs.
        """
        ...
    def GenerateRevisionIds(self, Input: list[GenerateRevisionIdsProperties]) -> GenerateRevisionIdsResponse:
        """    
             This operation generates a set of revision IDs.  The ID can be either the next ID
             for an existing Item or the first revision ID for a new Item.
             

Dependencies:

             revise, revise2
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Input: 
                         A list <b>Item</b> and <b>Item</b> type
             
        :return: 
        """
        ...
    def DeleteObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the input objects.  In the case of Item, it also deletes
             all ItemRevision objects,  associated ItemMaster, ItemRevisionMaster
             forms, and Dataset objects.  The input object can be an ImanRelation.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param Objects: 
                         A list of objects to be deleted
             
        :return: . Any errors that occur will be
             returned as a partial error with the source business object attached to the partial
             error.
        """
        ...
    def CreateRelations(self, Input: list[Relationship]) -> CreateRelationsResponse:
        """    
             Creates the specified relation between the input objects (primary and secondary objects).
             If the relation name is not specified then default relation name specified in either
             the preference ParentTypeName_ChildTypeName_default_relation or ParentTypeName_default_relation
             is considered as the relation name. In case none of these preferences are set
             the relation between the primary and secondary object is not created. If the primary
             object has a relation property by the specified relation name, then the secondary
             object is associated with the primary object through the relation property.
             

Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param Input: 
                         A list of structures containing details of relationships to be created between primary
                         and secondary objects with the given relation.
             
        :return: The created relations. The partial error 214116 is returned for any requtest relation
             types that are not valid relation type name. The clientId is added to the partial
             error to identify which input element is incorrect.
        """
        ...
    def DeleteRelations(self, Input: list[Relationship]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes the specified relation between the primary and secondary object for each
             input structure.
             

Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param Input: 
                         A list of structures containing details of relationships to be deleted between primary
                         and secondary objects with the given relation.
             
        :return: list of partial errors.
        """
        ...
    def Revise(self, Input: System.Collections.Hashtable) -> ReviseResponse:
        """    
             Revises a list of next Item Revisions based on input existing Item Revision object
             references and any additional attributes.  Uses deep copy rules to propagate existing
             relations from the Item Revision or to create new references.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Input: 
                         A map of Item Revisions and ReviseProperties structures
             
        :return: is a structure which contains a map of old and new Item Revisions and the ServiceData
             structure.  Any failures will be returned with input Item Revision mapped to error
             message in the ServiceData list of partial errors.
        """
        ...

