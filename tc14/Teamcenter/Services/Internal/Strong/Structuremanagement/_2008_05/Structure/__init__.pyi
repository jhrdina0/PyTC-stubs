import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BOMLinePair:
    def __init__(self, ) -> None: ...
    Source: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Target: Teamcenter.Soa.Client.Model.Strong.BOMLine

class Structure:
    def __init__(self , *args: typing.Any) -> None: ...
    def SyncAlignedOccurrences(self, Input: list[BOMLinePair]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

