import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class GetTCSessionInfoResponse:
    def __init__(self, ) -> None: ...
    ServerVersion: str
    TransientVolRootDir: str
    IsInV7Mode: bool
    ModuleNumber: int
    User: Teamcenter.Soa.Client.Model.ModelObject
    Group: Teamcenter.Soa.Client.Model.ModelObject
    Role: Teamcenter.Soa.Client.Model.ModelObject
    TcVolume: Teamcenter.Soa.Client.Model.ModelObject
    Project: Teamcenter.Soa.Client.Model.ModelObject
    WorkContext: Teamcenter.Soa.Client.Model.ModelObject
    Site: Teamcenter.Soa.Client.Model.ModelObject
    Bypass: bool
    Journaling: bool
    AppJournaling: bool
    SecJournaling: bool
    AdmJournaling: bool
    Privileged: bool
    IsPartBOMUsageEnabled: bool
    IsSubscriptionMgrEnabled: bool
    TextInfos: list[TextInfo]
    ExtraInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MultiPreferencesResponse:
    def __init__(self, ) -> None: ...
    Preferences: list[ReturnedPreferences]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ReturnedPreferences:
    def __init__(self, ) -> None: ...
    Name: str
    Scope: str
    Values: list[str]

class ScopedPreferenceNames:
    def __init__(self, ) -> None: ...
    Scope: str
    Names: list[str]

class TextInfo:
    def __init__(self, ) -> None: ...
    RealName: str
    DisplayName: str

class Session:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPreferences(self, RequestedPrefs: list[ScopedPreferenceNames]) -> MultiPreferencesResponse: ...
    def GetTCSessionInfo(self) -> GetTCSessionInfoResponse: ...
    def SetObjectPropertyPolicy(self, PolicyName: str) -> bool: ...

