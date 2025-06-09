import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateFormsOutput:
    """
    This structure contains newly created form or updated form information.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created or updated."""
    Form: Teamcenter.Soa.Client.Model.ModelObject
    """The Form object created or updated"""

class CreateOrUpdateFormsResponse:
    """
    Holds the Response of created or updated Forms
    """
    def __init__(self, ) -> None: ...
    Outputs: list[CreateFormsOutput]
    """List of created or updated Form objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class FormAttributesInfo:
    """
    This structure contains the Form Attributes Information.
    """
    def __init__(self, ) -> None: ...
    FormType: str
    """Form Type"""
    FormPDs: list[FormPropDescriptor]
    """A list of property descriptors"""

class FormInfo:
    """
    Holds the Information of Form to be created or updated
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Identifier that helps the client to track the object(s) created, required; should
            be unique for the input set
            """
    FormObject: Teamcenter.Soa.Client.Model.ModelObject
    """The Form object, if null then create; otherwise, update."""
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    """Parent object of the Form to be created"""
    RelationName: str
    """Relation name between Parent and Form to be created"""
    SaveDB: bool
    """If true, save the Form to database"""
    Name: str
    """Name of the Form to be created"""
    Description: str
    """Description of the Form to be created, can be an empty string."""
    FormType: str
    """Form Type of the Form to be created"""
    AttributesMap: System.Collections.Hashtable
    """Form property map for the Form to be updated"""

class FormPropDescriptor:
    """
    This structure contains information for Form Properties Descriptor.
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Propety name"""
    DisplayName: str
    """Property display name"""
    PropValueType: int
    """Property value type"""
    PropType: int
    """Property type"""
    IsDisplayable: bool
    """true if property is displayable, otherwise false"""
    IsArray: bool
    """true if property is an array, otherwise false"""
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    """List of values"""
    IsRequired: bool
    """true if propety is required, otherwise false"""
    IsEnabled: bool
    """true if property is enabled, otherwise false"""
    IsModifiable: bool
    """true if Property is Modifiable"""
    AttachedSpecifier: int
    """Attached specifier"""
    MaxLength: int
    """Property maximumlLength"""
    InterdependentProps: list[str]
    """A list of interdependent properties"""

class GenerateUIDResponse:
    """
    Return structure for generateUID operation
    """
    def __init__(self, ) -> None: ...
    Uids: list[str]
    """List of the UIDs that were generated"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any errors encountered during processing in the partial errors list."""

class GetDatasetCreationRelatedInfoResponse:
    """
    Holds the Response data from getDatasetCreationRelatedInfo
    """
    def __init__(self, ) -> None: ...
    ToolNames: list[str]
    """List of Tool names"""
    NewDatasetName: str
    """The name of the new Dataset, can be an empty string"""
    NameCanBeModified: bool
    """If true, the name of the Dataset can be modified"""
    InitValuePropertyRules: list[str]
    """List of properties have the initialized values from property constant attachments"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class GetItemCreationRelatedInfoResponse:
    """
    
            This data structure contains a naming rules, property rules, form property descriptor,
            unit of measure, and ItemRevision type. Partial failure message will be returned
            in ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    ComplexValuePropertyRules: list[str]
    """List of complex value property rules"""
    InitValuePropertyRules: list[str]
    """List of initial values"""
    PatternMap: System.Collections.Hashtable
    """Pattern map (string/string)"""
    Uoms: list[str]
    """List of unit of measures"""
    FormAttrs: list[FormAttributesInfo]
    """List of Form attributes"""
    RevTypeName: str
    """ItemRevision type name"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The successful object ids, partial errors and failures"""

class GetItemFromIdInfo:
    """
    
            Input structure for getItemFromIdInfo, each of which contain an item id and optionally
            a list of revision ids which specify which Item Revisions to retrieve.
            
    """
    def __init__(self, ) -> None: ...
    ItemId: str
    """Item id string for Item to retrieve, required"""
    RevIds: list[str]
    """Revision ids which specify which Item Revisions to retrieve, optional"""

