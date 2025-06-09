import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CutbackInfo:
    def __init__(self, ) -> None: ...
    Cutback: Teamcenter.Soa.Client.Model.Strong.POM_object
    Name: str
    Description: str
    Sequence: int
    Effectivity: list[str]
    Solutions: list[OccCutbackValueInfo]
    Impacted: list[OccCutbackValueInfo]
    AllowGaps: bool
    ActionForCutback: int

class CutbackUnitEffectivityResponse:
    def __init__(self, ) -> None: ...
    Cutbacks: list[OccEffCutbackInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class NetEffectivityOutput:
    def __init__(self, ) -> None: ...
    OccEffectivity: str
    NetEffectivity: str
    NetEOC: bool

class NetEffectivityResponse:
    def __init__(self, ) -> None: ...
    NetEffectivityOutputVector: list[NetEffectivityOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class OccCutbackValueInfo:
    def __init__(self, ) -> None: ...
    Occ: Teamcenter.Soa.Client.Model.ModelObject
    EffProposals: list[ProposalInfo]

class OccEffCutbackInfo:
    def __init__(self, ) -> None: ...
    CutbackParent: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    Cutbacks: list[CutbackInfo]

class ProposalInfo:
    def __init__(self, ) -> None: ...
    Proposal: Teamcenter.Soa.Client.Model.Strong.POM_object
    Effectivity: str

class Effectivity:
    def __init__(self , *args: typing.Any) -> None: ...
    def CutbackUnitOccurrenceEffectivity(self, OccEffCutbacks: list[OccEffCutbackInfo]) -> CutbackUnitEffectivityResponse: ...
    def GetUnitNetOccurrenceEffectivity(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> NetEffectivityResponse: ...

