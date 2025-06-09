import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Tm0.Services.Internal.Strong.Testmanagement._2014_12.InstanceManagement
import typing

class CreateObjectInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    TypeName: str
    ObjectName: str
    AssignedToLine: Teamcenter.Soa.Client.Model.ModelObject
    ExecutionScopeLine: Teamcenter.Soa.Client.Model.ModelObject
    ReferenceBOMWindow: Teamcenter.Soa.Client.Model.ModelObject
    TestCase: Teamcenter.Soa.Client.Model.ModelObject
    TestSteps: list[Tm0.Services.Internal.Strong.Testmanagement._2014_12.InstanceManagement.TestStepInfo]
    BoolProps: System.Collections.Hashtable
    DateProps: System.Collections.Hashtable
    DoubleProps: System.Collections.Hashtable
    IntProps: System.Collections.Hashtable
    ObjectProps: System.Collections.Hashtable
    StringProps: System.Collections.Hashtable
    PrimaryRelations: System.Collections.Hashtable
    SecondaryRelations: System.Collections.Hashtable

class CreateObjectsResponse:
    def __init__(self, ) -> None: ...
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData
    ResultMap: System.Collections.Hashtable

class EditObjectInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    ObjectToEdit: Teamcenter.Soa.Client.Model.ModelObject
    AssignedToLine: Teamcenter.Soa.Client.Model.ModelObject
    ExecutionScopeLine: Teamcenter.Soa.Client.Model.ModelObject
    ReferenceBOMWindow: Teamcenter.Soa.Client.Model.ModelObject
    TestCase: Teamcenter.Soa.Client.Model.ModelObject
    TestSteps: list[Tm0.Services.Internal.Strong.Testmanagement._2014_12.InstanceManagement.TestStepInfo]
    BoolProps: System.Collections.Hashtable
    DateProps: System.Collections.Hashtable
    DoubleProps: System.Collections.Hashtable
    IntProps: System.Collections.Hashtable
    ObjectProps: System.Collections.Hashtable
    StringProps: System.Collections.Hashtable
    PrimaryRelations: System.Collections.Hashtable
    SecondaryRelations: System.Collections.Hashtable

class TestInstancesSearchCriteria:
    def __init__(self, ) -> None: ...
    ClientId: str
    SearchScope: Teamcenter.Soa.Client.Model.ModelObject
    ExecutionScope: Teamcenter.Soa.Client.Model.ModelObject
    TestCase: Teamcenter.Soa.Client.Model.ModelObject
    SearchDate: System.DateTime
    SearchDateOperator: str
    ResultStatus: str
    ReferredObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    BoolProps: System.Collections.Hashtable
    DateProps: System.Collections.Hashtable
    DoubleProps: System.Collections.Hashtable
    IntProps: System.Collections.Hashtable
    ObjectProps: System.Collections.Hashtable
    StringProps: System.Collections.Hashtable

class TestInstancesSearchResponse:
    def __init__(self, ) -> None: ...
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData
    ResultMap: System.Collections.Hashtable

class TestInstancesSearchResult:
    def __init__(self, ) -> None: ...
    TestInstance: Teamcenter.Soa.Client.Model.ModelObject
    AssignedTo: Teamcenter.Soa.Client.Model.ModelObject
    ExecutionScope: Teamcenter.Soa.Client.Model.ModelObject
    Activities: list[Teamcenter.Soa.Client.Model.ModelObject]

class InstanceManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateObjects(self, Inputs: list[CreateObjectInfo]) -> CreateObjectsResponse: ...
    def EditObjects(self, InputData: list[EditObjectInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetTestInstances(self, Inputs: list[TestInstancesSearchCriteria]) -> TestInstancesSearchResponse: ...

