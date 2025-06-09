import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ApplyMroRevisionRuleInfo:
    """
    Structure represents the parameters of the MRORevisionRule.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input ApplyMroRevisionRuleInfo element. This value is unchanged from
            the input, and can be used to identify this response element with the corresponding
            input element.
            """
    Today: bool
    """If true, the As-Maintained structure is to be configured for today's date."""
    Serviceable: bool
    """If true, only the Serviceable objects are to be configured."""
    Any: bool
    """A Boolean which indicates the status required to create the Mro Revision rule."""
    EffectiveDate: System.DateTime
    """
            The date used to configure the exact PhysicalPartRevision objects. If "today"
            flag is selected, this field value will not be considered.
            """

class ApplyMroRevisionRuleInputInfo:
    """
    
            Structure represents the parameters required to apply MRO Revision rule to an as-maintained
            PhysicalPart structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    TopLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine
    """The top AsMaintainedBOMLine object set in the MroBOMWindow object."""
    MroRevRule: Teamcenter.Soa.Client.Model.Strong.MroRevisionRule
    """The MroRevisionRule object."""
    ApplyMroRevisionRuleInfo: ApplyMroRevisionRuleInfo
    """The structure containing information about the MroRevisionRule object."""

class ApplyMroRevisionRuleOutput:
    """
    Structure contains the configured AsMaintainedBOMLine object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input ApplyMroRevisionRuleInputInfo element. This value is unchanged
            from the input, and can be used to identify this response element with the corresponding
            input element.
            """
    ConfiguredTopLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine
    """The configured top line object."""

class ApplyMroRevisionRuleResponse:
    """
    
            Structure contains the configured top level AsMaintainedBOMLine object and
            the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    ApplyMroRevRuleOutput: list[ApplyMroRevisionRuleOutput]
    """Structure containing the configured top line."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class AsMaintainedStructureInfo:
    """
    
            Structure represents the parameters required to generate an as-maintained PhysicalPart
            structure for a given design Item structure.
            
    """
    def __init__(self, ) -> None: ...
    NeutralItemId: str
    """The item id of the design Item object."""
    SerialNumber: str
    """The Serial Number, required to uniquely identify a serialized PhysicalPart."""
    LotNumber: str
    """The Lot Number,  if the PhysicalPart is of Lot type."""
    ManufacturerId: str
    """The Manufacturer's id, required to uniquely identify a serialized PhysicalPart."""
    NumberOfLevels: int
    """
            An integer which indicates the depth of the design Item structure to be traversed
            for generating the as-maintained PhysicalPart structure.
            """
    UseSerialNumberGenerators: bool
    """
            A Boolean to indicate if Serial Number generators are to be used to generate the
            Serial Numbers for the PhysicalParts.
            """
    StructureContext: str
    """
            Name of the Structure Context object. Structure context object is created with the
            current configuration of the MroBOMWindow and saved on the top PhysicalPart.
            """
    LocationName: str
    """The name of the PhysicalLocation object."""
    InstallationDate: System.DateTime
    """The date on which the actual PhysicalPart was installed on its parent PhysicalPart."""
    ManufacturingDate: System.DateTime
    """The date on which the PhysicalPart was manufactured."""
    DispositionType: str
    """The disposition type to be applied to the PhysicalPart objects."""
    EffectiveFromDate: System.DateTime
    """The Date from which the PhysicalPartRevision object is effective."""
    EffectiveToDate: System.DateTime
    """The Date up to which the PhysicalPartRevision object is effective."""

class ChangeDispositionInfo:
    """
    
            Represents the parameters required to change the disposition of an as-maintained
            PhysicalPart object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PhysicalPart: Teamcenter.Soa.Client.Model.Strong.PhysicalPart
    """The PhysicalPart object, whose disposition is to be changed."""
    DispositionType: Teamcenter.Soa.Client.Model.Strong.DispositionType
    """The DispositionType object which is the new disposition value."""
    DispStartTime: System.DateTime
    """The start time of the new disposition."""

class ChangeDispositionOutput:
    """
    The output parameters of the Change Disposition operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input ChangeDispositionInfo element. This value is unchanged from the
            input, and can be used to identify this response element with the corresponding input
            element.
            """
    DispRelation: Teamcenter.Soa.Client.Model.Strong.DispositionApplicability
    """The relation object."""

class ChangeDispositionResponse:
    """
    DispositionApplicability relation object and the ServiceData.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""
    Output: list[ChangeDispositionOutput]
    """DispositionApplicability relation object."""

