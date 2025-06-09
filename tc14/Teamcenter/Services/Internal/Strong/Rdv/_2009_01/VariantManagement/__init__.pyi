import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddDesignToProductResponse:
    def __init__(self, ) -> None: ...
    NewOcc: list[Teamcenter.Soa.Client.Model.ModelObject]
    NewOccType: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CompMeapnAndBomLine:
    def __init__(self, ) -> None: ...
    ChildMeapn: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine

class CompMeapnGcidAndDesc:
    def __init__(self, ) -> None: ...
    Gcid: str
    Desc: str
    ChildMeapn: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode

class GetABandABEInputInfo:
    def __init__(self, ) -> None: ...
    Gcid: str
    TopArchTag: Teamcenter.Soa.Client.Model.Strong.Item
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow

class GetABandABEResponse:
    def __init__(self, ) -> None: ...
    CompsApnAndGcid: list[CompMeapnGcidAndDesc]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetAbeBomlineChildComponentsResponse:
    def __init__(self, ) -> None: ...
    ComponentsApnAndBomLines: list[CompMeapnAndBomLine]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetAbeChildComponentsInputInfo:
    def __init__(self, ) -> None: ...
    TopLevelItem: Teamcenter.Soa.Client.Model.Strong.Item
    MeApn: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow

class GetAbeMeapnChildComponentsResponse:
    def __init__(self, ) -> None: ...
    ComponentsApnAndGcid: list[CompMeapnGcidAndDesc]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MetaExprTokens:
    def __init__(self, ) -> None: ...
    Tokens: list[NVEMetaToken]

class NVEMetaExpressionResponse:
    def __init__(self, ) -> None: ...
    MetaExprs: list[MetaExprTokens]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NVEReference:
    def __init__(self, ) -> None: ...
    NveType: str
    NveName: str
    Nve: Teamcenter.Soa.Client.Model.Strong.NamedVariantExpression

class NVEMetaToken:
    def __init__(self, ) -> None: ...
    TokenType: str
    NveRef: NVEReference

class ValidateNVEMetaExprResponse:
    def __init__(self, ) -> None: ...
    XoCharts: list[XOChartData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class XOChartData:
    def __init__(self, ) -> None: ...
    NoOfRows: int
    NoOfColumns: int
    ColHeaderExprStrs: list[str]
    TableChars: list[int]

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddDesignToProduct(self, Component: Teamcenter.Soa.Client.Model.ModelObject, IaRev: Teamcenter.Soa.Client.Model.ModelObject, ProdRevs: list[Teamcenter.Soa.Client.Model.ModelObject], ArchApn: Teamcenter.Soa.Client.Model.ModelObject, Lous: list[Teamcenter.Soa.Client.Model.ModelObject], NoRequestedOccs: int, MetaExpr: list[NVEMetaToken], Validate: bool) -> AddDesignToProductResponse: ...
    def GetApnComponents(self, Inputs: GetABandABEInputInfo) -> GetABandABEResponse: ...
    def GetArchbreakdownBomlineChildComponents(self, Inputs: GetAbeChildComponentsInputInfo) -> GetAbeBomlineChildComponentsResponse: ...
    def GetArchbreakdownMeapnChildComponents(self, Inputs: GetAbeChildComponentsInputInfo) -> GetAbeMeapnChildComponentsResponse: ...
    def ReplaceDesignInProduct(self, Component: Teamcenter.Soa.Client.Model.ModelObject, BomlinesToReplace: list[Teamcenter.Soa.Client.Model.ModelObject], ProdRevs: list[Teamcenter.Soa.Client.Model.ModelObject], ArchApn: Teamcenter.Soa.Client.Model.ModelObject, Lous: list[Teamcenter.Soa.Client.Model.ModelObject], MetaExpr: list[NVEMetaToken], Validate: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ValidateNVEMetaExpressions(self, MetaExprs: list[MetaExprTokens]) -> ValidateNVEMetaExprResponse: ...
    def ApplyNVEMetaExpression(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], MetaExpr: list[NVEMetaToken], Validate: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AskNVEMetaExpression(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> NVEMetaExpressionResponse: ...
    def ReapplyNVEMetaExpressions(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Validate: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

