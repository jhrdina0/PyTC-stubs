import System
import Teamcenter.Services.Internal.Strong.Core._2007_06.ProjectLevelSecurity
import Teamcenter.Soa.Client.Model
import typing

class GetFilteredProjectObjectsOutput:
    def __init__(self, ) -> None: ...
    ProjectID: str
    ObjectsInProject: list[str]

class GetFilteredProjectObjectsResponse:
    def __init__(self, ) -> None: ...
    FilteredObjectsInProjects: list[GetFilteredProjectObjectsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ProjectLevelSecurity:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetFilteredObjectsInProject(self, Input: list[Teamcenter.Services.Internal.Strong.Core._2007_06.ProjectLevelSecurity.GetFilteredProjectDataInputData]) -> GetFilteredProjectObjectsResponse: ...

