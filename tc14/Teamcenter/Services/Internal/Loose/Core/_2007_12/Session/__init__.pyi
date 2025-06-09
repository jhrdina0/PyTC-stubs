import System
import Teamcenter.Soa.Client.Model
import typing

class Session:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

