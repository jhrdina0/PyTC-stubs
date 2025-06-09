import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExportConfigRuntimeOverrideInfo:
    """
    Structure holding runtime overrides for Simulation Tool export configuration.
    """
    def __init__(self, ) -> None: ...
    PlmxmlExportFileName: str
    """
            Name of the PLMXML file to be exported. This is optional. If no value is provided,
            file name specified in the Simulation Tool configuration will be used.
            """
    RuntimeArguments: list[str]
    """
            List of runtime arguments and their values. The argument and values are represented
            by a single string.  The values will be separated by two colons "::"  which is converted
            to the "=" equals sign.  Arguments that have no value are represented by blank or
            white space.  Argument will be prefixed by a single dash "-".  Example: To pass the
            argument and value pairs of as an argument, the user should pass "fem::3D dat::blk"
            as a string list. This will result in the following argumets "-fem=3D -dat=blk".
            This is optional.
            """

class ImportConfigRuntimeOverrideInfo:
    """
    Structure holding runtime overrides for Simulation Tool ouput configuration.
    """
    def __init__(self, ) -> None: ...
    ItemCreationSetting: str
    """
            Item creation flag, which can be take one of the following values - "As_Needed",
            "Always" or "Never". This parameter is optional. If no value is provided, default
            value configured in the Simulation Tool will be used.
            """
    DatasetCreationSetting: str
    """
            Dataset creation flag, which can be take one of the following values - "As_Needed",
            "Always" or "Never". This parameter is optional. If no value is provided, default
            value configured in the Simulation Tool will be used.
            """
    OutputNamePatterns: list[str]
    """
            Specifies the naming pattern for the created Items. The argument and values are represented
            by a single string separated by token "::" Example: To pass AnalysisObject naming
            patterns for objects of type CAEAnalysis as an argument, the user should pass [CAEAnalysis::AnalysisObject]
            as a string vector. This is an optional argument.
            """

class LaunchInputInfo:
    """
    
            Structure containing the input object on which tool needs to be launched and the
            configuration information which needs to be applied in case the input object is of
            type ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """Input object on which Simulation Tool is to be launched."""
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
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[LaunchInputInfo], WorkingDirectory: str, LaunchType: str, ExportRuntimeConfiguration: ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: ImportConfigRuntimeOverrideInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation launches the Simulation Tool as per the pre-defined configuration.
             The configuration contains details about the tool launch type, export and import
             rules for the files, notification, and cleanup. The inputs to the operation is an
             array of InputObjectStructure, each containing one or more business objects, name
             of the tool to be launched and the launch type. Based on the input values of parameters
             itemCreationSetting and datasetCreationSetting, ItemRevision and Dataset objects
             are created or modified.
             
             It is a pre-requisite that the Simulation Administrator or user with DBA privileges
             must configure the Simulation Tool in CAEManager application of Teamcenter. To use
             this operation, the user should have either a simulation_author or rtt_author license.
             

Use Cases:

             Use Case 1: Import Simulation Objects with As Needed Item Creation Setting.
             
             When executed with itemCreationSetting as "As_Needed", no new Item will be created
             if there exists one as per the Simulation Tool output configuration. If found none,
             new Item will be created as per the Simulation Tool output configuration.
             

             Use Case 2: Import Simulation Objects with Always Item Creation Setting.
             
             When executed with itemCreationSetting as "Always", new Item will be created as per
             the Simulation Tool output configuration.
             

             Use Case 3: Import Simulation Objects with Never Item Creation Setting.
             
             When this operation is executed with itemCreationSetting as "Never" and if no existing
             Item is found as per the Simulation Tool output configuration, no new Item will be
             created.
             

             Use Case 4: Import Simulation Objects with As Needed Dataset Creation Setting.
             
             When executed with datasetCreationSetting as "As_Needed", no new Dataset will be
             created if there exists one as per the Simulation Tool output configuration. If found
             none, new Dataset will be created as per the Simulation Tool output configuration.
             

             Use Case 5: Import Simulation Objects with Always Dataset Creation Setting.
             
             When executed with datasetCreationSetting as "Always", new Dataset will be created
             as per the process Simulation Tool configuration.
             

             Use Case 6: Import Simulation Objects with Never Dataset Creation Setting.
             
             When executed with datasetCreationSetting as "Never" and if no existing Dataset is
             found as per the process output configuration, no new Dataset will be created.
             

Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param SimulationTool: 
                         Simulation Tool to be launched.
             
        :param InputObjects: 
                         Array of LaunchInputInfo
             
        :param WorkingDirectory: 
                         Working directory of the Simulation Tool
             
        :param LaunchType: 
                         Launch type for the process. Valid values are "LOCAL", "REMOTE", "SERVER", "LOCAL_DETACHED".
             
        :param ExportRuntimeConfiguration: 
                         ExportRuntimeOverrideInfo constaining runtime overrides for export configuration
                         of Simulation Tool.
             
        :param ImportRuntimeConfiguration: 
                         ImportRuntimeOverrideInfo constaining runtime overrides for export configuration
                         of Simulation Tool.
             
        :return: 
        """
        ...

