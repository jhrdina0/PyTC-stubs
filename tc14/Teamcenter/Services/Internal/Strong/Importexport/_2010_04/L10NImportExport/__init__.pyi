import System
import Teamcenter.Soa.Client.Model
import typing

class ExportObjectsForTranslationResponse:
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Soa.Client.Model.ServiceData
    Tickets: list[LocaleTicketInfo]

class LocaleTicketInfo:
    def __init__(self, ) -> None: ...
    Locale: str
    Ticket: str

class ObjectsInfo:
    def __init__(self, ) -> None: ...
    TranslationsExist: bool
    Locale: str
    Statuses: list[str]
    TransferMode: str
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    TypesPropertiesInfo: list[TypePropertiesInfo]

class TransientFileTicketStatusInfo:
    def __init__(self, ) -> None: ...
    TransientFileTicket: str
    LocalizationStatus: str

class TypePropertiesInfo:
    def __init__(self, ) -> None: ...
    TypeName: str
    PropertyNames: list[str]

class L10NImportExport:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportObjectsForTranslation(self, InpuInfo: ObjectsInfo) -> ExportObjectsForTranslationResponse: ...
    def FilterObjectsForTranslation(self, InputInfo: ObjectsInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ImportTranslations(self, FileInfo: list[TransientFileTicketStatusInfo]) -> ExportObjectsForTranslationResponse: ...

