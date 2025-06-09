import System
import Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification
import Teamcenter.Soa.Client.Model
import typing

class ExtensionMountAttachTypeDetails:
    def __init__(self, ) -> None: ...
    ExtensionName: str
    MountAttachDetailTypes: list[MountAttachDetailTypeElement]

class MountAttachComparisonsResponse:
    def __init__(self, ) -> None: ...
    MountAttachTypeDetails: list[MountAttachTypeDetail]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MountAttachDetail:
    def __init__(self, ) -> None: ...
    Attachments: list[Teamcenter.Soa.Client.Model.ModelObject]
    MatchType: int

class MountAttachDetailTypeElement:
    def __init__(self, ) -> None: ...
    RelationType: Teamcenter.Soa.Client.Model.ModelObject
    MountAttachDetails: list[MountAttachDetail]

class MountAttachTypeDetail:
    def __init__(self, ) -> None: ...
    Index: int
    EquivalentLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    MountAttachTypeExtensions: list[ExtensionMountAttachTypeDetails]

class StructureVerification:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMountAttachComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartialMatchCriteria: list[Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.StringToPartialMatchCriteria]) -> MountAttachComparisonsResponse: ...

