import Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClientConfigurations:
    """
    
            DEPRECATED: This structure contains command and column configuration data for the
            indicated client.
            
    """
    def __init__(self, ) -> None: ...
    Client: str
    """The client for which the configurations are applicable."""
    ColumnConfigurations: list[Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.ColumnConfigData]
    """List of column configurations."""
    CommandConfigurations: list[CommandConfigData]
    """List of command configurations."""

class CommandCollectionInfo:
    """
    
            DEPRECATED: Contains a command collection and indexes to its children commands or
            command collections.
            
    """
    def __init__(self, ) -> None: ...
    ChildIsCollection: list[bool]
    """Flag indicating if the child is a command or a command collection."""
    ChildIsVisible: list[bool]
    """Flag indicating if the command or collection is visible."""
    ChildConfigIndex: list[int]
    """
            Index of the child in either the CommandConfigData:commands list or the CommandConfigData:cmdsCollections
            list.
            """
    CommandCollection: Teamcenter.Soa.Client.Model.Strong.Fnd0CommandCollection
    """The Teamcenter command collection object."""

class CommandConfigData:
    """
    
            DEPRECATED: This structure returns information about the command configuration definitions
            for a client scope URI.
            
    """
    def __init__(self, ) -> None: ...
    ScopeName: str
    """The scope for which the command data is applicable."""
    HostingClient: Teamcenter.Soa.Client.Model.Strong.Fnd0Client
    """The hosting client for which the command data is applicable."""
    ClientScope: Teamcenter.Soa.Client.Model.Strong.Fnd0ClientScope
    """The client scope URI containing the list of command configurations."""
    CmdCollections: list[CommandCollectionInfo]
    """List of all top level and child command collections in the client scope."""
    CmdCollectionIndex: list[int]
    """Index into cmdCollections list for top level command collections in the client scope."""
    Commands: list[Teamcenter.Soa.Client.Model.Strong.Fnd0AbstractCommand]
    """List of all command children accessible in the client scope."""
    CommandCollectionRels: list[Teamcenter.Soa.Client.Model.Strong.Fnd0UIConfigCollectionRel]
    """
            List of all commandCollectionRel objects that associate top level command collections
            with client scope.
            """

class GetUIConfigResponse:
    """
    
            DEPRECATED: This structure returns information to the client about column configuration
            and command applicability. The ServiceData contains information about errors encountered
            during processing.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            ServiceData structure containing errors and command, command collection and icon
            objects. If there is an error retrieving the configuration information, the error
            added to the ServiceData as a partial error.
            """
    UiConfigInfo: list[ClientConfigurations]
    """List of configuration information including command and column information"""

class UiConfig:
    """
    Interface UiConfig
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetUIConfigs2(self, GetUiConfigsIn: list[Fnd0.Services.Strong.Uiconfig._2014_11.UiConfig.GetUIConfigInput]) -> GetUIConfigResponse:
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

