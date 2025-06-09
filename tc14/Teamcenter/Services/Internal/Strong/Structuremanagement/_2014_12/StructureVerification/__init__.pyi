import System
import Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdatePropagationDetailsIn:
    def __init__(self, ) -> None: ...
    ChangedLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ChangedObject: Teamcenter.Soa.Client.Model.ModelObject
    ChangeType: str
    Targets: list[TargetCreateOrUpdateParams]

class CreateOrUpdatePropagationDetailsResp:
    def __init__(self, ) -> None: ...
    Details: list[CreateOrUpdatePropagationDetailsRespElem]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CreateOrUpdatePropagationDetailsRespElem:
    def __init__(self, ) -> None: ...
    PropagationDetails: list[PropagationDetail]

class CreateOrUpdateReviewStatusDetails:
    def __init__(self, ) -> None: ...
    InputIndex: int
    StatusDetails: list[CreateOrUpdateSingleReviewStatusDetail]

class CreateOrUpdateReviewStatusIn:
    def __init__(self, ) -> None: ...
    ChangedLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ChangedObject: Teamcenter.Soa.Client.Model.ModelObject
    ChangeType: str
    ImpactedScopeStatus: list[ReviewStatusInfo]

class CreateOrUpdateReviewStatusResponse:
    def __init__(self, ) -> None: ...
    StatusDetails: list[CreateOrUpdateReviewStatusDetails]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CreateOrUpdateSingleReviewStatusDetail:
    def __init__(self, ) -> None: ...
    ImpactedScopeObject: Teamcenter.Soa.Client.Model.ModelObject
    ReviewStatus: str

class FindReviewStatusDetails:
    def __init__(self, ) -> None: ...
    InputIndex: int
    StatusDetails: list[FindSingleReviewStatusDetail]

class FindReviewStatusIn:
    def __init__(self, ) -> None: ...
    ChangedLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ChangedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    ImpactedScopes: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class FindReviewStatusResponse:
    def __init__(self, ) -> None: ...
    StatusDetails: list[FindReviewStatusDetails]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FindSingleReviewStatusDetail:
    def __init__(self, ) -> None: ...
    ResultantScope: Teamcenter.Soa.Client.Model.ModelObject
    ResultantStatus: str
    EvaluatedScopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    EvaluatedStatus: list[str]
    SetByUser: bool

class GetPropPropagationDetailsRespElem:
    def __init__(self, ) -> None: ...
    PropagationStatusDetails: list[FindReviewStatusDetails]
    PropertyDetails: list[PropertyDetail2]
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2

class GetPropPropagationStatusDetailsIn:
    def __init__(self, ) -> None: ...
    ChangedLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    ImpactedLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    ObjectsDescribingChange: list[Teamcenter.Soa.Client.Model.ModelObject]
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2

class GetPropPropagationStatusDetailsResp:
    def __init__(self, ) -> None: ...
    Details: list[GetPropPropagationDetailsRespElem]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetStructureChangeDetailsResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Details: list[StructureChangeDetailsResponseElement]

class GetStructureChangeImpactedLinesInfo:
    def __init__(self, ) -> None: ...
    IcImpactedLinesInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    RevisionImpactedLinesInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    OccEffImpactedLinesInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    PeriodImpactedLinesInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2

class GetStructureChangeImpactedLinesResponse:
    def __init__(self, ) -> None: ...
    ImpactedLinesInfo: list[GetStructureChangeImpactedLinesInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ImpactedLinesCriteria:
    def __init__(self, ) -> None: ...
    FindImpactedLinesByICInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    FindImpactedLinesByRevisionEff: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    FindImpactedLinesByOccEff: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    FindImpactedLinesByPeriod: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2

class PropagationDetail:
    def __init__(self, ) -> None: ...
    Status: str
    TargetContext: Teamcenter.Soa.Client.Model.ModelObject

class PropertyDetail2:
    def __init__(self, ) -> None: ...
    Index: int
    PropertyDetails: list[PropertyDetailsElement2]

class PropertyDetailsElement2:
    def __init__(self, ) -> None: ...
    PropertyName: str
    IsDifferent: bool

class ReviewStatusInfo:
    def __init__(self, ) -> None: ...
    ImpactedScopeLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Status: str

class StructureChangeDetailsElement:
    def __init__(self, ) -> None: ...
    SearchContext: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    IcChangesInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    RevisionChangesInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    OccEffChangesInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    PeriodChangesInfo: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2

class StructureChangeDetailsResponseElement:
    def __init__(self, ) -> None: ...
    IcChangeDetails: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    RevisionChangeDetails: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    OccEffChangeDetails: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2
    PeriodChangeDetails: Teamcenter.Services.Internal.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria2

class TargetCreateOrUpdateParams:
    def __init__(self, ) -> None: ...
    TargetLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    IncrementalChangeElement: Teamcenter.Soa.Client.Model.ModelObject
    Status: str

class StructureVerification:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdatePropagationDetails(self, Input: list[CreateOrUpdatePropagationDetailsIn]) -> CreateOrUpdatePropagationDetailsResp: ...
    def CreateOrUpdateReviewStatus(self, Input: list[CreateOrUpdateReviewStatusIn]) -> CreateOrUpdateReviewStatusResponse: ...
    def FindReviewStatus(self, Input: list[FindReviewStatusIn]) -> FindReviewStatusResponse: ...
    def GetPropertyPropagationStatusDetails(self, Input: list[GetPropPropagationStatusDetailsIn]) -> GetPropPropagationStatusDetailsResp: ...
    def GetStructureChangeDetails(self, DetailsElements: list[StructureChangeDetailsElement]) -> GetStructureChangeDetailsResponse: ...
    def GetStructureChangeImpactedLines(self, ImpactedLinesCriteria: list[ImpactedLinesCriteria]) -> GetStructureChangeImpactedLinesResponse: ...

