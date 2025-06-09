import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2007_01.StructureManagement
import Teamcenter.Services.Strong.Cad._2008_03.StructureManagement
import Teamcenter.Services.Strong.Cad._2009_04.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AskChildPathBOMLineOutputNode:
    """
    
            This structure represents a node in the product structure. This structure is tied
            to a specific client ID of the input. Within the context of an input client ID, this
            structure represents the child path and its corresponding BOMLine object in
            the product structure.
            
    """
    def __init__(self, ) -> None: ...
    ChildPath: str
    """
            This is the PSOccurrenceThread UID or the Clone Stable ID specified in the
            input that represents a particular node in the context of the child path or occurrence
            thread chain.
            """
    Bomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The BOMLine object corresponding to the input child path."""

class AskChildPathBOMLinesResponse2:
    """
    
            This structure defines the response from the askChildPathBOMLines
            operation. The response contains the BOMLine objects for each of the input
            child paths which are still present in the Product Structure in Teamcenter. Each
            BOMLine object in the output is mapped
            to its corresponding input clientId and one
            childpath. Only the input nodes which are
            still in the Product Structure in Teamcenter will be in the output. If an input node no longer exists in the Product Structure,
            it will not be present in the output.
            
    """
    def __init__(self, ) -> None: ...
    Output: System.Collections.Hashtable
    """
            A map of input Client ID to a vector of structure containing the input child path
            and its corresponding BOMLine object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The SOA framework object containing plain objects and error information."""

class CreateOrUpdateRelativeStructureInfo4:
    """
    
            Contains the data for creating or updating the relative product structure for a item
            revision. It includes the information about the parent and its object and a list
            of type RelativeStructureChildInfo3 that
            describes the first level children and their occurrence information.
            
    """
    def __init__(self, ) -> None: ...
    ParentInfo: Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.RelativeStructureParentInfo
    """
            Object reference of the context assembly for create or update of the child occurrence,
            required input reference.
            """
    ChildInfo: list[RelativeStructureChildInfo3]
    """
            List of child info structures for creating the occurrences or updating the occurrence
            attributes. If no child objects are specified and RelativeStructureParentInfo
complete is true, all existing child objects
            will be removed. If no child objects are specified and RelativeStructureParentInfo
complete is false, the input is ignored.
            """

class CreateWindowsInfo2:
    """
    
            Main input structure that defines Item or ItemRevision of the top line
            in the BOMWindow. In the input, either revRuleConfigInfo object and objectsForConfigure
            object(variant rules or saved option set) or configContext object is required.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the objects created."""
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """Item object reference."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference."""
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """PSBOMView object reference"""
    RevRuleConfigInfo: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.RevisionRuleConfigInfo
    """Structure with information about RevisionRuleConfigInfo"""
    ObjectsForConfigure: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of variant rules or single stored option set object to set on this window"""
    ActiveAssemblyArrangement: Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement
    """Active assembly arrangement of this BOMWindow"""
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """ConfigurationContext object reference."""
    BomWinPropFlagMap: System.Collections.Hashtable
    """
            Mapping for window property and respective value that needs to be set on window.
            User need to populate this map with following property string values as key and true
            or false as value, which will be set or unset on the window
            

            Valid property values are
            

    show_unconfigured_variants
            
                show_unconfigured_changes
            
                show_suppressed_occurrences
            
                is_packed_by_default
            
                show_out_of_context_lines
            
                fnd0show_uncnf_occ_eff
            
                fnd0bw_in_cv_cfg_to_load_md

