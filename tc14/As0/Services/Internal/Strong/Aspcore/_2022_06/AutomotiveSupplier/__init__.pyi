import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AutomotiveSupplier:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteReadinessCheck(self, ChangeItemRev: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision, ReadinessCheckOptions: list[str], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

