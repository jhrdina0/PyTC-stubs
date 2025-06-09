import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DatasetAttrInfo:
    def __init__(self, ) -> None: ...
    AttrName: str
    AttrValues: list[str]

class DatasetFileInfo:
    def __init__(self, ) -> None: ...
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    ReferenceFileTicket: str

class DatasetFileQueryInfo:
    def __init__(self, ) -> None: ...
    ClientID: str
    DatasetType: str
    ReferenceTypes: list[str]
    AttrInfo: list[DatasetAttrInfo]

class DatasetFilesOutput:
    def __init__(self, ) -> None: ...
    ClientID: str
    DatasetType: str
    DatasetReferenceFileInfo: list[DatasetReferenceFileInfo]

class DatasetFilesResponse:
    def __init__(self, ) -> None: ...
    DatasetFilesOutput: list[DatasetFilesOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DatasetReferenceFileInfo:
    def __init__(self, ) -> None: ...
    DatasetReferenceTypeName: str
    DatasetFiles: list[DatasetFileInfo]

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDatasetFiles(self, Inputs: list[DatasetFileQueryInfo], RetrieveFiles: bool) -> DatasetFilesResponse: ...

