import System
import Teamcenter.Services.Internal.Strong.Importexport._2010_04.L10NImportExport
import Teamcenter.Soa.Client.Model
import typing

class ObjectsInfo2:
    def __init__(self, ) -> None: ...
    TranslationsExist: bool
    Locale: str
    Statuses: list[str]
    TransferOptionSet: str
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    TypesPropertiesInfo: list[Teamcenter.Services.Internal.Strong.Importexport._2010_04.L10NImportExport.TypePropertiesInfo]

class L10NImportExport:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportObjectsForTranslation2(self, InputObjectsInfo: ObjectsInfo2) -> Teamcenter.Services.Internal.Strong.Importexport._2010_04.L10NImportExport.ExportObjectsForTranslationResponse: ...

