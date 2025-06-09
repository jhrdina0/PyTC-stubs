import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ColumnConfig:
    def __init__(self, ) -> None: ...
    ColumnConfigId: str
    OperationType: str
    Columns: list[ColumnDefInfo]
    TypesToArrange: list[str]

class ColumnConfigInput:
    def __init__(self, ) -> None: ...
    ClientName: str
    HostingClientName: str
    ClientScopeURI: str
    OperationType: str
    ColumnsToExclude: list[str]

class ColumnDefInfo:
    def __init__(self, ) -> None: ...
    DisplayName: str
    AssociatedTypeName: str
    PropertyName: str
    PixelWidth: int
    ColumnOrder: int
    HiddenFlag: bool
    SortPriority: int
    SortDirection: str

class Cursor:
    def __init__(self, ) -> None: ...
    StartUIDLevel: int
    EndUIDLevel: int
    StartUID: str
    EndUID: str
    PageAction: str

class InputObject:
    def __init__(self, ) -> None: ...
    SvSearchForBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    VariantRuleSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    InputVariantRules: list[Teamcenter.Soa.Client.Model.Strong.VariantRule]

class VariantRuleAndSolVariantInfo:
    def __init__(self, ) -> None: ...
    SvItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    SvSourceCofigRelation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    SourceModifiedProps: System.Collections.Hashtable

class SortingInfo:
    def __init__(self, ) -> None: ...
    PropName: str
    ClassName: str
    SortOrder: str

class SVFilterInfo:
    def __init__(self, ) -> None: ...
    HasSolutionVariant: str
    VrValidAndCompleteCheck: str
    SvSourceCategory: str
    ReleaseStatusNameOnVR: str
    GrmRelationTypeName: str

class VariantRulesAndSolVariantsInput:
    def __init__(self, ) -> None: ...
    InputObjects: list[InputObject]
    FilterInfo: list[SVFilterInfo]
    SortingInfo: SortingInfo
    Cursor: Cursor
    PageSize: int
    ColumnConfigInput: ColumnConfigInput

class VariantRulesAndSolVariantsOutput:
    def __init__(self, ) -> None: ...
    OutInfo: list[VariantRulesInfo]
    Cursor: Cursor
    PageSize: int
    ColumnConfigOutput: ColumnConfig
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VariantRulesInfo:
    def __init__(self, ) -> None: ...
    SvSearchForBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    VariantRuleSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    SvrToSolutionVariants: System.Collections.Hashtable

class SolutionVariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetVariantRulesAndSolVariants(self, Input: VariantRulesAndSolVariantsInput) -> VariantRulesAndSolVariantsOutput: ...

