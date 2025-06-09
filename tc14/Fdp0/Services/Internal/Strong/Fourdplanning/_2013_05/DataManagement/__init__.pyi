import System
import Teamcenter.Soa.Client.Model
import typing

class NamingInput:
    def __init__(self, ) -> None: ...
    MatchSourceName: bool
    StartNum: int
    Prefix: str
    Suffix: str

class AutomaticProcessCreationInfo:
    def __init__(self, ) -> None: ...
    SourceTasks: list[Teamcenter.Soa.Client.Model.ModelObject]
    ConsiderNewRoot: bool
    Target: Teamcenter.Soa.Client.Model.ModelObject
    NewObjectType: str
    NamingInput: NamingInput

class AutomaticProcessCreationResponse:
    def __init__(self, ) -> None: ...
    LogFileTicket: str
    LogFileName: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AutomaticProcessCreation(self, Input: AutomaticProcessCreationInfo) -> AutomaticProcessCreationResponse: ...

