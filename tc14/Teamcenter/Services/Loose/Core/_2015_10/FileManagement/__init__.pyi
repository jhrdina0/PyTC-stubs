import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class DatasetDigestInfoResponse:
    def __init__(self, ) -> None: ...
    DatasetDigestInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DigestInfo:
    def __init__(self, ) -> None: ...
    DigestAlgorithm: str
    Digest: str
    Certainty: int

class FileDigestInfoResponse:
    def __init__(self, ) -> None: ...
    FileDigestInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class FileDigestInfoSet:
    def __init__(self, ) -> None: ...
    Map: System.Collections.Hashtable

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDigestInfoForDatasets(self, Datasets: list[Teamcenter.Soa.Client.Model.ModelObject]) -> DatasetDigestInfoResponse: ...
    def GetDigestInfoForFiles(self, Files: list[Teamcenter.Soa.Client.Model.ModelObject]) -> FileDigestInfoResponse: ...

