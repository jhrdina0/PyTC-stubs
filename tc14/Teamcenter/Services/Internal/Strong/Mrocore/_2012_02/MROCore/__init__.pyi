import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetLotsforItemInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    Item: Teamcenter.Soa.Client.Model.Strong.Item

class GetLotsforItemOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Lots: list[Teamcenter.Soa.Client.Model.Strong.Lot]

class GetLotsforItemResponse:
    def __init__(self, ) -> None: ...
    Output: list[GetLotsforItemOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MROCore:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLotsforItem(self, Inputs: list[GetLotsforItemInputInfo]) -> GetLotsforItemResponse: ...

