import System
import System.Collections
import Teamcenter.Services.Loose.Core._2007_01.Session
import Teamcenter.Services.Loose.Core._2008_03.Session
import Teamcenter.Soa.Client.Model
import typing

class GetShortcutsResponse:
    def __init__(self, ) -> None: ...
    Favorites: Teamcenter.Services.Loose.Core._2008_03.Session.FavoritesList
    Shortcuts: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LHNNonTcObjectSectionComponent:
    def __init__(self, ) -> None: ...
    NonTcObjects: System.Collections.Hashtable

class LHNSectionComponents:
    def __init__(self, ) -> None: ...
    NonTcObjects: System.Collections.Hashtable
    TcObjects: System.Collections.Hashtable

class LHNTcObjectSectionComponent:
    def __init__(self, ) -> None: ...
    TcObject: Teamcenter.Soa.Client.Model.ModelObject
    Details: System.Collections.Hashtable

class MultiPreferenceResponse2:
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    Preferences: list[ReturnedPreferences2]

class ReturnedPreferences2:
    def __init__(self, ) -> None: ...
    Scope: str
    Category: str
    Description: str
    PrefType: int
    IsArray: bool
    IsDisabled: bool
    Values: list[str]
    Name: str

class Session:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPreferences2(self, PreferenceNames: list[Teamcenter.Services.Loose.Core._2007_01.Session.ScopedPreferenceNames]) -> MultiPreferenceResponse2: ...
    def GetShortcuts(self, ShortcutInputs: System.Collections.Hashtable) -> GetShortcutsResponse: ...

