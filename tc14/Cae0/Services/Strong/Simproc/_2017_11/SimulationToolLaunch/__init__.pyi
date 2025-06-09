import Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch
import Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class OptionalInputInfo:
    """
    
            Structure containing the ItemRevision object and directory name where the
            named references from the ItemRevision object will be exported.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
ItemRevision object whose named references are to be exported during Simulation
            tool launch operation.
            """
    ExportDirectory: str
    """Name of directory where the named references from Optional Input will be exported."""

class SimulationToolLaunch:
    """
    Interface SimulationToolLaunch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.LaunchInputInfo2], WorkingDirectory: str, LaunchType: str, ExportRunTimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext], OptionalInputInfo: list[OptionalInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

