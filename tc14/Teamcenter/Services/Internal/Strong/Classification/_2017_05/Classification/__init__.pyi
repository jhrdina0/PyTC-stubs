import System
import System.Collections
import Teamcenter.Services.Strong.Classification._2007_01.Classification
import Teamcenter.Services.Strong.Classification._2009_10.Classification
import Teamcenter.Soa.Client.Model
import typing

class FormatPropertiesNX:
    def __init__(self, ) -> None: ...
    Format: Teamcenter.Services.Strong.Classification._2007_01.Classification.AttributeFormat
    UnitDisplayName: str
    UnitID: str
    NxUnitID: str
    DefaultValue: str
    MinimumValue: str
    MaximumValue: str

class ClassAttributeNX:
    def __init__(self, ) -> None: ...
    Id: int
    Name: str
    ShortName: str
    Description: str
    MetricFormat: FormatPropertiesNX
    NonMetricFormat: FormatPropertiesNX
    Annotation: str
    AttributeConfiguration: Teamcenter.Services.Strong.Classification._2009_10.Classification.AttributeConfiguration
    ArraySize: int
    Options: int
    DependencyAttribute: str
    DependencyConfiguration: str
    ExtendedProperties: list[Teamcenter.Services.Strong.Classification._2009_10.Classification.ExtendedProeprty]

class ClassAttributesDefinitionNX:
    def __init__(self, ) -> None: ...
    ClassAttributes: list[ClassAttributeNX]
    ConfiguredKeyLOVs: System.Collections.Hashtable

class GetClassDefinitionsResponseNX:
    def __init__(self, ) -> None: ...
    ClassDefinitionMap: System.Collections.Hashtable
    ClassAttributesMap: System.Collections.Hashtable
    KeylovDefintion: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Classification:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetClassDefinitionsNX(self, ClassIDs: list[str]) -> GetClassDefinitionsResponseNX: ...

