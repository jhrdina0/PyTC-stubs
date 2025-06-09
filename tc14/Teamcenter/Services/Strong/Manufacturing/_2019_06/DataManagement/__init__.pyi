import System
import Teamcenter.Soa.Client.Model
import typing

class SelectedStudySourceResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data containing partial errors if any."""
    LogFileTicket: str
    """The FMS ticket to the log file."""

class SelectedSyncPublishStudyInput:
    """
    
A list of selected business objects from Simulation Study. The valid types are
Mfg0BvrSimStudy,
Mfg0BvrProcessArea, Mfg0BvrProcessLine, Mfg0BvrProcessStation Mfg0BvrProcess,
and
Mfg0BvrOperation.It also contains the study root node and the synchronization
mode (Time based/ Event based).
    """
    def __init__(self, ) -> None: ...
    SelectedLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of selected objects in a simulation study.The valid types are: Mfg0BvrSimStudy,
            Mfg0BvrProcessArea, Mfg0BvrProcessLine, Mfg0BvrProcessStation, Mfg0BvrProcess, Mfg0BvrOperation
            and Mfg0BvrWorkarea.
            """
    Mode: str

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def PublishSelectionFromStudyToSource(self, Input: list[SelectedSyncPublishStudyInput]) -> SelectedStudySourceResponse: ...
    def SyncSelectionInStudyWithSource(self, Input: list[SelectedSyncPublishStudyInput]) -> SelectedStudySourceResponse: ...

