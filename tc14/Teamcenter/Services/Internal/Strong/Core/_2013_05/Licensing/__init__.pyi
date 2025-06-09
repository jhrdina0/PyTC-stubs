import System
import Teamcenter.Soa.Client.Model
import typing

class GetLicenseBundlesResponse:
    def __init__(self, ) -> None: ...
    LicServerInfo: list[LicenseServerInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LicenseBundleInfo:
    def __init__(self, ) -> None: ...
    LicenseBundleName: str
    BaseFeatureKey: str
    NumberPurchased: int
    ExpirationDate: System.DateTime

class LicenseServerInfo:
    def __init__(self, ) -> None: ...
    LicenseServerName: str
    LicenseBundles: list[LicenseBundleInfo]

class Licensing:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLicenseBundles(self, LicenseServerNames: list[str]) -> GetLicenseBundlesResponse: ...

