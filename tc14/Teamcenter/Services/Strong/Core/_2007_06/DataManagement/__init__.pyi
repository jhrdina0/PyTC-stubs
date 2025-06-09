import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AvailableTypeInfo:
    """
    This structure represents string  instance of type and its hierarchy.
    """
    def __init__(self, ) -> None: ...
    Type: str
    """The name of instance type"""
    Hierarchies: list[str]
    """hierarchies"""

class BaseClassInput:
    """
    
            The baseClassInput structure represents input data structure to get available
            Business Objects.
            
    """
    def __init__(self, ) -> None: ...
    BaseClass: str
    """
            This is the name of the Business Object for which this operation returns the descendant
            Business Objects.
            """
    ExclusionTypes: list[str]
    """
            Names of Business Objects (and its secondary Business Objects) to be excluded from
            returned list.
            """

class DatasetTypeInfo:
    """
    
            This structure contains the Dataset type object reference corresponding to
            the input Dataset type name and the reference information for each valid named
            reference of the Dataset type.
            
    """
    def __init__(self, ) -> None: ...
    Tag: Teamcenter.Soa.Client.Model.Strong.DatasetType
    """Dataset type reference object for the Dataset type"""
    RefInfos: list[ReferenceInfo]
    """List of valid references for the Dataset type"""

class DatasetTypeInfoResponse:
    """
    The response from getDatasetTypeInfo operation.
    """
    def __init__(self, ) -> None: ...
    Infos: list[DatasetTypeInfo]
    """
            List of named reference information for each dataset type specified in datasetTypeNames input.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData.  This operation will populate
            the ServiceData plain objects with the dataset
            type object that corresponds to the input dataset type name.
            """

class ExpandGRMRelationsData:
    """
    This structure contains information for ExpandGRMRelationsData.
    """
    def __init__(self, ) -> None: ...
    OtherSideObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Objects on the other side of the relationship"""
    RelationName: str
    """Input GRM relation name"""

class ExpandGRMRelationsOutput:
    """
    This structure contains information for Expand GRM Relations Output.
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """Object that was expanded"""
    OtherSideObjData: list[ExpandGRMRelationsData]
    """List of ExpandGRMRelationsData"""

class ExpandGRMRelationsPref:
    """
    Expand GRM Relations Pref
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """Flag to expand any Item Revisions that are in the return data"""
    Info: list[RelationAndTypesFilter2]
    """List of RelationAndTypesFilter2"""

class ExpandGRMRelationsResponse:
    """
    Expand GRM Relations Response
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandGRMRelationsOutput]
    """List of SaveQueryCriteriaInfo"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class GetAvailableTypesResponse:
    """
    
            The GetAvailableTypesResponse struct resprents return repsonse of all types implemented
            by the given class.
            
    """
    def __init__(self, ) -> None: ...
    InputClassToTypes: System.Collections.Hashtable
    """A map of given class names and all according AvailableTypeInfo objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData contains any parital error if any failure happens."""

class PurgeSequencesInfo:
    """
    
            The data structure represents all of the data necessary to purge sequences. The structure
            contains the selected object and a flag indicating whether to validate that the selected
            sequences is the active sequence.
            
    """
    def __init__(self, ) -> None: ...
    ValidateLatestFlag: bool
    """
            A flag indicating if inputObject should be
            validated that it is the latest sequence of the ItemRevision. To purge all
            previous sequences, set validateLatestFlag
            true and set inputObject to the latest sequence
            of the ItemRevision.  To purge a specific sequence, set validateLatestFlag false and set inputObject
            to the specific sequence of the ItemRevision that should be purged.
            """
    InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """A business object representing the ItemRevision sequence that should be purged."""

class ReferenceInfo:
    """
    This structure contains information for a given Dataset type.
    """
    def __init__(self, ) -> None: ...
    ReferenceName: str
    """Reference name for the input Dataset type"""
    IsObject: bool
    """
            Flag that signifies the reference is an object if the value is true.  False signifies
            the reference is a file.
            """
    FileFormat: str
    """
            The format for reference object.  Valid values are either TEXT, BINARY
            or OBJECT.
            """
    FileExtension: str
    """The default extension for a file, such as *.gif or *.doc."""

class RelationAndTypesFilter:
    """
    
            This structure contains the relation name to traverse for the given operation and
            a list of other side object types that are valid to return.
            
    """
    def __init__(self, ) -> None: ...
    RelationTypeName: str
    """Name of relation to traverse"""
    OtherSideObjectTypes: list[str]
    """List of names of valid other side object types to return"""

class RelationAndTypesFilter2:
    """
    
            This structure contains the relation name to traverse for the given operation and
            a list of other side object types that are valid to return.
            
    """
    def __init__(self, ) -> None: ...
    RelationName: str
    """Types of relationships allowed"""
    ObjectTypeNames: list[str]
    """Types of other objects allowed"""

class SetOrRemoveImmunityInfo:
    """
    
            The data structure represents all of the data necessary to toggle the immunity of
            an ItemRevision sequence. It contains a reference to the ItemRevision
            sequence whose immunity will be is modified and a flag indicating whether immunity
            will be revoked or applied.
            
    """
    def __init__(self, ) -> None: ...
    SetOrRemoveFlag: bool
    """
            Flag indicating if immunity should be set or removed on the inpoutObject.  To set immunity, the setOrRemoveImmunityFlag
            should be true.  To remove immunity, the setOrRemoveImmunityFlag
            should be false.
            """
    InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
ItemRevision sequence object which should be made immune or have immunity
            removed.
            """

