import System
import Teamcenter.Services.Strong.Cad._2007_01.StructureManagement
import Teamcenter.Services.Strong.Cad._2007_06.StructureManagement
import Teamcenter.Services.Strong.Cad._2007_09.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BomLineVariantCondition:
    """
    This contains the variant condition information for a given BOMLine object.
    """
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Refers to BOMLine object on which variant condition are defined."""
    ConditionClauses: list[Teamcenter.Services.Strong.Cad._2007_09.StructureManagement.VariantCondInfo]
    """
            Refers to a list of VariantCondInfo struct objects which has classic variant
            condition information.
            """

class ClassicOptionData:
    """
    Contains the option information for a single item revision.
    """
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """itemRevision"""
    OptionData: list[Teamcenter.Services.Strong.Cad._2007_06.StructureManagement.ClassicOptionInfo]
    """optionData"""

class ClassicOptionsResponse:
    """
    Contains the option information for a set of ItemRevision objects.
    """
    def __init__(self, ) -> None: ...
    ItemRevisionOptionData: list[ClassicOptionData]
    """
            Refers to a list of ClassicOptionData struct,
            which has ItemRevision and corresponding classic variant option list.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the service operation, plain objects, and error information.
            """

class CreateOrUpdateAbsoluteStructureInfo2:
    """
    
            Contains Last Modified Date of BVR, contextItemRev, List of AbsOccInfo for bvr qualified
            overrides and a list of AssemblyArrangementInfo for bvr/arrangement qualified overrides.
            
    """
    def __init__(self, ) -> None: ...
    LastModifiedOfBVR: System.DateTime
    """Last Modified Date of BVR"""
    ContextItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            ItemRevision object reference of the context assembly to create/validate the occurrence,
            required reference
            """
    BvrAbsOccInfo: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.AbsOccInfo]
    """List of AbsOccInfo for bvr qualified overrides"""
    ArrAbsOccInfo: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.AssemblyArrangementInfo]
    """List of AssemblyArrangementInfo for bvr/arrangement qualified overrides, may be null"""

class CreateOrUpdateAbsoluteStructurePref2:
    """
    
            Contains a flag to check whether BVR needs to be modified, if input last modified
            date is different from actual and a cadOccIdAttrName which identifies the BOMLine
            attribute that is used to identify relative occurrences to update.
            
    """
    def __init__(self, ) -> None: ...
    OverwriteForLastModDate: bool
    """
            Flag to check whether BVR needs to be modified, if input last modified date is different
            from actual.
            """
    CadOccIdAttrName: str
    """
            Identifies the BOMLine attribute that is used to identify relative occurrences to
            update.
            """

class CreateOrUpdateRelativeStructureInfo2:
    """
    
            Contains lastModifiedOfBVR, a parent ItemRevision object, list of type RelativeStructureChildInfo
            and a  boolean value to convey precision of the BVR.
            
    """
    def __init__(self, ) -> None: ...
    LastModifiedOfBVR: System.DateTime
    """Last Modified Date of BVR"""
    Parent: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            ItemRevision object reference for which the context assembly is created or updated,
            required reference
            """
    ChildInfo: list[Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.RelativeStructureChildInfo]
    """List of type RelativeStructureChildInfo"""
    Precise: bool
    """Flag for updating the BVR to precise(true)/imprecise(false)"""

class CreateOrUpdateRelativeStructurePref2:
    """
    Contains overwriteForLastModDate, cadOccIdAttrName and a list of item types.
    """
    def __init__(self, ) -> None: ...
    OverwriteForLastModDate: bool
    """
            Flag to check whether BVR needs to be modified, if input last modified date is different
            from actual.
            """
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

class DeleteAssemblyArrangementsInfo2:
    """
    Information to delete assembly arrangements.
    """
    def __init__(self, ) -> None: ...
    LastModifiedOfBVR: System.DateTime
    """
            Last modified date of BOM view revision object under the input itemRev.  This input is not required.  If this input date is different
            than the current last modified date and the overwriteForLastModDate
            preference is false the input will be ignored and processing will continue with the
            next input.  In this scenario, error 215033 will be returned.  If the dates are different
            and the overwriteForLastModDate preference
            is true, processing will continue with the current input, the BVR will be modified
            and the arrangements deleted.  In this scenario, error 215034 will be returned.
            """
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Object reference of the item revision context assembly from which the assembly arrangements
            are to be removed.  This is a required input.  An error will be returned if a valid
            itemRev is not specified.
            """
    Arrangements: list[Teamcenter.Soa.Client.Model.Strong.AssemblyArrangement]
    """List of assembly arrangement object references to be deleted."""