class GetItemFromIdItemOutput:
    """
    
            This structure contains information for getItemFromId
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """Item object reference of the item found"""
    ItemRevOutput: list[GetItemFromIdItemRevOutput]
    """List of GetItemFromIdItemRevOutput"""

class GetItemFromIdItemRevOutput:
    """
    
            This structure contains an ItemRevision object and a list of found Dataset
            objects.
            
    """
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference of the item revision found"""
    Datasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """List of Dataset object references found"""

class GetItemFromIdPref:
    """
    
            Input structure for getItemFromAttribute
            used to filter the returned ItemRevision objects.
            
    """
    def __init__(self, ) -> None: ...
    Prefs: list[RelationFilter]
    """
            A list of RelationFilter structures for determining
            which ItemRevision objects to return
            """

class GetItemFromIdResponse:
    """
    Return structure for getItemFromId operation
    """
    def __init__(self, ) -> None: ...
    Output: list[GetItemFromIdItemOutput]
    """List of GetItemFromIdItemOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class MoveToNewFolderInfo:
    """
    
            Input structure for the moveToNewFolder operation.
            

    """
    def __init__(self, ) -> None: ...
    OldFolder: Teamcenter.Soa.Client.Model.Strong.Folder
    """
            Folder object reference of the old folder, whose content is going to move to new
            folder.
            """
    NewFolder: Teamcenter.Soa.Client.Model.Strong.Folder
    """
            Folder object reference of the new folder, where object content is going to move,
            required. If not specified, processing will continue to the new input.
            """
    ObjectsToMove: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of object references to be moved from the old folder to the new folder or copied
            to the new folder, required. If not specified, processing will continue to the next
            input.
            
"""

class MoveToNewFolderResponse:
    """
    
            Return structure for the moveToNewFolder
            operation.
            

    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains the updated old folder, the new folder, and partial errors from this operation."""

class RelationFilter:
    """
    A filter for determining which ItemRevision objects to return.
    """
    def __init__(self, ) -> None: ...
    RelationTypeName: str
    """
            The  relation type name that specifies the relation that relates the ItemRevision
            to the Dataset.
            """
    ObjectTypeNames: list[str]
    """A list of  Dataset object type names to return"""

class SaveAsNewItemInfo:
    """
    Input structure for saveAsNewItem operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Used to uniquely identify the input (Required)"""
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Original Item Revision to be used for the SaveAsNewItem operation (Required)"""
    ItemId: str
    """Item id string for creating new item, optional"""
    RevId: str
    """Revision id string for creating new revision, optional"""
    Name: str
    """Name string for creating new item/revision, optional"""
    Description: str
    """Description string for creating new item/revision, optional"""
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """
            Folder object reference to attach Item to, if null, the Item will go to the default
            preference location for created objects.
            """

class SaveAsNewItemOutput:
    """
    The data strucutre contains newly created object inforamtiobn.
    """
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """New Item object"""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """New ItemRevision object"""

class SaveAsNewItemResponse:
    """
    The data structure contains return information for the operation.
    """
    def __init__(self, ) -> None: ...
    InputToNewItem: System.Collections.Hashtable
    """
            Map whose keys are the input clientIds and output values (newly created Item
            and ItemRevision objects) pairs (string,
            SaveAsNewItemOutput)
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data"""

class VecStruct:
    """
    This structure contains string list.
    """
    def __init__(self, ) -> None: ...
    StringVec: list[str]
    """A list of strings"""

class WhereReferencedInfo:
    """
    This data structure contains output information of referencer, relation and level.
    """
    def __init__(self, ) -> None: ...
    Referencer: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """WorkspaceObject that references the input object"""
    Relation: str
    """String name of the relation between the reference and the input object"""
    Level: int
    """Level at which referencer was found."""

class WhereReferencedOutput:
    """
    
            This data structure contains output information of reference, relation name and level
            for given input objects.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """WorkspaceObject that is referenced by info"""
    Info: list[WhereReferencedInfo]
    """
            Output information containing reference, relation name and level for inputObject
"""

class WhereReferencedResponse:
    """
    This data structure contains output information for a list of where referenced objects.
    """
    def __init__(self, ) -> None: ...
    Output: list[WhereReferencedOutput]
    """List of information containing reference, relation name and level for input object"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data"""

