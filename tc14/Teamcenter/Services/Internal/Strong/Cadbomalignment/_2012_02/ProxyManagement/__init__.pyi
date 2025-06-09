import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class PersistentProxyResponse:
    def __init__(self, ) -> None: ...
    ProxyVector: list[Teamcenter.Soa.Client.Model.Strong.Cba0PersistentProxy]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PmmObjectInfo:
    def __init__(self, ) -> None: ...
    PmmObjectType: str
    PmmObjectId: str
    QueryCriteria: System.Collections.Hashtable

class ProxyManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreatePMMPersistentProxy(self, InputData: list[PmmObjectInfo]) -> PersistentProxyResponse: ...
    def SavePMMPersistentProxy(self, InputData: list[Teamcenter.Soa.Client.Model.Strong.Cba0PersistentProxy]) -> PersistentProxyResponse: ...

