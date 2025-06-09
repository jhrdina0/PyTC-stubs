import Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AutoFilterValue:
    def __init__(self, ) -> None: ...
    UnitSystem: int
    PropertyValue: str
    Count: int

class ClassDescriptor:
    def __init__(self, ) -> None: ...
    Irdi: str
    ClassNamespace: str
    Id: str
    Revision: str
    Status: str
    ClassType: str
    IsAbstract: bool
    UnitSystem: int
    Name: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    ShortName: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Definition: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Note: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Remark: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    ClassAttributes: list[Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.ClassAttribute]
    AdditionalProperties: System.Collections.Hashtable

class EmptyProperty:
    def __init__(self, ) -> None: ...
    PropertyName: str
    PropertyIdentifier: str
    PropertyAnnotation: str

class FindValueInput:
    def __init__(self, ) -> None: ...
    PropertyID: str
    ClassID: str
    ActiveUnitsystem: int
    FindValuePropertyValues: list[FindValuePropertyValue]

class FindValuePropertyValue:
    def __init__(self, ) -> None: ...
    PropertyID: str
    PropertyValue: str

class FindValuesOutput:
    def __init__(self, ) -> None: ...
    AutoFilterValues: list[AutoFilterValue]

class FindValuesResponse:
    def __init__(self, ) -> None: ...
    FindValuesOutputs: list[FindValuesOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetGraphicsTemplateInfoResponse:
    def __init__(self, ) -> None: ...
    GraphicsTemplateInfos: list[GraphicsTemplateInfos]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GraphicsTemplateInfo:
    def __init__(self, ) -> None: ...
    TemplateType: str
    TemplateName: str
    TemplateObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    Unitsystem: int
    EmptyProperties: list[EmptyProperty]

class GraphicsTemplateInfos:
    def __init__(self, ) -> None: ...
    TemplatesInfos: list[GraphicsTemplateInfo]

class OrderByTerm:
    def __init__(self, ) -> None: ...
    PropertyName: str
    SortAscending: bool

class PropertyValue:
    def __init__(self, ) -> None: ...
    Datatype: str
    BoolValue: list[bool]
    IntValue: list[int]
    DoubleValue: list[float]
    StringValue: list[str]

class SaveGraphicsMemberRequest:
    def __init__(self, ) -> None: ...
    TemplateObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    ClassificationObject: str
    CreatePartFile: bool
    CreateJTFile: bool
    RecreateFromTemplate: bool

class SearchClassDescriptorResponse:
    def __init__(self, ) -> None: ...
    SearchResults: list[SearchClassDescriptorResults]
    ClassDescriptors: System.Collections.Hashtable
    Parents: System.Collections.Hashtable
    Children: System.Collections.Hashtable
    Blocks: System.Collections.Hashtable
    KeyLOVs: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SearchClassDescriptorResult:
    def __init__(self, ) -> None: ...
    ClassIRDI: str
    SelectProperties: list[SelectValue]

class SearchClassDescriptorResults:
    def __init__(self, ) -> None: ...
    ResultStatus: int
    ErrorDetails: list[str]
    TotalFound: int
    TotalLoaded: int
    Results: list[SearchClassDescriptorResult]

class SearchCriteria:
    def __init__(self, ) -> None: ...
    SelectProperties: list[str]
    SearchExpressions: list[SearchExpression]
    OrderByTerms: list[OrderByTerm]
    Limit: int
    Offset: int

class SearchExpression:
    def __init__(self, ) -> None: ...
    OperatorExpression: str
    PropertyName: str
    PropertyValue: PropertyValue

class SearchIcoCriteria:
    def __init__(self, ) -> None: ...
    SelectProperties: list[str]
    SearchExpressions: list[SearchExpression]
    OrderByTerms: list[OrderByTerm]
    SearchInHierarchy: bool
    Offset: int
    Limit: int
    LoadClassificationObjects: bool
    LoadClassDescriptors: bool

class SearchIcoResponse:
    def __init__(self, ) -> None: ...
    SearchResults: list[SearchIcoResults]
    ClassificationObjects: System.Collections.Hashtable
    ClassDescriptors: System.Collections.Hashtable
    Blocks: System.Collections.Hashtable
    KeyLOVs: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SearchIcoResult:
    def __init__(self, ) -> None: ...
    ObjectUID: str
    SelectProperties: list[SelectValue]

class SearchIcoResults:
    def __init__(self, ) -> None: ...
    ResultStatus: int
    ErrorDetails: list[str]
    TotalFound: int
    TotalLoaded: int
    Results: list[SearchIcoResult]

class SelectValue:
    def __init__(self, ) -> None: ...
    PropertyName: str
    PropertyValues: list[PropertyValue]

class Classification:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindValues(self, FindValueInputs: list[FindValueInput]) -> FindValuesResponse: ...
    def GetGraphicsTemplateInfo(self, ClassificationObjects: list[str], ClassificationClasses: list[str]) -> GetGraphicsTemplateInfoResponse: ...
    def SaveGraphicsMember(self, RequestObjects: list[SaveGraphicsMemberRequest]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SearchClassDescriptor(self, SearchCriteria: list[SearchCriteria], Options: int) -> SearchClassDescriptorResponse: ...
    def SearchClassificationObjects(self, SearchCriteria: list[SearchIcoCriteria], Options: int) -> SearchIcoResponse: ...

