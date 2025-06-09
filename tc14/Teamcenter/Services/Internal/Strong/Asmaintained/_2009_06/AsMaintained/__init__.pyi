import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ASMBomCompareInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    NumSrcBOMLines: int
    SrcBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    NumTarBOMLines: int
    TarBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    Options: int
    SrcCtxtLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    TarCtxtLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ModeStr: str
    OutputMode: int
    UseBomCompareEngine: bool

class ASMBomCompareOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    NumSrcRetBOMLines: int
    SrcRetBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    NumMatRetBOMLines: int
    TarRetBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    ReportLines: list[str]

class ASMBomCompareResponse:
    def __init__(self, ) -> None: ...
    Output: list[ASMBomCompareOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CreateMROBOMWindowsInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    ObjectForConfigure: Teamcenter.Soa.Client.Model.ModelObject
    MroRevRule: Teamcenter.Soa.Client.Model.Strong.MroRevisionRule

class CreateMROBOMWindowsOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine

class CreateMROBOMWindowsResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreateMROBOMWindowsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetAllAsmOpenUsageInputInfo:
    def __init__(self, ) -> None: ...
    ParentAsMaintainedBOMLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine
    ChildPhysicalPart: Teamcenter.Soa.Client.Model.Strong.PhysicalPart

class GetAllAsmOpenUsageOutput:
    def __init__(self, ) -> None: ...
    UsagePropertyName: str
    UsagePropertyValue: list[str]
    UsageBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class GetAllAsmOpenUsageResponse:
    def __init__(self, ) -> None: ...
    OpenUsageOutput: GetAllAsmOpenUsageOutput
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AsMaintained:
    def __init__(self , *args: typing.Any) -> None: ...
    def AsmBomCompare(self, Info: list[ASMBomCompareInfo]) -> ASMBomCompareResponse: ...
    def CreateMROBOMWindows(self, Info: list[CreateMROBOMWindowsInfo]) -> CreateMROBOMWindowsResponse: ...
    def GetAllAsmOpenUsage(self, UsageInput: list[GetAllAsmOpenUsageInputInfo]) -> GetAllAsmOpenUsageResponse: ...

