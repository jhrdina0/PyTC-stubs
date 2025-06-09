import Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch
import Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch
import Cae0.Services.Strong.Simproc._2017_11.SimulationToolLaunch
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExportFileOptions:
    """
    
            This structure contains the information of export option for a file object which
            is to be exported in staging directory.
            
    """
    def __init__(self, ) -> None: ...
    IsAutoProcessSelected: bool
    """
            If true, auto process is selected for file export and autoProcessOption is
            used for export action; otherwise promptUserOptions is used for export action.
            """
    AutoProcessOption: str
    PromptUserOptions: list[ExportFilePromptUserOption]
    """List of export options for file object from prompt user action."""

class ExportFilePromptUserOption:
    """
    
            This structure contains the information of export option for a file object from prompt
            user action which is to be exported in staging directory.
            
    """
    def __init__(self, ) -> None: ...
    FileObject: Teamcenter.Soa.Client.Model.ModelObject
    """File object which is to be exported in staging directory."""
    ExportOption: str

class LaunchInputInfo3:
    """
    
            Structure containing the input object on which tool needs to be launched and the
            configuration information which needs to be applied in case the input object is of
            type ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """Input object on which Simulation Tool is to be launched."""
    InputDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
Dataset on which Simulation Tool is to be launched. To launch a Simulation
            Tool, the user selects the ItemRevision on which the Simulation Tool is to
            be launched. This inputDataset is the Dataset attached to this selected
            ItemRevision. If the selected ItemRevision is has multiple datasets
            of the same type, then a conflict resolution dialog is presented to the user to pick
            the appropriate Dataset and proceed with the Simulation Tool Launch.
            """
    InputFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    """Interactively selected file on which Simulation Tool is to be launched."""
    InputWebLink: Teamcenter.Soa.Client.Model.Strong.Form
    """
Web Link on which Simulation Tool is to be launched. To launch a Simulation
            Tool, the user selects the ItemRevision on which the Simulation Tool is to
            be launched. This inputWebLink is the Web Link attached to this selected
            ItemRevision. If the selected ItemRevision has mutiple web links, then
            a conflict resolution dialog is presented to the user to pick appropriate Web
            Link and proceed with the Simulation Tool Launch.
            """
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
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[LaunchInputInfo3], ScratchDirectory: str, UserStagingLocation: str, UserStagingDir: str, LaunchType: str, ExportRunTimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext], OptionalInputInfo: list[Cae0.Services.Strong.Simproc._2017_11.SimulationToolLaunch.OptionalInputInfo], FileExportOptions: list[ExportFileOptions]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

