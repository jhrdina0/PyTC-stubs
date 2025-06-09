import System
import Teamcenter.Services.Internal.Strong.Core._2007_06.ProjectLevelSecurity
import Teamcenter.Soa.Client.Model
import typing

class ProjectSmartFolderHierarchyOutput2:
    def __init__(self, ) -> None: ...
    ProjectID: str
    ProjectSmartFolderHierarchy: list[SmartFolderOutputInfo2]

class ProjectSmartFolderHierarchyOutputResponse2:
    def __init__(self, ) -> None: ...
    Output: list[ProjectSmartFolderHierarchyOutput2]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SmartFolderOutputInfo2:
    def __init__(self, ) -> None: ...
    ParentName: str
    ParentInternalName: str
    Name: str
    InternalName: str
    Filters: list[Teamcenter.Services.Internal.Strong.Core._2007_06.ProjectLevelSecurity.Filter]
    IsLeaf: bool

class ProjectLevelSecurity:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetProjectsSmartFolderHierarchy2(self, ProjectIDs: list[str]) -> ProjectSmartFolderHierarchyOutputResponse2: ...

