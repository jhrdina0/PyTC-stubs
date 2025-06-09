import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MakeUserResponse:
    def __init__(self, ) -> None: ...
    UserOutputMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class UserInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    Email: str
    FirstName: str
    LastName: str
    UserName: str
    AttrInfo: System.Collections.Hashtable

class TenantCreateOption:
    def __init__(self, ) -> None: ...
    TenantName: str
    CadTool: str
    AdminUserInfo: UserInfo
    OnboardInfo: System.Collections.Hashtable

class UserCreateInput:
    def __init__(self, ) -> None: ...
    TenantName: str
    UserInfos: list[UserInfo]
    OnboardInfo: System.Collections.Hashtable

class UserOutput:
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    GroupObject: Teamcenter.Soa.Client.Model.Strong.Group

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def MakeUserAndTenant(self, TenantCreateOption: TenantCreateOption, UserCreateInput: UserCreateInput) -> MakeUserResponse: ...