class ValidateIdsInfo:
    """
    
            The ValidateIdsInfo struct contains the input
            ids for item and revision and the item type.
            
    """
    def __init__(self, ) -> None: ...
    ItemId: str
    """Item ID to be validated"""
    RevId: str
    """Revision ID to be validated"""
    ItemType: str
    """Item type to validate against, can be null"""

class ValidateIdsOutput:
    """
    
            This structure contains the modified item and revision ids and enum status of the
            ids respectively.  Valid values for the enums are Valid (ids are valid), Invalid
            (ids are not valid), Modified (ids are not ideal but can be used if the user really
            wants them), Override (ids are not valid, silently replace with modified ones), and
            Duplicate (ids are already allocated in the system).
            
    """
    def __init__(self, ) -> None: ...
    ModItemId: str
    """Modified item id if specified by Naming Rules"""
    ItemIdStatus: str
    """
            Status of the item id represented as a ValidateIdsStatus
            enum
            """
    ModRevId: str
    """Modified rev id if specified by Naming Rules"""
    RevIdStatus: str
    """
            Status of the revision id represented as a ValidateIdsStatus
            enum
            """

class ValidateItemIdsAndRevIdsResponse:
    """
    
            The list of ValidateIdsOutput structures
            and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ValidateIdsOutput]
    """List of ValidateIdsOutput structures"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData contains only error information returned by this operation."""

class WhereReferencedByRelationNameInfo:
    """
    
            The data structure contains the object to perform the where referenced operation
            on and the filters to narrow the list of referencing objects returned.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Desired business object to find referencing objects of"""
    Filter: list[RelationAndTypesFilter]
    """A list of filters to limit the search of referencing objects"""

