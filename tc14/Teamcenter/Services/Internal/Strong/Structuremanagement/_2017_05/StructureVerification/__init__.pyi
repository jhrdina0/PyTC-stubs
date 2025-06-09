import System
import Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification
import Teamcenter.Soa.Client.Model
import typing

class AttachmentComparisonDetailsResponse:
    def __init__(self, ) -> None: ...
    Details: list[AttachmentTypeDetail]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AttachmentDetail:
    def __init__(self, ) -> None: ...
    Attachments: list[Teamcenter.Soa.Client.Model.ModelObject]
    MatchType: int

class AttachmentTypeDetail:
    def __init__(self, ) -> None: ...
    Index: int
    EquivalentLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    AttachmentExtDetails: list[ExtensionAttachmentTypeDetails]

class AttachmentTypeDetailElement:
    def __init__(self, ) -> None: ...
    AttachmentRelType: Teamcenter.Soa.Client.Model.ModelObject
    AttachmentsDetails: list[AttachmentDetail]

class ExtensionAttachmentTypeDetails:
    def __init__(self, ) -> None: ...
    ExtensionName: str
    AttachmentTypesDetails: list[AttachmentTypeDetailElement]

class StructureVerification:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAttachmentComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartialMatchCriteria: list[Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.StringToPartialMatchCriteria]) -> AttachmentComparisonDetailsResponse: ...

