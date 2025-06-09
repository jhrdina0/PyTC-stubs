import Teamcenter.Services.Internal.Strong.Administration._2013_05.UserManagement
import Teamcenter.Soa.Client.Model
import typing

class ActivateUserInput:
    def __init__(self, ) -> None: ...
    LicenseLevel: int
    LicenseBundle: str
    TargetUser: Teamcenter.Soa.Client.Model.ModelObject
    LicenseServer: str

class UserManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ActivateUsers2(self, ActivateUsers: list[ActivateUserInput]) -> Teamcenter.Services.Internal.Strong.Administration._2013_05.UserManagement.LicenseStatusResponse: ...

