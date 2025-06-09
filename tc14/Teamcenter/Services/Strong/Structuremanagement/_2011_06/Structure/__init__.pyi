import System
import Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure
import Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClosureRuleVariableInfo:
    """
    
Contains variable name and value pair where the variable is a part of the
ClosureRule.
The values are to be replaced with variable during ClosureRule evaluation.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Variable name used in ClosureRule."""
    Value: str
    """Value for the variable."""

class DuplicateIdStructure:
    """
    Structure of oldItem component and NewItemInfo structure.
    """
    def __init__(self, ) -> None: ...
    OldItemComponent: Teamcenter.Soa.Client.Model.Strong.Item
    """The original Item"""
    NewItemInfo: Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.NewItemInfo
    """The proposed new ItemId and ItemName"""

class DuplicateInputInfo3:
    """
    Input for Duplicate SOA API
    """
    def __init__(self, ) -> None: ...
    TopLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            The top BOMLine or selected BOMLine of the structure to be cloned.
            The user can select a sub assembly from the original structure to clone.  This input
            cannot be NULL.  If it is the duplicate dialog will not come up at all.
            """
    ClonedIdStructure: list[DuplicateIdStructure]
    """
            A structure of oldItem which points to the NewItemInfo.  The newItemInfo is made
            up of the proposed new ItemId and the proposed new ItemName
            """
    DefaultName: Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DefaultNaming
    """The pattern to form the new ItemId"""
    RenameCadFile: bool
    """Whether to rename the CAD files or not"""
    Options: list[str]
    """The list of dependency types.  This defines the cad traversal."""
    Projects: Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure.ProjectInfo
    """The user selected projects to add the duplicated Item objects to"""
    DuplicateOption: int
    """
            A bitmap for the duplicate option. 1 means smart selection. It can be used for future
            extension.
            """

class ExpandOrUpdateDuplicateItemsOutput2:
    """
    
The ExpandOrUpdateDuplicateItemsOutput2 represents
the collection of all related data objects with the structure ItemRevision
object(s) or part family masters ItemRevision object(s).
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The BOM structure ItemRevision or a part family master ItemRevision."""
    RelatedObjInfo: list[RelatedItemsInfo2]
    """List of all dependent objects that are related to the object."""

class ExpandOrUpdateDuplicateItemsResponse2:
    """
    
The ExpandOrUpdateDuplicateItemsResponse2
structure represents the results of the structure dependent data search.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[ExpandOrUpdateDuplicateItemsOutput2]
    """
            List of ExpandOrUpdateDuplicateItemsOutput2
            which contains information about the BOM structure ItemRevision to its related
            data relationships.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The error information will be recorded here."""

class RelatedItemsInfo2:
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
    Mandatory: bool
    """
            Is dependent type mandatory or not - If it is mandatory that cad dependent type will
            come in pre-checked and the user will not be able to de-select it.
            """

class ValidateStructureItemIdsInfo3:
    """
    
Input to ValidateStructureItemIds3. It contains top BOMLine, structure of
oldItemComponent to NewItemInfo(NewItemId,
NewItemName), default naming pattern and list of dependency types specified by
the
user.
    """
    def __init__(self, ) -> None: ...
    TopLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Top BOMLine or the selected BOMLine of the structure or sub structure
            to be cloned.
            """
    ClonedIdStructure: list[DuplicateIdStructure]
    """
            Structure of OldItem components to the NewItemInfo
            struct that contains the proposed New ItemId and New ItemName
            """
    DefaultName: Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DefaultNaming
    """Pattern to form a new ItemId."""
    Options: list[str]
    """The list of dependency types."""
    Projects: Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure.ProjectInfo
    """
            The list of user defined projects to which the duplicated Item objects will
            be added.
            """

class ValidateStructureItemIdsResponse3:
    """
    