class WhereUsedOutput:
    """
    This structure contains information for WhereUsedOutput.
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Input WorkspaceObject object reference for mapping to the output"""
    Info: list[WhereUsedParentInfo]
    """List of WhereUsedParentInfo structures"""

class WhereUsedParentInfo:
    """
    This structure contains Generic Parent Info.
    """
    def __init__(self, ) -> None: ...
    ParentItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Parent ItemRevision object reference which uses the given object"""
    Level: int
    """The level at which the parent ItemRevision was found"""

class WhereUsedResponse:
    """
    
WhereUsedResponse contains list of WhereUsedOutput  structure. This structure contains
            list of Item and ItemRevision objects which are results of whereUsed search.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[WhereUsedOutput]
    """List of WhereUsedOutput structures"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is to support updating list of objects with the given property names
             and values. All the objects updated with same set of property and values data.  Also
             see  Teamcenter::Soa::Core::2010_09::setProperties operation.
             
             Note: Objects are saved as a part of this operation itself.
             
        :param Objects: 
                         List of Business Objects for which the properties values to be set.
             
        :param Attributes: 
                         A map of attribute names and desired value pairs (string/VecStruct). The <font face="courier" height="10">VecStruct</font> is a list of strings to support both single valued and
                         multivalued properties of any type. The calling client is responsible for converting
                         the different property types (like integer, double, date etc...) to a string using
                         the appropriate toXXXString functions in the SOA client frameworks Property class.
             
        :return: Each updated Business Object is added to the Updated list of the ServiceData. If
             property name is missing, error 214121 is returned as a Partial Error. If setting
             of property value(s) fails , error 214114 is returned as a Partial Error. The corresponding
             Business Objects from the input is attached to the Partial Error.
        """
        ...
    def GenerateUID(self, NUID: int) -> GenerateUIDResponse:
        """    
             This function returns a number of Teamcenter UIDs generated from the Teamcenter server.
             This operation can be used for assigning unique identifiers to objects that will
             not be stored in Teamcenter or for objects which have yet to be created in Teamcenter.
             

             The createObjects and createOrUpdateParts operations will support input of a preallocated
             UID for use during creation. Please see those operation descriptions for further
             details.
             


Use Cases:

             The integration create workflow requires data to be precreated and stored outside
             of Teamcenter and then used during the Teamcenter create process. For example, generating
             a UID for an ItemRevision object and then storing that UID in the CAD integration
             data file. The UID is then used as input to the create SOA operation and that UID
             is assigned to the created object.
             


Dependencies:

             createOrUpdateParts, createObjects
             

Teamcenter Component:

             Core Model CXPOM - Provides a (sparse) set of functions for the interface of C++
             on POM.
             
        :param NUID: 
                         The number of UIDs to be generated.
             
        :return: 
        """
        ...
    def GetDatasetCreationRelatedInfo(self, TypeName: str, ParentObject: Teamcenter.Soa.Client.Model.ModelObject) -> GetDatasetCreationRelatedInfoResponse:
        """    
             This operation pre-populates Dataset creation information, default new Dataset
             name and Tool names, for a specified Dataset type.  This operation
             is used to get all the information associates with the specified Dataset prior
             to the creation operation. The returned default new Dataset name may be determined
             by the parent container object.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param TypeName: 
                         desired <b>Dataset</b> type name
             
        :param ParentObject: 
                         The containe object under which the new <b>Dataset</b> object will be created
             
        :return: .
        """
        ...
    def MoveToNewFolder(self, MoveToNewFolderInfos: list[MoveToNewFolderInfo]) -> MoveToNewFolderResponse:
        """    
             The moveToNewFolder operation moves a set
             of objects from one folder to another. This operation allows for moving multiple
             sets of objects to and from different folders. If no old folder is specified, this
             operation adds the objects to the new folder.
             


Use Cases:


The user selects an object or group of objects and specifies the
             folder for the objects to be copied into.
             
The user selects an object or group of objects, removes them from
             a specified folder and specifies the folder for the objects to be copied into.
             



Teamcenter Component:

             Core Model Folder - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component covers Folders.
             
        :param MoveToNewFolderInfos: 
                         A list of <font face="courier" height="10">MoveToNewFolderInfo</font> structures
                         each containing an old <b>Folder</b> object a new <b>Folder</b> object, and a vector
                         of objects to be moved from the old folder to the new folder
             
        :return: 
        """
        ...
    def CreateOrUpdateForms(self, Info: list[FormInfo]) -> CreateOrUpdateFormsResponse:
        """    
             This operation creates Form objects or update existing Form objects
             using the info provided. A new Form will be associated to the container object
             with specified relation type. The properties of the existing Form will be
             updated.
             

Teamcenter Component:

             Core Model Form - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform. This component covers Forms .
             
        :param Info: 
                         Input for creating or updating <b>Form</b> objects
             
        :return: 
        """
        ...
    def GetItemCreationRelatedInfo(self, TypeName: str, ParentObject: Teamcenter.Soa.Client.Model.ModelObject) -> GetItemCreationRelatedInfoResponse:
        """    
             This operation will return naming rules, property rule, form property descriptor,
             unit of measurement and ItemRevision type name based on Item type selected
             by user during Item creation.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param TypeName: 
<b>Item</b> type name
             
        :param ParentObject: 
<b>parentObject</b> is an unused parameter and may be null
             
        :return: 
        """
        ...
    def GetItemFromId(self, Infos: list[GetItemFromIdInfo], NRev: int, Pref: GetItemFromIdPref) -> GetItemFromIdResponse:
        """    
             This operation returns Items, Item Revisions, and Dataset based on the input item
             id. Input is a list of GetItemFromIdInfo structures each of which contain an item
             id (GetItemFromIdInfo.itemId) and optionally a list of revision ids (GetItemFromIdInfo.revIds)
             which specify which Item Revisions to retrieve.  Also input is and integer value
             (nRev) which can also be used to help specify which Item Revisions to return with
             the Item.  The final input is a GetItemFromIdPref structure which contains a list
             of RelationFilter structures (GetItemFromIdPref.prefs) each of which contain a relation
             type name (RelationFilter.relationTypeName) and a list of object type names (RelationFilter.objectTypeNames).
             This filter can be used to specify which Datasets are returned.  The relation type
             name specifies the relation that relates the Item Revision to the Dataset.  The object
             type name is the type of Dataset to return.  For example, if relationTypeName is
             "IMAN_reference" and the object type name is "Text" then only those Datasets of type
             "Text" that are related to candidate Item Revisions with the "IMAN_reference" relation
             will be returned.  Supplying no value or an empty value for the rev id list and 0
             for nRevs will signify the return of no Item Revisions, and thus no Datasets will
             be returned either.  Supplying no value or an empty value for the rev id list and
             a negative value for nRevs will signify the return of all Item Revisions.   Supplying
             no value or an empty value for the rev id list and a positive value for nRev will
             signify the return of the latest number of Item Revisions specified by the integer--if
             the number of actual revisions found is greater than the input nRev, all revisions
             for the found Item will be returned. Supplying a rev id list will only return those
             revisions, and the nRev value will not be processed. For example, if the input rev
             Id is "A" and the nRev value is 0, only revision "A" will be returned. If the rev
             id list is empty and nRevs = 5, then the 5 latest Item Revisions will be returned.
             If no preference filter is specified, all Datasets will be returned.  The return
             is a GetItemFromIdResponse which contains a list of GetItemFromIdItemOutput (GetItemFromIdResponse.output
             and a ServiceData (GetItemFromIdResponse.serviceData).  Each GetItemFromIdItemOutput
             contains an Item (GetItemFromIdItemOutput.item) and a list of GetItemFromIdItemRevOutput
             structures (GetItemFromIdItemOutput.itemRevOutput).  Each GetItemFromIdItemRevOutput
             structure contains an Item Revision (GetItemFromIdItemRevOutput.itemRevision) and
             a list of found Datasets (GetItemFromIdItemRevOutput.datasets).
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Infos: 
                         list of GetItemFromIdInfo structures
             
        :param NRev: 
                         value for the latest number of Item Revisions to return
             
        :param Pref: 
                         GetItemFromIdPref structure for relation and types filtering
             
        :return: contains found item, its item revisions and the datasets attached to the revision.
             Partial Errors will be returned as a map of input item id to error message.
        """
        ...
    def SaveAsNewItem(self, Info: list[SaveAsNewItemInfo]) -> SaveAsNewItemResponse:
        """    
             This operation creates a new Item object and ItemRevision object from
             an existing ItemRevision object.  The master form properties may be supplied
             for the new ItemRevision and item master form objects.  If master form data
             is not supplied the master forms will be initialized from the master forms attached
             to the existing ItemRevision.  Deep Copy rules may also be supplied to override
             the default Deep Copy rules.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Info: 
                         The necessary information to create the new <b>Item</b> and <b>ItemRevision</b>

        :return: .
        """
        ...
    def RefreshObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used to reload the in-memory representation of the objects from
             the database. Any references to the object will still be valid. Any in-memory changes
             to the original object will be lost. If the object has been changed in the database
             since it was last loaded, then those changes will not be present in memory. The operation
             updates the in memory representation to reflect database changes and does not obtain
             write lock on any objects.
             

