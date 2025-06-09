import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CleanDynamicIPALinesInfo:
    def __init__(self, ) -> None: ...
    InputBOPLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    CleanSubHierarchy: bool

class GetDynamicIPALinesResponse:
    def __init__(self, ) -> None: ...
    BopLineToIPALines: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class IPAManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CleanDynamicIPALines(self, Input: CleanDynamicIPALinesInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetDynamicIPALines(self, InputBOPLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetDynamicIPALinesResponse: ...

