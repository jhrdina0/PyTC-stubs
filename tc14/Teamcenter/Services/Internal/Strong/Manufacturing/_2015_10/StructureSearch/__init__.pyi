import System
import System.Collections
import Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch
import Teamcenter.Soa.Client.Model
import typing

class EquivalenceResult:
    def __init__(self, ) -> None: ...
    EquivalenceResults: System.Collections.Hashtable

class FindCPCResponse:
    def __init__(self, ) -> None: ...
    FoundCPCs: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindEquivalentLinesIn:
    def __init__(self, ) -> None: ...
    SourceLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    TargetScopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    IsSourceAScope: bool
    SourceClosureRule: str
    SearchCriteria: int
    AdditionalInfo: Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.AdditionalInfo

class FindEquivalentLinesResp:
    def __init__(self, ) -> None: ...
    EquivalenceResults: list[EquivalenceResult]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AdditionalInfo: Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.AdditionalInfo

class StructureSearch:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindCollabPlanningContext(self, InputScopes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> FindCPCResponse: ...
    def FindEquivalentLines(self, SearchInputs: list[FindEquivalentLinesIn]) -> FindEquivalentLinesResp: ...

