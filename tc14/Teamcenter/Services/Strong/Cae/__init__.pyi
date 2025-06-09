import System
import Teamcenter.Services.Strong.Cae._2012_02.StructureManagement
import Teamcenter.Services.Strong.Cae._2013_12.SimulationProcessManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class SimulationProcessManagementRestBindingStub(SimulationProcessManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def LaunchSimulationTool2(self, InputObjects: list[Teamcenter.Services.Strong.Cae._2013_12.SimulationProcessManagement.InputObjectsStructure2], ToolName: str, LaunchType: str, ItemCreationOption: str, DatasetCreationOption: str, PlmxmlExportFileName: str, WorkingDirectory: str, RuntimeArguments: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class SimulationProcessManagementService:
    """
    
            The SimulationProcessManagement service provides operations for launching
            simulation tools that can include preprocessors, solvers, postprocessors, and other
            tools to perform custom actions. It is pre-requisite that the Simulation Administrator
            or user with DBA privileges must configure the simulation tool and store it
            in XML format as a named reference with the Dataset name specified
            in the preference CAE_simulation_tool_config_dsname.
            
            The SimulationProcessManagement service provides following operations:
            

Launching pre-configured simulation tool



            The launchSimulationTool operation will launch the simulation tool as per
            the pre-defined configuration on the given input ItemRevision objects. The
            configuration contains details about the tool launch type (local or remote), rules
            to navigate from the primary input object to the output object through a combination
            of relationships, output objects (ItemRevision and Dataset) creation
            settings, and naming pattern for each of the output objects (Item, ItemRevision,
            or Dataset) that are created during the tool launch. Temporary files that
            are created during simulation tool launch will be stored in the specified output
            directory.
            

Importing simulation tool launch output data in Teamcenter



            The importSimulationObjects operation is an internal operation to import the
            output files generated from the execution of simulation tool launch process into
            Teamcenter objects (Item, ItemRevision, and Dataset). The output
            files will be picked from the specified output directory and based on the pre-configured
            output rules and ItemRevision and Dataset creation settings; they will
            be imported as Teamcenter objects.
            

Notifying the pre-configured users by sending e-mail notifications
            after execution of simulation tool launch



            The notifyUser operation is an internal operation to notify the users and
            groups specified in the simulation tool configuration after execution of simulation
            tool launch by sending e-mail notifications. The notification will contain the details
            of the launch relative to its success or failure and will also contain information
            about the newly created objects if any.
            


Library Reference:

TcSoaCaeStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SimulationProcessManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def LaunchSimulationTool2(self, InputObjects: list[Teamcenter.Services.Strong.Cae._2013_12.SimulationProcessManagement.InputObjectsStructure2], ToolName: str, LaunchType: str, ItemCreationOption: str, DatasetCreationOption: str, PlmxmlExportFileName: str, WorkingDirectory: str, RuntimeArguments: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
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

class StructureManagementRestBindingStub(StructureManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExecuteDatamap(self, RootIR: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SnapshotFolder: Teamcenter.Soa.Client.Model.Strong.Snapshot, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule, Domain: str) -> Teamcenter.Services.Strong.Cae._2012_02.StructureManagement.ExecuteRuleResponse2: ...
    def ExecuteStructureMap(self, RootIR: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SnapshotFolder: Teamcenter.Soa.Client.Model.Strong.Snapshot, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule, StructureMapIR: Teamcenter.Soa.Client.Model.Strong.StructureMapRevision) -> Teamcenter.Services.Strong.Cae._2012_02.StructureManagement.ExecuteRuleResponse2: ...

class StructureManagementService:
    """
    
            The StructureManagement service provides operations to create and manage the
            Computer Aided Engineering (CAE) structures. Given an input BOM structure, the output
            BOM structure is determined by a combination of XSLT-based Data Map and StructureMap
rules executed against the input BOM structure.
            

Data Map rules define the mapping between an input item type and its resulting
            output item type. Data Map rules are defined for an entire site and are stored
            in the datamapping.xml file located in TC_DATA.
            

StructureMap rules tailor the output BOM Structure. There are several rule
            types:
            

Filter - Removes input BOMLine objects (and their children)
            from Data Map evaluation.
            
Include - Inserts ItemRevision objects in either the input
            or the output BOM structure as required.
            
Reuse - Retrieve existing ItemRevision to be used in the output
            structure.
            
Create collector - Reorganization rule that creates "container" ItemRevision
            objects to move BOMLine objects and sub-assemblies around.
            
Move to Collector - Reorganization rule that moves BOMLine
            objects and sub-assemblies to collector components.
            
Collapse Single Component Assembly - Identifying sub-assemblies with
            a single child component, elevating the child component to the parent sub-assembly
            and removing the parent sub-assembly.
            
Remove Empty Assembly - Identifying sub-assemblies with no child
            components and removing the empty sub-assembly.
            
Skip - Skips a BOMLine but still process their children.
            



            For more details on building and executing Data Map and StructureMap rules,
            please refer to the "Creating StructureMap rules" section in the Simulation
            Process Management Guide->Using StructureMaps chapter of the Teamcenter documentation.
            

            The operations in this service allow the creation and reorganization of output BOM
            structure by applying Data Map and StructureMap rules. This service
            also provides operations to generate a NodeXML for selected BOMLine
            object(s). NodeXML is XML-based and is most commonly used in the process of
            creating Data Map and StructureMap rules. The generated NodeXML
            consists of the visible attributes and their values associated with the Item,
            ItemRevision, related Form objects and the BOMLine.
            

            The StructureManagement service can be used for supporting following use-cases:
            

Create an output BOM structure by applying Data Map rules,
            given a root BOMLine of the input BOM structure along with its configuration.
            
Create an output BOM structure by applying Data Map rules
            given a Snapshot folder of the input BOM structure and its VariantRule.
            
Create an output BOM structure by applying Data Map and StructureMap
            rules, given a root BOMLine of the input BOM structure along with its
            configuration.
            
Create an output BOM structure by applying Data Map and StructureMap
            rules given a Snapshot folder of the input BOM structure and its VariantRule.
            
Generate a NodeXML for selected BOMLine object(s) and
            a selected CAEStructureMap Domain LOV defined in BMIDE.
            To configure the domains, in the Extensions view in BMIDE, open LOV->StructureMap
            Domains and add additional domain values.
            




Library Reference:

TcSoaCaeStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExecuteDatamap(self, RootIR: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SnapshotFolder: Teamcenter.Soa.Client.Model.Strong.Snapshot, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule, Domain: str) -> Teamcenter.Services.Strong.Cae._2012_02.StructureManagement.ExecuteRuleResponse2:
        """    
             This operation creates an output BOM structure given the root ItemRevision
             of the root BOMLine of an input BOM structure along with its RevisionRule
             and the VariantRule. A Snapshot folder of the input BOM structure along
             with the VariantRule can also be provided as an input. The output BOM structure
             is determined by the XSLT-based Data Map rules executed against the
             input BOM structure. Data Map syntax is in compliance with the schema defined
             in tcsim_xslWithNode.xsd, located in TC_DATA.
             

Data Map rules define the mapping between an input item type and its resulting
             output item type. Data Map rules are defined for an entire site and are stored
             in the datamapping.xml file located in TC_DATA. The name of the datampping
             file is defined by the site preference CAE_dataMapping_file.
             

             The Data Map rules can be configured for various domains defined as LOV
             objects under StructureMap Domains in BMIDE. To configure the domains,
             in the Extensions view in BMIDE, open LOV->StructureMap Domains
             and add additional domain values. The domain to be used for applying Data Map
             rules can also be provided as an input.
             

             To use this operation, a well-defined datamapping.xml is required in TC_DATA
             and the user should have either a simulation_author or rtt_author license.
             


Use Cases:

             Use Case 1: Create an output structure given a top BOMLine of the input structure
             along with its configuration

             Given an input root BOMLine of a BOM structure, along with its RevisionRule
             and VariantRule, the user can apply Data Map rule to the BOM structure
             and generate a corresponding output BOM structure. The output BOM structure would
             consist of BOMLine occurrences of ItemRevision objects as defined in
             the datamapping.xml file. The user can review the actions executed with the
             process log returned with the BOMViewRevision. An email notification containing
             the activity log would be sent to the current user if the session option for email
             notification is set to true.
             

             Use Case 2: Create an output structure given a Snapshot folder of the input structure
             along with the variant rule

             Given a Snapshot folder of the input BOM structure and its VariantRule,
             the user can apply Data Map rules to the BOM structure and generate a corresponding
             output BOM structure. The output BOM structure would consist of BOMLine occurrences
             of ItemRevision objects as defined in the datamapping.xml file. The
             user can review the actions executed with the process log returned with the BOMViewRevision.
             An email notification containing the activity log would be sent to the current user
             if the session option for email notification is set to true.
             


Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param RootIR: 
<b>ItemRevision</b> of the root item of the input structure. This can be null if
                         the <i>snapshotFolder</i> is provided as input to the operation. If the <i>rootIR</i>
                         is not null and <i>snapshotFolder</i> is also provided as an input, then <i>rootIR</i>
                         input will be ignored and <i>snapshotFolder</i> will take precedence.
             
        :param SnapshotFolder: 
                         The <b>Snapshot</b> folder of the input structure. The <i>snapshotFolder</i> can
                         be null if the root <i>rootIR</i> is used as an input to the operation. The <i>snapshotFolder</i>
                         takes precedence over the <i>rootIR</i>.
             
        :param RevRule: 
                         The <b>RevisionRule</b> of the input structure. This is an optional parameter and
                         can be provided if the root <b>ItemRevision</b> is used as an input to the operation.
                         This parameter will be ignored if <i>snapshotFolder</i> is used as an input.
             
        :param VariantRule: 
                         The <b>VariantRule</b> for the input structure. This can be provided for both, the
                         <i>rootIR</i> or <i>snapshotFolder</i> as input. This is an optional parameter and
                         can be null.
             
        :param Domain: 
                         The domain for the <i>Data Map rules</i> to be applied. The <i>datamapping.xml</i>
                         file can be configured for various domains defined as <b>LOV</b> objects under <b>StructureMap
                         Domains</b> in <i>BMIDE</i>. This argument is used to specify which domain to be
                         used from the <i>datamapping.xml</i> file. If the value is not provided, the default
                         is assumed to be <b>CAE</b>.
             
        :return: . Any failures in creation of the output item or
             relationships are also returned as a part of the activity log.
        """
        ...
    def ExecuteStructureMap(self, RootIR: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SnapshotFolder: Teamcenter.Soa.Client.Model.Strong.Snapshot, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule, StructureMapIR: Teamcenter.Soa.Client.Model.Strong.StructureMapRevision) -> Teamcenter.Services.Strong.Cae._2012_02.StructureManagement.ExecuteRuleResponse2:
        """    
             This operation creates an output BOM structure given the root ItemRevision
             of the root BOMLine of an input BOM structure along with its RevisionRule
             and the VariantRule. A Snapshot folder of the input BOM structure along
             with the VariantRule can also be provided as an input. The output BOM structure
             is determined by a combination of XSLT-based Data Map and StructureMap
             rules executed against the input BOM structure. Data Map/StructureMap
             syntax is in compliance with the schema defined in tcsim_xslWithNode.xsd,
             located in TC_DATA.
             

Data Map rules define the mapping between an input item type and its resulting
             output item type. Data Map rules are defined for an entire site and are stored
             in the datamapping.xml file located in TC_DATA. The name of the data
             mapping file is defined by the site preference CAE_dataMapping_file.
             

StructureMap rules tailor the output BOM Structure. There are several rule
             types:
             

Filter - Removes input BOM lines (and their children) from Data
             Map evaluation.
             
Include - Inserts item revisions in either the input or output BOM
             structure as required.
             
Reuse - Retrieve existing item revision to be used in the output
             structure.
             
Create Collector - Reorganization rule that creates "container" item
             revisions to move BOMLine objects and sub-assemblies around.
             
Move to Collector - Reorganizational rule that moves BOMLine
             objects and sub-assemblies to collector components.
             
Collapse Single Component Assembly - Identifying sub-assemblies with
             single child component, elevating the child component to the parent sub-assembly
             and removing the parent sub-assembly.
             
Remove Empty Assembly - Identifying sub-assemblies with no child
             components and removing the empty sub-assembly.
             
Skip - Skips the BOMLine but still process its children.
             



StructureMap rules are stored an XML named reference in CAEStructureMap
             dataset attached to a StructureMapRevision. StructureMap rules are
             created with Simulation Process Management CAE Structure Designer.
             

             To use this operation, a well-defined datamapping.xml is required in TC_DATA
             and a StructureMapRevision with an attached CAEStructureMap dataset
             must exist and the user should have either a simulation_author or rtt_author
license.
             

Use Cases:

             Use Case 1:
             
             Given an input root BOMLine of a BOM structure, along with its RevisionRule
             and VariantRule, the user can apply a StructureMap rule to the BOM
             structure and generate a corresponding output BOM structure. The output BOM structure
             would consist of BOMLine occurrences of ItemRevision objects as defined
             in the datamapping.xml file and would be organized by the StructureMap
             rules defined in the CAEStructureMap dataset attached to the StructureMapRevision.
             The user can review the actions executed with the process log returned with the BOMViewRevision.
             An email notification containing the activity log would be sent to the current user
             if the session option for email notification is set to true.
             

             Use Case 2:
             
             Given a Snapshot folder of the input BOM structure and its VariantRule,
             the user can apply a StructureMap rule to the BOM structure and generate a
             corresponding output BOM structure. The output BOM structure would consist of BOMLine
             occurrences of ItemRevision objects as defined in the datamapping.xml
             file and would be organized by the StructureMap rules defined in the CAEStructureMap
             dataset attached to the StructureMapRevision. The user can review the actions
             executed with the process log returned with the BOMViewRevision. An email
             notification containing the activity log would be sent to the current user if the
             session option for email notification is set to true.
             


Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param RootIR: 
                         The <b>ItemRevision</b> of the root item of the input structure. This can be null
                         if the <i>snapshotFolder</i> is provided as input to the operation. If the <i>rootIR</i>
                         is not null and <i>snapshotFolder</i> is also provided as an input, then <i>rootIR</i>
                         input will be ignored and <i>snapshotFolder</i> will take precedence.
             
        :param SnapshotFolder: 
                         The <b>Snapshot</b> folder of the input structure. The <i>snapshotFolder</i> can
                         be null if the root <i>rootIR</i> is used as an input to the operation. The <i>snapshotFolder</i>
                         takes precedence over the <i>rootIR</i>.
             
        :param RevRule: 
                         The <b>RevisionRule</b> of the input structure. This is an optional parameter and
                         can be provided if the root <b>ItemRevision</b> is used as an input to the operation.
                         This parameter will be ignored if <i>snapshotFolder</i> is used as an input.
             
        :param VariantRule: 
                         The <b>VariantRule</b> for the input structure. This can be provided for both, the
                         <i>rootIR</i> or <i>snapshotFolder</i> as input. This is an optional parameter and
                         can be null.
             
        :param StructureMapIR: 
                         The <b>StructureMapRevision</b> containing a <b>CAEStructureMap</b> <i>Dataset</i>
                         with an XML <i>named reference</i> containing valid <i>StructureMap rules</i>.
             
        :return: . Any failures in creation of the output item or
             relationships are also returned as a part of the activity log.
        """
        ...

