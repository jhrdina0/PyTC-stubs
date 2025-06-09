import System
import Teamcenter.Services.Internal.Strong.Businessmodeler._2010_04.DataModelManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeployDataModelResponse:
    def __init__(self, ) -> None: ...
    SiteID: str
    SiteName: str
    TemplateDeployInfo: Teamcenter.Soa.Client.Model.Strong.InstalledTemplates
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    LogFileTickets: list[str]

class SiteTemplateDeployInfoResponse:
    def __init__(self, ) -> None: ...
    SiteID: str
    SiteName: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    TemplatesDeployInfo: list[Teamcenter.Soa.Client.Model.Strong.InstalledTemplates]

class DataModelManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def DeployDataModel2(self, DeployOption: str, UpdaterUpdateOption: str, UpdaterModeOption: str, Inputs: list[Teamcenter.Services.Internal.Strong.Businessmodeler._2010_04.DataModelManagement.DataModelDeploymentInput]) -> DeployDataModelResponse: ...
    def GetSiteTemplateDeployInfo(self, TemplateNames: list[str]) -> SiteTemplateDeployInfoResponse: ...

