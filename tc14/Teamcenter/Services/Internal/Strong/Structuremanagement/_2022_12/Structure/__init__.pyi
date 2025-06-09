import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeInfo:
    def __init__(self, ) -> None: ...
    PropName: str
    PropValues: list[str]

class CreateOrUpdateOccAttrObjectsIn:
    def __init__(self, ) -> None: ...
    ClientId: str
    BvrOrOccRev: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    Occurrence: Teamcenter.Soa.Client.Model.Strong.PSOccurrenceThread
    OccAttrObjectType: str
    PropInfo: list[AttributeInfo]

class CreateOrUpdateOccAttrObjectsResp:
    def __init__(self, ) -> None: ...
    CreatedOrUpdatedOccAttrObjects: list[OccWithAttrObjectsInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetOccAttrsObjectsIn:
    def __init__(self, ) -> None: ...
    ClientId: str
    BvrOrOccRev: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    Occurrence: Teamcenter.Soa.Client.Model.Strong.PSOccurrenceThread
    OccAttrObjectTypes: list[str]

class GetOccAttrsObjectsResponse:
    def __init__(self, ) -> None: ...
    OccAttrObjects: list[OccWithAttrObjectsInfo]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class OccAttrInfo:
    def __init__(self, ) -> None: ...
    OccAttrType: str
    OccAttrObject: Teamcenter.Soa.Client.Model.Strong.POM_object

class OccWithAttrObjectsInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    BvrOrOccRev: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    Occurrence: Teamcenter.Soa.Client.Model.Strong.PSOccurrenceThread
    OccAttrInfo: list[OccAttrInfo]

class Structure:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateOccAttrObjects(self, Inputs: list[CreateOrUpdateOccAttrObjectsIn]) -> CreateOrUpdateOccAttrObjectsResp: ...
    def GetOccAttrsObjects(self, Inputs: list[GetOccAttrsObjectsIn]) -> GetOccAttrsObjectsResponse: ...

