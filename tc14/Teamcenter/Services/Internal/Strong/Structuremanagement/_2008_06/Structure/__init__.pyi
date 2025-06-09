import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CopyRecursivelyResponse:
    def __init__(self, ) -> None: ...
    CreatedIcRevs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    CreatedFutureIcRevs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindHighestFindNumberInExpandResponse:
    def __init__(self, ) -> None: ...
    IncrementNumber: int
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Output: list[FindHighestFindNumberOutputStruct]

class FindHighestFindNumberOutputStruct:
    def __init__(self, ) -> None: ...
    HighestFindNumber: int
    ClientId: str

class FindHighestFindNumInExpandInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Bvr: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    OccType: str

class Structure:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindHighestFindNumberInExpand(self, Input: list[FindHighestFindNumInExpandInput]) -> FindHighestFindNumberInExpandResponse: ...
    def CopyRecursively(self, ObjectToClone: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, CopyActionRulesKey: str, TemplateBOMWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow, WindowOfSelectedLine: Teamcenter.Soa.Client.Model.Strong.BOMWindow, NewName: str, NewDescription: str, NewId: str, NewRevId: str, CopyFutureEffectivities: bool) -> CopyRecursivelyResponse: ...

