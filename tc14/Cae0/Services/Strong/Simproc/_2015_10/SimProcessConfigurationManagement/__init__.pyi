import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class ToolTabsInfo:
    """
    The response contains information about the Simulation Tools along with Service Data.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data containing partial errors."""
    ToolTabsMaster: list[ToolTabsMaster]
    """
            The structure that contains the tool information as well as the properties of the
            tabs.
            """

class ToolTabsMaster:
    """
    
            This structure contains UID of the tool object, its properties and the associated
            tabs information.
            
    """
    def __init__(self, ) -> None: ...
    ToolUID: str
    """UID of the tool."""
    ToolTabValue: list[ToolTabValue]
    """The properties of the tabs."""

class ToolTabValue:
    """
    
            This structure contains the information of tab object along with its name, properties
            and associated referenced properties if any.
            
            For example, the InputConfiguration tab, the tabIdentifier will be CAEToolInputConfigTab,the
            toolTabMap will hold the information of the properties of the tab and the internamePropsVector
            will hold the information about the properties of the referenced object like Rules.
            
    """
    def __init__(self, ) -> None: ...
    TabIdentifier: str
    """Identifier of the tab"""
    ToolTabMap: System.Collections.Hashtable
    """Property name value map (string, string) of tab object."""
    InternalProps: list[ToolTabValue]
    """List of referenced property names with values for the  tab."""

class SimProcessConfigurationManagement:
    """
    Interface SimProcessConfigurationManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetToolTabProperties(self, InputItemTypes: list[str], TabIdentifiers: list[str], LaunchTypes: list[str]) -> ToolTabsInfo:
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

