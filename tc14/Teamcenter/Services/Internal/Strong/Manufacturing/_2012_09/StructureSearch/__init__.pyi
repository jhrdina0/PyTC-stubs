import System
import Teamcenter.Soa.Client.Model
import typing

class MapSrchCriteriaToLinesInputInfo:
    def __init__(self, ) -> None: ...
    Criteria: Teamcenter.Soa.Client.Model.ModelObject
    Contexts: list[Teamcenter.Soa.Client.Model.ModelObject]

class MapSrchCriteriaToLinesResponse:
    def __init__(self, ) -> None: ...
    Output: list[SrchCriteriaToLinesMap]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SaveOGLinesInSrchCriteriaInputInfo:
    def __init__(self, ) -> None: ...
    SelectedNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    UnselectedNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ScopeAttribute: bool

class SaveOGLinesInSrchCriteriaResponse:
    def __init__(self, ) -> None: ...
    SrchCriterias: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SrchCriteriaToLinesMap:
    def __init__(self, ) -> None: ...
    SrchCriteria: Teamcenter.Soa.Client.Model.ModelObject
    SelectedNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    UnselectedNodes: list[Teamcenter.Soa.Client.Model.ModelObject]

class StructureSearch:
    def __init__(self , *args: typing.Any) -> None: ...
    def MapSrchCriteriaToLines(self, Inputs: list[MapSrchCriteriaToLinesInputInfo]) -> MapSrchCriteriaToLinesResponse: ...
    def SaveOGLinesInSrchCriteria(self, Inputs: list[SaveOGLinesInSrchCriteriaInputInfo]) -> SaveOGLinesInSrchCriteriaResponse: ...

