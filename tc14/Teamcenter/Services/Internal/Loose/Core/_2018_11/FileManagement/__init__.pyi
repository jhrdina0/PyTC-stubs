import System
import Teamcenter.Soa.Client.Model
import typing

class GetTransientTicketsDownloadInput:
    def __init__(self, ) -> None: ...
    TransientFileWriteTicket: str
    DeleteFlag: bool

class GetTransientTicketsDownloadResponse:
    def __init__(self, ) -> None: ...
    TransientFileReadTickets: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTransientFileTicketsForDownload(self, Tickets: list[GetTransientTicketsDownloadInput]) -> GetTransientTicketsDownloadResponse: ...

