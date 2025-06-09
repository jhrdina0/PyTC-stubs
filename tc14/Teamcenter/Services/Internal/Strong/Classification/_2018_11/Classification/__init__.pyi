import System
import Teamcenter.Services.Strong.Classification._2007_01.Classification
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClassificationObjectInfo:
    def __init__(self, ) -> None: ...
    ClsObjUid: str
    InstanceId: str
    ClassId: str
    UnitBase: str
    WsoId: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    Properties: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.ClassificationProperty]
    RelationUid: str
    LastModDate: str

class SaveClassificationObjectsResponse:
    def __init__(self, ) -> None: ...
    ClsObjs: list[ClassificationObjectInfo]
    Data: Teamcenter.Soa.Client.Model.ServiceData

class Classification:
    def __init__(self , *args: typing.Any) -> None: ...
    def SaveClassificationObjects(self, ClassificationObjects: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.ClassificationObject]) -> SaveClassificationObjectsResponse: ...