class DeleteAssemblyArrangementsPref:
    """
    Preference structure for deleteAssemblyArrangements.
    """
    def __init__(self, ) -> None: ...
    OverwriteForLastModDate: bool
    """
            Flag to check whether the structure needs to be updated if the input last modified
            date is different from the current last modified date of the object in Teamcenter.
            If false, but the DeleteAssemblyArrangementsInfo2
lastModifiedOfBVR input specified is different
            than the set modified date, partial error 215033 will be returned.
            """

class DeleteRelativeStructureInfo2:
    """
    Contains lastModifiedOfBVR, parent itemRevision and childInfo.
    """
    def __init__(self, ) -> None: ...
    LastModifiedOfBVR: System.DateTime
    """Last Modified Date of BVR"""
    Parent: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            ItemRevision object reference for the context assembly from which children are to
            be removed
            """
    ChildInfo: list[str]
    """
            List of identifiers of the relative occurrences to be deleted. This is the CAD occurrence
            id or PSOccurrenceThread uid to uniquely identify the occurrence under a particular
            context Item Revision.
            """

class DeleteRelativeStructurePref2:
    """
    Preference structure for deleteRelativeStructure.
    """
    def __init__(self, ) -> None: ...
    OverwriteForLastModDate: bool
    """
            Flag to check whether the structure needs to be updated if the input last modified
            date is different from the current last modified date of the object in Teamcenter.
            If false, but the DeleteRelativeStructureInfo3
