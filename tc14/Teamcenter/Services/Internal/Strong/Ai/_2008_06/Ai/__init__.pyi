import Teamcenter.Services.Strong.Ai._2006_03.Ai
import Teamcenter.Services.Strong.Ai._2007_12.Ai
import Teamcenter.Soa.Client.Model
import typing

class BeginGenerateMonolithicJtResponse:
    def __init__(self, ) -> None: ...
    Ticket: str
    LogFileticket: str
    Request: Teamcenter.Soa.Client.Model.ModelObject
    CurrentState: str
    Data: Teamcenter.Soa.Client.Model.ServiceData

class EndGenerateMonolithicJtResponse:
    def __init__(self, ) -> None: ...
    Ticket: str
    LogFileticket: str
    CurrentState: str
    Data: Teamcenter.Soa.Client.Model.ServiceData

class GenerateMonolithicJtOptions:
    def __init__(self, ) -> None: ...
    ContinueOnError: int
    ProcessIntermediateNodes: int
    RemoteProcessing: bool
    WaitSecondsAtServer: int

class Ai:
    def __init__(self , *args: typing.Any) -> None: ...
    def BeginGenerateMonolithicJt(self, StartingNode: Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef, ItemId: str, RevId: str, Config: Teamcenter.Services.Strong.Ai._2007_12.Ai.Configuration2, Options: GenerateMonolithicJtOptions, ServerMode: int) -> BeginGenerateMonolithicJtResponse: ...
    def EndGenerateMonolithicJt(self, Request: Teamcenter.Soa.Client.Model.ModelObject, ServerMode: int) -> EndGenerateMonolithicJtResponse: ...
    def Invoke(self, MethodName: str, StrIn: str) -> str: ...

