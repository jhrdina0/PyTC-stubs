import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Core._2017_11.LogicalObject
import Teamcenter.Soa.Client.Model
import typing

class AddMembersPresentedPropsInput2:
    def __init__(self, ) -> None: ...
    LogicalObjectType: Teamcenter.Soa.Client.Model.ModelObject
    MemberPropertiesDefinitions: list[MemberPropertyDefinition2]
    PresentedPropertiesDefinitions: list[Teamcenter.Services.Internal.Strong.Core._2017_11.LogicalObject.PresentedPropertyDefinition]

class LogicalObjectTypeInput2:
    def __init__(self, ) -> None: ...
    Name: str
    DisplayName: str
    Description: str
    RootTypeName: str
    ParentTypeName: str
    RetrieveClassificationData: bool
    MemberPropertyDefinitions: list[MemberPropertyDefinition2]
    PresentedPropertyDefinitions: list[Teamcenter.Services.Internal.Strong.Core._2017_11.LogicalObject.PresentedPropertyDefinition]

class MemberPropertyDefinition2:
    def __init__(self, ) -> None: ...
    MemberPropertyName: str
    DisplayName: str
    Description: str
    TraversalPath: list[TraversalHop2]
    RetrieveClassificationData: bool

class TraversalHop2:
    def __init__(self, ) -> None: ...
    PropertyName: str
    PropertyType: str
    DestinationType: str
    Direction: str
    DestinationObjectCriteria: str

class UpdateMemberInput:
    def __init__(self, ) -> None: ...
    LogicalObjectType: Teamcenter.Soa.Client.Model.ModelObject
    MembersToBeUpdated: System.Collections.Hashtable

class LogicalObject:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddMembersAndPresentedProps2(self, AddMembersAndPresentedProps: AddMembersPresentedPropsInput2) -> Teamcenter.Services.Internal.Strong.Core._2017_11.LogicalObject.AddMemberAndPresentedPropsResponse: ...
    def CreateLogicalObjectTypes2(self, LogicalObjectTypeInputs: list[LogicalObjectTypeInput2]) -> Teamcenter.Services.Internal.Strong.Core._2017_11.LogicalObject.LogicalObjectTypeResponse: ...
    def UpdateMembers(self, UpdateMemberInputStruct: UpdateMemberInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...

