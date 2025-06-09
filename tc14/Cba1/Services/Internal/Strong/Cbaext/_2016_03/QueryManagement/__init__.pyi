import Cba1.Services.Internal.Strong.Cbaext._2014_12.QueryManagement
import System
import System.Collections
import typing

class AdditionalFieldQueryCriteria:
    def __init__(self, ) -> None: ...
    FieldQueryCriteriaList: list[FieldQueryCriteria]

class BOMSolveInputInfo:
    def __init__(self, ) -> None: ...
    Type: str
    ProductType: str
    VehicleLine: str
    ModelExpression: str
    ModelOption: str
    RevisionRule: str

class FieldQueryCriteria:
    def __init__(self, ) -> None: ...
    FieldName: str
    TableName: str
    AdditionalCriteriaField: System.Collections.Hashtable

class SpatialSearchTargetInfo:
    def __init__(self, ) -> None: ...
    TargetLOUs: Cba1.Services.Internal.Strong.Cbaext._2014_12.QueryManagement.RowColumn
    TargetSolutions: Cba1.Services.Internal.Strong.Cbaext._2014_12.QueryManagement.RowColumn
    TargetLOUSolutionsMap: System.Collections.Hashtable
    TableSpecificQuery: list[Cba1.Services.Internal.Strong.Cbaext._2014_12.QueryManagement.QueryInfo]
    BomSolveInput: BOMSolveInputInfo
    CommonCriteria: Cba1.Services.Internal.Strong.Cbaext._2014_12.QueryManagement.CommonCriteria
    Reconcile: bool
    IsVisRequested: bool
    RootContext: str

class SpatialSearchInput:
    def __init__(self, ) -> None: ...
    ClientID: str
    TargetDetails: SpatialSearchTargetInfo
    SpatialSearchCriterias: Cba1.Services.Internal.Strong.Cbaext._2014_12.QueryManagement.SpatialSearchCriterias
    AdditionalFieldQueryCriteria: AdditionalFieldQueryCriteria

class QueryManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteSpatialSearch(self, Input: list[SpatialSearchInput]) -> Cba1.Services.Internal.Strong.Cbaext._2014_12.QueryManagement.SpatialSearchResponse: ...

