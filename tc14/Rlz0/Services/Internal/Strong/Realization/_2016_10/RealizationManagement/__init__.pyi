import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateRelationsOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation

class CreateRelationsResponse:
    def __init__(self, ) -> None: ...
    Output: list[CreateRelationsOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Relationship:
    def __init__(self, ) -> None: ...
    ClientId: str
    RelationType: str
    PrimaryObject: Teamcenter.Soa.Client.Model.ModelObject
    SecondaryObject: Teamcenter.Soa.Client.Model.ModelObject
    UserData: Teamcenter.Soa.Client.Model.ModelObject

class RealizationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateRelations(self, Input: list[Relationship]) -> CreateRelationsResponse: ...

