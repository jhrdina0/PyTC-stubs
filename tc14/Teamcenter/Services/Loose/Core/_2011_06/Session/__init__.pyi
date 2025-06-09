import System
import System.Collections
import Teamcenter.Schemas.Soa._2011_06.Metamodel
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Common
import typing

class ClientCacheInfo:
    def __init__(self, ) -> None: ...
    Features: list[Feature]
    PartialErrors: Teamcenter.Soa.Client.Model.PartialErrors

class Credentials:
    def __init__(self, ) -> None: ...
    User: str
    Password: str
    Group: str
    Role: str
    Locale: str
    Descrimator: str

class Feature:
    def __init__(self, ) -> None: ...
    Name: str
    CacheTickets: System.Collections.Hashtable

class LoginResponse:
    def __init__(self, ) -> None: ...
    ServerInfo: System.Collections.Hashtable
    PartialErrors: Teamcenter.Soa.Client.Model.PartialErrors

class Session:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetClientCacheData(self, Features: list[str]) -> ClientCacheInfo: ...
    def GetTypeDescriptions(self, TypeNames: list[str]) -> Teamcenter.Schemas.Soa._2011_06.Metamodel.TypeSchema: ...
    def Login(self, Credentials: Credentials) -> LoginResponse: ...
    def LoginSSO(self, Credentials: Credentials) -> LoginResponse: ...
    def UpdateObjectPropertyPolicy(self, PolicyID: str, AddProperties: list[Teamcenter.Soa.Common.PolicyType], RemoveProperties: list[Teamcenter.Soa.Common.PolicyType]) -> str: ...

