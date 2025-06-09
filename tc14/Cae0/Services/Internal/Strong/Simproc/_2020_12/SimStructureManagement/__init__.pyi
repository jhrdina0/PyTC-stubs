import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FileDetails:
    def __init__(self, ) -> None: ...
    File: Teamcenter.Soa.Client.Model.Strong.ImanFile
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    FolderPath: str

class GetFileDetailsResponse3:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    FileDetails: list[FileDetails]
    ItemRevisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]

class SimStructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetFileDetails3(self, InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetFileDetailsResponse3: ...

