import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateSnapshot3DResponse:
    def __init__(self, ) -> None: ...
    Snapshot3DOutputMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindNodesInProductViewResultResponse:
    def __init__(self, ) -> None: ...
    OutputNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindProductViewForNodesResult:
    def __init__(self, ) -> None: ...
    ProductView: Teamcenter.Soa.Client.Model.Strong.Dataset
    NodesPresentInPv: list[Teamcenter.Soa.Client.Model.ModelObject]
    PvAttachedTo: Teamcenter.Soa.Client.Model.ModelObject

class FindProductViewForNodesResultRespose:
    def __init__(self, ) -> None: ...
    ProductViews: list[FindProductViewForNodesResult]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GatherSnapshot3DInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    RefType: str

class GatherSnapshot3DListOutputPreview:
    def __init__(self, ) -> None: ...
    SnapshotList: list[Snapshot3DOutput]

class GatherSnapshot3DListResponse:
    def __init__(self, ) -> None: ...
    Snapshot3DOutputMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NewSnapshot3DInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    AttachToBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    DatasetInfo: Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.DatasetInfo
    VisibleLinesList: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    CreateStructureFile: bool
    NamedRefFileUpdateInfoList: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.NamedRefUploadOrUpdateInfo]

class SearchCriteria:
    def __init__(self, ) -> None: ...
    SearchScope: list[Teamcenter.Soa.Client.Model.ModelObject]
    NodesToSearch: list[Teamcenter.Soa.Client.Model.ModelObject]
    NodeCombination: str

class Snapshot3DInfoInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Snapshot3DDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    GetStaticFilesInfo: bool

class Snapshot3DVisibleLines:
    def __init__(self, ) -> None: ...
    UidType: str
    VisibleLinesMap: System.Collections.Hashtable
    RelDatasetInfoMap: System.Collections.Hashtable

class Snapshot3DInfoOutput:
    def __init__(self, ) -> None: ...
    NamedRefFileInfoList: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.NamedRefsInDataset]
    RelObjList: list[Snapshot3DRelObjInfo]
    Snapshot3DVisibleLines: Snapshot3DVisibleLines

class Snapshot3DInfoResponse:
    def __init__(self, ) -> None: ...
    Snapshot3DInfoMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Snapshot3DOutput:
    def __init__(self, ) -> None: ...
    Snapshot3DDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    NamedRefFileInfoList: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.NamedRefsInDataset]

class Snapshot3DRelObjInfo:
    def __init__(self, ) -> None: ...
    RelType: str
    RelObj: Teamcenter.Soa.Client.Model.ModelObject
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation

class Snapshot3DStructureFilesInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Snapshot3DDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    VisibleLinesList: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class Snapshot3DUpdateInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Snapshot3DDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    AttachToBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    CreateStructureFile: bool
    UpdateVisibleLinesList: bool
    VisibleLinesList: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    NamedRefFileInfoList: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.NamedRefUploadOrUpdateInfo]

class Snapshot3DUpdateResponse:
    def __init__(self, ) -> None: ...
    Snapshot3DUpdateOutputMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Snapshot3DUpdateStructureFilesResponse:
    def __init__(self, ) -> None: ...
    Snapshot3DStrFilesOutputMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StaticFileInfo:
    def __init__(self, ) -> None: ...
    DatasetUID: str
    ImanFileUID: str
    OriginalFileName: str

class VisibleLine:
    def __init__(self, ) -> None: ...
    UidString: str
    RelDatasetRef: str
    ParentRef: str

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSnapshot3D(self, NewSnapshot3DInputList: list[NewSnapshot3DInput]) -> CreateSnapshot3DResponse: ...
    def FindProductViewsForNodes(self, SearchCriteria: list[SearchCriteria]) -> FindProductViewForNodesResultRespose: ...
    def GatherSnapshot3DList(self, Input: list[GatherSnapshot3DInput]) -> GatherSnapshot3DListResponse: ...
    def GetNodesPresentInProductView(self, SearchScope: list[Teamcenter.Soa.Client.Model.ModelObject], ProductView: Teamcenter.Soa.Client.Model.ModelObject, NodesToSearch: list[Teamcenter.Soa.Client.Model.ModelObject]) -> FindNodesInProductViewResultResponse: ...
    def GetSnapshot3DInfo(self, Snapshot3DInputList: list[Snapshot3DInfoInput]) -> Snapshot3DInfoResponse: ...
    def UpdateSnapshot3D(self, Snapshot3DUpdateInputList: list[Snapshot3DUpdateInput]) -> Snapshot3DUpdateResponse: ...
    def UpdateSnapshot3DStructureFiles(self, Snapshot3DStructureFilesInput: list[Snapshot3DStructureFilesInput]) -> Snapshot3DUpdateStructureFilesResponse: ...

