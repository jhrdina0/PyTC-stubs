import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class PropertyData:
    def __init__(self, ) -> None: ...
    PropertyName: str
    Values: list[str]
    DataType: str

class SyncMasterAndAlternativeInputInfo:
    def __init__(self, ) -> None: ...
    SyncStructsInfo: list[SyncStructsInfo]
    SyncParams: System.Collections.Hashtable

class SyncMasterAndAlternativeResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    SyncResult: list[SyncResult]

class SyncResult:
    def __init__(self, ) -> None: ...
    Source: Teamcenter.Soa.Client.Model.ModelObject
    Target: Teamcenter.Soa.Client.Model.ModelObject
    ResultData: list[PropertyData]

class SyncStructsInfo:
    def __init__(self, ) -> None: ...
    Target: list[Teamcenter.Soa.Client.Model.ModelObject]
    Source: list[Teamcenter.Soa.Client.Model.ModelObject]

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def SyncMasterAndAlternative(self, SyncMasterAndAlternativeInputInfo: SyncMasterAndAlternativeInputInfo) -> SyncMasterAndAlternativeResponse: ...

