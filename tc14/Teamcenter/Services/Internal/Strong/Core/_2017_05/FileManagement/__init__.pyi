import Teamcenter.Services.Internal.Strong.Core._2014_10.FileManagement
import Teamcenter.Soa.Client.Model.Strong
import typing

class DatashareManagerReplaceInfo:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    ImanFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    NamedReferenceName: str
    AbsoluteFilePath: str

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPlmdFileTicketForReplace(self, Infos: list[DatashareManagerReplaceInfo]) -> Teamcenter.Services.Internal.Strong.Core._2014_10.FileManagement.GetPlmdFileTicketResponse: ...

