import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ArchiveRestoreResponse:
    def __init__(self, ) -> None: ...
    ReportFileName: str
    ReportFileTicket: str
    ProgRecUid: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetReportTicketResponse:
    def __init__(self, ) -> None: ...
    Ticket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NamesAndValues:
    def __init__(self, ) -> None: ...
    NameStr: str
    ValueStr: str

class ArchiveRestore:
    def __init__(self , *args: typing.Any) -> None: ...
    def ArchiveObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], ExcludeObjects: list[Teamcenter.Soa.Client.Model.ModelObject], SessionOptionsAndValues: list[NamesAndValues]) -> ArchiveRestoreResponse: ...
    def GetReportFileTicket(self, ReportFileName: str) -> GetReportTicketResponse: ...
    def RestoreObjects(self, Objects: list[Teamcenter.Soa.Client.Model.Strong.PublishedObject], SessionOptionsAndValues: list[NamesAndValues]) -> ArchiveRestoreResponse: ...

