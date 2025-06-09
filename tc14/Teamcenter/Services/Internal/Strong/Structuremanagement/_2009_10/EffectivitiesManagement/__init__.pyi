import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class EffectivitiesInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    EffectivityComponent: Teamcenter.Soa.Client.Model.Strong.Effectivity
    EndItemComponent: Teamcenter.Soa.Client.Model.Strong.Item
    UnitRangeText: str
    Decision: int

class EffectivityGroupInputInfo:
    def __init__(self, ) -> None: ...
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    EffGrpRevisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    ClientId: str

class GetEffectivityGrpListResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    EffGrpRevList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]

class EffectivitiesManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def SetEndItemEffectivityGroups(self, EffectivityGrpInput: list[EffectivityGroupInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateEffectivites(self, EffectivitiesInfo: list[EffectivitiesInputInfo], EffectivityGroupRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetEffectivityGrpRevList(self, BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow) -> GetEffectivityGrpListResponse: ...

