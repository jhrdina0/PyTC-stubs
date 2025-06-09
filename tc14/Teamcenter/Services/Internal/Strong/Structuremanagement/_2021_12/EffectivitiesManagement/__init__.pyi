import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class EffectivitiesInputInfo2:
    def __init__(self, ) -> None: ...
    ClientId: str
    EffectivityComponent: Teamcenter.Soa.Client.Model.Strong.Effectivity
    EndItemComponent: Teamcenter.Soa.Client.Model.Strong.Item
    DateRange: list[System.DateTime]
    OpenEndedStatus: int
    Decision: int

class EffectivitiesManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateDateEffectivities(self, EffectivitiesInfo: list[EffectivitiesInputInfo2], EffectivityGroupRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...

