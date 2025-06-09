import Teamcenter.Soa.Client.Model
import typing

class LicAdminInput:
    def __init__(self, ) -> None: ...
    FeatureKey: str
    LicensingAction: str

class Session:
    def __init__(self , *args: typing.Any) -> None: ...
    def LicenseAdmin(self, LicAdminInput: list[LicAdminInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

