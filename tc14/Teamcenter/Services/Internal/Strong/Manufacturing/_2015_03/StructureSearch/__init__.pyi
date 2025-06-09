import System
import Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch
import Teamcenter.Soa.Client.Model
import typing

class GetSearchCrieriaFromRecipeResp:
    def __init__(self, ) -> None: ...
    CriteriaElements: list[SearchCriteriaElement]
    AdditionalInfo: Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.AdditionalInfo
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SearchCriteriaElement:
    def __init__(self, ) -> None: ...
    FeatureType: str
    LogicalOperator: str
    RelatedObjs: list[SearchCriteriaRelatedObject]
    SearchCriteria: list[Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.KeyValuePair]

class SearchCriteriaRelatedObject:
    def __init__(self, ) -> None: ...
    ConditionType: str
    ConnectedObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    MatchType: str
    WithHierarchy: bool

class StructureSearch:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSearchCriteriaFromRecipe(self, Recipes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetSearchCrieriaFromRecipeResp: ...

