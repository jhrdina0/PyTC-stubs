import Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig
import Fnd0.Services.Strong.Uiconfig._2015_10.UiConfig
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class UiConfigRestBindingStub(UiConfigService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetUIConfigs(self, GetUiConfigsIn: list[Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.GetUIConfigInput]) -> Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.GetUIConfigResponse: ...
    def SaveUiConfigs(self, SaveUiConfigsIn: Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.SaveUiConfigurations) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetUIConfigs2(self, GetUiConfigsIn: list[Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.GetUIConfigInput]) -> Fnd0.Services.Strong.Uiconfig._2015_10.UiConfig.GetUIConfigResponse: ...

class UiConfigService:
    """
    
            The UIConfig service provides operations to support confgurable Teamcenter commands
            and columns. These configurations are persisted in the Teamcenter database and defined
            using the Business Modeler IDE.
            


Library Reference:

Fnd0SoaUiConfigStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> UiConfigService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetUIConfigs(self, GetUiConfigsIn: list[Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.GetUIConfigInput]) -> Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.GetUIConfigResponse:
        """    
             This operation returns information used by the client to render the User Interface.
             The information returned includes command and column configuration information.
             

Use Cases:

             Use Case 1: Request UI Configuration(s) based on the current login user
             
             Client requests the column and/or command information for one or more client scopes
             using this operation and scope as login user.
             

             Use Case 2: Request UI Configuration(s) based on a specific Teamcenter scope
             
             Client requests the column and/or command information for one or more client scopes
             using this operation and scope as Role, Site or Group.
             


Teamcenter Component:

             UI Configuration - This component provides framework and functionalities for User
             Interface Configuration like Column Configuration and Command Contribution.
             
        :param GetUiConfigsIn: 
                         Contains input information required to retrieve UI configurations from the Teamcenter
                         database.
             
        :return: Returns: A list of command and column configurations based on the input provided
             to the operation. The following partial errors may be returned: 302010-Invalid Client
             Scope. 302012-Invalid Client. 302013-Invalid Scope. 302014-Invalid Hosting Client.
        """
        ...
    def SaveUiConfigs(self, SaveUiConfigsIn: Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.SaveUiConfigurations) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service operation saves column and command configuration information to the
             Teamcenter database.  A Teamcenter client may use this information to render the
             user interface as the user navigates the Teamcenter client.  Default configurations
             are created using the Business Modeler IDE and installed with Teamcenter.
             

Use Cases:

             Use Case 1: User level column configuration
             

             A User wants to change the default column configuration for a Client Scope when he
             is logged into the client.  The saved configuration will override the default configuration
             for the user's applicable role, group or site.
             

             Use Case 2: Administrator level column and command configuration
             
             An Administrator wants to change the UI configurations for Client Scope URI for a
             specific Group, Role, or User.  Columns may be reordered, removed, or if removed,
             added back to a specific configuration.  Commands and command collections may be
             reordered, hidden or unhidden.  The Business Modeler IDE must be used to create new
             commands, commands and command collections.
             


Teamcenter Component:

             UI Configuration - This component provides framework and functionalities for User
             Interface Configuration like Column Configuration and Command Contribution.
             
        :param SaveUiConfigsIn: 
                         Command and column configuration changes to save.
             
        :return: The ServiceData structure containing any partial errors that may have occurred while
             saving the data in the input structures.  The following partial errors may be returned:
             302001 - Invalid column configuration id. 302003 - Invalid object type name. 302004
             - Invalid property name. 302005 - Invalid pixel width. 302010 - Invalid Client Scope
             URI. 302011 - Invalid command id.
        """
        ...
    def GetUIConfigs2(self, GetUiConfigsIn: list[Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.GetUIConfigInput]) -> Fnd0.Services.Strong.Uiconfig._2015_10.UiConfig.GetUIConfigResponse:
        """    
             This operation returns information used by the client to render the User Interface.
             The information returned includes command and column configuration information. This
             operation replaces getUIConfigs operation, it returns the Fnd0CommandCollectionRel
             objects that associate the top level command collections to client scope in CommandConfigData
             structure in addition to Fnd0CommandCollection objects.
             

Teamcenter Component:

             UI Configuration - This component provides framework and functionalities for User
             Interface Configuration like Column Configuration and Command Contribution.
             
        :param GetUiConfigsIn: 
                         Contains input information required to retrieve UI configurations from the Teamcenter
                         database.
             
        :return: Returns: A list of command and column configurations based on the input provided
             to the operation. The following partial errors may be returned: 302010-Invalid Client
             Scope. 302012-Invalid Client. 302013-Invalid Scope. 302014-Invalid Hosting Client.
        """
        ...

