import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateInput:
    def __init__(self, ) -> None: ...
    BoName: str
    StringProps: System.Collections.Hashtable
    StringArrayProps: System.Collections.Hashtable
    DoubleProps: System.Collections.Hashtable
    DoubleArrayProps: System.Collections.Hashtable
    FloatProps: System.Collections.Hashtable
    FloatArrayProps: System.Collections.Hashtable
    IntProps: System.Collections.Hashtable
    IntArrayProps: System.Collections.Hashtable
    BoolProps: System.Collections.Hashtable
    BoolArrayProps: System.Collections.Hashtable
    DateProps: System.Collections.Hashtable
    DateArrayProps: System.Collections.Hashtable
    ObjectProps: System.Collections.Hashtable
    ObjectArrayProps: System.Collections.Hashtable
    CompoundCreateInput: System.Collections.Hashtable

class CreateIn:
    def __init__(self, ) -> None: ...
    ClientId: str
    Data: CreateInput

class GenerateDesignContextOption:
    def __init__(self, ) -> None: ...
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    Models: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel]
    ProximityDistance: float

class GenerateDesignContextInfo:
    def __init__(self, ) -> None: ...
    CreateInput: CreateIn
    Option: GenerateDesignContextOption
    DesignItems: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]

class GenerateDesignContextResponse:
    def __init__(self, ) -> None: ...
    ClientIdMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateDesignContext(self, DesignContextInfos: list[GenerateDesignContextInfo]) -> GenerateDesignContextResponse: ...

