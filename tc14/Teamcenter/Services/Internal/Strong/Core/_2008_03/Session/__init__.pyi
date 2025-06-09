import System
import Teamcenter.Soa.Client.Model
import typing

class Session:
    def __init__(self , *args: typing.Any) -> None: ...
    def DisableUserSessionState(self, Names: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

