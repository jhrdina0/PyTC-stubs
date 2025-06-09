import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class PackageBriefcaseContentsInfo:
    def __init__(self, ) -> None: ...
    SourceSiteId: int
    TargetSiteIds: list[int]
    RequestingUserName: str
    TcplmxmlFmsTickets: list[str]
    ExportLogFmsTickets: list[str]
    DatasetName: str

class PackageBriefcaseContentsResponse:
    def __init__(self, ) -> None: ...
    BriefcaseDataSet: Teamcenter.Soa.Client.Model.Strong.Dataset
    BriefcaseDataSetUrl: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class UnpackBriefcaseContentsResponse:
    def __init__(self, ) -> None: ...
    SourceSiteId: int
    TcplmxmlFmsTickets: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Briefcase:
    def __init__(self , *args: typing.Any) -> None: ...
    def PackageBriefcaseContents(self, PackageBriefcaseContentsInfo: PackageBriefcaseContentsInfo) -> PackageBriefcaseContentsResponse: ...
    def UnpackBriefcaseContents(self, UidOfBriefcaseTcFile: str) -> UnpackBriefcaseContentsResponse: ...

