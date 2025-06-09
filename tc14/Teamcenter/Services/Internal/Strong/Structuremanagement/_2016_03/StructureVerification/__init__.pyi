import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AdditionalData:
    def __init__(self, ) -> None: ...
    IntMap: System.Collections.Hashtable
    DblMap: System.Collections.Hashtable
    StrMap: System.Collections.Hashtable
    ObjMap: System.Collections.Hashtable
    DateMap: System.Collections.Hashtable

class AlignMatchedCandidateElem:
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    AlignAction: str

class AlignMatchedCandidatesResp:
    def __init__(self, ) -> None: ...
    AdditionalInfo: AdditionalData
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindMatchingCandidatesResp:
    def __init__(self, ) -> None: ...
    MatchedCandidates: list[MatchingCandidateElems]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MatchingCandidateElemForSingleObj:
    def __init__(self, ) -> None: ...
    ObjectToSearchFor: Teamcenter.Soa.Client.Model.ModelObject
    MatchingCandidates: list[Teamcenter.Soa.Client.Model.ModelObject]
    HowMatched: list[str]

class MatchingCandidateElems:
    def __init__(self, ) -> None: ...
    Matches: list[MatchingCandidateElemForSingleObj]

class SearchCandidateElems:
    def __init__(self, ) -> None: ...
    ObjectsToSearchFor: list[Teamcenter.Soa.Client.Model.ModelObject]
    SearchCandidates: list[Teamcenter.Soa.Client.Model.ModelObject]
    ScopesToSearchIn: list[TargetScopeElem]

class TargetScopeElem:
    def __init__(self, ) -> None: ...
    Scopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ClosureRule: str

class StructureVerification:
    def __init__(self , *args: typing.Any) -> None: ...
    def AlignMatchedCandidates(self, InputObjects: list[AlignMatchedCandidateElem], AdditionalInfo: AdditionalData) -> AlignMatchedCandidatesResp: ...
    def FindMatchingCandidates(self, InputObjects: list[SearchCandidateElems], AdditionalInfo: AdditionalData) -> FindMatchingCandidatesResp: ...

