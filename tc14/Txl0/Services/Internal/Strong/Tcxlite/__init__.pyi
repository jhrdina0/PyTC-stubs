import Teamcenter.Soa.Client
import Txl0.Services.Internal.Strong.Tcxlite._2022_12.DataManagement

class DataManagementRestBindingStub(DataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def MakeUserAndTenant(self, TenantCreateOption: Txl0.Services.Internal.Strong.Tcxlite._2022_12.DataManagement.TenantCreateOption, UserCreateInput: Txl0.Services.Internal.Strong.Tcxlite._2022_12.DataManagement.UserCreateInput) -> Txl0.Services.Internal.Strong.Tcxlite._2022_12.DataManagement.MakeUserResponse: ...

class DataManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DataManagementService: ...
    def MakeUserAndTenant(self, TenantCreateOption: Txl0.Services.Internal.Strong.Tcxlite._2022_12.DataManagement.TenantCreateOption, UserCreateInput: Txl0.Services.Internal.Strong.Tcxlite._2022_12.DataManagement.UserCreateInput) -> Txl0.Services.Internal.Strong.Tcxlite._2022_12.DataManagement.MakeUserResponse: ...

