import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Rdv._2009_01.VariantManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddPartSolutionInputInfo:
    def __init__(self, ) -> None: ...
    Values: list[OccNotesAttributes]
    Component: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    AbeLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ProdRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    AbeApn: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode
    MetaExpr: list[Teamcenter.Services.Internal.Strong.Rdv._2009_01.VariantManagement.NVEMetaToken]
    Validate: bool
    Quantity: int

class AddPartSolutionOutputInfo:
    def __init__(self, ) -> None: ...
    Component: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    PartSolutionAPN: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode

class AddPartSolutionResponse:
    def __init__(self, ) -> None: ...
    Output: list[AddPartSolutionOutputInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class BackgroundOccurrences:
    def __init__(self, ) -> None: ...
    NumProcessedRequests: int
    NumSuggestedRequests: int
    NodeanswerLists: list[NodeAnswer]

class BackgroundOccurrencesResponse:
    def __init__(self, ) -> None: ...
    Output: System.Collections.Hashtable
    Servicedata: Teamcenter.Soa.Client.Model.ServiceData

class NodeAnswer:
    def __init__(self, ) -> None: ...
    BackgroundNodeList: list[str]

class OccNotesAttributes:
    def __init__(self, ) -> None: ...
    NoteType: str
    NoteText: str

class ProximityTarget:
    def __init__(self, ) -> None: ...
    ProxtargetId: str
    Proximity: float
    Target: str

class ReplacePartSolutionInputInfo:
    def __init__(self, ) -> None: ...
    Values: list[OccNotesAttributes]
    Component: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    AbeAPN: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode
    MetaExpr: list[Teamcenter.Services.Internal.Strong.Rdv._2009_01.VariantManagement.NVEMetaToken]
    Validate: bool
    SplitAndClone: bool
    CarrySubstitutes: bool
    Quantity: int

class ReplacePartSolutionOutputInfo:
    def __init__(self, ) -> None: ...
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Component: Teamcenter.Soa.Client.Model.Strong.ItemRevision

class ReplacePartSolutionResponse:
    def __init__(self, ) -> None: ...
    Output: list[ReplacePartSolutionOutputInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class TargetOccurrences:
    def __init__(self, ) -> None: ...
    ClientId: str
    Topitemrev: str
    Revrulename: str
    DisttargetsList: list[ProximityTarget]

class VariantManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetValidBackgroundOverlays(self, AbortOnError: bool, Questions: list[TargetOccurrences]) -> BackgroundOccurrencesResponse: ...
    def AddPartToProduct(self, Inputs: list[AddPartSolutionInputInfo]) -> AddPartSolutionResponse: ...
    def ReplacePartInProduct(self, Inputs: list[ReplacePartSolutionInputInfo]) -> ReplacePartSolutionResponse: ...

