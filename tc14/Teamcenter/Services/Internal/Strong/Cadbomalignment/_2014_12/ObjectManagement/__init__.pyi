import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddCADOccToLayoutInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    LayoutItemRevision: str
    SelectedLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class ColumnSet:
    def __init__(self, ) -> None: ...
    Column: list[Column]
    Table: str

class RowSet:
    def __init__(self, ) -> None: ...
    Row: list[Row]

class RowColumn:
    def __init__(self, ) -> None: ...
    ColumnSet: ColumnSet
    RowSet: RowSet

class AddSelectionToLayoutInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    LayoutItemRevision: str
    PmmInputObject: RowColumn

class AddSelectionToLayoutOutput:
    def __init__(self, ) -> None: ...
    LayoutWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    LayoutTopline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    LayoutChildren: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    Confilictpmmobject: list[Confilictingobject]

class AddToLayoutInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    LayoutItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ViewType: str
    SelectedLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class AddToLayoutOutput:
    def __init__(self, ) -> None: ...
    LayoutWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    LayoutTopline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    LayoutChildren: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    ConflictingLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class CadStructureState:
    def __init__(self, ) -> None: ...
    StructureType: int
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    SelectedLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]

class Column:
    def __init__(self, ) -> None: ...
    Name: str
    Datatype: str
    Table: str
    LogicalName: str
    Width: int

class Confilictingobject:
    def __init__(self, ) -> None: ...
    Conflictingbomline: Teamcenter.Soa.Client.Model.Strong.BOMLine
    PmmObject: RowColumn

class PMMReferenceStates:
    def __init__(self, ) -> None: ...
    SelectedObjects: list[PMMReferenceObjects]
    UnselectedObjects: list[PMMReferenceObjects]

class PMMBaseSearchInfo:
    def __init__(self, ) -> None: ...
    QueryInfos: list[QueryInfo]
    PmmResults: PMMReferenceStates
    CadResults: list[CadStructureState]

class PMMSpatialSearchCriteria:
    def __init__(self, ) -> None: ...
    SearchType: int
    TstState: bool
    VooState: bool
    Coords: list[float]
    Lengths: list[float]
    Distance: float
    Attributes: list[QueryInfo]
    MeasUnit: str

class PMMAdvancedSearchInfo:
    def __init__(self, ) -> None: ...
    SearchCriteria: PMMSpatialSearchCriteria
    PmmResults: PMMReferenceStates
    CadResults: list[CadStructureState]

class PMMSCOInfo:
    def __init__(self, ) -> None: ...
    BaseSearch: PMMBaseSearchInfo
    AdvancedSearch: PMMAdvancedSearchInfo

class CreatePMMSCOInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    PmmServiceName: str
    ScoType: int
    ScoName: str
    ScoDesc: str
    ContextName: str
    PlmxmlFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    ScoInfo: PMMSCOInfo

class CreatePMMSCOResponse:
    def __init__(self, ) -> None: ...
    PmmscoOutputMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetPLMXMLFromPMMSCORecipeResponse:
    def __init__(self, ) -> None: ...
    PmmscoPlmxmlInfoMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PMMAddSelectionToLayoutResponse:
    def __init__(self, ) -> None: ...
    AddSelectionToLayoutMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PMMAddToLayoutResponse:
    def __init__(self, ) -> None: ...
    AddToLayoutMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PMMAdvancedSearchExecInfo:
    def __init__(self, ) -> None: ...
    AdvSearchInfo: PMMAdvancedSearchInfo
    SelectedObjects: list[RowColumn]
    UnSelectedObjects: list[RowColumn]

class PMMBaseSearchExecInfo:
    def __init__(self, ) -> None: ...
    BaseSearchInfo: PMMBaseSearchInfo
    SelectedObjects: list[RowColumn]
    UnSelectedObjects: list[RowColumn]

class PMMReferenceObjects:
    def __init__(self, ) -> None: ...
    ObjectType: str
    Objects: list[str]

class PMMSCOInfoInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Pmmsco: Teamcenter.Soa.Client.Model.Strong.Cba0PMMStructureContext
    OpenMode: int
    OutputRequested: int

class PMMSCOInfoOutput:
    def __init__(self, ) -> None: ...
    ServiceName: str
    ContextName: str
    ScoType: int
    StaticPlmxmlReadTicket: str
    StaticStructureReadTicket: str
    DynamicPlmxmlReadTicket: str
    BaseSearchExecInfo: PMMBaseSearchExecInfo
    AdvSearchExecInfo: PMMAdvancedSearchExecInfo

class PMMSCOInfoResponse:
    def __init__(self, ) -> None: ...
    PmmscoInfoMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PMMSCOPLMXMLInfo:
    def __init__(self, ) -> None: ...
    Type: int
    PlmxmlFileReadTicket: str
    PlmxmlFilename: str

class PMMSCORecipeInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    OpenMode: int
    PmmSco: Teamcenter.Soa.Client.Model.Strong.Cba0PMMStructureContext

class QueryInfo:
    def __init__(self, ) -> None: ...
    TableName: str
    QueryNameValues: System.Collections.Hashtable

class Row:
    def __init__(self, ) -> None: ...
    Value: list[str]
    ClientID: str

class SaveOrClonePMMSCOWithFilesInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    OpMode: int
    PlmxmlFiles: list[UploadOrUpdateFileInfo]
    PmmSco: Teamcenter.Soa.Client.Model.Strong.Cba0PMMStructureContext

class SaveOrClonePMMSCOWithFilesResponse:
    def __init__(self, ) -> None: ...
    PmmscoUploadMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class UploadOrUpdateFileInfo:
    def __init__(self, ) -> None: ...
    RefType: int
    PlmxmlFile: Teamcenter.Soa.Client.Model.Strong.ImanFile

class ObjectManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddCADOccurrencesToLayout(self, Inputs: list[AddCADOccToLayoutInput]) -> PMMAddToLayoutResponse: ...
    def CreatePMMSCO(self, Input: list[CreatePMMSCOInputInfo]) -> CreatePMMSCOResponse: ...
    def GetPLMXMLFromPMMSCORecipe(self, Input: list[PMMSCORecipeInputInfo]) -> GetPLMXMLFromPMMSCORecipeResponse: ...
    def GetPMMSCOInfo(self, PmmscoInputs: list[PMMSCOInfoInput]) -> PMMSCOInfoResponse: ...
    def PmmAddSelectionToLayout(self, Inputs: list[AddSelectionToLayoutInput]) -> PMMAddSelectionToLayoutResponse: ...
    def PmmAddToLayout(self, Inputs: list[AddToLayoutInput]) -> PMMAddToLayoutResponse: ...
    def SaveOrClonePMMSCOWithFiles(self, Inputs: list[SaveOrClonePMMSCOWithFilesInputInfo]) -> SaveOrClonePMMSCOWithFilesResponse: ...

