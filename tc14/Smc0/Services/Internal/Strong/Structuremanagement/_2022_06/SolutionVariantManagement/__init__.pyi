import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SolutionVariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindOrCreateSolutionVariantUsages(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

