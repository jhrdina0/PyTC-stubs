import System
import Teamcenter.Services.Internal.Strong.Core._2017_11.LogicalObject
import Teamcenter.Services.Internal.Strong.Core._2018_06.LogicalObject
import Teamcenter.Soa.Client.Model
import typing

class AddMemAndPresentedPropsWriteInput:
    def __init__(self, ) -> None: ...
    LogicalObjectType: Teamcenter.Soa.Client.Model.ModelObject
    MemberPropertiesDefinitions: list[Teamcenter.Services.Internal.Strong.Core._2018_06.LogicalObject.MemberPropertyDefinition2]
    PresentedPropertiesDefinitions: list[PresentedPropertyDefinition2]

class PresentedPropertyDefinition2:
    def __init__(self, ) -> None: ...
    PresentedPropertyName: str
    DisplayName: str
    Description: str
    RootOrMemberName: str
    SourcePropertyName: str
    IsWritable: bool

class LogicalObject:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddMemAndPresentedPropsWithWrite(self, AddMembersAndPresentedProps: AddMemAndPresentedPropsWriteInput) -> Teamcenter.Services.Internal.Strong.Core._2017_11.LogicalObject.AddMemberAndPresentedPropsResponse: ...

