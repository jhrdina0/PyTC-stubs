import System
import Teamcenter.Soa.Client.Model
import typing

class AutoPositionComponentByCSYSResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    PossibleSourceCSYSs: list[AutoPositioningOutput]
    PossibleTargetCSYSs: list[AutoPositioningOutput]

class AutoPositioningOutput:
    def __init__(self, ) -> None: ...
    StrCSYSBOMLine: str
    StrCSYSBOMLineName: str

class ResourceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AutoPositionComponentByCSYS(self, StrSourceBOMLines: list[str], StrTargetBOMLine: str, StrSourceCSYS: str, StrTargetCSYS: str) -> AutoPositionComponentByCSYSResponse: ...

