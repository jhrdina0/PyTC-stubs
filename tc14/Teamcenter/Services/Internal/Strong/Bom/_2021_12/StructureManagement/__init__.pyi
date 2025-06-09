import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetAlignDesignsInput:
    def __init__(self, ) -> None: ...
    PartLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    RequestPref: System.Collections.Hashtable

class GetAlignedDesignsResp:
    def __init__(self, ) -> None: ...
    AlignedOccCsidPaths: list[str]
    AlignedBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    DesignProduct: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetAlignedPartsCsidChainResp:
    def __init__(self, ) -> None: ...
    AlignedOccCsidPaths: list[str]
    AlignedBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetAlignedPartsInput:
    def __init__(self, ) -> None: ...
    InputPartLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    OccurrenceChains: list[str]
    RequestPref: System.Collections.Hashtable

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAlignedDesigns(self, Input: GetAlignDesignsInput) -> GetAlignedDesignsResp: ...
    def GetAlignedPartsCsidChain(self, Input: GetAlignedPartsInput) -> GetAlignedPartsCsidChainResp: ...

