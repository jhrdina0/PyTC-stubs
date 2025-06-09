import Cae0.Services.Internal.Strong.Simproc._2014_12.SimProcessConfigurationManagement
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CAEToolConfigInfo2:
    def __init__(self, ) -> None: ...
    ToolBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ParentToolBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ToolName: str
    ToolItemId: str
    ToolItemRevId: str
    ToolType: str
    TabObjects: list[Cae0.Services.Internal.Strong.Simproc._2014_12.SimProcessConfigurationManagement.CAEToolTabConfigInfo]

class SimProcessConfigurationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CloneTool2(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], CloneName: str, CloneItemId: str, CloneItemRevId: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateToolObjects2(self, ToolObjects: list[CAEToolConfigInfo2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetToolBOMProperties2(self, TabIdentifiers: list[str], ReleasedToolsOnly: bool) -> Cae0.Services.Internal.Strong.Simproc._2014_12.SimProcessConfigurationManagement.CAEToolBOMPropStructResponse: ...
    def UnreleaseTools(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], IsUnreleaseAll: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

