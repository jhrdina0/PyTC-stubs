import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Filter:
    def __init__(self, ) -> None: ...
    SourceTypeName: str
    Name: str
    Value: str

class GetFilteredProjectDataInputData:
    def __init__(self, ) -> None: ...
    ProjectID: str
    Filters: list[Filter]

class GetFilteredProjectDataOutput:
    def __init__(self, ) -> None: ...
    ProjectID: str
    FilteredData: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]

class GetFilteredProjectDataResponse:
    def __init__(self, ) -> None: ...
    Output: list[GetFilteredProjectDataOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ProjectSmartFolderHierarchyOutput:
    def __init__(self, ) -> None: ...
    ProjectID: str
    ProjectSmartFolderHierarchy: list[SmartFolderOutputInfo]

class ProjectSmartFolderHierarchyOutputResponse:
    def __init__(self, ) -> None: ...
    Output: list[ProjectSmartFolderHierarchyOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SmartFolderOutputInfo:
    def __init__(self, ) -> None: ...
    ParentName: str
    Name: str
    Filters: list[Filter]
    IsLeaf: bool

class TopLevelHierarchyOutputResponse:
    def __init__(self, ) -> None: ...
    TopHierarchy: list[SmartFolderOutputInfo]
    UserProjects: list[UserProjectsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class UserProjectsOutput:
    def __init__(self, ) -> None: ...
    Project: Teamcenter.Soa.Client.Model.Strong.TC_Project
    Filters: list[Filter]

class ProjectLevelSecurity:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetFilteredProjectData(self, Input: list[GetFilteredProjectDataInputData]) -> GetFilteredProjectDataResponse: ...
    def GetProjectsSmartFolderHierarchy(self, ProjectIDs: list[str]) -> ProjectSmartFolderHierarchyOutputResponse: ...
    def GetTopLevelSmartFolderHierarchy(self) -> TopLevelHierarchyOutputResponse: ...

