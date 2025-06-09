import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CloneStructureDefaultNaming:
    """
    
The CloneStructureDefaultNaming structure conatians the information to help form
new Item IDs.
    """
    def __init__(self, ) -> None: ...
    Autogen: bool
    """Auto assign new item IDs. If set to True this takes precedence over all other parameters."""
    Prefix: str
    """
            Substring to be prefixed to the old item ID to form a new item ID. This parameter
            can be used in conjuction with the other parameters except when autogen is set to
            True.
            """
    Suffix: str
    """
            Substring to be suffixed to the old item ID to form a new item ID. This parameter
            can be used in conjuction with the other parameters except when autogen is set to
            True..
            """
    From: str
    """
            Substring to be replaced from the old item ID by another substring to form a new
            item ID. This parameter is required to work in conjuction with the "to" parameter
            but can be used in conjuction with the other parameters except when autogen is set
            to True.
            """
    To: str
    """
            Substring to replace with a substring from the old item ID to form a new item ID.
            This parameter is required to work in conjuction with the "from" parameter but can
            be used in conjuction with the other parameters when except autogen is set to True.
            """

class CloneStructureExpandOrUpdateDuplicateItemsOutput:
    """
    
The CloneStructurExpandOrUpdateDuplicateItemsOutput represents the collection of
all related data objects with the structure ItemRevision object(s) or part
family masters ItemRevision object(s).
    """
    def __init__(self, ) -> None: ...
    ParentObject: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The BOM structure ItemRevision or a part family master ItemRevision."""
    ParentObjectCloneable: int
    """
            Indicates if the object can be cloned.
            
            0 - users choice to clone or not
            
            1 - mandatory - If it is mandatory that cad dependent type will come in pre-checked
            and the user will not be able to de-select it.
            
            2 - Must not be cloned - If set the cad dependent type will come in unchecked and
            the user will not be able to select it.
            
"""
    RelatedObjectInfo: list[CloneStructureRelatedItemsInfo]
    """List of all dependent objects that are related to the object."""

class CloneStructureExpandOrUpdateItemsInfo:
    """
    
The CloneStructureExpandOrUpdateItemsInfo structure contains the information
needed
to conduct an expand or update of a BOM structure that will be duplicated.
    """
    def __init__(self, ) -> None: ...
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            If it is not null, expand it and get its dependencies based on the depTypes. The
            BOMLine can be any line in the structure that the user picks for expansion.
            """
    ItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """
            The ItemRevision objects to perform search dependencies on. If empty, the
            ItemRevision objects to be used will be from the expansion of the BOMLine.
            """
    CadOptions: list[str]
    """
            The dependency types to use for the operation.
            
            Following are the CAD options values that are used for CAD Dependency searches:
            
            Drawings, Required, PartFamilyMaster, PartFamilyMember, AllDep and  Internal.
            """

class CloneStructureExpandOrUpdateResponse:
    """
    
The CloneStructureExpandOrUpdateResponse structure contains the results of the
structure
dependent data search.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[CloneStructureExpandOrUpdateDuplicateItemsOutput]
    """
            List of CloneStructureExpandOrUpdateDuplicateItemsOutput which contains information
            about the BOM structure ItemRevision to its related data relationships.
            """
    AdditionalDependencies: list[str]
    """
            List of available non static CAD dependencies that are derived from the CAD dependency
            closure rules
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The error information will be recorded here."""

class CloneStructureProjectInfo:
    """
    
The CloneStructureProjectInfo contains project information for Structure Clone
to
validate the projects and assign the cloned objects to the user selected
projects.
    """
    def __init__(self, ) -> None: ...
    Assign: bool
    """Flag that determines if projects are to be assigned to new cloned objects."""
    Validate: bool
    """Flag that determines if validation needs to be executed on projects."""
    Projects: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """List of projects that the new cloned objects will be assigned to."""

class CloneStructureInputInfo:
    """
    