class ExtendedAttributes:
    """
    Structure represents the structure containing additional attributes.
    """
    def __init__(self, ) -> None: ...
    ObjectType: str
    """Object Type"""
    Attributes: System.Collections.Hashtable
    """Attributes"""

class GenerateAsMaintainedStructureInfo:
    """
    
            Represents the parameters required to generate an as-maintained PhysicalPart
            structure for a given design Item structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    NeutralBOMLine: Teamcenter.Soa.Client.Model.Strong.NeutralBOMLine
    """The line object which holds all the properties from the PartLogisticsForm."""
    AsMaintainedStructureInfo: AsMaintainedStructureInfo
    """
            The structure holding all the information required to generate an as-maintained PhysicalPart
            structure.
            """

class GenerateAsMaintainedStructureOutput:
    """
    Structure represents the output parameters of the generateAsMaintainedStructure operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the output GenerateAsMaintainedStructureInfo element. This value is unchanged
            from the input, and can be used to identify this response element with the corresponding
            input element.
            """
    PhysicalPartRevision: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """The top level object."""

class GenerateAsMaintainedStructureResponse:
    """
    
            Structure contains the created top level PhysicalPart object and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GenerateAsMaintainedStructureOutput]
    """Created top level PhysicalPart object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class InstallAsmPhysicalPartInfo:
    """
    The parameters required to install an as-maintained PhysicalPart under a parent.
    """
    def __init__(self, ) -> None: ...
    UsagePropertyValue: str
    """Usage Property Value"""
    InstallationDate: System.DateTime
    """
            The Installation Date which will be set on the AsMaintainedStructure relation
            object.
            """
    ExtendedData: ExtendedAttributes
    """An AttributeNameValueMap object, used to pass additional information."""

class InstallAsmPhysicalPartInputInfo:
    """
    The parameters required to install an as-maintained PhysicalPart under a parent.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    SelectedLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine
    """The parent  line object, under which the PhysicalPart object will be installed."""
    CopiedPhysPart: Teamcenter.Soa.Client.Model.Strong.PhysicalPart
    """The object which will be installed."""
    SelectedUsageLine: Teamcenter.Soa.Client.Model.Strong.NeutralBOMLine
    """The line object corresponding to the selected usage."""
    InstallInfo: InstallAsmPhysicalPartInfo
    """A structure containing the install information like install date."""

class InstallAsmPhysicalPartOutput:
    """
    
            Structure represents the output parameters of the Install as-maintained PhysicalPart
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input InstallAsmPhysicalPartInputInfo element. This value is unchanged
            from the input, and can be used to identify this response element with the corresponding
            input element.
            """
    InstalledLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine
    """The line object created to represent the installed PhysicalPartRevision object."""

class InstallAsmPhysicalPartResponse:
    """
    
            Structure contains the new AsMaintainedBOMLine and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[InstallAsmPhysicalPartOutput]
    """A list of newly created AsMaintainedBOMLine."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class MovePhysicalPartInfo:
    """
    Structure represents the parameters required to move the PhysicalPart .
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PhysicalPart: Teamcenter.Soa.Client.Model.Strong.PhysicalPart
    """The  object to move into location."""
    Location: Teamcenter.Soa.Client.Model.Strong.PhysicalLocation
    """The location object."""
    InTime: System.DateTime
    """The installation time."""

class MovePhysicalPartOutput:
    """
    Structure represents the output parameters of the move PhysicalPart operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input MovePhysicalPartInfo element. This value is unchanged from the
            input, and can be used to identify this response element with the corresponding input
            element.
            """
    Relation: Teamcenter.Soa.Client.Model.Strong.PhysicalLocationUsage
    """The location usage object created to represent the moved  PhysicalPart object."""

class MovePhysicalPartResponse:
    """
    
            Structure represents a list of PhysicalLocationUsage relation and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""
    Output: list[MovePhysicalPartOutput]
    """A list of PhysicalLocationUsage relation."""

class ReplaceAsMaintainedPartInfo:
    """
    Structure represents the parameters required to replace an as-maintained PhysicalPart.
    """
    def __init__(self, ) -> None: ...
    DispositionValue: str
    """Disposition value."""
    LocationName: str
    """Location name."""
    ReplaceDate: System.DateTime
    """The date at which the PhysicalPart object which is replaced."""
    ExtendedData: ExtendedAttributes
    """An AttributeNameValueMap object, used to pass additional information."""

