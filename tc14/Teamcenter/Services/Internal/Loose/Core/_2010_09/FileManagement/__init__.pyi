import System
import Teamcenter.Soa.Client.Model
import typing

class CommitReplacedFileInfo:
    def __init__(self, ) -> None: ...
    ReplaceFileTicket: str
    NewOriginalFileName: str
    ImanFile: Teamcenter.Soa.Client.Model.ModelObject

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CommitReplacedFiles(self, CommitInfos: list[CommitReplacedFileInfo], Flags: list[bool]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

