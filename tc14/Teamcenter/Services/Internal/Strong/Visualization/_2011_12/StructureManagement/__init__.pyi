import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Visualization._2008_06.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExpandPSData1:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ObjectOfBOMLine: Teamcenter.Soa.Client.Model.ModelObject
    IndexOfrelatedObjectsInfo: list[int]

class ExpandPSFromOccurrenceListInfo:
    def __init__(self, ) -> None: ...
    OccurListClientId: str
    OccurrenceChainsByParent: list[OccurrenceChainList]

class ExpandPSFromOccurrenceListOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    OccurrenceList: list[OccurrenceListResults]

class ExpandPSFromOccurrenceListPref:
    def __init__(self, ) -> None: ...
    PrefKeyValue: System.Collections.Hashtable
    Info: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.StructureManagement.RelationAndTypesFilter]

class ExpandPSFromOccurrenceListResponse:
    def __init__(self, ) -> None: ...
    Output: list[ExpandPSFromOccurrenceListOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    RelatedObjects: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.StructureManagement.ExpandPSRelatedObjectInfo]
    ChildrenOfParent: System.Collections.Hashtable

class OccurrenceChain:
    def __init__(self, ) -> None: ...
    NgidClientId: str
    AttributeNames: list[str]
    OccurrenceChainStr: list[str]

class OccurrenceChainList:
    def __init__(self, ) -> None: ...
    ListClientId: str
    ParentBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    OccurrenceList: list[OccurrenceChain]

class OccurrenceChainResult:
    def __init__(self, ) -> None: ...
    ClientId: str
    OccurrenceChain: list[ExpandPSData1]

class OccurrenceListResults:
    def __init__(self, ) -> None: ...
    ClientId: str
    Parent: ExpandPSData1
    OccurrenceList: list[OccurrenceChainResult]

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandPSFromOccurrenceList(self, Info: list[ExpandPSFromOccurrenceListInfo], Pref: ExpandPSFromOccurrenceListPref) -> ExpandPSFromOccurrenceListResponse: ...

