import Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetFileDetailsResponse2:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    FileToDatasetMap2: System.Collections.Hashtable
    FileToItemRevisionMap2: System.Collections.Hashtable
    FileToFolderPathMap: System.Collections.Hashtable
    ItemRevisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    Files: list[Teamcenter.Soa.Client.Model.Strong.ImanFile]

class RemoveDuplicateCadJtResponse:
    def __init__(self, ) -> None: ...
    NoOfObjectsProcessed: int
    NoOfObjectsSkipped: int
    NoOfDatasetsDeleted: int
    NoOfDatasetsCut: int
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SimStructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateNodeXMLWithFocus(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Domain: str, Focus: str) -> Cae0.Services.Internal.Strong.Simproc._2015_03.SimStructureManagement.GenerateNodeXMLResponse: ...
    def GetFileDetails2(self, InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetFileDetailsResponse2: ...
    def RemoveDuplicateCadJt(self, SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> RemoveDuplicateCadJtResponse: ...

