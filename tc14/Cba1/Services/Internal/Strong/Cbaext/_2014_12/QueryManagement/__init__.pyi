import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ActLineInput:
    def __init__(self, ) -> None: ...
    ActLine: Teamcenter.Soa.Client.Model.Strong.ACTLine
    ClientID: str

class BomLineType:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ClientID: str

class BOMSolveInputInfo:
    def __init__(self, ) -> None: ...
    Type: str
    ProductType: str
    VehicleLine: str
    ModelExpression: str
    ModelOption: str

class BoundingBox:
    def __init__(self, ) -> None: ...
    Xmin: float
    Xmax: float
    Ymin: float
    Ymax: float
    Zmin: float
    Zmax: float

class Column:
    def __init__(self, ) -> None: ...
    Name: str
    Datatype: str
    Table: str
    LogicalName: str
    Width: int

class ColumnSet:
    def __init__(self, ) -> None: ...
    Column: list[Column]
    Table: str

class CommonCriteria:
    def __init__(self, ) -> None: ...
    Recordstate: str
    Stream: str
    EffectiveInDate: str
    EffectiveOutDate: str
    EffectiveDate: str
    EffectivePoint: str
    EffectiveInPoint: str
    EffectiveOutPoint: str
    ProductionDate: str
    ProductionPoint: str
    AdditionalCriteriaFields: System.Collections.Hashtable

class RowSet:
    def __init__(self, ) -> None: ...
    Row: list[Row]

class RowColumn:
    def __init__(self, ) -> None: ...
    ColumnSet: ColumnSet
    RowSet: RowSet

class DesignProxyToAlignedPartsInfo:
    def __init__(self, ) -> None: ...
    DesignProxy: Teamcenter.Soa.Client.Model.Strong.TcUsageProxy
    Parts: RowColumn

class DesignToAlignedACTLineInfo:
    def __init__(self, ) -> None: ...
    Design: Teamcenter.Soa.Client.Model.Strong.BOMLine
    PmmACTLine: list[Teamcenter.Soa.Client.Model.Strong.ACTLine]

class DesignToAlignedPartsInfo:
    def __init__(self, ) -> None: ...
    LocalDesign: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    Parts: RowColumn

class DesignToAlignedSolutionsInfo:
    def __init__(self, ) -> None: ...
    Design: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Solutions: RowColumn

