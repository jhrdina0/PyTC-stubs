import Cbm0.Services.Internal.Strong.Colorbompmm._2016_03.ColorBOMManagement
import Teamcenter.Soa.Client

class ColorBOMManagementRestBindingStub(ColorBOMManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def QueryColorRules(self, QueryInput: Cbm0.Services.Internal.Strong.Colorbompmm._2016_03.ColorBOMManagement.QueryRuleInput) -> Cbm0.Services.Internal.Strong.Colorbompmm._2016_03.ColorBOMManagement.QueryRuleResponse: ...

class ColorBOMManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ColorBOMManagementService: ...
    def QueryColorRules(self, QueryInput: Cbm0.Services.Internal.Strong.Colorbompmm._2016_03.ColorBOMManagement.QueryRuleInput) -> Cbm0.Services.Internal.Strong.Colorbompmm._2016_03.ColorBOMManagement.QueryRuleResponse: ...

