import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class TestStepInfo:
    def __init__(self, ) -> None: ...
    Contents: list[TextSegmentOrPlaceholderInfo]

class TestStepsInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    BomLineScope: Teamcenter.Soa.Client.Model.ModelObject
    TestObject: Teamcenter.Soa.Client.Model.ModelObject
    CustomProps: System.Collections.Hashtable

class TestStepsResponse:
    def __init__(self, ) -> None: ...
    StepResults: list[TestStepsResult]
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData

class TestStepsResult:
    def __init__(self, ) -> None: ...
    ClientId: str
    Steps: list[TestStepInfo]

class TextSegmentOrPlaceholderInfo:
    def __init__(self, ) -> None: ...
    ElementType: str
    UiValue: str
    AllowedTypes: str
    Bomlines: list[Teamcenter.Soa.Client.Model.ModelObject]
    PlaceholderStatus: str
    CustomProps: System.Collections.Hashtable

class InstanceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTestSteps(self, Inputs: list[TestStepsInputInfo]) -> TestStepsResponse: ...

