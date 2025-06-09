import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConfigIssueListsResp:
    """
    Configure issue lists response.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data. Teamcenter error stack content will be returned when error occurs."""
    ConfigData: list[IssueListConfigData]
    """Issue List configuration data."""

class GetIssueListInput:
    """
    
            Input to get configuration for accessible issue list or expand one issue list for
            current user.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    Name: str
    """
            Issue list name. When name is NULL, this operation returns configuration data for
            all accessible issue lists for the current user. The issue list name must be provided
            when expanding an issue list.
            """
    SiteLevel: str
    """Teamcenter preference name to save site level issue list configuration."""
    UserLevel: str
    """Teamcenter preference name to save user level issue list configuration."""
    ExpandList: bool
    """TRUE: expand issue list; FALSE: do not expand issue list."""

class IssueListConfigData:
    """
    Saved query and conditions and other data to create an issue list.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Issue list name."""
    Visible: bool
    """TRUE: issue list is visible; FALSE: issue list is invisible."""
    QueryName: str
    """Saved query name. Pre defined in Teamcenter."""
    SavedSearchName: str
    """
            Saved search name. When a saved search is provided, the saved query name and conditions
            will be extracted automatically to create an issue list. When this input is provided,
            the next three inputs (queryName, queryCriteria and queryValues are ignored).
            """
    QueryCriteria: list[str]
    """List of attribute names."""
    QueryValues: list[str]
    """List of attribute values."""
    IsFolderSiteLevel: bool
    """
            TRUE: issue list is site level (use this value only for system admin user); FALSE:
            issue list is user level.
            """
    PrefName: str
    """
            Teamcenter preference name to save issue list configuration data. When not provided,
            the value set in the ISSUE_issuelists_site preference (for system level issue
            lists) and the value set in the ISSUE_issuelists_user preference (for user
            level issue lists) are assumed. The client can choose different names and use the
            names consistently.
            """
    Operation: bool
    """
            TRUE: create or update issue list; FALSE: delete issue list. When deleting an issue
            list, only the issue list name is needed.
            """

class GetIssueListOutput:
    """
    
            It may contain configuration data for all accessible issue lists for current user
            or issue report revision objects returned from expanding one issue list.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    ConfigData: IssueListConfigData
    """Issue list configuration."""
    Results: list[Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision]
    """Issue report revision objects for given issue list."""

class GetIssueListsResp:
    """
    Get issue list response.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data. Teamcenter error stack content will be returned when error occurs."""
    OutputStru: list[GetIssueListOutput]
    """Output structures."""

class IssueManagement:
    """
    Interface IssueManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ConfigureIssueLists(self, Inputs: list[IssueListConfigData]) -> ConfigIssueListsResp:
        """    
             The client calls this operation to create/update/delete issue list configuration.
             
             The way to browse issue reports is to execute a query with properly defined query
             conditions. With Teamcenter Issue Management, the query and conditions can be saved
             as an issue list for re-use. An issue list is not a sub class of Teamcenter Folder.
             The configuration data for an issue list is saved as a Teamcenter preference.
             
             There are two levels of issue lists: a system level issue list that is created by
             a Teamcenter administrative user and accessible to all users, or a user level issue
             list that is created by a user and accessible to the owning user only. By default,
             system level issue lists are saved in preference ISSUE_issuelists_site with
             site protection scope. User level issue lists are saved in preference ISSUE_issuelists_user
             with user protection scope. The services client can specify a different preference
             name for system level or user level issue lists. An issue list can be set as visible
             or invisible by its owning user. Visible issue lists are accessible. Invisible issue
             lists can't be expanded (not accessible).
             
             The Issue Management service client application should not assume that an issue report
             can be created under a selected issue list. An issue list doesn't reference (or contain)
             any issue reports till the query is executed. The client must refresh the issue list
             (re-execute the query) whenever necessary.
             



Use Cases:

             The user can create an issue list to list all issues reported for a Detail Review
             gate. The user can use saved query __find_issue_objects, set query condition
             design review gate to Detail Review. Save the issue list as user level which
             is accessible for owning user only.
             

Teamcenter Component:

             Issue Management - Teamcenter Issue Management is an application that allows users
             to capture issue, share issue data and collaborate on the business process to resolve
             issue in product life management.
             
        :param Inputs: 
                         Inputs to configure issue lists.
             
        :return: Array of issue list configurations.
        """
        ...
    def GetExpandIssueLists(self, Inputs: list[GetIssueListInput]) -> GetIssueListsResp:
        """    
             The client calls this operation to get configuration data for all accessible issue
             lists for the current user or to expand one issue list.
             
             The client needs to get all accessible issue lists configuration data to construct
             the issue list management UI for the current user. Accessible issue lists include
             system level lists plus user level lists that are defined by current user. Invisible
             issue lists are not returned because these issue lists are not accessible.
             
             This operation can also be called to expand one issue list. Expanding an issue list
             means to execute the query with the conditions configured for the issue list and
             return issue report revision objects to the client. In cases where this may cause
             performance degradation, and the client application is capable of lazy-loading issue
             report revision objects, the client is recommended to leverage the Teamcenter query
             service to get issue report revision object UIDs for an issue list.
             



Use Cases:

             NX Issue Tracking constructs a user interface showing accessible issue lists for
             the current user. When the user clicks to expand a selected issue list, the client
             code calls this operation with the selected issue list name and expandList = TRUE.
             Issue report revision objects are returned to the NX application.
             

Teamcenter Component:

             Issue Management - Teamcenter Issue Management is an application that allows users
             to capture issue, share issue data and collaborate on the business process to resolve
             issue in product life management.
             
        :param Inputs: 
                         Inputs to get or expand issue lists.
             
        :return: Array of issue list configuration and issue objects.
        """
        ...