class FindAlignedACTLinesForDesignsResponse:
    def __init__(self, ) -> None: ...
    DesignToAlignedACTLineInfos: list[DesignToAlignedACTLineInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindAlignedDesignsForACTResponse:
    def __init__(self, ) -> None: ...
    DesignToAlignedACTLineInfos: list[DesignToAlignedACTLineInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindAlignedDesignsForSolutionsResponse:
    def __init__(self, ) -> None: ...
    SolutionToAlignedDesignInfos: list[SolutionToAlignedDesignInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindAlignedDesignsResponse:
    def __init__(self, ) -> None: ...
    PartToAlignedDesignsInfos: list[PartToAlignedDesignsInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindAlignedPartForProxyResponse:
    def __init__(self, ) -> None: ...
    DesignProxyToAlignedPartsInfos: list[DesignProxyToAlignedPartsInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindAlignedPartsResponse:
    def __init__(self, ) -> None: ...
    DesignToAlignedPartsInfos: list[DesignToAlignedPartsInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindAlignedSolutionsForDesignsResponse:
    def __init__(self, ) -> None: ...
    DesignToAlignedSolutionsInfos: list[DesignToAlignedSolutionsInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LocalDesignsInfo:
    def __init__(self, ) -> None: ...
    LocalDesign: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    IsPrimary: bool
    IsPublished: bool

class PartToAlignedDesignsInfo:
    def __init__(self, ) -> None: ...
    ImpreciseUniqueKey: str
    LocalDesigns: list[LocalDesignsInfo]
    RemoteDesigns: list[RemoteDesignsInfo]

class PreciseEffectivityDetails:
    def __init__(self, ) -> None: ...
    PreciseEffectivityDate: str
    PreciseEffectivityPoint: str

class QueryInfo:
    def __init__(self, ) -> None: ...
    TableName: str
    SelectList: ColumnSet
    TableSpecificQueryCriteria: System.Collections.Hashtable

class RemoteDesignsInfo:
    def __init__(self, ) -> None: ...
    RemoteDesign: Teamcenter.Soa.Client.Model.Strong.TcUsageProxy
    IsPrimary: bool
    IsPublished: bool

class Row:
    def __init__(self, ) -> None: ...
    Value: list[str]
    ClientID: str

class SolutionToAlignedDesignInfo:
    def __init__(self, ) -> None: ...
    ImpreciseUniqueKey: str
    Design: Teamcenter.Soa.Client.Model.Strong.BOMLine

class SpatialSearchBkgCADOccsInfo:
    def __init__(self, ) -> None: ...
    BomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    ToplineItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    TargetBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    BkgBOMLineAndRelatedSolutionsMap: System.Collections.Hashtable
    LayoutWindowFlag: bool

class SpatialSearchCriterias:
    def __init__(self, ) -> None: ...
    TrueShapeFilter: bool
    ValidOverlayFilter: bool
    SearchType: str
    Proximity: float
    AdditionalCriterias: System.Collections.Hashtable
    BoundingBox: BoundingBox
    DesignItemID: str
    ContextItemID: str
    LayoutItemID: str

class SpatialSearchTargetInfo:
    def __init__(self, ) -> None: ...
    TargetLOUs: RowColumn
    TargetSolutions: RowColumn
    TargetLOUSolutionsMap: System.Collections.Hashtable
    TableSpecificQuery: list[QueryInfo]
    BomSolveInput: BOMSolveInputInfo
    CommonCriteria: CommonCriteria
    Reconcile: bool
    IsVisRequested: bool
    RootContext: str

class SpatialSearchInput:
    def __init__(self, ) -> None: ...
    ClientID: str
    TargetDetails: SpatialSearchTargetInfo
    SpatialSearchCriterias: SpatialSearchCriterias

class SpatialSearchOutputInfo:
    def __init__(self, ) -> None: ...
    ClientID: str
    BackgroundLOUs: RowColumn
    BackgroundSolutions: RowColumn
    BackgroundCADOccDetails: list[SpatialSearchBkgCADOccsInfo]
    TargetSolutionToBkgSolutionsMap: System.Collections.Hashtable
    ConflictBOMLineSolutionMap: System.Collections.Hashtable
    DynamicPLMXML: str

class SpatialSearchResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    SpatialSearchResults: list[SpatialSearchOutputInfo]

class QueryManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindAlignedDesignsForACT(self, InputACTData: list[ActLineInput]) -> FindAlignedDesignsForACTResponse: ...
    def ExecuteSpatialSearch(self, Input: list[SpatialSearchInput]) -> SpatialSearchResponse: ...
    def FindAlignedACTLinesForDesigns(self, Designs: list[BomLineType], PreciseEffectivityDetails: PreciseEffectivityDetails) -> FindAlignedACTLinesForDesignsResponse: ...
    def FindAlignedCADForPart(self, PmmParts: RowColumn) -> FindAlignedDesignsResponse: ...
    def FindAlignedDesignsForSolutions(self, Solutions: RowColumn) -> FindAlignedDesignsForSolutionsResponse: ...
    def FindAlignedDrawingForPart(self, PmmParts: RowColumn) -> FindAlignedDesignsResponse: ...
    def FindAlignedPartForCAD(self, Designs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> FindAlignedPartsResponse: ...
    def FindAlignedPartForDrawing(self, Designs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> FindAlignedPartsResponse: ...
    def FindAlignedPartForDrawingProxy(self, DesignProxies: list[Teamcenter.Soa.Client.Model.Strong.TcUsageProxy]) -> FindAlignedPartForProxyResponse: ...
    def FindAlignedSolutionsForDesigns(self, Designs: list[BomLineType]) -> FindAlignedSolutionsForDesignsResponse: ...

