import Teamcenter.Soa.Client.Model
import typing

class GetSubscribableTypesAndSubtypesResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    TypesNames: list[TypesAndSubtypesData]

class TypesAndSubtypesData:
    def __init__(self, ) -> None: ...
    DisplayName: str
    TypeName: str

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSubscribableTypesAndSubTypes(self, ChildTypeOption: str) -> GetSubscribableTypesAndSubtypesResponse: ...

