import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AbsOccAttachment:
    """
    
            Contains a dataset object reference with the JT override data and a relationTypeName
            to relate AbsOccData to Dataset.
            
    """
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Dataset object reference with the JT override data"""
    RelationTypeName: str
    """Relation/property to relate AbsOccData to Dataset"""

class AbsOccDataInfo:
    """
    
            Contains list of AttributesInfo for overrides to set, list of attribute names to
            unset/remove the overrides, a boolean flag, occTransform which contains the positioning
            information for the occurrence, list of note information for the occurrence, list
            of AbsOccAttachment for the attachments, list of the AbsOccAttachment to unattach,
            client id of the used arrangement for this absolute occurrence and a reference of
            used arrangement for this absolute occurrence.
            
    """
    def __init__(self, ) -> None: ...
    OverridesToSet: list[AttributesInfo]
    """List of AttributesInfo for overrides to set"""
    OverridesToRemove: list[str]
    """
            List of attribute names to unset/remove the overrides for on the occurrence, for
            example to remove a transform override, add the attribute name for the transform
            to this list.
            """
    AsRequired: bool
    """Used to the set the quantity as required occurrence flag"""
    OccTransform: list[float]
    """Positioning information for the occurrence"""
    OccNotes: list[OccNote]
    """List of note information for the occurrence"""
    Attachments: list[AbsOccAttachment]
    """List of AbsOccAttachment for the attachments"""
    AttachmentsToUnattach: list[AbsOccAttachment]
    """List of the AbsOccAttachment to unattach"""
    ClientIdOfUsedArrangement: str
    """
            Client id of the used arrangement for this absolute occurrence, if arrangement is
            yet to be created
            """
    UsedArr: Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement
    """
            Reference of used arrangement for this absolute occurrence if arrangement has already
            been created
            """

class AbsOccInfo:
    """
    Attribute information for the occurrence
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the object(s) created"""
    AbsOcc: Teamcenter.Soa.Client.Model.Strong.AbsOccurrence
    """AbsOccurrence object reference , may be null for create"""
    CadOccIdPath: list[str]
    """List of IDs of the cad occurrences"""
    AbsOccData: AbsOccDataInfo
    """Member of AbsOccDataInfo"""

class AssemblyArrangementInfo:
    """
    Structure with arrangement qualified override information for the occurrence.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    Arrangement: Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement
    """
            The assembly arrangement object reference.  This input can be null for create, but
            it is required for update.
            """
    Name: str
    """The name of the arrangement."""
    IsDefault: bool
    """
            Flag to specify whether arrangement is the
            default arrangement.
            """
    Description: str
    """The arrangement description."""
    ExternalUid: str
    """The UID required for create."""
    AbsOccInfo: list[AbsOccInfo]
    """List of absolute occurrence information for the BOM view revision qualified overrides."""

class AttributesInfo:
    """
    Name and value data to be set as attributes on the related object.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The attribute name."""
    Value: str
    """The value to set for the attribute."""

class CloseBOMWindowsResponse:
    """
    Contains a serviceData containing objects that were deleted.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information. For this service, ServiceData
            contains BOM window and top line.
            """

class RevisionRuleEntryProps:
    """
    This contains information about the RevisionRule Entry Properties.
    """
    def __init__(self, ) -> None: ...
    UnitNo: int
    """Refers to the unit number of RevisionRule object."""
    Date: System.DateTime
    """Refers to the date of RevisionRule object."""
    Today: bool
    """Refers to a flag to indicate that the date is today on RevisionRule object."""
    EndItem: Teamcenter.Soa.Client.Model.Strong.Item
    """Refers to Item and indicates end item for RevisionRule object."""
    EndItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Refers to ItemRevision and indicates end item revision for RevisionRule
            object.
            """
    OverrideFolders: list[OverrideInfo]
    """Refers to a list of OverrideInfo struct."""

class RevisionRuleConfigInfo:
    """
    This contains the RevisionRule object configuration information.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the object(s) created"""
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """The RevisionRule object used for configuration of this BOMWindow object."""
    Props: RevisionRuleEntryProps
    """Refers to RevisionRuleEntryProps struct object."""

class CreateBOMWindowsInfo:
    """
    
            main input structure that defines item or item revision of the top line in the BOM
            window
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the object(s) created"""
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """Item object reference for which BOM window needs to create"""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference"""
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """PSBOMView object reference"""
    RevRuleConfigInfo: RevisionRuleConfigInfo
    """Structure with information about the RevisionRuleConfigInfo"""
    ObjectForConfigure: Teamcenter.Soa.Client.Model.ModelObject
    """Tag for Variant rule or option set to use on this BOM window"""
    ActiveAssemblyArrangement: Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement
    """Active assembly arrangement of this BOM window"""

class CreateBOMWindowsOutput:
    """
    
            The output structure that contains the created BOMWindow object and top line BOMLine
            object representing the item or item revision.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the object(s) created"""
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """Object reference for the BOMWindow created"""
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Oject reference for the BOMLine created"""

class CreateBOMWindowsResponse:
    """
    
            Contains list of CreateBOMWindowsOutput which contains created BOMWindow object and
            top line BOMLine object representing the item or item revision along with the client
            id and a serviceData containing objects that were created/deleted.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateBOMWindowsOutput]
    """
            List of CreateBOMWindowsOutput which contains created BOMWindow object and top line
            BOMLine object representing the item or item revision along with the client id
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information. For this service, ServiceData
            contains BOM window and top line.
            """

class CreateOrUpdateAbsoluteStructureInfo:
    """
    
            Contains item revision object reference of the context assembly to create/validate
            the occurrence, list of AbsOccInfo for bvr qualified overrides and a list of AssemblyArrangementInfo
            for bvr/arrangement qualified overrides.
            
    """
    def __init__(self, ) -> None: ...
    ContextItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            ItemRevision object reference of the context assembly to create/validate the occurrence,
            required reference
            """
    BvrAbsOccInfo: list[AbsOccInfo]
    """List of AbsOccInfo for bvr qualified overrides"""
    ArrAbsOccInfo: list[AssemblyArrangementInfo]
    """List of AssemblyArrangementInfo for bvr/arrangement qualified overrides, may be null"""

class CreateOrUpdateAbsoluteStructurePref:
    """
    
            Contain cadOccIdAttrName which identifies the BOMLine attribute that is used to identify
            relative occurrences to update.
            
    """
    def __init__(self, ) -> None: ...
    CadOccIdAttrName: str
    """
            Identifies the BOMLine attribute that is used to identify relative occurrences to
            update.
            """

class CreateOrUpdateAbsoluteStructureResponse:
    """
    Contains response for createOrUpdateAbsoluteStructure operation.
    """
    def __init__(self, ) -> None: ...
    AbsOccOutput: System.Collections.Hashtable
    """
            Map of input clientId for the absolute occurrence to created/updated/found absolute
            occurrence
            """
    AsmArrOutput: System.Collections.Hashtable
    """Map of input client id to created/updated/found AssemblyArrangement"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData contains any other created (AbsOccData, AbsOccDataQualifier), updated
            (like BVR), relevant related, or deleted objects from this operation.
            """

class CreateOrUpdateRelativeStructureInfo:
    """
    
            Contains a parent ItemRevision object, list of type RelativeStructureChildInfo and
            a boolean value for whether the BVR should be set to precise.
            
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            ItemRevision object reference for which the context assembly is created or updated,
            required reference
            """
    ChildInfo: list[RelativeStructureChildInfo]
    """List of type RelativeStructureChildInfo"""
    Precise: bool
    """Flag for updating the BVR to precise(true)/imprecise(false)"""

class CreateOrUpdateRelativeStructurePref:
    """
    Contains cadOccIdAttrName and a list of item types.
    """
    def __init__(self, ) -> None: ...
    CadOccIdAttrName: str
    """
            String representing the occurrence note type which holds the value for the CAD occurrence
            id or PSOccurrenceThread uid
            """
    ItemTypes: list[str]
    """
            List of item types that the client is interested in, such that if the overall structure
            in Teamcenter contains structure relating to other item types or subtypes not in
            this list, that structure will not be deleted if this operation is complete.
            """

class CreateOrUpdateRelativeStructureResponse:
    """
    The response for createOrUpdateRelativeStructure operation.
    """
    def __init__(self, ) -> None: ...
    Output: System.Collections.Hashtable
    """Member of type ClientIdToPSOccurrenceThreadMap"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Mwmber of type Teamcenter::Soa::Server::ServiceData serviceData"""

