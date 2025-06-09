import Teamcenter.Soa.Client.Model
import typing

class AddMultiToolCutterResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    StrNewICOUID: str
    StrNewCutterID: str

class DeleteMultiToolCutterResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    LastICOUID: str

class ResourceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddMultiToolCutter(self, StrItemRevUID: str) -> AddMultiToolCutterResponse: ...
    def DeleteMultiToolCutter(self, DeleteICOUID: str) -> DeleteMultiToolCutterResponse: ...

