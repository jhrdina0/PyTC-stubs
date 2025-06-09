import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BrokenLinkReplacementResponse:
    def __init__(self, ) -> None: ...
    BrokenLinkWithReplacementCandidates: list[BrokenLinkWithReplacementCandidate]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ReplacementCandidateSearchInput:
    def __init__(self, ) -> None: ...
    SearchScopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ReplacementCandidateSearchCriteria: list[ReplacementCandidateSearchCriteria]
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule

class BrokenLinkSearchInput:
    def __init__(self, ) -> None: ...
    SearchScope: list[Teamcenter.Soa.Client.Model.ModelObject]
    ReplacementCandidateSearchInput: ReplacementCandidateSearchInput
    AutoRepair: bool
    FullStructure: bool

class BrokenLinkWithReplacementCandidate:
    def __init__(self, ) -> None: ...
    BrokenLink: Teamcenter.Soa.Client.Model.ModelObject
    ReplacementCandidates: list[ReplacementCandidate]

class ReplacementCandidate:
    def __init__(self, ) -> None: ...
    Candidate: Teamcenter.Soa.Client.Model.ModelObject
    MatchedProps: list[str]

class ReplacementCandidateSearchCriteria:
    def __init__(self, ) -> None: ...
    OperatorName: str
    PropertyName: str
    PropertyValue: str

class BrokenLinks:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetBrokenLinkAndReplacements(self, BrokenLinkInput: BrokenLinkSearchInput) -> BrokenLinkReplacementResponse: ...

