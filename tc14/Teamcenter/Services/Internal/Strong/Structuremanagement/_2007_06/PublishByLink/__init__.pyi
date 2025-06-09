import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateIDCWindowOutput:
    def __init__(self, ) -> None: ...
    InputIndex: int
    IdcWindow: Teamcenter.Soa.Client.Model.Strong.IDCWindow

class CreateIDCWindowResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreateIDCWindowOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PublishByLink:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateIDCWindowForDesignAsm(self, Comps: list[Teamcenter.Soa.Client.Model.ModelObject]) -> CreateIDCWindowResponse: ...

