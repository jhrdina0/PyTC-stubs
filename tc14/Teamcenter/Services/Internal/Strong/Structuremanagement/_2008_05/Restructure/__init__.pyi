import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ReplaceInContextParameter:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision

class Restructure:
    def __init__(self , *args: typing.Any) -> None: ...
    def ReplaceInContext(self, Input: list[ReplaceInContextParameter]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

