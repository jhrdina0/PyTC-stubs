import System
import System.Collections
import Teamcenter.Schemas.Soa._2011_06.Metamodel
import Teamcenter.Services.Strong.Core._2006_03.DataManagement
import Teamcenter.Services.Strong.Core._2006_03.FileManagement
import Teamcenter.Services.Strong.Core._2006_03.Reservation
import Teamcenter.Services.Strong.Core._2006_03.Session
import Teamcenter.Services.Strong.Core._2007_01.DataManagement
import Teamcenter.Services.Strong.Core._2007_01.FileManagement
import Teamcenter.Services.Strong.Core._2007_01.ManagedRelations
import Teamcenter.Services.Strong.Core._2007_01.Session
import Teamcenter.Services.Strong.Core._2007_06.DataManagement
import Teamcenter.Services.Strong.Core._2007_06.LOV
import Teamcenter.Services.Strong.Core._2007_06.PropDescriptor
import Teamcenter.Services.Strong.Core._2007_09.DataManagement
import Teamcenter.Services.Strong.Core._2007_09.ProjectLevelSecurity
import Teamcenter.Services.Strong.Core._2007_12.DataManagement
import Teamcenter.Services.Strong.Core._2007_12.Session
import Teamcenter.Services.Strong.Core._2008_03.Session
import Teamcenter.Services.Strong.Core._2008_06.DataManagement
import Teamcenter.Services.Strong.Core._2008_06.DispatcherManagement
import Teamcenter.Services.Strong.Core._2008_06.ManagedRelations
import Teamcenter.Services.Strong.Core._2008_06.PropDescriptor
import Teamcenter.Services.Strong.Core._2008_06.Session
import Teamcenter.Services.Strong.Core._2008_06.StructureManagement
import Teamcenter.Services.Strong.Core._2009_04.ProjectLevelSecurity
import Teamcenter.Services.Strong.Core._2009_10.DataManagement
import Teamcenter.Services.Strong.Core._2009_10.ProjectLevelSecurity
import Teamcenter.Services.Strong.Core._2010_04.DataManagement
import Teamcenter.Services.Strong.Core._2010_04.LanguageInformation
import Teamcenter.Services.Strong.Core._2010_04.Session
import Teamcenter.Services.Strong.Core._2010_09.DataManagement
import Teamcenter.Services.Strong.Core._2011_06.DataManagement
import Teamcenter.Services.Strong.Core._2011_06.LOV
import Teamcenter.Services.Strong.Core._2011_06.OperationDescriptor
import Teamcenter.Services.Strong.Core._2011_06.PropDescriptor
import Teamcenter.Services.Strong.Core._2011_06.Reservation
import Teamcenter.Services.Strong.Core._2011_06.Session
import Teamcenter.Services.Strong.Core._2012_02.DataManagement
import Teamcenter.Services.Strong.Core._2012_02.OperationDescriptor
import Teamcenter.Services.Strong.Core._2012_02.Session
import Teamcenter.Services.Strong.Core._2012_09.DataManagement
import Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity
import Teamcenter.Services.Strong.Core._2012_10.DataManagement
import Teamcenter.Services.Strong.Core._2013_05.DataManagement
import Teamcenter.Services.Strong.Core._2013_05.LOV
import Teamcenter.Services.Strong.Core._2014_06.DataManagement
import Teamcenter.Services.Strong.Core._2014_06.DigitalSignature
import Teamcenter.Services.Strong.Core._2014_10.DataManagement
import Teamcenter.Services.Strong.Core._2015_07.DataManagement
import Teamcenter.Services.Strong.Core._2015_10.DataManagement
import Teamcenter.Services.Strong.Core._2015_10.FileManagement
import Teamcenter.Services.Strong.Core._2016_05.DataManagement
import Teamcenter.Services.Strong.Core._2016_09.DataManagement
import Teamcenter.Services.Strong.Core._2017_05.FileManagement
import Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity
import Teamcenter.Services.Strong.Core._2017_11.LogicalObject
import Teamcenter.Services.Strong.Core._2018_06.DataManagement
import Teamcenter.Services.Strong.Core._2018_06.LogicalObject
import Teamcenter.Services.Strong.Core._2018_11.LogicalObject
import Teamcenter.Services.Strong.Core._2018_11.ProjectLevelSecurity
import Teamcenter.Services.Strong.Core._2019_06.DataManagement
import Teamcenter.Services.Strong.Core._2019_06.Session
import Teamcenter.Services.Strong.Core._2020_01.DataManagement
import Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity
import Teamcenter.Services.Strong.Core._2020_04.DataManagement
import Teamcenter.Services.Strong.Core._2021_06.DataManagement
import Teamcenter.Services.Strong.Core._2021_12.LOV
import Teamcenter.Services.Strong.Core._2021_12.Session
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import Teamcenter.Soa.Common
import typing

