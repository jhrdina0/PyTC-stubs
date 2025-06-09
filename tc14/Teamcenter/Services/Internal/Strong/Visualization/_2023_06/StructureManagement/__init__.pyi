import System
import Teamcenter.Services.Internal.Strong.Visualization._2008_06.StructureManagement
import Teamcenter.Services.Internal.Strong.Visualization._2020_12.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BOMLineInfo:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Reason: str

class BOMLinesRelatedObjectInfo:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    RelatedObjects: list[RelatedObjectInfo]

class DatasetNamedReferenceInfo:
    def __init__(self, ) -> None: ...
    NamedReferenceType: str
    NamedReferenceName: str
    ReferenceObject: Teamcenter.Soa.Client.Model.ModelObject
    FileTicket: str

class DeltaInfo:
    def __init__(self, ) -> None: ...
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    BomLineInfo: list[BOMLineInfo]
    DeletedLinesUidStr: list[str]

class GetDeltaUpdatesOnBOMWindowsResponse:
    def __init__(self, ) -> None: ...
    DeltaInfo: list[DeltaInfo]
    EstimatedObjectsLeft: int
    RelatedObjects: list[BOMLinesRelatedObjectInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RelatedObjectInfo:
    def __init__(self, ) -> None: ...
    RelatedObject: Teamcenter.Soa.Client.Model.ModelObject
    NamedRefList: list[DatasetNamedReferenceInfo]

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDeltaUpdatesOnSharedBOMWindows(self, InputBOMWindows: list[Teamcenter.Soa.Client.Model.Strong.BOMWindow], PageSize: int, DeltaOptions: Teamcenter.Services.Internal.Strong.Visualization._2020_12.StructureManagement.AdditionalInfo, RelatedObjectFilter: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.StructureManagement.RelationAndTypesFilter]) -> GetDeltaUpdatesOnBOMWindowsResponse: ...

