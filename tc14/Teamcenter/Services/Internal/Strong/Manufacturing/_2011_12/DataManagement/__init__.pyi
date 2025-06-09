import System
import Teamcenter.Soa.Client.Model
import typing

class OccurenceInfo:
    def __init__(self, ) -> None: ...
    OccThreadsChain: list[str]
    StockAbleOccThread: str
    ClientID: str

class OccurrenceIDIC:
    def __init__(self, ) -> None: ...
    ReturnID: str
    ClientID: str

class PostAssignIDICInput:
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    Occurrences: list[OccurenceInfo]

class PostAssignIDICResponse:
    def __init__(self, ) -> None: ...
    OccurrenceIDICs: list[OccurrenceIDIC]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def PostAssignIDICMaker(self, PostAssignInput: list[PostAssignIDICInput]) -> PostAssignIDICResponse: ...

