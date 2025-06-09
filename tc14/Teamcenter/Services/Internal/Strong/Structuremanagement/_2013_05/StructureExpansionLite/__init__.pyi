import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ChildLineInfo:
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject
    IndexToAttachedObjInfos: list[int]
    ConfigNotReliable: bool

class Controls:
    def __init__(self, ) -> None: ...
    ExpansionPref: System.Collections.Hashtable
    RelationCriteria: list[RelationTypesAndCriteria]

class DatasetInfo:
    def __init__(self, ) -> None: ...
    RelationName: str
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    NamedRefInfo: list[NamedRefInfo]

class DatasetTypeAndNamedRefs:
    def __init__(self, ) -> None: ...
    DatasetTypeName: str
    NamedReferenceNames: list[str]

class ExpansionResponse:
    def __init__(self, ) -> None: ...
    ParentChildInfo: System.Collections.Hashtable
    DatasetInfo: list[DatasetInfo]
    UndeliveredLines: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LineAndPaths:
    def __init__(self, ) -> None: ...
    StartingLine: Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject
    Paths: list[Path]

class NamedRefInfo:
    def __init__(self, ) -> None: ...
    Name: str
    Type: str
    Object: Teamcenter.Soa.Client.Model.ModelObject
    FileTicket: str

class PartialExpansionControls:
    def __init__(self, ) -> None: ...
    ExpansionPrefValues: System.Collections.Hashtable
    RelationCriteria: list[RelationTypesAndCriteria]

class Path:
    def __init__(self, ) -> None: ...
    PathId: str
    BasedOn: list[str]
    Elements: list[str]

class RelationTypesAndCriteria:
    def __init__(self, ) -> None: ...
    RelationName: str
    NamedRefHandler: str
    DatasetTypeAndNamedRefs: list[DatasetTypeAndNamedRefs]

class StructureExpansionLite:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandBasedOnOccurrenceList(self, LinePaths: list[LineAndPaths], Controls: PartialExpansionControls) -> ExpansionResponse: ...
    def ExpandNext(self, LinesToExpand: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject], Controls: Controls) -> ExpansionResponse: ...
    def GetUndelivered(self, UndeliveredLineUids: list[str], Controls: Controls) -> ExpansionResponse: ...
    def UnloadBelow(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.Fnd0BOMLineLite]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

