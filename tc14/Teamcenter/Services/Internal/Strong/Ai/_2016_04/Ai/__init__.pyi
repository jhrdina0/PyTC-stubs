import Teamcenter.Soa.Client.Model
import typing

class InvokeResponse:
    def __init__(self, ) -> None: ...
    XmlOut: str
    Data: Teamcenter.Soa.Client.Model.ServiceData

class Ai:
    def __init__(self , *args: typing.Any) -> None: ...
    def Invoke2(self, MethodName: str, XmlIn: str) -> InvokeResponse: ...

