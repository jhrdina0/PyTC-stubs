import Cae0.Services.Internal.Strong.Simproc._2014_12.SimProcessConfigurationManagement
import Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement
import Cae0.Services.Internal.Strong.Simproc._2016_03.SimStructureManagement
import Cae0.Services.Internal.Strong.Simproc._2016_05.SimProcessConfigurationManagement
import Cae0.Services.Internal.Strong.Simproc._2016_10.SimProcessConfigurationManagement
import Cae0.Services.Internal.Strong.Simproc._2017_05.SimStructureManagement
import Cae0.Services.Internal.Strong.Simproc._2017_05.SimulationToolLaunch
import Cae0.Services.Internal.Strong.Simproc._2017_11.SimStructureManagement
import Cae0.Services.Internal.Strong.Simproc._2018_06.SimStructureManagement
import Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement
import Cae0.Services.Internal.Strong.Simproc._2018_11.SimStructureManagement
import Cae0.Services.Internal.Strong.Simproc._2018_11.SimulationToolLaunch
import Cae0.Services.Internal.Strong.Simproc._2019_06.SimProcessConfigurationManagement
import Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement
import Cae0.Services.Internal.Strong.Simproc._2020_04.SimulationToolLaunch
import Cae0.Services.Internal.Strong.Simproc._2020_12.SimStructureManagement
import Cae0.Services.Internal.Strong.Simproc._2021_06.SimDataManagement
import Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch
import Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement
import System
import System.Collections
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SimDataManagementRestBindingStub(SimDataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def ProcessCAEPackage(self, InputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageInputConfig], OutputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageOutputConfig], DatasetConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDatasetConfig], BvrConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageBVRConfig], DestinationFolder: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDestFolderConfig, DetailsLogConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDetailsLogConfig, WorkflowConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageWorkFlowConfig, ConfigObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ProcessCAEPackage(self, InputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement.Cae0PackageInputConfig2], OutputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement.Cae0PackageOutputConfig2], DatasetConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDatasetConfig], BvrConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageBVRConfig], DestinationFolder: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDestFolderConfig, DetailsLogConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDetailsLogConfig, WorkflowConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageWorkFlowConfig, ConfigObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ImportCAEData(self, ZipFileTickets: list[str], SelectedFolder: Teamcenter.Soa.Client.Model.Strong.Folder, IsAsync: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ProcessCAEPackageWithPatterns(self, InputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement.Cae0PackageInputConfig2], OutputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2021_06.SimDataManagement.Cae0PackageOutputConfig3], DatasetConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDatasetConfig], BvrConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageBVRConfig], DestinationFolder: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDestFolderConfig, DetailsLogConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDetailsLogConfig, WorkflowConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageWorkFlowConfig, PatternToCounterListMap: System.Collections.Hashtable, ConfigObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ResolveCAEPackagePatterns(self, CaePackageConfig: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, OutputDescToInputObjMap: System.Collections.Hashtable, PatternToCounterListMap: System.Collections.Hashtable) -> Cae0.Services.Internal.Strong.Simproc._2021_06.SimDataManagement.Cae0PackagePatternValuesResp: ...

class SimDataManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimDataManagementService: ...
    @typing.overload
    def ProcessCAEPackage(self, InputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageInputConfig], OutputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageOutputConfig], DatasetConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDatasetConfig], BvrConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageBVRConfig], DestinationFolder: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDestFolderConfig, DetailsLogConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDetailsLogConfig, WorkflowConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageWorkFlowConfig, ConfigObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ProcessCAEPackage(self, InputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement.Cae0PackageInputConfig2], OutputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement.Cae0PackageOutputConfig2], DatasetConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDatasetConfig], BvrConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageBVRConfig], DestinationFolder: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDestFolderConfig, DetailsLogConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDetailsLogConfig, WorkflowConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageWorkFlowConfig, ConfigObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ImportCAEData(self, ZipFileTickets: list[str], SelectedFolder: Teamcenter.Soa.Client.Model.Strong.Folder, IsAsync: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ProcessCAEPackageWithPatterns(self, InputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimDataManagement.Cae0PackageInputConfig2], OutputConfigList: list[Cae0.Services.Internal.Strong.Simproc._2021_06.SimDataManagement.Cae0PackageOutputConfig3], DatasetConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDatasetConfig], BvrConfigList: list[Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageBVRConfig], DestinationFolder: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDestFolderConfig, DetailsLogConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageDetailsLogConfig, WorkflowConfig: Cae0.Services.Internal.Strong.Simproc._2018_11.SimDataManagement.Cae0PackageWorkFlowConfig, PatternToCounterListMap: System.Collections.Hashtable, ConfigObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ResolveCAEPackagePatterns(self, CaePackageConfig: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, OutputDescToInputObjMap: System.Collections.Hashtable, PatternToCounterListMap: System.Collections.Hashtable) -> Cae0.Services.Internal.Strong.Simproc._2021_06.SimDataManagement.Cae0PackagePatternValuesResp: ...

