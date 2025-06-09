import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class PSForPMMInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    SelectedLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class ObjectManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdatePSFromPMM(self, PsForPMMInput: list[PSForPMMInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

