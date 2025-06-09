import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class InvalidAssociation:
    def __init__(self, ) -> None: ...
    AssociationType: str
    Primary: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Secondary: Teamcenter.Soa.Client.Model.Strong.BOMLine
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    Reason: str

class ValidateInStructureAssociationsResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    FailedAssociations: list[InvalidAssociation]

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ValidateInStructureAssociations(self, AssociationType: str, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], NumLevels: int) -> ValidateInStructureAssociationsResponse: ...

