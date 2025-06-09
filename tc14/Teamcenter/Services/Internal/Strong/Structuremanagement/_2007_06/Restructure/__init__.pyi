import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class InsertLevelParameter:
    def __init__(self, ) -> None: ...
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ViewType: Teamcenter.Soa.Client.Model.ModelObject
    IsPrecise: bool

class MoveNodeParameter:
    def __init__(self, ) -> None: ...
    NewParent: Teamcenter.Soa.Client.Model.Strong.BOMLine
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class SplitOccurrenceParameter:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Quantity: str

class Restructure:
    def __init__(self , *args: typing.Any) -> None: ...
    def InsertLevel(self, Input: list[InsertLevelParameter]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def MoveNode(self, Input: list[MoveNodeParameter]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SplitOccurrence(self, Input: list[SplitOccurrenceParameter]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveLevel(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

