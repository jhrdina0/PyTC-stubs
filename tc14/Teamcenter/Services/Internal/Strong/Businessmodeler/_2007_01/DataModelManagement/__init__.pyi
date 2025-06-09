import System
import Teamcenter.Soa.Client.Model
import typing

class ExportDataModelResponse:
    def __init__(self, ) -> None: ...
    ModelXmlFileTicket: str
    LogFileTicket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ImportDataModelResponse:
    def __init__(self, ) -> None: ...
    LogFileTickets: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataModelManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportDataModel(self, Mode: str) -> ExportDataModelResponse: ...
    def ImportDataModel(self, CustTemplateFileTicket: str, CustDependencyFileTicket: str, UpdateOption: str, RunMode: str) -> ImportDataModelResponse: ...

