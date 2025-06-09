import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2008_03.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MappedDatasetAttrPropertyInfoForNX:
    def __init__(self, ) -> None: ...
    CadAttrMappingDefinition: Teamcenter.Soa.Client.Model.Strong.CadAttrMappingDefinition
    ResolvedObject: Teamcenter.Soa.Client.Model.ModelObject
    ResolvedPropertyName: str

class NxFrozenAndModifiableInfo:
    def __init__(self, ) -> None: ...
    IsModifiable: bool
    IsFrozen: bool

class NxResolvedConstOrPrefAttrInfo:
    def __init__(self, ) -> None: ...
    IsFrozen: bool
    Value: str

class ResolveAttrMappingsForNXResponse:
    def __init__(self, ) -> None: ...
    ResolvedMappingsMap: System.Collections.Hashtable
    FrozenAndModifiableInfoMap: System.Collections.Hashtable
    ResolvedConstOrPrefAttrInfoMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ResolveAttrMappingsForNX(self, Info: list[Teamcenter.Services.Strong.Cad._2008_03.DataManagement.ResolveAttrMappingsInfo]) -> ResolveAttrMappingsForNXResponse: ...

