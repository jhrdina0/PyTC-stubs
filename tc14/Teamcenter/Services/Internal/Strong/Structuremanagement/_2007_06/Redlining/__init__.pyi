import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Redlining:
    def __init__(self , *args: typing.Any) -> None: ...
    def RevertAllPendingEdits(self, Windows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RevertPendingEdits(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

