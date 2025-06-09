import System
import Teamcenter.Soa.Client.Model
import typing

class AddMemberAndPresentedPropsResponse:
    def __init__(self, ) -> None: ...
    MemberOrPresentedProps: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AddMembersPresentedPropsInput:
    def __init__(self, ) -> None: ...
    LogicalObjectType: Teamcenter.Soa.Client.Model.ModelObject
    MemberDefinitions: list[MemberPropertyDefinition]
    PresentedPropertiesDefinitions: list[PresentedPropertyDefinition]

class DeleteMembersPresentedPropsInput:
    def __init__(self, ) -> None: ...
    LogicalObject: Teamcenter.Soa.Client.Model.ModelObject
    MemberIdsOrPresentedProps: list[str]

class LogicalObjectTypeInput:
    def __init__(self, ) -> None: ...
    Name: str
    DisplayName: str
    Description: str
    RootTypeName: str
    ParentTypeName: str
    RetrieveClassificationData: bool
    MemberPropertyDefinitions: list[MemberPropertyDefinition]
    PresentedPropertyDefinitions: list[PresentedPropertyDefinition]

class LogicalObjectTypeResponse:
    def __init__(self, ) -> None: ...
    LoTypes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MemberPropertyDefinition:
    def __init__(self, ) -> None: ...
    MemberPropertyName: str
    DisplayName: str
    Description: str
    TraversalPath: list[TraversalHop]
    RetrieveClassificationData: bool

class PresentedPropertyDefinition:
    def __init__(self, ) -> None: ...
    PresentedPropertyName: str
    DisplayName: str
    Description: str
    RootOrMemberName: str
    SourcePropertyName: str

class TraversalHop:
    def __init__(self, ) -> None: ...
    PropertyName: str
    PropertyType: str
    DestinationType: str
    Direction: str

class LogicalObject:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddMembersAndPresentedProps(self, AddMembersAndPresentedProps: AddMembersPresentedPropsInput) -> AddMemberAndPresentedPropsResponse: ...
    def CreateLogicalObjectTypes(self, LogicalObjectTypeInputs: list[LogicalObjectTypeInput]) -> LogicalObjectTypeResponse: ...
    def DeleteLogicalObjectTypes(self, LogicalObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteMembersAndPresentedProps(self, DeleteMembersAndPresentedProps: list[DeleteMembersPresentedPropsInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

