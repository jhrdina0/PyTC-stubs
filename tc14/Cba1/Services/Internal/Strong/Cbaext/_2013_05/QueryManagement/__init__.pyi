import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindAlignedACTResponse:
    def __init__(self, ) -> None: ...
    ActLines: list[Teamcenter.Soa.Client.Model.Strong.ACTLine]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class QueryManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindAlignedACTForCAD(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], ActBomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow) -> FindAlignedACTResponse: ...

