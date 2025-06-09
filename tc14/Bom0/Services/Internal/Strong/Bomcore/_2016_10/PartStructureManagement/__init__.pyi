import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetPartStructureResponse:
    def __init__(self, ) -> None: ...
    PartStructureWindow: Teamcenter.Soa.Client.Model.Strong.Bom0PartStructureWindow
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PartStructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPartStructure(self, Part: Teamcenter.Soa.Client.Model.Strong.Bom0AbstractPart, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, IncludeAlignedDesignInfo: bool) -> GetPartStructureResponse: ...

