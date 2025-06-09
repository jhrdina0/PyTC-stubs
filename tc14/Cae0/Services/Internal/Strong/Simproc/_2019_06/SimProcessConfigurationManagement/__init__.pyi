import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SimulationDashboardColumnCellInfo:
    def __init__(self, ) -> None: ...
    ColumnName: str
    ColumnType: str
    ColumnCellValue: str
    ColumnCellValueType: str
    StatusValue: str
    AttributeName: str
    AttributeComponent: Teamcenter.Soa.Client.Model.ModelObject
    PedigreeObject: Teamcenter.Soa.Client.Model.Strong.StructureContext
    IsModifiable: bool
    FileDetails: list[SimulationDashboardFileDetails]

class SimulationDashboardDetailsResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    FileSummaryInfo: list[SimulationDashboardFileSummaryInfo]
    DashboardTableInfoDetails: System.Collections.Hashtable
    ObjectsToMonitor: int
    ObjectsFiltered: int

class SimulationDashboardFileDetails:
    def __init__(self, ) -> None: ...
    ItemRevName: str
    DatasetName: str
    FileName: str
    FileOwningUser: str
    LastModifiedDate: str
    ItemRevComp: Teamcenter.Soa.Client.Model.ModelObject
    DatasetComponent: Teamcenter.Soa.Client.Model.Strong.Dataset
    FileComponent: Teamcenter.Soa.Client.Model.Strong.ImanFile

class SimulationDashboardFileSummaryInfo:
    def __init__(self, ) -> None: ...
    ColumnNameHeading: str
    DatasetType: str
    FoundCount: int
    AmbiguousCount: int
    NotFoundCount: int
    NotApplicableCount: int
    TotalCount: int

class SimProcessConfigurationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDashboardDataForIRList(self, DashboardConfiguration: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, ItemRevisionList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> SimulationDashboardDetailsResponse: ...
    def GetDashboardDataForModelStructure(self, DashboardConfiguration: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision, RootBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> SimulationDashboardDetailsResponse: ...

