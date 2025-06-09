import System
import Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport
import Teamcenter.Soa.Client.Model
import typing

class KeywordImportOptions:
    def __init__(self, ) -> None: ...
    ImportOptions: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportExportOptions]
    KeywordImportRules: list[KeywordImportRule]

class ImportDocumentInputData:
    def __init__(self, ) -> None: ...
    ClientId: str
    TransientFileWriteTicket: str
    ChildSpecElementType: str
    SpecificationType: str
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    KeywordImportOptions: KeywordImportOptions
    SpecDesc: str

class KeywordImporCondition:
    def __init__(self, ) -> None: ...
    OpType: str
    Keyword: str

class KeywordImportRule:
    def __init__(self, ) -> None: ...
    TargetChildType: str
    ConditionProcessingType: str
    KeywordImportConditions: list[KeywordImporCondition]

class FileImportExport:
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportDocumentOffline(self, Inputs: list[ImportDocumentInputData]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportFromApplicationResponse1: ...

