import System
import System.Collections
import Teamcenter.Services.Strong.Core._2011_06.DataManagement
import Teamcenter.Services.Strong.Core._2012_09.DataManagement
import Teamcenter.Services.Strong.Core._2013_05.DataManagement
import Teamcenter.Services.Strong.Core._2014_10.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class ReviseIn:
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    InputPropValues: System.Collections.Hashtable
    DeepCopyDatas: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.DeepCopyData]

class SaveAsIn:
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    InputPropValues: System.Collections.Hashtable
    DeepCopyDatas: list[Teamcenter.Services.Strong.Core._2014_10.DataManagement.DeepCopyData]

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ReviseObjectsInBulk(self, ReviseData: list[ReviseIn]) -> Teamcenter.Services.Strong.Core._2013_05.DataManagement.ReviseObjectsResponse: ...
    def SaveAsObjectsInBulkAndRelate(self, SaveAsData: list[SaveAsIn], RelationInfo: list[Teamcenter.Services.Strong.Core._2012_09.DataManagement.RelateInfoIn]) -> Teamcenter.Services.Strong.Core._2011_06.DataManagement.SaveAsObjectsResponse: ...

