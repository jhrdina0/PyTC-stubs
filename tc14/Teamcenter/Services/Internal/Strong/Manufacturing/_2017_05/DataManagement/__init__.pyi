import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement
import Teamcenter.Soa.Client.Model
import typing

class EffectivityInfo:
    def __init__(self, ) -> None: ...
    Effectivity: Teamcenter.Soa.Client.Model.ModelObject
    Ranges: list[str]
    EffectivityTransitionsMap: System.Collections.Hashtable

class GetFutureRevisionsIn:
    def __init__(self, ) -> None: ...
    InputLine: Teamcenter.Soa.Client.Model.ModelObject
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class GetFutureRevisionsInfo:
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.ModelObject
    RevInfoList: list[RevisionInfo]
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class GetFutureRevisionsResponse:
    def __init__(self, ) -> None: ...
    LineFutureRevisionInfoMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class RevisionInfo:
    def __init__(self, ) -> None: ...
    FutureRevision: Teamcenter.Soa.Client.Model.ModelObject
    FutureRevStatusInfo: list[StatusInfo]
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class StatusInfo:
    def __init__(self, ) -> None: ...
    Status: Teamcenter.Soa.Client.Model.ModelObject
    FutureRevEffectivityInfo: list[EffectivityInfo]

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetFutureRevisions(self, Input: list[GetFutureRevisionsIn]) -> GetFutureRevisionsResponse: ...

