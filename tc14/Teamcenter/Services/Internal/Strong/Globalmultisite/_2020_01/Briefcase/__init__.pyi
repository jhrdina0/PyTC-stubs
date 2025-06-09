import System
import Teamcenter.Soa.Client.Model
import typing

class AddMarkOTResponse:
    def __init__(self, ) -> None: ...
    SuccessInfo: list[MarkOTInfo]
    FailureInfo: list[MarkOTErrorInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetObjectsLockInfoResponse:
    def __init__(self, ) -> None: ...
    LockInfo: list[MarkOTLockInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MarkOTErrorInfo:
    def __init__(self, ) -> None: ...
    ObjectUID: str
    ErrorInfo: list[NameAndValue]

class MarkOTInfo:
    def __init__(self, ) -> None: ...
    ObjectUID: str
    TargetSiteId: int
    UserId: str
    ParentUID: str

class MarkOTLockInfo:
    def __init__(self, ) -> None: ...
    ObjectUID: str
    LockUserId: str
    LockTime: str
    LockNodeName: str

class NameAndValue:
    def __init__(self, ) -> None: ...
    ElementName: str
    ElementValue: str

class QueryMarkOTResponse:
    def __init__(self, ) -> None: ...
    MarkInfo: list[MarkOTInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RemoveMarkOTResponse:
    def __init__(self, ) -> None: ...
    SuccessInfo: list[str]
    FailureInfo: list[MarkOTErrorInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Briefcase:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddMarkOTForCurrentUser(self, Objects: list[str], TargetSiteId: int, AppId: str) -> AddMarkOTResponse: ...
    def GetObjectsLockInfo(self, Objects: list[str]) -> GetObjectsLockInfoResponse: ...
    def QueryMarkOT(self, Objects: list[str], UserId: str, TargetSiteId: int, NeedHelperObjects: bool, AppId: str) -> QueryMarkOTResponse: ...
    def RemoveMarkOTForCurrentUser(self, Objects: list[str], AppId: str) -> RemoveMarkOTResponse: ...

