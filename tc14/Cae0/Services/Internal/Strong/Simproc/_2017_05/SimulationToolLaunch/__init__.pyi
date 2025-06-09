import System
import Teamcenter.Soa.Client.Model
import typing

class ExportObjectsToPLMXMLResponse:
    def __init__(self, ) -> None: ...
    XmlAndLogFileTickets: list[FileTicket]
    NamedRefFileTickets: list[FileTicket]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FileTicket:
    def __init__(self, ) -> None: ...
    Ticket: str
    FileName: str

class SimulationToolLaunch:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportObjectsToPLMXMLForToolLaunch(self, PlmxmlFileName: str, TransferMode: str, ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject], CheckOutOnExport: bool, ToolName: str, LogFileTickets: list[str]) -> ExportObjectsToPLMXMLResponse: ...

