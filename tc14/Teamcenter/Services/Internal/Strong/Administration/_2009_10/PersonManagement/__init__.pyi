import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class GetPersonPropertiesResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    PersonData: list[PropertyValuesData]

class PropertyValuesData:
    def __init__(self, ) -> None: ...
    PropValues: list[str]

class PersonManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetStringProperties(self, PersonObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: list[str]) -> GetPersonPropertiesResponse: ...
    def SetStringProperties(self, PersonObject: list[Teamcenter.Soa.Client.Model.ModelObject], Attributes: System.Collections.Hashtable) -> Teamcenter.Soa.Client.Model.ServiceData: ...

