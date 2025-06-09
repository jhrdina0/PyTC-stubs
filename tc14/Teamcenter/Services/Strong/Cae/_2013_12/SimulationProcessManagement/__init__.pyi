import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class InputObjectData:
    """
    
            Structure containing the input object on which tool needs to be launched and the
            configuration information which needs to be applied in case the input object is of
            type ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The business object on which configured tool needs to be launched."""
    ConfigCntx: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Object holding the configuration information that needs to be applied on the input
            object if it is of type ItemRevision.
            """

class InputObjectsStructure2:
    """
    
            Structure containing selected input object data on which pre-configured simulation
            tool needs to be launched.
            
    """
    def __init__(self, ) -> None: ...
    InputObjectDataVec: list[InputObjectData]
    """
            Array of InputObjectData on which pre-configured simulation tool needs to
            be launched.
            """

class SimulationProcessManagement:
    """
    Interface SimulationProcessManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def LaunchSimulationTool2(self, InputObjects: list[InputObjectsStructure2], ToolName: str, LaunchType: str, ItemCreationOption: str, DatasetCreationOption: str, PlmxmlExportFileName: str, WorkingDirectory: str, RuntimeArguments: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation launches the simulation tool as per the pre-defined configuration.
             The configuration contains details about the tool launch type, export and import
             rules for the files, notification, and cleanup. The inputs to the operation is an
             array of InputObjectStructure2, each containing one or more business objects,
             name of the tool to be launched and the launch type. The launch type could be LOCAL
             or REMOTE. Based on the input values of parameters itemCreationOption
             and datasetCreationOption, ItemRevision and Dataset objects
             are created or modified.
             

             It is a pre-requisite that the Simulation Administrator or user with DBA
             privileges must configure the simulation tool and store it in XML format as
             a named reference with the Dataset name specified in the preference CAE_simulation_tool_config_dsname.
             

             To use this operation, the user should have either a simulation_author or
             rtt_author license.
             


Use Cases:

             Use Case 1: Launch Simulation Tool with As Needed Item Creation Option

             When this operation is executed with itemCreationOption "As Needed",
             no new Teamcenter Item will be created if there exists one as per the process
             output configuration. If found none, new Item will be created as per the process
             output configuration.
             

             Use Case 2: Launch Simulation Tool with Always Item Creation Option

             When this operation is executed with itemCreationOption "Always", new
             Teamcenter Item objects will be created as per the process output configuration.
             

             Use Case 3: Launch Simulation Tool with Never Item Creation Option

             When this operation is executed with itemCreationOption "Never" and
             if no existing Item is found as per the process output configuration, no new
             Teamcenter Item objects will be created.
             

             Use Case 4: Launch Simulation Tool with As Needed Dataset Creation Option

             When this operation is executed with datasetCreationOption "As Needed",
             no new Teamcenter Dataset will be created if there exists one as per the process
             output configuration. If found none, new Dataset will be created as per the
             process output configuration.
             

             Use Case 5: Launch Simulation Tool with Always Dataset Creation Option

             When this operation is executed with datasetCreationOption "Always",
             new Teamcenter Dataset objects will be created as per the process output configuration.
             

             Use Case 6: Launch Simulation Tool with Never Dataset Creation Option

             When this operation is executed with datasetCreationOption "Never"
             and if no existing Dataset is found as per the process output configuration,
             no new Teamcenter Dataset objects will be created.
             


Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param InputObjects: 
                         Array of <i>InputObjectsStructure2</i>, each containing array of <i>InputObjectData</i>
                         which are processed as inputs to the tool.
             
        :param ToolName: 
                         The simulation process including the complete inheritance hierarchy. The "::" should
                         be used to create the string for processes having inheritance.
             
        :param LaunchType: 
                         Launch type for the process. This can be either "<i>LOCAL</i>" or "<i>REMOTE</i>".
             
        :param ItemCreationOption: 
                         Specifies Item creation option. It can be either "<i>As Needed</i>", "<i>Always</i>"
                         or "<i>Never</i>". This parameter is optional. If no value is provided, default Item
                         creation setting in the process configuration will be used.
             
        :param DatasetCreationOption: 
                         Specifies Dataset creation option. It can be either "<i>As Needed</i>", "<i>Always</i>"
                         or "<i>Never</i>". This parameter is optional. If no value is provided, default Dataset
                         creation setting in the process configuration will be used.
             
        :param PlmxmlExportFileName: 
                         Name of the PLMXML file to be exported the simulation tool launch framework. This
                         is optional. If no value is provided, file name specified in the process configuration
                         will be used.
             
        :param WorkingDirectory: 
                         The directory where the current job runs and generates the output files.
             
        :param RuntimeArguments: 
                         List of runtime arguments and their values. The argument and values are represented
                         by a single string separated by token "::" Example: To pass -fem -dat=blk as an argument,
                         the user should pass [fem::, dat::blk] as a string vector. This is optional.
             
        :return: 
        """
        ...

