import System
import Teamcenter.Services.Internal.Strong.Rdv._2009_01.VariantManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class NVEMetaExprTokensResponse:
    def __init__(self, ) -> None: ...
    MetaExprs: list[Teamcenter.Services.Internal.Strong.Rdv._2009_01.VariantManagement.MetaExprTokens]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SearchResponse:
    def __init__(self, ) -> None: ...
    PlmxmlFileLocation: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SearchResults:
    def __init__(self, ) -> None: ...
    BackgroundBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    UnconfiguredBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    UnconfigurableBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    UnconfiguredVOOBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def RealignNVEMetaExpressionTokens(self, MetaExprs: list[Teamcenter.Services.Internal.Strong.Rdv._2009_01.VariantManagement.MetaExprTokens]) -> NVEMetaExprTokensResponse: ...
    def ExecuteAdhocSearchWithOverlays(self, DatasetTag: Teamcenter.Soa.Client.Model.ModelObject, ProductRevTag: Teamcenter.Soa.Client.Model.ModelObject, BookMarkStringsToMatch: list[str], BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow, TargetBOMLine: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], VooFlag: bool, SvrTag: Teamcenter.Soa.Client.Model.ModelObject) -> SearchResponse: ...
    def ExecuteSearchWithOverlays(self, BookMarkStringsToMatch: list[str], BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, TargetBOMLine: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], VooFlag: bool) -> SearchResults: ...

