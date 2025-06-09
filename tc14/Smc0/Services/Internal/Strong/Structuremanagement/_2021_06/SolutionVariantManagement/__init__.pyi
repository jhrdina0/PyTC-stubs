import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateBOMLineVariantRuleResponse:
    def __init__(self, ) -> None: ...
    ChildVariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    IsValidAndComplete: bool
    RequestPreferenceOutput: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SolutionVariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateBOMLineVariantRule(self, BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, Validate: bool, CheckCompleteness: bool, SaveVariantRule: bool, VariantRuleName: str, RequestPreferences: System.Collections.Hashtable) -> CreateBOMLineVariantRuleResponse: ...

