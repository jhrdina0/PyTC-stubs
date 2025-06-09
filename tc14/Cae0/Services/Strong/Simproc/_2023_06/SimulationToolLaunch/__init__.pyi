import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExportConfigRuntimeOverrideInfo2:
    """
    This structure holds runtime overrides for Simulation Tool export configuration.
    """
    def __init__(self, ) -> None: ...
    PlmxmlExportFileName: str
    """
            The name of the PLMXML file to be exported. This is optional. If no value is provided,
            the file name specified in the Simulation Tool configuration will be used.
            """
    RuntimeArguments: list[str]
    """
            A list of runtime arguments and their values to be provided to the Simulation tool.
            The argument and values are represented by a single string. The values will be separated
            by two colons "::" which is converted to the "=" equals sign. Arguments that have
            no value are represented by blank or white space. The argument will be prefixed by
            a single dash "-". Example: To pass the argument and value pairs as an argument,
            the user should pass "fem::3D dat::blk" as a string list. This will result in the
            following arguments "-fem=3D -dat=blk". This is optional.
            """

class ExportFileOptions2:
    """
    
            This structure contains the information of the export option for a file object which
            is to be exported in the staging directory.
            
    """
    def __init__(self, ) -> None: ...
    IsAutoProcessSelected: bool
    """
            If true, the auto process is selected for file export and autoProcessOption
            is used for export action; otherwise, promptUserOptions is used for export
            action.
            """
    AutoProcessOption: str
    PromptUserOptions: list[ExportFilePromptUserOption2]
    """A list of export options for file object from a prompt user action."""

class ExportFilePromptUserOption2:
    """
    
            This structure contains the information of the export option for a file object from
            prompt user action which is to be exported in the staging directory.
            
    """
    def __init__(self, ) -> None: ...
    FileObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            File object which is to be exported in the staging directory. The supported object
            is ImanFile.
            """
    ExportOption: str

class ImportConfigRuntimeOverrideInfo3:
    """
    This structure holds runtime overrides for Simulation Tool output configuration.
    """
    def __init__(self, ) -> None: ...
    ItemCreationSetting: str
    DatasetCreationSetting: str
    """
Dataset creation option. Supported values are: "As_Needed", "Always" or "Never".
            This parameter is optional. If no value is provided, the default value configured
            in the Simulation Tool will be used. These Dataset creation options works
            similarly to the Item creation options
            """
    AutoProcessOptions: str
    OutputNamePatterns: list[str]

class LaunchInputInfo4:
    """
    
            This structure contains the input object for which the tool needs to be launched
            and the configuration information which needs to be applied in case the input object
            is of type ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """Input object on which Simulation Tool is to be launched."""
    InputDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            A Dataset on which Simulation Tool is to be launched. To launch a Simulation
            Tool, the user selects the ItemRevision on which the Simulation Tool is to
            be launched. This inputDataset is the Dataset attached to this selected
            ItemRevision. If the selected ItemRevision has multiple datasets of
            the same type, then a conflict resolution dialog is presented to the user to pick
            the appropriate Dataset and proceed with the Simulation Tool Launch.
            """
    InputFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    """The file on which Simulation Tool is to be launched."""
    InputWebLink: Teamcenter.Soa.Client.Model.Strong.Form
    """
            A Web Link on which Simulation Tool is to be launched. To launch a Simulation
            Tool, the user selects the ItemRevision on which the Simulation Tool is to
            be launched. This inputWebLink is the Web Link attached to this selected
            ItemRevision. If the selected ItemRevison has multiple web links, then
            a conflict resolution dialog is presented to the user to pick the appropriate Web
            Link and proceed with the Simulation Tool Launch.
            """
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            A ConfigurationContext object holding the configuration details for the Input
            object.
            """

class OptionalInputInfo2:
    """
    
            This structure contains the ItemRevision object and directory name where the
            named references from the ItemRevision object will be exported.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
ItemRevision object whose named references are to be exported during simulation
            tool launch operation.
            """
    ExportDirectory: str
    """
            Name of the directory where the named references from Optional Input will be exported.
            This is name of the directory which will be created inside scratchDirectory
            or userStagingDir if it is configured and the named references from inputObject
            will be exported to. If no value is provided, then the named references from Optional
            Input will be exported to scratchDirectory or userStagingDir if it
            is configured on Simulation Tool.
            """

class SimulationToolLaunch:
    """
    Interface SimulationToolLaunch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[LaunchInputInfo4], ScratchDirectory: str, UserStagingLocation: str, UserStagingDir: str, LaunchType: str, ExportRuntimeConfiguration: ExportConfigRuntimeOverrideInfo2, ImportRuntimeConfiguration: ImportConfigRuntimeOverrideInfo3, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext], OptionalInputInfo: list[OptionalInputInfo2], FileExportOptions: list[ExportFileOptions2], HpcConnectionObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...

