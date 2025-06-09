import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CriteriaInfoOutput:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    SearchCriteriaMap: System.Collections.Hashtable

class GetSearchCriteriaResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    CriteriaInfoOutput: CriteriaInfoOutput

class SearchCriteriaInput:
    def __init__(self, ) -> None: ...
    CriteriaType: int
    IsCreate: bool
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    SearchCriteriaMap: System.Collections.Hashtable

class SearchCriteriaResponse:
    def __init__(self, ) -> None: ...
    SearchCriteriaOutputMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ObjectManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateSearchCriteria(self, CriteriaInputVector: list[SearchCriteriaInput]) -> SearchCriteriaResponse: ...
    def DeleteSearchCriteria(self, CriteriaInput: list[SearchCriteriaInput]) -> SearchCriteriaResponse: ...
    def GetSearchCriteria(self, CriteriaInput: list[SearchCriteriaInput]) -> GetSearchCriteriaResponse: ...

