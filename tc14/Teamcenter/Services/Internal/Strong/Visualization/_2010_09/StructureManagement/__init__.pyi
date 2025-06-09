import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateVisSCInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    TopLine: Teamcenter.Soa.Client.Model.ModelObject
    OccurrencesList: list[str]
    StaticStructureFile: Teamcenter.Soa.Client.Model.ModelObject

class CreateVisSCOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    StructureRecipe: Teamcenter.Soa.Client.Model.Strong.VisStructureContext

class CreateVisSCResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreateVisSCOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateVisSC(self, Info: list[CreateVisSCInfo]) -> CreateVisSCResponse: ...

