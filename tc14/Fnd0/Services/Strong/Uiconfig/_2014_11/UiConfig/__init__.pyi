import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClientConfigurations:
    """
    This structure contains command and column configuration data for the indicated client.
    """
    def __init__(self, ) -> None: ...
    Client: str
    """The client for which the configurations are applicable."""
    ColumnConfigurations: list[ColumnConfigData]
    """List of column configurations."""
    CommandConfigurations: list[CommandConfigData]
    """List of command configurations."""

class ClientInput:
    """
    Specifies client input information including client name and hosting client name.
    """
    def __init__(self, ) -> None: ...
    ClientName: str
    """
            The name of a client application, as represented by an instance of Fnd0Client in
            the Teamcenter database. This value must match the value of fnd0ClientName property.
            """
    HostingClientName: str
    """
            Specifies the name of a hosting client application, as represented by an instance
            of Fnd0Client, in the Teamcenter databases. This value must match a value of the
            fnd0ClientName property. For example, if client A is integrated with client B and
            the user can invoke client B commands from within client A, the input to getUiConfigs
            would specify client A as hosting client and client B as the client. If the caller
            wanted native commands for client A, client A would be specified as client and hosting
            client would be empty.
            """

class ColumnConfig:
    """
    
            This structure contains information for a column configuration within a client scope
            URI. It contains a unique column config id, a list of column definition information
            , and default sort direction.
            
    """
    def __init__(self, ) -> None: ...
    ColumnConfigId: str
    """The unique identifier of the column."""
    SortDirection: str
    """How the columns are sorted.  Valid values are Ascending or Descending."""
    Columns: list[ColumnDefInfo]
    """Ordered list of column details."""

class ColumnConfigData:
    """
    
            This structure returns information about the column configuration definitions for
            a scope, hosting client and client scope.
            
    """
    def __init__(self, ) -> None: ...
    Scope: str
    """The scope for which the column data is applicable."""
    HostingClient: str
    """
            The name of hosting client for which the list of column configurations is applicable.
            This value must correspond to the value of the property fnd0ClientName for an Fnd0Client
            object in the Teamcenter database.
            """
    ClientScopeURI: str
    """
            The client scope for which the list of column configurations is applicable. This
            must match a value of fnd0ClientScopeURI which is the unique identifier of a client
            scope (Fnd0ClientScope).
            """
    ColumnConfigurations: list[ColumnConfig]
    """List of column configuration details."""

class ColumnDefInfo:
    """
    
            Contains details about a specific column. This includes the type of object for which
            the column is applicable, the name of the property displayed in the column, a flag
            indicating if the column should be used to order information displayed in the client
            and pixel width.
            
    """
    def __init__(self, ) -> None: ...
    TypeName: str
    """
            The Business Object type for the value displayed in the column.   This can be any
            valid Teamcenter business object type.
            """
    PropertyName: str
    """The property name for the value displayed in the column."""
    SortByFlag: bool
    """True if the column is used to sort the information displayed to the user."""
    PixelWidth: int
    """
            The pixel width for the column.  Valid pixel widths are integer values between1 and
            500.
            """

class CommandCollectionInfo:
    """
    Contains a command collection and indexes to its children commands or command collections.
    """
    def __init__(self, ) -> None: ...
    ChildIsCollection: list[bool]
    """Flag indicating if the child is a command or a command collection."""
    ChildConfigIndex: list[int]
    """
            Index of the child in either the CommandConfigData:commands list or the CommandConfigData:cmdsCollections
            list.
            """
    CommandCollection: Teamcenter.Soa.Client.Model.Strong.Fnd0CommandCollection
    """The Teamcenter command collection object."""