lastModifiedOfBVR input specified is different
            than the set modified date, partial error 215033 will be returned.
            """
    CadOccIdAttrName: str
    """The BOMLine attribute that contains the CAD occurrence identifier."""

class VariantConditionResponse:
    """
    This contains the variant condition information for a set of BOMLine objects.
    """
    def __init__(self, ) -> None: ...
    VariantConditions: list[BomLineVariantCondition]
    """
            Refers to a list of BomLineVariantCondition
            struct objects, contains the variant condition on BOMLine object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The SOA framework object containing objects that were created, deleted, or updated
            by the Service, plain objects, and error information.
            """

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateAbsoluteStructure(self, Info: list[CreateOrUpdateAbsoluteStructureInfo2], BomViewTypeName: str, Complete: bool, Pref: CreateOrUpdateAbsoluteStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateAbsoluteStructureResponse:
        """    
             This is the overloaded function of Cad::_2007_01::StructureManagement::createOrUpdateAbsoluteStructure.
             It takes an additional variable into the CreateOrUpdateAbsoluteStructurePref2 structure
             to hold the last modified date of the BVR with an extra preference value to check
             it with server modifed date to make a decision whether we want to make modification
             on BVR. CreateOrUpdateAbsoluteStucture allows the user to find or create the absolute
             structure network of objects and relations for the input model. The service first
             attempts to check for the presence of duplicate context objects and then validate
             the existence of the structure to be created. If any of the objects exist and the
             input attribute values differ from those already set, an attempt is made to update
             the values. Note: The following AbsOccData attributes are not supported for arrangement
             qualified overrides. These attributes can only be overridden at the bvr level (which
             applies to all arrangements). If these attributes are overridden in the AssemblyArrangementInfo,
             they will be ignored. 1.child item 2.GDE object 3.instance number 4.occurrence name
             5.note 6.occurrence type 7.Variant instance As we process one contextItemRev object
             at one time, it is assumed that all edits for a given contextItemRev come in as one
             set of input.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         List of input structures that defines all the occurrence for a given parent
             
        :param BomViewTypeName: 
                         Type of BOMView
             
        :param Complete: 
                         flag that if true signifies that the structure represented in the input is the full
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
    def CreateOrUpdateRelativeStructure(self, Inputs: list[CreateOrUpdateRelativeStructureInfo2], BomViewTypeName: str, Complete: bool, Pref: CreateOrUpdateRelativeStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.CreateOrUpdateRelativeStructureResponse:
        """    
             This is the overloaded function of Cad::_2007_01::StructureManagement::createOrUpdateRelativeStructure.
             It takes an additional variable into the CreateOrUpdateRelativeStructureInfo2 structure
             to hold the last modified date of the BVR with an extra preference value to check
             it with server modifed date to make a decision whether we want to make modification
             on BVR. Create or update the relative structure objects and relations for the input
             model. The service first attempts to check for the presence of duplicate context
             objects and then validate the existence of the structure to be created. If any of
             the objects exist but the input attribute values that differ from those already set,
             an attempt is made to update the values if possible. This service assumes the input
             is in a bottom-up format such that if any failures occur, the structure that is created
             will be consistent. No attempt is made in the service to rearrange the input and
             process it in the correct order. As we process one parent context Object at one time,
             it is assumed that all edits for a given parent context come in as one set of input.
             

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
    def DeleteAssemblyArrangements(self, Info: list[DeleteAssemblyArrangementsInfo2], BomViewTypeName: str, Pref: DeleteAssemblyArrangementsPref) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteAssemblyArrangementsResponse:
        """    
             This operation deletes assembly arrangements and all the absolute occurrence data
             associated with the assembly arrangements.  It also deletes the relation between
             assembly arrangements and the BOM view revision object. The last modified date of
             the BVR can be specified for comparison against the last modified date in Teamcenter
             to ensure the BVR that contains the arrangement has not changed outside of this client
             context.
             

Use Cases:

             User deletes an existing assembly arrangement from an existing assembly.
             

             For this operation, the assembly is passed in as the itemRev
             and the assembly arrangement is passed in through arrangements.
             The assembly arrangement is removed from the assembly, as well as the relation between
             the arrangement and the BVR, and the UID of the deleted arrangement is added to the
             ServiceData list of deleted objects.
             


Dependencies:

             createOrUpdateAbsoluteStructure
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Info: 
                         List of item revisions and the assembly arrangements to delete from the found BOM
                         view revision.
             
        :param BomViewTypeName: 
                         The BOM view type used to find the existing BOM view object.
             
        :param Pref: 
                         The structure for setting specific preference input used by this operation.
             
        :return: 
        """
        ...
    def DeleteRelativeStructure(self, Inputs: list[DeleteRelativeStructureInfo2], BomViewTypeName: str, Pref: DeleteRelativeStructurePref2) -> Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.DeleteRelativeStructureResponse:
        """    
             Deletes one or more first level children of a parent assembly.  This is the overloaded
             function of Cad::_2007_01::StructureManagement::deleteRelativeStructure. It takes
             an additional variable into the DeleteRelativeStructureInfo2 structure to hold the
             last modified date of the BVR with an extra preference value to check it with server
             modifed date to make a decision whether we want to make modification on BVR.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Inputs: 
                         List input of structures that defines the parent and first level children to be deleted.
             
        :param BomViewTypeName: 
                         Qualifies the specified parent item revision(s) to identify a unique BOM   view revision.
             
        :param Pref: 
                         Preference structure specific for this service
             
        :return: The ServiceData contains the UIDs of any deleted occurrences
        """
        ...
    def QueryClassicOptions(self, InputRevisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> ClassicOptionsResponse:
        """    
             This operation is to find classic variant options defined on an ItemRevision
             object(s).
             

Use Cases:

             The user can use this operation to find all the classic variant options defined on
             given ItemRevision object. The option and values can be used for configuration
             or creating other related objects like variant conditions, constraint (defaults,
             derived defaults and rule checks) rules or VariantRule objects.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputRevisions: 
                         This is list of <b>ItemRevision</b> object on which variant options are to be queried.
             
        :return: with original input object(s)
             if any.
        """
        ...
    def QueryVariantConditions(self, InputBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> VariantConditionResponse:
        """    
             This operation is to find a variant condition value ( load if - this is a type of
             variant expression represents variant condition) for a BOMLine object.
             

Use Cases:

             The user needs variant condition defined on the BOMLine object, for display
             or editing purpose.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputBomLines: 
                         This has the list of <b>BOMLine</b> objects, on which variant condition are defined.
             
        :return: 
        """
        ...

