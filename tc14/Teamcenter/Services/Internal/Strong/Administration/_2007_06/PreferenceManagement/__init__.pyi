import System
import Teamcenter.Soa.Client.Model
import typing

class InternalContext:
    def __init__(self, ) -> None: ...
    ContextName: str
    Value: list[str]

class InternalPreferenceDefinition:
    def __init__(self, ) -> None: ...
    PreferenceName: str
    PreferenceCategory: str
    PreferenceDescription: str
    PreferenceScope: str
    PreferenceType: str
    IsArray: bool
    IsDisabled: bool

class InternalPreferenceInfo:
    def __init__(self, ) -> None: ...
    PreferenceDefinition: InternalPreferenceDefinition
    ContextInformation: list[InternalContext]

class InternalPreferencesInfo:
    def __init__(self, ) -> None: ...
    PrefsInfo: list[InternalPreferenceInfo]

class PreferenceExportResponse:
    def __init__(self, ) -> None: ...
    FileTicket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PreferenceResponse:
    def __init__(self, ) -> None: ...
    PreferencesArray: list[InternalPreferencesInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PreferencesDeleteInput:
    def __init__(self, ) -> None: ...
    PreferenceScope: str
    PreferenceName: str
    Object: Teamcenter.Soa.Client.Model.ModelObject

class PreferencesExportInput:
    def __init__(self, ) -> None: ...
    PreferenceScope: str
    CategoryNames: list[str]

class PreferencesImportInput:
    def __init__(self, ) -> None: ...
    PreferenceScope: str
    FileTicket: str
    CategoryNames: list[str]
    ImportAction: str

class PreferenceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreatePreferenceCategories(self, CategoryNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeletePreferences(self, DeletePrefs: list[PreferencesDeleteInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ExportPreferences(self, ExportPrefs: PreferencesExportInput) -> PreferenceExportResponse: ...
    def GetModifiedSitePreferences(self) -> PreferenceResponse: ...
    def GetNonSessionPreferences(self, PreferenceScope: str, Object: Teamcenter.Soa.Client.Model.ModelObject) -> PreferenceResponse: ...
    def ImportPreferences(self, ImportPrefs: PreferencesImportInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...

