import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateBOEfromPlantBOPResponse:
    def __init__(self, ) -> None: ...
    BoeStructureTopLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LinkBOPtoBOEObjectInfo:
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    TargetLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    ClientID: str

class LinkedRelationObject:
    def __init__(self, ) -> None: ...
    ClientId: str
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation

class LinkPlantBOPtoBOEResponse:
    def __init__(self, ) -> None: ...
    RelationObjects: list[LinkedRelationObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SynchronizeBOPAndBOEInputInfo:
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    TargetLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    RemoveObsoleteTwin: bool
    ClientID: str

class SynchronizePlantBOPAndBOEOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Relations: list[Teamcenter.Soa.Client.Model.Strong.ImanRelation]

class SynchronizePlantBOPAndBOEResponse:
    def __init__(self, ) -> None: ...
    SynchronizePlantBOPAndBOEOutput: list[SynchronizePlantBOPAndBOEOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def LinkPlantBOPtoBOE(self, LinkBOPtoBOEObjectInfo: list[LinkBOPtoBOEObjectInfo]) -> LinkPlantBOPtoBOEResponse: ...
    def SynchronizePlantBOPAndBOE(self, SynchronizeBopAndBoeInputInfo: list[SynchronizeBOPAndBOEInputInfo]) -> SynchronizePlantBOPAndBOEResponse: ...
    def CreateBOEfromPlantBOP(self, RootBOPLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> CreateBOEfromPlantBOPResponse: ...

