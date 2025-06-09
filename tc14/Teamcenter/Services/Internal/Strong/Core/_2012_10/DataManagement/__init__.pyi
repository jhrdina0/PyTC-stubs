import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CreateInput2:
    def __init__(self, ) -> None: ...
    BoName: str
    PropertyNameValues: System.Collections.Hashtable
    CompoundCreateInput: System.Collections.Hashtable

class CreateIn2:
    def __init__(self, ) -> None: ...
    ClientId: str
    CreateData: CreateInput2
    DataToBeRelated: System.Collections.Hashtable
    WorkflowData: System.Collections.Hashtable
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    PasteProp: str

class CreateOut2:
    def __init__(self, ) -> None: ...
    ClientId: str
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]

class CreateResponse2:
    def __init__(self, ) -> None: ...
    Output: list[CreateOut2]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateRelateAndSubmitObjects(self, Inputs: list[CreateIn2]) -> CreateResponse2: ...

