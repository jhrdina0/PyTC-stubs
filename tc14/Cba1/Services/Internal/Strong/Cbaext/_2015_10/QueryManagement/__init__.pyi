import Cba1.Services.Internal.Strong.Cbaext._2014_12.QueryManagement
import System
import Teamcenter.Soa.Client.Model.Strong
import typing

class PreciseEffectivityDetails:
    def __init__(self, ) -> None: ...
    PreciseEffectivityDate: str
    PreciseEffectivityPoint: str
    DbEQueryStream: str

class QueryManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindAlignedACTLinesForDesigns(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], PreciseEffectivityDetails: PreciseEffectivityDetails) -> Cba1.Services.Internal.Strong.Cbaext._2014_12.QueryManagement.FindAlignedACTLinesForDesignsResponse: ...

