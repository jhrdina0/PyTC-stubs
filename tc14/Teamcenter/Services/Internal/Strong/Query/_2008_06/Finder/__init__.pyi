import System
import Teamcenter.Soa.Client.Model
import typing

class FindObjectsAttrAndValues:
    def __init__(self, ) -> None: ...
    AttrName: str
    Values: list[str]

class FindObjectsInput:
    def __init__(self, ) -> None: ...
    ClassName: str
    ClientId: str
    OutputAttributeNames: list[str]
    AttrAndValues: list[FindObjectsAttrAndValues]

class FindObjectsResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Result: list[Teamcenter.Soa.Client.Model.ModelObject]
    AttrAndValues: list[FindObjectsAttrAndValues]

class Finder:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindObjectsByClassAndAttributes(self, Input: FindObjectsInput) -> FindObjectsResponse: ...

