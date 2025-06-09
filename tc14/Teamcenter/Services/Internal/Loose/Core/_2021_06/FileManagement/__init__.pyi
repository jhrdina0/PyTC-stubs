import System
import Teamcenter.Services.Loose.Core._2006_03.FileManagement
import Teamcenter.Services.Loose.Core._2007_01.FileManagement
import typing

class FileManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDatasetTicketsForChunkedUpload(self, Inputs: list[Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsInputData]) -> Teamcenter.Services.Loose.Core._2006_03.FileManagement.GetDatasetWriteTicketsResponse: ...
    def GetTransientTicketsForChunkedUpload(self, TransientFileInfos: list[Teamcenter.Services.Loose.Core._2007_01.FileManagement.TransientFileInfo]) -> Teamcenter.Services.Loose.Core._2007_01.FileManagement.GetTransientFileTicketsResponse: ...

