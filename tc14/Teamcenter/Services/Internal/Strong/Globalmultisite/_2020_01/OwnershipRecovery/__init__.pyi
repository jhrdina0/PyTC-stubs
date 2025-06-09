import System
import Teamcenter.Soa.Client.Model
import typing

class OtSearchInfo:
    def __init__(self, ) -> None: ...
    TransactionType: str
    SiteId: int
    StartDate: System.DateTime
    EndDate: System.DateTime
    BriefcaseName: str

class OtTransactionInfo:
    def __init__(self, ) -> None: ...
    TransactionId: str
    TransactionType: str
    SiteId: int
    UserId: str
    TransactionDate: System.DateTime
    BriefcaseName: str

class OtTransactionResponse:
    def __init__(self, ) -> None: ...
    OtTransactions: list[OtTransactionInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RecoverOwnershipResponse:
    def __init__(self, ) -> None: ...
    ReportFmsTicket: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class OwnershipRecovery:
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteOtTransaction(self, TransactionId: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def FindOtTransactions(self, OtSearchInfo: OtSearchInfo) -> OtTransactionResponse: ...
    def RecoverOwnership(self, TransactionId: str, DryRun: bool) -> RecoverOwnershipResponse: ...
    def RecoverOwnershipUsingBriefcase(self, BriefcaseUid: str, DryRun: bool) -> RecoverOwnershipResponse: ...