"""

class MoveInfo:
    """
    
            This structure represents the information for moving a single occurrence from its
            current parent assembly to its target parent assembly in the context of a higher
            level assembly.
            
    """
    def __init__(self, ) -> None: ...
    CommonParent: Teamcenter.Soa.Client.Model.ModelObject
    """
            The item revision of the common parent assembly where this move is occurring. Only
            ItemRevision type is supported for now.
            """
    SourceAssembly: Teamcenter.Soa.Client.Model.ModelObject
    """The item revision of the source assembly from where the occurrence is being moved."""
    OccThreadPathToBeMoved: list[str]
    """
            The occurrence thread path of the BOM line to be moved. The occurrence thread path
            is in a bottom up list. The first entry in the list should be occurrence to be moved
            and the last entry should be the occurrence thread for the common parent.
            """
    OccThreadPathTargetParent: list[OccThreadEquivalent]
    """
            The occurrence thread path of the target parent. The thread path is a bottom up list.
            The first entry in the list is the target parent assembly and the last entry in the
            list the common parent for the move.
            """

class OccThreadEquivalent:
    """
    
            This structure identifies the child occurrence in the parent assembly. This structure
            can identify an child occurrence that are already existing in Teamcenter as well
            as the child occurrences that are not yet created in Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """The item revision of the parent assembly. Only item revisions are allowed."""
    IdType: str
    """
            Type of child identifier. The legal values are: OccurrenceThread,
            CadOccId, ClientId.
            """
    Id: str
    """
            The identifier for the occurrence as specified by the idType
            member. The types of identifiers that can be used are the occurrence thread path,
            CAD occurrence Id and client Id. In cases where an occurrence with the specified
            identifier value does not exist in Teamcenter, the corresponding occurrence will
            be created.
            """
    IsNew: bool
    """flag to indicate if this occurrence is new in the parent assembly."""

class RelOccInfo:
    """
    
            This structure contains the list of attributes information, a flag to specify if
            the quantity is to be set as required, occurrence transform and occurrence notes
            information for the occurrence.
            
            The MoveInfo structure contains details on
            the moving an occurrence from its current parent to a new target parent.
            
    """
    def __init__(self, ) -> None: ...
    AttrsToSet: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.AttributesInfo]
    """
            Name and value pairs for the attribute information to set or update on the occurrence
            specified in the form of BOM line property names. For example, the BOM line occurrence
            name property could be specified with the attrsToSet name as bl_occurrence_name and
            the value as the occurrence name.
            """
    AsRequired: bool
    """Flag to specify that the quantity is as required. The default value is FALSE."""
    OccTransform: list[float]
    """
            Positioning information for the occurrence. This needs to be ordered in the standard
            matrix format.
            """
    OccNotes: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.OccNote]
    """Note information for the occurrence."""
    MoveInfo: MoveInfo
    """
            Optional data specifying the occurrence to be moved and the parent to which to be
            moved to.
            """

