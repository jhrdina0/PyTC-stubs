import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ValidationContext:
    def __init__(self, ) -> None: ...
    ValAgent: Teamcenter.Soa.Client.Model.Strong.POM_object
    ValDataList: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    BusinessObjectArrayContexts: System.Collections.Hashtable

class NXValidation:
    def __init__(self , *args: typing.Any) -> None: ...
    def RunValidations(self, ValidationContextList: list[ValidationContext]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