class ReplaceAsMaintainedPartInputInfo:
    """
    Structure represents the parameters required to replace an as-maintained PhysicalPart.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    SelectedAsMaintainedBOMLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine
    """The line object, line which will be replaced."""
    CopiedPhysPart: Teamcenter.Soa.Client.Model.Strong.PhysicalPart
    """The object which will be replaced."""
    ReplacePhysicalPartInfo: ReplaceAsMaintainedPartInfo
    """A structure containing the information to replace the part like replace date."""

class ReplacePhysicalPartOutput:
    """
    
            Structure represents the output parameters of the replace as-maintained PhysicalPart
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input ReplaceAsMaintainedPartInputInfo element. This value is unchanged
            from the input, and can be used to identify this response element with the corresponding
            input element.
            """
    ReplacerAsMaintainedBOMLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine
    """The line object, created to represent the replaced PhysicalPartRevision object."""

class ReplacePhysicalPartResponse:
    """
    
            Structure containing the replace AsMaintainedBOMLine and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ReplacePhysicalPartOutput]
    """A structure containing the replaced AsMaintainedBOMLine."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class UninstallPhysicalPartInfo:
    """
    The structure containing the information to uninstall the PhysicalPart.
    """
    def __init__(self, ) -> None: ...
    DispositionValue: str
    """Disposition value."""
    LocationName: str
    """Location name."""
    UninstallationDate: System.DateTime
    """The date at which the PhysicalPart object which is uninstalled."""
    ExtendedData: ExtendedAttributes
    """An AttributeNameValueMap object, used to pass additional information."""

class UninstallPhysicalPartInputInfo:
    """
    
            The parameters required to uninstall an as-maintained PhysicalPartRevision
            object from the structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    SelectedAsMaintainedBOMLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine
    """The line object to be removed from the structure."""
    UninstallPhysicalPartInfo: UninstallPhysicalPartInfo
    """The structure containing the information to uninstall the PhysicalPart."""

class UninstallPhysicalPartOutput:
    """
    
            Structure represents the output parameters of the replace as-maintained PhysicalPart
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input UninstallPhysicalPartInputInfo element. This value is unchanged
            from the input, and can be used to identify this response element with the corresponding
            input element.
            """
    ReplacerAsMaintainedBOMLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine
    """The created object to represent the replaced PhysicalPartRevision object."""

