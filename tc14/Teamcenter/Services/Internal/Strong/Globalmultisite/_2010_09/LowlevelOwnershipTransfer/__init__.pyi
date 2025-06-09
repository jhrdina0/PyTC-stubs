import Teamcenter.Services.Internal.Strong.Globalmultisite._2010_02.LowlevelOwnershipTransfer
import typing

class LowlevelOwnershipTransfer:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetObjectsForOwnershipTransfer(self, TcGSMessageId: str, ChangeOwnershipToSite: int, Dryrun: bool, StartDate: str, EndDate: str) -> Teamcenter.Services.Internal.Strong.Globalmultisite._2010_02.LowlevelOwnershipTransfer.ObjectsForOwnershipTransferResponse: ...

