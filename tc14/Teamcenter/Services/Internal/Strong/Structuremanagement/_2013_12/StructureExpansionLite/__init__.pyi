import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Structuremanagement._2013_05.StructureExpansionLite
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DatasetInfo2:
    def __init__(self, ) -> None: ...
    RelationName: str
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    NamedRefInfo: list[NamedRefInfo2]

class ExpansionResponse2:
    def __init__(self, ) -> None: ...
    ParentChildInfo: System.Collections.Hashtable
    DatasetInfo: list[DatasetInfo2]
    ParentUndeliveredChildrenUids: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NamedRefInfo2:
    def __init__(self, ) -> None: ...
    Name: str
    Type: str
    OriginalFileName: str
    Object: Teamcenter.Soa.Client.Model.ModelObject
    FileTicket: str

class StructureExpansionLite:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandBasedOnOccurrenceList2(self, LinePaths: list[Teamcenter.Services.Internal.Strong.Structuremanagement._2013_05.StructureExpansionLite.LineAndPaths], Controls: Teamcenter.Services.Internal.Strong.Structuremanagement._2013_05.StructureExpansionLite.PartialExpansionControls) -> ExpansionResponse2: ...
    def ExpandNext2(self, LinesToExpand: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject], Controls: Teamcenter.Services.Internal.Strong.Structuremanagement._2013_05.StructureExpansionLite.Controls) -> ExpansionResponse2: ...
    def GetUndelivered2(self, UndeliveredLineUids: list[str], Controls: Teamcenter.Services.Internal.Strong.Structuremanagement._2013_05.StructureExpansionLite.Controls) -> ExpansionResponse2: ...
    def UnloadBelow2(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