class DeleteAssemblyArrangementsInfo:
    """
    Contains ItemRevision object reference and list of AssemblyArrangement.
    """
    def __init__(self, ) -> None: ...
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference"""
    Arrangements: list[Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement]
    """List of AssemblyArrangement object references to be deleted"""

class DeleteAssemblyArrangementsResponse:
    """
    
            The response for the deleteAssemblyArrangements
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData.  This operation will populate
            the ServiceData with deleted assembly arrangements.
            Assembly arrangement UIDs will be returned as deleted objects.
            """

class DeleteRelativeStructureInfo:
    """
    Contains parent item revision and list of child information structures.
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            ItemRevision object reference for the context assembly from which children are to
            be removed
            """
    ChildInfo: list[str]
    """
            List of identifiers of the relative occurrences to be deleted. This is the CAD occurrence
            id or PSOccurrenceThread uid to uniquely identify the occurrence under a particular
            context Item Revision
            """

class DeleteRelativeStructurePref:
    """
    Contains cadOccIdAttrName.
    """
    def __init__(self, ) -> None: ...
    CadOccIdAttrName: str
    """BOMLine attribute name that contains the CAD occurrence identifier."""

class DeleteRelativeStructureResponse:
    """
    
            The response for deleteRelativeStructure
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData.  This operation will populate
            the ServiceData with updated context BVR
            objects and the deleted relative occurrences. CAD occurrence IDs or PSOccurrenceThread
            UIDs will be returned as deleted objects.
            """

class ExpandPSAllLevelsInfo:
    """
    Contains parent BOMLines to expand and an exclude filter to specify children to exclude.
    """
    def __init__(self, ) -> None: ...
    ParentBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of parent bom lines that needs to be expanded"""
    ExcludeFilter: str
    """
            Filter to exclude the type of BOMLines. Valid values are: None -- Returns all information
            about the structure. ExcludeOverridden -- Excludes structure or property values that
            are removed by AbsOccs subsititution. ExcludeICHistory -- Excludes structure (or
            property values) that are configured out by ICs. ExcludeGDEs -- Excludes lines that
            are GDEOccurrences. ExcludeNonImanItemLines -- Excludes any lines that are not ImanItemLines.
            """

class ExpandPSParentData:
    """
    
            Through this structure, the parent bom line , the item revision of the bom line and
            the datasets attached to the bom line item revision are returned.
            
    """
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMline object reference of the parent"""
    ItemRevOfBOMLine: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference of parent"""
    ParentDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """List of Dataset object references attached to parent"""

class ExpandPSAllLevelsOutput:
    """
    
            Contains ExpandPSParentData corresponding to the parent and a list of ExpandPSData
            of the children
            
    """
    def __init__(self, ) -> None: ...
    Parent: ExpandPSParentData
    """ExpandPSParentData member"""
    Children: list[ExpandPSData]
    """List of ExpandPSData children found for this parent."""

class ExpandPSAllLevelsPref:
    """
    
            More than one filtering criteria can be specified using this which is nothing but
            a list of  RelationAndTypesFilter
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """Flag to check for expanding the item revision further"""
    Info: list[RelationAndTypesFilter]
    """
            List of the relation name and the types of objects of the given relation to return
            along with the children
            """

class ExpandPSAllLevelsResponse:
    """
    A list of ExpandPSAllLevelsOutput so that a set of parent bom lines can be expanded.
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandPSAllLevelsOutput]
    """List of ExpandPSAllLevelsOutput which contains ExpandPSParentData and list of ExpandPSData"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information. For this service, all objects
            are returned to the plain objects group. Error information will also be returned.
            """

class ExpandPSData:
    """
    
            Through this structure, the child bom line , the item revision of the bom line and
            the datasets attached to the bom line item  revision are returned.
            
    """
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMline object reference of the children"""
    ItemRevOfBOMLine: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference of children"""
    Datasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """List of Dataset object references attached to children"""

