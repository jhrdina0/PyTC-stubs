import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Structuremanagement._2013_05.StructureExpansionLite
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AbsoccDataIncludeList:
    def __init__(self, ) -> None: ...
    AbsoccDataTypeInclusionList: list[AbsoccDataOverrideInfo]

class AbsoccDataOverrideInfo:
    def __init__(self, ) -> None: ...
    AbsoccDataType: int
    AdditionalInfo: str

class ChildLineInfo2:
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject
    IndexToAttachedObjInfos: list[int]
    UnSupportedInfo: int

class Controls2:
    def __init__(self, ) -> None: ...
    ExpansionPref: System.Collections.Hashtable
    RelationCriteria: list[Teamcenter.Services.Internal.Strong.Structuremanagement._2013_05.StructureExpansionLite.RelationTypesAndCriteria]
    ProcessLeafNodesFirst: bool
    AbsoccFilterList: AbsoccDataIncludeList
    ConfigurationSolveType: int

class Controls3:
    def __init__(self, ) -> None: ...
    ExpansionPref: System.Collections.Hashtable
    RelationCriteria: list[Teamcenter.Services.Internal.Strong.Structuremanagement._2013_05.StructureExpansionLite.RelationTypesAndCriteria]
    ProcessLeafNodesFirst: bool

class DatasetInfo3:
    def __init__(self, ) -> None: ...
    RelationName: str
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    NamedRefInfo: list[NamedRefInfo3]

class ExpansionResponse3:
    def __init__(self, ) -> None: ...
    ParentChildInfo: System.Collections.Hashtable
    DatasetInfo: list[DatasetInfo3]
    ParentUndeliveredChildrenUids: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NamedRefInfo3:
    def __init__(self, ) -> None: ...
    Name: str
    Type: str
    NamedReference: Teamcenter.Soa.Client.Model.ModelObject
    OriginalFileName: str
    FileTicket: str

class StructureExpansionLite:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandNext3(self, LinesToExpand: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject], Controls: Controls2) -> ExpansionResponse3: ...
    def GetUndelivered3(self, UndeliveredLineUids: list[str], Controls: Controls3) -> ExpansionResponse3: ...

