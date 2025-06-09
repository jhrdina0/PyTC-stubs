import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Visualization._2008_06.StructureManagement
import Teamcenter.Services.Internal.Strong.Visualization._2011_12.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AdditionalInfo:
    def __init__(self, ) -> None: ...
    StrToDateVectorMap: System.Collections.Hashtable
    StrToDoubleVectorMap: System.Collections.Hashtable
    StrToStringVectorMap: System.Collections.Hashtable
    StrToObjectVectorMap: System.Collections.Hashtable
    StrToIntegerVectorMap: System.Collections.Hashtable

class ExpandPSData1:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ObjectOfBOMLine: Teamcenter.Soa.Client.Model.ModelObject
    IndexOfrelatedObjectsInfo: list[int]
    ResolutionStatus: int
    IsAlternate: bool

class ExpandPSFromOccurrenceListOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    OccurrenceList: list[OccurrenceListResults]

class ExpandPSFromOccurrenceListResponse:
    def __init__(self, ) -> None: ...
    Output: list[ExpandPSFromOccurrenceListOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    RelatedObjects: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.StructureManagement.ExpandPSRelatedObjectInfo]
    ChildrenOfParent: System.Collections.Hashtable
    AdditionalInfo: AdditionalInfo

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
    def ExpandPSFromOccurrenceList2(self, Info: list[Teamcenter.Services.Internal.Strong.Visualization._2011_12.StructureManagement.ExpandPSFromOccurrenceListInfo], Pref: Teamcenter.Services.Internal.Strong.Visualization._2011_12.StructureManagement.ExpandPSFromOccurrenceListPref, AdditionalInfo: AdditionalInfo) -> ExpandPSFromOccurrenceListResponse: ...