CloneStructureInputInfo that contains all the information needed to validate and
duplicated multiple structures in one API call.
    """
    def __init__(self, ) -> None: ...
    TopLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            The top BOMLine or selected BOMLine of the structure to be cloned.
            The user can select a sub assembly from the original structure to clone. (If running
            Async mode this input needs to be NULL.)
            """
    CadOptions: list[str]
    """
            List of CAD dependency options to process and traverse in the structure to be duplicated.
            
            Typical options would be Drawings, Required, PartFamilyMaster, PartFamilyMember,
            AllDep and Internal.
            """
    DefaultName: CloneStructureDefaultNaming
    """The pattern to form the new ItemId."""
    DataMap: list[CloneStructureSaveAsIn]
    """
            A struct vector of original ItemRevisions and instructions which tells duplicate
            operation what to do with each component of the structure.
            """
    CloneFlags: int
    """
            A bitmap for the duplicate flags set.
            
            1 - smart selection using topLine assigned projects
            
            2 - rename cad files
            
            4 - return cloned object map information
            
                  (nor supported in background mode)
            
                  (RAC will always set this to false)
            
            8 - run duplicate in background mode
            
                  (this activates the Async mode if it is available)
            
            16- run duplicate in validate mode
            
"""
    Projects: CloneStructureProjectInfo
    """The user selected projects to which to add the duplicated Item objects."""
    DefaultFolder: Teamcenter.Soa.Client.Model.Strong.Folder
    """The folder to add the duplicated structures into. (can be NULL)"""
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """
            If duplicate operation is being run in the background send in the revRule to use
            when creating the new BOMWindow (required for Async).
            """
    TopItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """
            If duplicate operation is being run in the background need the top item revision
            of the structure to create the new BOM Window (required for Async).
            """

class CloneStructureRelatedItemsInfo:
    """
    
The CloneStructureRelatedItemsInfo represents the dependent data found and how
it
is related to a structure ItemRevision. RelatedItemsInfo also can represent
a family table member to a family table master.
    """
    def __init__(self, ) -> None: ...
    RelatedObject: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """An ItemRevision that is the related data."""
    RelatedObjectCloneable: int
    """
            Indicates if the relObj can be cloned.
            
            0 - users choice to clone or not
            
            1 - mandatory - If it is mandatory that cad dependent type will come in pre-checked
            and the user will not be able to de-select it.
            
            2 - Must not be cloned - If set the cad dependent type will come in unchecked and
            the user will not be able to select it
            
"""
    RelatedObjectGRMName: str
    """The GRM relationship used to find the related data."""
    RelatedObjectCADOptionName: str
    """The cad dependency type use for the operation."""

class CloneStructureResponse:
    """
    
The CloneStructureResponse structure contains the response information for the
cloneStructure
API.
    """
    def __init__(self, ) -> None: ...
    DataMap: list[CloneStructureSaveAsIn]
    """
            This is populated when validation of BOM structure fails or validateOnly flag is
            set to true. Reason for returning this information is it allows the calling client
            to reuse this data to speed the re-validation of the structure once the user fixes
            the error. The struct vector will contain the original Item Revisions, operation
            type, replacing item revision, MFK, PropertyValues and DeepCopyData overrides for
            each level of the structure.
            

            If validation passes and validateOnly flag is set to false this will be empty.
            
"""
    ClonedItemRevInfoMap: System.Collections.Hashtable
    """Map of bomlines to their new cloned item rev and clone status."""
    ClonedObjectInfoMap: System.Collections.Hashtable
    """
            Map of original objects and their cloned equivalent (will be empty if validation
            fails). (not support in Async mode)
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data return where the partial errors are placed."""

class CloneStructureSaveAsIn:
    """
    
The CloneStructureSaveAsIn structure contains all the instructions that tells
duplicate
what to do with the children of the structure to be duplicated.
    """
    def __init__(self, ) -> None: ...
    OrigItemRevComp: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Original item revision component to be cloned."""
    CloneOperationType: int
    """
            Indicates if the original item revision component is to be:
            
            0 - Clone, component is part of the structure to be cloned and we want to clone the
            component.
            
            1 - Reference, component is part of the structure to be cloned and we want to reference,
            not clone the component.
            
            2 - Revise, component is part of the structure to be cloned and we want to revise
            the component.
            
            3 - Replace, component is part of the structure to be cloned and we want to replace
            the component with an existing part.
            
            4 - Include, component is not a part of the structure to be cloned and we want to
            clone the component because it has some relation to the structure to be cloned that
            is not published to Teamcenter.
            
"""
    NewItemRevinfo: System.Collections.Hashtable
    """
            Struct that contains all information related to item revision based on following
            operations:
            


