import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class GetValidCriteriaResponse:
    def __init__(self, ) -> None: ...
    Criteriamap: list[System.Collections.Hashtable]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ValidCriteriaInput:
    def __init__(self, ) -> None: ...
    Sourcescope: list[Teamcenter.Soa.Client.Model.ModelObject]
    Targetscope: list[Teamcenter.Soa.Client.Model.ModelObject]

class StructureVerification:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetValidCriteria(self, Inputscope: list[ValidCriteriaInput]) -> GetValidCriteriaResponse: ...

