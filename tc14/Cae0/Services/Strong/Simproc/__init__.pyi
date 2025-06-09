import Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch
import Cae0.Services.Strong.Simproc._2015_10.SimProcessConfigurationManagement
import Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch
import Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement
import Cae0.Services.Strong.Simproc._2017_11.SimulationToolLaunch
import Cae0.Services.Strong.Simproc._2020_01.SimulationToolLaunch
import Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SimProcessConfigurationManagementRestBindingStub(SimProcessConfigurationManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetToolTabProperties(self, InputItemTypes: list[str], TabIdentifiers: list[str], LaunchTypes: list[str]) -> Cae0.Services.Strong.Simproc._2015_10.SimProcessConfigurationManagement.ToolTabsInfo: ...

class SimProcessConfigurationManagementService:
    """
    
            This service contains the SOAs for creation, update, clone, delete, paste, revise
            and release operations on the tool objects and the tab objects associated with them.
            This is also used to retrieve the CAE Configuration objects and get the simulation
            dashboard data from the dashboard configuration objects.
            


Library Reference:

CAE0SoaSimProcStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimProcessConfigurationManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetToolTabProperties(self, InputItemTypes: list[str], TabIdentifiers: list[str], LaunchTypes: list[str]) -> Cae0.Services.Strong.Simproc._2015_10.SimProcessConfigurationManagement.ToolTabsInfo:
        """    
             This operation returns a list of structures having tab information for Simulation
             Tools provided the input item types, required tab identifiers, user name, role and
             group.
             
             The operation fetches the configurations for all tabs from input tab identifiers
             for all tools and then applies constraints to this list as per the logged in user/role/group
             access restrictions, input item configuration being same as the provided input item
             types and configured launch types being same as provided launch types.
             

Use Cases:

Use Case1


             User selects a CAE 3D Model item revision and clicks on Launch Simulation Tools command
             icon in active workspace.
             
             User sees a command panel populated with list of Simulation Tool names list which
             have primary input type configured as CAE 3D Model , have Local launch as configured
             launch type and have enabled the access to logged in user's name/group/role.
             

Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param InputItemTypes: 
                         Input item type names for which Simulation Tools are to be fetched. Support type
                         names are: ItemRevision, CAEModelRevision, and CAEAnalysisRevision.
             
        :param TabIdentifiers: 
<ul>
<li type="disc">CAE0General
                         </li>
<li type="disc">CAE0LaunchParameters
                         </li>
<li type="disc">CAE0EnvVariables
                         </li>
<li type="disc">CAE0InputConfiguration
                         </li>
<li type="disc">CAE0OutputConfiguration
                         </li>
<li type="disc">CAE0InputParameters
                         </li>
<li type="disc">CAE0AttributeConfiguration
                         </li>
<li type="disc">CAE0AccessControl
                         </li>
<li type="disc">CAE0Feedback
                         </li>
</ul>

        :param LaunchTypes: 
<ul>
<li type="disc">cae0LocalLaunch
                         </li>
<li type="disc">cae0LocalDetachedLaunch
                         </li>
<li type="disc">cae0RemoteLaunch
                         </li>
<li type="disc">cae0ServerLaunch
                         </li>
</ul>

        :return: 
        """
        ...

class SimProcessStatusManagementRestBindingStub(SimProcessStatusManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateSimProcessStatus(self, Attributes: list[str], Values: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteSimProcessStatus(self, JobIds: list[str]) -> bool: ...
    def GetSimProcessStatus(self, Attribute: str, Value: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UpdateSimProcessStatus(self, JobID: str, Attributes: list[str], Values: list[str]) -> bool: ...

class SimProcessStatusManagementService:
    """
    
            The SimPorcessStatusManagement service provides operations to create and manage the
            Simulation Process Status objects.
            


Library Reference:

CAE0SoaSimProcStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimProcessStatusManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateSimProcessStatus(self, Attributes: list[str], Values: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The simulation tool launch feature in CAE Manager application supports a progress
             monitor dialog with persistent status management objects. These objects are maintained
             in the database for each simulation tool launch job initiated by a user.
             

             This operation supports creation of the CAE0SimProcessStatus object from the
             client side with necessary parameters and conditions. The cae0JobId
             attribute will be populated on the newly created object with a unique string with
             current time stamp appended to it. This operation will be used by the client whenever
             the user launches the simulation tool and selects to view the progress monitor for
             the launched tool.
             


Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param Attributes: 

        :param Values: 

        :return: 
        """
        ...
    def DeleteSimProcessStatus(self, JobIds: list[str]) -> bool:
        """    
             The simulation tool launch feature in CAE Manager application supports a progress
             monitor dialog with a persistent status management object which will be maintained
             in the database.
             

             This operation removes the corresponding CAE0SimProcessStatus objects from
             datatbase for the given job IDs.
             



Use Cases:

             The progress monitor will display status for all the jobs initiated by a user. However,
             once the job is finished, user may not need its status  tracked on progress monitor.
             Such jobs can be deleted from database using this operation Deleted job attributes
             will no longer apprear on the progress monitor after this operation is completed.
             



Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param JobIds: 

        :return: 
        """
        ...
    def GetSimProcessStatus(self, Attribute: str, Value: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The simulation tool launch feature in CAE Manager application supports a progress
             monitor dialog with a persistent status management object which is maintained in
             the database for each simulation tool launched by the user.
             

             This operation fetches  CAE0SimProcessStatus objects from database that match
             the attribute-value provided as input argument.
             

Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param Attribute: 

        :param Value: 

        :return: 
        """
        ...
    def UpdateSimProcessStatus(self, JobID: str, Attributes: list[str], Values: list[str]) -> bool:
        """    
             The simulation tool launch feature in CAE Manager application supports a progress
             monitor dialog with persistent status management object which are maintained in the
             database for every simulation tool launch job initiated by a user.
             

             The status object CAE0SimProcessStatus, which will be created during the launch
             of the simulation tool launch will need to be updated at different stages of tool
             launch. This operation updates the attributes such as status, last upload date, finish
             time and the last working directory of the CAE0SimProcessStatus object for
             a given simulation tool launch job.
             


Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param JobID: 
                         The unique job ID of the <b>CAE0SimProcessStatus</b> object to be updated.
             
        :param Attributes: 

        :param Values: 

        :return: False - if the attributes updated fails for the status object.
        """
        ...

class SimStructureManagementRestBindingStub(SimStructureManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExecuteStructureMap(self, StructureMapInputs: Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapInputsInfo) -> Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapExecutionResponse: ...

class SimStructureManagementService:
    """
    
            This class holds the operations for the CAE Simulation Module functionality. All
            the TcSim Structure Management related operations should be added to this class.
            

Dependencies:

            SimStructureManagement
            


Library Reference:

CAE0SoaSimProcStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimStructureManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExecuteStructureMap(self, StructureMapInputs: Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapInputsInfo) -> Cae0.Services.Strong.Simproc._2017_05.SimStructureManagement.StructureMapExecutionResponse:
        """    
             This operation creates an output BOM structure given the root ItemRevision
             of the root BOMLine of an input BOM structure along with its RevisionRule
             and the VariantRule. A Snapshot folder of the input BOM structure along
             with the VariantRule can also be provided as an input. The output BOM structure
             is determined by the XSLT-based Data Map rules executed against the input
             BOM structure. Data Map syntax is in compliance with the schema defined in
             tcsim_xslWithNode.xsd, located in TC_DATA.
             

Data Map rules define the mapping between an input item type and its resulting
             output item type. Data Map rules are defined for an entire site and are stored
             in the datamapping.xml file located in TC_DATA. The name of the datamapping
             file is defined by the site preference CAE_dataMapping_file.
             

             The Data Map rules can be configured for various domains defined as LOV objects
             under StructureMap Domains in BMIDE. To configure the domains, in the Extensions
             view in BMIDE, open LOV->StructureMap Domains and add additional domain
             values. The domain to be used for applying Data Map rules can also be provided
             as an input.
             

             To use this operation, a well-defined datamapping.xml is required in TC_DATA
             and the user should have either a simulation_author or rtt_author license.
             

             This service operation calls asynchronous service operation internlly to execute
             Datamap with the given parameters.
             

Use Cases:

             A user can asynchronously execute StructureMap function in ActiveWorkspace Client
             using an existing opened Product structure. Subsequently CAEModel structure
             and a relation are created between newly created CAEModel structure and the
             selected  Product Structure.
             
             Use Case 1: Open a Product structure, select root ItemRevision and internally
             call operation to execute StructureMap asynchronously.
             

             Use Case 2: Open a Product structure, apply revision and variant configurations on
             that structure and internally call operation to execute StructureMap asynchronously.
             

Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param StructureMapInputs: 
                         A structure holding inputs for executeStructureMap operation.
             
        :return: 206679 - Mapped BOMView Type does not exist, creating default view type.
        """
        ...

class SimulationToolLaunchRestBindingStub(SimulationToolLaunchService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.LaunchInputInfo], WorkingDirectory: str, LaunchType: str, ExportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.LaunchInputInfo2], WorkingDirectory: str, LaunchType: str, ExportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.LaunchInputInfo2], WorkingDirectory: str, LaunchType: str, ExportRunTimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext], OptionalInputInfo: list[Cae0.Services.Strong.Simproc._2017_11.SimulationToolLaunch.OptionalInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2020_01.SimulationToolLaunch.LaunchInputInfo3], ScratchDirectory: str, UserStagingLocation: str, UserStagingDir: str, LaunchType: str, ExportRunTimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext], OptionalInputInfo: list[Cae0.Services.Strong.Simproc._2017_11.SimulationToolLaunch.OptionalInputInfo], FileExportOptions: list[Cae0.Services.Strong.Simproc._2020_01.SimulationToolLaunch.ExportFileOptions]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.LaunchInputInfo4], ScratchDirectory: str, UserStagingLocation: str, UserStagingDir: str, LaunchType: str, ExportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo2, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo3, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext], OptionalInputInfo: list[Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.OptionalInputInfo2], FileExportOptions: list[Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.ExportFileOptions2], HpcConnectionObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class SimulationToolLaunchService:
    """
    
            This service provides functionalities related to launch of Simulation Tool.
            


Library Reference:

CAE0SoaSimProcStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimulationToolLaunchService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.LaunchInputInfo], WorkingDirectory: str, LaunchType: str, ExportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.LaunchInputInfo2], WorkingDirectory: str, LaunchType: str, ExportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.LaunchInputInfo2], WorkingDirectory: str, LaunchType: str, ExportRunTimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext], OptionalInputInfo: list[Cae0.Services.Strong.Simproc._2017_11.SimulationToolLaunch.OptionalInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2020_01.SimulationToolLaunch.LaunchInputInfo3], ScratchDirectory: str, UserStagingLocation: str, UserStagingDir: str, LaunchType: str, ExportRunTimeConfiguration: Cae0.Services.Strong.Simproc._2014_12.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2016_05.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo2, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext], OptionalInputInfo: list[Cae0.Services.Strong.Simproc._2017_11.SimulationToolLaunch.OptionalInputInfo], FileExportOptions: list[Cae0.Services.Strong.Simproc._2020_01.SimulationToolLaunch.ExportFileOptions]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ExecuteSimulationToolLaunch(self, SimulationTool: Teamcenter.Soa.Client.Model.ModelObject, InputObjects: list[Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.LaunchInputInfo4], ScratchDirectory: str, UserStagingLocation: str, UserStagingDir: str, LaunchType: str, ExportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.ExportConfigRuntimeOverrideInfo2, ImportRuntimeConfiguration: Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.ImportConfigRuntimeOverrideInfo3, PedigreeCaptureInfo: list[Teamcenter.Soa.Client.Model.Strong.StructureContext], OptionalInputInfo: list[Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.OptionalInputInfo2], FileExportOptions: list[Cae0.Services.Strong.Simproc._2023_06.SimulationToolLaunch.ExportFileOptions2], HpcConnectionObject: Teamcenter.Soa.Client.Model.Strong.CAE0ConfigRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...

