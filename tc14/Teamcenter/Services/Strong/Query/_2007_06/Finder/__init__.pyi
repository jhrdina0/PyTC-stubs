import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindWorkspaceObjectsOutput:
    """
    FindWorkspaceObjectsOutput
    """
    def __init__(self, ) -> None: ...
    FindSetIndex: int
    """The index of FindSet that generated the output."""
    FoundObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """The WorkspaceObject business objects matching the search criteria."""

class FindWorkspaceObjectsResponse:
    """
    FindWorkspaceObjectsResponse
    """
    def __init__(self, ) -> None: ...
    OutputList: list[FindWorkspaceObjectsOutput]
    """A list of found workspace objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class WSOFindCriteria:
    """
    WSOFindCriteria
    """
    def __init__(self, ) -> None: ...
    ObjectType: str
    """
            If set, must be set to the corresponding class name . If not set, this criteria will
            be ignored by the search.
            """
    ObjectName: str
    """
            Name of object  Can contain wild card characters.  The percent sign and underscore
            are the only valid wild card characters,  where:  % Represents any set of characters
            in the substring.  _ (Underscore) Represents any single character in the substring.
            """
    Owner: Teamcenter.Soa.Client.Model.ModelObject
    """
            The owning User to limit found objects for. A null value will expand the search
            to all users.
            """
    Group: Teamcenter.Soa.Client.Model.ModelObject
    """
            The owning Group to limit found objects for. A null value will expand the
            search to all groups.
            """
    CreatedBefore: System.DateTime
    """
            The maximum creation date to limit found objects. A null value will not limit the
            results.
            """
    ModifiedBefore: System.DateTime
    """
            The maximum last modified date to limit found objects. A null value will not limit
            the results.
            """
    ReleasedBefore: System.DateTime
    """
            The maximum released date to limit found objects. A null value will not limit the
            results.
            """
    CreatedAfter: System.DateTime
    """
            The minimum creation date to limit found objects. A null value will not limit the
            results.
            """
    ModifiedAfter: System.DateTime
    """
            The minimum last modified date to limit found objects. A null value will not limit
            the results.
            """
    ReleasedAfter: System.DateTime
    """
            The minimum released date to limit found objects. A null value will not limit the
            results.
            """
    Scope: str
    """
            Scope of search,  WSO_scope_All = entire database,  WSO_search_Approved = searches
            for objects that have at least  one status of approval.
            """

class WSOFindSet:
    """
    WSOFindSet
    """
    def __init__(self, ) -> None: ...
    Criterias: list[WSOFindCriteria]
    """A list of FindCriteria to search with."""

class Finder:
    """
    Interface Finder
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindWorkspaceObjects(self, FindList: list[WSOFindSet]) -> FindWorkspaceObjectsResponse:
        """    
             Query the database for WorkspaceObjects. A collection of WSOFindSets are used
             to do the queries. For each WSOFindSet , a FindWorkspaceObjectsOutput will be generated
             if any WorkspaceObjects are found that meet all the criteria.  Each FindWorkspaceObjectsOutput
             will contain the tags of the WorkspaceObjects that meet all the criteria and
             the index of the WSOFindSet in the findList that generated the output.  If an error
             is encountered, then no FindWorkspaceObjectsOutput will be generated for that WSOFindSet
             (no partial data returned) and the index for the WSOFindSet in the findList will
             be the client ID in the partial error.  If no WSOFindSet generates any output, a
             null outputList is returned.
             

Use Cases:

             Find workspace object using basic attributes such as object type, object name, owner,
             group, created before, created after etc.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param FindList: 
                         A list of WSOFindSet used to find workspace objects.
             
        :return: Contains a list of FindWorkspaceObjectsOutput structures (which contain the found
             workspace objects). Any found workspace objects will be sent back in the standard
             ServiceData list of plain objects. Any failure will be returned as partial errors
             in ServiceData with index for the WSOFindSet in the findList.
        """
        ...

