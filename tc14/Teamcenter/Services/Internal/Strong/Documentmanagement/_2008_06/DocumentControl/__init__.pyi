import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class IRDCResponse:
    def __init__(self, ) -> None: ...
    OutIRDC: list[Teamcenter.Soa.Client.Model.Strong.IRDC]
    SvcData: Teamcenter.Soa.Client.Model.ServiceData

class DocumentControl:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetIRDCs(self, ItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> IRDCResponse: ...

