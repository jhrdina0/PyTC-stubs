import Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AspectSearchExpressionIn:
    def __init__(self, ) -> None: ...
    ClientId: str
    Aspects: list[Teamcenter.Soa.Client.Model.Strong.Asp0Aspect]
    LevelsToTraverse: int
    TraverseDown: bool
    EngineeringObjects: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    Schemes: list[Teamcenter.Soa.Client.Model.Strong.Asp0AspectScheme]

class AspectSearchExpressionOut:
    def __init__(self, ) -> None: ...
    ClientId: str
    SearchDef: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchDef

class AspectSearchExpressionResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Expressions: list[AspectSearchExpressionOut]

class ExpandAspectsResponse:
    def __init__(self, ) -> None: ...
    ExpandContent: list[Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement.ExpandResult]
    ChildParentMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AspectManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAspectSearchExpressions(self, ExprInputs: list[AspectSearchExpressionIn]) -> AspectSearchExpressionResponse: ...
    def ExpandAspects(self, AspectExpandInfo: list[Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement.ExpandAspectsInfo], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> ExpandAspectsResponse: ...

