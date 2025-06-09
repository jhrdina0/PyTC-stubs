import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MappedPortFeature:
    def __init__(self, ) -> None: ...
    FeatureID1: str
    FeatureID2: str
    FeaturePortAttrCode: list[str]

class MappedPortFeatureResponse:
    def __init__(self, ) -> None: ...
    MappedPortFeatureData: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PortRoutineSetInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    Routine1: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    Routine2: Teamcenter.Soa.Client.Model.Strong.ItemRevision

class EngineeringDataQuery:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMappedPortFeatureData(self, Request: list[PortRoutineSetInfo]) -> MappedPortFeatureResponse: ...

