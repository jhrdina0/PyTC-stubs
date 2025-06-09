import System
import Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement
import typing

class PreferenceManagement:
    """
    Interface PreferenceManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RefreshPreferences2(self, PreferenceNames: list[str], IncludePreferenceDescriptions: bool) -> Teamcenter.Services.Strong.Administration._2012_09.PreferenceManagement.GetPreferencesResponse: ...

