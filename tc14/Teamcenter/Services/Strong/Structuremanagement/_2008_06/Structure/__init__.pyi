import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DefaultNaming:
    """
    prefix/suffix/replace-with/autoAssign to form new Item IDs.
    """
    def __init__(self, ) -> None: ...
    Autogen: bool
    """auto assign new item IDs."""
    Prefix: str
    """substring to be prefixed to the old item ID to form a new item ID."""
    Suffix: str
    """substring to be sufficed to the old item ID to form a new item ID."""
    From: str
    """
            substring to be replaced from the old item ID by another substring to form a new
            item ID.
            """
    To: str
    """substring to replace with a substring from the old item ID to form a new item ID."""

class DuplicateInputInfo:
    """
    Input for Duplicate SOA API
    """
    def __init__(self, ) -> None: ...
    TopLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The top BOMLine of the structure to be cloned."""
    ClonedIdMap: System.Collections.Hashtable
    """
            A map of oldItemId and NewItemInfo structure.  The newItemInfo is made up of the
            proposed new ItemId and the proposed new ItemName.
            """
    DefaultName: DefaultNaming
    """A pattern to form a new ItemId."""
    RenameCadFile: bool
    """Whether to rename the CAD files or not."""
    Options: list[str]
    """A list of dependency types. This defines the cad traversal."""

class DuplicateResponse:
    """
    response from the Duplicate SOA.
    """
    def __init__(self, ) -> None: ...
    ClonedItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Top ItemRevision of the Cloned structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData object - The service data object
            consists of the   top ItemRevision of the cloned structure.  The error stack
            will contain those ItemRevision objects that failed cloning and the reason.
            Those ItemRevision objects that fail to get cloned are referenced.
            """

class ExpandOrUpdateDuplicateItemsInfo:
    """
    
The ExpandOrUpdateDuplicateItemsInfo contains
the BOMLine objects, list of ItemRevision objects and list of Dependency
types.
    """
    def __init__(self, ) -> None: ...
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            If it is not null, expand it and get its dependencies based on the depTypes.  The
            BOMLine can be any line in the structure that the user picks for expansion.
            """
    ItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """
            The ItemRevision objects to perform search dependencies on. If empty, the
            ItemRevision objects to be used will be from the expansion of the BOMLine.
            """
    DepTypes: list[str]
    """The dependency types to use for the operation."""

class ExpandOrUpdateDuplicateItemsOutput:
    """
    
The ExpandOrUpdateDuplicateItemsOutput represents
the collection of all related data objects with the structure ItemRevision
object(s) or part family masters ItemRevision object(s).
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The BOM structure ItemRevision."""
    RelatedObjInfo: list[RelatedItemsInfo]
    """List of all dependent objects that are related to the object."""

class ExpandOrUpdateDuplicateItemsResponse:
    """
    
The ExpandOrUpdateDuplicateItemsResponse
structure represents the the results of the structure dependent data search.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[ExpandOrUpdateDuplicateItemsOutput]
    """
            List of ExpandOrUpdateDuplicateItemsOutput
            which contains information about the BOM structure ItemRevision to its related
            data relationships.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The error information will be recorded here."""

class NewItemInfo:
    """
    The proposed new ItemIds and new ItemNames.
    """
    def __init__(self, ) -> None: ...
    NewItemId: str
    """The proposed new ItemId."""
    NewItemName: str
    """The proposed new ItemName."""

class RelatedItemsInfo:
    """
    
The RelatedItemsInfo represents the dependent data found and how it is related
to
a structure ItemRevision. RelatedItemsInfo also can represent a family table
member to a family table master.
    """
    def __init__(self, ) -> None: ...
    RelObj: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """An ItemRevision  - it is the related data."""
    RelationshipName: str
    """The GRM relationship used to find the related data."""
    DepType: str
    """The cad dependency types to use for the operation."""

class ValidateStructureItemIdsInfo:
    """
    
Input to ValidateStructureItemIds. It contains top BOM line, map of oldItemId to
NewItemInfo(NewItemId, NewItemName), default naming pattern and list of
dependency
types specified by the user.
    """
    def __init__(self, ) -> None: ...
    TopLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Top BOMLine of the structure to be cloned."""
    InputMap: System.Collections.Hashtable
    """Map of oldItemId and NewItemInfo structure."""
    DefaultName: DefaultNaming
    """The pattern to form new ItemIds."""
    Options: list[str]
    """A list of dependency types."""

class ValidateStructureItemIdsResponse:
    """
    
