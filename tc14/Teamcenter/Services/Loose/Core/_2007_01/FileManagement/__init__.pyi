import Teamcenter.Soa.Client.Model
import typing

class GetTransientFileTicketsResponse:
    def __init__(self, ) -> None: ...
    TransientFileTicketInfos: list[TransientFileTicketInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class TransientFileInfo:
    def __init__(self, ) -> None: ...
    FileName: str
    IsBinary: bool
    DeleteFlag: bool

class TransientFileTicketInfo:
    def __init__(self, ) -> None: ...
    TransientFileInfo: TransientFileInfo
    Ticket: str

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTransientFileTicketsForUpload(self, TransientFileInfos: list[TransientFileInfo]) -> GetTransientFileTicketsResponse: ...

