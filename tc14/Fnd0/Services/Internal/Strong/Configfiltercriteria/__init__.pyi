import Fnd0.Services.Internal.Strong.Configfiltercriteria._2013_12.VariantManagement
import Teamcenter.Soa.Client

class VariantManagementRestBindingStub(VariantManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExecuteConfiguratorService(self, InputXMLString: str, ConfiguratorURL: str) -> Fnd0.Services.Internal.Strong.Configfiltercriteria._2013_12.VariantManagement.ConfiguratorServiceResponse: ...

class VariantManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> VariantManagementService: ...
    def ExecuteConfiguratorService(self, InputXMLString: str, ConfiguratorURL: str) -> Fnd0.Services.Internal.Strong.Configfiltercriteria._2013_12.VariantManagement.ConfiguratorServiceResponse: ...