class DataManagementRestBindingStub(DataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def SetDisplayProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateDatasets(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.DatasetProperties]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateDatasetsResponse: ...
    @typing.overload
    def CreateDatasets(self, Input: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.DatasetInfo]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.CreateDatasetsResponse: ...
    def CreateFolders(self, Folders: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateFolderInput], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateFoldersResponse: ...
    def ChangeOwnership(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.ObjectOwner]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateItems(self, Properties: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.ItemProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateItemsResponse: ...
    def GenerateItemIdsAndInitialRevisionIds(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.GenerateItemIdsAndInitialRevisionIdsProperties]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.GenerateItemIdsAndInitialRevisionIdsResponse: ...
    def GenerateRevisionIds(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.GenerateRevisionIdsProperties]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.GenerateRevisionIdsResponse: ...
    def DeleteObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateRelations(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.Relationship]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateRelationsResponse: ...
    def DeleteRelations(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.Relationship]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def Revise(self, Input: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.ReviseResponse: ...
    @typing.overload
    def SetProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetProperties(self, Info: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.PropInfo], Options: list[str]) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.SetPropertyResponse: ...
    def GenerateUID(self, NUID: int) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.GenerateUIDResponse: ...
    def GetDatasetCreationRelatedInfo(self, TypeName: str, ParentObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetDatasetCreationRelatedInfoResponse: ...
    def MoveToNewFolder(self, MoveToNewFolderInfos: list[Teamcenter.Services.Strong.Core._2007_01.DataManagement.MoveToNewFolderInfo]) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.MoveToNewFolderResponse: ...
    def CreateOrUpdateForms(self, Info: list[Teamcenter.Services.Strong.Core._2007_01.DataManagement.FormInfo]) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.CreateOrUpdateFormsResponse: ...
    def GetItemCreationRelatedInfo(self, TypeName: str, ParentObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemCreationRelatedInfoResponse: ...
    def GetItemFromId(self, Infos: list[Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemFromIdInfo], NRev: int, Pref: Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemFromIdPref) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemFromIdResponse: ...
    def SaveAsNewItem(self, Info: list[Teamcenter.Services.Strong.Core._2007_01.DataManagement.SaveAsNewItemInfo]) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.SaveAsNewItemResponse: ...
    def RefreshObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def WhereUsed(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], NumLevels: int, WhereUsedPrecise: bool, Rule: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.WhereUsedResponse: ...
    @typing.overload
    def WhereUsed(self, Input: list[Teamcenter.Services.Strong.Core._2012_02.DataManagement.WhereUsedInputData], ConfigParams: Teamcenter.Services.Strong.Core._2012_02.DataManagement.WhereUsedConfigParameters) -> Teamcenter.Services.Strong.Core._2012_02.DataManagement.WhereUsedResponse: ...
    def WhereReferenced(self, Objects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject], NumLevels: int) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.WhereReferencedResponse: ...
    @typing.overload
    def ExpandGRMRelationsForPrimary(self, PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Core._2007_06.DataManagement.ExpandGRMRelationsPref) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.ExpandGRMRelationsResponse: ...
    @typing.overload
    def ExpandGRMRelationsForPrimary(self, PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Core._2007_09.DataManagement.ExpandGRMRelationsPref2) -> Teamcenter.Services.Strong.Core._2007_09.DataManagement.ExpandGRMRelationsResponse2: ...
    def GetAvailableTypes(self, Classes: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.BaseClassInput]) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.GetAvailableTypesResponse: ...
    def PurgeSequences(self, Objects: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.PurgeSequencesInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetOrRemoveImmunity(self, Objects: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.SetOrRemoveImmunityInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetDatasetTypeInfo(self, DatasetTypeNames: list[str]) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.DatasetTypeInfoResponse: ...
    def ValidateItemIdsAndRevIds(self, Infos: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.ValidateIdsInfo]) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.ValidateItemIdsAndRevIdsResponse: ...
    @typing.overload
    def ExpandGRMRelationsForSecondary(self, SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Core._2007_06.DataManagement.ExpandGRMRelationsPref) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.ExpandGRMRelationsResponse: ...
    @typing.overload
    def ExpandGRMRelationsForSecondary(self, SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Core._2007_09.DataManagement.ExpandGRMRelationsPref2) -> Teamcenter.Services.Strong.Core._2007_09.DataManagement.ExpandGRMRelationsResponse2: ...
    def WhereReferencedByRelationName(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.WhereReferencedByRelationNameInfo], NumLevels: int) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.WhereReferencedByRelationNameResponse: ...
    def RemoveNamedReferenceFromDataset(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_09.DataManagement.RemoveNamedReferenceFromDatasetInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def LoadObjects(self, Uids: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateAlternateIdentifiers(self, Input: list[Teamcenter.Services.Strong.Core._2007_12.DataManagement.AlternateIdentifiersInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ListAlternateIdDisplayRules(self, Input: Teamcenter.Services.Strong.Core._2007_12.DataManagement.ListAlternateIdDisplayRulesInfo) -> Teamcenter.Services.Strong.Core._2007_12.DataManagement.ListAlternateIdDisplayRulesResponse: ...
    def ValidateAlternateIds(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_12.DataManagement.ValidateAlternateIdInput]) -> Teamcenter.Services.Strong.Core._2007_12.DataManagement.ValidateAlternateIdResponse: ...
    def GetContextsAndIdentifierTypes(self, TypeTags: list[Teamcenter.Soa.Client.Model.Strong.ImanType]) -> Teamcenter.Services.Strong.Core._2007_12.DataManagement.GetContextAndIdentifiersResponse: ...
    def UnloadObjects(self, ObjsToUnload: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def FindDisplayableSubBusinessObjects(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.BOWithExclusionIn]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.DisplayableSubBOsResponse: ...
    def CreateDatasets2(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.DatasetProperties2]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateDatasetsResponse: ...
    def GetItemAndRelatedObjects(self, Infos: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetItemAndRelatedObjectsInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetItemAndRelatedObjectsResponse: ...
    def Revise2(self, Info: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.ReviseInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.ReviseResponse2: ...
    def SaveAsNewItem2(self, Info: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.SaveAsNewItemInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.SaveAsNewItemResponse2: ...
    def GetNextIds(self, VInfoForNextId: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.InfoForNextId]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetNextIdsResponse: ...
    def GetNRPatternsWithCounters(self, VAttachInfo: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.NRAttachInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetNRPatternsWithCountersResponse: ...
    def GetRevNRAttachDetails(self, TypeAndItemRevInfos: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.TypeAndItemRevInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetRevNRAttachResponse: ...
    def CreateOrUpdateRelations(self, Infos: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateOrUpdateRelationsInfo], Sync: bool) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateOrUpdateRelationsResponse: ...
    def CreateConnections(self, Properties: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.ConnectionProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateConnectionsResponse: ...
    def CreateOrUpdateGDELinks(self, GdeLinkInfos: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.GDELinkInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateOrUpdateGDELinksResponse: ...
    def CreateOrUpdateItemElements(self, Properties: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.ItemElementProperties]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateOrUpdateItemElementsResponse: ...
    @typing.overload
    def CreateObjects(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateIn]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    @typing.overload
    def CreateObjects(self, CreateInputs: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateIn], RunInBackground: bool) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    def AddParticipants(self, AddParticipantInfo: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.AddParticipantInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.AddParticipantOutput: ...
    def RemoveParticipants(self, Participants: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.Participants]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetTableProperties(self, TableData: list[Teamcenter.Services.Strong.Core._2009_10.DataManagement.TableInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetItemFromAttribute(self, Infos: list[Teamcenter.Services.Strong.Core._2009_10.DataManagement.GetItemFromAttributeInfo], NRev: int, Pref: Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemFromIdPref) -> Teamcenter.Services.Strong.Core._2009_10.DataManagement.GetItemFromAttributeResponse: ...
    def GetTableProperties(self, Table: list[Teamcenter.Soa.Client.Model.Strong.Table]) -> Teamcenter.Services.Strong.Core._2009_10.DataManagement.GetTablePropertiesResponse: ...
    def FindDisplayableSubBusinessObjectsWithDisplayNames(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.BOWithExclusionIn]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.DisplayableSubBusinessObjectsResponse: ...
    def GetAvailableTypesWithDisplayNames(self, Classes: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.BaseClassInput]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.GetAvailableBusinessObjectTypesResponse: ...
    def GetDatasetCreationRelatedInfo2(self, TypeName: str, ParentObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.GetDatasetCreationRelatedInfoResponse2: ...
    def GetLocalizedProperties(self, Info: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.PropertyInfo]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizedPropertyValuesList: ...
    def IsPropertyLocalizable(self, InputInfo: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizableStatusInput]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizableStatusResponse: ...
    def SetLocalizedProperties(self, Info: Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizedPropertyValuesInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetLocalizedPropertyValues(self, Info: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizedPropertyValuesInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def VerifyExtension(self, ExtensionInfo: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.VerifyExtensionInfo]) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.VerifyExtensionResponse: ...
    def CreateOrUpdateStaticTableData(self, StaticTableInfo: Teamcenter.Services.Strong.Core._2010_09.DataManagement.StaticTableInfo, RowProperties: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.RowData]) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.CreateOrUpdateStaticTableDataResponse: ...
    def GetEventTypes(self, Input: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.EventObject]) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.EventTypesResponse: ...
    def PostEvent(self, Input: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.PostEventObjectProperties], EventTypeName: str) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.PostEventResponse: ...
    def GetStaticTableData(self, StaticTable: Teamcenter.Soa.Client.Model.Strong.Fnd0StaticTable) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.StaticTableDataResponse: ...
    def ValidateRevIds(self, Inputs: list[Teamcenter.Services.Strong.Core._2011_06.DataManagement.ValidateRevIdsInfo]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.ValidateRevIdsResponse: ...
    def SaveAsObjects(self, SaveAsIn: list[Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsIn]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsObjectsResponse: ...
    @typing.overload
    def GetTraceReport(self, Input: Teamcenter.Services.Strong.Core._2011_06.DataManagement.TraceabilityInfoInput) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.TraceabilityReportOutput: ...
    @typing.overload
    def GetTraceReport(self, Input: list[Teamcenter.Services.Strong.Core._2012_10.DataManagement.TraceabilityInfoInput1]) -> Teamcenter.Services.Strong.Core._2012_10.DataManagement.TraceabilityReportOutput1: ...
    def ValidateIdValue(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateIn]) -> Teamcenter.Services.Strong.Core._2012_02.DataManagement.ValidationResponse: ...
    def BulkCreateObjects(self, Input: list[Teamcenter.Services.Strong.Core._2012_02.DataManagement.BulkCreIn]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    def SaveAsObjectAndRelate(self, SaveAsInput: list[Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsIn], RelateInfo: list[Teamcenter.Services.Strong.Core._2012_09.DataManagement.RelateInfoIn]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsObjectsResponse: ...
    def GetDatasetTypesWithFileExtension(self, FileExtensions: list[str]) -> Teamcenter.Services.Strong.Core._2012_10.DataManagement.GetDatasetTypesWithFileExtensionResponse: ...
    def RefreshObjects2(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], LockObjects: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPasteRelations(self, Inputs: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetPasteRelationsInputData]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetPasteRelationsResponse: ...
    def ReviseObjects(self, ReviseIn: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.ReviseIn]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.ReviseObjectsResponse: ...
    def ValidateValues(self, Inputs: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.ValidateInput]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.ValidateValuesResponse: ...
    def GetChildren(self, Inputs: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetChildrenInputData]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetChildrenResponse: ...
    def GetSubTypeNames(self, InBOTypeNames: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.SubTypeNamesInput]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.SubTypeNamesResponse: ...
    def GenerateNextValues(self, GenerateNextValuesIn: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.GenerateNextValuesIn]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.GenerateNextValuesResponse: ...
    def GetTraceReport2(self, Input: list[Teamcenter.Services.Strong.Core._2012_10.DataManagement.TraceabilityInfoInput1]) -> Teamcenter.Services.Strong.Core._2014_06.DataManagement.TraceabilityReportOutput2: ...
    def GetTraceReportLegacy(self, Input: Teamcenter.Services.Strong.Core._2011_06.DataManagement.TraceabilityInfoInput) -> Teamcenter.Services.Strong.Core._2014_06.DataManagement.TraceabilityReportOutputLegacy: ...
    def AddChildren(self, InputData: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.ChildrenInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPasteRelations2(self, Inputs: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetPasteRelationsInputData]) -> Teamcenter.Services.Strong.Core._2014_10.DataManagement.GetPasteRelationsResponse2: ...
    def RemoveChildren(self, InputData: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.ChildrenInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GenerateIdsUsingIDGenerationRules(self, GenerateIdsInputs: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.GenerateIdInput]) -> Teamcenter.Services.Strong.Core._2014_10.DataManagement.GenerateIdsResponse: ...
    @typing.overload
    def GetDeepCopyData(self, DeepCopyDataInput: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.DeepCopyDataInput]) -> Teamcenter.Services.Strong.Core._2014_10.DataManagement.GetDeepCopyDataResponse: ...
    @typing.overload
    def GetDeepCopyData(self, DeepCopyDataInput: Teamcenter.Services.Strong.Core._2015_07.DataManagement.DeepCopyDataInput) -> Teamcenter.Services.Strong.Core._2015_07.DataManagement.GetDeepCopyDataResponse: ...
    def SaveAsObjectsAndRelate(self, IVecSoaSavAsIn: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.SaveAsIn], IVecSoaRelteInfoIn: list[Teamcenter.Services.Strong.Core._2012_09.DataManagement.RelateInfoIn]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsObjectsResponse: ...
    def PruneNamedReferences(self, NamedReferences: list[Teamcenter.Soa.Client.Model.Strong.POM_object]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetLocalizedProperties2(self, PropertyInfo: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.PropertyInfo]) -> Teamcenter.Services.Strong.Core._2015_07.DataManagement.LocalizedPropertyValuesResponse: ...
    def GetCreatbleSubBuisnessObjectNames(self, Input: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreatableSubBONamesInput]) -> Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreatableSubBONamesResponse: ...
    def GenerateNextValuesForProperties(self, PropertyNamingRuleInfo: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.PropertyNamingruleInfo]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.GenerateNextValuesResponse: ...
    def GetDomainOfObjectOrType(self, Inputs: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.GetDomainInput]) -> Teamcenter.Services.Strong.Core._2015_07.DataManagement.DomainOfObjectOrTypeResponse: ...
    def CreateRelateAndSubmitObjects2(self, CreateInputs: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreateIn2]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    def ReassignParticipants(self, ReassignParticipantInfo: list[Teamcenter.Services.Strong.Core._2015_10.DataManagement.ReassignParticipantInfo]) -> Teamcenter.Services.Strong.Core._2015_10.DataManagement.ReassignParticipantResponse: ...
    def GenerateContextSpecificIDs(self, GenerateContextIDsIn: list[Teamcenter.Services.Strong.Core._2016_05.DataManagement.GenerateContextIDsInput]) -> Teamcenter.Services.Strong.Core._2016_05.DataManagement.GenerateContextSpecificIDsResponse: ...
    def ResetContextID(self, ContextNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetPropertiesAndDetectOverwrite(self, PropData: list[Teamcenter.Services.Strong.Core._2016_05.DataManagement.PropData], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Core._2016_05.DataManagement.SetPropsAndDetectOverwriteResponse: ...
    def CreateAttachAndSubmitObjects(self, Inputs: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreateIn2]) -> Teamcenter.Services.Strong.Core._2016_09.DataManagement.CreateAttachResponse: ...
    def CreateObjectsInBulkAndRelate(self, CreateInputs: list[Teamcenter.Services.Strong.Core._2018_06.DataManagement.CreateIn3]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    def UnlinkAndDeleteObjects(self, DeleteInput: list[Teamcenter.Services.Strong.Core._2019_06.DataManagement.DeleteIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateIdDisplayRules(self, IdDispRuleCreIns: list[Teamcenter.Services.Strong.Core._2020_01.DataManagement.IDDispRuleCreateIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetIdentifierTypes(self, IdentifierTypesIn: list[Teamcenter.Services.Strong.Core._2020_01.DataManagement.IdentifierTypesIn]) -> Teamcenter.Services.Strong.Core._2020_01.DataManagement.IdentifierTypesOut: ...
    def GetIdContexts(self, InputObjs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Teamcenter.Services.Strong.Core._2020_01.DataManagement.IDContextOutput: ...
    def GenerateContextSpecificIDs2(self, GenerateContextIDsIn: list[Teamcenter.Services.Strong.Core._2020_04.DataManagement.GenerateContextIDsInput2]) -> Teamcenter.Services.Strong.Core._2016_05.DataManagement.GenerateContextSpecificIDsResponse: ...
    def AddNamedReferenceToDatasets(self, AddNamedReferenceIn: list[Teamcenter.Services.Strong.Core._2021_06.DataManagement.AddNamedReferenceToDatasetInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveNamedReferenceFromDataset2(self, RemoveNamedReferenceIn: list[Teamcenter.Services.Strong.Core._2021_06.DataManagement.RemoveNamedReferenceFromDataset]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class DataManagementService:
    """
    
            The DataManagement service provides a broad
            range of operations to manage data throughout its life cycle in Teamcenter from data
            creation to data retrieval. The applications or clients can create, store, retrieve
            and manipulate data using the operations as organizational resource interactively.
            The data can be any business object such as an Item, ItemRevision,
            Dataset, Form, Folder, etc.
            

            The operations in this service allow creation (or bulk creation), modification and
            deletion of all business objects. This service also provides operations to revise,
            save as, and query for all business objects, to get details of a specific business
            object's information such as property values, to expand GRM relations for primary/secondary
            business objects and to find where the business objects are used/referenced, etc.
            

            The DataManagement service can be used for
            supporting following main use-cases:
            

Create/update/delete a business object
            
Load/unload/refresh/revise/save as/validate business object
            
Find and expand business object GRM relationship
            
Get details of a business object such as type info, attribute values,
            next ids, dataset files, localized properties, Organization information, etc.
            
Remove Named Reference from a Dataset

Add and remove Participants, change ownership
            
Generate UIDs/Revision Ids
            




Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DataManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def SetDisplayProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is provided to update the Teamcenter objects for the given name/display
             value pairs. This operation works for all supported property value types to set display
             values. When setting this operation it invokes the server PROP_UIF_set_value
             extensions. For updating an array property, display values need to be comma (,) separated
             which server parses them into individual values before assigning.
             
             Note:  Since LOVs support the display as feature where internal values of
             the LOV can be different from displayable values, this operation expects that internal
             value of the selection to be passed and not the display value.
             

        :param Objects: 
                         A list of objects for which property values need to be set
             
        :param Attributes: 
                         A map of attribute names and display values of a property  (string/string)
             
        :return: Objects that successfully have properties set are returned in the ServiceData list
             of updated objects.  Any failures will be returned with the input object mapped to
             the error message in the ServiceData list of partial errors.
        """
        ...
    @typing.overload
    def CreateDatasets(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.DatasetProperties]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateDatasetsResponse: ...
    @typing.overload
    def CreateDatasets(self, Input: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.DatasetInfo]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.CreateDatasetsResponse: ...
    def CreateFolders(self, Folders: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateFolderInput], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateFoldersResponse:
        """    
             This operation creates a list of new Folder objects with the given names,
             descriptions and attaches them to the parent container. If attaching a created Folder
             to its parent container fails, the Folder will not be deleted.
             

Teamcenter Component:

             Core Model Folder - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component covers Folders.
             
        :param Folders: 
                         Input struture to create <b>Folder</b> Objects
             
        :param Container: 
                         The object to which all the created <b>Folder</b> objects will be related to via
                         the input relation type, may be null.
             
        :param RelationType: 
                         The name of relation type that all created <b>Folder</b> objects will be related
                         to the container, may be an empty string.
             
        :return: 
        """
        ...
    def ChangeOwnership(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.ObjectOwner]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation can be used to change the ownership on a given business object to
             the given user and group.  Owning user attribute on the business object will be changed
             to the given user and owning group attribute is changed to the given group.  The
             user needs CHANGE_OWNER privilege and WRITE privilege on the business
             object to be able to change its ownership.  If user does not have the required privileges
             then this operation will return error code 515001. If the given user is invalid
             or given group is invalid then this operation will return error code 515024.
             

Use Cases:

             Change owner menu action calls this operation.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param Input: 
                         Input object to the operation that holds the business object, new owning user and
                         new owning group.
             
        :return: This operation returns ServiceData object.  If the object's ownership is changed
             successfully then the object is returned in the updated objects list in the ServiceData.
             Any failure will be returned with the input object mapped to the error message in
             the list of partial errors in the ServiceData.
        """
        ...
    def GetProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation is provided to get property values of instances outside of
             the current object property policy for a particular business object.  Net
             result of this operation includes the properties expressly defined in the input attributes
             as well as the properties defined in the current Object Property Policy.
             

             This operation takes care of following:
             

Since all relations are stored as properties on the primary object,
             this operation supports the expanding of relations.
             
Properties in the input attribute argument that reference other objects
             (relations) will have the properties for those referenced objects returned as defined
             by the Object Property Policy.
             


Limitation:


Classification objects attached to WorkspaceObjects using "IMAN_classification"
             relation are not returned by this operation. User need to use findClassificationObjects
             operation from Classification service to retrieve properties of such objects. For
             more information about findClassificationObjects operation please refer classification
             service guide.
             



Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param Objects: 
                         List of attribute/property name strings for which values are needed
             
        :param Attributes: 
                         List of object references for which property values are requested
             
        :return: Objects that successfully have properties added are returned in the ServiceData list
             of plain objects.  Any failures will be returned with the input object mapped to
             the error message in the ServiceData list of partial errors.
        """
        ...
    def CreateItems(self, Properties: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.ItemProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateItemsResponse:
        """    
             This operation creates a list of Items and associated data (ItemRevision/ItemMasterForm/ItemRevisionMasterForm)
             based on the input attribute structures and the specified relation type between created
             Item and input object.  If container and relation type are not input, none
             of the Items will be related to a container. (There is no default, if any
             destination is desired, it must be provided as input). Note: createItems are for
             items creation, if a compound object such as ItemRevision adds a required
             property in BMIDE, createItems will fail since it only accepts required properties
             for item types, not for its associated data such as ItemRevision. Also, if
             any other properties including object description and custom properties are
             added as required on Item, createItems will fail. In this case, user
             should use createObjects instead.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Properties: 
                         A list of properties to create new <b>Item</b> objects
             
        :param Container: 
                         The container object to which all the items will be related to via the input relation
                         type, optional.
             
        :param RelationType: 
                         The relation type that will be used to relate the newly created <b>Item</b>s to the
                         container, optional.
             
        :return: list of partial errors.
        """
        ...
    def GenerateItemIdsAndInitialRevisionIds(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.GenerateItemIdsAndInitialRevisionIdsProperties]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.GenerateItemIdsAndInitialRevisionIdsResponse:
        """    
             This operation generates a list of Item IDs and initial ItemRevision
             IDs.  The initial revision ID is defined as the first revision ID for the given type.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Input: 
                         A list of the <b>Item</b>, <b>Item</b> type, and the number of IDs to generate.
             
        :return: IDs.
        """
        ...
    def GenerateRevisionIds(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.GenerateRevisionIdsProperties]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.GenerateRevisionIdsResponse:
        """    
             This operation generates a set of revision IDs.  The ID can be either the next ID
             for an existing Item or the first revision ID for a new Item.
             

Dependencies:

             revise, revise2
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Input: 
                         A list <b>Item</b> and <b>Item</b> type
             
        :return: 
        """
        ...
    def DeleteObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the input objects.  In the case of Item, it also deletes
             all ItemRevision objects,  associated ItemMaster, ItemRevisionMaster
             forms, and Dataset objects.  The input object can be an ImanRelation.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param Objects: 
                         A list of objects to be deleted
             
        :return: . Any errors that occur will be
             returned as a partial error with the source business object attached to the partial
             error.
        """
        ...
    def CreateRelations(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.Relationship]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateRelationsResponse:
        """    
             Creates the specified relation between the input objects (primary and secondary objects).
             If the relation name is not specified then default relation name specified in either
             the preference ParentTypeName_ChildTypeName_default_relation or ParentTypeName_default_relation
             is considered as the relation name. In case none of these preferences are set
             the relation between the primary and secondary object is not created. If the primary
             object has a relation property by the specified relation name, then the secondary
             object is associated with the primary object through the relation property.
             

Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param Input: 
                         A list of structures containing details of relationships to be created between primary
                         and secondary objects with the given relation.
             
        :return: The created relations. The partial error 214116 is returned for any requtest relation
             types that are not valid relation type name. The clientId is added to the partial
             error to identify which input element is incorrect.
        """
        ...
    def DeleteRelations(self, Input: list[Teamcenter.Services.Strong.Core._2006_03.DataManagement.Relationship]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes the specified relation between the primary and secondary object for each
             input structure.
             

Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param Input: 
                         A list of structures containing details of relationships to be deleted between primary
                         and secondary objects with the given relation.
             
        :return: list of partial errors.
        """
        ...
    def Revise(self, Input: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.ReviseResponse:
        """    
             Revises a list of next Item Revisions based on input existing Item Revision object
             references and any additional attributes.  Uses deep copy rules to propagate existing
             relations from the Item Revision or to create new references.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Input: 
                         A map of Item Revisions and ReviseProperties structures
             
        :return: is a structure which contains a map of old and new Item Revisions and the ServiceData
             structure.  Any failures will be returned with input Item Revision mapped to error
             message in the ServiceData list of partial errors.
        """
        ...
    @typing.overload
    def SetProperties(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetProperties(self, Info: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.PropInfo], Options: list[str]) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.SetPropertyResponse: ...
    def GenerateUID(self, NUID: int) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.GenerateUIDResponse:
        """    
             This function returns a number of Teamcenter UIDs generated from the Teamcenter server.
             This operation can be used for assigning unique identifiers to objects that will
             not be stored in Teamcenter or for objects which have yet to be created in Teamcenter.
             

             The createObjects and createOrUpdateParts operations will support input of a preallocated
             UID for use during creation. Please see those operation descriptions for further
             details.
             


Use Cases:

             The integration create workflow requires data to be precreated and stored outside
             of Teamcenter and then used during the Teamcenter create process. For example, generating
             a UID for an ItemRevision object and then storing that UID in the CAD integration
             data file. The UID is then used as input to the create SOA operation and that UID
             is assigned to the created object.
             


Dependencies:

             createOrUpdateParts, createObjects
             

Teamcenter Component:

             Core Model CXPOM - Provides a (sparse) set of functions for the interface of C++
             on POM.
             
        :param NUID: 
                         The number of UIDs to be generated.
             
        :return: 
        """
        ...
    def GetDatasetCreationRelatedInfo(self, TypeName: str, ParentObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetDatasetCreationRelatedInfoResponse:
        """    
             This operation pre-populates Dataset creation information, default new Dataset
             name and Tool names, for a specified Dataset type.  This operation
             is used to get all the information associates with the specified Dataset prior
             to the creation operation. The returned default new Dataset name may be determined
             by the parent container object.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param TypeName: 
                         desired <b>Dataset</b> type name
             
        :param ParentObject: 
                         The containe object under which the new <b>Dataset</b> object will be created
             
        :return: .
        """
        ...
    def MoveToNewFolder(self, MoveToNewFolderInfos: list[Teamcenter.Services.Strong.Core._2007_01.DataManagement.MoveToNewFolderInfo]) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.MoveToNewFolderResponse:
        """    
             The moveToNewFolder operation moves a set
             of objects from one folder to another. This operation allows for moving multiple
             sets of objects to and from different folders. If no old folder is specified, this
             operation adds the objects to the new folder.
             


Use Cases:


The user selects an object or group of objects and specifies the
             folder for the objects to be copied into.
             
The user selects an object or group of objects, removes them from
             a specified folder and specifies the folder for the objects to be copied into.
             



Teamcenter Component:

             Core Model Folder - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component covers Folders.
             
        :param MoveToNewFolderInfos: 
                         A list of <font face="courier" height="10">MoveToNewFolderInfo</font> structures
                         each containing an old <b>Folder</b> object a new <b>Folder</b> object, and a vector
                         of objects to be moved from the old folder to the new folder
             
        :return: 
        """
        ...
    def CreateOrUpdateForms(self, Info: list[Teamcenter.Services.Strong.Core._2007_01.DataManagement.FormInfo]) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.CreateOrUpdateFormsResponse:
        """    
             This operation creates Form objects or update existing Form objects
             using the info provided. A new Form will be associated to the container object
             with specified relation type. The properties of the existing Form will be
             updated.
             

Teamcenter Component:

             Core Model Form - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform. This component covers Forms .
             
        :param Info: 
                         Input for creating or updating <b>Form</b> objects
             
        :return: 
        """
        ...
    def GetItemCreationRelatedInfo(self, TypeName: str, ParentObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemCreationRelatedInfoResponse:
        """    
             This operation will return naming rules, property rule, form property descriptor,
             unit of measurement and ItemRevision type name based on Item type selected
             by user during Item creation.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param TypeName: 
<b>Item</b> type name
             
        :param ParentObject: 
<b>parentObject</b> is an unused parameter and may be null
             
        :return: 
        """
        ...
    def GetItemFromId(self, Infos: list[Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemFromIdInfo], NRev: int, Pref: Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemFromIdPref) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemFromIdResponse:
        """    
             This operation returns Items, Item Revisions, and Dataset based on the input item
             id. Input is a list of GetItemFromIdInfo structures each of which contain an item
             id (GetItemFromIdInfo.itemId) and optionally a list of revision ids (GetItemFromIdInfo.revIds)
             which specify which Item Revisions to retrieve.  Also input is and integer value
             (nRev) which can also be used to help specify which Item Revisions to return with
             the Item.  The final input is a GetItemFromIdPref structure which contains a list
             of RelationFilter structures (GetItemFromIdPref.prefs) each of which contain a relation
             type name (RelationFilter.relationTypeName) and a list of object type names (RelationFilter.objectTypeNames).
             This filter can be used to specify which Datasets are returned.  The relation type
             name specifies the relation that relates the Item Revision to the Dataset.  The object
             type name is the type of Dataset to return.  For example, if relationTypeName is
             "IMAN_reference" and the object type name is "Text" then only those Datasets of type
             "Text" that are related to candidate Item Revisions with the "IMAN_reference" relation
             will be returned.  Supplying no value or an empty value for the rev id list and 0
             for nRevs will signify the return of no Item Revisions, and thus no Datasets will
             be returned either.  Supplying no value or an empty value for the rev id list and
             a negative value for nRevs will signify the return of all Item Revisions.   Supplying
             no value or an empty value for the rev id list and a positive value for nRev will
             signify the return of the latest number of Item Revisions specified by the integer--if
             the number of actual revisions found is greater than the input nRev, all revisions
             for the found Item will be returned. Supplying a rev id list will only return those
             revisions, and the nRev value will not be processed. For example, if the input rev
             Id is "A" and the nRev value is 0, only revision "A" will be returned. If the rev
             id list is empty and nRevs = 5, then the 5 latest Item Revisions will be returned.
             If no preference filter is specified, all Datasets will be returned.  The return
             is a GetItemFromIdResponse which contains a list of GetItemFromIdItemOutput (GetItemFromIdResponse.output
             and a ServiceData (GetItemFromIdResponse.serviceData).  Each GetItemFromIdItemOutput
             contains an Item (GetItemFromIdItemOutput.item) and a list of GetItemFromIdItemRevOutput
             structures (GetItemFromIdItemOutput.itemRevOutput).  Each GetItemFromIdItemRevOutput
             structure contains an Item Revision (GetItemFromIdItemRevOutput.itemRevision) and
             a list of found Datasets (GetItemFromIdItemRevOutput.datasets).
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Infos: 
                         list of GetItemFromIdInfo structures
             
        :param NRev: 
                         value for the latest number of Item Revisions to return
             
        :param Pref: 
                         GetItemFromIdPref structure for relation and types filtering
             
        :return: contains found item, its item revisions and the datasets attached to the revision.
             Partial Errors will be returned as a map of input item id to error message.
        """
        ...
    def SaveAsNewItem(self, Info: list[Teamcenter.Services.Strong.Core._2007_01.DataManagement.SaveAsNewItemInfo]) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.SaveAsNewItemResponse:
        """    
             This operation creates a new Item object and ItemRevision object from
             an existing ItemRevision object.  The master form properties may be supplied
             for the new ItemRevision and item master form objects.  If master form data
             is not supplied the master forms will be initialized from the master forms attached
             to the existing ItemRevision.  Deep Copy rules may also be supplied to override
             the default Deep Copy rules.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Info: 
                         The necessary information to create the new <b>Item</b> and <b>ItemRevision</b>

        :return: .
        """
        ...
    def RefreshObjects(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used to reload the in-memory representation of the objects from
             the database. Any references to the object will still be valid. Any in-memory changes
             to the original object will be lost. If the object has been changed in the database
             since it was last loaded, then those changes will not be present in memory. The operation
             updates the in memory representation to reflect database changes and does not obtain
             write lock on any objects.
             

Use Cases:

             Use this operation to reload the in-memory representation of one or more objects
             from the Teamcenter database.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param Objects: 
                         A list of object to be refreshed
             
        :return: 
        """
        ...
    @typing.overload
    def WhereUsed(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], NumLevels: int, WhereUsedPrecise: bool, Rule: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.WhereUsedResponse: ...
    @typing.overload
    def WhereUsed(self, Input: list[Teamcenter.Services.Strong.Core._2012_02.DataManagement.WhereUsedInputData], ConfigParams: Teamcenter.Services.Strong.Core._2012_02.DataManagement.WhereUsedConfigParameters) -> Teamcenter.Services.Strong.Core._2012_02.DataManagement.WhereUsedResponse: ...
    def WhereReferenced(self, Objects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject], NumLevels: int) -> Teamcenter.Services.Strong.Core._2007_01.DataManagement.WhereReferencedResponse:
        """    
             This operation finds the objects and relations that reference a given object.  It
             returns objects where the input object is specified in a Reference property on that
             object.  It also returns relations where the input object is listed as the secondary
             object for that relation.  It does not return relations where the input object is
             the primary object for that relation. The Datamanagement service operation expandGRMRelationsForPrimary
             can be used to return the relations where the input object is the primary object
             and the objects which are the secondary object for the relation.
             

Use Cases:

             User selects an object, specifies the number of levels (or all) of referencers to
             return and executes a where referenced query.
             

             For example, the user selects a Dataset which has a specification relation
             to an Item and is contained in the users Home folder. The Item is contained
             in the user Newstuff folder and in the view folder of another Item Revision.
             If the user selects level 2, the Item and Home folder would be returned at
             level 1 and the Newstuff folder and view folder of the other ItemRevision
             would be returned at level 2.
             

Teamcenter Component:

             Core Model Method Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform. This component defines basic method
             structure.
             
        :param Objects: 

        :param NumLevels: 

        :return: 
        """
        ...
    @typing.overload
    def ExpandGRMRelationsForPrimary(self, PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Core._2007_06.DataManagement.ExpandGRMRelationsPref) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.ExpandGRMRelationsResponse: ...
    @typing.overload
    def ExpandGRMRelationsForPrimary(self, PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Core._2007_09.DataManagement.ExpandGRMRelationsPref2) -> Teamcenter.Services.Strong.Core._2007_09.DataManagement.ExpandGRMRelationsResponse2: ...
    def GetAvailableTypes(self, Classes: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.BaseClassInput]) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.GetAvailableTypesResponse:
        """    
             This will return type names implemented by the given classes. This is lightweight
             way to get all displayable types by name rather than model object.
             
        :param Classes: 
                         A list of given base class name and exclusion list.
             
        :return: A map of given base class name and its available instance types. Failure will be
             returned with error messages in service data.
        """
        ...
    def PurgeSequences(self, Objects: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.PurgeSequencesInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Given a list of ItemRevision sequences, this opertion is used ot perform per
             the following criteria:
             

If the input object is the latest sequence of an ItemRevision,
             all previous sequences will be purged.
             
If the input object is not the latest sequence of the ItemRevision
             and the validateLatestFlag is false, the
             input object will be purged.
             
If the input object is not the latest sequence of the ItemRevision
             and the validateLatestFlag is true, the ServiceData will be updated with an error.
             



Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Objects: 
                         A list of the objects to be purged and a flag noting whether to validate the object
                         is the latest sequence.
             
        :return: 
        """
        ...
    def SetOrRemoveImmunity(self, Objects: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.SetOrRemoveImmunityInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used to add or remove immunity for each object in the input list
             according to the value of the associated setOrRemoveFlag.
             A value of true indicates to apply immunity to the object.  A value of false indicates
             that immunity should be removed from the object.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Objects: 
                         A list of the <b>ItemRevision</b> sequence objects and a flag set true or false.
             
        :return: 
        """
        ...
    def GetDatasetTypeInfo(self, DatasetTypeNames: list[str]) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.DatasetTypeInfoResponse:
        """    
             This operation returns the named reference information for a set of dataset types.
             Named references are Teamcenter objects that relate to a specific data file.
             

             Any failure that occurs during this operation is returned in the ServiceData list of partial errors with the dataset type name
             string mapped to error message.
             


Use Cases:

             User wants to see which file type is allowed for attaching to a dataset.
             

             For this operation, the dataset type name is passed in the datasetTypeNames
             input and the named reference information is returned.  The file extension, fileExtension, is returned in ReferenceInfo and can be used to determine the supported file
             type for the dataset.
             


Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param DatasetTypeNames: 
                         List of dataset type names used to get the named reference information. An empty
                         list will return information for all dataset types defined in Teamcenter.
             
        :return: 
        """
        ...
    def ValidateItemIdsAndRevIds(self, Infos: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.ValidateIdsInfo]) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.ValidateItemIdsAndRevIdsResponse:
        """    
             Validates the item ID and revision ID based on the naming rules and user exit callbacks.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param Infos: 

        :return: - the response object containts a list of ValidateIdsOutput and ServiceData. The
             ValidateIdsOutput contains validation statuses for Item Id and Revision Id. If the
             Ids are modified because of the Naming Rules, then the modified Item Id and Revision
             Id are returned. Any failure is returned in the ServiceData list of partial errors
             with index of ValidateIdsInfo mapped to error message.
        """
        ...
    @typing.overload
    def ExpandGRMRelationsForSecondary(self, SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Core._2007_06.DataManagement.ExpandGRMRelationsPref) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.ExpandGRMRelationsResponse: ...
    @typing.overload
    def ExpandGRMRelationsForSecondary(self, SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: Teamcenter.Services.Strong.Core._2007_09.DataManagement.ExpandGRMRelationsPref2) -> Teamcenter.Services.Strong.Core._2007_09.DataManagement.ExpandGRMRelationsResponse2: ...
    def WhereReferencedByRelationName(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.WhereReferencedByRelationNameInfo], NumLevels: int) -> Teamcenter.Services.Strong.Core._2007_06.DataManagement.WhereReferencedByRelationNameResponse:
        """    
             Finds the objects that reference a given object by a specific relation. The input
             object will be the secondary object for that relation.  It does not return relations
             where the given input object is the primary object for the relation.  The Datamanagement
             service operation expandGRMRelationsForPrimary can be used to return the relations
             where the input object is the primary object and the objects which are the secondary
             object for the relation
             

Use Cases:

             Use case 1: Use this operation to find the objects referencing the input object by
             a specific relation.
             
             Use case 2: Use this operation to find objects of a specific type that reference
             the input object by a specific relation.
             
             Use case 3: Use this operation to find objects of a specific type referencing the
             input object.
             


Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param Inputs: 
                         A list of desired business objects and filters to find the referencing objects for
             
        :param NumLevels: 
                         The number of levels to search.  For example, if A references B, and B references
                         C, a 1-level search from C produces just B, but a 2-level search produces both A
                         and B. If -1, all levels are returned.
             
        :return: 
        """
        ...
    def RemoveNamedReferenceFromDataset(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_09.DataManagement.RemoveNamedReferenceFromDatasetInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes the specified named references from a dataset.
             

             If the NamedReferenceInfo.targetObject input
             is not specified then all named references of the type specified are removed from
             the dataset.  If the NamedReferenceInfo.targetObject
             input is specified then only that named reference is removed from the dataset.  If
             the NamedReferenceInfo.deleteTarget input
             is true then the NamedReferenceInfo.targetObject
             will be deleted if it is no longer referenced.
             


Use Cases:

             User deletes a single named reference from a dataset that has multiple named references
             of the same type.
             

             For this operation, the dataset is passed in along with the named reference type
             and object reference for the specific named reference to be removed from the dataset.
             The specific named reference is removed from the dataset and the dataset is added
             to the ServiceData list of updated objects.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param Inputs: 
                         A list of datasets and the named references to be removed from the datasets.
             
        :return: 
        """
        ...
    def LoadObjects(self, Uids: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Load business objects into the client data model for each of the UIDs supplied. The
             business objects are loaded from the Teamcenter server's in memory cache of business
             objects or from the database. UIDs of runtime business objects (BOMLines)
             that are not currently loaded in the Teamcenter server's memory will result in a
             partial error being returned.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Uids: 
                         An array of UIDs. These UID may come from an outside source or from other service
                         operations such as executeSavedQuery.
             
        :return: 
        """
        ...
    def CreateAlternateIdentifiers(self, Input: list[Teamcenter.Services.Strong.Core._2007_12.DataManagement.AlternateIdentifiersInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Create new alternate identifiers. Given an IdContext,
             an IdentifierType and an Item ( and
             optionally an ItemRevision ), create an Identifier object to display
             an option part number when the IdContext
             is valid.
             

Use Cases:

             User has a part number for an Item that is used to track the Item.
             The manufacturer of the Item has a different part number. The sales department
             has another part number. The user needs to keep all 3 part numbers with the Item
             and display them at different times. The user can get a list of IdContext and IdentifierTypes
             from the getContextsAndIdentifierTypes operation.
             Using the IdContext and IdentifierType, the client can create an Identifer for
             the Item and ItemRevision to be displayed when the IdContext is valid.
             

Dependencies:

             getContextsAndIdentifierTypes, listAlternateIdDisplayRules
             

Teamcenter Component:

             Identifier - Component to define Identifier and associate it with an Item or Item
             Revision. An identifier can be an Alternate identifier for an object as well as an
             Alias identifier for other objects at the same time.
             
        :param Input: 
                         This data describes the alternate identifiers to create.
             
        :return: ( if requested ) will be in the updatedObjects
             section.. Error messages are returned in the ServiceData as partial errors, this
             service does not have any specific errors, just errors from the sub-system.
        """
        ...
    def ListAlternateIdDisplayRules(self, Input: Teamcenter.Services.Strong.Core._2007_12.DataManagement.ListAlternateIdDisplayRulesInfo) -> Teamcenter.Services.Strong.Core._2007_12.DataManagement.ListAlternateIdDisplayRulesResponse:
        """    
             Return the current display rule. If the current user flag is set then also return
             the display rules for the current user. If a list of users is supplied, then return
             the display rules for the list of users; otherwise return the display rules for all
             users.
             

Use Cases:

             Return the current display rule in effect and optionally return all the display rules
             for the current user. Also return the display rules for all users or for a list of
             users only.
             

Teamcenter Component:

             Identifier - Component to define Identifier and associate it with an Item or Item
             Revision. An identifier can be an Alternate identifier for an object as well as an
             Alias identifier for other objects at the same time.
             
        :param Input: 
                         A <font face="courier" height="10">ListAlternateIdDisplayRulesInfo</font> data structure.
             
        :return: partial errors. This service throws no specific errors but the subsystem may.
        """
        ...
    def ValidateAlternateIds(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_12.DataManagement.ValidateAlternateIdInput]) -> Teamcenter.Services.Strong.Core._2007_12.DataManagement.ValidateAlternateIdResponse:
        """    
             Determines if the supplied alternateIds are valid. The USER exit USER_validate_alt_id
             is used for validation. A "modified" alternate id is returned. If the alternate id
             supplied is valid then the modified one returned is the same as the one supplied.
             If the alternate id supplied is not valid, then the one returned is a valid one.
             

Use Cases:

             The user has an alternate id that they wish to use for an object. The alternate id
             is sent to this function to determine if the new alternate id conforms to the rules
             defined by the user.
             

Dependencies:

             getContextsAndIdentifierTypes
             

Teamcenter Component:

             Identifier - Component to define Identifier and associate it with an Item or Item
             Revision. An identifier can be an Alternate identifier for an object as well as an
             Alias identifier for other objects at the same time.
             
        :param Inputs: 
                         A list of <font face="courier" height="10">ValidateAlternateIdInput</font> data structures.
             
        :return: partial errors.
        """
        ...
    def GetContextsAndIdentifierTypes(self, TypeTags: list[Teamcenter.Soa.Client.Model.Strong.ImanType]) -> Teamcenter.Services.Strong.Core._2007_12.DataManagement.GetContextAndIdentifiersResponse:
        """    
             Returns the context and identifier types for the supplied identifiable types.
             

Use Cases:

             A user has defined several IdContexts and Idenitfiers in preparation
             for creating AlternateIds. This service returns the current IdContext
             and Identifiers allowing the user to select the appropriate data for AlternateId
             creation.
             

Teamcenter Component:

             Identifier - Component to define Identifier and associate it with an Item or Item
             Revision. An identifier can be an Alternate identifier for an object as well as an
             Alias identifier for other objects at the same time.
             
        :param TypeTags: 
                         A list of <b>ImanType</b> objects.
             
        :return: is invalid. Other error messages are for problems in the subsystem.
        """
        ...
    def UnloadObjects(self, ObjsToUnload: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation unloads Business Objects. If input contains one or more Business Objects
             then it will call AOM_unload for each object otherwise it will call unloadAll  to
             unload all the objects.
             

             Note that unloadAll will unload both C++ along with POM objects.
             

        :param ObjsToUnload: 
                         A list of model objects to unload.
             
        :return: It will return partial error if any.
        """
        ...
    def FindDisplayableSubBusinessObjects(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.BOWithExclusionIn]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.DisplayableSubBOsResponse:
        """    
             Operation to retrieve sub Business Object Names for a Business Object that are displayable
             to the login user in the object creation dialog. e.g File-new, select Item, what
             types to be displayed for Item
             
        :param Input: 
                         - a list of input objects representing the BO type names for which the displayable
                         types are to be retrieved
             
        :return: contains a list of BO type names to be displayed for input
        """
        ...
    def CreateDatasets2(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.DatasetProperties2]) -> Teamcenter.Services.Strong.Core._2006_03.DataManagement.CreateDatasetsResponse:
        """    
             This operation creates a list of Dataset objects and creates the specified
             relation type between created Dataset and input container object.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param Input: 
                         The information needed to create  <b>Dataset</b>

        :return: 
        """
        ...
    def GetItemAndRelatedObjects(self, Infos: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetItemAndRelatedObjectsInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetItemAndRelatedObjectsResponse:
        """    
             This operation returns Items, ItemRevisions, Dataset and NamedReference
             information based on the input. Input is a list of GetItemAndRelatedObjectsInfo
             structures each of which contains item uid or id, revison information and optionally
             a list of filters to determine the datasets to be returned. For the Datasets
             the client can request information about the NamedReferences. NamedReferences
             are how Data files are attached to Datasets. The Data file is what
             a CAD client is really interested in. The return is a GetItemAndRelatedObjectsResponse
             which contains a list of GetItemAndRelatedObjectsItemOutput
             and a ServiceData.
             

Use Cases:

             The client has an item of ItemRevision and needs to know what CAD data is
             attached to the ItemRevision. The client fills in either the Item or
             ItemRevision information along with the information about the types of Dataset
             and NamedReferences the client is interested in. For the NamedReferences
             the user can get the tickets which will allow the client retrieve the files attached
             to the Datasets. The results of the query will give the client all the information
             about the Datasets and NamedReferences and optional tickets.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Infos: 
                         list of <font face="courier" height="10">GetItemAndRelatedObjectsInfo</font> structures.
             
        :return: Contains found items, revisions and the datasets attached to the revision. Partial
             Errors will be returned as a map of input client id to error message.
        """
        ...
    def Revise2(self, Info: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.ReviseInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.ReviseResponse2:
        """    
             This operation provides the ability to revise the ItemRevision objects given
             in the input list and carries forward relations to existing objects. When applying
             deep copy rules, if user overridden deep copy information is provided in the input,
             relations are propagated to the new ItemRevision based on that input. If no
             deep copy information is provided in the input, the deep copy rules in the database
             are used to propagate relations to the new ItemRevision.  If the input contains
             property values for the master form, those values are set on the new ItemRevision
             master form.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Info: 
                         The necessary information to create the new revision
             
        :return: 
        """
        ...
    def SaveAsNewItem2(self, Info: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.SaveAsNewItemInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.SaveAsNewItemResponse2:
        """    
             This operation provides the capability to create one or more new Item objects
             based on a list of existing ItemRevision objects. It optionally carries forward
             ItemRevision relations based on the deepCopyRequired
             flag. When applying deep copy rules, if user overridden deep copy information is
             provided in the input, then old ItemRevision relations are propagated to the
             new ItemRevision based on the input. If no deep copy rule information is provided
             in the input, the deep rules in the database will be applied. If user provides new
             property values for the Item and ItemRevision master forms in the input,
             then these will be copied to the master forms of the newly created Item and
             ItemRevision.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Info: 
                         The necessary information to create the new <b>Iitem</b> and <b>ItemRevision</b>

        :return: 
        """
        ...
    def GetNextIds(self, VInfoForNextId: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.InfoForNextId]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetNextIdsResponse: ...
    def GetNRPatternsWithCounters(self, VAttachInfo: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.NRAttachInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetNRPatternsWithCountersResponse:
        """    
             This operation gives the list of Patterns which has counters along with preferred
             patterns and conditions for the Naming Rule attached to the property of an object
             Type. The Type name and the Property name are passed in the input structure. The
             input for this operation contains a list of this structure. The return structure
             contains the vector of patterns with counters, preferredPattern and condition, along
             with the service data member.
             

Use Cases:

             This operation is used in create, revise or save-as dialogs to receive list of applicable
             patterns for item and revision ids. The list of patterns returned is displayed in
             these dialogs for user selection. After user selects a pattern and clicks "Assign"
             button, an id is generated matching the pattern selected and populated in the corresponding
             field's box.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param VAttachInfo: 
                         Struct that contains Type Name and Property Name
             
        :return: (This list may be incomplete, and is subject to change without notice.)
        """
        ...
    def GetRevNRAttachDetails(self, TypeAndItemRevInfos: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.TypeAndItemRevInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.GetRevNRAttachResponse:
        """    
             This operation gets all the possible initial, secondary and supplemental revision
             next Ids for an ItemRevision along with the available formats and the set
             of excluded letters for revision. The Revision Type Name and the current revision
             are passed in the input typeAndItemRevInfos structure. The input for this operation
             contains a list of this structure. The return structure contains list of Initial
             Revision details, Secondary Revision details, Supplemental Revision details and exclude
             Skip letters along with the service data member.
             

Use Cases:

             This operation is used to get the next available options for revision id for a new
             or existing object. User can select one of the values returned by this operation
             and use as revision id input value for create, revise or save-as operation.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param TypeAndItemRevInfos: 
                         List of <font face="courier" height="10">TypeAndItemRevInfo</font> structs which
                         contains <b>Item</b> and <b>ItemRevision</b> type name and the revision object.
             
        :return: (This list may be incomplete, and is subject to change without notice.)
        """
        ...
    def CreateOrUpdateRelations(self, Infos: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateOrUpdateRelationsInfo], Sync: bool) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateOrUpdateRelationsResponse:
        """    
             Creates the specified relation between the input objects (primary and secondary objects)
             for each input structure. If the sync flag
             is specified, then if any Generic Relationship Management (GRM) relations exist between
             the primary and secondary objects and they are not specified in the input they will
             be deleted. If sync flag is provided, the
             relations member of CreateOrUpdateRelationsInfo
             is ignored.
             

Use Cases:

             Use Case 1: Create a relation based on the GRM rule definition.
             

             One can create a relation specified by name of the relation in the input structure
             between the primary and secondary object, when there exists a GRM rule between the
             primary and secondary object with the given relation type.
             

             Use Case 2: Update a relation based on the GRM rule definition.
             

             One can update a relation specified by name of the relation in the input structure
             between the primary and secondary object, when there exists a GRM rule between the
             primary and secondary object with the given relation type.
             

             Use Case 3: Remove a relation based on the GRM rule definition.
             

             One can remove a relation by setting the sync to true and do not provide any relation
             between the primary and secondary object in the input structure. When there exists
             a GRM rule between the primary and secondary object with the given relation type,
             and the sync flag is set to true, then if any GRM relations exist between the primary
             and secondary objects and they are not specified in the input they will be deleted.
             


Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param Infos: 
                         A list of <font face="courier" height="10">CreateOrUpdateRelationsInfo</font> structures
                         containing details of relationships to be created between primary and secondary objects
                         with the given relation.
             
        :param Sync: 
                         If true then GRM relations in db and the number of secondary objects specified in
                         the <font face="courier" height="10">input</font> will be synchronized. Note that
                         in this case the <font face="courier" height="10">secondaryData</font> member of
                         the <font face="courier" height="10">input</font> structure is used and not the <font face="courier" height="10">relations</font> member.
             
        :return: list of partial errors.
        """
        ...
    def CreateConnections(self, Properties: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.ConnectionProperties], Container: Teamcenter.Soa.Client.Model.ModelObject, RelationType: str) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateConnectionsResponse:
        """    
             Creates a list of Connection objects and any associated data (ConnectionRevision,
             ConnectionMaster Form and ConnectionRevision Master Form) based on
             the input properties structure. It also creates the specified relation type between
             newly created Connection object and input container object. If container and
             relation type are not supplied, none of the Connection objects will be related
             to a container. If any destination to paste the newly created objects is desired
             then it must be supplied as input.
             

Use Cases:

             This operation supports creation of single or multiple Connection objects.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Properties: 
                         A <b>Connection</b> object is created for each ConnectionProperties in the list.
                         The data on the ConnectionProperties is used to create initial values on the <b>Connection</b>
                         and related objects
             
        :param Container: 
                         Object to which all the <b>Connection</b> objects created will be related to via
                         the input relationType (Folder instance and contents relationType). If not specified
                         the <b>Connection</b> will be created, but without a relation to a container object.
             
        :param RelationType: 
                         The name of the relation used to attach the created <b>Connection</b> objects to
                         input container. This argument is used only when the container argument is present,
                         optional.
             
        :return: object will still be created, but will not be placed in any container.
        """
        ...
    def CreateOrUpdateGDELinks(self, GdeLinkInfos: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.GDELinkInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateOrUpdateGDELinksResponse:
        """    
             Create and/or update GeneralDesignElementLink(GDELink) objects based
             on the input properties structure. If the given GDELink object exists in Teamcenter
             then the operation will be treated as an update based on the input properties structure
             

Use Cases:

             This operation supports creation or updation of GDELink objects
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param GdeLinkInfos: 
                         An input of vector of structures containing values necessary to create or update
                         the Teamcenter Model Data representing the <i>GDELink</i>. If a reference to an existing
                         <i>GDELink</i> is supplied then an update is assumed, otherwise a new <i>GDELink</i>
                         is created. On update the <i>GDELink</i> name and description may be changed but
                         not the type. After the <i>GDELink</i> is created, and if for an update the property
                         values are supplied, the <i>GDELink</i> created will be updated with the properties.
             
        :return: with the error message mapped
             to input client id
        """
        ...
    def CreateOrUpdateItemElements(self, Properties: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.ItemElementProperties]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateOrUpdateItemElementsResponse:
        """    
             Allows the user to create a new GeneralDesignElement (GDE) or its subtype
             and set its properties. In the case of existing GDE, user can update the properties.
             

Use Cases:

             This operation can be used when user wants to create a GDE in a product structure
             or wants to update the properties of an existing GDE. User has to pass unique
             client Id, name and type when a new element has to be created. Whenever properties
             of an existing GDE have to be updated the itemElement business object
             and itemElemAttributes should be passed
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Properties: 
                         This is a vector of <i>ItemElementProperties</i>. While creating a new element it
                         shall contain a unique clientId, name and type. In the case of an existing <i>GDE</i>,
                         this structure must contain <i>itemElemAttributes</i> to be modified and the <i>itemElement</i>
                         whose properties have to be modified.
             
        :return: 
        """
        ...
    @typing.overload
    def CreateObjects(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateIn]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    @typing.overload
    def CreateObjects(self, CreateInputs: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateIn], RunInBackground: bool) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    def AddParticipants(self, AddParticipantInfo: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.AddParticipantInfo]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.AddParticipantOutput:
        """    
             This operation creates the Participant objects and adds them to the input
             Item Revision. If a Participant object with specified attributes already exists,
             it is added to the Item Revision.
             

Use Cases:

             For Change Management use cases, user may need to add different participants to the
             change objects like analyst, change specialist etc. The creator of the change object
             will assign the analyst for the change where this operation can be used.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param AddParticipantInfo: 
                         Contains a list of <font face="courier" height="10">ParticipantInfo</font> structures
                         with information about participants to be added and an Item Revision to add the participants
                         to.
             
        :return: If the service fails to create the participant, it returns "SOACORE_failed_to_create_participant"
             error code.
        """
        ...
    def RemoveParticipants(self, Participants: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.Participants]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation allows the user to remove Participant objects associated with
             specified Item Revision. If a participant being removed is no longer associated with
             any other objects, it gets deleted.
             

Use Cases:

             This operation can be used to remove the assigned Participant objects like
             Analyst, Proposed Reviewers etc. from the change objects. Change creator can use
             addParticipants service operation to assign
             an analyst or use this operation to remove an assigned analyst.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Participants: 
                         List of participants structures each containing a list of <b>Participant</b> objects
                         to be removed and an Item Revision to remove the <b>Participant</b> objects from.
             
        :return: 
        """
        ...
    def SetTableProperties(self, TableData: list[Teamcenter.Services.Strong.Core._2009_10.DataManagement.TableInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation allows client applications to set the properties pertaining to one
             or more Table business objects. Client developers will need to set information
             pertaining to the number of rows, columns, descriptions of each row and column, and
             cell information for each cell of the Table. The cell information must contain
             the type of cell, value to be placed in the cell, and optionally, a description of
             those values. The current operation only works on cells of specific types and it
             is mandatory that the type of the cells being set on the input structure corresponds
             to one of the cell types defined in the database schema viewable through the BMIDE.
             Supported valid types are:
             

TableCellInt

TableCellString

TableCellDouble

TableCellLogical

TableCellHex

TableCellSED

TableCellBCD

TableCellDate




Use Cases:

             This operation can be used by a client developer, when he/she deals with setting
             Table Business Object specific properties. Typically, Table Business
             Objects are not themselves visible in the Teamcenter workspace and appear as properties
             of other owning objects that are visible in the workspace. Modification to the owning
             objects, may involve changes to one or more of the Table properties that they reference
             through the Table.  In such cases, the setTableProperties is to be called,
             passing in the input structure which is setup to specify the modified values.
             
             One such example of existing usage of this operation, is the existing Teamcenter
             Rich Client functionality for modification of an Integer type of Parameter Definition
             [ ParmDefIntRevision Business Object ]. This Business Object and the functionality
             for its modification are provided by the add on Calibration and Configuration Data
             Management module.  During modification, of the integer parameter definition object,
             client code renders table like UI for each table property of the Parameter Definition,
             gathers the input values from the UI and populates a vector of the input structure
             of type TableInfo, sets the type of thecells to TableCellInt and makes
             the operation call. Client code will then parse the Service Data returned from the
             operation to obtain a handle to the updated Table Business Object. Errors,
             if any were encountered during the operation execution, are handled via the Service
             Data.
             


Teamcenter Component:

             CCDM - Calibration and Configuration Data Management
             
        :param TableData: 
                         This vector contains a list of <i>TableInfo</i>, and each <i>TableInfo</i> contains
                         information pertaining to the specific <b>Table</b> it references. The data present
                         in the <i>TableInfo</i> structures are used to modify specific cell values and/or
                         descriptions of the rows, columns or values.
             
        :return: This operation returns a Service Data structure. The updated Table business objects
             are included in the updated service data member list, which contains any modifications
             to row and column descriptions and the size of the table. Any errors encountered
             at the time of modification are included as part of the Service Data errors.
        """
        ...
    def GetItemFromAttribute(self, Infos: list[Teamcenter.Services.Strong.Core._2009_10.DataManagement.GetItemFromAttributeInfo], NRev: int, Pref: Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemFromIdPref) -> Teamcenter.Services.Strong.Core._2009_10.DataManagement.GetItemFromAttributeResponse:
        """    
             This service retrieves Item and its related ItemRevision objects based
             on the supplied attribute key-value pairs supplied in the infos
             list. All the key-value pairs except for the rev_id
             key are used to create a query for Item objects.
             

             Once a set of Item objects have been retrieved, their ItemRevision
             objects are retrieved based on the following rules:
             

If  nRev is a negative value
             then all the ItemRevision objects are returned
             
If nRev is a positive value
             then the nRev most recent ItemRevision
             objects are returned. If nRev is greater
             than the number of revisions then all of them are returned.
             
If nRev is zero and a rev_id attribute key was supplied in the attribute
             key-value pairs, then that ItemRevision object is returned.
             
If nRev is zero and rev ids
             values were supplied in the GetItemFromAttributeInfo
             object then all of the specified rev ids will be returned.
             



Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Infos: 
                         The list of attribute value keys for the retrieval. The attributes must be the unique
                         key attributes of the class. Currently, only item_id attribute should be used
             
        :param NRev: 
<ul>
<li type="disc">nRev &lt; 0        retrieve all available ItemRevision objects
                         </li>
<li type="disc">nRev = 0        retrieve no ItemRevision objects
                         </li>
<li type="disc">nRev &gt; 0        retrieve the most recent nRev number of ItemRevision
                         objects
                         </li>
</ul>

        :param Pref: 
<font face="courier" height="10">GetItemFromIdPref</font> object used to filter the
                         returned <b>ItemRevision</b> objects. If a <b>Dataset</b> is found related to the
                         <b>ItemRevision</b> with this relation type name and is one of the types specified
                         in the list of object type names, return the <b>ItemRevision</b> object
             
        :return: 
        """
        ...
    def GetTableProperties(self, Table: list[Teamcenter.Soa.Client.Model.Strong.Table]) -> Teamcenter.Services.Strong.Core._2009_10.DataManagement.GetTablePropertiesResponse:
        """    
             This operation allows client applications to obtain the properties pertaining to
             one or more Table Business Objects. Client developers will need to pass in
             references to each Table that they need to query information on.  Note that
             the input vector needs to contain only references to the Teamcenter Table business
             object, this operation cannot be used to fetch properties of any other Business Objects.
             

Use Cases:

             This operation can be used by a client developer, when he/she deals with obtaining
             specific Table Business Object specific properties. Typically, Table
             Business Objects are not themselves visible in the Teamcenter workspace and appear
             as properties of other owning objects that are visible in the workspace.  The typical
             scenario in such cases is that a user attempts to obtain/view all properties of the
             the owning object, which may have one or more reference properties pointing to a
             Table.  A custom UI would need to display the Table related properties on the parent
             object in such cases and rendering these properties would require the client applications
             to obtain such information using the getTableProperties operation.
             
             One such example of existing usage of this operation, is the existing Teamcenter
             Rich Client functionality for viewing properties an Integer type of Parameter
             Definition [ ParmDefIntRevision Business Object ]. This Business Object
             and the functionality for viewing its properties are provided by the add on Calibration
             and Configuration Data Management module, through custom stylesheets which render
             a Table like UI for each referenced Table property.  At the time of rendering the
             UI, the client operations call the getTableProperties operation to obtain
             properties such as the number of rows, number of columns, labels for each row and
             column, the type of the cells and cell values and descriptions for each cell in the
             table.
             


Dependencies:

             getProperties
             

Teamcenter Component:

             CCDM - Calibration and Configuration Data Management
             
        :param Table: 
                         This is a vector of the Table Business Objects for which the properties need to be
                         obtained.
             
        :return: Returns GetTablePropertiesResponse
        """
        ...
    def FindDisplayableSubBusinessObjectsWithDisplayNames(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.BOWithExclusionIn]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.DisplayableSubBusinessObjectsResponse:
        """    
             This operation returns sub Business Object names that are displayable to the
             login user in the object creation dialog and their display names for each Primary
             Business Object given as the input.  Returned Business Object lists have exclusions
             of Business Objects and their secondary Business Objects as specified in the input.
             This returns the hierarchy of displayable objects for each Business Object it returns.
             
        :param Input: 
                         A list of Business Object names and their exclusion list for which the displayable
                         Business Objects are to be retrieved.
             
        :return: Contains a list of BO type names to be displayed for input
        """
        ...
    def GetAvailableTypesWithDisplayNames(self, Classes: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.BaseClassInput]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.GetAvailableBusinessObjectTypesResponse:
        """    
             This operation returns Business Object names and their display names for each
             primary Business Object given as the input.  Returned Business Object lists have
             exclusions of Business Objects and their secondary Business Objects as specified
             in the input. If any of the returned Business Objects is also a primary Business
             Object then this operation may not return its secondary Business Objects by default.
             In order to return its secondary Business Objects also, it is required to add this
             Business Object name to following preference TYPE_DISPLAY_RULES_list_types_of_subclasses.
             
             Please see the Preferences and Environment Variables Reference documentation for
             preference TYPE_DISPLAY_RULES_list_types_of_subclasses for more information.
             
             This is a lightweight way of getting all displayable Business Objects by name rather
             than model object.
             

        :param Classes: 
                         A list of primary Business Object names and their exclusion list.
             
        :return: A map of given base class name and its available instance types. Failure will be
             returned with error messages in service data.
        """
        ...
    def GetDatasetCreationRelatedInfo2(self, TypeName: str, ParentObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.GetDatasetCreationRelatedInfoResponse2:
        """    
             This operation pre-populates Dataset creation information, default new Dataset
             name and Tool names, for a specified Dataset type.  This operation
             is used to get all the information associates with the specified Dataset prior
             to the creation operation. The returned default new Dataset name may be determined
             by the parent container object.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param TypeName: 
                         The desired <b>Dataset</b> type name
             
        :param ParentObject: 
                         The container object under which the new <b>Dataset</b> object will be created
             
        :return: .
        """
        ...
    def GetLocalizedProperties(self, Info: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.PropertyInfo]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizedPropertyValuesList:
        """    
             Typically business object property values are returned in the locale of the current
             session, this operation returns desired property values in any of the supported locales
             of the Teamcenter server.  String type properties may be localized with values for
             each supported locale, this operation will return the translated values for one or
             more desired locales.
             

Use Cases:

Retrieve the localized values for localizable property
             

When running Teamcenter in language environment other than the English, user
             wants to see the localized property value to be displayed in corresponding language
             in the UI.   This operation can be used to fulfill this requirement. By providing
             the desired business object, internal name of the properties, and specific locale
             name(s), this operation will return the localized property value(s) in that particular
             locale(s).
             

Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param Info: 
                         A list of desired business objects, property names, and locales to retrieve those
                         properties in.
             
        :return: Â Â Â Â 38044: The property value is not set.
        """
        ...
    def IsPropertyLocalizable(self, InputInfo: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizableStatusInput]) -> Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizableStatusResponse:
        """    
             The operation is used to determine if string-type property is localizable or not
             and can retrieve the localizable status for ONE or MORE properties.
             

Use Cases:

Determine whether a string property is marked as localizable property
             

User needs to use this service operation to determine a string property is localizable
             first before he can add the translations to the value of this property.
             


Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param InputInfo: 
                         A list of business object type names and internal property names
             
        :return: 
        """
        ...
    def SetLocalizedProperties(self, Info: Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizedPropertyValuesInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation allows user to set or modify the display values for a localized property
             on a single object. This sets the property values for a single property on an object
             in different locales. With the display values capability, each localized string property
             could have different language translations associated with that.
             

             Please be aware of the following:
             

This operation is only used to set the secondary (not the master)
             values of the localized property. User can still package the master value (with localization
             status marked as "M") in the LocalizedPropertyValuesInfo
             structure, however, the operation will ignore and skip the master value during the
             process.
             
This operation is only used to set the localization values for one
             property. If you want to set the localized values for multiple properties, please
             use operation setLocalizedPropertyValues().
             



Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param Info: 
                         The business object and a list of the property name, value and locale of the property
                         value.
             
        :return: 
        """
        ...
    def SetLocalizedPropertyValues(self, Info: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.LocalizedPropertyValuesInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Sets the property values for multiple properties on a single object in different
             locales. With the display values capability, each localized string property could
             have different language translations associated with that. This operation allows
             user to set or modify the display values for the localized properties on a single
             object.
             

             It should be noted that this operation is only used to set the secondary (not the
             master) values of the localized properties. User can still package the master value
             (with localization status marked as "M") in the LocalizedPropertyValuesInfo
             structure, however, the operation will ignore and skip these master values during
             the process.
             


Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param Info: 
                         A list of business object, the property name, value and locale of the property value.
             
        :return: 
        """
        ...
    def VerifyExtension(self, ExtensionInfo: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.VerifyExtensionInfo]) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.VerifyExtensionResponse:
        """    This operation checks if an extension exists on an operation of a specific type.
        :param ExtensionInfo: 
                         The specific type, operation and extension information required to verify an extension
                         exists.
             
        :return: If extension exists.
        """
        ...
    def CreateOrUpdateStaticTableData(self, StaticTableInfo: Teamcenter.Services.Strong.Core._2010_09.DataManagement.StaticTableInfo, RowProperties: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.RowData]) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.CreateOrUpdateStaticTableDataResponse:
        """    
             This creates a new Table along with Rows or updates an existing Table with rows and
             their values based on input StaticTableInfo and created Table rows are added to the
             Table. ServiceData is updated with newly created/updated Table.
             

Use Cases:

             This operation is used to create/update the data for TableProperties objects of Fnd0StaticTable
             object. When user selects Cdm0DataReqItemRevision object, the attribute cdm0EventsList
             is displayed in the summary as well as on View/Edit Properties menu in RAC. The attribute
             cdm0EventsList is type referenced to Fnd0StaticTable.
             
             User can add the data in columns for each row of the table or adds rows to the table
             or deletes rows. After creation/updation of the table, user saves the object which
             invokes this SOA operation.
             

Dependencies:

             getStaticTableData
             

Teamcenter Component:

             Contract Data Management - Provides functionality to save or retrieve Event List
             data for Data Requirement Item Revision
             
        :param StaticTableInfo: 
                         This represents static table object that needs to be created/updated.
             
        :param RowProperties: 
                         Vector of RowData where each element is of type TableProperties
             
        :return: (This list may be incomplete, and is subject to change without notice.)
        """
        ...
    def GetEventTypes(self, Input: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.EventObject]) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.EventTypesResponse:
        """    
             The getEventTypes operation retrieves the valid Auditable and Subscribable
             events for each of the businessObject in the input EventObject
             vector. When an event is auditable, you can audit actions on Teamcenter objects when
             that event happens on the businessObject. When an event is Subscribable, that means
             subscriptions can be created for that event. Partial failures, if any, will be returned
             in the serviceData.
             

Teamcenter Component:

             Subscription Management - Application in Teamcenter that allows users to subscribe
             to a certain events on business objects.
             
        :param Input: 
                         A vector of <font face="courier" height="10">EventObject</font> structure consisting
                         of list of Business Objects, for which the valid auditable and subscribable events
                         are to be fetched.
             
        :return: Output is a vector of eventsOutput structures packaged in a custom response. Partial
             failures will be returned in the ServiceData as a map of client id to error message.
        """
        ...
    def PostEvent(self, Input: list[Teamcenter.Services.Strong.Core._2010_09.DataManagement.PostEventObjectProperties], EventTypeName: str) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.PostEventResponse:
        """    
             This operation will post an event for each of the Teamcenter business objects in
             the input list, with all the supplied information: secondaryObject,
             properties to be logged, and the error details. . Partial failures will be returned
             in the serviceData.
             

Use Cases:

             Most events are posted by Teamcenter server logic. Use this operation to make an
             event known only to your client code recorded in Audit Manager or supported by Subscription
             Manager.
             
Use Case1: Auditing events
             
             This operation helps auditing Teamcenter objects history by logging audit records
             when event eventTypeName occurs on primaryObject.
             

When site preference TC_audit_manager is set to ON and no Audit Definition
             exists for object type primaryObject and the eventTypeName, no audit records will
             be logged. Audit Definitions are Audit Manager Application configurations and can
             be viewed in Audit Manager Application.
             
When site preference TC_audit_manager is set to ON and Audit Definition
             exists for object type primaryObject and the eventTypeName, audit records will be
             logged with all the information provided in the structure PostEventObjectProperties
             
No audit records are written when preference TC_audit_manager is
             set to OFF or if the event posted is not defined as Auditable.
             




             Use Case2: Subscription Notifications    
             
             the site preference TC_subscription is set to ON , users can create subscriptions
             for notifications for certain events on Teamcenter Objects  The event posted must
             be described as subscribable and there should also exist an associated subscription
             object for the notification to occur.
             

Teamcenter Component:

             Subscription Management - Application in Teamcenter that allows users to subscribe
             to a certain events on business objects.
             
        :param Input: 
                         A vector of <font face="courier" height="10">ObjectProperties</font> structure. Each
                         structure consists of Primary Business Object, a manadatory parameter, on which event
                         has occurred, any secondary object to post its information, along with any additional
                         properties and the values and error code while performing the event.
             
        :param EventTypeName: 
                         Name of the event. This is a mandatory parameter and should be a valid auditable
                         or subscribable event mapped for the primary object. List of valid event types could
                         be found using command line utility: install_event_types
             
        :return: )
             if any. Success is defined by the return of ifailError for post event on each Business
             Object, primaryObject. If error is encountered while processing post event on elements
             in the set, it is reported as partial errors and processing continues for the remaining
             elements in the input set. Partial failures will be returned in the  serviceData.
        """
        ...
    def GetStaticTableData(self, StaticTable: Teamcenter.Soa.Client.Model.Strong.Fnd0StaticTable) -> Teamcenter.Services.Strong.Core._2010_09.DataManagement.StaticTableDataResponse:
        """    
             Returns a list of objects of type TableProperties which are associated with Fnd0StaticTable
             object. Fnd0StaticTable object has an attribute fnd0StaticTableData which
             is an array of TableProperties objects.  Any failures will be returned with
             the input object mapped to the error message in the ServiceData list of partial errors.
             

Use Cases:

             This operation is used to get the data for attribute fnd0StaticTableData of Fnd0StaticTable
             object. Attribute fhd0StaticTableData is an array of TableProperties objects. When
             user selects Cdm0DataReqItemRevision object, the attribute cdm0EventsList
             is displayed in the summary as well as on View/Edit Properties menu in RAC. The attribute
             cdm0EventsList is Typed Reference to Fnd0StaticTable object.
             

Dependencies:

             createOrUpdateStaticTableData
             

Teamcenter Component:

             Contract Data Management - Provides functionality to save or retrieve Event List
             data for Data Requirement Item Revision
             
        :param StaticTable: 
                         StaticTable
             
        :return: 
        """
        ...
    def ValidateRevIds(self, Inputs: list[Teamcenter.Services.Strong.Core._2011_06.DataManagement.ValidateRevIdsInfo]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.ValidateRevIdsResponse:
        """    
             Validates and/or modifies the Revision Id based on the naming rules/revision naming
             rules and user exit callbacks.
             

Use Cases:

             This operation is generally used to validate revision id before providing it as input
             for create, revise and save-as operations.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param Inputs: 
                         A list of <font face="courier" height="10">ValidateRevIdsInfo</font> structures,
                         each of which contain revId/itemObject/itemType that have to be validated.
             
        :return: (This list may be incomplete, and is subject to change without notice.)
        """
        ...
    def SaveAsObjects(self, SaveAsIn: list[Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsIn]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsObjectsResponse:
        """    
             This operation is generic operation for saving of Business Objects. It will also
             save any secondary objects that also need to be saved based on deep copy rule information
             

Use Cases:

             Client constructs the SaveAs dialog for a Business Object using OperationDescriptor.getSaveAsDesc operation.  The information
             returned by that operation allows client to construct the SaveAs dialogs and DeepCopy
             panels for user input. Once the user input is received, client can make subsequent
             invocation to this (DataManagement.saveAsObjects)
             operation to execute SaveAs on the object.
             

Dependencies:

             getSaveAsDesc
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param SaveAsIn: 
                         Input data containing target object and DeepCopyData of the attached objects
             
        :return: . The Partial Error includes
             the index of the failed element from the input vector.
        """
        ...
    @typing.overload
    def GetTraceReport(self, Input: Teamcenter.Services.Strong.Core._2011_06.DataManagement.TraceabilityInfoInput) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.TraceabilityReportOutput: ...
    @typing.overload
    def GetTraceReport(self, Input: list[Teamcenter.Services.Strong.Core._2012_10.DataManagement.TraceabilityInfoInput1]) -> Teamcenter.Services.Strong.Core._2012_10.DataManagement.TraceabilityReportOutput1: ...
    def ValidateIdValue(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateIn]) -> Teamcenter.Services.Strong.Core._2012_02.DataManagement.ValidationResponse:
        """    
             This operation determines if the given MultiFieldKey
             properties are unique based on the MultiFieldKey
             definition.
             

Use Cases:

             Use this operation before creating a new object to validate if the MultiFieldKey property combination is already used.  This is an
             existence check rather than a true validation. It does not validate the property
             values against Naming Rules.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Input: 
                         A list of MultiFieldKey attribute/value pairs for the object to be created
             
        :return: attribute/value pairs
             for the object to be created.
        """
        ...
    def BulkCreateObjects(self, Input: list[Teamcenter.Services.Strong.Core._2012_02.DataManagement.BulkCreIn]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse:
        """    
             This is a generic operation for bulk creation of Business Objects. This will create
             instances of the given quantity of the specified type in their specified containing
             folders. This will also create any secondary(compounded) objects that need to be
             created, assuming the CreateInput for the secondary object is represented in the
             recursive CreateInput object e.g. Item is Primary Object that also creates
             Item Master, ItemRevision and ItemRevision in turn creates ItemRevision
Master. The input for all these levels is passed in through the recursive
             CreateInput object. This operation is applicable for bulk creation of Item,
             Form ,Dataset and Asp0Aspect Types only.
             

Use Cases:

             1. To create large number of objects of specified types namely Item, Dataset
             and Form each of specified quantities and save them through a single transaction
             to significantly reduce the number of sql queries incurred during object creation,
             thus improving object creation performance and making object creation scalable.
             
             2. To create large number of Asp0Aspect objects of specified types and save
             them through a single transaction to significantly reduce the number of sql queries
             incurred during object creation, thus improving object creation performance and making
             object creation scalable.
             

Dependencies:

             createFolders
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param Input: 
                         A vector of <font face="courier" height="10">BulkCreIn</font> structures representing
                         the <font face="courier" height="10">CreateInput</font> for the bulk creation of
                         business objects of the specified quantity for each type.
             
        :return: business objects respectively.
        """
        ...
    def SaveAsObjectAndRelate(self, SaveAsInput: list[Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsIn], RelateInfo: list[Teamcenter.Services.Strong.Core._2012_09.DataManagement.RelateInfoIn]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsObjectsResponse:
        """    
             This operation saves the given object and its related objects as new instances. Related
             objects are identifed using deep copy rules. Optionally,this method relates the new
             object to the input target object or to a default folder.
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param SaveAsInput: 
                         The property values to be used for the new objects. The properties passed in should
                         be defined in SaveAs descriptor.
             
        :param RelateInfo: 
                         The paste options used to relate the newly created object.
             
        :return: A list of objects that are created through saveas operation, including children objects.
             CreatedList contains objects that are created by SaveAs operation.. It contains GRM
             relations created due to paste operation. UpdatedList contains target objects to
             which the newly created objects are related. Failure for any element in the input
             list is returned as a Partial Error in the ServiceData . The Partial Error includes
             the index of the failed element from the input list. 214424: SaveAs action succeeded.
             But server could not identify a suitable target object to relate the newly created
             object.. 214425:  When item revision is saved as new instance,server relates item
             to target folder. Presence of this error code indicates that server could not paste
             item and instead has pasted the created item revision. 214426: SaveAs operation on
             that specifc object has failed.
        """
        ...
    def GetDatasetTypesWithFileExtension(self, FileExtensions: list[str]) -> Teamcenter.Services.Strong.Core._2012_10.DataManagement.GetDatasetTypesWithFileExtensionResponse:
        """    
             This operation returns the dataset type and reference information for a set of file
             extensions. Named references are Teamcenter objects that relate to a specific data
             file. For each file extension, it is possible that it belongs to multiple dataset
             types. For such cases, all matching dataset types will be returned using the file
             extension as the key in the GetDatasetTypesWithFileExtensionOutput structure. The
             order of file extension in the GetDatasetTypesWithFileExtensionOutput structure may
             be different than the order of file extension input. This operation will insert file
             extensions that match the default dataset type defined in AE_default_dataset_type
             preference at the beginning of the list. This operation uses TC_Dataset_Import_Exclude_Wildcard
             preference to determine if wildcard may be used in file extension input. If the preference
             is set and file extension is set to asterisk, this operation will return all data
             set types that allow wildcards in its name reference in Teamcenter. Details about
             these two preferences can be found in Preferences and Environment (Variables Reference
             Configuration preferences, under Data management preferences).
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param FileExtensions: 
                         List of file extensions used to get the named reference information
             
        :return: Dataset type and reference information for each fileExtensions input. Possible errors
             returned in ServiceData are: 214135 The input file extension does not exist
        """
        ...
    def RefreshObjects2(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], LockObjects: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used to reload the in-memory representation of the objects from
             the database.
             
             Any references to the object will still be valid. Any in-memory changes to the original
             object will be lost. If the object has been changed in the database since it was
             last loaded, then those changes will not be present in memory.
             
             The operation updates the in memory representation to reflect database changes.
             

             If the lockObjects flag is true then it will aquire write lock on objects otherwise
             operation will release the write lock on the business objects.
             
             This is useful when client needs to do an in-process lock and unlock for shorter
             duration that does not require checkout or checkin mechanism. Client caling this
             operation to lock the objects must unlock those objects by callng this operation.
             
             This operation must be used in pairs to lock and unlock the objects.
             

Use Cases:

             Use this operation to do bulk lock & bulk unlock of Input Objects.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Objects: 
                         A list of business objects for which lock or unlock operation is required .
             
        :param LockObjects: 
                         If true then business objects will be locked , false will unlock the given business
                         objects.
             
        :return: 515109:  The instance is in use.
        """
        ...
    def GetPasteRelations(self, Inputs: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetPasteRelationsInputData]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetPasteRelationsResponse:
        """    
             Returns the paste relation names for the given parent types and the child types,
             within which the expandable relations and the preferred paste relation are indicated.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param Inputs: 
                         The list of  the parent object and the child type.
             
        :return: 39030: No preferred paste relation was found for the type.
        """
        ...
    def ReviseObjects(self, ReviseIn: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.ReviseIn]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.ReviseObjectsResponse:
        """    
             This operation is generic single revise operation for revisable business objects.
             This operation revises the given objects and copies or creates new objects using
             the data for the property values and deep copy data. Deep copy processing is recursive
             such that relations between secondary objects, or from secondary objects to the revised
             object, are replicated during this revise operation based upon deep copy rule configuration.
             This operation supports codeless configuration of custom properties. The following
             lists of revisable types are supported for this operation:
             

ItemRevision ( foundation template) and its sub-types
             
Identifier ( foundation template ) and its sub-types
             
Mdl0ConditionalElement (CPD solution ) and its sub-types
             



Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param ReviseIn: 
                         Input data containing target object and DeepCopyData of the attached objects
             
        :return: 
        """
        ...
    def ValidateValues(self, Inputs: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.ValidateInput]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.ValidateValuesResponse: ...
    def GetChildren(self, Inputs: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetChildrenInputData]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetChildrenResponse:
        """    
             This operation returns the children for each input object.  The children returned
             is determined by the input propertyNames
             list of strings which defines the properties which are to be processed in order to
             collect the children to be returned  If the propertyNames
             list is empty, then the properties which are processed to object the children is
             based on the <Type>_DefaultChildProperties and <Type>_DefaultPseudoFolder preferences.
             Please see the Preferences and Environment Variables Reference and the
             RichClient Interface Guide for information on configuring these preferences.
             Children for which the user does not have read-access will be excluded from the returned
             list of children. No partial error is given if the propertyNames
             list or the <Type>_DefaultChildProperties preference contains an invalid property
             name for the input object, children for the remaining propertyNames
             will be returned.
             

Use Cases:

             Assume the following data exists in Teamcenter:
             
             Item
             
                 Item Revision
             
                 Item Master Form
             

             The ItemRevision exists in the Item's "revision_list" property.
             
             Item Item Master Form exists in the Item's "IMAN_master_form" property.
             

Use case 1 (Get all children/no filter)

             1.    The user selects the Item in the above data in a tree viewer
             which shows all objects.
             
             2.    The user clicks the "+" to expand the Item.
             
             3.    The client then invokes getChildren with the selected object
             (Item), and no entries in the propertyNames
             argument.
             
             4.    getChildren determines the selected object's type, retrieves
             <Type>_DefaultChildProperties and <Type>_PseudoFolders preferences, and returns
             the Item Revision and Item Master Form, their type objects, and the propertyName
             in which they exist related to the parent.
             
             5.    The client then displays the returned list of children
             as child nodes in the tree.
             

Use case 2 (Get subset of children/with filter)

             1.    The user selects the Item in the above data in a tree viewer
             which only shows object related via the revision_list property.
             
             2.    The user clicks the "+" to expand the Item.
             
             3.    The client then invokes getChildren with the selected object
             (Item), and gives "revision_list" in the propertyNames
             list.
             
             4.    getChildren iterates over the propertyNames list, and returns
             the Item Revision object, its child type object, and the propertyName in which it
             exists related to the parent.
             
             5.    The client then displays the returned list of children
             as child nodes in the tree.
             


Teamcenter Component:

             Core Model Method Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform. This component defines basic method
             structure.
             
        :param Inputs: 
                         The list of objects and desired children for which to expand and return children.
             
        :return: The partial error 236027 (error) is returned if there is an error retrieving the
             value for a valid property.
        """
        ...
    def GetSubTypeNames(self, InBOTypeNames: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.SubTypeNamesInput]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.SubTypeNamesResponse:
        """    
             This operation returns sub business object type names for each business object type
             name given as the input for the specified context.
             

             It returns the input base type in the sub business object type names list too.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param InBOTypeNames: 
                         A list of business object type names with the desired context.
             
        :return: 39031: The requested context is not supported
        """
        ...
    def GenerateNextValues(self, GenerateNextValuesIn: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.GenerateNextValuesIn]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.GenerateNextValuesResponse:
        """    
             This operation generates values for the given properties of an object(s) during create/revise/save
             as action based on the user exits or naming rules configured on those properties.
             Customer user exits are given priority over the naming rules if both of them are
             configured on the same property. The counter has to be set active on the naming rule
             in order to generate the next value for a property. This operation also performs
             naming rule and multi field key validation on the generated values and return appropriate
             partial errors if the validation fails.
             
             This operation does not support generating values for attached Revision Name Rules
             on an Object type.
             
             For user exit support, an existing user exit will be called to generate values. Right
             now we support below given user exits for corresponding Object type.
             

             Object: Item
             
             User exit name: USER_new_item_id
             
             Property: item_id
             

             Object: ItemRevision
             
             User exit name: USER_new_revision_id, USER_new_revision_id_from_alt_rule (Baseline)
             
             Property: item_revision_id
             

             Object: Dataset
             
             User exit name: USER_new_dataset_id
             
             Property: pubr_object_id
             

             Object: Dataset
             
             User exit name: USER_new_dataset_rev
             
             Property: rev
             

             Object: Identifier
             
             User exit name: IDFR_new_alt_id, IDFR_new_rev_id (In Revise case)
             
             Property: idfr_id
             

             Object: CPD Objects
             
             User exit name: USER_new_cpd_id
             
             Property: CPD Objects related property
             

             Each of these user exits need some specific inputs which are required by them to
             generate IDs. These inputs are part of "generateNextValuesIn" structure and are described
             in details in its description.
             

Use Cases:

             a)    User clicks on assign button in Create/Revise/Saveas dialog:
             

             Autoassignable properties are those that have either a user exit or a naming rule
             with counter configured.A constant "autoassignable" is defined on the PropertyDescription
             class and its value can be obtained using PropertyDescription.getConstant() API.
             "Assign" button is displayed in create/revise/save as dialog to populate their values.
             

             This operation is used  to  generate the values for the autoassignable properties
             when the user clicks on the "Assign" button.The caller should collect the list of
             all autoassignable properties  that do not have any user input and pass them to this
             operation. If  the autoassignable  property has a naming rule , the  naming rule
             pattern selected by the user  for  that property should also be passed as input to
             this operation. In all other cases the naming rule pattern should be passed as empty
             string.
             

             b)    User clicks on finish button in Create/Revise/Saveas dialog:
             

             This operation is also used to generate the values for the autoassignable properties
             when the user clicks "Finish" button in in create/revise/save as dialog. The caller
             should collect the list of  all autoassignable properties that do not have any value
             generated and pass them to this operation. If  the autoassignable  property has a
             naming rule , the  naming rule pattern selected by the user  for  that property should
             also be passed as input to this operation. In all other cases the naming rule pattern
             should be passed as empty string.
             


Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param GenerateNextValuesIn: 
                         [ 1. CREATE 2. REVISE 3. SAVE-AS ].
             
        :return: 
        """
        ...
    def GetTraceReport2(self, Input: list[Teamcenter.Services.Strong.Core._2012_10.DataManagement.TraceabilityInfoInput1]) -> Teamcenter.Services.Strong.Core._2014_06.DataManagement.TraceabilityReportOutput2:
        """    
             This operation generates a Trace Report for the input objects.  The report will contain
             information about complying as well as defining objects which are connected to input
             object using FND_TraceLink, or its subtype. This operation checks if there is any
             FND_TraceLink relation starting or ending from input object(s). If FND_TraceLink
             relation exists for input object(s), then it gets the other end of FND_TraceLink
             relation and generates a trace report.
             

             Trace links can be between following objects:
             
             1  Between occurrences of an ItemRevision
             
             2  Between any two WorkspaceObject.
             

             If scope of search structure is defined for the getting trace report in input of
             this operation by sending top lines of BOMWindow instances, then matching trace link
             instances within the scope windows will be returned.
             

             If input of this operation is having list of object type names, then object type
             filter will be applied to target objects of trace link.
             

             If input of this operation is having list of trace link type names, then those types
             of trace link will be returned in trace report.
             

             If property filter is given in the input of this operation, then the additional filter
             of property will be applied on the output before sending to client.
             

             Trace report tree will be sorted for given property, sort direction can also be defined,
             if not defined then it will get default sorted in ascending direction.
             

             The output of this operation can be either sent to rich client to build the report
             or to MSExcel application.
             

             User can export this trace report to MSExcel application by sending appropriate exportTo
             mode in input. If the mode of export is "TraceReportMSExcelExport", then trace report
             will be exported to .xlsm file and this file ticket will be sent to rich client.
             Then rich client will download the file and open MSExcel application.
             


Use Cases:

             Suppose user created trace link between Requirement R1 as start point and R2 as end
             point and creates trace link from Requirement R3 as start and R1 as end point.
             
             When user runs traceability report on R1 requirement he will get R2 object as complying
             object and R3 will come as defining object.
             

             If filter will be added to show only Paragraph type objects, then nothing will be
             returned in Trace Report as the type is not matching with filter.
             

             If filter will be applied to a subtype of FND_TraceLink and above trace link is of
             type FND_TraceLink, then also empty trace report will be returned, as trace link
             type does not match with filter trace link type vector from operation input.
             

             If user invokes command to export the trace report to Excel, then trace report for
             Requirement R1 will be generated and exported in .xlsm file and opened in MSExcel
             application.
             

             Trace link on occurences:
             
             Suppose user created trace link between Requirement R1 as start point and Trace Link
             on occurrence on part P1 as end point by setting the P1's parent line as context
             line then this SOA will also return the PSBomViewRevision which was set as context
             line while creating the Trace Link.
             


Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         Information required to generate a trace report. The object(s) (for which trace report
                         needs to be generated), trace report type, if indirect report required, list of FND_TraceLink
                         types (which are expected in output of this operation), scoped line of BOM Windows
                         (within which trace link needs to searched in), the vector of object types (which
                         need to be added in output of this operation), property search input list, property
                         name by which trace report needs to be sorted, and sorting direction, format of export
                         , and if export to MSExcel application then template name to be applied on trace
                         report.
             
        :return: 
        """
        ...
    def GetTraceReportLegacy(self, Input: Teamcenter.Services.Strong.Core._2011_06.DataManagement.TraceabilityInfoInput) -> Teamcenter.Services.Strong.Core._2014_06.DataManagement.TraceabilityReportOutputLegacy:
        """    
             This operation generates a Trace Report for the input objects.  This operation returns
             information about complying as well as defining objects which are connected to selected
             object using FND_TraceLink or its subtype of GRM relation.
             

             Trace links can be between following objects:
             
             1.    Between occurrences of an ItemRevision
             
             2.    Between any two WorkspaceObject.
             

             If indirect trace report flag is set to true during this operation, then user will
             get trace report for ItemRevision if selected object is occurrence, and trace report
             for Items if selected objects is ItemRevision in addition to direct trace report
             for the selected object.
             

             If trace link is on occurrence then This SOA version will return PSBOMViewRevision
             context line information also.
             


Use Cases:

             Suppose user created trace link between Requirement R1 as start point and R2 as end
             point and creates trace link from Requirement R3 as start and R1 as end point.
             
             When user runs traceability report on R1 requirement he will get R2 object as complying
             object and R3 will come as defining object.
             

             TraceLink on occurrences:
             
             Suppose user created trace link between Requirement R1 as start point and trace link
             on occurrence on part P1 as end point by setting the P1's parent line as context
             line then this SOA will also return the PSBomViewRevision which was set as context
             line while creating the trace link.
             



Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         A TraceabilityInfoInput structure to generate a Trace Report.This input structure
                         holds selected objects for which trace report needs to be generated, trace report
                         type, if indirect report required, and base relation type.
             
        :return: 
        """
        ...
    def AddChildren(self, InputData: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.ChildrenInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation adds a list of objects as children to a list of parent objects which
             could be related by relation or reference properties. If the property name is not
             supplied as input it will use the default relation property between the parent and
             the children given by <ParentTypeName>_<ChildTypeName>_default_relation.
             
             Please see the Preferences and Environment variables reference in the Rich client
             interface guide for information on configuring these preferences.
             


Use Cases:

Add MSWord object as target attachments to EPMTask object.


             Use AddChildren operation and provide EPMTask as the parentObj, MSWord
             object as the childrenObj and target_attachments as the property name. Also,
             provide clientId value to identify this add operation.
             
             Here, the target_attachments property is a runtime property. The AddChildren
             operation internally will modify two properties attachments and attachment_types
             which are saved in the database.
             


Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param InputData: 

        :return: 
        """
        ...
    def GetPasteRelations2(self, Inputs: list[Teamcenter.Services.Strong.Core._2013_05.DataManagement.GetPasteRelationsInputData]) -> Teamcenter.Services.Strong.Core._2014_10.DataManagement.GetPasteRelationsResponse2:
        """    
             This operation returns the paste relation names for the given parent business objects
             and the child business objects name; the expandable relations and the preferred paste
             relation are also indicated.
             



Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param Inputs: 
                         List of parent parent and child buiness objects<b> </b>with clientId
             
        :return: 
        """
        ...
    def RemoveChildren(self, InputData: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.ChildrenInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes a list of objects as children to a list of parent objects
             which could be related by relation or reference properties. If the property name
             is not supplied as input it will use the default relation property between the parent
             and the children given by ParentTypeName>_ChildTypeName>_default_relation.
             
             Please see the Preferences and Environment variables reference in the Rich client
             interface guide for information on configuring these preferences.
             


Use Cases:

Remove Item object from Folder object with contents property name.


             Use RemoveChildren operation and provide Folder object as the parent object,
             Item object as the children object and contents as the property name. Also,
             provide clientId value to identify this remove children operation. The RemoveChildren
             operation will remove Item object from the Folder parent object.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param InputData: 

        :return: 
        """
        ...
    def GenerateIdsUsingIDGenerationRules(self, GenerateIdsInputs: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.GenerateIdInput]) -> Teamcenter.Services.Strong.Core._2014_10.DataManagement.GenerateIdsResponse:
        """    
             This operation generates object ids using ID Generation Rules associated with the
             business object's property. Currently only Item and its subtypes are supported. Object
             ids are generated using information provided in createInput.
             
             This operation should be called in case of a specific requirement where ID Generation
             is independent of creating Objects. (e.g. in case of some CAD applications where
             ids are created first, used in the system with temporary objects which can be saved
             at the later point of time). In most of the cases 'Teamcenter::Soa::Core::_2008_06::createObjects(const
             std::vector<CreateIn> &input)' handles id Generation and object creation.
             
             This operation should be invoked when an ID Generation Rule is attached to a Business
             Object. To identify whether the ID Generation Rule is attached to the Business Object,
             check if 'fnd0IdGenerator' property points to the compound Create Descriptor of same
             Business Object.
             

             For more information on how to configure ID Generation RUles, refer to the Business
             Modeler IDE Guide.
             


Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param GenerateIdsInputs: 
<ul>
<li type="disc">A Structure containing input values for the operation
                         </li>
</ul>

        :return: 74033  : No ID Generation Rule is attached to the type Type. Please contact your
             system administrator.
        """
        ...
    @typing.overload
    def GetDeepCopyData(self, DeepCopyDataInput: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.DeepCopyDataInput]) -> Teamcenter.Services.Strong.Core._2014_10.DataManagement.GetDeepCopyDataResponse: ...
    @typing.overload
    def GetDeepCopyData(self, DeepCopyDataInput: Teamcenter.Services.Strong.Core._2015_07.DataManagement.DeepCopyDataInput) -> Teamcenter.Services.Strong.Core._2015_07.DataManagement.GetDeepCopyDataResponse: ...
    def SaveAsObjectsAndRelate(self, IVecSoaSavAsIn: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.SaveAsIn], IVecSoaRelteInfoIn: list[Teamcenter.Services.Strong.Core._2012_09.DataManagement.RelateInfoIn]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsObjectsResponse:
        """    
             This operation performs SaveAs on the input target business object and its related
             objects as new instances. Related objects are identifed using deep copy rules. Optionally,
             this method relates the new object to the input target object or to a default folder.
             

Use Cases:

Use Case 1:     SaveAs without relate

             Client constructs the "SaveAs" dialog for a business object using SaveAs operation
             descriptor. The information returned by that operation allows client to construct
             the SaveAs dialogs and DeepCopy panels for user input.
             
             Once the user input is received, client makes subsequent invocation to this operation
             to execute SaveAs on the object. The method is invoked with "relate" option as false.
             
             New object is created using values passed in. It is not found under Home / NewStuff
             folder / anyother parent object. The new object stays dangling.
             
Use Case 2:     SaveAs and relate to default folder

             Client invokes SaveAs operation as mentioned in use case 1 with "relate" as true
             but chooses not to specify target object or relation. This operation will choose
             a default folder and choose a default relation to be used. The default folder is
             decided based on the value set for the preference, WsoInsertNoSelectionsPref. When
             the preference value is set as 1 the default folder will be the New Stuff folder
             of the service user. When the preference value is 2 the default folder will be the
             Home folder of the service user.
             
             Newly created object is related to the default folder using default relation. For
             any other value of the preference, the relation will not be created.
             
Use Case 3:     SaveAs and relate to specified target object using specified
             relation

             Client invokes SaveAs operation as mentioned in use case 1. The input parameter carrying
             the relation info has the boolean "relate" flag which is true, a valid target object
             and a property name to which the relation is to be created.
             
             After a successful creation, this operation relates the newly created object to the
             specified target object using specified relation.
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param IVecSoaSavAsIn: 
                         Input data containing target object, map (PropertyValuesMap) of properties and their
                         corresponding values and DeepCopyData of the attached objects.
             
        :param IVecSoaRelteInfoIn: 
                         Input data containing the paste options used to relate the newly created object.
             
        :return: :     The SaveAs operation performed on the object input in the parameter
             carrying the SaveAs info has failed.
        """
        ...
    def PruneNamedReferences(self, NamedReferences: list[Teamcenter.Soa.Client.Model.Strong.POM_object]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation performs a prune operation by a given list of Dataset named references, per the following criteria
             
             1. Remove the input named references from their owning Dataset

             2. Delete the input named reference objects
             
             3. Delete the owning Dataset objects which contain no named references after the prune operation
             
             4. The pruned named references, deleted Datasets
             and updated Datasets will be returned
             


Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param NamedReferences: 
                         List of <b>Dataset</b> <font face="courier" height="10">named references</font> to
                         be pruned
             
        :return: 
        """
        ...
    def GetLocalizedProperties2(self, PropertyInfo: list[Teamcenter.Services.Strong.Core._2010_04.DataManagement.PropertyInfo]) -> Teamcenter.Services.Strong.Core._2015_07.DataManagement.LocalizedPropertyValuesResponse:
        """    
             Typically business object property values are returned in the locale of the current
             session, this operation returns desired property values in any of the supported locales
             of the Teamcenter server. String type properties may be localized with values for
             each supported locale, this operation will return the translated values for one or
             more desired locales.
             

Use Cases:

             Retrieve the localized values for localizable property
             

             When running Teamcenter in language environment other than the English, user wants
             to see the localized property value to be displayed in corresponding language in
             the UI. This operation can be used to fulfill this requirement. By providing the
             desired business object, internal name of the properties, and specific locale name(s),
             this operation will return the localized property value(s) in that particular locale(s)
             and the internal value(s) of the status corresponding to localized value(s) in that
             locale(s).
             

Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param PropertyInfo: 
                         A list of desired business objects, property names, and locales to retrieve those
                         properties in.
             
        :return: 38044: The property value is not set.
        """
        ...
    def GetCreatbleSubBuisnessObjectNames(self, Input: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreatableSubBONamesInput]) -> Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreatableSubBONamesResponse:
        """    
             This operation returns sub business object  names that are displayable to the login
             user in the object creation dialog and their display names for each primary business
             object given as the input, based on specified context. Returned business object lists
             have exclusions of business objects and their secondary business objects as per the
             exclusion preference and/or exlusion business object names specified in the input.
             If the context is specified as legacy, the sub business objects of the primary business
             object are returned only if the primary business object is listed in the site preference
             TYPE_DISPLAY_RULES_list_types_of_subclasses. If the context is left blank, then all
             creatable sub business objects are returned. This operation returns the hierarchy
             of creatable objects for each business object it returns.
             

Use Cases:

Use Case 1: Get all Creatable sub business object names for a given business object

             While creating an object of a business object, user needs to know all the sub business
             objects that can be created. To get all creatable sub business objects for a given
             business object for the logged in user, this operation should be invoked by providing
             empty value for context. Any specific sub business objects that need to be excluded
             from the returned list, can be specified through exclusionPreference and/or exclusionBONames
             parameters.
             

Use Case 2: Get Creatable sub business objects for a given primary business object,
             excluding sub business objects from its sub classes

             While creating an object of a primary business object, user needs to know only the
             sub business objects that can be created for the primary business object, excluding
             the business objects from its sub classes, for example, in the legacy Create wizards
             from Teamcenter Rich Application Client. To get only the creatable direct sub business
             objects for a given primary business object for the logged in user, this operation
             should be invoked by providing legacy as the value for context parameter.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param Input: 
                         A list of primary business object names and the exclusion preferences and/or types,
                         along with context, for which the creatable sub business object names are to be retrieved
             
        :return: 
        """
        ...
    def GenerateNextValuesForProperties(self, PropertyNamingRuleInfo: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.PropertyNamingruleInfo]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.GenerateNextValuesResponse: ...
    def GetDomainOfObjectOrType(self, Inputs: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.GetDomainInput]) -> Teamcenter.Services.Strong.Core._2015_07.DataManagement.DomainOfObjectOrTypeResponse: ...
    def CreateRelateAndSubmitObjects2(self, CreateInputs: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreateIn2]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    def ReassignParticipants(self, ReassignParticipantInfo: list[Teamcenter.Services.Strong.Core._2015_10.DataManagement.ReassignParticipantInfo]) -> Teamcenter.Services.Strong.Core._2015_10.DataManagement.ReassignParticipantResponse:
        """    
             Reassigns the participant roles from one user to another for a given list of participant
             types on the input list of objects. The Particpant for the fromAssignee User
             is replaced with the Particpant for the toAssignee User. If the toAssignee
             User already exists as participant, then the fromAssignee User will
             not be replaced.
             

Use Cases:

             For Change Management use cases, user may need to reassign participant roles on the
             change objects like analyst, change specialist etc.  This operation can be used to
             reassign such participants.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param ReassignParticipantInfo: 
                         A list of structures containing a list of input objects whose participant roles are
                         reassigned, assignee to reassign from, assignee to reassign to list of participant
                         types, flag to indicate all participan types and comments.
             
        :return: 214470 - Failed to reassign participants.
        """
        ...
    def GenerateContextSpecificIDs(self, GenerateContextIDsIn: list[Teamcenter.Services.Strong.Core._2016_05.DataManagement.GenerateContextIDsInput]) -> Teamcenter.Services.Strong.Core._2016_05.DataManagement.GenerateContextSpecificIDsResponse:
        """    
             Generates the range of unique IDs for input context names. The number of IDs generated
             for each context name depends on the input. If for a given context name, the ID has
             been reset using Teamcenter service resetContextID, then this service generates IDs
             for that context from the beginning.
             
             ID generation will also reset when the maximum limit is met. This limit is maximum
             number supported on 64 bit machine.
             

             WARNING: IDs generated using this service  are unique within a given context name,
             but are not guaranteed to be unique in all Teamcenter contextx. Caution should be
             used if requesting ids for item or other Teamcenter objects that require unique ids.
             The caller may choose to validate uniqueness in the use cases. By default Teamcenter
             will not allow an object be saved if it violates defined uniqueness criteria.
             

Use Cases:

             A user has a context name for which he wants to generate IDs. The user provides the
             context name and the number for IDs to be generated to this Teamcenter service. In
             response the user recives a block of IDs. If the user again uses this service to
             generate additional IDs for the same context name, new IDs are generated and returned
             in the response structure. The IDs generated in two calls of this service for a given
             context name are unique unless the service resetContextID has been called for that
             context between the two calls to generate IDs.
             

Teamcenter Component:

             Core Model Property Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform.  This component defines properties.
             
        :param GenerateContextIDsIn: 
                         List of GenerateContextIDsInput which contains the context name and number of IDs
                         to be generated for that context. Context name string length is supported up to 256
                         characters. There is no limit for the number fo IDs that can be generated for a given
                         context name.
             
        :return: 
        """
        ...
    def ResetContextID(self, ContextNames: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service enables the client to reset the ID for given context names. When the
             IDs for a context name are reset, ID generation will begain from beginning value.
             

             WARNING: Be advised that if a client resets the ID for a context name, it is possible
             that repeated IDs will be returned from generateContextSpecificIDs service for that
             context name.
             

Use Cases:

             A client has a context name for which it has generated IDs and now wants to generate
             the IDs for that context name again from the beginning. Client calls this Teamcenter
             service to reset the ID for this context name. The next time the client calls generateContextSpecificIDs
             for this context block of returned IDs starts from the beginning value 0.
             

Teamcenter Component:

             Core Model Property Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform.  This component defines properties.
             
        :param ContextNames: 
                         List of the context names for those, IDs to be reset. Empty strings should not be
                         used to reset ID. An error is returned, if the client tries to send empty string
                         as context name.
             
        :return: 
        """
        ...
    def SetPropertiesAndDetectOverwrite(self, PropData: list[Teamcenter.Services.Strong.Core._2016_05.DataManagement.PropData], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Core._2016_05.DataManagement.SetPropsAndDetectOverwriteResponse: ...
    def CreateAttachAndSubmitObjects(self, Inputs: list[Teamcenter.Services.Strong.Core._2015_07.DataManagement.CreateIn2]) -> Teamcenter.Services.Strong.Core._2016_09.DataManagement.CreateAttachResponse:
        """    
             This is a generic operation for creation of business objects. This will also create
             any secondary (compound) objects that need to be created, assuming the CreateInput2
             for the secondary object is represented in the nested CreateInput2 object. e.g. Item
             is primary object that also creates an  Item Master and ItemRevision.
             ItemRevision in turn creates ItemRevision Master. The input for all
             these levels is passed in through the recursive CreateInput2 object.
             

             This operation also performs following tasks:
             

A list of file names can be passed in through the dataToBeRelated
             input of the CreateIn2 input object, and Dataset objects for the files will
             be created and related to the created business object. The information needed to
             subsequently upload the file contents will be passed back to the user in the CreateAttachResponse
             object.
             
Submit the created business object to a workflow process. The input
             for creating the workflow process is passed in through the workflowData input of
             CreateIn2 object.
             
Relate the created business object to the input target object.
             
If the created business object is under Item Revision Definition
             Configuration (IRDC) control, proposed file attachments are first evaluated against
             the object's IRDC settings to check if they are valid or not. Invalid files will
             be discarded. If the created business object is not under IRDC control, the files
             will simply be related to the created business object as Dataset objects.
             
Proposed file attachments to the created business object are specified
             as file names rather than unique ids of existing business objects. Empty Dataset
             objects are created and write tickets are fetched for the files that will be uploaded
             as named references.
             



Use Cases:

             Use Case 1: Create an Item object under IRDC control.
             

             The user wants to create and Item and its associated objects, and furthermore will
             set some of the create inputs so that the newly created object will be under Item
             Revision Definition Configuration (IRDC) control. No files or workflow inputs are
             provided.
             

             Use Case 2: Create an Item object under IRDC control and submit it to a workflow.
             

             As with Use Case 1, but the name of a workflow template is provided. After the Item
             object is created, it will be submitted to the specified workflow.
             

             Use Case 2: Create an Item object under IRDC control, attach files, and submit it
             to a workflow.
             

             As with Use Case 2, but a list of file names is provided. After the Item object is
             created, one Dataset object will be created for each file name and related to the
             ItemRevision. File tickets will be passed back to the user in the CreateAttachResponse
             object so that the files can be uploaded to the Dataset objects' named references.
             Then the newly created Item is submitted to the specified workflow.
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param Inputs: 
                         Each CreateIn2 object has a client id which can be used to map to any partial errors
                         in the ServiceData information returned in the output.
             
        :return: 33028 - The template (value) cannot be found.
        """
        ...
    def CreateObjectsInBulkAndRelate(self, CreateInputs: list[Teamcenter.Services.Strong.Core._2018_06.DataManagement.CreateIn3]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse: ...
    def UnlinkAndDeleteObjects(self, DeleteInput: list[Teamcenter.Services.Strong.Core._2019_06.DataManagement.DeleteIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation unlinks the input objects from their corresponding container and then
             attempts to deletes them. The input objects are related to the container as the reference
             or relation property supplied as part of the input. The operation also takes a flag
             whether to unlink the objects from the container in case the deletion fails.
             

             After unlinking the objects from the input container, if the objects being deleted
             are still referenced by other objects then error is returned to the caller. Any other
             error in deletion of the objects are also returned to the caller.
             

             In case the input argument objectsToDelete contains objects of type Item,
             then the operation also deletes all ItemRevision objects, associated ItemMaster,
             ItemRevisionMaster form objects.
             

             If the input argument objectsToDelete are of type ItemRevision and if is the
             last revision of the Item then the operation deletes the Item, associated
             ItemMaster, ItemRevisionMaster form objects.
             

             The input argument objectsToDelete can be an ImanRelation.
             

Teamcenter Component:

             Core Model Types - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Types
             framework.
             
        :param DeleteInput: 
                         A list containing an input container and list of objects to be first unrelated from
                         the container and then deleted.
             
        :return: 214139  - The business object could not be deleted. Please refer to the Teamcenter
             server syslog file for more information.
        """
        ...
    def CreateIdDisplayRules(self, IdDispRuleCreIns: list[Teamcenter.Services.Strong.Core._2020_01.DataManagement.IDDispRuleCreateIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates the ID Display Rules (IdDispRule) with the input ID
             Context information.
             
             ID Display Rule contains the list of ID Contexts and their order. Based on the order
             of the ID Contexts defined, the system evaluates the display name of the Item
             and ItemRevision from their Alternate IDs.
             

             ID Context (IdContext), represents the context information under which the
             OEM defines the unique IDs of their Item and ItemRevision. This context
             information is used when Teamcenter users define the unique IDs of Item and
             ItemRevision objects.
             

             User can set one of the ID Display Rules as the current ID Display Rule. The current
             ID Display Rule is used to evaluate the display names of the Item and ItemRevision.
             In case the ID Context of the Alternate ID with the Item and ItemRevision
             object does not match with that of the current ID Display Rule then system uses the
             default ID Display Rule to evaluate the display names of Item and ItemRevision
             objects.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param IdDispRuleCreIns: 
                         A list of objects of type IdDispRuleCreateIn. The data on IdDispRuleCreateIn is used
                         to create the <b>IdContextRule</b> objects with input name and ID contexts.
             
        :return: 
        """
        ...
    def GetIdentifierTypes(self, IdentifierTypesIn: list[Teamcenter.Services.Strong.Core._2020_01.DataManagement.IdentifierTypesIn]) -> Teamcenter.Services.Strong.Core._2020_01.DataManagement.IdentifierTypesOut:
        """    
             This operation fetches the applicable Identifier types for the input objects
             of type Item and/or ItemRevision along with the input IdContext
             object. System queries the ID Context Rules defined in Teamcenter database and retrives
             the Identifier types.
             

             Alternate and Alias IDs are defined in Teamcenter as instances of business object
             of type Identifier. ID Context, of business object type IdContext,
             represents the context information under which the OEM defines the unique IDs of
             their Item and ItemRevision. This context information is used when
             Teamcenter users define the Alternate and Alias IDs of Item and ItemRevision
             objects.
             

             ID Context Rules are defined as instances of business object type IdContextRule
             in Teamcenter database. These rules map the combination of ID Context and the object
             type e.g.  Item or ItemRevision, called Identifiable types, to the
             type of the Identifier applicable in the context.
             

             This operation also returns the other applicable objects for which Alternate IDs
             along with the input objects can be defined. In case of input objects of type Item,
             this operation returns the list of revision objects of the Item, and in case
             of input objects of type ItemRevision, this operation returns the Item
             object as the applicable object for which Alternate IDs can be defined.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param IdentifierTypesIn: 
                         A list of objects of type IdentifierTypesIn. The data on IdentifierTypesIn is used
                         to query <b>Identifer</b> type based on input <b>Item</b> or <b>ItemRevision</b>
                         and <b>IdContext</b>.
             
        :return: 
        """
        ...
    def GetIdContexts(self, InputObjs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Teamcenter.Services.Strong.Core._2020_01.DataManagement.IDContextOutput:
        """    
             This operation fetches all instances of the ID Context objects (IdContext)
             from the Teamcenter database applicable for the input objects of type Item
             and ItemRevision based on defined ID Context Rules (IdContextRule)
             by the system administrators.
             

             This operation queries ID Context Rule objects and fetches the ID Context objects
             based on the input Item, ItemRevision or null. The input is the identifiable
             type defined on the ID Context Rules. For a null input, it returns the Id Context
             objects where the identifiable type is null.
             
             All ID Context objects from the Teamcenter data base are returned in case input object
             is other than Item, ItemRevision or null. An empty input list would
             also return all ID Context objects from the Teamcenter data base.
             

IdContext objects represents the context information under which the OEM defines
             the unique IDs of their Item and ItemRevision objects. This context
             information is used when Teamcenter users define the unique IDs of Item and
             ItemRevision objects.
             

             Alternate and Alias IDs of Teamcenter are the example of the such unique IDs of Item
             and ItemRevision. Users define Alternate and Alias IDs with the help of the
             ID Context as one of the unique attribute of the ID.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param InputObjs: 
                         A list of objects of type <b>WorkspaceObject</b> or null for which the objects of
                         type <b>IdContext</b> are fetched.
             
        :return: objects found.
        """
        ...
    def GenerateContextSpecificIDs2(self, GenerateContextIDsIn: list[Teamcenter.Services.Strong.Core._2020_04.DataManagement.GenerateContextIDsInput2]) -> Teamcenter.Services.Strong.Core._2016_05.DataManagement.GenerateContextSpecificIDsResponse:
        """    
             Generates the range of unique IDs for input context names. The number of IDs generated
             for each context name depends on the input. If for a given context name, the ID has
             been reset using Teamcenter service resetContextID, then this service generates IDs
             for that context from the beginning.
             

             ID generation will also reset when the maximum limit is met. This limit is maximum
             number supported on 64 bit machine.
             

             If the validation flag is true and both contextType and contextPropName are provided,
             the generated IDs will be validated for uniquness.
             

Teamcenter Component:

             Core Naming Rules - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines Naming
             Rules and Revision Naming Rules.
             
        :param GenerateContextIDsIn: 
                         A list of GenerateContextIDsInput2 which contains the context name, type, property
                         name, validation flag, and number of IDs to be generated for that context. Context
                         name string length is supported up to 256 characters. There is no limit for the number
                         fo IDs that can be generated for a given context name.
             
        :return: 
        """
        ...
    def AddNamedReferenceToDatasets(self, AddNamedReferenceIn: list[Teamcenter.Services.Strong.Core._2021_06.DataManagement.AddNamedReferenceToDatasetInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveNamedReferenceFromDataset2(self, RemoveNamedReferenceIn: list[Teamcenter.Services.Strong.Core._2021_06.DataManagement.RemoveNamedReferenceFromDataset]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class DigitalSignatureRestBindingStub(DigitalSignatureService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ApplySignatures(self, Input: list[Teamcenter.Services.Strong.Core._2014_06.DigitalSignature.ApplySignaturesInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetSignatureMessages(self, TargetObject: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Core._2014_06.DigitalSignature.GetSignatureMessagesResponse: ...
    def VoidSignatures(self, Input: list[Teamcenter.Services.Strong.Core._2014_06.DigitalSignature.VoidSignaturesInputData], ElectronicSignature: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class DigitalSignatureService:
    """
    
            The DigitalSignature service provides operations to digitally sign objects in Teamcenter.
            The Digital Signature service  is used for data management to help establish authenticity,
            integrity and non-repudiation between data and user in a business environment. The
            operations in this service allow computation of signature messages, applying of digital
            signature and voiding the digital signatures on a given Business Object.
            


Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DigitalSignatureService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ApplySignatures(self, Input: list[Teamcenter.Services.Strong.Core._2014_06.DigitalSignature.ApplySignaturesInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation applies digital signature to a list of Business objects provided in
             the input. The operation input is a list of DigitalSignatureInput structures. Each
             structure in this list consists of details pertaining to the Business Object and
             its corresponding CMS (Cryptographic Message Syntax). Digital Signature is allowed
             to be applied on business objects for which the business object constant Fnd0AllowDigitalSignature
             is enabled.
             

Use Cases:

             To apply digital signature from RAC, the operation getSignatureMessages should first
             be called to compute the signature messages for the input business objects. This
             should be followed by a call to the SOA framework method com.teamcenter.soa.client.PKCS7.sign
             , which takes signature message as input and provides the encrypted string as output.
             The encrypted string is passed as input to the operation applyDigitalSignatures.
             Successful completion of the operation, is an indication that the digital signature
             has been applied to the input business object.
             

Teamcenter Component:

             Fnd0CoreModelSignature - Digital signature core model signature component.
             
        :param Input: 
                         A list of DigitalSignatureInput structures containing the business object and its
                         corresponding CMS ( Cryptographic Message Syntax ).
             
        :return: 
        """
        ...
    def GetSignatureMessages(self, TargetObject: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Core._2014_06.DigitalSignature.GetSignatureMessagesResponse:
        """    
             This operation returns signature messages for a list of business objects. These signature
             messages are used by SOA framework method  com.teamcenter.soa.client.PKCS7.sign
             API to generate CMS string (Cryptographic Message Syntax). The operation response
             GetSignatureMessagesResponse contains details of signature messages computed for
             each of the input business objects along with the ServiceData. The attributes that
             are to be used for signature message computation are configured using the business
             object constant Fnd0DigitalSignatureAttributes and Fnd0DigitalSignatureChildObjects.
             

Teamcenter Component:

             Fnd0CoreModelSignature - Digital signature core model signature component.
             
        :param TargetObject: 
                         A list of business objects for which signature messages need to be computed.
             
        :return: 
        """
        ...
    def VoidSignatures(self, Input: list[Teamcenter.Services.Strong.Core._2014_06.DigitalSignature.VoidSignaturesInputData], ElectronicSignature: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation voids the selected digital signatureson a given target object.. The
             details of  the electronic signature may be obtained by calling the requisite SOA
             framework method com.teamcenter.soa.client.PKCS7.sign. ..This is provided as input
             to the voidDigitalSignatures opearation along with the other inputs. Successful completion
             of the operation, is an indication that the selected digital signature objects have
             been voided for the input business object.
             

Use Cases:

             After applying a digital signature,the object is locked for modification and users
             would not be able to modify any of the attribute values. In certain conditions, the
             current values on the object would need to be updated and the digital signature would
             need to be reapplied with the updated set of values. To achieve this, the existing
             digital signatures on the object are voided and  required values are updated . After
             all the updates are complete,  digital signature is reapplied on the object. It is
             to be noted that if all the Digital Signatures on an object are voided, then the
             object state is equivalent to not having any digital signature applied and is open
             for updates
             

Teamcenter Component:

             Fnd0CoreModelSignature - Digital signature core model signature component.
             
        :param Input: 
                         This structure contains input parameters required for voidSignatures operation.
             
        :param ElectronicSignature: 
                         An electronic signature that will be used to validate that the person requesting
                         the void operation is the one who logged in to the tcserver that will process the
                         request.
             
        :return: 
        """
        ...

class DispatcherManagementRestBindingStub(DispatcherManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateDispatcherRequest(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.DispatcherManagement.CreateDispatcherRequestArgs]) -> Teamcenter.Services.Strong.Core._2008_06.DispatcherManagement.CreateDispatcherRequestResponse: ...

class DispatcherManagementService:
    """
    
            This service provides the method for creating a Dispatcher Request object within
            Teamcenter.  The Dispatcher Request objects are used with the Dispatcher application
            for performing asynchronous operations such as translations, workflow updates, etc.
            where distributed processing is preferred.
            



Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DispatcherManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateDispatcherRequest(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.DispatcherManagement.CreateDispatcherRequestArgs]) -> Teamcenter.Services.Strong.Core._2008_06.DispatcherManagement.CreateDispatcherRequestResponse:
        """    
             Create a DispatcherRequest within Teamcenter for use with Dispatcher Management
             Services.
             

Use Cases:

             The Dispatcher Management application provides the ability to process requests in
             an asynchronous fashion thus removing the processing burden from the clients to provisioned
             machine dedicated to processing these requests.  There are quite a few services,
             within Teamcenter and other applications that use this application.
             

             Here are a few examples:
             

Asynchronous Processing (if configured)
             
NXtoPVDirect (provided with NX)
             
PreviewService
             



Teamcenter Component:

             Dispatcher - A set of component (scheduler; translation modules; and translators)
             that provides distributed execution of translations across multiple machine. It has
             capability to schedule jobs to run at specified times in an asynchronous manner.
             
        :param Inputs: 
                         holds the values needed to create the <b>DispatcherRequest</b>.
             
        :return: (s) back to the client
             or a NULLTAG if the creation was unsuccessful.
        """
        ...

class EnvelopeRestBindingStub(EnvelopeService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def SendAndDeleteEnvelopes(self, Envelopes: list[Teamcenter.Soa.Client.Model.Strong.Envelope]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class EnvelopeService:
    """
    
            The Envelope service provides an operation for sending envelopes to the associated
            recipients. An envelope represents Envelope business object with information about
            a mail such as subject, body of message, recipients, and attachments. Recipients
            are of two types: external and internal, and can be added under To or Cc list. External
            recipients are email addresses, while internal recipients are Teamcenter users, groups
            and address lists. Envelopes are delivered as email notifications to external recipients.
            For internal recipients, the envelopes are delivered to the associated user Teamcenter
            Mailbox. However, if the Mail_OSMail_activated site preference is set to true, email notifications are also sent to the internal recipients.
            
            This service addresses the following use cases:
            

Send mail messages and emails to Teamcenter users
            
Send emails to external users
            

            .
            

Dependencies:

            DataManagement
            


Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> EnvelopeService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def SendAndDeleteEnvelopes(self, Envelopes: list[Teamcenter.Soa.Client.Model.Strong.Envelope]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sends mails to the recipients of each Envelope business object
             in envelopes. All the envelopes passed to this operation are deleted after they are
             processed, even if the processing is not successful. Each Envelope business
             object contains mail information such as subject, body, recipients, and attachments.
             Recipients can be Teamcenter users, groups and address lists, or, external email
             addresses. Teamcenter users receive envelopes in their Teamcenter Mailbox and also
             as emails if Mail_OSMail_activated site preference is set to true.To send the emails, the site preference Mail_server_name
             should be properly configured. Any errors that occur while sending envelopes are
             returned as partial errors in ServiceData.
             

Use Cases:

             Use case 1: Send envelopes to Teamcenter users

             You can send envelopes to the Mailbox of Teamcenter users by specifying the users
             as recipients on Envelope business objects.  Also, email messages can be sent to
             Teamcenter users if Mail_OSMail_activated site preference is set to true.
             

             User case 2: Send emails to external email addresses

             Email messages can be sent to external users by specifying their email addresses
             as recipients on Envelope business objects.
             


Teamcenter Component:

             Mail - Sends SMTP (Simple Mail Transfer Protocol) e-mail to Teamcenter users.Uses
             platform-independent utility to send e-mail on both UNIX and Windows platforms.
             
        :param Envelopes: 
                         The list of <b>Envelope</b> business objects to be sent.
             
        :return: 
        """
        ...

class LanguageInformationRestBindingStub(LanguageInformationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetAllTranslationStatuses(self) -> Teamcenter.Services.Strong.Core._2010_04.LanguageInformation.TranslationStatusResponse: ...
    def GetLanguagesList(self, Scenario: str) -> Teamcenter.Services.Strong.Core._2010_04.LanguageInformation.LanguageResponse: ...

class LanguageInformationService:
    """
    
            The LanguageInformation service contains
            operations that are used to retrieve different language information relative to the
            Teamcenter session, or to the language settings as specified in the preference values.
            
            This language information is used for language related data by Teamcenter processes
            (e.g. property value creation, property value display, data search, etc.).
            
            This service fulfills the following use cases for the manipulation of language information:
            

Retrieval of all information regarding translation statuses (the
            enumeration, localized name and description) which have been defined in the current
            Teamcenter system.
            
Retrieval of a list of languages that can be used for displaying
            localized property values.
            
Retrieval of a list of languages that can be used for localized property
            value entries.
            
Retrieval of a list of languages that are supported by the system
            and can be used for property localization in the BMIDE.
            
Retrieval of the language that can be used for search operations.
            
Retrieval of all the languages that are supported by the system.
            




Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LanguageInformationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetAllTranslationStatuses(self) -> Teamcenter.Services.Strong.Core._2010_04.LanguageInformation.TranslationStatusResponse:
        """    
             Retrieves the full set of translation statuses: their enumeration, localized name
             and description.
             
             Currently, the translation statuses in the Teamcenter system includes: "Master",
             "Approved", "Pending", "In-Review", and "Invalid"
             


Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :return: 
        """
        ...
    def GetLanguagesList(self, Scenario: str) -> Teamcenter.Services.Strong.Core._2010_04.LanguageInformation.LanguageResponse:
        """    
             Retrieves a list of languages according to different scenarios as specified in the
             input parameter.
             
             All the returned language names are in the Java-standard format.
             

Teamcenter Component:

             Core Model L10N framework - The framework to provide a user interface in the locale
             of users as well as manage the product information (metadata, operation data and
             file content) in multiple languages.
             
        :param Scenario: 
<ul>
<li type="disc">"<i>supportedLanguages</i>": To retrieve all the languages supported
                         by the system.
                         </li>
<li type="disc">"<i>localizationLanguages</i>": To retrieve all languages supported
                         by the system and declared as usable for property value localization in the both
                         BMIDE Global Constant "<font face="courier" height="10">Fnd0SelectedLocales</font>"
                         and "<font face="courier" height="10">SiteMasterLocale</font>".
                         </li>
</ul>

        :return: 
        """
        ...

class LogicalObjectRestBindingStub(LogicalObjectService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetLogicalObjects(self, LoInputs: list[Teamcenter.Services.Strong.Core._2017_11.LogicalObject.GetLogicalObjectInput]) -> Teamcenter.Services.Strong.Core._2017_11.LogicalObject.GetLogicalObjectResponse: ...
    def GetLogicalObjects2(self, LoInputs: list[Teamcenter.Services.Strong.Core._2018_06.LogicalObject.GetLogicalObjectInput2]) -> Teamcenter.Services.Strong.Core._2018_06.LogicalObject.GetLogicalObjectResponse2: ...
    def GetLogicalObjectsWithContext(self, LoInputs: list[Teamcenter.Services.Strong.Core._2018_11.LogicalObject.GetLogicalObjectInput3]) -> Teamcenter.Services.Strong.Core._2018_11.LogicalObject.GetLogicalObjectResponse3: ...

class LogicalObjectService:
    """
    
            The logical object service provides various operations to create, update, delete
            and retrieve logical object definitions and also to retrieve logical objects and
            their properties.
            

            Logical Object Definition is composed of:
            

A root object
            
Member objects which are traversed starting from root
            
Presented properties which are presented onto the logical object
            from the root and member objects
            




Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LogicalObjectService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetLogicalObjects(self, LoInputs: list[Teamcenter.Services.Strong.Core._2017_11.LogicalObject.GetLogicalObjectInput]) -> Teamcenter.Services.Strong.Core._2017_11.LogicalObject.GetLogicalObjectResponse: ...
    def GetLogicalObjects2(self, LoInputs: list[Teamcenter.Services.Strong.Core._2018_06.LogicalObject.GetLogicalObjectInput2]) -> Teamcenter.Services.Strong.Core._2018_06.LogicalObject.GetLogicalObjectResponse2: ...
    def GetLogicalObjectsWithContext(self, LoInputs: list[Teamcenter.Services.Strong.Core._2018_11.LogicalObject.GetLogicalObjectInput3]) -> Teamcenter.Services.Strong.Core._2018_11.LogicalObject.GetLogicalObjectResponse3: ...

class LOVRestBindingStub(LOVService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetAttachedLOVs(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_06.LOV.LOVInfo]) -> Teamcenter.Services.Strong.Core._2007_06.LOV.AttachedLOVsResponse: ...
    def GetLOVAttachments(self, ObjectStructArray: list[Teamcenter.Services.Strong.Core._2011_06.LOV.LOVAttachmentsInput]) -> Teamcenter.Services.Strong.Core._2011_06.LOV.LOVAttachmentsResponse: ...
    def GetInitialLOVValues(self, InitialData: Teamcenter.Services.Strong.Core._2013_05.LOV.InitialLovData) -> Teamcenter.Services.Strong.Core._2013_05.LOV.LOVSearchResults: ...
    def GetNextLOVValues(self, LovData: Teamcenter.Services.Strong.Core._2013_05.LOV.LOVData) -> Teamcenter.Services.Strong.Core._2013_05.LOV.LOVSearchResults: ...
    def ValidateLOVValueSelections(self, LovInput: Teamcenter.Services.Strong.Core._2013_05.LOV.LOVInput, PropName: str, UidOfSelectedRows: list[str]) -> Teamcenter.Services.Strong.Core._2013_05.LOV.ValidateLOVValueSelectionsResponse: ...
    def ValidatePropertyValuesForLOVInBulk(self, Inputs: list[Teamcenter.Services.Strong.Core._2021_12.LOV.ValidatePropertyValuesForLOVInBulkInputData]) -> Teamcenter.Services.Strong.Core._2021_12.LOV.ValidatePropertyValuesForLOVInBulkResponse: ...

class LOVService:
    """
    
            This service exposes the operations to returns LOV attachments attached to properties
            which are attached with project based conditions. This service can also be
            used for properties attached with session based attachments. Please note following
            points when using this service for efficient use:
            

            a)Â Â Â Â This service need to be used for each object which has
            properties attached with project based conditions.  To figure out whether a property
            is attached with project based conditions or not look at the value of the lovAttachmentCategory
            on respective property descriptor.
            

            b)Â Â Â Â Project based conditions would come into picture when editing
            an object. For create/save as/revise scenario's applications should display session
            based attachments which would have been retrieved using property services.
            

            c)Â Â Â Â This service also returns session based valid attachment.
            If application codes deals with Property Descriptors, then properties may have already
            holding valid session based attachment
            
            .
            

Dependencies:

            PropDescriptor
            


Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LOVService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetAttachedLOVs(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_06.LOV.LOVInfo]) -> Teamcenter.Services.Strong.Core._2007_06.LOV.AttachedLOVsResponse:
        """    
             Get attached LOV based on input type name and property names structure. The LOV Tag
             is returned in the response and service data.
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param Inputs: 
                         - vector of structure of LOVInfo with type name and property names vector.
             
        :return: AttachedLOVsResponse - Response structure with Map of input Index to LOV tag and
             serviceData
        """
        ...
    def GetLOVAttachments(self, ObjectStructArray: list[Teamcenter.Services.Strong.Core._2011_06.LOV.LOVAttachmentsInput]) -> Teamcenter.Services.Strong.Core._2011_06.LOV.LOVAttachmentsResponse:
        """    
             Returns valid LOV attachments for the properties of each object passed in as input.
             It may return LOV or null based on condition validations. If none of the conditions
             evaluated to be True, then no LOV attachment is returned for the property
             of an instance.
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param ObjectStructArray: 
                         LOV attachments are evaluated for each property of the structure LOVAttachmentsInut
                         based on each object in <font face="courier" height="10">objects</font> list.
             
        :return: Returns LOV attachments currently attached to properties.
        """
        ...
    def GetInitialLOVValues(self, InitialData: Teamcenter.Services.Strong.Core._2013_05.LOV.InitialLovData) -> Teamcenter.Services.Strong.Core._2013_05.LOV.LOVSearchResults:
        """    
             This operation is invoked to query the data for a property having an LOV attachment.
             The results returned from the server also take into consideration any filter string
             that is in the input.  This operation returns both LOV meta data as necessary for
             the client to render the LOV and partial LOV values list as specified.  The operation
             will return the results in the LOVSearchResults data structure. Maximum number of
             results to be returned are specified in the InitialLOVData data structure. If there
             are more results, the moreValuesExist flag in the LOVSearchResults data structure
             will be true. If the flag is true, more values can be retrieved with a call to the
             getNextLOVValues operation.
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param InitialData: 
                         Input data to get LOV results for any LOV
             
        :return: 
        """
        ...
    def GetNextLOVValues(self, LovData: Teamcenter.Services.Strong.Core._2013_05.LOV.LOVData) -> Teamcenter.Services.Strong.Core._2013_05.LOV.LOVSearchResults:
        """    
             This operation is invoked after a call to getInitialLOVValues if the moreValuesExist
             flag is true in the LOVSearchResults output returned from a call to the getInitialLOVValues
             operation. The operation will retrieve the next set of LOV values
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param LovData: 
                         Input data to get next set of LOV results for Dynamic LOV. This is returned as part
                         of the LOVSearchResults output from the call to getInitialLOVValues operation
             
        :return: LOV Search Results (LOVSearchResults instance). The LOV Search Results contains LOV
             metadata information (LOV usage, LOV style, etc.). It also contains the instance
             data (LOV values) that the client can use to render the LOV UI widget. The output
             also contains information as to whether there are more results to be processed in
             which case a user can page to get next set of values (this triggers a call to the
             subsequent getNextLOVValues operation).  Partial errors are returned in the ServiceData
             field in the LOV Search Results. Possible errors are:
        """
        ...
    def ValidateLOVValueSelections(self, LovInput: Teamcenter.Services.Strong.Core._2013_05.LOV.LOVInput, PropName: str, UidOfSelectedRows: list[str]) -> Teamcenter.Services.Strong.Core._2013_05.LOV.ValidateLOVValueSelectionsResponse:
        """    
             This operation can be invoked after selecting a value from the LOV.  Use this operation
             to do additional validation to be done on server such as validating Range value,
             getting the dependent properties values in case of interdependent LOV (resetting
             the dependendent property values), Coordinated LOVs ( populating dependent property
             values )
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param LovInput: 
                         updated LOV input with new selection
             
        :param PropName: 
                         It is the name of the Property for which LOV is being evaluated
             
        :param UidOfSelectedRows: 
                         Pass the uids from the selected rows. Every LovValueRow returned from server is designated
                         with valid UID for dynamic LOV. That is the value need to be passed to the server
                         for effective validation. For other LOVs it is empty
             
        :return: The response data indicating validity of LOV value selections and containing updated
             property values and interdependent property values
        """
        ...
    def ValidatePropertyValuesForLOVInBulk(self, Inputs: list[Teamcenter.Services.Strong.Core._2021_12.LOV.ValidatePropertyValuesForLOVInBulkInputData]) -> Teamcenter.Services.Strong.Core._2021_12.LOV.ValidatePropertyValuesForLOVInBulkResponse: ...

class ManagedRelationsRestBindingStub(ManagedRelationsService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateRelation(self, Relationinfo: list[Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.CreateManagedRelationInput]) -> Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.ManagedRelationResponse: ...
    def GetTraceReport(self, Input: Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.TraceabilityInfoInput) -> Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.TraceabilityReportOutput: ...
    def ModifyRelation(self, NewInput: list[Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.ModifyManagedRelationInput]) -> Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.ManagedRelationResponse: ...
    def GetManagedRelations(self, Inputdata: Teamcenter.Services.Strong.Core._2008_06.ManagedRelations.GetManagedRelationInput) -> Teamcenter.Services.Strong.Core._2008_06.ManagedRelations.GetManagedRelationResponse: ...

class ManagedRelationsService:
    """
    
            Contains ManagedRelations Services
            


Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ManagedRelationsService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateRelation(self, Relationinfo: list[Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.CreateManagedRelationInput]) -> Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.ManagedRelationResponse:
        """    
             This operation will create new managed relation.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Relationinfo: 
                         input information required to create managed relation
             
        :return: has any created relation and the service data.Failure will be returned with input
             index and error message in the ServiceData.
        """
        ...
    def GetTraceReport(self, Input: Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.TraceabilityInfoInput) -> Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.TraceabilityReportOutput:
        """    
             This operation will create traceability report for the selected TC object.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         information required to create report
             
        :return: has traceability tree for the given TC object and the service data. Failure will
             be returned with input index and error message in the ServiceData.
        """
        ...
    def ModifyRelation(self, NewInput: list[Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.ModifyManagedRelationInput]) -> Teamcenter.Services.Strong.Core._2007_01.ManagedRelations.ManagedRelationResponse:
        """    
             This operation will Edit the managed relation.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param NewInput: 
                         will have the modification info for given relation
             
        :return: will loadthe modified relation along with service data. Failure will be returned
             with input index and error message in the ServiceData.
        """
        ...
    def GetManagedRelations(self, Inputdata: Teamcenter.Services.Strong.Core._2008_06.ManagedRelations.GetManagedRelationInput) -> Teamcenter.Services.Strong.Core._2008_06.ManagedRelations.GetManagedRelationResponse:
        """    
             This operation will return tracelinks between primary and secondary objects.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputdata: 
                         information required to get tracelink relations
             
        :return: will return tracelink relations between primary and secondary objects and error message
             in the ServiceData.
        """
        ...

class OperationDescriptorRestBindingStub(OperationDescriptorService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetSaveAsDesc(self, TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Core._2011_06.OperationDescriptor.SaveAsDescResponse: ...
    def GetDeepCopyData(self, DeepCopyDataInput: list[Teamcenter.Services.Strong.Core._2012_02.OperationDescriptor.DeepCopyDataInput]) -> Teamcenter.Services.Strong.Core._2012_02.OperationDescriptor.GetDeepCopyDataResponse: ...

class OperationDescriptorService:
    """
    
            The OperationDescriptor service is used to
            obtain the metadata for operations like SaveAs.
            Clients can use the metadata information to construct the dialogs to be presented
            to the end user for the operations.
            

Dependencies:

            DataManagement
            


Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> OperationDescriptorService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetSaveAsDesc(self, TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Core._2011_06.OperationDescriptor.SaveAsDescResponse:
        """    
             This operation returns information required to save a business object. The SaveAsDescriptor includes the metadata information
             for the properties required when saving a business object, i.e., the property is
             mandatory, the property is visible, if value is to be copied from original object,
             etc.  The SaveAsDescriptor also includes
             the DeepCopyData which is a recursive data
             structure. The DeepCopyData contains information
             about how the secondary objects (related and referenced objects) are to be copied
             (reference, copy as object, no copy).
             

Use Cases:

Get SaveAsDescriptor for the SaveAs wizard

             Client constructs the SaveAs dialog for a Business Object using this operation. The
             information returned by this operation allows a client to construct the SaveAs dialogs
             and DeepCopy panels for user input. Once the user input is received, client can make
             subsequent invocation to the DataManagement.saveAsObjects
             operation to execute SaveAs on the object.
             

Dependencies:

             saveAsObjects
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param TargetObjects: 
                         Set of objects for which the SaveAs Descriptor is needed.
             
        :return: contains information about how the secondary objects (related and referenced objects)
             are to be copied (reference, copy as object, no copy).
        """
        ...
    def GetDeepCopyData(self, DeepCopyDataInput: list[Teamcenter.Services.Strong.Core._2012_02.OperationDescriptor.DeepCopyDataInput]) -> Teamcenter.Services.Strong.Core._2012_02.OperationDescriptor.GetDeepCopyDataResponse:
        """    
             This operation returns information required to perform SaveAs on a Business Object
             instance.
             

Use Cases:

             Client constructs the SaveAs dialog for a Business Object using this operation. The
             information returned by this operation allows a client to construct the SaveAs dialogs
             and the DeepCopy panels for user input. Once the user input is received, client can
             make subsequent invocation to the DataManagement.saveAsObjects
             operation to execute SaveAs on the object.
             

Dependencies:

             saveAsObjects
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param DeepCopyDataInput: 
                         A list of DeepCopyDataInput structures which contains an object, and operation type.
             
        :return: as a partial error
        """
        ...

class ProjectLevelSecurityRestBindingStub(ProjectLevelSecurityService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AssignOrRemoveObjects(self, AssignedOrRemovedobjects: list[Teamcenter.Services.Strong.Core._2007_09.ProjectLevelSecurity.AssignedOrRemovedObjects]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def LoadProjectDataForUser(self, User: Teamcenter.Soa.Client.Model.Strong.User, Group: Teamcenter.Soa.Client.Model.Strong.Group, Role: Teamcenter.Soa.Client.Model.Strong.Role) -> Teamcenter.Services.Strong.Core._2009_04.ProjectLevelSecurity.LoadProjectDataForUserResponse: ...
    def GetUserProjects(self, UserProjectsInfoInputs: list[Teamcenter.Services.Strong.Core._2009_10.ProjectLevelSecurity.UserProjectsInfoInput]) -> Teamcenter.Services.Strong.Core._2009_10.ProjectLevelSecurity.UserProjectsInfoResponse: ...
    def CopyProjects(self, CopyProjectsInfos: list[Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.CopyProjectsInfo]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse: ...
    def CreateProjects(self, ProjectInfos: list[Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectInformation]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse: ...
    def GetProjectTeams(self, ProjectObjs: list[Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectClientId]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectTeamsResponse: ...
    def ModifyProjects(self, ModifyProjectsInfos: list[Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ModifyProjectsInfo]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse: ...
    def GetDefaultProject(self, TcUser: Teamcenter.Soa.Client.Model.Strong.User, TcGroup: Teamcenter.Soa.Client.Model.Strong.Group, TcRole: Teamcenter.Soa.Client.Model.Strong.Role) -> Teamcenter.Services.Strong.Core._2009_04.ProjectLevelSecurity.LoadProjectDataForUserResponse: ...
    def AssignOrRemoveObjectsFromProjects(self, AssignOrRemoveInput: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ProjectAssignOrRemoveInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CopyProjects2(self, CopyProjectInfos: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.CopyProjectsInfo2]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse: ...
    def CreateProjects2(self, ProjectInfos: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ProjectInformation2]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse: ...
    def GetProjectsForAssignOrRemove(self, ProjectsInput: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ProjectsInput]) -> Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ProjectsOutputResponse: ...
    def ModifyProjects2(self, ModifyProjectsInfos: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ModifyProjectsInfo2]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse: ...
    def ChangeOwningProgram(self, ChgOwnProgramInput: list[Teamcenter.Services.Strong.Core._2018_11.ProjectLevelSecurity.ChangeOwningProgramInput2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetUserProjects2(self, UserInfoList: list[Teamcenter.Services.Strong.Core._2018_11.ProjectLevelSecurity.UserGroupRoleInfo], ActiveProjectsOnly: bool, VisibleProjectsOnly: bool, PrivilegedProjectsOnly: bool, ProgramsOnly: bool, ProgramsAndTheChildProjects: bool) -> Teamcenter.Services.Strong.Core._2018_11.ProjectLevelSecurity.UserProjectsResponse: ...
    def AddOrRemoveProjectMembers(self, Inputs: list[Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.AddOrRemoveProjectMemberInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetFirstLevelProjectTeamStructure(self, Input: Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.ProjectTeamPagedInput) -> Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.ProjectTeamPagedResponse: ...
    def GetModifiableProjects(self, StartIndex: int, PageSize: int) -> Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.UserProjectsAndPrivilegeResponse: ...
    def SetUserPrivilege(self, Inputs: list[Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.SetPrivilegeForUserInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetPrivilegeInProjects(self, Projects: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]) -> Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.ProjectPrivilegeResponse: ...
    def GetProjectTeamChildNodes(self, Project: Teamcenter.Soa.Client.Model.Strong.TC_Project, Node: Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.GroupRoleNode, Depth: int) -> Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.ChildStructureResponse: ...

class ProjectLevelSecurityService:
    """
    
            This service provides operations that are mainly used to accomplish Project Administration
            Application and Smart Navigator related use cases.  Project Administration Application
            provides the functionality to manage TC_Project objects. TC_project
            creation, modification, copying and deletion are the main operations that are supported,
            besides providing a way to manage team members and manage their membership status
            like privileged, non-privileged and team administrators. This service also provides
            operations to assign objects to projects and remove  objects from  projects.  The
            following are list of supported actions by the project level security service.
            

Creation of a TC_Project or list of TC_Project objects.
            
Modification of a TC_Project or list of TC_Project
            objects.
            
Copying of TC_Project or list of TC_Project objects.
            
Deletion of TC_Project or list of TC_Project objects.
            
Getting team members of a TC_Project or list of TC_Project
            objects.
            
Assignment of objects to a TC_Project or list of TC_Project
            objects.
            
Removal of objects from a TC_Project or list of TC_Project
            objects.
            
Enabling user or list of users to set their default projects
            
Enabling users to get configuration of Smart folders for displaying
            projects in hierarchical manner which is configured by an administrator.
            




Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ProjectLevelSecurityService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AssignOrRemoveObjects(self, AssignedOrRemovedobjects: list[Teamcenter.Services.Strong.Core._2007_09.ProjectLevelSecurity.AssignedOrRemovedObjects]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation assigns the given set of workspace objects to the given projects.
             Similarly, it removes an additional set of given workspace objects from the same
             set of given projects. If user is not privileged to assign objects to any of the
             given projects then this operation will return the error 101014 : You have insufficient
             privilege to assign object to a project. Similarly, if user is not privileged to
             remove objects from any of the given projects then this operation will return error
             101015: You have insufficient privilege to remove object from a project.  These errors
             will not terminate processing of rest of the objects.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param AssignedOrRemovedobjects: 
                         A list of AssignedOrRemovedObjects.
             
        :return: Are returned.
        """
        ...
    def LoadProjectDataForUser(self, User: Teamcenter.Soa.Client.Model.Strong.User, Group: Teamcenter.Soa.Client.Model.Strong.Group, Role: Teamcenter.Soa.Client.Model.Strong.Role) -> Teamcenter.Services.Strong.Core._2009_04.ProjectLevelSecurity.LoadProjectDataForUserResponse:
        """    
             This operation returns list of projects for a given user, group and role combination.
             If no group and role is specified it obtains all the projects for the specified user.
             If any of the arguments passed are invalid an error is returned by the operation
             added as a partial error.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param User: 
                         The <b>User</b> object.
             
        :param Group: 
                         The <b>Group</b> object in which the user belongs to.
             
        :param Role: 
                         The <b>Role</b> object in which the user belongs to.
             
        :return: This operation returns a LoadProjectDataForUserResponse structure. Any error that
             occurred while finding the projects for the given arguments is added to the sandard
             ServiceData object.
        """
        ...
    def GetUserProjects(self, UserProjectsInfoInputs: list[Teamcenter.Services.Strong.Core._2009_10.ProjectLevelSecurity.UserProjectsInfoInput]) -> Teamcenter.Services.Strong.Core._2009_10.ProjectLevelSecurity.UserProjectsInfoResponse:
        """    
             This operation returns the list of  TC_Project objects for each of  the users
             in the input structure based on the additional criteria like active projects only,
             user privileged projects only and programs only. The output for this operation is
             a UserProjectsInfoResponse structure.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param UserProjectsInfoInputs: 
                         A list of UserProjectsInfoInput structures.
             
        :return: This operation returns a UserProjectsInfoResponse structure. Any error that occurred
             while finding the projects for the given user is added to the error list in ServiceData
             object against the user object.
        """
        ...
    def CopyProjects(self, CopyProjectsInfos: list[Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.CopyProjectsInfo]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse:
        """    
             This operation copies  the given list of TC_Project objects. The operation
             also copies any information which is in contained in the project. Data such as project
             team members and any objects assigned to the source project will also be copied to
             the new project. If a project with given project ID exists in the system then this
             operation will return error 101010.  The operation will continue with copying the
             other projects.
             


Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param CopyProjectsInfos: 
                         A list of CopyProjectsInfo structures.
             
        :return: This operation returns a ProjectOpsOutput structure.
        """
        ...
    def CreateProjects(self, ProjectInfos: list[Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectInformation]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse:
        """    
             This operation creates TC_Project objects using the given input information.
             If the project with given project ID exists in the system then this operation will
             return unique id violation error 101010.  However, creation of rest of the projects
             will continue.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ProjectInfos: 
                         A list of ProjectInformation objects.
             
        :return: This operation returns a ProjectOpsOutput structure.
        """
        ...
    def GetProjectTeams(self, ProjectObjs: list[Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectClientId]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectTeamsResponse:
        """    
             This operation returns team members for the given list of TC_Project objects.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ProjectObjs: 
                         A list of ProjectClientId structures one for each of the given projects.
             
        :return: This operation returns a ProjectTeamsResponse structure. Any partial errors that
             occur while getting the team for any given project will be returned in the error
             list in ServiceData against the unique client id given as input.
        """
        ...
    def ModifyProjects(self, ModifyProjectsInfos: list[Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ModifyProjectsInfo]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse:
        """    
             This operation modifies the given list of TC_Project objects using the input
             specified. The input contains new values for all the project properties. Values for
             properties other than the project team are ignored unless the user is the Project
             Administrator.
             

             The entire Project Team, with the exception of the Project Administrator, is replaced
             with the specified team. Therefore, a Project Team Administrator must be specified.
             If the new Project Team is different than the current team, the user performing this
             operation must be either the Project Administrator or Project Team Administrator
             for the project being modified.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ModifyProjectsInfos: 
                         Vector of ModifyProjectsInfo structures.
             
        :return: 
        """
        ...
    def GetDefaultProject(self, TcUser: Teamcenter.Soa.Client.Model.Strong.User, TcGroup: Teamcenter.Soa.Client.Model.Strong.Group, TcRole: Teamcenter.Soa.Client.Model.Strong.Role) -> Teamcenter.Services.Strong.Core._2009_04.ProjectLevelSecurity.LoadProjectDataForUserResponse: ...
    def AssignOrRemoveObjectsFromProjects(self, AssignOrRemoveInput: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ProjectAssignOrRemoveInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation assigns the given set of workspace objects to the given projects.
             Similarly, it removes an additional set of given workspace objects from the same
             set of given projects. If the input contains revision rule and or variant rule these
             will be applied to the given set of objects for traversing the structure i.e. the
             project will be propagated to the objects which are obtained by applying these configurations.
             If the additional input parameters type options and depth are specified; the assign
             or remove operation will filter out additional objects based on the inputs. If user
             is not privileged to assign objects to any of the given projects then this operation
             will return the error 101014 : You have insufficient privilege to assign object to
             a project. Similarly, if user is not privileged to remove objects from any of the
             given projects then this operation will return error 101015: You have insufficient
             privilege to remove object from a project. These errors will not terminate processing
             of rest of the objects.
             

Use Cases:


Assign projects to objects specified in an input by applying the
             given revision rules and variant rules for 4GD structures.
             
Assign project to objects specified in the input by applying the
             current BOM window in classic BOM
             
Assign projects to objects specified without applying any configuration
             information
             



Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param AssignOrRemoveInput: 
                         The list of ProjectAssignOrRemoveInput structure.
             
        :return: The service data will contain nothing in case the operation is to be processed asynchronously.
             This is controlled by one of the arguments in ProjectAssignOrRemoveInput input structure.
        """
        ...
    def CopyProjects2(self, CopyProjectInfos: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.CopyProjectsInfo2]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse:
        """    
             This operation copies the given list of TC_Project objects. The operation also copies
             any information which is in contained in the project. Data such as project team members
             and any objects assigned to the source project will also be copied to the new project.
             If a project with given project ID exists in the system then this operation will
             return error 101010. The operation will continue with copying the other projects.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param CopyProjectInfos: 
                         List of CopyProjectsInfo2 structure.
             
        :return: * 101026: The Project name is already exists. It must be unique within a site.
        """
        ...
    def CreateProjects2(self, ProjectInfos: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ProjectInformation2]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse: ...
    def GetProjectsForAssignOrRemove(self, ProjectsInput: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ProjectsInput]) -> Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ProjectsOutputResponse:
        """    
             This operation retrieves the assigned projects to the input data and all available
             projects where the input user is a priveleged member. When multiple business objects
             are selected this operation retrieves the assigned projects which are in common for
             the complete input data. It also retrieves level or structure information in case
             of ActiveWorkspace Content context. In ActiveWorkspace Content context, if the selected
             object does not have further child objects then level or structure information will
             not be returned.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ProjectsInput: 
                         A list of ProjectsInput objects.
             
        :return: A list of assigned projects to the input data and all available projects where the
             input user is a priveleged member of. In the ProjectOutputsResponse, all the available
             TC_Project are returned in the availableProjects list and all the assigned projects
             to the input data are returned in the assignedProjects list, level or structure information
             in ActiveWorkspace Content context is returned in projectOptions Map.
        """
        ...
    def ModifyProjects2(self, ModifyProjectsInfos: list[Teamcenter.Services.Strong.Core._2017_05.ProjectLevelSecurity.ModifyProjectsInfo2]) -> Teamcenter.Services.Strong.Core._2012_09.ProjectLevelSecurity.ProjectOpsResponse:
        """    
             This operation modifies the given list of TC_Project objects using the input specified.
             The input contains new values for all the project properties. Values for properties
             other than the project team are ignored unless the user is the Project Administrator.
             
             The entire Project Team, with the exception of the Project Administrator, is replaced
             with the specified team. Therefore, a Project Team Administrator must be specified.
             If the new Project Team is different than the current team, the user performing this
             operation must be either the Project Administrator or Project Team Administrator
             for the project being modified.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ModifyProjectsInfos: 
                         List of ModifyProjectsInfo2 structures.
             
        :return: * 101026: The Project name is already exists. It must be unique within a site.
        """
        ...
    def ChangeOwningProgram(self, ChgOwnProgramInput: list[Teamcenter.Services.Strong.Core._2018_11.ProjectLevelSecurity.ChangeOwningProgramInput2]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation changes the owning program of the given set of objects. Owning Program
             (owning_project attribute ) is changed to the new value passed in.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ChgOwnProgramInput: 
                         The list of ChangeOwningProgramInput2 structure.
             
        :return: 
        """
        ...
    def GetUserProjects2(self, UserInfoList: list[Teamcenter.Services.Strong.Core._2018_11.ProjectLevelSecurity.UserGroupRoleInfo], ActiveProjectsOnly: bool, VisibleProjectsOnly: bool, PrivilegedProjectsOnly: bool, ProgramsOnly: bool, ProgramsAndTheChildProjects: bool) -> Teamcenter.Services.Strong.Core._2018_11.ProjectLevelSecurity.UserProjectsResponse: ...
    def AddOrRemoveProjectMembers(self, Inputs: list[Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.AddOrRemoveProjectMemberInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Adds or removes GroupMember objects or Group objects to/from the ProjectTeam
             of the given TC_Project.
             

Use Cases:

             Use Case 1: The login user selects a TC_Project and adds some Group
             or GroupMember objects to the ProjectTeam.
             
             Use Case 2: The login user selects a TC_Project and removes some Group
             or GroupMember objects from the ProjectTeam.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Inputs: 
                         A list of <b>AddOrRemoveProjectMemberInput</b> structures which consists of the <b>TC_Project</b>
                         object to add or remove, a flag that indicates to add or to remove, and lists of
                         nodes to be added or removed.
             
        :return: 
        """
        ...
    def GetFirstLevelProjectTeamStructure(self, Input: Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.ProjectTeamPagedInput) -> Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.ProjectTeamPagedResponse:
        """    
             This operations returns the paginated output of the first level nodes of the ProjectTeam
             for the given TC_Project object.
             

Use Cases:

             Select a TC_Project object to display all first level nodes in the ProjectTeam
             tree.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Input: 
                         The <b>TC_Project</b> and the pagination configuration to return <b>ProjectTeam</b>
                         first level nodes and configuration input to load <b>ProjectTeam</b> from server
                         cache.
             
        :return: members with their privilege status.
        """
        ...
    def GetModifiableProjects(self, StartIndex: int, PageSize: int) -> Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.UserProjectsAndPrivilegeResponse:
        """    
             This operation returns the TC_Project objects that the login user can modify.
             The TC_Project objects in the response are based on the pagination input.
             

Use Cases:

             A User loads all modifiable project.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param StartIndex: 
                         The start index for pagination.
             
        :param PageSize: 
                         The size of a page.
             
        :return: objects that are modifiable.
        """
        ...
    def SetUserPrivilege(self, Inputs: list[Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.SetPrivilegeForUserInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set the privilege of the given User objects in ProjectTeam of the given
             TC_Project.
             

Use Cases:

             This service allows the project team administrator to achieve the following use cases.
             

             Use Case 1: The project team administrator sets a list of User objects to
             be non-privileged in the ProjectTeam of a TC_Project.
             
             Use Case 2: The project team administrator sets a list of User objects to
             be privileged in the ProjectTeam of a TC_Project.
             
             Use Case 3: The project team administrator sets a list of User objects to
             be project team administrator in the ProjectTeam of a TC_Project.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Inputs: 
                         A list of <b>SetPrivilegeForUserInput</b> structures. The structure holds the <b>TC_Project</b>,
                         a list of <b>User</b> objects, a list of <b>Group</b> nodes, and a list of <b>GroupRole</b>
                         nodes which the privileges to be set, as well as the type of privilege to set.
             
        :return: 
        """
        ...
    def GetPrivilegeInProjects(self, Projects: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]) -> Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.ProjectPrivilegeResponse:
        """    
             This operation returns the privilege of the current user in each TC_Project
             object in the input.
             

Use Cases:

             When the login user checks the privilege in a list of TC_Project objects,
             the operation returns the privilege value of the login user of each project.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Projects: 
                         A list of <b>TC_Project</b> objects to check the current user's privilege.
             
        :return: 
        """
        ...
    def GetProjectTeamChildNodes(self, Project: Teamcenter.Soa.Client.Model.Strong.TC_Project, Node: Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.GroupRoleNode, Depth: int) -> Teamcenter.Services.Strong.Core._2020_01.ProjectLevelSecurity.ChildStructureResponse:
        """    
             The operation returns child nodes for the given Group node or a Role
             node in the ProjectTeam tree based on the given depth.
             

Use Cases:

             Expanding a Group or a Role node in a Project Team tree, the
             child nodes are returned.
             

Dependencies:

             getFirstLevelProjectTeamStructure
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Project: 
                         The <b>TC_Project</b> object which associated with the <b>ProjectTeam</b> to load
                         child nodes.
             
        :param Node: 
                         If the <i>isRemovable</i> field is true, and <i>tcRole</i> is not NULL or empty,
                         then load the direct members in the <b>ProjectTeam</b> that is associated with the
                         given <b>GroupRole</b>.
             
        :param Depth: 
                         The depth of the tree to load children.
             
        :return: .
        """
        ...

class PropDescriptorRestBindingStub(PropDescriptorService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetAttachedPropDescs(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_06.PropDescriptor.PropDescInfo]) -> Teamcenter.Services.Strong.Core._2007_06.PropDescriptor.AttachedPropDescsResponse: ...
    def GetCreateDesc(self, BusinessObjectTypeNames: list[str]) -> Teamcenter.Services.Strong.Core._2008_06.PropDescriptor.CreateDescResponse: ...
    def GetAttachedPropDescs2(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_06.PropDescriptor.PropDescInfo]) -> Teamcenter.Services.Strong.Core._2011_06.PropDescriptor.AttachedPropDescsResponse: ...

class PropDescriptorService:
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> PropDescriptorService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetAttachedPropDescs(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_06.PropDescriptor.PropDescInfo]) -> Teamcenter.Services.Strong.Core._2007_06.PropDescriptor.AttachedPropDescsResponse:
        """    
             Get the attached property descriptor based on input type name and property names
             structure.
             
        :param Inputs: 
                         - vector of structure of PropDescInfo with type name and property names vector.
             
        :return: AttachedPropDescsResponse - Response structure with Map of input typeName to PropDesc
             structure and serviceData
        """
        ...
    def GetCreateDesc(self, BusinessObjectTypeNames: list[str]) -> Teamcenter.Services.Strong.Core._2008_06.PropDescriptor.CreateDescResponse:
        """    
             The operation returns information required to create a Business Object. The Create
             Descriptor (CreateDesc object) includes the metadata information for the properties
             required when creating a business object  i.e, property is mandatory, property is
             visible, etc. The CreateDesc is a recursive data structure. The CreateDesc object
             can also reference CreateDesc on secondary objects through a reference or relation
             property. For example, the CreateDesc for Item points to CreateDesc on its
             related secondary objects, ItemRevison and Item Master. The CreateDesc
             for ItemRevision in turn points to the CreateDesc for ItemRevision Master.
             

             NOTE:  The operation will be deprecated as of Teamcenter 10. All the metadata information
             necessary for the Create operation can be retrieved from the SOA client metamodel.
             


Use Cases:

             Get Create Descriptor information for the Create wizard for an object.
             
             This call is made to populate the Create dialog for any Business Object. After obtaining
             the user input on the fields of the create dialog, a call is made to the Teamcenter::Soa::Core::_2008_06::DataManagement::createObjects
             operation to create the object
             


Dependencies:

             createObjects
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param BusinessObjectTypeNames: 
                         list of business object names for which Create Descriptor is needed.
             
        :return: 214133  No type was found for the given name
        """
        ...
    def GetAttachedPropDescs2(self, Inputs: list[Teamcenter.Services.Strong.Core._2007_06.PropDescriptor.PropDescInfo]) -> Teamcenter.Services.Strong.Core._2011_06.PropDescriptor.AttachedPropDescsResponse:
        """    
             Returns a list of Property Descriptors based on the input structure.  The Property
             Descriptors contain the Display Name, Description and other information about the
             input property.
             

Use Cases:

             This operation provides following use case for retrieving a set of Property Descriptors
             given a type name and list of property names for that type.
             

             Use Case 1:Retrieve a set of Property Descriptors for a list of property names.


Create a new PropDescInfo input structure.
             
Populate the type name and input list of property names.
             
Call getAttachedPropDescs2 with the newly created input structure.
             



Teamcenter Component:

             Core Model Property Layer - A set of capabilities/functionality (data model and behaviours)
             that form the very core of our PLM platform.  This component defines properties.
             
        :param Inputs: 
                         An input Type Name and a list of property names on the input type.  A Property Descriptor
                         is returned for each Property Name in the list.
             
        :return: 
        """
        ...

class ReservationRestBindingStub(ReservationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CancelCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def Checkin(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def Checkout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Comment: str, ChangeId: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetReservationHistory(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Core._2006_03.Reservation.GetReservationHistoryResponse: ...
    def TransferCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], UserId: Teamcenter.Soa.Client.Model.Strong.User) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def OkToCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Core._2011_06.Reservation.OkToCheckoutResponse: ...
    def BulkCancelCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def BulkCheckin(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def BulkCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Comment: str, ChangeId: str, ReservationType: int) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class ReservationService:
    """
    
            This service exposes operations related to reservations in Teamcenter. The reservation
            concept is used to gain exclusive rights to Teamcenter business objects so that multiple
            users don't modify the same object accidently. There are underlying complex rules
            for reservation governing each object based on type of objects. Many business objects
            (e.g. Dataset and ItemRevision) have their own set of validations and
            internal implementation on how reservation works. Broadly user can perform checkout operation which gives exclusive modification
            right to given business object; checkin operation
            that makes sure that checked out business object status is saved and exclusive right
            on that object is withdrawn so as other user can do checkout on this object; cancelCheckout operation that is applicable to
            certain business objects only; getReservationHistory
            operation provides history for a given business objects on how reservation operations
            were applied for a given business object.
            

            The reservation operations checkout, checkin and cancelCheckout
            operate process each input business object in a sequential manner. In situations
            where the reservation of business objects needs to be done in bulk manner, the following
            operations are available; bulkCheckout operation
            checks-out the given set of business objects in bulk; bulkCancelCheckout
            operation cancels the reservation made on business objects and restores them to the
            pre-checked-out state in bulk; bulkCheckin
            operation makes sure that checked-out business objects  status is saved and exclusive
            right on the objects is withdrawn so as other user can do checkout on this object,
            this is also done in bulk fashion.
            


Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ReservationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CancelCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation cancels a check-out for a set of previously checked-out business objects.
             The objects will be restored to the pre-check-out state. Only one user can perform
             a cancel check-out transaction on the object if the user has enough privilege on
             the object.  This action may be applied to remote checked out objects, and will cancel
             the check-out and records the cancel check-out transaction event. Cancel checkout
             is not supported for some of the business objects for e.g. - Item, BOMView,BOMViewRevision,
             Schedule.
             

Dependencies:

             checkout
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of objects to be canceled for previously check-out.
             
        :return: 
        """
        ...
    def Checkin(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation checks-in a set of previously checked-out business objects. This operation
             takes care of all complex business logic involved to check-in passed in business
             objects.  Each input object is verified that it is locally owned, site owned, and
             not transferred to another user after the checkout was performed. This operation
             validates precondition defined per type in COTS object and site customization and
             performs basic check-in. Dataset, ItemRevision and many other business
             object types have their own business logic for check-in. This operation calls underlying
             checkin method of those individual objects.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         Set of previously checked-out valid business objects. (e.g. <b>Dataset</b>, <b>Item</b>,
                         <b>ItemRevision</b> )
             
        :return: 
        """
        ...
    def Checkout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Comment: str, ChangeId: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation checks  out a set of business objects with given comment and change
             identifier. Only one user can perform a check-out transaction on the object. The
             user must have sufficient  privilege on the object or the check out will fail. This
             operation allows for remote check-out and records the check-out transaction event.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of business objects to be checked out.
             
        :param Comment: 
                         A comment describing the reason for the check-out.  An empty string is allowed.
             
        :param ChangeId: 
                         A string value to identify the change.  Empty string allowed.
             
        :return: 
        """
        ...
    def GetReservationHistory(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Core._2006_03.Reservation.GetReservationHistoryResponse:
        """    
             This operation gets the reservation history for a set of business objects, such as
             Dataset, Item, ItemRevision and many other business object types.
             An object which has never been checked out will have a valid reservation history
             with an empty sequence of events.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of business objects to query for reservation history.
             
        :return: 
        """
        ...
    def TransferCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], UserId: Teamcenter.Soa.Client.Model.Strong.User) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation transfers the previously checked-out business objects to the user
             given from input. This operation takes care of all complex business logic involved
             in transfer checked-out based on passed in objects. Each input object is verified
             that it is valid for transferring its checkout.
             
             This operation validates precondition defined per type in COTS object and site customization
             before performing transfer checked-out objects to the target user. Dataset,
             ItemRevision and many other business object types have their own business
             logic for transfer check-out. This operation calls underlying transfer checkout method
             of those individual objects.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of the previously checked-out Teamcenter objects (e.g. <b>Dataset</b>, <b>Item</b>,
                         <b>ItemRevision</b> ) to transfer the checkout.
             
        :param UserId: 
                         The Teamcenter user id to who checked-out has to be transferred to.
             
        :return: 
        """
        ...
    def OkToCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Core._2011_06.Reservation.OkToCheckoutResponse:
        """    
             This operation determines whether or not the input objects may be checked out given
             the type of object, access rules, and current checkout state of the object.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         The list of objects which should be validated for Checkout.
             
        :return: The possible partial error 32053 is returned if the object's type is not supported
             by the check out facility.
        """
        ...
    def BulkCancelCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation cancels a check-out for a set of previously checked-out business objects
             in bulk. The objects will be restored to the pre-check-out state. Only one user can
             perform a cancel check-out transaction on the object if the user has enough privilege
             on the object. This action may be applied to remote checked-out objects, and will
             cancel the check-out and records the cancel check-out transaction event. Cancel checkout
             is not supported for some of the business objects for e.g. - Item, BOMView,BOMViewRevision,
             Schedule.
             

Dependencies:

             bulkCheckout, checkout
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of objects which are in the checked-out state.(e.g. Dataset, Item, ItemRevision
                         )
             
        :return: 
        """
        ...
    def BulkCheckin(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation checks-in a set of previously checked-out business objects in bulk.
             This operation takes care of all complex business logic involved to check-in passed
             in business objects. Each input object is verified that it is locally owned, site
             owned, and not transferred to another user after the checkout was performed. This
             operation validates precondition defined per type in COTS object and site customization
             and performs basic check-in. Dataset, ItemRevision and many other business object
             types have their own business logic for check-in. This operation calls underlying
             checkin method of those individual objects.
             

             Note: If the business object ItemRevision is checked out using reservation type "RES_RESERVE_BULK_WITH_DELAY_DEEP_COPY"
             and if the given object is not modified after it was checked out using this reservation
             type then the checkin opetation performed on this object will not increase the sequence
             number of the ItemRevision business object
             


Dependencies:

             bulkCheckout, checkout
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of objects which are in the checked-out state.
             
        :return: 
        """
        ...
    def BulkCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Comment: str, ChangeId: str, ReservationType: int) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation checks out a set of business objects with given comment and, change
             identifier in bulk fashion. Only one user can perform a check-out transaction on
             the object. The user must have sufficient privilege on the object or the checkout
             will fail. This operation allows for remote check-out and records the check-out transaction
             event. In the case where the reservationType is RES_RESERVE_BULK_WITH_DELAY_DEEP_COPY,
             this operation checks out business objects without creating the backup copy of the
             reserved objects. The backup copy will be created on demand when the reserved object
             is modified. This operation is faster than the checkout operation.
             

Use Cases:

             The object can be reserved to gain exclusive rights so that no other user can modify
             it while the reserver is modifying the given object.
             

Teamcenter Component:

             Reservation - A reservation is created by a user by checking out the master copy
             at the owning site.  A reservation prevents other users from checking out the master
             copy; and from transferring site ownership by effectively placing a lock on the master.
             
        :param Objects: 
                         A list of business objects to be checked out.
             
        :param Comment: 
                         A comment describing the reason for the check-out. An empty string is allowed.
             
        :param ChangeId: 
                         The ID of the change. Empty string allowed.
             
        :param ReservationType: 
<ul>
<li type="disc">RES_EXCLUSIVE_RESERVE for checking out business objects  and create
                         with the backup copy of the reserved objects to  maintaining its their states before
                         the chekcout
                         </li>
<li type="disc">RES_RESERVE_BULK_WITH_DELAY_DEEP_COPY for bulk checking out business
                         objects without creating the backup copy of the reserved objects. maintaining its
                         state before the chekcout. The backup copy will be created on demand when the reserved
                         object is modified.  This reservation type is of checkout operation is faster than
                         the reservation type : one with "RES_EXCLUSIVE_RESERVE".
                         </li>
</ul>

        :return: 
        """
        ...

class StructureManagementRestBindingStub(StructureManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateInStructureAssociations(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.StructureManagement.InStructureAssociationInfo]) -> Teamcenter.Services.Strong.Core._2008_06.StructureManagement.CreateInStructureAssociationResponse: ...
    def GetPrimariesOfInStructureAssociation(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.StructureManagement.GetPrimariesOfInStructureAssociationInfo]) -> Teamcenter.Services.Strong.Core._2008_06.StructureManagement.GetPrimariesOfInStructureAssociationResponse: ...
    def GetSecondariesOfInStructureAssociation(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.StructureManagement.GetSecondariesOfInStructureAssociationInfo]) -> Teamcenter.Services.Strong.Core._2008_06.StructureManagement.GetSecondariesOfInStructureAssociationResponse: ...
    def RemoveInStructureAssociations(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.StructureManagement.RemoveInStructureAssociationsInfo]) -> Teamcenter.Services.Strong.Core._2008_06.StructureManagement.RemoveInStructureAssociationsResponse: ...

class StructureManagementService:
    """
    
            StructureManagement services allows user to create, delete or validate associations
            between BOMLines, get primary or secondary objects associated with a BOMLine.
            

Dependencies:

            StructureManagement
            


Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateInStructureAssociations(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.StructureManagement.InStructureAssociationInfo]) -> Teamcenter.Services.Strong.Core._2008_06.StructureManagement.CreateInStructureAssociationResponse:
        """    
             This operation creates the specified association between primary and secondary BOMLine
             objects in a structure.  As the name indicates, these associations are created in
             a specific context and are applicable only in that context. The context is specified
             as an additional input in the input structure, by the caller. Some examples of these
             associations are: the ConnectTo, ImplementedBy, RealizedBy, SignalToSource, SignalToTarget,
             SignalToTransmitter, ProcessVariable, RedundantSignal relations that are provided
             in Teamcenter [see Use case]. This operation takes a vector of InStructureAssociationInfo
             as input. The input structures contain information on the BOMLine objects
             that need to be associated, what context they need to be associated in and the type
             of association. Note that the associations created are only valid in the context
             specified.
             
             If input primary is Signal object's BOMLine, then for associating signal BOMLine
             to secondary as source or target, the association type is optional, and if input
             association type is empty, the secondary BOMLine objects GDE object direction
             attirbute value will be used for associating signal BOMLine to secondary as
             source or target.
             

Use Cases:

             Use this operation to create an association between BOMLine objects. This is a generic
             Teamcenter service to create various types of associations. The type of the association
             that gets created depends on the Association Type specified in the input structure.
             
             The ConnectTo  functionality establishes an association between 1 or more BOMLine
             objects and a Connection BOMLine. The association signifies that the BOMLine objects
             are connected to the Connection BOMLine in a certain context.  Outside of that context
             the association is not valid. The caller of this operation provides as input, one
             or more BOMLine objects, and a Connection BOMLine. The associationType should be
             set in the input structure to ConnectTo and specifies a BOMLine that will act as
             a context line within which the association is valid.
             

Dependencies:

             createBOMWindows
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a vector of InStructureAssociationInfo structure. Each element shall consist
                         of a primary <b>BOMLine</b>, the secondary <b>BOMLine</b> objects to be associated
                         with the primary, the line in whose context the association takes place and the association
                         type.
             
        :return: 
        """
        ...
    def GetPrimariesOfInStructureAssociation(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.StructureManagement.GetPrimariesOfInStructureAssociationInfo]) -> Teamcenter.Services.Strong.Core._2008_06.StructureManagement.GetPrimariesOfInStructureAssociationResponse:
        """    
             This operation gets the primary BOMLines like PSConnection, Signal
             of an association given the secondary object and association type.  Examples of these
             associations are: ConnectTo, ImplementedBy, RealizedBy, RoutedBy, FixingToSegment,
             DeviceToConnector, SignalToTransmitter, SignalToSource, SignalToTarget, ProcessVariable,
             RedundantSignal. This operation takes a vector of GetPrimariesOfInStructureAssociationInfo
             as input.
             

Use Cases:

             A typical usecase for this operation is where callers would like to obtain primary
             BOMLine objects by providing the association type and the corresponding secondary
             BOMLine associated.  In a SignalToTransmitter association for example,
             if the transmitting BOMLine  is provided, callers can get the corresponding
             Signal which is the primary BOMLine in this relation.
             

Dependencies:

             createBOMWindows
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a vector of <i>GetPrimariesOfInStructureAssociationInfo</i> structure. Each
                         element consists of a secondary <b>BOMLine</b>, the context <b>BOMLine</b> of the
                         association and the association type.
             
        :return: 
        """
        ...
    def GetSecondariesOfInStructureAssociation(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.StructureManagement.GetSecondariesOfInStructureAssociationInfo]) -> Teamcenter.Services.Strong.Core._2008_06.StructureManagement.GetSecondariesOfInStructureAssociationResponse:
        """    
             Given the primary object and association type, returns the secondary BOMLine
             business objects of in structure associations. These associations can be ConnectTo,
             ImplementedBy, RealizedBy, RoutedBy, FixingToSegment, DeviceToConnector, SignalToSource,
             SignalToTarget, SignalToTransmitter, ProcessVariable or RedundantSignal.
             It takes a vector of GetSecondariesOfInStructureAssociationInfo as input.
             

Use Cases:

             Users shall use this operation to get secondary BOMLine business objects for
             a given association type and the primary object associated with it.
             
             For instance, this operation could be used to get all the secondary GDE lines connected
             to a PSConnection by passing the association type as ConnectTo. Similarly,
             it can be used to get the connector lines connected to the Device Line by
             passing appropriate primary Device and the association type as DeviceToConnector.
             

Dependencies:

             createBOMWindows
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a vector of <i>GetSecondariesOfInStructureAssociationInfo</i> structure.
                         Each element shall consist of a primary <b>BOMLine</b>, the parent line in whose
                         context the association takes place and the association type.
             
        :return: 
        """
        ...
    def RemoveInStructureAssociations(self, Inputs: list[Teamcenter.Services.Strong.Core._2008_06.StructureManagement.RemoveInStructureAssociationsInfo]) -> Teamcenter.Services.Strong.Core._2008_06.StructureManagement.RemoveInStructureAssociationsResponse:
        """    
             Given the primary BOMLine, the association type, and the secondary BOMLines
             this operation removes the instructure associations between the BOMLines.
             These associations can be ConnectTo, ImplementedBy, RealizedBy, RoutedBy, FixingToSegment,
             DeviceToConnector, SignalToSource, SignalToTarget, SignalToTransmitter, ProcessVariable
             or RedundantSignal. The operation takes a vector of RemoveInStructureAssociationsInfo
             as Input.
             
             If input primary is Signal object's BOMLine, then for associatiion type input
             between signal and secondary as source or target can be optional, and if input association
             type is empty, then the secondary BOMLine association to input primary Signal
             BOMLine  as source and target will be removed.
             

Use Cases:

             Developers shall use this operation when an association has to be removed between
             the BOMLines. This is a generic Teamcenter service to remove various types
             of associations.
             
             In the case of ConnectTo, if the secondary BOMLines are passed as null
             then all the secondary associations with the primary BOMLine shall be removed.
             


Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a vector of <i>RemoveInStructureAssociationsInfo</i> structure. Each element
                         shall consist of a primary <b>BOMLine</b>, the secondary <b>BOMLines</b> to be removed,
                         the parent line in whose context the association takes place and the association
                         type.
             
        :return: 
        """
        ...

class FileManagementRestBindingStub(FileManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CommitDatasetFiles(self, CommitInput: list[Teamcenter.Services.Strong.Core._2006_03.FileManagement.CommitDatasetFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetDatasetWriteTickets(self, Inputs: list[Teamcenter.Services.Strong.Core._2006_03.FileManagement.GetDatasetWriteTicketsInputData]) -> Teamcenter.Services.Strong.Core._2006_03.FileManagement.GetDatasetWriteTicketsResponse: ...
    def GetFileReadTickets(self, Files: list[Teamcenter.Soa.Client.Model.Strong.ImanFile]) -> Teamcenter.Services.Strong.Core._2006_03.FileManagement.FileTicketsResponse: ...
    def GetTransientFileTicketsForUpload(self, TransientFileInfos: list[Teamcenter.Services.Strong.Core._2007_01.FileManagement.TransientFileInfo]) -> Teamcenter.Services.Strong.Core._2007_01.FileManagement.GetTransientFileTicketsResponse: ...
    def GetDigestInfoForDatasets(self, Datasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]) -> Teamcenter.Services.Strong.Core._2015_10.FileManagement.DatasetDigestInfoResponse: ...
    def GetDigestInfoForFiles(self, Files: list[Teamcenter.Soa.Client.Model.Strong.ImanFile]) -> Teamcenter.Services.Strong.Core._2015_10.FileManagement.FileDigestInfoResponse: ...
    def CommitDatasetFilesInBulk(self, CommitInput: list[Teamcenter.Services.Strong.Core._2006_03.FileManagement.CommitDatasetFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReplaceFiles(self, Inputs: list[Teamcenter.Services.Strong.Core._2017_05.FileManagement.ReplaceFileInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class FileManagementService:
    """
    
            This service implements operations which support the File Management System (FMS).
            This service contains operations that run in the Teamcenter Server context to supply
            business logic functionality which controls the flow of user data.  The data being
            controlled by this service exists within files, as represented by ImanFile
            objects within the Teamcenter Product Lifecycle Management (PLM) system.
            
            This service provides the following file management use cases:
            

Manage PLM file downloads (reading a file from a Teamcenter volume).
            
Manage PLM file uploads (adding a file to a Teamcenter volume).
            


            This service interoperates with the File Management System (FMS), and is intended
            to be used with FMS client APIs.  The set of FMS client APIs includes various forms
            and implementations of the FMS Client Cache (FCC) Client Proxy and the FMS Server
            Cache (FSC) Client Proxy.
            
            Please see the Teamcenter glossary for the definitions of any terms with which you
            may not be familiar.  Please see the Teamcenter documentation for summary information
            regarding the File Management System (FMS), or any other parts of the Teamcenter
            product with which you are not familiar.
            
            NOTE: The File Management System (FMS) APIs are unpublished and proprietary intellectual
            property of Siemens Product Lifecycle Management (Siemens PLM).  The few published
            portions of this service, which were created prior to the advent of unpublished Teamcenter
            service operations, are not particularly useful to clients, for whom access to the
            File Management System (FMS) APIs is unavailable.  This entire service is therefore
            considered unpublished and proprietary intellectual property of Siemens Product Lifecycle
            Management (Siemens PLM).
            
            It is seldom necessary for a client to invoke the operations of this service directly.
            The com.teamcenter.soa.client.FileManagementUtility class provides a simplified
            interface for most use cases that require the use of this service.  The FileManagementUtility
            class coordinates the task sequencing and error management between the FileManagementService
            and the appropriate FMS client API, as described in this document.
            
            FileManagementUtility supports both FCC client and FSC server interfaces.  Please
            be sure to construct the form of FileManagementUtility instance appropriate for your
            context.  The FSC interface should be used by all web tier services or applications.
            The default, or FCC, form should only be used by client applications.
            
            FileManagementUtility is a heavyweight, but reusable, object.  Please cache and reuse
            the FileManagementUtility object within your application, whenever possible.
            


Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> FileManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CommitDatasetFiles(self, CommitInput: list[Teamcenter.Services.Strong.Core._2006_03.FileManagement.CommitDatasetFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation supports the upload (addition) of files to a Teamcenter volume.  The
             mechanism for a client application adding files to a Teamcenter volume contains several
             steps.  This mechanism is implemented in the com.teamcenter.soa.client.FileManagementUtility
             class, which provides this functionality to clients in a consistent, reusable package.
             The com.teamcenter.soa.client.FileManagementUtility
             class invokes this operation after successfully uploading a file to a Teamcenter
             volume.
             
             This operation was unintentionally published.  It is supported only for internal
             Siemens PLM purposes.  Customers should not invoke this operation.
             

Use Cases:

             This operation supports the upload (addition) of files representing named references
             of a Dataset object to a Teamcenter volume.
             

Dependencies:

             getDatasetWriteTickets
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param CommitInput: 
                         The vector of <font face="courier" height="10">CommitDatasetFileInfo</font> structures
                         returned in the commitInfo element of the <font face="courier" height="10">GetDatasetWriteTicketsResponse</font>
                         structure returned by the <font face="courier" height="10">FileManagementService::getDatasetWriteTickets</font>
                         operation.  In the event of partial upload success, the <font face="courier" height="10">com.teamcenter.soa.client.FileManagementUtility</font>
                         class removes all of the <font face="courier" height="10">CommitDatasetFileInfo</font>
                         structures representing the files that failed to upload to the Teamcenter volume
                         from this vector, before invoking the <font face="courier" height="10">FileManagementService::commitDatasetFiles</font>
                         operation.
             
        :return: object.  This Teamcenter Services structure is used to return status of the operation.
             Any errors that occurred during the operation are returned here.
        """
        ...
    def GetDatasetWriteTickets(self, Inputs: list[Teamcenter.Services.Strong.Core._2006_03.FileManagement.GetDatasetWriteTicketsInputData]) -> Teamcenter.Services.Strong.Core._2006_03.FileManagement.GetDatasetWriteTicketsResponse:
        """    
             This operation obtains File Management System (FMS) write tickets and file storage
             information for a set of supplied Dataset objects. The write tickets are used
             to transfer files from a local storage to Teamcenter volume, and the file storage
             information can be used to commit Dataset objects referencing those transferred
             files.
             
             The caller will provide a vector of GetDatasetWriteTicketsInputData
             objects that contains one or more Dataset objects and information about each
             associated file (e.g., filename, text/binary flag, etc.).  Upon return, the GetDatasetWriteTicketsResponse object will contain
             FMS write tickets that can be used to upload the file to the Teamcenter volume, and
             Dataset information that can be used to commit the changes to the database
             by using the FileManagementService commitDatasetFiles() operation.
             
             This operation supports the upload (addition) of files representing named references
             of a Dataset object to a Teamcenter volume.
             
             This operation was unintentionally published.  It is supported only for internal
             Siemens PLM purposes.  Customers should not invoke this operation.
             

Use Cases:

             This operation supports the upload (addition) of files representing named references
             of a Dataset object to a Teamcenter volume.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Inputs: 
                         A vector of <font face="courier" height="10">GetDatasetWriteTicketsInputData</font>
                         structures which holds the <b>Dataset</b> objects and related <font face="courier" height="10">DatasetFileTicketInfo</font>.  The calling client must construct this
                         input.
             
        :return: ().
        """
        ...
    def GetFileReadTickets(self, Files: list[Teamcenter.Soa.Client.Model.Strong.ImanFile]) -> Teamcenter.Services.Strong.Core._2006_03.FileManagement.FileTicketsResponse:
        """    
             This operation obtains File Management System (FMS) read tickets for a set of supplied
             
ImanFile objects.  The supplied tickets are used to transfer files from a
             Teamcenter volume
             
             to local storage.  The files input parameter
             contains a list of the ImanFile objects to be read
             
             from the Teamcenter volume and transferred to local storage.
             
             FMS requires tickets for all file transfers to and from Teamcenter volumes.  An FMS
             read ticket is
             
             required to obtain a file from a Teamcenter volume, while an FMS write ticket is
             needed to place a file in the Teamcenter volume.  It is often times more expedient
             to request several tickets at one time, especially if it is known ahead of time that
             many files will need to be moved.  For this reason, the caller may supply multiple
             ImanFile objects, for which FMS tickets are desired, in the input vector.
             
             This operation was unintentionally published.  It is supported only for internal
             Siemens PLM purposes.  Customers should not invoke this operation.
             

Use Cases:

             This operation supports the download of data files represented by ImanFile
             objects from a Teamcenter volume into a local client environment.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Files: 

        :return: , string) of read tickets.
        """
        ...
    def GetTransientFileTicketsForUpload(self, TransientFileInfos: list[Teamcenter.Services.Strong.Core._2007_01.FileManagement.TransientFileInfo]) -> Teamcenter.Services.Strong.Core._2007_01.FileManagement.GetTransientFileTicketsResponse:
        """    
             This operation gets the tickets for the desired files to be uploaded to the transient
             volume. These tickets can be used to upload corresponding files via FileManagementUtility::putFileViaTicket. The TransientFileInfo contains the basic information for a file to
             be uploaded such as file name, file type and whether the file should be deleted after
             reading.
             

Use Cases:

             This operation supports the uploading of files into the FMS transient volume.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param TransientFileInfos: 
                         List containing the details of the files for which the tickets are requested.
             
        :return: structure,
             which will contain the file tickets and status of the operation.
        """
        ...
    def GetDigestInfoForDatasets(self, Datasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]) -> Teamcenter.Services.Strong.Core._2015_10.FileManagement.DatasetDigestInfoResponse:
        """    
             Gets the file digest information for the ImanFile objects contained in the
             Dataset objects. These digests can be used by clients to check for file integrity.
             Clients must use the same digest algorithm (as returned by this operation) to compute
             the digest on their end and compare with the digest returned by this operation.
             
             The Teamcenter File Management System (FMS) computes and stores the file digests
             on the volume if the content verification feature is turned on.
             
             This operation returns digests for binary files only.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Datasets: 
                         the <b>Dataset</b> objects for which the digest information is to be obtained for
                         each of the <b>ImanFile</b> objects in them.
             
        :return: 
        """
        ...
    def GetDigestInfoForFiles(self, Files: list[Teamcenter.Soa.Client.Model.Strong.ImanFile]) -> Teamcenter.Services.Strong.Core._2015_10.FileManagement.FileDigestInfoResponse:
        """    
             Gets the file digest information for all the ImanFile objects specified using
             files. These digests can be used by clients to check for file integrity. Clients
             must use the same digest algorithm (as returned by this operation) to compute the
             digest on their end and compare with the digest returned by this operation.
             
             The Teamcenter File Management System (FMS) computes and stores the file digests
             on the volume if the content verification feature is turned on.
             
             This operation returns digests for binary files only.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Files: 
                         The <b>ImanFile</b> objects for which the digest information is to be obtained.
             
        :return: 
        """
        ...
    def CommitDatasetFilesInBulk(self, CommitInput: list[Teamcenter.Services.Strong.Core._2006_03.FileManagement.CommitDatasetFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ReplaceFiles(self, Inputs: list[Teamcenter.Services.Strong.Core._2017_05.FileManagement.ReplaceFileInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation replaces an existing volume file with a new file that has already
             been uploaded to a transient volume.  It uploads the file from the transient volume
             to the regular Teamcenter volume.  The original volume file is replaced with the
             new file, and the ImanFile references the new file.  Note that there is no
             new ImanFile object created.  This operation includes the ability to change
             the original file name or retain its existing value.  The file type on the ImanFile
             object is updated to match the value from the input write tickets.  The tickets for
             the upload to the transient volume can be obtained by calling getTransientFileTicketsForUpload.
             

             This operation is used for replacing an existing file in a volume when the original
             file content is to be replaced with a newly encrypted file.
             

Use Cases:

             There are very specific cases where this operation should be used. One use case is
             where encryption software needs to replace the contents of the original file with
             the encrypted contents.
             

Dependencies:

             getTransientFileTicketsForUpload
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Inputs: 
                         The input to this operation includes a list of write tickets used to upload the new
                         file to the transient volume.  It also includes a flag to indicate if the original
                         file name on the <b>ImanFile</b> should be updated to match the new file.  This new
                         file replaces the existing file referenced by the <b>ImanFile</b> object.
             
        :return: 
        """
        ...

class SessionRestBindingStub(SessionService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def GetPreferences(self, PrefScope: str, PrefNames: list[str]) -> Teamcenter.Services.Strong.Core._2006_03.Session.PreferencesResponse: ...
    @typing.overload
    def GetPreferences(self, RequestedPrefs: list[Teamcenter.Services.Strong.Core._2007_01.Session.ScopedPreferenceNames]) -> Teamcenter.Services.Strong.Core._2007_01.Session.MultiPreferencesResponse: ...
    def SetPreferences(self, Settings: list[Teamcenter.Services.Strong.Core._2006_03.Session.PrefSetting]) -> Teamcenter.Services.Strong.Core._2006_03.Session.PreferencesResponse: ...
    def GetAvailableServices(self) -> Teamcenter.Services.Strong.Core._2006_03.Session.GetAvailableServicesResponse: ...
    def GetGroupMembership(self) -> Teamcenter.Services.Strong.Core._2006_03.Session.GetGroupMembershipResponse: ...
    def GetSessionGroupMember(self) -> Teamcenter.Services.Strong.Core._2006_03.Session.GetSessionGroupMemberResponse: ...
    @typing.overload
    def Login(self, Username: str, Password: str, Group: str, Role: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    @typing.overload
    def Login(self, Username: str, Password: str, Group: str, Role: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    @typing.overload
    def Login(self, Credentials: Teamcenter.Services.Strong.Core._2011_06.Session.Credentials) -> Teamcenter.Services.Strong.Core._2011_06.Session.LoginResponse: ...
    @typing.overload
    def LoginSSO(self, Username: str, SsoCredentials: str, Group: str, Role: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    @typing.overload
    def LoginSSO(self, Username: str, SsoCredentials: str, Group: str, Role: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    @typing.overload
    def LoginSSO(self, Credentials: Teamcenter.Services.Strong.Core._2011_06.Session.Credentials) -> Teamcenter.Services.Strong.Core._2011_06.Session.LoginResponse: ...
    def Logout(self) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetSessionGroupMember(self, GroupMember: Teamcenter.Soa.Client.Model.Strong.GroupMember) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetTCSessionInfo(self) -> Teamcenter.Services.Strong.Core._2007_01.Session.GetTCSessionInfoResponse: ...
    @typing.overload
    def SetObjectPropertyPolicy(self, PolicyName: str) -> bool: ...
    @typing.overload
    def SetObjectPropertyPolicy(self, Policy: Teamcenter.Soa.Common.ObjectPropertyPolicy) -> str: ...
    @typing.overload
    def SetObjectPropertyPolicy(self, PolicyName: str, UseRefCounting: bool) -> Teamcenter.Services.Strong.Core._2012_02.Session.SetPolicyResponse: ...
    def RefreshPOMCachePerRequest(self, Refresh: bool) -> bool: ...
    def SetUserSessionState(self, Pairs: list[Teamcenter.Services.Strong.Core._2007_12.Session.StateNameValue]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetAndEvaluateIdDisplayRule(self, IdentifiableObjects: list[Teamcenter.Soa.Client.Model.ModelObject], DisplayRule: Teamcenter.Soa.Client.Model.Strong.IdDispRule, SetRuleAsCurrentInDB: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def Connect(self, FeatureKey: str, Action: str) -> Teamcenter.Services.Strong.Core._2008_03.Session.ConnectResponse: ...
    def GetFavorites(self) -> Teamcenter.Services.Strong.Core._2008_03.Session.FavoritesResponse: ...
    def SetFavorites(self, Input: Teamcenter.Services.Strong.Core._2008_03.Session.FavoritesInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetDisplayStrings(self, Info: list[str]) -> Teamcenter.Services.Strong.Core._2008_06.Session.GetDisplayStringsResponse: ...
    def StartOperation(self) -> str: ...
    def StopOperation(self, OpId: str) -> bool: ...
    def GetPreferences2(self, PreferenceNames: list[Teamcenter.Services.Strong.Core._2007_01.Session.ScopedPreferenceNames]) -> Teamcenter.Services.Strong.Core._2010_04.Session.MultiPreferenceResponse2: ...
    def GetShortcuts(self, ShortcutInputs: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Core._2010_04.Session.GetShortcutsResponse: ...
    def GetClientCacheData(self, Features: list[str]) -> Teamcenter.Services.Strong.Core._2011_06.Session.ClientCacheInfo: ...
    def GetTypeDescriptions(self, TypeNames: list[str]) -> Teamcenter.Schemas.Soa._2011_06.Metamodel.TypeSchema: ...
    def UpdateObjectPropertyPolicy(self, PolicyID: str, AddProperties: list[Teamcenter.Soa.Common.PolicyType], RemoveProperties: list[Teamcenter.Soa.Common.PolicyType]) -> str: ...
    def RegisterState(self, Level: str) -> Teamcenter.Services.Strong.Core._2012_02.Session.RegisterIndex: ...
    def UnregisterState(self, Index: int) -> bool: ...
    def GetTypeDescriptions2(self, TypeNames: list[str], Options: System.Collections.Hashtable) -> Teamcenter.Schemas.Soa._2011_06.Metamodel.TypeSchema: ...
    def SetUserSessionStateAndUpdateDefaults(self, Pairs: list[Teamcenter.Services.Strong.Core._2007_12.Session.StateNameValue]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SponsoredLogin(self, SponsoringUser: str, Password: str, SponsoredUser: str, SponsoredGroup: str, SponsoredRole: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    def SponsoredLoginSSO(self, SponsoringUser: str, SsoCredentials: str, SponsoredUser: str, SponsoredGroup: str, SponsoredRole: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    def LicenseAdmin(self, LicAdminInput: list[Teamcenter.Services.Strong.Core._2019_06.Session.LicAdminInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def AddObjectPropertyPolicies(self, ClientPolicies: list[Teamcenter.Soa.Common.ObjectPropertyPolicy], NamedPolicies: list[str]) -> Teamcenter.Services.Strong.Core._2021_12.Session.AddPoliciesResponse: ...
    def TcServerSleep(self, Seconds: int) -> str: ...

class SessionService:
    """
    
            The Session service exposes operations used
            to manage a client session with the Teamcenter server. All client sessions must start
            with a login operation and end with a logout operation. Throughout the client session,
            the Session service may be used to change
            state such as Group, Role, and object property policy.
            


Library Reference:

TcSoaCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SessionService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def GetPreferences(self, PrefScope: str, PrefNames: list[str]) -> Teamcenter.Services.Strong.Core._2006_03.Session.PreferencesResponse: ...
    @typing.overload
    def GetPreferences(self, RequestedPrefs: list[Teamcenter.Services.Strong.Core._2007_01.Session.ScopedPreferenceNames]) -> Teamcenter.Services.Strong.Core._2007_01.Session.MultiPreferencesResponse: ...
    def SetPreferences(self, Settings: list[Teamcenter.Services.Strong.Core._2006_03.Session.PrefSetting]) -> Teamcenter.Services.Strong.Core._2006_03.Session.PreferencesResponse:
        """    
             Set preference values.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param Settings: 
                         vector of PrefSetting structures, which specify the scope, name, and value(s) for
                         each of the preferences to be set.
             
        :return: A PreferencesResponse structure. The preferences element returns the new values of
             preferences which were successfully set. The serviceData element returns any partial
             errors encountered while setting specific preference values.
        """
        ...
    def GetAvailableServices(self) -> Teamcenter.Services.Strong.Core._2006_03.Session.GetAvailableServicesResponse:
        """    
             This operation returns a list of services and service operations that this Teamcenter
             server instance supports. This is useful for client applications that expose different
             functionality based on the version of the Teamcenter server it is connecting to.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def GetGroupMembership(self) -> Teamcenter.Services.Strong.Core._2006_03.Session.GetGroupMembershipResponse:
        """    
             Get the valid groups and roles for the current user.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def GetSessionGroupMember(self) -> Teamcenter.Services.Strong.Core._2006_03.Session.GetSessionGroupMemberResponse:
        """    
             Get the Group and Role for the current session. The group and role
             are set at login, either to default values or as specified by the input arguments
             to the login operation. The group and role can be changed at any time throughout
             the session through the setSessionGroupMember
             or setUserSessionState operations.
             

Dependencies:

             setSessionGroupMember
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    @typing.overload
    def Login(self, Username: str, Password: str, Group: str, Role: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    @typing.overload
    def Login(self, Username: str, Password: str, Group: str, Role: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    @typing.overload
    def Login(self, Credentials: Teamcenter.Services.Strong.Core._2011_06.Session.Credentials) -> Teamcenter.Services.Strong.Core._2011_06.Session.LoginResponse: ...
    @typing.overload
    def LoginSSO(self, Username: str, SsoCredentials: str, Group: str, Role: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    @typing.overload
    def LoginSSO(self, Username: str, SsoCredentials: str, Group: str, Role: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse: ...
    @typing.overload
    def LoginSSO(self, Credentials: Teamcenter.Services.Strong.Core._2011_06.Session.Credentials) -> Teamcenter.Services.Strong.Core._2011_06.Session.LoginResponse: ...
    def Logout(self) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Logout and terminate the Teamcenter session. If the Teamcenter server is being shared
             with multiple client applications, it will not be terminated until each client has
             issued the logout.
             


Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def SetSessionGroupMember(self, GroupMember: Teamcenter.Soa.Client.Model.Strong.GroupMember) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set the Group and Role for the current session. The group and role
             are set at login, either to default values or as specified by the input arguments
             to the login operation. The group and role can be changed at any time throughout
             the session through this operation or the setUserSessionState
             operations. The getSessionGroupMember will
             return the current group and roll.
             

Dependencies:

             getSessionGroupMember
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param GroupMember: 
                         The desired <b>GroupMember</b> for the current session.  The <b>GroupMember</b> defines
                         the <b>Group</b> and <b>Role</b> for the session.
             
        :return: property
             values returned in addition to any properties defined in the object property policy.
        """
        ...
    def GetTCSessionInfo(self) -> Teamcenter.Services.Strong.Core._2007_01.Session.GetTCSessionInfoResponse:
        """    
             This operation gets information about the current user's Teamcenter session. This
             will return more detail session information than the login service operation including
             User, Group, Role, Site, Volume, Project, and
             WorkContext.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    @typing.overload
    def SetObjectPropertyPolicy(self, PolicyName: str) -> bool: ...
    @typing.overload
    def SetObjectPropertyPolicy(self, Policy: Teamcenter.Soa.Common.ObjectPropertyPolicy) -> str: ...
    @typing.overload
    def SetObjectPropertyPolicy(self, PolicyName: str, UseRefCounting: bool) -> Teamcenter.Services.Strong.Core._2012_02.Session.SetPolicyResponse: ...
    def RefreshPOMCachePerRequest(self, Refresh: bool) -> bool:
        """    
             By Default the service operations will retrieve property value data straight from
             the POM. When refresh is set to true, a refresh
             will be done on business objects before getting any property data. This will update
             the POM with fresh data from the database. The refresh is only applied to business
             objects that are actually being returned by a service operation. This applies only
             to database objects, and is not applied to runtime objects.  This is applied to all
             subsequent service requests from the same client. If multiple clients are sharing
             the same Teamcenter server session the refresh POM state is applied per client. Setting
             this to true will have a performance impact but will grantee all property values
             returned are up-to-date.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Refresh: 
                         If true, the business objects are refreshed before getting property values, if false
                         the properties are retrieved from the POM without checks to the database.
             
        :return: True is always returned.
        """
        ...
    def SetUserSessionState(self, Pairs: list[Teamcenter.Services.Strong.Core._2007_12.Session.StateNameValue]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set the desired user session state values.  To clear a field's value, pass an empty
             string "" as the value. Failure to set a particular state value will result in a
             Partial Error with the clientId set to the name of the state property. State values
             can be per client session or per server session. Client session state is kept separate
             for each client application sharing the same Teamcenter server session, while server
             session state is shared with all client application sharing the Teamcenter server
             session. Valid keys for the session state pairs are:
             


currentChangeNotice: The UID of the ChangeNotice business
             object for this session (client session). This is deprecated from release Teamcenter
             11.5.
             
refreshPOM: If true the business objects in the POM are refreshed
             before returning property values.  This ensures property data is up-to-date, but
             is a performance hit (client session).
             
objectPropertyPolicy: The name of the current object property
             policy. This can also be controlled through the ObjectPropertyPolicyManager in the
             SOA client framework  (client session).
             
maxOperationBracketTime: Time (seconds) to bracket to limit
             a  POM refresh (client session).
             
maxOperationBracketInactiveTime: Time (seconds) to bracket
             to limit a  POM refresh (client session).
             
usePolicyOnly: If true, only properties defined in the current
             Object Property Policy will be returned. Objects that are added to the updated list
             of the ServiceData without named properties by default are returned with all properties
             currently loaded in the POM.
             
formatProperties: If true, the display value of the property
             will be formatted, if there is an active property formatter is attached to it. If
             false, the display value of the property will not be formatted, even if there is
             an active property formatter attached to it.
             
currentProject: The UID of the Project object (server
             session).
             
workContex: The UID of the WorkContext object (server
             session).
             
volume: The UID of the Volume object (server session).
             
local_volume: The UID of the LocalVolume object (server
             session).
             
groupMember: The UID of the GroupMember object (server
             session).
             
currentDisplayRule: The UID of the DisplayRule object
             (server session).
             
currentOrganization: The UID of the Organization object
             (server session).
             
locationCodePref: The CAGE/Location Code preference. This
             value is set on the Item attribute fnd0OriginalLocationCode
             when Item objects are created (server session).
             
currentChangeItem: The UID of the Change Item Revision business
             object for this session. This functionality is supported from Teamcenter 11.5.
             



Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Pairs: 
                         A list of name/value pairs of state properties to set.
             
        :return: 
        """
        ...
    def SetAndEvaluateIdDisplayRule(self, IdentifiableObjects: list[Teamcenter.Soa.Client.Model.ModelObject], DisplayRule: Teamcenter.Soa.Client.Model.Strong.IdDispRule, SetRuleAsCurrentInDB: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set the ID display rule for the session and optionally set it in the database.  The
             business objects from the identifiableObjects
             list are expanded using the new ID display rule and returned. The rule is applied
             to all business objects process throughout the rest of the session.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param IdentifiableObjects: 
                         A list of business objects for which the new ID display rule has to be re-evaluated.
             
        :param DisplayRule: 
                         The ID display rule that is to be used for evaluation.
             
        :param SetRuleAsCurrentInDB: 
                         If true then the ID display rule will be set for the current user in the database.
             
        :return: .
        """
        ...
    def Connect(self, FeatureKey: str, Action: str) -> Teamcenter.Services.Strong.Core._2008_03.Session.ConnectResponse:
        """    
             Performs Teamcenter Flexlm license related operations, depending on the input parameters.
             

             The low level actions are:
             

             1.  ILM__init_module: Initializes the license module (if it has not already been
             initialized).
             
             2.  ILM__leave_module: Deallocates a license of the given module. If the user had
             N free licenses for this module, (N plus one) will be left after this call.
             
             3.  ILM__check_module: Checks to see if the user has bought the specified module
             and returns the number of purchased licenses.
             
             4.  ILM__enter_module: Allocates one license of the given module. If the user has
             bought N licenses for this module, (N minus one) will be left after this call.
             
             5.  ILM__exit_module: Leaves the module.
             


Teamcenter Component:

             Licensing - Provides the capability to assign and monitor licenses such that the
             users (an individual; a system; a module etc.) of teamcenter can be limited to use
             the capabilities that they have privileges for
             
        :param FeatureKey: 
                         A string corresponding to the product as listed in the license file (e.g. teamcenter_author)
             
        :param Action: 

        :return: contains a ServiceData (ConnectResponse.serviceData), and number of licenses avaliable.
             Any failure will be returned via ServiceData with error message.
        """
        ...
    def GetFavorites(self) -> Teamcenter.Services.Strong.Core._2008_03.Session.FavoritesResponse:
        """    
             This operation retrieves the saved Favorites containers and Favorites objects for
             the current session user.  You can use Favorites to track containers and objects
             you access frequently, such as folders, parts or forms.
             

             If errors are encountered, partial results are returned. Partial errors are returned
             with client IDs reflecting the index value of the saved Favorite. A service exception
             is thrown if an error is encountered that is not related to a specific Favorite container
             or Favorite object.
             

             Any Teamcenter object that is returned as a Favorite object is added to ServiceData plain objects.  For example, if an item exists in
             the list of Favorite objects, the object tag value for that item will be returned
             in the ServiceData list of plain objects.
             


Use Cases:

             User logs in and selects their saved Favorites.
             

             The Favorites view in the client application is populated with the Favorites containers
             and objects returned from this operation.
             


Dependencies:

             setFavorites
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :return: 
        """
        ...
    def SetFavorites(self, Input: Teamcenter.Services.Strong.Core._2008_03.Session.FavoritesInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation saves new favorite containers and favorite objects for the current
             session user.
             

             Any partial errors encountered during this operation are returned using the clientID specified by the caller. A service exception
             is thrown if an error is encountered that is not related to a specific favorite container
             or favorite object.  You can use favorites to track containers and objects you access
             frequently, such as folders, parts or forms.  For example, the Newstuff folder could
             be added as a container to the list of favorites.
             


Use Cases:

             User saves a container to their favorites list.
             

             For this operation, the list of all current favorites for the user and the list containing
             the container the user desires to add are supplied as input and the new container
             is added to the list of saved favorites in Teamcenter.
             


Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Input: 
                         The information required to establish a new set of saved favorites for the current
                         session user.
             
        :return: 
        """
        ...
    def GetDisplayStrings(self, Info: list[str]) -> Teamcenter.Services.Strong.Core._2008_06.Session.GetDisplayStringsResponse:
        """    
             Get the localized text string for each input key from the info array. The input key
             must correspond to a key defined in the Text Server. If the input array is empty,
             the returned array will also be empty.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Info: 
                         A list of Text Server key names.
             
        :return: An array Text Server key/localized value pairs. Any errors encountered while looking
             up a given Text Server key will be returned as a partial error with the key name
             attached to the partial error.
        """
        ...
    def StartOperation(self) -> str:
        """    
             Start an operation bracket.  An operation bracket is a period of execution in which
             any object will need to be refreshed in the server from the database only once.
             This allows the client to avoid unnecessary database operations that the server might
             perform redundantly if underlying code accesses the same object multiple times.
             The client will use the return value to call the stopOperation
             operation to indicate the end of the bracket.  Brackets may be nested or overlapped.
             A bracket should start and end within the scope of a single client function and
             should not span a user interaction.  By default, each service operation starts and
             stops its own operation bracket.
             

Dependencies:

             stopOperation
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def StopOperation(self, OpId: str) -> bool:
        """    
             Stop an operation bracket, in which objects need to be refreshed only once.  See
             startOperation.
             

Dependencies:

             startOperation
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param OpId: 
                         The operation identifier assigned to the operation and returned by the <font face="courier" height="10">startOperation</font> request.
             
        :return: true
        """
        ...
    def GetPreferences2(self, PreferenceNames: list[Teamcenter.Services.Strong.Core._2007_01.Session.ScopedPreferenceNames]) -> Teamcenter.Services.Strong.Core._2010_04.Session.MultiPreferenceResponse2:
        """    
             This operation takes an input structure which contains a scope value and vector of
             preference names. The return type of this operation is the MultiPreferencesResponse2
             structure whose elements are the ServiceData and the vector of ReturnedPreferences2
             structure.
             

Teamcenter Component:

             Preference Management - Provides the capability to store and manage both system and
             user prefrences that are used to tune the system based on the settings. Typically
             these consist of name value pairs that the code looks up at runtime to configure
             the behavior.
             
        :param PreferenceNames: 
                         The input structure, the object of which would ahve 2 input parameters of scope and
                         the preference names.
             
        :return: This structure is used to return Preference
        """
        ...
    def GetShortcuts(self, ShortcutInputs: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Core._2010_04.Session.GetShortcutsResponse:
        """    
             This operation gets the sections and corresponding content in Left Hand Navigation
             task pane given the section name and the corresponding preference name for the current
             session user. The preference name is the key to look up section content stored in
             preference.    In the rich client, the LHN sections are Quick
             Links, Open Items, History, Favorites and I Want To. The user can organize Teamcenter
             data in these sections during runtime, which is persisted in the preference. The
             Quick Links section provides a quick access point to the user`s home folder, work
             list, favorite Web links, projects, saved searches, and View Markup. The Open Items
             section lists Teamcenter components currently opened in the active perspective. The
             History section lists Teamcenter components opened before, but currently closed.
             The Favorites section contains the Favorites container and Teamcenter components
             the user added there for quick access. The I Want To section contains commands configured
             by default or configured by the user.
             

Use Cases:

             The user logs in to the rich client and retrieves Quick Links, Open Items, History,
             Favorites and I Want To task pane section for Left Hand Navigation.
             

Teamcenter Component:

             RAC Views Viewer - Rich client views and viewer framework components extending from
             eclipse jface viewer and view extension.
             
        :param ShortcutInputs: 
                         A map of the key representing the  section name in the left hand navigation and the
                         value representing the preference name that needs to be looked up to get the content.
                         For example,  Key =QuickLinksSection, Value = MyTeamcenterQuicklinksection;  Key
                         = FavoritesSection, value= My Favorites . Valid keys in the map are QuickLinksSection,
                         HistorySection, FavoritesSection, IWantToSection, OpenItemsSection. Valid values
                         for these keys in the map could be MyFavorites, HistoryList, QuickLinksSection, MyQuicklinkSection,
                         OpenItemSection, etc.
             
        :return: Â Â Â Â 515024 (error code): The given tag does not exist in the
             database or is not a persistent object tag.
        """
        ...
    def GetClientCacheData(self, Features: list[str]) -> Teamcenter.Services.Strong.Core._2011_06.Session.ClientCacheInfo:
        """    
             This operation returns information required to maintain a client cache. The Teamcneter
             server maintains a set of Datasets with static or near static data that is
             pertainant to a client application.  This static data can be downloaded through FMS
             to the cleint host one time, and available for each subsequent client session, thus
             improving the overall performance of the client application. These Datasets are updated
             as part of the deploy process from the BMIDE. The cleint cache consits of serveral
             features, each of these features can be used independnatly of each other. The following
             features are available:
             


ClientMetaModel :The is the client side version of the server`s Meta
             Model. This includes type descriptions, property descriptions, List Of Values data,
             and Dataset tool data. The use of the ClientMetaModel cache replaces the need to
             use the getTypeDescriptions  service calls. By setting the Connection.setOption(OPT_USE_CLIENT_META_MODEL_CACHE,
             true), the SOA client framework will use the cache for Client  Meta Model
             data. The SOA client framework takes care of calling this service opeation and FMS
             to populate the cache. This feature includes the Dataset:Types, Lov, ToolsData,
             types_local (one for each locale i.e types_en_US), lov_local (one for
             each locale i.e lov_en_US).
             
TextData: This contains the localized string available in the Teamcenter
             server's Text Server. Using the localized data from this cache replaces the need
             to call the getDisplayStrings service operation.
             



Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Features: 
                         Names of features to return<i>, All</i> to return data for all features. Available
                         features are <i>ClientMetaModel</i> and <i>TextData</i>.
             
        :return: Feature descriptions
        """
        ...
    def GetTypeDescriptions(self, TypeNames: list[str]) -> Teamcenter.Schemas.Soa._2011_06.Metamodel.TypeSchema:
        """    
             Get the Meta data for the named Business Model object types. This includes type and
             property descriptions and LOV information.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param TypeNames: 
                         List of Business Model Object type names.
             
        :return: The Meta data for the named types.
        """
        ...
    def UpdateObjectPropertyPolicy(self, PolicyID: str, AddProperties: list[Teamcenter.Soa.Common.PolicyType], RemoveProperties: list[Teamcenter.Soa.Common.PolicyType]) -> str:
        """    
             Update the named policy, adding and removing the named properties. This operation
             only applies to object property policies that have been defined on the client side.
             

Dependencies:

             setObjectPropertyPolicy
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param PolicyID: 
                         The ID of the policy to update. This is the ID that is returned from the <font face="courier" height="10">setObjectPropetyPolicy</font> operation.
             
        :param AddProperties: 
                         List of properties to add to the named policy.  If the property already exists in
                         the policy, the flags (i.e. <font face="courier" height="10">excludeUiValues</font>)
                         from the input will take precedence over the flags on the existing property.
             
        :param RemoveProperties: 
                         List of properties to remove from the named policy. If a source <font face="courier" height="10">PolicyType</font> defines a type without properties, the whole type is
                         removed.
             
        :return: The policy ID, will be the same as the input ID.
        """
        ...
    def RegisterState(self, Level: str) -> Teamcenter.Services.Strong.Core._2012_02.Session.RegisterIndex:
        """    
             Register desired level for server state as used by the Server Manager to control
             server timeout. Note that an attempt to register at LEVEL_STATELESS is ignored since
             this is the default level when no registrations are in effect. To move from a higher
             level to the stateless level the unregister
             operation should be used to delete the earlier registration. Note that it is possible
             to be registered at more than one level and there may be multiple registrations at
             each level.
             

Dependencies:

             unregisterState
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Level: 
                         Desired server state: "<i>Edit</i>" or "<i>Read</i>"
             
        :return: operation to undo
             this registration.  If no registration occurs, zero is returned.
        """
        ...
    def UnregisterState(self, Index: int) -> bool:
        """    
             Remove the specified registration.
             

Dependencies:

             registerState
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Index: 
                         Index returned by previous call to <font face="courier" height="10">registerState</font>.
             
        :return: True
        """
        ...
    def GetTypeDescriptions2(self, TypeNames: list[str], Options: System.Collections.Hashtable) -> Teamcenter.Schemas.Soa._2011_06.Metamodel.TypeSchema:
        """    
             Gets the Meta data for the named Business Model object types based on the configurations
             specified by the client.  To improve performance, clients can specify to exclude
             certain Meta data such as LOV References and Naming Rule References for the given
             types.
             
             If options are not provided this operation returns all meta data associated with
             given types.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param TypeNames: 
                         List of Business Model Object type names.
             
        :param Options: 
                         A list of property constant names to be fetched. If the list of property constant
                         names is empty this operation does not return any constant values. If the PropertyConstants
                         option is not provided then it will return all constants that can server can return.
             
        :return: The Meta data for the named types as requested  . There are no errors returned, invalid
             input types names are ignored and no type information will be returned for those
             types.
        """
        ...
    def SetUserSessionStateAndUpdateDefaults(self, Pairs: list[Teamcenter.Services.Strong.Core._2007_12.Session.StateNameValue]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets the desired user session state values. This operation also updates
             the default value of the Group, Role and Project when these session states are changed.
             

             To clear a field's value, client needs to pass an empty string "" as the value.
             

             Failure to set a particular state value will result in a Partial Error with the clientId
             set to the name of the state property. State values can be per client session or
             per server session. Client session state is kept separate for each client application
             sharing the same Teamcenter server session, while server session state is shared
             with all client application sharing the Teamcenter server session.
             

             Valid keys for the session state pairs are:
             


currentChangeNotice - The UID of the ChangeNotice business
             object for this session (client session).This is deprecated from release Teamcenter
             11.5.
             
refreshPOM - If true the business objects in the POM are refreshed
             before returning property values.  This ensures property data is up-to-date, but
             is a performance hit (client session).
             
objectPropertyPolicy - The name of the current object property
             policy. This can also be controlled through the ObjectPropertyPolicyManager in the
             SOA client framework  (client session).
             
maxOperationBracketTime - Time (seconds) to bracket to limit
             a  POM refresh (client session).
             
maxOperationBracketInactiveTime - Time (seconds) to bracket
             to limit a  POM refresh (client session).
             
usePolicyOnly - If true, only properties defined in the current
             Object Property Policy will be returned. Objects that are added to the updated list
             of the ServiceData without named properties by default are returned with all properties
             currently loaded in the POM.
             
formatProperties - If true, the display value of the property
             will be formatted, if there is an active property formatter is attached to it. If
             false, the display value of the property will not be formatted, even if there is
             an active property formatter attached to it (client session).
             
currentProject - The UID of the Project object (server
             session).
             
workContex - The UID of the WorkContext object (server
             session).
             
volume - The UID of the Volume object (server session).
             
local_volume - The UID of the LocalVolume object (server
             session).
             
groupMember - The UID of the GroupMember object (server
             session).
             
currentDisplayRule - The UID of the DisplayRule object
             (server session).
             
currentOrganization - The UID of the Organization object
             (server session).
             
locationCodePref - The CAGE/Location Code preference. This
             value is set on the Item attribute fnd0OriginalLocationCode
             when Item objects are created (client session).
             
currentChangeItem - The UID of the Change Item Revision business
             object for this session. This functionality is supported from Teamcenter 11.5.
             



Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Pairs: 
                         A list of name/value pairs (string/string) of state properties to set.
             
        :return: 
        """
        ...
    def SponsoredLogin(self, SponsoringUser: str, Password: str, SponsoredUser: str, SponsoredGroup: str, SponsoredRole: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse:
        """    
             Authenticates the sponsoring user`s credentials and initialize a Teamcenter session
             for the sponsored user. The operation will throw an InvalidCredentialsException as
             described below.
             

             When the client application is deployed to a 4Tier environment the login operation
             also contributes to the assignment of a Teamcenter server instance to the client
             session. The sponsoring user, sponsored users and sessionDiscriminator are considered
             in server assignment.
             
             Note: The sessionDiscriminator could be blank ("") or have some value (e.g. "session1"
             or "session2")
             

             Example with blank ("") sessionDiscriminator:
             
             - Sponsor1/User1 and Sponsor1/User2 will be assigned to different servers since their
             access controls are based on User1 and User2
             
             - Sponsor1/User1 and Sponsor2/User1 will be assigned to different servers.
             
             - Sponsor1/User1 and User1 will be assigned to different servers.
             

             Example with "session1" and "session2" sessionDiscriminator:
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session1) will be assigned to same
             servers
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session2) will be assigned to different
             servers
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param SponsoringUser: 
                         The sponsoring user`s Teamcenter user name. This is case insensitive (jdoe or JDOE)
             
        :param Password: 
                         The sponsoring user`s Teamcenter password.
             
        :param SponsoredUser: 
                         Sponsored user`s user name. This is case insensitive (jdoe or JDOE)
             
        :param SponsoredGroup: 
                         The group ID for the sponsored user.
             
        :param SponsoredRole: 
                         The role of the sponsored user.
             
        :param Locale: 
                         The locale to be used by the Teamcenter server process for this session. If null,
                         the server`s default locale will be used.
             
        :param SessionDiscriminator: 
                         Client defined identifier for this session. This argument is ignored when the client
                         application is deployed in a 2Tier environment (IIOP communication).
             
        :return: 128004:  The logon is accepted. However, data entry should only contain characters
             that belong to the encoding of the database instance. The information is in the error
             message.
        """
        ...
    def SponsoredLoginSSO(self, SponsoringUser: str, SsoCredentials: str, SponsoredUser: str, SponsoredGroup: str, SponsoredRole: str, Locale: str, SessionDiscriminator: str) -> Teamcenter.Services.Strong.Core._2006_03.Session.LoginResponse:
        """    
             Authenticates the sponsoring user using Single-Sign-On (SSO) credentials and initialize
             a Teamcenter session for the sponsored user client. The username and ssoCredentials
             arguments are for the sponsoring user and must be obtained from Teamcenter's Security
             Services. The SsoCredentials class offers a simple API to get these values. The operation
             will throw an InvalidCredentialsException as described below.
             

             When the client application is deployed to a 4Tier environment the login operation
             also contributes to the assignment of a Teamcenter server instance to the client
             session. The sponsoring user, sponsored users and sessionDiscriminator are considered
             in server assignment.
             
             Note: The sessionDiscriminator could be blank ("") or have some value (e.g. "session1"
             or "session2")
             

             Example with blank ("") sessionDiscriminator:
             
             - Sponsor1/User1 and Sponsor1/User2 will be assigned to different servers since their
             access controls are based on User1 and User2
             
             - Sponsor1/User1 and Sponsor2/User1 will be assigned to different servers.
             
             - Sponsor1/User1 and User1 will be assigned to different servers.
             

             Example with "session1" and "session2" sessionDiscriminator:
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session1) will be assigned to same
             servers
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session2) will be assigned to different
             servers
             

             Example with "session1" and "session2" sessionDiscriminator:
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session1) will be assigned to same
             servers
             
             - Sponsor1/User1(session1) and Sponsor1/User1(session2) will be assigned to different
             servers
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param SponsoringUser: 
                         The sponsoring user`s Teamcenter user name. This is case insensitive (jdoe or JDOE)
             
        :param SsoCredentials: 
                         The sponsoring user's Teamcenter SSO credentials. This should have been obtained
                         from Teamcenter Security Services.
             
        :param SponsoredUser: 
                         Sponsored user`s user name. This is case insensitive (jdoe or JDOE)
             
        :param SponsoredGroup: 
                         The group ID for the sponsored user.
             
        :param SponsoredRole: 
                         The role of the sponsored user.
             
        :param Locale: 
                         The locale to be used by the Teamcenter server process for this session. If null,
                         the server`s default locale will be used.
             
        :param SessionDiscriminator: 
                         Client defined identifier for this session. This argument is ignored when the client
                         application is deployed in a 2Tier environment (IIOP communication).
             
        :return: 128004: The logon is accepted. However, data entry should only contain characters
             that belong to the encoding of the database instance. The information is in the error
             message.
        """
        ...
    def LicenseAdmin(self, LicAdminInput: list[Teamcenter.Services.Strong.Core._2019_06.Session.LicAdminInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation provides licensing related operations such as check-out and check-in
             of a license feature key.
             

Teamcenter Component:

             Licensing - Provides the capability to assign and monitor licenses such that the
             users (an individual; a system; a module etc.) of teamcenter can be limited to use
             the capabilities that they have privileges for
             
        :param LicAdminInput: 
                         A list of feature key and action pairs. This allows multiple license keys to be checked
                         out in one service operation call.
             
        :return: 
        """
        ...
    def AddObjectPropertyPolicies(self, ClientPolicies: list[Teamcenter.Soa.Common.ObjectPropertyPolicy], NamedPolicies: list[str]) -> Teamcenter.Services.Strong.Core._2021_12.Session.AddPoliciesResponse:
        """    
             Adds multiple object property policies to the session. Once these policies are added
             to the session, the client application can quickly switch between policies using
             the appropriate methods on the ObjectPropertyPolicyManager
             class in the SOA client framework.
             
             The business logic of a service operation determines what business objects are returned,
             while the object property policy determines which properties are returned on each
             business object instance. This allows the client application to determine how much
             or how little data is returned based on how the client application uses those returned
             business objects. The policy is applied uniformly to all service operations.
             
             By default, all applications use the Default object property policy, defined
             on the Teamcenter server $TC_DATA/soa/policies/default.xml.
             It is this policy that is applied to all service operation responses until the client
             application changes the policy. Siemens PLM Software strongly recommends that all
             applications change the policy to one applicable to the client early in the session.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param ClientPolicies: 
                         A list of client defined object property policies.
             
        :param NamedPolicies: 
                         A list of policy files defined on the Teamcenter server volume at<font face="courier" height="10"> $TC_Data/soa/policies/*.xml</font>.
             
        :return: 
        """
        ...
    def TcServerSleep(self, Seconds: int) -> str:
        """    
             A no-op serivce operation that puts the TcServer in a wait/sleep for the requested
             amount of time before returning.
             
             This can be used to simulate long running service requests.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Seconds: 
                         The number of seconds to sleep.
             
        :return: A message that the operation has completed.
        """
        ...

