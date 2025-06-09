import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AlignAssemblyData:
    def __init__(self, ) -> None: ...
    SourceNode: Teamcenter.Soa.Client.Model.ModelObject
    TargetNode: Teamcenter.Soa.Client.Model.ModelObject
    ReuseAssemblyNode: Teamcenter.Soa.Client.Model.ModelObject
    AlignMode: str

class ConfigurationsInfo:
    def __init__(self, ) -> None: ...
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    RootLine: Teamcenter.Soa.Client.Model.ModelObject
    RevisionRule: Teamcenter.Soa.Client.Model.ModelObject
    VariantRule: Teamcenter.Soa.Client.Model.ModelObject
    EffGrpRevisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    ShowUnconfigVariants: bool
    ShowUnconfigOccEffectivity: bool
    ShowSupressedOccurrences: bool
    ShowUnconfigICs: bool
    ShowUnconfigAssignedOccs: bool
    SaveCC: Teamcenter.Soa.Client.Model.ModelObject

class FileTicketDetails:
    def __init__(self, ) -> None: ...
    Filename: str
    FileTicket: str

class ConfigureMultipleStructuresResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    LogFileTicket: FileTicketDetails

class CreateReuseAssembly:
    def __init__(self, ) -> None: ...
    ParentNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ModelAssemblyNode: Teamcenter.Soa.Client.Model.ModelObject
    BasisOccurrenceChain: str
    NodesAssignedInModelAssembly: list[Teamcenter.Soa.Client.Model.ModelObject]
    ClusterElements: list[SearchForClustersElement]

class CreateReuseAssemblyResp:
    def __init__(self, ) -> None: ...
    Nodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetClusterDetails:
    def __init__(self, ) -> None: ...
    Clusters: list[SearchForClustersElement]

class SearchForClusters:
    def __init__(self, ) -> None: ...
    MbomModelAssemblyNode: Teamcenter.Soa.Client.Model.ModelObject
    EbomContext: Teamcenter.Soa.Client.Model.ModelObject

class SearchForClustersElement:
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.ModelObject
    IsBasis: bool
    Idic: str

class SearchForClustersResponse:
    def __init__(self, ) -> None: ...
    BasisOccurrenceChain: str
    NodesAssignedInModelAssembly: list[Teamcenter.Soa.Client.Model.ModelObject]
    Patterns: list[SearchForClustersResponseElement]
    UnassignedModelAssemblyNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SearchForClustersResponseElement:
    def __init__(self, ) -> None: ...
    PatternNodes: list[SearchForClustersElement]
    OwningModelAssemblies: list[Teamcenter.Soa.Client.Model.ModelObject]

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AlignAssemblies(self, Input: list[AlignAssemblyData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ConfigureMultipleStructures(self, ConfigurationsInfo: list[ConfigurationsInfo]) -> ConfigureMultipleStructuresResponse: ...
    def CreateReuseAssemblies(self, Input: list[CreateReuseAssembly]) -> CreateReuseAssemblyResp: ...
    def GetClusterDetails(self, Input: list[GetClusterDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SearchForClusters(self, Input: list[SearchForClusters]) -> SearchForClustersResponse: ...

