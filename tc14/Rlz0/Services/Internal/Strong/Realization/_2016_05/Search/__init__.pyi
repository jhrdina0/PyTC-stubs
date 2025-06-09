import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SearchExpression:
    def __init__(self, ) -> None: ...
    SearchExpressions: list[Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef]
    DoTrushapeRefinement: bool

class SearchExpressionSet:
    def __init__(self, ) -> None: ...
    SearchOperator: str
    SearchExpression: SearchExpression
    SearchExpressionSets: list[SearchExpressionSet]

class SearchOptions:
    def __init__(self, ) -> None: ...
    SortAttributes: list[str]
    DefaultLoadCount: int
    SortOrder: str

class SearchScope:
    def __init__(self, ) -> None: ...
    Composition: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    ObjectTypes: list[str]
    RecipeContainer: Teamcenter.Soa.Client.Model.ModelObject

class SearchRecipe:
    def __init__(self, ) -> None: ...
    Scope: SearchScope
    SearchExpression: SearchExpressionSet

class SearchResponse:
    def __init__(self, ) -> None: ...
    SearchResults: System.Collections.Hashtable
    Finished: bool
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Search:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteSearchInComposition(self, Recipe: SearchRecipe, Options: SearchOptions) -> SearchResponse: ...

