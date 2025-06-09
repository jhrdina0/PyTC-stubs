import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AddPropsOnTypeInput:
    def __init__(self, ) -> None: ...
    Type: str
    PropDefinitions: list[PropertyDefinition]

class PropertyDefinition:
    def __init__(self, ) -> None: ...
    Name: str
    DisplayName: str
    Description: str
    PropertyStorageType: str
    PropertyOptions: System.Collections.Hashtable
    PropertyType: str

class TypeDefinition:
    def __init__(self, ) -> None: ...
    Name: str
    DisplayName: str
    ParentTypeName: str
    TypeClassName: str
    Description: str
    CreatePrimaryBusinessObject: bool
    IsAbstract: bool
    TypeOptions: System.Collections.Hashtable

class TypeInput:
    def __init__(self, ) -> None: ...
    TypeDefinition: TypeDefinition
    TypeInputsMap: System.Collections.Hashtable
    DataModelOptions: System.Collections.Hashtable

class ActiveModeler:
    def __init__(self , *args: typing.Any) -> None: ...
    def AddPropertiesOnTypes(self, AddPropsOnTypeInputs: list[AddPropsOnTypeInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateTypes(self, TypeInput: list[TypeInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

