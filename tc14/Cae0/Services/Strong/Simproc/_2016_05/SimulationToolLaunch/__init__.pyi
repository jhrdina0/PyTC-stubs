import Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ImportConfigRuntimeOverrideInfo2:
    """
    Structure holding runtime overrides for Simulation Tool ouput configuration.
    """
    def __init__(self, ) -> None: ...
    ItemCreationSetting: str
    """
            Item creation flag. Supported values are: "As_Needed", "Always" or "Never". This
            parameter is optional. If no value is provided, default value configured in the Simulation
            Tool will be used.
            """
    DatasetCreationSetting: str
    """
            Dataset creation flag. Supported values are: "As_Needed", "Always" or "Never". This
            parameter is optional. If no value is provided, default value configured in the Simulation
            Tool will be used.
            """
    AutoProcessOptions: str
    OutputNamePatterns: list[str]

class LaunchInputInfo2:
    """
    
            Structure containing the input object on which tool needs to be launched and the
            configuration information which needs to be applied in case the input object is of
            type ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """Input object on which Simulation Tool is to be launched."""
    InputDataset: Teamcenter.Soa.Client.Model.ModelObject
    """Interactively selected dataset on which Simulation Tool is to be launched."""
    InputFile: Teamcenter.Soa.Client.Model.ModelObject
    """Interactively selected file on which Simulation Tool is to be launched."""
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Configuration Context object holding the configuration details for the Input object
            in case it is of type ItemRevision. NULL otherwise.
            """

class SimulationToolLaunch:
    """
    Interface SimulationToolLaunch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[LaunchInputInfo2], WorkingDirectory: str, LaunchType: str, ExportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: ImportConfigRuntimeOverrideInfo2, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

