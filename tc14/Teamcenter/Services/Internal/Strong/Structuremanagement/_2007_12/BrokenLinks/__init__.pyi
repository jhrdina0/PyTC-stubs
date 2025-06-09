import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CandidatesList:
    def __init__(self, ) -> None: ...
    BrokenLink: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Candidates: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class CriteriaStruct:
    def __init__(self, ) -> None: ...
    PropertyName: str
    OperatorName: str

class SearchCandidatesCriteria:
    def __init__(self, ) -> None: ...
    CandidateScopeBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    Criteria: list[CriteriaStruct]
    PreviousConfiguration: Teamcenter.Soa.Client.Model.Strong.RevisionRule

class FindAndFixInput:
    def __init__(self, ) -> None: ...
    BrokenLinkBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    QuickSearch: bool
    Criteria: SearchCandidatesCriteria
    AutofixAllowed: bool

class FindCandidatesResponse:
    def __init__(self, ) -> None: ...
    FoundCandidates: list[CandidatesList]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RepairBrokenLinksParam:
    def __init__(self, ) -> None: ...
    BrokenLink: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Candidate: Teamcenter.Soa.Client.Model.Strong.BOMLine

class BrokenLinks:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetBrokenLinkInfoWithFixOpt(self, Input: list[FindAndFixInput]) -> FindCandidatesResponse: ...
    def RepairBrokenLinks(self, Input: list[RepairBrokenLinksParam]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

