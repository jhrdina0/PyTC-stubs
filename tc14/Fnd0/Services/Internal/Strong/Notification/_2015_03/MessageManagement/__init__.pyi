import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class UserGroupAliasResponse:
    def __init__(self, ) -> None: ...
    Users: list[Teamcenter.Soa.Client.Model.Strong.User]
    Groups: list[Teamcenter.Soa.Client.Model.Strong.Group]
    AliasLists: list[Teamcenter.Soa.Client.Model.Strong.ImanAliasList]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MessageManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetUserGroupAlias(self) -> UserGroupAliasResponse: ...

