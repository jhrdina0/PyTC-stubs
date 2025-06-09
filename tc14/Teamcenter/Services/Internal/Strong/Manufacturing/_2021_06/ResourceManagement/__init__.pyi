import System
import Teamcenter.Soa.Client.Model
import typing

class GuidedComponentSearchForOccResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    MatchingClasses: list[MatchingClass]
    IcoUids: list[str]
    CpUids: list[str]
    DefaultClassId: str

class MatchingClass:
    def __init__(self, ) -> None: ...
    ClassID: str
    MatchingIcoCount: int

class ResourceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GuidedComponentSearchForOccurrence(self, OccUID: str) -> GuidedComponentSearchForOccResponse: ...

