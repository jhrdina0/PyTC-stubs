import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Snapshot3DInfoInput2:
    def __init__(self, ) -> None: ...
    ClientId: str
    Snapshot3DDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    GetStaticFilesInfo: bool

class Snapshot3DVisibleLines2:
    def __init__(self, ) -> None: ...
    UidType: str
    VisibleLinesMap: System.Collections.Hashtable
    RelDatasetInfoMap: System.Collections.Hashtable

class Snapshot3DInfoOutput2:
    def __init__(self, ) -> None: ...
    NamedRefFileInfoList: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.NamedRefsInDataset]
    RelObjList: list[Snapshot3DRelObjInfo2]
    Snapshot3DVisibleLines: Snapshot3DVisibleLines2

class Snapshot3DInfoResponse2:
    def __init__(self, ) -> None: ...
    Snapshot3DInfoMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Snapshot3DRelObjInfo2:
    def __init__(self, ) -> None: ...
    RelType: str
    RelObj: Teamcenter.Soa.Client.Model.ModelObject
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation

class StaticFileInfo2:
    def __init__(self, ) -> None: ...
    DatasetUID: str
    ImanFileUID: str
    OriginalFileName: str

class VisibleLine2:
    def __init__(self, ) -> None: ...
    UidString: str
    RelDatasetRef: str
    ParentRef: str
    AltKeyType: str
    AltKeyValue: str

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSnapshot3DInfo2(self, Snapshot3DInputList: list[Snapshot3DInfoInput2]) -> Snapshot3DInfoResponse2: ...

