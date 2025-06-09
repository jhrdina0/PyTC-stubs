import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ToolAndSupportedLaunchTypeInfo:
    def __init__(self, ) -> None: ...
    Tool: Teamcenter.Soa.Client.Model.Strong.Item
    SupportedLaunchTypes: list[str]

class ToolsForStructureMapResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ValidSimulationTools: list[ToolAndSupportedLaunchTypeInfo]

class SimulationToolLaunch:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetValidToolsForStructureMap(self) -> ToolsForStructureMapResponse: ...