class ExpandPSOneLevelInfo:
    """
    Contains parent BOMLines to expand and an exclude filter to specify children to exclude.
    """
    def __init__(self, ) -> None: ...
    ParentBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of parent bom lines that needs to be expanded"""
    ExcludeFilter: str
    """
            Filter to exclude the type of BOMLines. Valid values are: None -- Returns all information
            about the structure. ExcludeOverridden -- Excludes structure or property values that
            are removed by AbsOccs subsititution. ExcludeICHistory -- Excludes structure that
            are configured out by ICs. ExcludeGDEs -- Excludes lines that are GDEOccurrences.
            ExcludeNonImanItemLines -- Excludes any lines that are not ImanItemLines.
            """

class ExpandPSOneLevelOutput:
    """
    
            Structure containing ExpandPSParentData corresponding to the parent and a list of
            ExpandPSData of the children
            
    """
    def __init__(self, ) -> None: ...
    Parent: ExpandPSParentData
    """ExpandPSParentData member"""
    Children: list[ExpandPSData]
    """List of ExpandPSData children found for this parent."""

class ExpandPSOneLevelPref:
    """
    
            More than one filtering criteria can be specified using this which is nothing but
            a list of  RelationAndTypesFilter
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """Flag to check for expanding the item revision further"""
    Info: list[RelationAndTypesFilter]
    """
            List of RelationAndTypesFilters that contain the relation names and the types of
            objects of the given relation.
            """

class ExpandPSOneLevelResponse:
    """
    A ExpandPSOneLevelResponse containing the return for this operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandPSOneLevelOutput]
    """List of ExpandPSOneLevelOutput which contains ExpandPSParentData and list of ExpandPSData"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information. For this service, all objects
            are returned to the plain objects group. Error information will also be returned.
            """

class GetRevisionRulesResponse:
    """
    Contains the response for getRevisionRules operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[RevisionRuleInfo]
    """
            List of RevisionRuleInfo which contains Revision rule, configure attribute status
            along with override information
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error
            """

class GetVariantRulesResponse:
    """
    Contains the response for getVariantRules operation.
    """
    def __init__(self, ) -> None: ...
    InputItemRevToVarRules: System.Collections.Hashtable
    """Holds map of itemRevision to list of VariantRules."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData"""

class OccNote:
    """
    Contains note type and note text information for the occurrence note.
    """
    def __init__(self, ) -> None: ...
    NoteType: str
    """The type of the occurrence note to set."""
    NoteText: str
    """The text for the occurrence note."""

class OverrideInfo:
    """
    This contains information about the override RevisionRule Entry.
    """
    def __init__(self, ) -> None: ...
    RuleEntry: Teamcenter.Soa.Client.Model.Strong.CFMOverrideEntry
    """Refers to the CFMOverrideEntry of RevisionRule object."""
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """Refers to the Folder of override rule entry of RevisionRule object."""

class RelationAndTypesFilter:
    """
    
            This consists of a string which indicates the relation name and a list of strings
            which indicate the object types. An object that falls under these input criteria
            is returned along with the children.
            
    """
    def __init__(self, ) -> None: ...
    RelationName: str
    """Relation name"""
    RelationTypeNames: list[str]
    """List of the relation name types"""

class RelOccInfo:
    """
    Contains information about the relative occurrence.
    """
    def __init__(self, ) -> None: ...
    AttrsToSet: list[AttributesInfo]
    """
            Name and value pairs for the attribute information to set or update on the occurrence
            specified in the form of BOM line property names.  For example, the BOM line occurrence
            name property could be specified with the attrsToSet
name as bl_occurrence_name and the
            value as the occurrence name.
            """
    AsRequired: bool
    """Flag to specify that the quantity is as required.  The default is FALSE."""
    OccTransform: list[float]
    """
            Positioning information for the occurrence.  This needs to be ordered in the standard
            matrix format.
            """
    OccNotes: list[OccNote]
    """Note information for the occurrence."""

