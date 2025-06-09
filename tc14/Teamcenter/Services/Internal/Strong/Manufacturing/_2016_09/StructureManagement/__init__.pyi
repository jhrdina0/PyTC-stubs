import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AsyncCloningStructsInfo:
    def __init__(self, ) -> None: ...
    NewName: str
    NewDescription: str
    NewId: str
    NewRevId: str
    Scopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    CloningRule: str
    CloningParams: System.Collections.Hashtable

class AsyncEffectivityInfoInput:
    def __init__(self, ) -> None: ...
    EndItem: Teamcenter.Soa.Client.Model.Strong.Item
    EndItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    UnitRangeText: str
    DateRange: list[System.DateTime]
    OpenEndedStatus: int

class AsyncCreateCPCInputInfo:
    def __init__(self, ) -> None: ...
    CloningStructsInfo: list[AsyncCloningStructsInfo]
    ReleaseStatus: str
    EffectivityInfo: AsyncEffectivityInfoInput
    OriginalCCUid: Teamcenter.Soa.Client.Model.ModelObject
    CpcName: str
    CpcDesc: str
    RefStructures: list[Teamcenter.Soa.Client.Model.ModelObject]

class CompletenessCheckPartStructureResp:
    def __init__(self, ) -> None: ...
    CompleteLines: Teamcenter.Soa.Client.Model.ModelObject
    IncompleteLines: Teamcenter.Soa.Client.Model.ModelObject
    IncompleteLinesReason: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class CreateDesignPartAlignmentInput:
    def __init__(self, ) -> None: ...
    DesignLine: Teamcenter.Soa.Client.Model.ModelObject
    PartLine: Teamcenter.Soa.Client.Model.ModelObject
    AlignMode: str
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class DesignPartAlignmentInput:
    def __init__(self, ) -> None: ...
    DesignLine: Teamcenter.Soa.Client.Model.ModelObject
    PartLine: Teamcenter.Soa.Client.Model.ModelObject
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class DesignPartAlignmentResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class LinkStructuresInput:
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.ModelObject
    TargetLine: Teamcenter.Soa.Client.Model.ModelObject
    RelationName: str
    Link: bool

class LinkStructuresResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class ObjectAlignmentInput:
    def __init__(self, ) -> None: ...
    InputLine: Teamcenter.Soa.Client.Model.ModelObject
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CompletenessCheckPartStructure(self, Input: list[ObjectAlignmentInput]) -> CompletenessCheckPartStructureResp: ...
    def CreateOrUpdateDesignPartAlignment(self, Input: list[CreateDesignPartAlignmentInput]) -> DesignPartAlignmentResponse: ...
    def FindRelatedDesignOrPartStructures(self, Input: list[ObjectAlignmentInput]) -> DesignPartAlignmentResponse: ...
    def LinkOrUnlinkStructures(self, Input: list[LinkStructuresInput]) -> LinkStructuresResponse: ...
    def RemoveDesignPartAlignment(self, Input: list[ObjectAlignmentInput]) -> DesignPartAlignmentResponse: ...
    def VerifyDesignPartAlignment(self, Input: list[DesignPartAlignmentInput]) -> DesignPartAlignmentResponse: ...

