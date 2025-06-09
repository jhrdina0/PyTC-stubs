import System
import Teamcenter.Services.Internal.Strong.Manufacturing._2020_01.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class ReferencedAssemblyFileInfo:
    def __init__(self, ) -> None: ...
    InputIndex: int
    Transform: list[float]
    Data: Teamcenter.Services.Internal.Strong.Manufacturing._2020_01.DataManagement.AdditionalInfo
    Ticket: str
    ReferenceSet: str
    FileObject: Teamcenter.Soa.Client.Model.ModelObject
    OriginalFileName: str

class ReferencedAssemblyFileInputInfo:
    def __init__(self, ) -> None: ...
    Lines: list[Teamcenter.Soa.Client.Model.ModelObject]
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2020_01.DataManagement.AdditionalInfo

class ReferencedAssemblyFileResponse:
    def __init__(self, ) -> None: ...
    Result: list[ReferencedAssemblyFileInfo]
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2020_01.DataManagement.AdditionalInfo
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetReferencedAssemblyFileInfo(self, Input: ReferencedAssemblyFileInputInfo) -> ReferencedAssemblyFileResponse: ...