class UninstallPhysicalPartResponse:
    """
    
            Structure containing the un installed BOMLine and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[UninstallPhysicalPartOutput]
    """A un-installed BOMLine."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class AsMaintained:
    """
    Interface AsMaintained
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ApplyMroRevisionRule(self, InputData: list[ApplyMroRevisionRuleInputInfo]) -> ApplyMroRevisionRuleResponse:
        """    
             This operation applies the revision rule specific to as-maintained structure configuration.
             As-Maintained structures can be configured only by Date and Serviceability.
             
             The PhysicalPartRevision objects have "Effective From" and "Effective
             To" dates. If the date applied on the MroBOMWindow object falls in-between
             those two dates then that revision is considered to be effective. This filter is
             applied on the entire as-maintained structure. Once an MRORevisionRule is
             applied or changed, the entire structure is updated to show the updated configuration.
             
             Serviceability indicates whether a PhysicalPart object is in its useful life.
             By default, all the Serviceable parts are configured.
             


Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param InputData: 
                         Apply MRO Revision Rule Input
             
        :return: 
        """
        ...
    def ChangePhysicalPartDisposition(self, Input: list[ChangeDispositionInfo]) -> ChangeDispositionResponse:
        """    
             This operation changes the disposition of an as-maintained PhysicalPart object.
             When a PhysicalPart object is created, a default disposition In-Service
             is created. It can be changed to any user specified value later on.
             

Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param Input: 
                         The required information to change the disposition of an as-maintained <b>PhysicalPart</b>
                         object.
             
        :return: list of partial errors.
        """
        ...
    def GenerateAsMaintainedStructure(self, Input: list[GenerateAsMaintainedStructureInfo]) -> GenerateAsMaintainedStructureResponse:
        """    
             This operation generates an as-maintained PhysicalPart structure for a given
             design Item structure. The design structure should be first set in a BOMWindow
             object so that NeutralBOMLine objects are constructed for every Item
             in the structure. An as-maintained PhysicalPart is created for every Item
             in the structure which is marked as Traceable (This value is set on the PartLogisticsForm
             associated with the Item). All the parent/child as-maintained PhysicalPart
             objects are related to each other by AsMaintainedStructure relation. A StructureContext
             object is created with the configuration applied to the BOMWindow and saved
             on the top PhysicalPart objects.
             
             One can specify the following parameters on the PartLogisticsForm.
             

    Traceable    If marked
             true, a PhysicalPart will be created for the Item.
             
    Serialized    If marked
             true, the created PhysicalPart will be marked as serialized.
             
    Lot    If marked true,
             the created PhysicalPart will be marked as lot.
             
    Preserve Quantity    If
             marked true, only one PhysicalPart will be created irrespective of the quantity
             specified on the design Item.
             



             An as-maintained PhysicalPart structure is an imprecise structure. The parent
             and child relation, the AsMaintainedStructure relation, is between the revision
             of the parent and the item of the child.
             
             In a PhysicalPart structure, if the parts are serialized and all the required
             information like Serial Number, Lot Number(in case of Lot parts), Manufacturer's
             id are specified, then the PhysicalPart object's usage is set as Preferred.
             The parts which are not marked as Serialized or Lot, the default value
             is set to Preferred. For the serialized or lot parts, if the Serial Number
             or Lot Number is not specified, those parts are set as Missing. Once the
             required information is provided, the usage is changed to Preferred.
             
             A Business object constant defined for the Item class governs the type of PhysicalPart
             object to be created during the structure generation. By default the value it set
             to PhysicalPart.
             

Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param Input: 
                         Holds the required information to generate an as-maintained <b>PhysicalPart</b> structure
                         for a design <b>Item</b> structure.
             
        :return: 
        """
        ...
    def InstallAsmPhysicalPart(self, InputData: list[InstallAsmPhysicalPartInputInfo]) -> InstallAsmPhysicalPartResponse:
        """    
             This operation installs a PhysicalPart object under a parent object in a given
             position. In the as-maintained structure, the relations are imprecise. Hence the
             child PhysicalPart object will be installed under the parent PhysicalPartRevision
             object. An object of AsMaintainedStructure will be created between the two
             objects.
             
             Based on the specified position, the usage will be determined by the code. Following
             values are possible.
             

    Preferred    If the design
             Item of the child part is a part of the configured design Item structure
             for the parent part.
             
    Alternate    If the design
             Item of the child part is an Alternate of the Item configured in the design
             Item structure for the parent part.
             
    Substitute    If the
             design Item of the child part is a Substitute of the Item configured
             in the design Item structure for the parent part.
             
    Deviated    If the design
             Item of the child part is not a part of the Item configured in the
             design Item structure for the parent part. A Valid deviation should be already
             set up between the parent and the child parts.
             



Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param InputData: 
                         Holds the required information to install an as-maintained <b>PhysicalPart</b> under
                         a parent.
             
        :return: 
        """
        ...
    def MovePhysicalPart(self, Input: list[MovePhysicalPartInfo]) -> MovePhysicalPartResponse:
        """    
             This operation moves the PhysicalPart to specified location.
             

Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param Input: 
                         A list of structures which hold the required information to move the <b>PhysicalPart</b>
                         from one location to another.
             
        :return: 
        """
        ...
    def ReplaceAsmPhysicalPart(self, InputData: list[ReplaceAsMaintainedPartInputInfo]) -> ReplacePhysicalPartResponse:
        """    
             This operation replaces an as-maintained PhysicalPart in a structure with
             a given as-maintained PhysicalPart object.  The existing as-maintained PhysicalPart
             object will be removed from the structure and the new object will be installed in
             that position. A new AsMaintainedStructure relation will be created between
             the parent and the new PhysicalPart objects. The Installation Time specified
             will be set as the Installation Time on the relation object.
             

Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param InputData: 
                         A list of structures which hold the required information to replace the existing
                         as-maintained <b>PhysicalPart</b> object in a structure with a new <b>PhysicalPart</b>
                         object.
             
        :return: 
        """
        ...
    def UninstallPhysicalPart(self, InputData: list[UninstallPhysicalPartInputInfo]) -> UninstallPhysicalPartResponse:
        """    
             This operation uninstalls an as-maintained PhysicalPartRevision object from
             a structure. When an as-maintained object is uninstalled from a structure, if the
             usage is not 'Extra to Design' a new PhysicalPartRevision object is
             created in the structure in that position. A new AsMaintainedBOMLine is constructed
             to represent that new part. The usage of the new part is set to Missing as
             there is no actual part in that position. An object of AsMaintainedStructure
             relation is created between the new part and the parent part.
             

Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param InputData: 
                         Holds the required information to un-install an as-maintained <b>PhysicalPartRevision</b>
                         from a structure.
             
        :return: 
        """
        ...