class RelativeStructureChildInfo:
    """
    Contains clientId, cadOccId, an item revision and occurrence information structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client track the object(s) created"""
    CadOccId: str
    """
            This is the CAD occurrence id or PSOccurrenceThread uid to uniquely identify the
            occurrence under a particular context Item Revision, can be null for create. A valid
            cadOccId must be passed when the calling the service with complete = true. If a valid
            cadOccId is not supplied when complete = true, the service creates new occurrences
            and any data associated against the old occurrence is lost.
            """
    Child: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Item Revision for the PSOccurrence creation, required reference, if the precise flag
            is false, then the Item will be obtained from the Item Revision and used
            """
    OccInfo: RelOccInfo
    """Member of type RelOccInfo."""

class RevisionRuleInfo:
    """
    
            Contains the revisionRule object reference, a map of string attribute to boolean
            flag to indicate the configurable and a list of override information.
            
    """
    def __init__(self, ) -> None: ...
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """RevisionRule object reference"""
    HasValueStatus: System.Collections.Hashtable
    """
            A map of string attribute to boolean flag to indicate the configurable attribute
            has values on it and information about override folder.
            """
    OverrideFolders: list[OverrideInfo]
    """List of override information"""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateBOMWindows(self, Info: list[CreateBOMWindowsInfo]) -> CreateBOMWindowsResponse:
        """    
             Creates a BOMWindow and sets the input Item Revision as the top line.  Can be used
             to create the BOMLine for input to Expand Product Structure services.  All BOMLines
             under this window are unpacked.  To use the Teamcenter default unitNo or use your
             input RevisionRule with no changes, you must set unitNo to -1 in RevisionRuleEntryProps::unitNo.
             If it is not specified, your input rule will function as a modified/transient revision
             rule with a unitNo of 0.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         Input is an item or item Revision object
             
        :return: Output is the created BOMWindow object and top line BOMLine object representing the
             item or item revision
        """
        ...
    def CreateOrUpdateAbsoluteStructure(self, Info: list[CreateOrUpdateAbsoluteStructureInfo], BomViewTypeName: str, Complete: bool, Pref: CreateOrUpdateAbsoluteStructurePref) -> CreateOrUpdateAbsoluteStructureResponse:
        """    
             CreateOrUpdateAbsoluteStucture allows the user to find or create the absolute structure
             network of objects and relations for the input model. The service first attempts
             to check for the presence of duplicate context objects and then validate the existence
             of the structure to be created. If any of the objects exist and the input attribute
             values differ from those already set, an attempt is made to update the values. Note:
             The following AbsOccData attributes are not supported for arrangement qualified overrides.
             These attributes can only be overridden at the bvr level (which applies to all arrangements).
             If these attributes are overridden in the AssemblyArrangementInfo, they will be ignored.
             1.child item 2.GDE object 3.instance number 4.occurrence name 5.note 6.occurrence
             type 7.Variant instance As we process one contextItemRev object at one time, it is
             assumed that all edits for a given contextItemRev come in as one set of input.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         List of input structures that defines all the occurrence for a given parent
             
        :param BomViewTypeName: 
                         Type of BOMView
             
        :param Complete: 
                         Flag that if true signifies that the structure represented in the input is the full
                         representation of the structure under the input parent. Any other structure relations
                         that exist in Teamcenter but are not represented here will be removed. Upper and
                         lower qualified (including arrangements) absolute occurrence overrides will not be
                         implicitly deleted or removed.  Please use the deleteAssemblyArrangements operation.
             
        :param Pref: 
                         preference structure specific for this service
             
        :return: Output is an explicit response consisting of a map of input clientId for the absolute
             occurrence to created/updated/ found absolute occurrence and map of input client
             id to created/updated/found AssemblyArrangement.
        """
        ...
    def CreateOrUpdateRelativeStructure(self, Inputs: list[CreateOrUpdateRelativeStructureInfo], BomViewTypeName: str, Complete: bool, Pref: CreateOrUpdateRelativeStructurePref) -> CreateOrUpdateRelativeStructureResponse:
        """    
             Create or update the relative structure objects and relations for the input model.
             The service first attempts to check for the presence of duplicate context objects
             and then validate the existence of the structure to be created. If any of the objects
             exist but the input attribute values that differ from those already set, an attempt
             is made to update the values if possible. This service assumes the input is in a
             bottom-up format such that if any failures occur, the structure that is created will
             be consistent. No attempt is made in the service to rearrange the input and process
             it in the correct order. As we process one parent context object at one time, it
             is assumed that all edits for a given parent context come in as one set of input.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Inputs: 
                         List of input structures that defines all the occurrence for a given parent
             
        :param BomViewTypeName: 
                         Type of BOMView to create
             
        :param Complete: 
                         Flag that if true signifies that the structure represented in the input is the full
                         representation of the structure under the input parent.  Any other structure relations
                         that exist in Teamcenter but are not represented here will be removed.
             
        :param Pref: 
                         Preference structure specific for this service
             
        :return: Output is an explicit response consisting of a map of input clientId string to created/updated/found
             occurrence thread reference.
        """
        ...
    def DeleteAssemblyArrangements(self, Info: list[DeleteAssemblyArrangementsInfo], BomViewTypeName: str) -> DeleteAssemblyArrangementsResponse:
        """    
             Deletes assembly arrangements and all the absolute occurrence data associated with
             the assembly arrangements, it also delete the relation between assembly arrangements
             and bvr.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         Input is bvr and list of assembly arrangements to delete
             
        :param BomViewTypeName: 
                         The BOM view type name
             
        :return: the uids of the deleted assembly arrangements.
        """
        ...
    def DeleteRelativeStructure(self, Inputs: list[DeleteRelativeStructureInfo], BomViewTypeName: str, Pref: DeleteRelativeStructurePref) -> DeleteRelativeStructureResponse:
        """    
             Deletes one or more first level children of a parent assembly.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Inputs: 
                         List input of structures that defines the parent and first level children to be deleted.
             
        :param BomViewTypeName: 
                         Qualifies the specified parent item revision(s) to identify a unique BOM view revision.
             
        :param Pref: 
                         Preference structure specific for this service
             
        :return: The ServiceData contains the UIDs of any deleted occurrences
        """
        ...
    def ExpandPSAllLevels(self, Input: ExpandPSAllLevelsInfo, Pref: ExpandPSAllLevelsPref) -> ExpandPSAllLevelsResponse:
        """    
             Finds the chilren at all levels given parent bomlines. Also if required gets the
             objects of given type and relation that are attached to the parent and children
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         of  ExpandPSAllLevelsInfo which contains parent bom lines and a filter of the type
                         of bom lines to exclude.
             
        :param Pref: 
                         of a ExpandPSAllLevelsPref which contains a list of relation name and the types of
                         objects of the given relation to return along with the children.
             
        :return: list of ExpandPSData which contains parent bomlines, chilrens and datasets of given
             type and relation attached to them. All Object ids that were successfully found are
             added to ServiceData. Objects/object ids that failed the find are returned in a list
             of failures in the ServiceData
        """
        ...
    def ExpandPSOneLevel(self, Input: ExpandPSOneLevelInfo, Pref: ExpandPSOneLevelPref) -> ExpandPSOneLevelResponse:
        """    
             Finds the first level chilren of given parent bomlines. Also if required gets the
             objects of given type and relation that are attached to the parent and children
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         of  ExpandPSOneLevelInfo which contains parent bom lines and a filter of the type
                         of bom lines to exclude.
             
        :param Pref: 
                         of a ExpandPSOneLevelPref which contains a list of relation name and the types of
                         objects of the given relation to return along with the children.
             
        :return: list of ExpandPSData which contains parent bomlines, chilrens and datasets of given
             type and relation attached to them. All Object ids that were successfully found are
             added to ServiceData.  Objects/object ids that failed the find are returned in a
             list of failures in the ServiceData
        """
        ...
    def GetRevisionRules(self) -> GetRevisionRulesResponse:
        """    
             The GetRevisionRules service gets all the persistent revision rules in the database.
             It along with the revision rules returns its runtime configuration properties status
             of being fixed or not.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :return: 
        """
        ...
    def CloseBOMWindows(self, BomWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> CloseBOMWindowsResponse:
        """    
             Closes a BOMWindow.  Must be used to close the BOMWindow created during Create BOM
             Window after calls to Expand Product Structure services are complete.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param BomWindows: 
                         The BOMWindow to close
             
        :return: the uids of the BOMWindow.
        """
        ...
    def GetVariantRules(self, ItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> GetVariantRulesResponse:
        """    
             The GetVariantRules service gets all the variant rules in the database for the given
             Item Revision. To get Product Configurator authored variant rules, value of preference
             PSM_default_configurator_context must be true.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param ItemRevs: 
                         List of object references of ItemRevisions to get variant rules for
             
        :return: GetVariantRulesResponse which contains a map of input Item Revision to list of to
             list of Variant Rule objects for that Item Revision
        """
        ...