class WhereReferencedByRelationNameOutput:
    """
    
            This structure contains the object that the where referenced operation was performed
            on and list of WhereReferencedRelationNameOutputInfo
            structures.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """Input object for which referencers were found"""
    Info: list[WhereReferencedByRelationNameOutputInfo]
    """
            List of WhereReferencedByRelationNameOutputInfo
            structures
            """

class WhereReferencedByRelationNameOutputInfo:
    """
    
            This structure contains the referencer object, the corresponding relation name, and
            the level at which the referencer was found.
            
    """
    def __init__(self, ) -> None: ...
    Referencer: Teamcenter.Soa.Client.Model.ModelObject
    """Referencer object of the input object"""
    RelationTypeName: str
    """Relation type name of how referencer is related to input object"""
    Level: int
    """Integer value for the level depth where referencer found"""

class WhereReferencedByRelationNameResponse:
    """
    
            The data structure contains the list of the referencing objects that meet the filter
            criteria for each of the input objects.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[WhereReferencedByRelationNameOutput]
    """A list of filtered referencing objects for each input object"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandGRMRelationsForPrimary(self, PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: ExpandGRMRelationsPref) -> ExpandGRMRelationsResponse:
        """    
             Returns the secondary objects related to the input object for the given list of properties
             / relations and other side object types.  If no properties/relations or other side
             objects types are input, then all related objects will be returned.  In addition,
             for performance, if an Item is the output of the expansion, then its associated Item
             Revisions and the Datasets for those Item Revisions will be returned.  Similarly,
             if an Item Revision is the output of the expansion, then its associated Datasets
             will be returned.
             
        :param PrimaryObjects: 
                         A Vector of Teamcenter primary objects
             
        :param Pref: 
                         Expand GRM Relations Preference
             
        :return: Secondary objects related to the primary objects identified after filtering and ServiceData
        """
        ...
    def GetAvailableTypes(self, Classes: list[BaseClassInput]) -> GetAvailableTypesResponse:
        """    
             This will return type names implemented by the given classes. This is lightweight
             way to get all displayable types by name rather than model object.
             
        :param Classes: 
                         A list of given base class name and exclusion list.
             
        :return: A map of given base class name and its available instance types. Failure will be
             returned with error messages in service data.
        """
        ...
    def PurgeSequences(self, Objects: list[PurgeSequencesInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Given a list of ItemRevision sequences, this opertion is used ot perform per
             the following criteria:
             

If the input object is the latest sequence of an ItemRevision,
             all previous sequences will be purged.
             
If the input object is not the latest sequence of the ItemRevision
             and the validateLatestFlag is false, the
             input object will be purged.
             
If the input object is not the latest sequence of the ItemRevision
             and the validateLatestFlag is true, the ServiceData will be updated with an error.
             



Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Objects: 
                         A list of the objects to be purged and a flag noting whether to validate the object
                         is the latest sequence.
             
        :return: 
        """
        ...
    def SetOrRemoveImmunity(self, Objects: list[SetOrRemoveImmunityInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used to add or remove immunity for each object in the input list
             according to the value of the associated setOrRemoveFlag.
             A value of true indicates to apply immunity to the object.  A value of false indicates
             that immunity should be removed from the object.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Objects: 
                         A list of the <b>ItemRevision</b> sequence objects and a flag set true or false.
             
        :return: 
        """
        ...
    def GetDatasetTypeInfo(self, DatasetTypeNames: list[str]) -> DatasetTypeInfoResponse:
        """    
             This operation returns the named reference information for a set of dataset types.
             Named references are Teamcenter objects that relate to a specific data file.
             

             Any failure that occurs during this operation is returned in the ServiceData list of partial errors with the dataset type name
             string mapped to error message.
             


Use Cases:

             User wants to see which file type is allowed for attaching to a dataset.
             

             For this operation, the dataset type name is passed in the datasetTypeNames
             input and the named reference information is returned.  The file extension, fileExtension, is returned in ReferenceInfo and can be used to determine the supported file
             type for the dataset.
             


Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param DatasetTypeNames: 
                         List of dataset type names used to get the named reference information. An empty
                         list will return information for all dataset types defined in Teamcenter.
             
        :return: 
        """
        ...
    def ValidateItemIdsAndRevIds(self, Infos: list[ValidateIdsInfo]) -> ValidateItemIdsAndRevIdsResponse:
        """    
             Validates the item ID and revision ID based on the naming rules and user exit callbacks.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param Infos: 

        :return: - the response object containts a list of ValidateIdsOutput and ServiceData. The
             ValidateIdsOutput contains validation statuses for Item Id and Revision Id. If the
             Ids are modified because of the Naming Rules, then the modified Item Id and Revision
             Id are returned. Any failure is returned in the ServiceData list of partial errors
             with index of ValidateIdsInfo mapped to error message.
        """
        ...
    def ExpandGRMRelationsForSecondary(self, SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: ExpandGRMRelationsPref) -> ExpandGRMRelationsResponse:
        """    
             Returns the primary objects related to the input object for the given list of properties
             / relations and other side object types.  If no properties/relations or other side
             objects types are input, then all related objects will be returned.  In addition,
             for performance, if an Item is the output of the expansion, then its associated Item
             Revisions and the Datasets for those Item Revisions will be returned.  Similarly,
             if an Item Revision is the output of the expansion, then its associated Datasets
             will be returned.
             

Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param SecondaryObjects: 
                         A Vector of Teamcenter secondary objects
             
        :param Pref: 
                         Expand GRM Relations Preference
             
        :return: Primary objects related to the primary objects identified after filtering and ServiceData
        """
        ...
    def WhereReferencedByRelationName(self, Inputs: list[WhereReferencedByRelationNameInfo], NumLevels: int) -> WhereReferencedByRelationNameResponse:
        """    
             Finds the objects that reference a given object by a specific relation. The input
             object will be the secondary object for that relation.  It does not return relations
             where the given input object is the primary object for the relation.  The Datamanagement
             service operation expandGRMRelationsForPrimary can be used to return the relations
             where the input object is the primary object and the objects which are the secondary
             object for the relation
             

Use Cases:

             Use case 1: Use this operation to find the objects referencing the input object by
             a specific relation.
             
             Use case 2: Use this operation to find objects of a specific type that reference
             the input object by a specific relation.
             
             Use case 3: Use this operation to find objects of a specific type referencing the
             input object.
             


Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param Inputs: 
                         A list of desired business objects and filters to find the referencing objects for
             
        :param NumLevels: 
                         The number of levels to search.  For example, if A references B, and B references
                         C, a 1-level search from C produces just B, but a 2-level search produces both A
                         and B. If -1, all levels are returned.
             
        :return: 
        """
        ...

