import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateSitesResponse:
    def __init__(self, ) -> None: ...
    Outputs: list[CreateSitesOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SiteInfo:
    def __init__(self, ) -> None: ...
    SiteID: int
    SiteName: str
    AdditionalPropMap: System.Collections.Hashtable

class CreateSitesOutput:
    def __init__(self, ) -> None: ...
    SiteInfo: SiteInfo
    PomIMC: Teamcenter.Soa.Client.Model.Strong.POM_imc

class SiteManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateSites(self, SiteInfos: list[SiteInfo]) -> CreateOrUpdateSitesResponse: ...

