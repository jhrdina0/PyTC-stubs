import Bom0.Services.Internal.Strong.Bomcore._2016_10.AlignmentManagement
import Bom0.Services.Internal.Strong.Bomcore._2016_10.PartStructureManagement
import Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement
import System
import System.Collections
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class AlignmentManagementRestBindingStub(AlignmentManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetAlignedDesignElements(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, PartUsages: list[Teamcenter.Soa.Client.Model.Strong.Bom0AbstractPartUsage]) -> Bom0.Services.Internal.Strong.Bomcore._2016_10.AlignmentManagement.GetAlignedDesignElementsResponse: ...
    def AlignPartAndDesigns(self, PartAlgnmtInput: list[Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.PartDesignAlignmentInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AlignPartOccurrences(self, PartOccAlgnmtInput: list[Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.PartOccurrenceAlignmentInput]) -> Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.AlignPartOccurrenceResponse: ...
    def GetAlignedPartOccurrences(self, DesignLineInfoInput: list[Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.GetAlignedPartOccInputStructure]) -> Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.GetAlignedPartOccurrenceResponse: ...
    def MarkPrimaryDesignOnPart(self, MarkPrimaryDesignInput: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnAlignPartAndDesigns(self, PartUnAlgnmtInput: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnAlignPartOccurrences(self, PartOccUnAlgnmtInput: list[Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.PartOccurrenceUnAlignmentInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnAlignPartUsageAndDesignElements(self, PartUsageUnAlgnmtInputs: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class AlignmentManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AlignmentManagementService: ...
    def GetAlignedDesignElements(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, PartUsages: list[Teamcenter.Soa.Client.Model.Strong.Bom0AbstractPartUsage]) -> Bom0.Services.Internal.Strong.Bomcore._2016_10.AlignmentManagement.GetAlignedDesignElementsResponse: ...
    def AlignPartAndDesigns(self, PartAlgnmtInput: list[Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.PartDesignAlignmentInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AlignPartOccurrences(self, PartOccAlgnmtInput: list[Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.PartOccurrenceAlignmentInput]) -> Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.AlignPartOccurrenceResponse: ...
    def GetAlignedPartOccurrences(self, DesignLineInfoInput: list[Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.GetAlignedPartOccInputStructure]) -> Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.GetAlignedPartOccurrenceResponse: ...
    def MarkPrimaryDesignOnPart(self, MarkPrimaryDesignInput: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnAlignPartAndDesigns(self, PartUnAlgnmtInput: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnAlignPartOccurrences(self, PartOccUnAlgnmtInput: list[Bom0.Services.Internal.Strong.Bomcore._2017_05.AlignmentManagement.PartOccurrenceUnAlignmentInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnAlignPartUsageAndDesignElements(self, PartUsageUnAlgnmtInputs: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class PartStructureManagementRestBindingStub(PartStructureManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetPartStructure(self, Part: Teamcenter.Soa.Client.Model.Strong.Bom0AbstractPart, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, IncludeAlignedDesignInfo: bool) -> Bom0.Services.Internal.Strong.Bomcore._2016_10.PartStructureManagement.GetPartStructureResponse: ...
    def DeletePartStructures(self, PbeLinesToDelete: list[Teamcenter.Soa.Client.Model.Strong.Bom0PBELine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class PartStructureManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> PartStructureManagementService: ...
    def GetPartStructure(self, Part: Teamcenter.Soa.Client.Model.Strong.Bom0AbstractPart, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, IncludeAlignedDesignInfo: bool) -> Bom0.Services.Internal.Strong.Bomcore._2016_10.PartStructureManagement.GetPartStructureResponse: ...
    def DeletePartStructures(self, PbeLinesToDelete: list[Teamcenter.Soa.Client.Model.Strong.Bom0PBELine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

