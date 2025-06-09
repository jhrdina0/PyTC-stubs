import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateMROBOMWindowsInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    ObjectForConfigure: Teamcenter.Soa.Client.Model.ModelObject

class CreateMROBOMWindowsOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine

class CreateMROBOMWindowsResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreateMROBOMWindowsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetAllOpenUsageInput:
    def __init__(self, ) -> None: ...
    ParentAsBuiltBOMLine: Teamcenter.Soa.Client.Model.Strong.AsBuiltBOMLine
    ChildPhysicalPartRevision: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    AllUsages: bool

class GetAllOpenUsageOutput:
    def __init__(self, ) -> None: ...
    PropName: str
    Values: list[str]
    UsageType: list[str]
    ChildBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class GetAllOpenUsageResponse:
    def __init__(self, ) -> None: ...
    GetAllOpenUsageOutput: GetAllOpenUsageOutput
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MROBomCompareInfo:
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

class MROBomCompareOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    NumSrcRetBOMLines: int
    SrcRetBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    NumMatRetBOMLines: int
    MatRetBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    ReportLines: list[str]

class MROBomCompareResponse:
    def __init__(self, ) -> None: ...
    Output: list[MROBomCompareOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AsBuilt:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateMROBOMWindows(self, Info: list[CreateMROBOMWindowsInfo]) -> CreateMROBOMWindowsResponse: ...
    def GetAllOpenUsages(self, GetAllOpenUsageInput: list[GetAllOpenUsageInput]) -> GetAllOpenUsageResponse: ...
    def MroBomCompare(self, Info: list[MROBomCompareInfo]) -> MROBomCompareResponse: ...