Use Cases:

             Use this operation to reload the in-memory representation of one or more objects
             from the Teamcenter database.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param Objects: 
                         A list of object to be refreshed
             
        :return: 
        """
        ...
    def WhereUsed(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], NumLevels: int, WhereUsedPrecise: bool, Rule: Teamcenter.Soa.Client.Model.ModelObject) -> WhereUsedResponse:
        """    
             The whereUsed service identifies all the
             parent Item and ItemRevision objects in the structure where the input
             Item or ItemRevision is used. User can provide RevisionRule
             to search for specific ItemRevision. By default all ItemRevision objects
             are returned. The number of levels of whereUsed
             search indicates, whether to return one or top or all levels of assemblies. It supports
             search on Item, ItemRevision  and Dataset.
             

Use Cases:

             A user performs whereUsed search to find
             all the assemblies that contain a particular Item or ItemRevision.
             User inputs Item or ItemRevision and the search can be made with following
             options:
             

RevisionRule This can be set to All, displaying all ItemRevision
             objects  that have an occurrence of target ItemRevision. If a specific RevisionRule
             is selected only the ItemRevision objects  configured by the rule are returned
             in the search.
             
Depth up to which numbers of levels are to be returned.
             



             The output contains list of  each parent level search result in the structure.
             

Teamcenter Component:

             WhereUsed - Provides where used search capability for Item, ItemRevision, DataSet
             and apperanceGroup objects in the database. User can apply the Rev Rule criteria
             to filter the results for configured results.
             
        :param Objects: 
                         List of object references on which to perform the <font face="courier" height="10">whereUsed</font>
                         search. It is a required parameter.
             
        :param NumLevels: 
                         Number of levels to traverse in the <font face="courier" height="10">whereUsed</font>
                         search and return
             
        :param WhereUsedPrecise: 
                         Boolean representing whether to only send back precise parents ( used by <b>ItemRevision</b>
                         specifically and not <b>Item</b>)
             
        :param Rule: 
