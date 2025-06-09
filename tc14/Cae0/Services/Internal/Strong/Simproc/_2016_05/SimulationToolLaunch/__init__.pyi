import Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch
import Teamcenter.Soa.Client.Model
import typing

class SimulationToolLaunch:
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportSimulationToolLaunchOutputs(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, WorkingDirectory: str, InputObject: Teamcenter.Soa.Client.Model.ModelObject, XmlFileName: str, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, JobID: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...

