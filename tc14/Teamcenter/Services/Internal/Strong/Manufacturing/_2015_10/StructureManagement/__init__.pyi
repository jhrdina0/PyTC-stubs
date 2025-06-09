import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AdditionalInfo:
    def __init__(self, ) -> None: ...
    StrToDateVectorMap: System.Collections.Hashtable
    StrToDoubleVectorMap: System.Collections.Hashtable
    StrToStrVectorMap: System.Collections.Hashtable
    StrToObjVectorMap: System.Collections.Hashtable
    StrToIntVectorMap: System.Collections.Hashtable

class AlignLinesInBOMData:
    def __init__(self, ) -> None: ...
    ScopeElements: list[AlignmentScopeElement]
    EquivalentLines: list[EquivalentLinesPair]
    AlignmentMode: str
    AlignProperties: bool
    AlignAllAssemblies: bool
    AdditionalInfo: AdditionalInfo

class AlignLinesInBOMResponse:
    def __init__(self, ) -> None: ...
    LogTickets: list[str]
    Summaries: list[AlignmentSummary]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AdditionalInfo: AdditionalInfo

class AlignmentScopeElement:
    def __init__(self, ) -> None: ...
    SourceScope: Teamcenter.Soa.Client.Model.ModelObject
    TargetScopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    ReusedNodes: list[Teamcenter.Soa.Client.Model.ModelObject]

class AlignmentSummary:
    def __init__(self, ) -> None: ...
    Aligned: int
    NotAlignedWithError: int
    NotAlignedUnderReused: int

class Attachment:
    def __init__(self, ) -> None: ...
    RelationName: str
    Action: str
    Secondary: Teamcenter.Soa.Client.Model.ModelObject

class EquivalentLinesPair:
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.ModelObject
    TargetLine: Teamcenter.Soa.Client.Model.ModelObject

class EquivalentPropertyNames:
    def __init__(self, ) -> None: ...
    PropertyCategory: str
    PropertyNames: list[str]

class GetEquivalentPropValuesElement:
    def __init__(self, ) -> None: ...
    PropertyNamesByCategory: list[EquivalentPropertyNames]
    OriginalItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    NewItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision

class GetEquivalentPropValuesResp:
    def __init__(self, ) -> None: ...
    EquivalentPropValuesElements: list[GetEquivalentPropValuesRespElem]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetEquivalentPropValuesRespElem:
    def __init__(self, ) -> None: ...
    PropertyCategory: str
    EquivalentPropertyValues: list[PropertyNamePairValue]
    Attachments: list[Attachment]

class PasteOrReplaceAssemblyInContextInfo:
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    NewObject: Teamcenter.Soa.Client.Model.ModelObject
    AdditionalInfo: AdditionalInfo

class PasteOrReplaceAssemblyInContextResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AdditionalInfo: AdditionalInfo

class PropertyNamePairValue:
    def __init__(self, ) -> None: ...
    SourcePropName: str
    TargetPropName: str
    SourceValue: str

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def AlignLinesInBOM(self, AlignInputs: list[AlignLinesInBOMData]) -> AlignLinesInBOMResponse: ...
    def GetEquivalentPropertyValues(self, Input: list[GetEquivalentPropValuesElement]) -> GetEquivalentPropValuesResp: ...
    def PasteOrReplaceAssemblyInContext(self, AssemblyInContextInput: list[PasteOrReplaceAssemblyInContextInfo]) -> PasteOrReplaceAssemblyInContextResponse: ...

