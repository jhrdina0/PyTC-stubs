import System
import Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport
import Teamcenter.Services.Strong.Globalmultisite._2021_06.ImportExport
import typing

class ExportFilesOfflineInput:
    """
    Input structure for exportFilesOffline operation.
    """
    def __init__(self, ) -> None: ...
    DatasetUid: str
    """UID of Dataset"""
    ItemRevisionUid: str
    """UID of ItemRevision"""

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportFilesOffline2(self, Input: list[ExportFilesOfflineInput], Options: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2021_06.ImportExport.ExportFilesOfflineResponse: ...

