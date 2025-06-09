import System
import System.Collections
import Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ProjectInfo:
    """
    Project Information for Structure Clone
    """
    def __init__(self, ) -> None: ...
    Assign: bool
    """Flag that indicates if assigning projects"""
    Validate: bool
    """Flag that indicates if project needs validation"""
    Projects: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """Vector of user selected projects"""

class DuplicateInputInfo2:
    """
    Input for Duplicate2 SOA API
    """
    def __init__(self, ) -> None: ...
    TopLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            The top BOMLine or selected BOMLine of the structure to be cloned.
            The user can select a sub assembly from the original structure to clone.  This input
            cannot be NULL.  If it is the duplicate dialog will not come up at all.
            """
    DuplicateIdMap: System.Collections.Hashtable
    """
            A map of oldItemId and NewItemInfo structure. The newItemInfo is made up of the proposed
            new ItemId and the proposed new ItemName
            """
    DefaultName: Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DefaultNaming
    """The pattern to form a new ItemId"""
    Projects: ProjectInfo
    """The user selected projects to add the duplicated Item objects to"""
    RenameCadFile: bool
    """Whether to rename the cad files or not"""
    Options: list[str]
    """The list of dependency types.  This defines the cad traversal."""
    DuplicateOption: int
    """A bitmap for duplicate option. 1 means smart selection."""

class NewItemInfo2:
    """
    The proposed new ItemIds and new ItemNames.
    """
    def __init__(self, ) -> None: ...
    NewItemId: str
    """The proposed new ItemId"""
    NewItemName: str
    """The proposed new ItemName"""

class ValidateStructureItemIdsInfo2:
    """
    
Input to ValidateStructureItemIds2. It contains the top BOMLine, map of
oldItemId
to NewItemInfo(NewItemId, NewItemName), default naming pattern and list of
dependency
types specified by the user.
    """
    def __init__(self, ) -> None: ...
    TopLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Top BOMLine or the selected bom line of the structure or sub structure to
            be cloned.
            """
    InputMap: System.Collections.Hashtable
    """
            Map of OldItemIDs to  NewItemInfo2 that contains the proposed New ItemId and New
            ItemName.
            """
    DefaultName: Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DefaultNaming
    """Pattern to form a new ItemId."""
    Projects: ProjectInfo
    """
            List of user defined projects to which the duplicated Item objects will be
            added.
            """
    Options: list[str]
    """List of dependency types."""

