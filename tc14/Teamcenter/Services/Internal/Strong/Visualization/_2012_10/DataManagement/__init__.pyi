import System
import Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement
import Teamcenter.Services.Internal.Strong.Visualization._2010_09.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class Snapshot3DAttachToInfo:
    def __init__(self, ) -> None: ...
    AttachToObject: Teamcenter.Soa.Client.Model.ModelObject
    RelationName: str

class NewSnapshot3DInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    AttachToInfo: Snapshot3DAttachToInfo
    DatasetInfo: Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.DatasetInfo
    VisibleLinesList: list[Teamcenter.Soa.Client.Model.ModelObject]
    CreateStructureFile: bool
    VariantName: str
    NamedRefFileUpdateInfoList: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.NamedRefUploadOrUpdateInfo]

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSnapshot3D(self, Input: list[NewSnapshot3DInput]) -> Teamcenter.Services.Internal.Strong.Visualization._2010_09.DataManagement.CreateSnapshot3DResponse: ...