<b>RevisionRule</b> used get unique configured <b>ItemRevision</b> from each level
                         of <font face="courier" height="10">whereUsed</font> search, ignored if whereUsedPrecise
                         = true
             
        :return: 
        """
        ...
    def WhereReferenced(self, Objects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject], NumLevels: int) -> WhereReferencedResponse:
        """    
             This operation finds the objects and relations that reference a given object.  It
             returns objects where the input object is specified in a Reference property on that
             object.  It also returns relations where the input object is listed as the secondary
             object for that relation.  It does not return relations where the input object is
             the primary object for that relation. The Datamanagement service operation expandGRMRelationsForPrimary
             can be used to return the relations where the input object is the primary object
             and the objects which are the secondary object for the relation.
             

Use Cases:

             User selects an object, specifies the number of levels (or all) of referencers to
             return and executes a where referenced query.
             

             For example, the user selects a Dataset which has a specification relation
             to an Item and is contained in the users Home folder. The Item is contained
             in the user Newstuff folder and in the view folder of another Item Revision.
             If the user selects level 2, the Item and Home folder would be returned at
             level 1 and the Newstuff folder and view folder of the other ItemRevision
             would be returned at level 2.
             

Teamcenter Component:

             Core Model Method Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform. This component defines basic method
             structure.
             
        :param Objects: 

        :param NumLevels: 

        :return: 
        """
        ...

