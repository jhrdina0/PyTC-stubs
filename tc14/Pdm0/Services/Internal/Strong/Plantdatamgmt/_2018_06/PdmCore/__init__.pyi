import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindCondElementsAndRltdObjsResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    WorkspaceObjs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]

class PdmCore:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindCondlMdlElementsAndRltdWSObjs(self, Model: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> FindCondElementsAndRltdObjsResponse: ...
    def SetReleaseStatusInBulk(self, WorkspaceObjs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject], ReleaseStatus: str, ReleaseDate: System.DateTime, SkipIfAlreadyHasStatus: bool, ReleaseStatusListToSkip: list[str], RevisionRuleName: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...