Clone/Revise - will contain Property values (MFK complaint) to support
            business object "save-as" and "revise" operations
            
Reference - will be empty
            
Replace - will contain replacing Item revision "item_id" and "rev_id"
            values.
            

"""
    DeepCopyDataOverride: list[DeepCopyData]
    """
            Vector of DeepCopyData elements that instructs the "Save As" operation what attached
            data to clone and not clone (Save As Descriptors) for the item revision.
            
            Note: Reference, Revise and Replace operation will not use this parameter and such
            it will be empty.
            
"""

class CloneStructureTopLineData:
    """
    
The CloneStructureTopLineData structure contains the high-level status
information
of a BOM structure that was validated and duplicated.
    """
    def __init__(self, ) -> None: ...
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            The top line assembly that represent the original Item revision that was cloned to
            make the new cloned Item revision.
            """
    OrignalItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Original Item Revision that was cloned to make the new cloned Item Revision."""
    ClonedNewItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """New cloned topline item revision."""
    Status: int
    """
            Status of cloning the topline.
            
            0 - Clone Successful
            
            46229 - Clone Failed
            
            46230 - Clone With Partial Errors
            
            46231 - Validate Failed
            
            46232 - Clone Asynchronous Job Submitted
            
"""

class DeepCopyData:
    """
    
The DeepCopyData data structure holds the relevant information regarding
applicable
deep copy rules
    """
    def __init__(self, ) -> None: ...
    AttachedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Other side object."""
    PropertyName: str
    """Name of relation type or reference property for which DeepCopy rule is configured."""
    PropertyType: str
    """
            If Relation, it represents Relation type property. If Reference, it
            represents Reference property
            """
    CopyAction: str
    """DeepCopy action [NoCopy, CopyAsReference, CopyAsObject, Select ]."""
    IsTargetPrimary: bool
    """
            If true the target object is processed as primary, otherwise it is processed as a
            secondary object.
            """
    IsRequired: bool
    """
            If true, the copy action can not be modified. If false, the copy action can be changed
            to different action by the user.In this case, the copy action field in the revise
            dialog is editable.
            """
    CopyRelations: bool
    """
            If true, the custom properties on the source relation object are copied over to the
            newly-created relation. If false, custom properties are not copied.
            """
    OperationInputTypeName: str
    """OperationInput type name."""
    ChildDeepCopyData: list[DeepCopyData]
    """List of DeepCopy data for the secondary objects on the other side."""
    OperationInputs: System.Collections.Hashtable
    """
            OperationInput field to capture property values of attached object, to apply on copied
            object of attached object. Map of property name(key) and property values(values)
            in string format of attached object, to be set on copied object of attached object.
            The calling client is responsible for converting the different property types (int,
            float, date .etc) to a string using the appropriate toXXXString functions in the
            SOA client framework Property class.
            """

class Structure:
    """
    Interface Structure
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CloneStructure(self, Inputs: list[CloneStructureInputInfo]) -> CloneStructureResponse:
        """    
             This operation validates and creates a duplicate (clone) of the input structure
             from its top level down or a selected sub assembly.
             

             Depending on the input arguments, all or some of the original structure is duplicated
             and the rest are referenced, revised or replaced.
             

             The caller can define a specific naming pattern for the Item ids of the duplicated
             (cloned) structure. The caller can define specific Item ids for individually selected
             ItemRevision objects or a default naming pattern for the duplicated structure.
             The default pattern can be defined by adding prefixes, suffixes or replacing part
             of the original name with a different pattern. The caller can also choose to allow
             the system to assign default ids.
             

             If project(s) have been passed in as input, the cloned structure is assigned to that
             project(s). By default the projects to which the top BOMLine in the duplicate
             dialog belongs and to which the user has access, is used to populate the project
             list. The user has the option to modify that list based on which projects are available
             to that user.
             

             All of the structure dependent data of the input structure like Datasets and
             attachments are copied to the duplicated structure based on the Business Modeler
             IDE Deep Copy Rules for SaveAs or the Deep Copy Data override rules
             parameter passed in to the input structure. The duplicate operation internally uses
             SaveAs at every level of the structure; therefore it uses the SaveAs Deep
             Copy Rules.
             

             If the structure being cloned is a Requirements Manager structure,Tracelink
             GRMs are handled based on the deep copy rules set for ReqRev for SaveAs.
             
             CAD specific attachments and relations are copied based on the transfer mode defined
             for the Business Modeler IDE global constant StructureCloneTransferModes.
             The transfer mode contains dependent closure rules for expansion and cloning. The
             value for the closure rules is added by the installed CAD system.
             

             The caller can also tell the operation to just validate only and do not perform a
             duplicate of the input structures.
             

