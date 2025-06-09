import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AlignmentManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def LinkDesignOccToACTLine(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], ActLines: list[Teamcenter.Soa.Client.Model.Strong.ACTLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

