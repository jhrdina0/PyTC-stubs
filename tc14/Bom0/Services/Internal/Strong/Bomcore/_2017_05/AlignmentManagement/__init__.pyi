import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AlignPartOccurrenceResponse:
    def __init__(self, ) -> None: ...
    ListResponseData: list[AlignPartOccurrenceResponseData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AlignPartOccurrenceResponseData:
    def __init__(self, ) -> None: ...
    PbeLine: Teamcenter.Soa.Client.Model.Strong.Bom0PBELine
    PbeAlignment: Teamcenter.Soa.Client.Model.Strong.Bom0AbstractPBEAlignment

class GetAlignedPartOccInputStructure:
    def __init__(self, ) -> None: ...
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    DesignLine: Teamcenter.Soa.Client.Model.Strong.BOMLine

class GetAlignedPartOccResponseData:
    def __init__(self, ) -> None: ...
    DesignLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    PbeLines: list[Teamcenter.Soa.Client.Model.Strong.Bom0PBELine]

class GetAlignedPartOccurrenceResponse:
    def __init__(self, ) -> None: ...
    ResponseData: list[GetAlignedPartOccResponseData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PartDesignAlignmentInput:
    def __init__(self, ) -> None: ...
    Part: Teamcenter.Soa.Client.Model.Strong.Bom0AbstractPart
    DesignList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    PrimaryDesign: Teamcenter.Soa.Client.Model.Strong.ItemRevision

class PartOccurrenceAlignmentInput:
    def __init__(self, ) -> None: ...
    PbeLine: Teamcenter.Soa.Client.Model.Strong.Bom0PBELine
    DesignLine: Teamcenter.Soa.Client.Model.Strong.BOMLine

class PartOccurrenceUnAlignmentInput:
    def __init__(self, ) -> None: ...
    PbeLine: Teamcenter.Soa.Client.Model.Strong.Bom0PBELine
    UnAlignChildPBELines: bool

class AlignmentManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AlignPartAndDesigns(self, PartAlgnmtInput: list[PartDesignAlignmentInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AlignPartOccurrences(self, PartOccAlgnmtInput: list[PartOccurrenceAlignmentInput]) -> AlignPartOccurrenceResponse: ...
    def GetAlignedPartOccurrences(self, DesignLineInfoInput: list[GetAlignedPartOccInputStructure]) -> GetAlignedPartOccurrenceResponse: ...
    def MarkPrimaryDesignOnPart(self, MarkPrimaryDesignInput: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnAlignPartAndDesigns(self, PartUnAlgnmtInput: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnAlignPartOccurrences(self, PartOccUnAlgnmtInput: list[PartOccurrenceUnAlignmentInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnAlignPartUsageAndDesignElements(self, PartUsageUnAlgnmtInputs: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...