Note: The difference between the operations duplicate4 and cloneStructure
             are the following:
             

Duplicate4 and cloneStructure

             - cloneStructure was created as a result of the project to get NX CAD on board.
             The difference is cloneStructure will now process set based inputs, it combines
             the validate and duplicate actions into one API, provides a validate only mode, introduces
             the ability to override DeepCopyData GRM rules to change the core default DeepCopy
             rules behavior (with exception of restricted rules), the ability to choose the folder
             to store new cloned root item revisions into, added two new action types revise and
             replace along with the reference and clone action types for determining what to do
             with the children of the structure being cloned and  the cloneStructure will
             return all cloned mapping information to client if requested by cloneFlags.
             


Use Cases:

Use case1: Simple Clone


             A user has an assembly which does not have cad dependencies nor does it belong to
             a specific project(s). The user wants to duplicate the entire structure with a specific
             naming pattern for the ItemIds. The naming pattern is a prefix "test_".
             
             The user invokes the duplicate operation by passing in the top BOMLine of the structure
             to be cloned, and the naming pattern for the new structure. The result is a new structure
             with the following naming pattern for the ItemIds -> test_OriginalItemId.
             

Use case2: CAD Clone


             A user has an assembly structure which has cad dependencies. The user wants to start
             a new product with a similar structure and cad dependencies. The expansion and cloning
             rules have been defined in the Business Modeler IDE global constant StructureCloneTransferModes.
             
             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned.
             
             The user selects the cad dependency option Part Family Master. The expansion and
             cloning will be done based on the closure rules defined for Part Family Master in
             the CAD closure rules.
             
             The "Rename Cad Files" will be passed to the CAD integration in a callback.
             If the "Rename Cad Files", is set to true by the user, the cad files need
             to be renamed by the cad integration.
             
             The result will be a duplicated structure with the expected cad dependencies and
             it will open in the CAD tool without any errors.
             

Use case3: Requirements Manager (Systems Engineering) clone:


             The user has a requirements manager structure with internal and/or external tracelink
             GRMs that need to be copied to the cloned structure. The user defines a set of projects
             to which the newly cloned structure should belong. The user does not want to clone
             the entire structure only a sub-assembly.
             
             The precondition to this operation, is that the deep copy rules for SaveAs
             have been setup correctly
             
             The user invokes the duplicate operation by passing in the selected BOMLine
             of the sub structure to be cloned. The projects to which the cloned structure should
             belong are passed in as input. The naming rule for the ItemId is passed in.
             
             The result is a requirement manager structure with the tracelink relations pointing
             to the correct objects in the new structure. And the newly cloned structure belongs
             to the defined projects for which the user has permissions.
             

Use Case 4: Validate and Duplicate Process with Revise and Replace Child Component
             Options


             A user has an assembly to start a new product with a similar structure but wants
             to replace and revise some components for the new structure. The user will need to
             select the components to revise from the client interface and mark those selected
             as a revise action to be recorded in the data map. Then the user will need to select
             the components to replace from the client interface and enter an existing component
             to be the replacing component for the components selected for replace. The replacing
             action will also be recorded in the data map.
             
             The results will be a cloned structure where the children selected for replace and
             revise will be replaced and revised in the new cloned structure.
             

Use Case 5: Validate Only Mode


             A user has an assembly and wants to validate it before trying to clone it. User selects
             the assembly structure and selects the "Validate Only"  option.
             
             The results is the structure will run through a validation routine and not be cloned
             at all. The information of the validation will be returned to the client where the
             user then can fix any issues or proceed with the cloning.
             

Use Case 6: Run In Background Mode


             A user has a very large assembly and wants to clone it in background mode so they
             can free up there client interface to perform other work. The user selects the assembly
             structure and selects the "Run In Background"  option.
             
             The system will return a message saying the job was dispatched. Then the system will
             validate the structure against the input provided and then duplicate the structure
             in an Asynchronous Teamcenter server thread. The results of the "Run In Background"
             process will be recorded in a text dataset that will be sent to the user via Teamcenter
             Mail Envelope.
             

