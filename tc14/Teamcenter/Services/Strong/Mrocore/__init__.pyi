import System
import Teamcenter.Services.Strong.Mrocore._2009_06.MROCore
import Teamcenter.Services.Strong.Mrocore._2010_04.MROCore
import Teamcenter.Services.Strong.Mrocore._2012_02.MROCore
import Teamcenter.Services.Strong.Mrocore._2014_06.MROCore
import Teamcenter.Services.Strong.Mrocore._2018_06.MROCore
import Teamcenter.Services.Strong.Mrocore._2020_04.MROCore
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import typing

class MROCoreRestBindingStub(MROCoreService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def RebasePhysicalPart(self, InputData: list[Teamcenter.Services.Strong.Mrocore._2009_06.MROCore.RebasePhysPartInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2009_06.MROCore.RebasePhysPartResponse: ...
    def RecordUtilization(self, Info: list[Teamcenter.Services.Strong.Mrocore._2009_06.MROCore.RecordUtilizationInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2009_06.MROCore.RecordUtilizationResponse: ...
    def CreateMROBOMWindows(self, Input: list[Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.CreateMROBOMWindowsInfo]) -> Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.CreateMROBOMWindowsResponse: ...
    def DuplicatePhysicalStructure(self, InputData: list[Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.DuplicatePhysStructInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.DuplicatePhysStructResponse: ...
    def RenamePhysicalPart(self, InputInfo: list[Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.RenamePhysicalPartInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.RenamePhysicalPartResponse: ...
    def DisplayUtilization(self, InputInfo: list[Teamcenter.Services.Strong.Mrocore._2012_02.MROCore.DisplayUtilizationInfo]) -> Teamcenter.Services.Strong.Mrocore._2012_02.MROCore.DisplayUtilizationResponse: ...
    def AssignLot(self, Info: list[Teamcenter.Services.Strong.Mrocore._2014_06.MROCore.AssignLotInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def RecordAndInvalidateUtilization(self, Info: list[Teamcenter.Services.Strong.Mrocore._2018_06.MROCore.UtilizationInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2018_06.MROCore.UtilizationResponse: ...
    @typing.overload
    def RecordAndInvalidateUtilization(self, Info: list[Teamcenter.Services.Strong.Mrocore._2020_04.MROCore.UtilizationInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2020_04.MROCore.UtilizationResponse: ...

class MROCoreService:
    """
    
            The MROCore service provides operations to manage MRO PhysicalPart
structures
            and Item objects which are marked as MRO types.

            The MROCore service can be used to support the following:

Â Â Â Â Create BOM windows.

Â Â Â Â Get the Lots for the Neutral Item.

Â Â Â Â Name the Occurrence for the Neutral Item.

Â Â Â Â Rebase the Physical Part.

Â Â Â Â Rename the Physical Part.

Â Â Â Â Record utilization for physical Part.

Â Â Â Â Display Utilization for Physical Part.

Â Â Â Â Duplicate the Physical Structure.

Â Â Â Â Setup Deviation.

Library Reference:

TcSoaMROCoreStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MROCoreService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def RebasePhysicalPart(self, InputData: list[Teamcenter.Services.Strong.Mrocore._2009_06.MROCore.RebasePhysPartInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2009_06.MROCore.RebasePhysPartResponse:
        """    
             This operation allows rebasing the PhysicalPartRevision associated with the
             PhysicalBOMLine to the Neutral ItemRevision associated with the NeutralBOMLine.
             It also saves StructureContext associated with the Neutral Structure, with
             PhysicalPartRevision. You can rebase the PhysicalPartRevision to the
             different revision of the Item than the existing.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param InputData: 
                         Structures which holds the required information to rebase the <b>PhysicalPartRevision</b>.
             
        :return: 
        """
        ...
    def RecordUtilization(self, Info: list[Teamcenter.Services.Strong.Mrocore._2009_06.MROCore.RecordUtilizationInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2009_06.MROCore.RecordUtilizationResponse:
        """    
             This operation records the utilization for the PhysicalPart. Utilization
             can be recorded for the CharacteristicsDefinition associated to neutral Item
             for which the PhysicalPart is realized from.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param Info: 
                         Structures which hold the required information to record the utilization for the
                         <b>PhysicalPart</b>.
             
        :return: 
        """
        ...
    def CreateMROBOMWindows(self, Input: list[Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.CreateMROBOMWindowsInfo]) -> Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.CreateMROBOMWindowsResponse:
        """    
             This operation creates MroBOMWindow and applies the RevisionRule.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param Input: 
                         A list of structures which hold the required information to create <b>BOMwindows</b>.
             
        :return: list of partial errors.
        """
        ...
    def DuplicatePhysicalStructure(self, InputData: list[Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.DuplicatePhysStructInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.DuplicatePhysStructResponse:
        """    
             This operation duplicates the physical structure. PhysicalBOMLine is provided
             to identify the structure to duplicate and the Serial Number, Lot Number, Manufacturer
             Id, Installation Date, Manufacturing Date, Number of Levels etc. is provided
             to create the top PhysicalPart object. If the global constant ReuseAuthorizedDeviation
             is set to true then the deviation authority is reused in the duplicated structure.
             The structure below the PhysicalPart with usage as "Extra to Design"
             is not duplicated.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param InputData: 
                         Structures which hold the information to duplicate the Physical Structure like <b>PhysicalBOMLine</b>
                         and structure <i>DuplicatePhysStructInfo</i> which holds the information <i>Serial
                         Number, Lot Number, Manufacturer Id, Installation Date, Manufacturing Date, Number
                         of Levels</i> etc.
             
        :return: 
        """
        ...
    def RenamePhysicalPart(self, InputInfo: list[Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.RenamePhysicalPartInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2010_04.MROCore.RenamePhysicalPartResponse:
        """    
             This operation renames the PhysicalPart by modifying the modifying either
             Serial Number or Part Number or both. If the PhysicalPart is not as-built
             PhysicalPart and the PhysicalPartRevision is released then the PhysicalPart
             is revised otherwise the latest PhysicalPartRevision is updated.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param InputInfo: 
                         Structures which hold the required information to rename the <b>PhysicalPart</b>.
             
        :return: 
        """
        ...
    def DisplayUtilization(self, InputInfo: list[Teamcenter.Services.Strong.Mrocore._2012_02.MROCore.DisplayUtilizationInfo]) -> Teamcenter.Services.Strong.Mrocore._2012_02.MROCore.DisplayUtilizationResponse:
        """    
             This operation gets the utilization data till the date specified for a PhysicalPart.
             The data is represented by Utilization object. Utilization object contains
             the information like Characteristic Name, Characteristic Unit, Time Since New, Last
             Recorded Value etc.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param InputInfo: 
                         The information to capture the utilization data for a <b>PhysicalPart</b>.
             
        :return: list
             of partial errors.
        """
        ...
    def AssignLot(self, Info: list[Teamcenter.Services.Strong.Mrocore._2014_06.MROCore.AssignLotInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation assigns the Lot to the PhysicalPart and deducts the
             quantity by the specified size. If the Size is greater than the lot usage or the
             PhysicalPart quantity then the error is thrown.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param Info: 
                         A list of AssignLotInfo structures which hold the information to assign the <b>Lot</b>
                         to the <b>PhysicalPart</b>.
             
        :return: 
        """
        ...
    @typing.overload
    def RecordAndInvalidateUtilization(self, Info: list[Teamcenter.Services.Strong.Mrocore._2018_06.MROCore.UtilizationInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2018_06.MROCore.UtilizationResponse: ...
    @typing.overload
    def RecordAndInvalidateUtilization(self, Info: list[Teamcenter.Services.Strong.Mrocore._2020_04.MROCore.UtilizationInputInfo]) -> Teamcenter.Services.Strong.Mrocore._2020_04.MROCore.UtilizationResponse: ...