class ValidateStructureItemIdsResponse2:
    """
    
The response from ValidateStructureItemIds, containing a map of OldItemID to
NewItemInfo, list of ItemRevision objects
failed validation and a ServiceData object.
    """
    def __init__(self, ) -> None: ...
    ClonedIdMap: System.Collections.Hashtable
    """
            Map of OldItemID to NewItemInfo that contains
            the proposed New ItemId and New ItemName
            """
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
    def Duplicate2(self, Inputs: list[DuplicateInputInfo2]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateResponse:
        """    
             This operation will create a duplicate (clone) of the input structure from its top
             level down or a selected sub assembly.
             
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
             
             If project(s) have been passed in as input, the cloned structure is assigned to that
             project(s).  By default the projects to which the top BOMLine in the duplicate
             dialog belongs and to which the user has access, is used to populate the project
             list.  The user has the option to modify that list based on which projects are available
             to that user.
             
             All of the structure dependent data of the input structure like datasets and attachments
             are copied to the duplicated structure based on the Business Modeler IDE deep copy
             rules for SaveAs.  The duplicate operation
             internally uses SaveAs at every level of
             the structure; therefore it uses the SaveAs
             deep copy rules.
             
             If the structure being cloned is a Requirements Manager structure, tracelink GRMs
             are handled based on the deep copy rules set for ReqRev for SaveAs.
             
             Target                            
             ReqRev
             
             Relation                        
             FND_TraceLink                
             
             Attached Type                ReqRev
             
             Operation                        SaveAs
             
             Action                            
             CopyAsReference
             
             Condition
             
             Direction                        
             IsTargetPrimary= false
             

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
             and duplicate3 is that in duplicate2 is that the input and output had a DuplicateIdMap2 whereas to align with the MFK project, duplicate3 has a DuplicateIdStructure



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
             rules have been defined in the Business Modeler IDE global constant StructureCloneTransferModes.
             
             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned.
             
             The user selects the cad dependency option Part Family Master.  The expansion and
             cloning will be done based on the closure rules defined for Part Family Master in
             the CAD closure rules.
             
             The "Rename Cad Files" will be passed to
             the CAD integration in a callback.  If the "Rename
             Cad Files", is set to true by the user, the cad files need to be renamed by
             the cad integration.
             
             The result will be a duplicated structure with the expected cad dependencies and
             it will open in the CAD tool without any errors.
             

Use case3: Requirements Manager (Systems Engineering) Clone:

             The user has a requirements manager structure with internal and/or external tracelink
             GRMs that need to be copied to the cloned structure.  The user defines a set of projects
             to which the newly cloned structure should belong.  The user does not want to clone
             the entire structure only a sub-assembly.
             
             The precondition to this operation, is that the deep copy rules for SaveAs have been setup correctly
             
             The user invokes the duplicate operation by passing in the selected BOMLine
             of the sub structure to be cloned.  The projects to which the cloned structure should
             belong are passed in as input.  The naming rule for the ItemId is passed in.
             
             The result is a requirement manager structure with the tracelink relations pointing
             to the correct objects in the new structure.  And the newly cloned structure belongs
             to the defined projects for which the user has permissions.
             



Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A list of <font face="courier" height="10">DuplicateInputInfo2</font> - A struct
                         that contains the information needed to duplicate (clone) an assembly structure.
             
        :return: 
        """
        ...
    def ExpandOrUpdateDuplicateItems2(self, OpInput: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsInfo], SelectionOption: int) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsResponse:
        """    
             This operation is designed to expand structures one level at a time and get structure
             dependent data. When it is flagged for smart selection, it will try to solve the
             uncertain smart selection by expansion, in which case only qualified ItemRevision
             objects will be returned. This operation is used by the duplicate (clone) structure
             feature.  The dependencies have been defined to allow duplication of CAD dependent
             structure.  The expandOrUpdateDuplicateItems2
             operation uses Business Modeler IDE global constant StructureCloneTransferModes
             to determine which  of the cad specific attachments and relationships can be expanded.
             This constant defines the transfer modes containing dependent closure rules for expansion
             and cloning.  The value for the closure rules is added by the installed CAD system.
             

Note: The difference between expandOrUpdateDuplicateItems,
             expandOrUpdateDuplicateItems2 and expandOrUpdateDuplicateItems3 is as follows:
             

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

Use case 1: selectionOption is 0 and the original structure has cad data:
             
             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input and the value of the defined
             closure rule.  The input consists of the BOMLine for expansion and ItemRevision
             objects on which to perform the expansion,  the dependency types, and the selectionOption.
             The ItemRevision objects could be null, in which case the ItemRevision
             object(s) gotten from the expansion of the BOMLine are used.  The dependency
             types are checked against the definition in the closure rules to determine  what
             dependent data is expanded.
             

Use case 2: selectionOption is 1 and the original structure has no cad data
             
             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input.  In this case no closure
             rule may be defined, since the structure has no cad data.   The input consists of
             the BOMLine for expansion and ItemRevision objects on which to perform
             the expansion,  the dependency types, and the selectionOption.  The ItemRevision
             objects could be null, in which case the ItemRevision object(s) gotten from
             the expansion of the BOMLine are used.  Since the selectionOption is 1, the
             input lines will be checked based on the top BOMLine object's project assignments.
             


Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param OpInput: 
                         Contains the <b>BOMLine</b> objects, list of <b>ItemRevision</b> objects and list
                         of Dependency types
             
        :param SelectionOption: 
                         When the value is 1, the system will check the input lines based on the top <b>BOMLine</b>
                         item's project assignment. If any child belongs to the project, then the parent <b>BOMLine</b>
                         will be returned otherwise the parent <b>BOMLine</b> will not be returned. When the
                         value is 0, the operation will do expansion only.
             
        :return: 
        """
        ...
    def ValidateStructureItemIds2(self, Inputs: list[ValidateStructureItemIdsInfo2]) -> ValidateStructureItemIdsResponse2:
        """    
             This operation is called as part of the duplicate/clone operation.  It will validate
             the un-validated ItemIds and user selected projects that will be used to clone(duplicate)
             an assembly structure.   All portions of the structure that are displayed in the
             duplicate dialog have been validated by the client.
             

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

             The user sends in a structure for validation of the new ItemIds.  The input to this
             operation is the top BOMLine or the selected BOMLine, a map of old
             ItemIds to new ones for those Item objects that are already validated, the
             default naming scheme and a list of user defined projects to which the duplicated
             items will be added.  Based on the structure traversal, the input map, and the naming
             scheme this operation validates whether the proposed names for the un-validated Item
             objects are valid and whether the user can add the new structure to the list of user
             defined projects.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A list of structure <font face="courier" height="10">ValidateStructureItemIdsInput2</font>
                         that contains the information needed for validation before a duplicate operation
                         would be performed.
             
        :return: 
        """
        ...
    def PackOrUnpack(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Flag: int) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Provides set-based pack/unpack functionality. When recursive option is selected,
             all loaded substructures of the selected lines will also be packed or unpacked.
             

Use Cases:


User calls the operation with some lines to pack them, the lines
             will be packed.
             
User calls the operation with root line to unpack the whole structure,
             all loaded packed lines in the structure will be unpacked.
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Lines: 
                         The lines that need to be packed. If pack all option is selected, the children of
                         the lines will be packed.
             
        :param Flag: 
                         0:pack the lines 1:unpack the lines 2:pack all lines 3:unpack all lines
             
        :return: 
        """
        ...

