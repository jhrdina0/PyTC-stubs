import System
import Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport
import Teamcenter.Soa.Client.Model
import typing

class TransformDataResponse:
    def __init__(self, ) -> None: ...
    OutputFileTicket: str
    LogFileTicket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ImportExport:
    def __init__(self , *args: typing.Any) -> None: ...
    def TransformData(self, InputFileTickets: list[str], RuleFileNamesOrTickets: list[str], SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> TransformDataResponse: ...

