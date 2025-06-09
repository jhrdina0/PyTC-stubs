import System
import Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained
import Teamcenter.Services.Strong.Asmaintained._2010_04.AsMaintained
import Teamcenter.Services.Strong.Asmaintained._2014_06.AsMaintained
import Teamcenter.Services.Strong.Asmaintained._2015_03.AsMaintained
import Teamcenter.Services.Strong.Asmaintained._2021_12.AsMaintained
import Teamcenter.Soa.Client
import typing

class AsMaintainedRestBindingStub(AsMaintainedService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ApplyMroRevisionRule(self, InputData: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ApplyMroRevisionRuleInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ApplyMroRevisionRuleResponse: ...
    def ChangePhysicalPartDisposition(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ChangeDispositionInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ChangeDispositionResponse: ...
    @typing.overload
    def GenerateAsMaintainedStructure(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.GenerateAsMaintainedStructureInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.GenerateAsMaintainedStructureResponse: ...
    @typing.overload
    def GenerateAsMaintainedStructure(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2014_06.AsMaintained.GenerateAsMaintainedStructureInfo1]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.GenerateAsMaintainedStructureResponse: ...
    def InstallAsmPhysicalPart(self, InputData: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.InstallAsmPhysicalPartInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.InstallAsmPhysicalPartResponse: ...
    def MovePhysicalPart(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.MovePhysicalPartInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.MovePhysicalPartResponse: ...
    def ReplaceAsmPhysicalPart(self, InputData: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ReplaceAsMaintainedPartInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ReplacePhysicalPartResponse: ...
    def UninstallPhysicalPart(self, InputData: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.UninstallPhysicalPartInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.UninstallPhysicalPartResponse: ...
    def SearchInstallablePhysPart(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2010_04.AsMaintained.SearchInstallablePhysPartInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2010_04.AsMaintained.SearchInstallablePhysPartResponse: ...
    def SetMroWindowTopLine(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2010_04.AsMaintained.SetMroWindowTopLineInfo]) -> Teamcenter.Services.Strong.Asmaintained._2010_04.AsMaintained.SetMroWindowTopLineResponse: ...
    def RecordUtilization(self, RecordUtilizationInfo: list[Teamcenter.Services.Strong.Asmaintained._2015_03.AsMaintained.RecordUtilizationInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2015_03.AsMaintained.RecordUtilizationResponse: ...
    def RecordAndInvalidateUtilization(self, Info: list[Teamcenter.Services.Strong.Asmaintained._2021_12.AsMaintained.UtilizationInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2021_12.AsMaintained.UtilizationResponse: ...

class AsMaintainedService:
    """
    
            The AsMaintained service provides operations to manage as-maintained PhysicalPart
            structures. As-maintained PhysicalPart structures can be generated for the
            Item or subclasses of Item which are marked as MRO types.
            
            The AsMaintained service can be used to support the following:
            

Â Â Â Â Generate an AsMaintained Physical Part structure
            
Â Â Â Â Install AsMaintained parts in the structure
            
Â Â Â Â Uninstall AsMaintained parts from the structure
            
Â Â Â Â Replace AsMaintained parts in the structure
            
Â Â Â Â Move an AsMaintained part from one location
            to other
            
Â Â Â Â Change the disposition of an AsMaintained
            part
            
Â Â Â Â Get all open positions in an AsMaintained
            structure in which parts can be installed
            
Â Â Â Â Create BOM windows for AsMaintained parts
            
Â Â Â Â Apply revision rules for AsMaintained structures
            in the MRO BOM Window
            
Â Â Â Â Search for all installable AsMaintained parts
            in the system which can be installed in a given position in an AsMaintained structure
            
Â Â Â Â Perform BOM comparison of two AsMaintained
            structures
            
Â Â Â Â Perform accountability check on two AsMaintained
            structures
            




Library Reference:

TcSoaAsMaintainedStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AsMaintainedService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ApplyMroRevisionRule(self, InputData: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ApplyMroRevisionRuleInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ApplyMroRevisionRuleResponse:
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
    def ChangePhysicalPartDisposition(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ChangeDispositionInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ChangeDispositionResponse:
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
    @typing.overload
    def GenerateAsMaintainedStructure(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.GenerateAsMaintainedStructureInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.GenerateAsMaintainedStructureResponse: ...
    @typing.overload
    def GenerateAsMaintainedStructure(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2014_06.AsMaintained.GenerateAsMaintainedStructureInfo1]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.GenerateAsMaintainedStructureResponse: ...
    def InstallAsmPhysicalPart(self, InputData: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.InstallAsmPhysicalPartInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.InstallAsmPhysicalPartResponse:
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
    def MovePhysicalPart(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.MovePhysicalPartInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.MovePhysicalPartResponse:
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
    def ReplaceAsmPhysicalPart(self, InputData: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ReplaceAsMaintainedPartInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.ReplacePhysicalPartResponse:
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
    def UninstallPhysicalPart(self, InputData: list[Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.UninstallPhysicalPartInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2009_06.AsMaintained.UninstallPhysicalPartResponse:
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
    def SearchInstallablePhysPart(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2010_04.AsMaintained.SearchInstallablePhysPartInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2010_04.AsMaintained.SearchInstallablePhysPartResponse:
        """    
             This operation gets the installable PhysicalPartRevision based on the usage
             name. It will get the Preferred, Alternate, Substitute and Deviated
PhysicalPartRevision for specified usage.
             

Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param Input: 
                         The required information to search the installable Physical Parts.
             
        :return: list of partial errors.
        """
        ...
    def SetMroWindowTopLine(self, Input: list[Teamcenter.Services.Strong.Asmaintained._2010_04.AsMaintained.SetMroWindowTopLineInfo]) -> Teamcenter.Services.Strong.Asmaintained._2010_04.AsMaintained.SetMroWindowTopLineResponse:
        """    
             This operation will set the given object as top line for the specified BOMWindow.
             

Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param Input: 
                         The required information to set the object as top line for a <b>BOMWindow</b>.
             
        :return: list of partial errors.
        """
        ...
    def RecordUtilization(self, RecordUtilizationInfo: list[Teamcenter.Services.Strong.Asmaintained._2015_03.AsMaintained.RecordUtilizationInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2015_03.AsMaintained.RecordUtilizationResponse:
        """    
             Maintenance Repair and Overhaul (MRO) introduces physical parts and structures of
             physical parts which are generated from a neutral structure of part(s).  Either As-Built
             or As-Maintained physical structures may be generated. As-Built physical parts do
             not support utilization recording. All references to physical parts and physical
             part revisions in this operation are for As-Maintained physical parts only.
             
             Characteristic definitions describe usage characteristics that can be recorded or
             measured against a physical part.  Characteristic definitions may be created and
             related to parts before the As-Maintained physical part is generated
             
             This operation records utilization for a physical part revision.  Utilization may
             be recorded against any characteristic definition associated to a neutral part from
             which the physical part is realized.
             


Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param RecordUtilizationInfo: 
                         The information to record the utilization for the physical part revision.
             
        :return: 
        """
        ...
    def RecordAndInvalidateUtilization(self, Info: list[Teamcenter.Services.Strong.Asmaintained._2021_12.AsMaintained.UtilizationInputInfo]) -> Teamcenter.Services.Strong.Asmaintained._2021_12.AsMaintained.UtilizationResponse: ...

