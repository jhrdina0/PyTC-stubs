import Prg1.Services.Internal.Strong.Programplanningapp._2018_11.AdvancedProgramManagement
import System
import Teamcenter.Soa.Client

class AdvancedProgramManagementRestBindingStub(AdvancedProgramManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetVolumeTargets(self, InputInfo: list[Prg1.Services.Internal.Strong.Programplanningapp._2018_11.AdvancedProgramManagement.GetVolumeTargetsInputInfo]) -> Prg1.Services.Internal.Strong.Programplanningapp._2018_11.AdvancedProgramManagement.GetVolumeTargetsResponse: ...

class AdvancedProgramManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AdvancedProgramManagementService: ...
    def GetVolumeTargets(self, InputInfo: list[Prg1.Services.Internal.Strong.Programplanningapp._2018_11.AdvancedProgramManagement.GetVolumeTargetsInputInfo]) -> Prg1.Services.Internal.Strong.Programplanningapp._2018_11.AdvancedProgramManagement.GetVolumeTargetsResponse: ...

