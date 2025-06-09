import Teamcenter.Soa.Client.Model
import typing

class ObjectsForOwnershipTransferResponse:
    def __init__(self, ) -> None: ...
    FileFmsTickets: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class TransferOwnershipResponse:
    def __init__(self, ) -> None: ...
    FileFmsTickets: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class UpdateOwnershipTransferResponse:
    def __init__(self, ) -> None: ...
    FileFmsTickets: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LowlevelOwnershipTransfer:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetObjectsForOwnershipTransfer(self, TcGSMessageId: str, ChangeOwnershipToSite: int, Dryrun: bool) -> ObjectsForOwnershipTransferResponse: ...
    def TransferOwnership(self, TcGSMessageId: str, Dryrun: bool, IsSrcSiteExtinct: bool, FmsTicketOfObjs: str) -> TransferOwnershipResponse: ...
    def UpdateOwnershipTransfer(self, TcGSMessageId: str, ChangeOwnershipToSite: int, Dryrun: bool, IsSrcSiteExtinct: bool, FmsTicketOfObjs: str) -> UpdateOwnershipTransferResponse: ...