class SimProcessConfigurationManagementRestBindingStub(SimProcessConfigurationManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def DeleteTool(self, ToolsToBDeleted: list[Teamcenter.Soa.Client.Model.ModelObject], ShouldDeleteItemAndAllRev: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def PasteTool(self, ToolsTobePasted: list[Teamcenter.Soa.Client.Model.ModelObject], TargetBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReleaseTools(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], IsReleaseAll: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReviseSimTool(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CloneTool2(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], CloneName: str, CloneItemId: str, CloneItemRevId: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateToolObjects2(self, ToolObjects: list[Cae0.Services.Internal.Strong.Simproc._2016_05.SimProcessConfigurationManagement.CAEToolConfigInfo2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetToolBOMProperties2(self, TabIdentifiers: list[str], ReleasedToolsOnly: bool) -> Cae0.Services.Internal.Strong.Simproc._2014_12.SimProcessConfigurationManagement.CAEToolBOMPropStructResponse: ...
    def UnreleaseTools(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], IsUnreleaseAll: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetCAEConfigDetail(self, ConfigItemList: list[Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision]) -> Cae0.Services.Internal.Strong.Simproc._2016_10.SimProcessConfigurationManagement.CAEConfigDetailResponse: ...
    def RetrieveConfigurationList(self, InputCriteria: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetDashboardDataForIRList(self, DashboardConfiguration: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, ItemRevisionList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Cae0.Services.Internal.Strong.Simproc._2019_06.SimProcessConfigurationManagement.SimulationDashboardDetailsResponse: ...
    def GetDashboardDataForModelStructure(self, DashboardConfiguration: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, RootBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> Cae0.Services.Internal.Strong.Simproc._2019_06.SimProcessConfigurationManagement.SimulationDashboardDetailsResponse: ...

class SimProcessConfigurationManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimProcessConfigurationManagementService: ...
    def DeleteTool(self, ToolsToBDeleted: list[Teamcenter.Soa.Client.Model.ModelObject], ShouldDeleteItemAndAllRev: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def PasteTool(self, ToolsTobePasted: list[Teamcenter.Soa.Client.Model.ModelObject], TargetBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReleaseTools(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], IsReleaseAll: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReviseSimTool(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CloneTool2(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], CloneName: str, CloneItemId: str, CloneItemRevId: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateToolObjects2(self, ToolObjects: list[Cae0.Services.Internal.Strong.Simproc._2016_05.SimProcessConfigurationManagement.CAEToolConfigInfo2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetToolBOMProperties2(self, TabIdentifiers: list[str], ReleasedToolsOnly: bool) -> Cae0.Services.Internal.Strong.Simproc._2014_12.SimProcessConfigurationManagement.CAEToolBOMPropStructResponse: ...
    def UnreleaseTools(self, ToolBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], IsUnreleaseAll: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetCAEConfigDetail(self, ConfigItemList: list[Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision]) -> Cae0.Services.Internal.Strong.Simproc._2016_10.SimProcessConfigurationManagement.CAEConfigDetailResponse: ...
    def RetrieveConfigurationList(self, InputCriteria: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetDashboardDataForIRList(self, DashboardConfiguration: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, ItemRevisionList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Cae0.Services.Internal.Strong.Simproc._2019_06.SimProcessConfigurationManagement.SimulationDashboardDetailsResponse: ...
    def GetDashboardDataForModelStructure(self, DashboardConfiguration: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, RootBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> Cae0.Services.Internal.Strong.Simproc._2019_06.SimProcessConfigurationManagement.SimulationDashboardDetailsResponse: ...

class SimProcessStatusManagementRestBindingStub(SimProcessStatusManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def DeleteSimProcessStatusObjects(self) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class SimProcessStatusManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimProcessStatusManagementService: ...
    def DeleteSimProcessStatusObjects(self) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class SimStructureManagementRestBindingStub(SimStructureManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GenerateNodeXML(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Domain: str) -> Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement.GenerateNodeXMLResponse: ...
    def GetCompositeLineNodes(self, Component: Teamcenter.Soa.Client.Model.ModelObject, FilterItemType: int, FilterRelationType: list[str], ShowRelatedAnalysisRootOnly: bool, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement.CompositeViewResponse: ...
    def GetTargetReferencesLineNodes(self, TargetReferenceLine: Teamcenter.Soa.Client.Model.ModelObject, ModelConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ProductCurrentLine: Teamcenter.Soa.Client.Model.ModelObject, ProductConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement.TargetReferencesViewDataResponse: ...
    def GetCompositeLineNodesExpandBelow2(self, Component: Teamcenter.Soa.Client.Model.ModelObject, FilterItemType: int, FilterRelationType: list[str], ShowRelatedAnalysisAll: bool, ShowRelatedAnalysisRootOnly: bool, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ColumnNames: list[str]) -> Cae0.Services.Internal.Strong.Simproc._2016_03.SimStructureManagement.CompositeViewResponse2: ...
    def GetTargetRefLineNodesExpandBelow2(self, TargetReferenceLine: Teamcenter.Soa.Client.Model.ModelObject, ModelConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ProductCurrentLine: Teamcenter.Soa.Client.Model.ModelObject, ProductConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ColumnNames: list[str]) -> Cae0.Services.Internal.Strong.Simproc._2016_03.SimStructureManagement.TargetReferencesViewDataResponse2: ...
    def CreateDerivedStructures(self, RootBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, SelectedRule: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, SelectedVarConfig: str, VarConfigDetails: str, NumOfStructs: int, OptionalRootName: str, OptionalIndex: str, UseAutoIndex: bool) -> Cae0.Services.Internal.Strong.Simproc._2017_05.SimStructureManagement.DeriveResponse: ...
    def HighlightModelStructure(self, ModelRoot: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> Cae0.Services.Internal.Strong.Simproc._2017_05.SimStructureManagement.HighlightModelResponse: ...
    def ExecuteStructureMapOnSelection(self, StructureMapInputs: Cae0.Services.Internal.Strong.Simproc._2017_11.SimStructureManagement.StructureMapInputsInfo2) -> Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapExecutionResponse: ...
    def GenerateNodeXMLWithFocus(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Domain: str, Focus: str) -> Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement.GenerateNodeXMLResponse: ...
    def GetFileDetails2(self, InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Cae0.Services.Internal.Strong.Simproc._2018_06.SimStructureManagement.GetFileDetailsResponse2: ...
    def RemoveDuplicateCadJt(self, SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Cae0.Services.Internal.Strong.Simproc._2018_06.SimStructureManagement.RemoveDuplicateCadJtResponse: ...
    def ExecuteStructMapWithInclusionRule(self, StructureMapInputs: Cae0.Services.Internal.Strong.Simproc._2017_11.SimStructureManagement.StructureMapInputsInfo2, InclusionRuleInputs: Cae0.Services.Internal.Strong.Simproc._2018_11.SimStructureManagement.StructureMapFilterInclusionRuleInfo) -> Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapExecutionResponse: ...
    def GetFileDetails3(self, InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Cae0.Services.Internal.Strong.Simproc._2020_12.SimStructureManagement.GetFileDetailsResponse3: ...

class SimStructureManagementService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimStructureManagementService: ...
    def GenerateNodeXML(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Domain: str) -> Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement.GenerateNodeXMLResponse: ...
    def GetCompositeLineNodes(self, Component: Teamcenter.Soa.Client.Model.ModelObject, FilterItemType: int, FilterRelationType: list[str], ShowRelatedAnalysisRootOnly: bool, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement.CompositeViewResponse: ...
    def GetTargetReferencesLineNodes(self, TargetReferenceLine: Teamcenter.Soa.Client.Model.ModelObject, ModelConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ProductCurrentLine: Teamcenter.Soa.Client.Model.ModelObject, ProductConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement.TargetReferencesViewDataResponse: ...
    def GetCompositeLineNodesExpandBelow2(self, Component: Teamcenter.Soa.Client.Model.ModelObject, FilterItemType: int, FilterRelationType: list[str], ShowRelatedAnalysisAll: bool, ShowRelatedAnalysisRootOnly: bool, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ColumnNames: list[str]) -> Cae0.Services.Internal.Strong.Simproc._2016_03.SimStructureManagement.CompositeViewResponse2: ...
    def GetTargetRefLineNodesExpandBelow2(self, TargetReferenceLine: Teamcenter.Soa.Client.Model.ModelObject, ModelConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ProductCurrentLine: Teamcenter.Soa.Client.Model.ModelObject, ProductConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ColumnNames: list[str]) -> Cae0.Services.Internal.Strong.Simproc._2016_03.SimStructureManagement.TargetReferencesViewDataResponse2: ...
    def CreateDerivedStructures(self, RootBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, SelectedRule: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, SelectedVarConfig: str, VarConfigDetails: str, NumOfStructs: int, OptionalRootName: str, OptionalIndex: str, UseAutoIndex: bool) -> Cae0.Services.Internal.Strong.Simproc._2017_05.SimStructureManagement.DeriveResponse: ...
    def HighlightModelStructure(self, ModelRoot: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> Cae0.Services.Internal.Strong.Simproc._2017_05.SimStructureManagement.HighlightModelResponse: ...
    def ExecuteStructureMapOnSelection(self, StructureMapInputs: Cae0.Services.Internal.Strong.Simproc._2017_11.SimStructureManagement.StructureMapInputsInfo2) -> Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapExecutionResponse: ...
    def GenerateNodeXMLWithFocus(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Domain: str, Focus: str) -> Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement.GenerateNodeXMLResponse: ...
    def GetFileDetails2(self, InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Cae0.Services.Internal.Strong.Simproc._2018_06.SimStructureManagement.GetFileDetailsResponse2: ...
    def RemoveDuplicateCadJt(self, SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Cae0.Services.Internal.Strong.Simproc._2018_06.SimStructureManagement.RemoveDuplicateCadJtResponse: ...
    def ExecuteStructMapWithInclusionRule(self, StructureMapInputs: Cae0.Services.Internal.Strong.Simproc._2017_11.SimStructureManagement.StructureMapInputsInfo2, InclusionRuleInputs: Cae0.Services.Internal.Strong.Simproc._2018_11.SimStructureManagement.StructureMapFilterInclusionRuleInfo) -> Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapExecutionResponse: ...
    def GetFileDetails3(self, InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Cae0.Services.Internal.Strong.Simproc._2020_12.SimStructureManagement.GetFileDetailsResponse3: ...

class SimulationToolLaunchRestBindingStub(SimulationToolLaunchService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ImportSimulationToolLaunchOutputs(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, WorkingDirectory: str, InputObject: Teamcenter.Soa.Client.Model.ModelObject, XmlFileName: str, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, JobID: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ExportObjectsToPLMXMLForToolLaunch(self, PlmxmlFileName: str, TransferMode: str, ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject], CheckOutOnExport: bool, ToolName: str, LogFileTickets: list[str]) -> Cae0.Services.Internal.Strong.Simproc._2017_05.SimulationToolLaunch.ExportObjectsToPLMXMLResponse: ...
    def GetValidToolsForStructureMap(self) -> Cae0.Services.Internal.Strong.Simproc._2018_11.SimulationToolLaunch.ToolsForStructureMapResponse: ...
    def ExportAndCheckoutPLMXMLWithDSM(self, PlmxmlFileName: str, TransferMode: str, ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject], CheckOutOnExport: bool, ToolName: str, LogFileTickets: list[str], SessionOptions: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimulationToolLaunch.NameAndValue]) -> Cae0.Services.Internal.Strong.Simproc._2017_05.SimulationToolLaunch.ExportObjectsToPLMXMLResponse: ...
    def ExportMaterialsForToolLaunch(self, MaterialsObjects: list[Teamcenter.Soa.Client.Model.ModelObject], MaterialExportFileName: str, MaterialExportFilterName: str) -> Cae0.Services.Internal.Strong.Simproc._2020_04.SimulationToolLaunch.ExportMaterialResponse: ...
    def ImportAndCheckinPLMXMLwithDSM(self, XmlFileTicket: str, NamedRefFileTickets: list[str], LogFileTickets: list[str], TransferMode: str, CheckInOnImport: bool, PerformCancelCheckOut: bool, SessionOptions: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimulationToolLaunch.NameAndValue]) -> Cae0.Services.Internal.Strong.Simproc._2020_04.SimulationToolLaunch.ImportObjectsFromPLMXMLResponse2: ...

class SimulationToolLaunchService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimulationToolLaunchService: ...
    def ImportSimulationToolLaunchOutputs(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, WorkingDirectory: str, InputObject: Teamcenter.Soa.Client.Model.ModelObject, XmlFileName: str, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, JobID: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ExportObjectsToPLMXMLForToolLaunch(self, PlmxmlFileName: str, TransferMode: str, ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject], CheckOutOnExport: bool, ToolName: str, LogFileTickets: list[str]) -> Cae0.Services.Internal.Strong.Simproc._2017_05.SimulationToolLaunch.ExportObjectsToPLMXMLResponse: ...
    def GetValidToolsForStructureMap(self) -> Cae0.Services.Internal.Strong.Simproc._2018_11.SimulationToolLaunch.ToolsForStructureMapResponse: ...
    def ExportAndCheckoutPLMXMLWithDSM(self, PlmxmlFileName: str, TransferMode: str, ObjectsToExport: list[Teamcenter.Soa.Client.Model.ModelObject], CheckOutOnExport: bool, ToolName: str, LogFileTickets: list[str], SessionOptions: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimulationToolLaunch.NameAndValue]) -> Cae0.Services.Internal.Strong.Simproc._2017_05.SimulationToolLaunch.ExportObjectsToPLMXMLResponse: ...
    def ExportMaterialsForToolLaunch(self, MaterialsObjects: list[Teamcenter.Soa.Client.Model.ModelObject], MaterialExportFileName: str, MaterialExportFilterName: str) -> Cae0.Services.Internal.Strong.Simproc._2020_04.SimulationToolLaunch.ExportMaterialResponse: ...
    def ImportAndCheckinPLMXMLwithDSM(self, XmlFileTicket: str, NamedRefFileTickets: list[str], LogFileTickets: list[str], TransferMode: str, CheckInOnImport: bool, PerformCancelCheckOut: bool, SessionOptions: list[Cae0.Services.Internal.Strong.Simproc._2020_04.SimulationToolLaunch.NameAndValue]) -> Cae0.Services.Internal.Strong.Simproc._2020_04.SimulationToolLaunch.ImportObjectsFromPLMXMLResponse2: ...

