import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttachmentChangeResponse:
    def __init__(self, ) -> None: ...
    Response: list[AttachmentInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AttachmentICEInfo:
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.Strong.MECfgLine
    AbsOccRootLine: str
    ChildEditIces: list[BaseICEInfo]
    RelationIces: list[BaseICEInfo]

class AttachmentInfo:
    def __init__(self, ) -> None: ...
    ListOfAttachments: list[AttachmentICEInfo]

class AttributeChangeResponse:
    def __init__(self, ) -> None: ...
    Response: list[AttributeInfoOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class BaseICEInfo:
    def __init__(self, ) -> None: ...
    TypeOfIce: int
    HowConfigured: str
    IcRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    Ice: Teamcenter.Soa.Client.Model.Strong.IncrementalChangeElement

class ICEAttributes:
    def __init__(self, ) -> None: ...
    AttributeName: str
    AttributeValue: str
    AbsOccRootLine: str
    BomViewRevision: Teamcenter.Soa.Client.Model.Strong.POM_object

class AttributeICEInfo:
    def __init__(self, ) -> None: ...
    BaseICEInfo: BaseICEInfo
    Attributes: ICEAttributes

class AttributeInfoOutput:
    def __init__(self, ) -> None: ...
    AttributeInfo: list[AttributeICEInfo]

class ParentAndChildInfos:
    def __init__(self, ) -> None: ...
    ParentChildInfos: list[ParentChildInfo]

class ParentAndChildComponentsResponse:
    def __init__(self, ) -> None: ...
    ParentAndChildInfoResponse: ParentAndChildInfos
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ParentChildInfo:
    def __init__(self, ) -> None: ...
    Context: str
    Parent: Teamcenter.Soa.Client.Model.Strong.POM_object
    Child: Teamcenter.Soa.Client.Model.Strong.POM_object
    Ice: Teamcenter.Soa.Client.Model.Strong.IncrementalChangeElement

class PredecessorChangeInfo:
    def __init__(self, ) -> None: ...
    BaseICEInfo: list[BaseICEInfo]
    ListOfPredecessors: list[PredecessorICEInfo]

class PredecessorChangeResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Response: list[PredecessorChangeInfo]

class PredecessorICEInfo:
    def __init__(self, ) -> None: ...
    PredecessorName: str
    SequenceNumber: str

class StructureChangeResponse:
    def __init__(self, ) -> None: ...
    Response: list[StructureChangesOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StructureChangesOutput:
    def __init__(self, ) -> None: ...
    BaseInfo: list[BaseICEInfo]

class IncrementalChange:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAttachmentChanges(self, Attachmentlines: list[Teamcenter.Soa.Client.Model.Strong.MECfgLine], FRefresh: bool) -> AttachmentChangeResponse: ...
    def GetAttributeChanges(self, AttributeOccLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], FRefresh: bool) -> AttributeChangeResponse: ...
    def GetParentAndChildComponents(self, IcRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> ParentAndChildComponentsResponse: ...
    def GetPredecessorChanges(self, PredecessorLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], FRefresh: bool) -> PredecessorChangeResponse: ...
    def GetStructureChanges(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], FRefresh: bool) -> StructureChangeResponse: ...

