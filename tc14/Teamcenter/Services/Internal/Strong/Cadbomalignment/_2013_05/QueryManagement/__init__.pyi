import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BreakDownCriteria:
    def __init__(self, ) -> None: ...
    PartInfo: System.Collections.Hashtable
    QueryInfo: System.Collections.Hashtable
    ExplosionLevel: int

class MultilevelEngineeringBreakdownResponse:
    def __init__(self, ) -> None: ...
    AsmPartofLevelOneLOA: Teamcenter.Soa.Client.Model.Strong.Cba0PartProxy
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class QueryManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def PerformMultilevelEngineeringBreakdown(self, InputBreakdownCriteria: BreakDownCriteria) -> MultilevelEngineeringBreakdownResponse: ...

