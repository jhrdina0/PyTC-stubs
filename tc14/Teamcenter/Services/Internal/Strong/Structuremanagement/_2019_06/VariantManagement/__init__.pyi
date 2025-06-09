import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ApplyRollupVariantConfiguration(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], ConsiderWindowSVR: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