class CommandConfigData:
    """
    
            This structure returns information about the command configuration definitions for
            a client scope URI.
            
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

class ScopeInput:
    """
    Contains scope input information including scope name and scope query param.
    """
    def __init__(self, ) -> None: ...
    ScopeName: str
    """The name of a scope.  For Site and current login user, this value should be empty."""
    ScopeQueryParam: str
    """
            The query scope that is used to retrieve the UI configurations.  Valid values are
            Site, Group, Role, User, LoginUser, and AvailableForLoginUser. Site returns the configuration
            defined for the site. Group returns the configuration defined for a specific Teamcenter
            Group. Role returns the configuration defined for a specific Teamcenter Role. User
            returns the configurations defined for a specific Teamcenter User. LoginUser returns
            the current configuration defined for the current login user. AvailableForLoginUser
            returns all the configurations available for the current login user.   scopeName
            should be empty when scopeQueryParam is set for Site, LoginUser or AvailableForLoginUser.
            """

class GetUIConfigInput:
    """
    
            Contains input information requiredto retrieve UI configurations from the Teamcenter
            database.
            
    """
    def __init__(self, ) -> None: ...
    ClientScopeURIs: list[str]
    """
            List of client scope URIs representing, for example location.sublocation in Active
            Workspace. (Fnd0ClientScope::fnd0ClientScopeURI). If empty, the UI Configuration
            for all client scopes are returned.
            """
    Scope: ScopeInput
    """
            The scope of the desired UI configuration information. This includes the name of
            the scope (i.e. a user, group or role) and scope query parameter information.
            """
    Client: ClientInput
    """Client information including client name and hosting client name."""

class GetUIConfigResponse:
    """
    
            This structure returns information to the client about column configuration and command
            applicability. The ServiceData contains information about errors encountered during
            processing.
            
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

class SaveScopeInput:
    """
    
            SaveScopeInput structure contains information including scope name and details about
            scope applicability.  The value in scopeName should be empty if the value in param
            refers to Site or LoginUser.
            
    """
    def __init__(self, ) -> None: ...
    ScopeName: str
    """The name of a valid Teamcenter scope."""
    SaveScopeParam: str
    """
            The save scope that is used to apply some types of UI configurations. Valid values
            are:Site-Save configuration to the Teamcenter site. The scope name should be empty.
            Group-Save the configuration for a Teamcenter Group. Role-Save the configuration
            for a Teamcenter Role. User-Save the configuration for a Teamcenter User. LoginUser-Save
            the configuration for the current login user. The scope name should be empty.
            """

class SaveColumnConfigData:
    """
    
            This structure contains column configuration details and a list of column definition
            information.
            
    """
    def __init__(self, ) -> None: ...
    Scope: SaveScopeInput
    """
            The scope for which the column data is applicable.  This includes the name of the
            scope (i.e. a user, group or role) and the save scope parameter information.
            """
    ClientScopeURI: str
    """The unique name of the client scope containing configurations."""
    ColumnConfigId: str
    """The identifier for the column configuration."""
    SortDirection: str
    """Sort order for the columns. Valid values are Ascending and Descending."""
    Columns: list[ColumnDefInfo]
    """Ordered list of column information."""

class SaveCommandCollectionInfo:
    """
    This structure contains information to save for a command collection.
    """
    def __init__(self, ) -> None: ...
    CollectionId: str
    """Unique identifier of the command collection."""
    ConfigInfo: list[SaveCommandConfigInfo]
    """Configuration changes for the command collection."""

class SaveCommandConfigData:
    """
    
            This structure contains information about the command configuration definitions for
            a client scope URI.
            
    """
    def __init__(self, ) -> None: ...
    Scopes: list[SaveScopeInput]
    """
            List of scope names for which the command configuration for which the changes are
            application.  If the site scope should be changed scopeName should be empty.
            """
    SaveCommandCollectionInfo: list[SaveCommandCollectionInfo]
    """
            List of command collections changes.  Each change in this will be applied to each
            scope specified in the scope names list.
            """

class SaveCommandConfigInfo:
    """
    
            Configuration information which indicates if a command or command collection is being
            hidden or unhidden.
            
    """
    def __init__(self, ) -> None: ...
    IsCollection: bool
    """True if id is the id of a command collection.  False if id is a command."""
    Id: str
    """The unique identifier of a command or command collection."""
    Hidden: bool
    """True if the command or command collection should be hidden."""

class SaveUiConfigurations:
    """
    
            Contains two lists; one specifying column configuration information to save and the
            other specifying command configuraiton information to save.
            
    """
    def __init__(self, ) -> None: ...
    ColumnConfigurations: list[SaveColumnConfigData]
    """List of column configuration information."""
    CommandConfigurations: list[SaveCommandConfigData]
    """List of command configuration data."""

class UiConfig:
    """
    Interface UiConfig
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetUIConfigs(self, GetUiConfigsIn: list[GetUIConfigInput]) -> GetUIConfigResponse:
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
    def SaveUiConfigs(self, SaveUiConfigsIn: SaveUiConfigurations) -> Teamcenter.Soa.Client.Model.ServiceData:
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

