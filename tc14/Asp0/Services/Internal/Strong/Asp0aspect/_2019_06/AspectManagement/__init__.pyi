import Asp0.Services.Internal.Strong.Asp0aspect._2018_06.AspectManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeSearchOptions:
    def __init__(self, ) -> None: ...
    SortAttribute: str
    SortOrder: str

class ExpandAspectsInfo:
    def __init__(self, ) -> None: ...
    StartingNodes: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    ExpansionSemantic: int
    ExpandOptionsFlags: System.Collections.Hashtable
    ExpandOptions: System.Collections.Hashtable
    AttributeSortOptions: list[AttributeSearchOptions]
    LevelsToExpand: int

class AspectManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandAspects(self, AspectExpandInfos: list[ExpandAspectsInfo], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Asp0.Services.Internal.Strong.Asp0aspect._2018_06.AspectManagement.ExpandAspectsResponse: ...

