import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class IsMilestoneActivityInProgressRes2:
    def __init__(self, ) -> None: ...
    MileStoneActivityInProgressMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PdmCore:
    def __init__(self , *args: typing.Any) -> None: ...
    def IsMilestoneActivityInProgress2(self, CapitalAssetRoots: list[Teamcenter.Soa.Client.Model.Strong.Pdm0CARoot]) -> IsMilestoneActivityInProgressRes2: ...

