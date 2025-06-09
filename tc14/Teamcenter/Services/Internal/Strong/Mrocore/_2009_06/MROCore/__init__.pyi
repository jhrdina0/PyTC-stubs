import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DisplayUtilizationInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    PhysicalPart: Teamcenter.Soa.Client.Model.Strong.PhysicalPart
    TillDate: System.DateTime

class DisplayUtilizationOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Output: list[Teamcenter.Soa.Client.Model.Strong.Utilization]

class DisplayUtilizationResponse:
    def __init__(self, ) -> None: ...
    Output: list[DisplayUtilizationOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MROCore:
    def __init__(self , *args: typing.Any) -> None: ...
    def DisplayUtilization(self, InputInfo: list[DisplayUtilizationInfo]) -> DisplayUtilizationResponse: ...

