import System
import Teamcenter.Soa.Client.Model
import typing

class BomlinesInfoForValidoverlay:
    def __init__(self, ) -> None: ...
    ShowUnconfiguredVariant: bool
    ShowUnconfiguredBydate: bool
    VariantRuleTag: list[Teamcenter.Soa.Client.Model.ModelObject]
    BackgrndBomlines: list[Teamcenter.Soa.Client.Model.ModelObject]

class ConfigbomlinesInfoForValidoverlay:
    def __init__(self, ) -> None: ...
    BackgrndBomlines: list[Teamcenter.Soa.Client.Model.ModelObject]
    UnconfiguredBomlines: list[Teamcenter.Soa.Client.Model.ModelObject]

class GetValidoverlayBomlineResponse:
    def __init__(self, ) -> None: ...
    ValidoverlayBomlines: list[ConfigbomlinesInfoForValidoverlay]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetValidoverlayBomlinesInfo(self, Input: list[BomlinesInfoForValidoverlay]) -> GetValidoverlayBomlineResponse: ...

