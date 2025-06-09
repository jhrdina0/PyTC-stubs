import System
import Teamcenter.Soa.Client.Model
import Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement
import typing

class BOMLineCloneStableIdChainInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    CloneStableIdChain: str
    BomWindow: Teamcenter.Soa.Client.Model.ModelObject

class BOMLineCloneStableIdChainOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    BomLines: list[Teamcenter.Soa.Client.Model.ModelObject]

class BOMLineCloneStableIdChainResponse:
    def __init__(self, ) -> None: ...
    BomLinesOutput: list[BOMLineCloneStableIdChainOutput]
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData

class EditTestInstanceInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    TestInstance: Teamcenter.Soa.Client.Model.ModelObject
    TestName: str
    TestType: str
    ExecutionSystem: str
    ExecutionScope: str
    TestSteps: str
    OwningObject: Teamcenter.Soa.Client.Model.ModelObject
    OwningUserName: str

class TestCaseInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    ItemId: str
    RevisionId: str
    TestCaseName: str
    TestType: str
    ExecutionSystem: str
    ExpectedResult: str
    Steps: str

class TestCaseResult:
    def __init__(self, ) -> None: ...
    ClientId: str
    TestCaseItem: Teamcenter.Soa.Client.Model.ModelObject
    TestCaseRev: Teamcenter.Soa.Client.Model.ModelObject

class TestCasesResponse:
    def __init__(self, ) -> None: ...
    TestCaseResults: list[TestCaseResult]
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData

class TestInstFromTestCaseInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    TestName: str
    TestType: str
    ExecutionSystem: str
    ExecutionScope: str
    TestSteps: str
    TestCase: Teamcenter.Soa.Client.Model.ModelObject
    OwningObject: Teamcenter.Soa.Client.Model.ModelObject
    OwningUserName: str

class TestStepInfo:
    def __init__(self, ) -> None: ...
    Contents: list[TextSegmentOrPlaceMarkInfo]

class TestStepsInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    BomLineScope: Teamcenter.Soa.Client.Model.ModelObject
    TestObject: Teamcenter.Soa.Client.Model.ModelObject

class TestStepsResponse:
    def __init__(self, ) -> None: ...
    StepResults: list[TestStepsResult]
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData

class TestStepsResult:
    def __init__(self, ) -> None: ...
    ClientId: str
    StepsDescription: str
    Steps: list[TestStepInfo]

class TextSegmentOrPlaceMarkInfo:
    def __init__(self, ) -> None: ...
    ElementType: str
    TextSegOrPlaceMarkValue: str
    AllowedTypes: str
    MultipleObjects: bool
    Bomlines: list[Teamcenter.Soa.Client.Model.ModelObject]

class InstanceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateTestCases(self, Inputs: list[TestCaseInputInfo]) -> TestCasesResponse: ...
    def CreateTestInstancesFromTestCase(self, Inputs: list[TestInstFromTestCaseInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstancesResponse: ...
    def EditTestInstances(self, Inputs: list[EditTestInstanceInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstancesResponse: ...
    def GetBOMLinesFromCloneStableIdChain(self, Inputs: list[BOMLineCloneStableIdChainInputInfo]) -> BOMLineCloneStableIdChainResponse: ...
    def GetTestSteps(self, Inputs: list[TestStepsInputInfo]) -> TestStepsResponse: ...

