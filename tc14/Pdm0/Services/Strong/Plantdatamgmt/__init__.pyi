import Pdm0.Services.Strong.Plantdatamgmt._2019_06.PdmCore
import Pdm0.Services.Strong.Plantdatamgmt._2022_06.PdmCore
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model.Strong

class PdmCoreRestBindingStub(PdmCoreService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def FindPlantContentsUsingExtIds(self, Plant: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel, ExternalIds: list[str], ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Pdm0.Services.Strong.Plantdatamgmt._2019_06.PdmCore.FindPlantContentsUsingExtIdsResponse: ...
    def FindPlantContentsUsingExtIds2(self, CapitalAssetRoot: Teamcenter.Soa.Client.Model.Strong.Pdm0CARoot, ExternalIds: list[str], ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Pdm0.Services.Strong.Plantdatamgmt._2022_06.PdmCore.FindPlantContentsUsingExtIdsResp2: ...

class PdmCoreService:
    """
    
            This service contains utilities which augment the Plant data management services.
            


Library Reference:

Pdm0SoaPlantDataMgmtStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> PdmCoreService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def FindPlantContentsUsingExtIds(self, Plant: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel, ExternalIds: list[str], ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Pdm0.Services.Strong.Plantdatamgmt._2019_06.PdmCore.FindPlantContentsUsingExtIdsResponse: ...
    def FindPlantContentsUsingExtIds2(self, CapitalAssetRoot: Teamcenter.Soa.Client.Model.Strong.Pdm0CARoot, ExternalIds: list[str], ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Pdm0.Services.Strong.Plantdatamgmt._2022_06.PdmCore.FindPlantContentsUsingExtIdsResp2: ...