response from ValidateStructureItemIds, containing Structure of OldItem
component,
NewItemInfo, list of itemrevisions failed validation and Service Data object.
    """
    def __init__(self, ) -> None: ...
    ClonedIdStructure: list[DuplicateIdStructure]
    """
            Structure of OldItem components to the Structure NewItemInfo that contains the proposed
            New ItemId and New ItemName.
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
    def Duplicate3(self, Inputs: list[DuplicateInputInfo3]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateResponse:
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
             does not have projects as input.
             

duplicate2 and duplicate3

             - duplicate3 was created as a result of the
             Multi Field Key (MFK ) project.   The difference between duplicate2
             and duplicate3 is that in duplicate2 is that the input and output had a DuplicateIdMap2 whereas to align with the MFK project, duplicate3 has a DuplicateIdStructure.
             


Use Cases:

Use case1: Simple Clone

             A user has an assembly which does not have cad dependencies nor does it belong to
             a specific project(s).  The user wants to duplicate the entire structure with a specific
             naming pattern for the ItemIds.  The naming pattern is a prefix "test_".
             
             The user invokes the duplicate operation by passing in the top BOMLine of the structure
             to be cloned, and the naming pattern for the new structure.  The result is a new
             structure with the following naming pattern for the ItemIds -> test_OriginalItemId.
             

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
             

Use case3: Requirements Manager (Systems Engineering) clone:

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
                         A vector of DuplicateInputInfo3 structs that contains the information needed to duplicate
                         (clone) an assembly structure.
             
        :return: 
        """
        ...
    def ExpandOrUpdateDuplicateItems3(self, OpInput: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsInfo], SelectionOption: int) -> ExpandOrUpdateDuplicateItemsResponse2:
        """    
             This operation  is designed to expand structures one level at a time and get structure
             dependent data. When it is flagged for smart selection, it will try to solve the
             uncertain smart selection by expansion, in which case only qualified ItemRevision
             objects will be returned. This operation is used by the duplicate (clone) structure
             feature.  The dependencies have been defined to allow duplication of CAD dependent
             structure.  The expandOrUpdateDuplicateItems3
             operation uses Business Modeler IDE global constant StructureCloneTransferModes
             to determine which  of the cad specific attachments and relationships can be expanded.
             This constant defines the transfer modes containing dependent closure rules for expansion
             and cloning.  The value for the closure rules is added by the installed CAD system.
             For this version of the operation a mandatory clause has been added in the closure
             rules that removes the limit on one level of relationship traversal.   This was done
             to enhance the Duplicate functionality to ensure that the duplicated structure is
             CAD consistent.
             

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
             The ItemRevision objects could be null, in which case the ItemRevision object(s)
             gotten from the expansion of the BOMLine are used.  The dependency types are
             checked against the definition in the closure rules to determine  what dependent
             data is expanded.
             


             Use case 2: selectionOption is 1 and the original structure has no cad data
             
             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input.  In this case no closure
             rule may be defined, since the structure has no cad data.   The input consists of
             the BOMLine for expansion and ItemRevision objects on which to perform
             the expansion,  the dependency types, and the selectionOption.  The ItemRevision
             objects could be null, in which case the ItemRevision object(s) gotten from
             the expansion of the BOMLine are used.  Since the selectionOption is 1, the
             input lines will be checked based on the top Use case 1: selectionOption is 0 and
             the original structure has cad data:
             
             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input and the value of the defined
             closure rule.  The input consists of the BOMLine for expansion and ItemRevision objects
             on which to perform the expansion,  the dependency types, and the selectionOption.
             The ItemRevision objects could be null, in which case the ItemRevision object(s)
             gotten from the expansion of the BOMLine are used.  The dependency types are
             checked against the definition in the closure rules to determine  what dependent
             data is expanded.
             


Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param OpInput: 
                         Contains the <b>BOMLine</b> objects, list of <b>ItemRevision</b> objects and list
                         of Dependency types.
             
        :param SelectionOption: 
                         When the value is 1, the system will check the input lines based on the top <b>BOMLine</b>
                         item's project assignment. If any child belongs to the project, then the parent <b>BOMLine</b>
                         will be returned otherwise the parent <b>BOMLine</b> will not be returned. When the
                         value is 0, the operation will do expansion only.
             
        :return: 
        """
        ...
    def ValidateStructureItemIds3(self, Inputs: list[ValidateStructureItemIdsInfo3]) -> ValidateStructureItemIdsResponse3:
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
             operation is the top BOMLine or the selected BOMLine, a structure of
             old item components to new ItemId and new ItemName for those Item objects that are
             already validated, the default naming scheme and a list of user defined projects
             to which the duplicated Item objects will be added.  Based on the structure
             traversal, the input structure, and the naming scheme this operation validates whether
             the proposed names for the un-validated Item objects are valid and whether
             the user can add the new structure to the list of user defined projects.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A list of structure <font face="courier" height="10">ValidateStructureItemIdsInput3</font>
                         that contains the information needed for validation before a duplicate operation
                         would be performed.
             
        :return: 
        """
        ...
    def SetClosureRuleVariablesAndValues(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, ClosureRuleName: str, ClosureRuleVariableInfos: list[ClosureRuleVariableInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Sets ClosureRule on the BOMWindow. If ClosureRule has variables
             then respective values supplied are used during ClosureRule evaluation. Only
             ClosureRule with scope PIE_TEAMCENTER is considered by this operation.
             

             In case if ClosureRule should be reset on BOMWindow then input ClosureRule
             name should be empty string.
             

Use Cases:

             Perform controlled BOM expansion using ClosureRule.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Window: 
                         The <b>BOMWindow</b> on which <b>ClosureRule</b> is to be set.
             
        :param ClosureRuleName: 
                         Valid <b>ClosureRule</b> name to search <b>ClosureRule</b> object with scope as scope
                         PIE_TEAMCENTER.
             
        :param ClosureRuleVariableInfos: 
                         List of structures holding variable name and corresponding value as string.
             
        :return: 
        """
        ...
    def UnloadBelow(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], UnloadType: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation unloads and destroy the BOM structure ( i.e. BOMLine objects)
             below supplied BOMLine object or objects. It would unload associated persistence
             objects like Item, ItemRevision, PSBomViewrevision and PSOccurrence
             etc. and free up memory.
             

Use Cases:

             The operation is intended to improve the scalability of BOM structure expansion.
             From a large BOM structure, user can unload the BOM structure that he has finished
             working on. This will free up the memory which would be used for expanding another
             sub-structure that user starts working on.
             

Teamcenter Component:

             BOM Expand - Set of core services that allow to efficiently solve a product structure
             based on revision rules; effectivities etc.
             
        :param Bomlines: 
                         The <b>BOMLine</b> itself is not unloaded.
             
        :param UnloadType: 
                         Currently only <font face="courier" height="10">Unrecoverable</font> unload Type
                         is supported.
             
        :return: objects could
             not be unloaded.
        """
        ...

