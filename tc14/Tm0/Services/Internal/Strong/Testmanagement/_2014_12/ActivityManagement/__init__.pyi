import System
import Teamcenter.Soa.Client.Model
import typing

class TestResultsInputInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    TestActivity: Teamcenter.Soa.Client.Model.ModelObject
    TestInstance: Teamcenter.Soa.Client.Model.ModelObject

class TestResultsOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    TestResults: list[Teamcenter.Soa.Client.Model.ModelObject]

class TestResultsResponse:
    def __init__(self, ) -> None: ...
    TestResultsOutput: list[TestResultsOutput]
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData

class ActivityManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTestResults(self, Inputs: list[TestResultsInputInfo]) -> TestResultsResponse: ...

