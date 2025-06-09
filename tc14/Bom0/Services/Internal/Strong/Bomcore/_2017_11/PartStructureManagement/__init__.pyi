import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class PartStructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def DeletePartStructures(self, PbeLinesToDelete: list[Teamcenter.Soa.Client.Model.Strong.Bom0PBELine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

