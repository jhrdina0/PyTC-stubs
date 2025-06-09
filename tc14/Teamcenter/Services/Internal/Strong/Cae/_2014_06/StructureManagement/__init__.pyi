import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FileStatus:
    def __init__(self, ) -> None: ...
    Heading: str
    Dstype: str
    FoundCount: int
    TotalCount: int

class MonitoredColumn:
    def __init__(self, ) -> None: ...
    ColumnHeading: str
    IsImage: bool
    Value: str

class MonitorResponse:
    def __init__(self, ) -> None: ...
    ColumnHeadings: list[str]
    ProgressHeadings: list[FileStatus]
    MonitoredComponentMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def LoadSimulationDataMonitor(self, Rootbomline: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> MonitorResponse: ...
    def RefreshSimulationDataMonitor(self, Itemrevisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> MonitorResponse: ...

