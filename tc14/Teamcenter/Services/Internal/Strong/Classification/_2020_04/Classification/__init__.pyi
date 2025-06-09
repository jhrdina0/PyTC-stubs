import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Classification._2017_05.Classification
import Teamcenter.Services.Strong.Classification._2007_01.Classification
import Teamcenter.Services.Strong.Classification._2009_10.Classification
import Teamcenter.Soa.Client.Model
import typing

class ClassAttributeInfo:
    def __init__(self, ) -> None: ...
    Id: int
    Name: str
    ShortName: str
    Description: str
    MetricFormat: Teamcenter.Services.Internal.Strong.Classification._2017_05.Classification.FormatPropertiesNX
    NonMetricFormat: Teamcenter.Services.Internal.Strong.Classification._2017_05.Classification.FormatPropertiesNX
    Annotation: str
    AttributeConfiguration: Teamcenter.Services.Strong.Classification._2009_10.Classification.AttributeConfiguration
    ArraySize: int
    Options: int
    DependencyAttribute: str
    DependencyConfiguration: str
    ExtendedProperties: list[ExtendedPropertyInfo]
    ConfiguredKeyLOV: Teamcenter.Services.Strong.Classification._2009_10.Classification.KeyLOVDefinition2

class ClassificationObjectInformation:
    def __init__(self, ) -> None: ...
    ClsObject: Teamcenter.Soa.Client.Model.ModelObject
    ClsObjId: str
    ClassId: str
    Unit: str
    Properties: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.ClassificationProperty]
    Relations: list[Teamcenter.Soa.Client.Model.ModelObject]

class ClassInformation:
    def __init__(self, ) -> None: ...
    Id: str
    Parent: str
    Name: str
    ShortName: str
    Description: str
    UnitSystem: str
    IsAbstract: bool
    IsGroup: bool
    IsAssembly: bool
    UserData1: str
    UserData2: str
    Documents: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.TypedDocument]
    ClassAttributesInfo: list[ClassAttributeInfo]

class ExtendedPropertyInfo:
    def __init__(self, ) -> None: ...
    PropName: str
    PropValue: list[str]

class FindClassificationInfoRequest:
    def __init__(self, ) -> None: ...
    WorkspaceObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    RelationTypes: list[str]

class FindClassificationInfoResponse:
    def __init__(self, ) -> None: ...
    ClassificationObjectsInfoMap: System.Collections.Hashtable
    ClassInfoMap: System.Collections.Hashtable
    KeylovInfoMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Classification:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindClassificationInfo(self, Request: list[FindClassificationInfoRequest], Options: int) -> FindClassificationInfoResponse: ...

