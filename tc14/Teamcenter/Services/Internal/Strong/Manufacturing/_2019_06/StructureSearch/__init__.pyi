import System
import System.Collections
import Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class PartsInProximityOutput:
    def __init__(self, ) -> None: ...
    ProximityDistance: float
    FeatureToPartsInProximity: System.Collections.Hashtable
    AdditionalInfoOut: Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.AdditionalInfo

class PartsInProximityResponse:
    def __init__(self, ) -> None: ...
    PartsInProximityOut: list[PartsInProximityOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ProximityCriteriaInput:
    def __init__(self, ) -> None: ...
    ProximityDistance: float
    MfgFeatureLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    AdditionalInfoIn: Teamcenter.Services.Strong.Manufacturing._2014_12.StructureSearch.AdditionalInfo

class StructureSearch:
    def __init__(self , *args: typing.Any) -> None: ...
    def SearchPartsInProximityOfMFGFeatures(self, CriteriaInput: list[ProximityCriteriaInput]) -> PartsInProximityResponse: ...