class RelativeStructureChildInfo3:
    """
    This structure contains information for the child node of a relative structure
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure. If clientId is not provided
            then it can be difficult to align the input with the output or any returned errors.
            """
    ChildBomViewTypeName: str
    """
            The name of the BOM view type of the child to be added to the parent BOMViewRevision.
            If not specified, the bomViewTypeName specified
            in the input preference  CreateOrUpdateRelativeStructurePref
            will be used as the default. For example, this can be used in a mult-CAD usage, where
            a JTView of a child originally created in a different CAD system needs to
            be added to a parent in NX, where the default view type is view.
            """
    CadOccId: str
    """
            The CAD occurrence ID or PSOccurrenceThread UID is used to uniquely identify
            the occurrence under a particular context item revision or General Design Element
            (GDE) for update. The cadOccId can be null
            for create. A valid cadOccId must be passed when this operation is called with the
            RelativeStructureParentInfo complete input set to true. If a valid cadOccId
            is not supplied when complete is set to true,
            this operation creates a new occurrence and any data associated against an existing
            occurrence is removed/lost. This parameter depends on the CreateOrUpdateRelativeStructurePref
cadOccIdAttrName preference for finding the
            existing BOM line
            """
    Child: Teamcenter.Soa.Client.Model.ModelObject
    """
            The child object for the occurrence creation. Only ItemRevision and GeneralDesignElement
            (GDE) are supported. If the child occurrence exists, but the input child object is
            different than the existing child object, the existing child will be replaced by
            the input child. Existing children are found referencing the occurrence found by
            the cadOccId input
            """
    OccInfo: RelOccInfo
    """
            The property information to set or updated for this occurrence. The optional moveInfo structure specifies if this occurrence
            is being moved to a new parent assembly.
            """

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AskChildPathBOMLines2(self, Input: list[Teamcenter.Services.Strong.Cad._2008_03.StructureManagement.AskChildPathBOMLinesInfo]) -> AskChildPathBOMLinesResponse2:
        """    
             This operation returns the BOMLine objects corresponding to input sets of
             child paths.
             

             The child path is defined by an ordered set of PSOccurrenceThread UIDs, starting
             from the top level assembly to a child node. The child node can be an immediate child
             or can be multi-level deep.
             

             This operation will return the BOMLine for each input child path. If a particular
             child path no longer exists in the Teamcenter product structure, there will be no
             entry for that input child path in the output AskChildPathClientIdToBOMLineMap.
             

             This operation works on existing BOM windows. The BOM window must have been created
             prior to using this operation.
             

Use Cases:

             If the client has a previously saved list of PSOccurrenceThread paths of a
             product structure, a new BOM window for the top level Item can be created and all
             the BOM line objects corresponding to the leaf node of the PSOccurrenceThread
             paths can be queried through this operation.
             

Dependencies:

             createBOMWindows
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         Specifies sets of product structure information each containing parent <b>BOMLine</b>
                         object, based on a BOM window opened by the client and one or more child paths specified
                         as an ordered set of <b>PSOccurrenceThread</b> UIDs. BOM configuration is managed
                         by the BOM window. Input client IDs must be unique for all input. The output <b>BOMLine</b>
                         objects are mapped to the input client IDs and the input child path UID.
             
        :return: 
        """
        ...
    def CreateOrUpdateRelativeStructure(self, Inputs: list[CreateOrUpdateRelativeStructureInfo4], Pref: Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructurePref) -> Teamcenter.Services.Strong.Cad._2009_04.StructureManagement.CreateOrUpdateRelativeStructureResponse:
        """    
             This operation creates or updates the relative structure for the input parent assembly
             and child components.  The objects created or updated by this operation include a
             BOM view (BV), BOM view revision (BVR) and occurrence data (PSOccurrence,
             PSOccurrenceThread).
             

             Before creating the relative structure objects and relations, this operation will
             check that the structure to be created does not already exist.  If the occurrence
             exists but the input attribute values differ from those already set, an attempt is
             made to update the values.
             

             This operation assumes the input is in a bottom up format such that if any failures
             occur, the structure that is created will still be consumable.  For example:
             

             Parent assembly A, subassembly B and child C are input into this operation.  If the
             relative structure for subassembly B and child C is created successfully but an error
             occurs during the creation of the structure for assembly A and subassembly B, the
             client can still access the subassembly B, child C relative structure.
             

             No attempt is made in the operation to rearrange the input and process it in the
             correct order. One parent context object is processed at one time and it is assumed
             that all edits for a given parent context come in as one set of input.
             

             This operation can also perform structure move operations. The move operation is
             performed within the context of the lowest common parent. Along with moving the occurrence
             from one parent to a new parent, any absolute occurrence data present in the original
             occurrence will also be moved to the new occurrence. The input for the move operation
             is specified in the MoveInfo substructure
             of RelOccInfo. The MoveInfo
             data is specified in the context of the RelativeStructureChildInfo3.
             Each RelativeStructureChildInfo3 will allow
             specifying only moving of one instance only. In cases where there are multiple instances
             of the same occurrence, MoveInfo has to be
             specified for each instance. In such cases, each instance data will be specified
             in its own RelativeStructureChildInfo3 structure.
             However, the child object is specified only
             once per occurrence. For the other instances of the same occurrence, the child object in the RelativeStructureChildInfo3
             is specified as NULL.
             

             In the following example, to move Part_P1 (instance 1) to SubAssembly_B (instance
             1), create a new occurrence of Part_P1 under SubAssembly_B. After this add, SubAssembly_B
             (instance 1) will have a child  Part_P1 (instance 1) and SubAssembly_B (instance
             2) will have a child  Part_P1 (instance 2). Specify the move from the occurrence
             of Part_P1 (instance 1) under SubAssembly_C to the Part_P1 (instance 1) under SubAssembly_B
             (instance 1).  And similarly for the instance 2.
             

             Move Example:
             
             Assembly_A
             
             |
             
             |-->SubAssembly_B  (instance 1)
             
             |
             
             |-->SubAssembly_B  (instance 2)
             
             |
             
             |-->SubAssembly_C
             
             |       |
             
             |       |-->Part_P1    (instance 1)
             
             |
             
             |-->SubAssembly_C
             
             |       |
             
             |       |-->Part_P1    (instance 2)
             


             To move "Part_P1" from SubAssembly_C to Sub_Assembly_B:
             
relStrInfo4s[0] = new CreateOrUpdateRelativeStructureInfo4();
             
relStrInfo4s[0].parentInfo = new
             RelativeStructureParentInfo();
             
relStrInfo4s[0].parentInfo.parent
             = SubAssembly_B_ItemRev;
             
relStrInfo4s[0].childInfo = new
             RelativeStructureChildInfo3[1];
             

relStrInfo4s[0].childInfo[0] = new RelativeStructureChildInfo3();
             
relStrInfo4s[0].childInfo[0].clientId = "Add_Part_P1_to_SubAssembly_B";
             
relStrInfo4s[0].childInfo[0].child = Part_P1;
             
relStrInfo4s[0].childInfo[0].occInfo = new
             RelOccInfo();
             
relStrInfo4s[0].childInfo[0].occInfo.moveInfo
             = new MoveInfo();
             
relStrInfo4s[0].childInfo[0].occInfo.moveInfo.commonParent = Assembly_A_ItemRev;
             
relStrInfo4s[0].childInfo[0].occInfo.moveInfo.sourceAssembly = SubAssembly_C_ItemRev;
             
relStrInfo4s[0].childInfo[0].occInfo.moveInfo.occThreadPathToBeMoved = occThreadPathToBeMoved;
             
relStrInfo4s[0].childInfo[0].occInfo.moveInfo.occThreadPathTargetParent = targetParentOccThr;


             relStrInfo4s[0].childInfo[1] = new RelativeStructureChildInfo3();
             
             relStrInfo4s[0].childInfo[1].clientId = "Add_Part_P1_instance_2_to_SubAssembly_B";
             
             relStrInfo4s[0].childInfo[1].child = NULL;   // For the second instance, set child
             to NULL
             
             relStrInfo4s[0].childInfo[1].occInfo = new RelOccInfo();
             
             relStrInfo4s[0].childInfo[1].occInfo.moveInfo = new MoveInfo();
             
             relStrInfo4s[0].childInfo[1].occInfo.moveInfo.commonParent = Assembly_A_ItemRev;
             
             relStrInfo4s[0].childInfo[1].occInfo.moveInfo.sourceAssembly = SubAssembly_C_ItemRev;
             
             relStrInfo4s[0].childInfo[1].occInfo.moveInfo.occThreadPathToBeMoved = occThreadPathToBeMoved;
             
             relStrInfo4s[0].childInfo[1].occInfo.moveInfo.occThreadPathTargetParent = targetParentOccThr;
             


Use Cases:

             Use Case 1:
             

             User adds an existing component to an existing assembly to create a relative occurrence.
             
             For this operation, the assembly is passed in as the parent and the component is
             passed in as the child. The relative occurrence is created and a map of the input
             clientID to MappedReturnData
             is returned in output and the occurrence, BOM view and BOM view revision are returned
             as created objects in ServiceData.
             

             Use Case 2:
             

             User wants to update the position of the child component relative to the parent assembly.
             
             For this operation, the transform on the child occurrence information is updated
             with the new position relative to the parent. The assembly is passed in as the parent
             and the component is passed in as the child. The relative occurrence is updated and
             a map of the clientID to MappedReturnData is returned in output
             and the occurrence and BOM view revision are returned as updated objects in ServiceData.
             

Dependencies:

             createOrUpdateParts, createObjects
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Inputs: 
                         List of input structures that defines all the occurrence for a given parent.
             
        :param Pref: 
                         Preference structure specific for this service.
             
        :return: 215034 (error): The dataset or BVR was modified even when the input last modified
             dates was different than the current last modified data.
        """
        ...
    def CreateBOMWindows2(self, Info: list[CreateWindowsInfo2]) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateBOMWindowsResponse:
        """    
             Creates a list of window and sets the respective input ItemRevision as the
             top line. This operation can be used to set multiple saved variant rules or single
             stored option set to the window. For setting Product Configurator authored varaint
             rule on the window, value of preference PSM_enable_product_configurator must be true.It
             can be used to set certain window property, if sent as a part of input. It can be
             used to create the BOMLine for input to Expand Product Structure services.
             All BOMLines under this window are unpacked.  To use the Teamcenter default
             unitNo or use your input RevisionRule with no changes, you must set unitNo to -1
             in RevisionRuleEntryProps::unitNo.  If it is not specified, your input rule will
             function as a modified/transient revision rule with a unitNo of 0. All BOMLines
             under this window will be shown or hide depending upon the values set in map bomWinPropFlagMap.
             

Use Cases:

             This operation creates a list of window and sets the respective input Item revision
             as the top line. This operation can be used to set multiple saved variant rules or
             single stored option set to the window.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Info: 
                         list of objects containing window creation information
             
        :return: 
        """
        ...