Response from ValidateStructureItemIds, containing
map of OldItemID to NewItemInfo, list of
ItemRevision objects that failed validation and the ServiceData
object.
    """
    def __init__(self, ) -> None: ...
    ClonedIdMap: System.Collections.Hashtable
    """A map of OldItemID to NewItemInfo that contains the proposed New ItemId and New ItemName."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData object.  The error stack will
            contain those ItemRevision objects that failed cloning and the reason.
            """

class Structure:
    """
    Interface Structure
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def Duplicate(self, Inputs: list[DuplicateInputInfo]) -> DuplicateResponse:
        """    
             This operation will create a duplicate (clone) of the input structure from its top
             level down.
             
             Depending on the user action, all or some of the original structure is duplicated
             and the rest is referenced.  The user has the option to de-select a sub assembly
             or leaf Item on the duplicate dialog.  Those Item objects that are
             not selected in the duplicate dialog will not be cloned but referenced from the original
             structure.
             

             The user can define a specific naming pattern for the ItemIds of the duplicated (cloned)
             structure.  The user can define specific ItemIds for individually selected ItemRevision
             objects or a default naming pattern for the duplicated structure.   The default pattern
             can be defined by adding prefixes, suffixes or replacing part of the original name
             with a different pattern.  The user can also choose to allow the system to assign
             default ids.
             

             All of the structure dependent data of the input structure like datasets and attachments
             are copied to the duplicated structure based on the Business Modeler IDE deep copy
             rules for SaveAs.  The duplicate operation
             internally uses SaveAs at every level of
             the structure; therefore it uses the SaveAs
             deep copy rules.
             

             CAD specific attachments and relations are copied based on the transfer mode defined
             for the Business Modeler IDE global constant StructureCloneTransferModes.
             The transfer mode contains dependent closure rules for expansion and cloning.  The
             value for the closure rules is added by the installed CAD system.
             

             For e.g. The closure rule defined for IPEM ProE integration (ipemSCloneClosureRule)
             looks like this:
             

TYPE.ProPrt:CLASS.ItemRevision:RELATIONP2S.IPEM_master_dependency:PROCESS:PartFamilyMaster:R,
             TYPE.ProAsm:CLASS.ItemRevision:RELATIONP2S.IPEM_master_dependency:PROCESS:PartFamilyMaster:R,
             TYPE.ProPrt:CLASS.ItemRevision:RELATIONS2P.IPEM_master_dependency:PROCESS+TRAVERSE:PartFamilyMember,
             


Note: The difference between the three operations duplicate,
             duplicate2 and duplicate3
             are the following:
             

duplicate and duplicate2

             - In duplicate the input top BOMLine
             is the top BOMLine of the original configured structure in Structure Manager.
             In duplicate2 the input top BOMLine
             is the selected BOMLine from the configured structure in Structure Manager
             or Systems Engineering.  i.e. the user can select to clone a sub-assembly of the
             original structure.
             

             - The input for duplicate2 includes project(s).
             The cloned structure is assigned to those project(s).  duplicate
             does not have project(s) as input.
             

duplicate2 and duplicate3

             - duplicate3 was created as a result of the
             Multi Field Key (MFK ) project.   The difference between duplicate2
             and duplicate3 is that in duplicate2 is that the input and output had a DuplicateIdMap2 whereas to align with the MFK project, duplicate3 has a DuplicateIdStructure.
             


Use Cases:

Use case1: Simple Clone

             A user has an assembly which does not have cad dependencies nor does it belong to
             a specific project(s).  The user wants to duplicate the entire structure with a specific
             naming pattern for the ItemIds.  The naming pattern is a prefix "test_".
             

             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned, and the naming pattern for the new structure.  The result
             is a new structure with the following naming pattern for the ItemIds -> test_OriginalItemId.
             

Use case2: CAD Clone

             A user has an assembly structure which has cad dependencies.  The user wants to start
             a new product with a similar structure and cad dependencies.  The expansion and cloning
             rules have been defined in the Business Modeler IDE global constant StructureCloneTransferModes

             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned.
             
             The user picks the cad dependency option "Part Families
             Masters".  The expansion and cloning will be done based on the closure rules
             defined for Part Family Master in the CAD closure rules.
             
             The "Rename Cad Files" will be passed to
             the CAD integration in a callback.  If the "Rename
             Cad Files", is set to true by the user, the cad files need to be renamed by
             the cad integration.
             
             The result will be a duplicated structure with the expected cad dependencies and
             it will open in the CAD tool without any errors.
             


Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A list of <font face="courier" height="10">DuplicateInputInfo</font>, the struct
                         that contains the information needed to duplicate (clone) an assembly structure.
             
        :return: 
        """
        ...
    def ExpandOrUpdateDuplicateItems(self, Infos: list[ExpandOrUpdateDuplicateItemsInfo]) -> ExpandOrUpdateDuplicateItemsResponse:
        """    
             This operation is called as part of the duplicate functionality.   It expands the
             structure one level at a time and gets structure dependent data. The dependencies
             have been defined to allow duplication of CAD dependent structure.  The expandOrUpdateDuplicateItems operation uses Business Modeler IDE
             global constant StructureCloneTransferModes to determine which of the cad
             specific attachments and relationships can be expanded. This constant defines the
             transfer modes containing dependent closure rules for expansion and cloning.  The
             value for the closure rules is added by the installed CAD system.
             

             Note: The difference between expandOrUpdateDuplicateItems,
             expandOrUpdateDuplicateItems2 and expandOrUpdateDuplicateItems3 are as follows:
             

             Difference in expandOrUpdateDuplicateItems
             and expandOrUpdateDuplicateItems2

             -    We allow the user to select a sub assembly for duplication.
             There is a performance problem that was uncovered.  Even though a sub assembly is
             sent for duplication, traversal on the server side was happening from the top BOMLine
             of the structure.  To improve the performance we get a BOB object.
             

             -    The smart selection logic was added to decide whether to
             clone or reference an Item in a structure based on the project that the top
             line of the original structure belongs to.  This smart selection logic is bottom
             up, so if a child is selected based on project assignment, the parent will be selected,
             no matter whether the parent belongs to the top item project assignment or not.
             

             Difference in expandOrUpdateDuplicateItems2
             and expandOrUpdateDuplicateItems3

             The mandatory flag is passed back to the client.  When a cad option has been flagged
             with a mandatory flag, a "R" predicate in the closure rules, that option will
             come up in the Duplicate Dialog pre-checked and its selected status will be un-changeable.
             This will prevent the user from un-checking those ItemRevision objects that
             were added in to make the structure cad consistent.  That is if a family table member
             in the assembly structure has been selected for duplication, then automatically include
             all its masters from the referenced ItemRevision all the way to the top master.
             Including the masters automatically will only happen if the CAD closure rules are
             defined with a predicate "R" that says this CAD relation is mandatory for
             duplication.
             


Use Cases:

             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input and the value of the closure
             rules defined.  The input consists of the BOMLine for expansion, the ItemRevision
             objects on which to perform the expansion, and the dependency types.  The ItemRevision
             objects could be null, in which case the ItemRevision object(s) gotten from
             the expansion of the BOMLine are used.  The dependency types are checked against
             the definition in the closure rules to determine what dependent data is expanded.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Infos: 
                         It contains the <b>BOMLine</b> objects, list of <b>ItemRevision</b> objects and list
                         of Dependency types
             
        :return: 
        """
        ...
    def ValidateStructureItemIds(self, Inputs: list[ValidateStructureItemIdsInfo]) -> ValidateStructureItemIdsResponse:
        """    
             This operation will validate the un-validated ItemIds that will be used to clone(duplicate)
             an assembly structure.  All portions of the structure that are displayed in the duplicate
             dialog have been validated by the client.
             

             Note: The differences between the three operations validateStructureItemIds,
             validateStructureItemIds2 and validateStructureItemIds3 are the following:
             
             - In validateStructureItemIds the input is
             the top BOMLine of the original configured structure in Structure Manager.
             In validateStructureItemIds2 the input is
             the selected BOMLine of the configured structure in Structure Manager or Systems
             Engineering.  i.e. the user can select to clone a sub-assembly of the original structure
             or the entire assembly.  The input for validateStructureItemIds2
             includes project(s).  The cloned structure is assigned to those project(s).  validateStructureItemIds did not have projects
             as input.
             

             - validateStructureItemIds3 was created as
             a result of the Multi Field Key(MFK) project.  The difference between validateStructureItemIds2 and validateStructureItemIds3
             is that in validateStructureItemIds2 the
             input and output have a DuplicateIdMap2 whereas
             to align with the MFK project, validateStructureItemIds3
             has a DuplicateIdStructure.
             


Use Cases:

             The user sends in a structure for validation of the new ItemIds .  The input to this
             operation is the top BOMLine, a map of old ItemIds to new ones for those Item
             objects that are already validated, and the default naming scheme.  Based on the
             structure traversal, the input map, and the naming scheme this operation validates
             whether the proposed names for the un-validated Item objects are valid.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         List of structure ValidateStructureItemIdsInput that contains the information needed
                         for validation before a duplicate operation  can be performed.
             
        :return: 
        """
        ...

