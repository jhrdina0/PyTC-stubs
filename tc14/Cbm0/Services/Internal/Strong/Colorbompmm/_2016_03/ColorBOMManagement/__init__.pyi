import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class QueryRuleInput:
    def __init__(self, ) -> None: ...
    ProductContext: Teamcenter.Soa.Client.Model.Strong.Cfg0ProductItem
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    QueryCriteria: System.Collections.Hashtable
    LessFinishParts: list[str]
    ColorRules: list[Teamcenter.Soa.Client.Model.Strong.Cbm0ColorRule]

class QueryRuleResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    QueryRuleOutput: list[Teamcenter.Soa.Client.Model.Strong.Cbm0ColorRule]

class ColorBOMManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryColorRules(self, QueryInput: QueryRuleInput) -> QueryRuleResponse: ...

