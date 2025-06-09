import Teamcenter.Soa.Client.Model
import typing

class ActivateUserInput:
    def __init__(self, ) -> None: ...
    LicenseLevel: int
    LicenseBundle: str
    TargetUser: Teamcenter.Soa.Client.Model.ModelObject

class LicenseStatus:
    def __init__(self, ) -> None: ...
    NumPurchasedLicenses: int
    NumUsedLicenses: int
    NumPurchasedLicenseBundles: int
    NumUsedLicenseBundles: int

class LicenseStatusResponse:
    def __init__(self, ) -> None: ...
    LicStatus: list[LicenseStatus]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class UserManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ActivateUsers2(self, ActivateUsers: list[ActivateUserInput]) -> LicenseStatusResponse: ...

