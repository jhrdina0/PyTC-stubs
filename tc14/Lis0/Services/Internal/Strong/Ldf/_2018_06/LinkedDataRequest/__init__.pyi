import System
import Teamcenter.Soa.Client.Model
import typing

class LdfSupportedDatasetTypesResponse:
    def __init__(self, ) -> None: ...
    DatasetTypeList: list[str]
    LdfServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LinkedDataRequest:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLDFSupportedDatasetTypes(self, LdfListFileExtensions: list[str]) -> LdfSupportedDatasetTypesResponse: ...

