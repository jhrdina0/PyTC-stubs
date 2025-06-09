import System
import Teamcenter.Soa.Client.Model
import typing

class GetICOMappingTargetsResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    MappingInfoVector: list[MappingInfo]

class MappingInfo:
    def __init__(self, ) -> None: ...
    SourceIcoID: str
    SourceIcoUID: str
    SourceClassID: str
    SourceClassName: str
    TargetMachine: str
    TargetWorkpiece: str
    TargetGTCBase: str
    TargetClasses: list[TargetClass]

class TargetClass:
    def __init__(self, ) -> None: ...
    TargetID: str
    TargetName: str

class ResourceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetICOMappingTargets(self, IcoUIDs: list[str], ViewType: int) -> GetICOMappingTargetsResponse: ...

