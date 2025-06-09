import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateInput:
    def __init__(self, ) -> None: ...
    ClientId: str
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
    BusinessObjectProps: System.Collections.Hashtable
    BusinessObjectArrayProps: System.Collections.Hashtable
    CompoundCreateInput: System.Collections.Hashtable

class ValidationResultPropInfo:
    def __init__(self, ) -> None: ...
    StringProps: System.Collections.Hashtable
    StringArrayProps: System.Collections.Hashtable
    BusinessObjectProps: System.Collections.Hashtable
    BusinessObjectArrayProps: System.Collections.Hashtable

class DeleteResultsInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    AgentName: str
    CheckerClassName: str
    ValidationId: str
    TargetContextObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    CheckerReferencedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    EffectivityFormula: str
    VariantFormula: str
    AdditionalPropInfo: ValidationResultPropInfo

class GetResultsInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    AgentName: str
    TargetContextObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    CheckerReferencedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    EffectivityFormula: str
    VariantFormula: str
    AdditionalPropInfo: ValidationResultPropInfo

class NXValidation:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateValidationResults(self, CreateOrUpdateInputs: list[CreateInput], GetResultsInputs: list[GetResultsInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteValidationResults(self, DeleteResultsInputs: list[DeleteResultsInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetValidationResults(self, GetResultsInputs: list[GetResultsInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

