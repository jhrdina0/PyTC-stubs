import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class AutomotiveSupplierRestBindingStub(AutomotiveSupplierService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExecuteReadinessCheck(self, ChangeItemRev: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision, ReadinessCheckOptions: list[str], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class AutomotiveSupplierService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AutomotiveSupplierService: ...
    def ExecuteReadinessCheck(self, ChangeItemRev: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision, ReadinessCheckOptions: list[str], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

