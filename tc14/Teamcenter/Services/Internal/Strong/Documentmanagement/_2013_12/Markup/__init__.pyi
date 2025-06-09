import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MarkupResponse:
    def __init__(self, ) -> None: ...
    Version: str
    Message: str
    Markups: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Markup:
    def __init__(self , *args: typing.Any) -> None: ...
    def LoadMarkups(self, BaseObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, Version: str, Message: str) -> MarkupResponse: ...
    def SaveMarkups(self, BaseObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject, Version: str, Message: str, Markups: str) -> MarkupResponse: ...

