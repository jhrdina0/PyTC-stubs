import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Visualization._2010_09.DataManagement
import Teamcenter.Services.Internal.Strong.Visualization._2012_10.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class AdditionalInfo:
    def __init__(self, ) -> None: ...
    StrToDateVectorMap: System.Collections.Hashtable
    StrToDoubleVectorMap: System.Collections.Hashtable
    StrToStringVectorMap: System.Collections.Hashtable
    StrToObjectVectorMap: System.Collections.Hashtable
    StrToIntegerVectorMap: System.Collections.Hashtable

class CreateSnapshot3DResponse2:
    def __init__(self, ) -> None: ...
    Snapshot3DOutputMap: System.Collections.Hashtable
    AdditionalInfo: AdditionalInfo
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Snapshot3DUpdateResponse2:
    def __init__(self, ) -> None: ...
    Snapshot3DUpdateOutputMap: System.Collections.Hashtable
    AdditionalInfo: AdditionalInfo
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSnapshot3D2(self, Input: list[Teamcenter.Services.Internal.Strong.Visualization._2012_10.DataManagement.NewSnapshot3DInput], AdditionalInfo: AdditionalInfo) -> CreateSnapshot3DResponse2: ...
    def UpdateSnapshot3D2(self, Snapshot3DUpdateInputList: list[Teamcenter.Services.Internal.Strong.Visualization._2010_09.DataManagement.Snapshot3DUpdateInput], AdditionalInfo: AdditionalInfo) -> Snapshot3DUpdateResponse2: ...