Use Case 7: Simple Validate and Duplicate Process And Return Cloned Data to Client


             A user has an assembly and wants to the cloned information to be returned to the
             client. The user selects the assembly structure and sets the "return cloned object
             information"  option for the cloneFlags.
             
             The results of the "return cloned object information " option will be returned to
             the client.
             
             Note: The "return cloned object information " option is primarily used for
             CAD Integrations to resolve there internal part to part links that Teamcenter would
             not know about. The RAC Duplicate Dialog does not use this option.
             


Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A vector of CloneStructureInputInfo structs that contains the information needed
                         to duplicate (clone) an assembly structure. Based on whether the processInBackground
                         flag is true, CloneStructureAsync will be called.
             
        :return: 46232 - The clone structure operation was successful submitting the Asynchronous
             clone job to the dispatcher.
        """
        ...
    def CloneStructureExpandOrUpdate(self, OpInput: list[CloneStructureExpandOrUpdateItemsInfo], SelectionOption: int) -> CloneStructureExpandOrUpdateResponse:
        """    
             This operation expand structures one level at a time and gets structure dependent
             data.
             

             When the 'selectionOption" is set to "1" for smart selection, it will try
             to solve the uncertain smart selection by expansion, in which case only qualified
             ItemRevision objects will be returned.
             

             The following are the CAD Dependency options the user can use when expanding or Updating
             a structure to be cloned.
             

Drawings
             
Required
             
PartFamilyMaster
             
PartFamilyMember
             
AllDep
             
Internal
             



             The CAD Dependency options correspond with the CAD Dependency rules defined by the
             Business Modeler IDE global constant "StructureCloneTransferModes". The CAD
             specific rules defined in the "StructureCloneTransferModes" will determine
             which of the CAD specific attachments and relationships can be expanded and included
             as part of the structure to be cloned. The values for the closure rules is added
             by the installed CAD system.
             

Note: The differences between expandOrUpdateDuplicateItems3 and cloneStructureExpandOrUpdate
             are as follows:
             

The CAD options passed into this operation are now strings and no
             longer integers.
             
The cloneStructureExpandOrUpdate API calls a DuplicateExpandOrUpdate
             Business Object operation.The new Business Object operation allows CAD integrations
             to register extension code to identify CAD specific "Internal" relations to a structure
             being duplicated that are not published to Teamcenter.
             



Use Cases:

Use case 1: selectionOption is 0 and the original structure has CAD data:


             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input and the value of the defined
             closure rule. The input consists of the BOMLine for expansion and ItemRevision
             objects on which to perform the expansion, the dependency types, and the selectionOption.
             The ItemRevision objects could be null, in which case the ItemRevision
             object(s) gotten from the expansion of the BOMLine are used. The dependency
             types are checked against the definition in the closure rules to determine what dependent
             data is expanded.
             

Use case 2: selectionOption is 1 and the original structure has no CAD data


             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input. In this case no closure
             rule may be defined, since the structure has no CAD data. The input consists of the
             BOMLine for expansion and ItemRevision objects on which to perform
             the expansion, the dependency types, and the selectionOption. The ItemRevision
             objects could be null, in which case the ItemRevision object(s) gotten from
             the expansion of the BOMLine are used. Since the selectionOption is 1, the
             input lines will be checked based on the top.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param OpInput: 

        :param SelectionOption: 

        :return: 
        """
        ...
    def ToggleOccurrenceSuppression(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation toggles occurrence suppression of the selected lines.
             

Use Cases:

             User wants to suppress some lines after the structure is constructed, user can call
             this operation to toggle the occurrence suppression of the lines.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Inputs: 
                         A list of <b>BOMLine</b> object to toggle the occurrence suppression.
             
        :return: 
        """
        ...
    def TogglePrecision(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation toggles precision of all lines.
             
Note: 

             -    leaf lines cannot change precision.
             
             -    If multiple lines for same item revision are passed in to
             the operation, the precision for the structure of the lines will be changed only
             once.
             


Use Cases:

             User wants to change precision of some lines after the structure is constructed,
             user can call this operation to toggle the precisions of the lines.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Inputs: 
                         the lines to toggle precision
             
        :return: 
        """
        ...

