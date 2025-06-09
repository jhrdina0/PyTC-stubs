import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AnalyticsData:
    def __init__(self, ) -> None: ...
    IsDataCollectionEnabled: bool
    UseInternalServer: bool
    BurstTimeInterval: int
    AnalyticsExtraInfo: System.Collections.Hashtable

class TCSessionAndAnalyticsInfo:
    def __init__(self, ) -> None: ...
    UserSession: Teamcenter.Soa.Client.Model.ModelObject
    ExtraInfoOut: System.Collections.Hashtable
    AnalyticsData: AnalyticsData
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTCSessionAnalyticsInfo(self, ExtraInfoIn: list[str]) -> TCSessionAndAnalyticsInfo: ...

