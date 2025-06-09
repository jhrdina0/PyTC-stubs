import Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification
import Cla0.Services.Internal.Strong.Classificationcommon._2021_06.Classification
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AttributeFormat3:
    def __init__(self, ) -> None: ...
    IsUnsigned: bool
    Precision: int
    Scale: int
    Unit: str
    KeyLOV: str
    NumberOfDigits: int
    NxUnitID: str
    DisplayOptions: int
    DefaultValue: str
    MinValue: str
    MaxValue: str

class AttributeDataType3:
    def __init__(self, ) -> None: ...
    Type: str
    IsLocalizable: bool
    IsOptimized: bool
    IsProtected: bool
    IsRequired: bool
    IsPolymorphicController: bool
    BlockReference: str
    CardinalityController: str
    NonMetricFormat: AttributeFormat3
    MetricFormat: AttributeFormat3

class ClassAttribute3:
    def __init__(self, ) -> None: ...
    AttributeIndex: int
    DbIndex: int
    Type: str
    Reference: str
    Cardinality: int
    Annotation: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Name: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    DataType: AttributeDataType3
    UserData: list[Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.UserDataEntry]
    AdditionalProperties: list[Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.AdditionalProperties]
    Definition: str
    Note: str

class ClassDescriptor3:
    def __init__(self, ) -> None: ...
    Irdi: str
    ClassNamespace: str
    Id: str
    Revision: str
    Status: str
    ClassType: str
    IsAbstract: bool
    HasChildren: bool
    ChildCount: int
    UnitSystem: int
    Name: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Parent: str
    ShortName: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Definition: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Note: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Remark: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    ClassAttributes: list[ClassAttribute3]
    AdditionalProperties: System.Collections.Hashtable

class LOVItems2:
    def __init__(self, ) -> None: ...
    DataType: str
    IntegerItems: list[LOVIntegerItems2]
    DoubleItems: list[LOVDoubleItems2]
    StringItems: list[LOVStringItems2]
    BoolItems: list[LOVBooleanItems2]
    DateItems: list[LOVDateItems2]
    ReferenceItems: list[LOVReferenceItems2]

class KeyLOVDefinition2:
    def __init__(self, ) -> None: ...
    ObjectType: str
    Irdi: str
    KeyLOVNamespace: str
    Id: str
    Revision: str
    Status: str
    Name: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    IsHideKeys: bool
    KeyLOVItems: LOVItems2

class LOVBooleanItems2:
    def __init__(self, ) -> None: ...
    BoolValue: bool
    DisplayValue: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    ValueMeaning: str
    IsDeprecated: bool

class LOVDateItems2:
    def __init__(self, ) -> None: ...
    DateValue: str
    ValueMeaning: str
    IsDeprecated: bool
    IsSubMenu: bool
    IsSeparator: bool
    SubMenuTitle: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    DependencyKey: str
    SubMenuItems: list[LOVDateItems2]

class LOVDoubleItems2:
    def __init__(self, ) -> None: ...
    ValueMeaning: str
    DoubleValue: float
    IsDeprecated: bool
    IsSuMenu: bool
    IsSeperator: bool
    SubMenuTitle: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    DependencyKey: str
    SubMenuItems: list[LOVDoubleItems2]

class LOVIntegerItems2:
    def __init__(self, ) -> None: ...
    IntegerValue: int
    ValueMeaning: str
    IsDeprecated: bool
    IsSubMenu: bool
    IsSeparator: bool
    SubMenuTitle: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    DependencyKey: str
    SubMenuItems: list[LOVIntegerItems2]

class LOVReferenceItems2:
    def __init__(self, ) -> None: ...
    StringValue: str
    DisplayValue: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    ValueMeaning: str
    BlockReference: str
    IsDeprecated: bool

class LOVStringItems2:
    def __init__(self, ) -> None: ...
    StringValue: str
    DisplayValue: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    IsDeprecated: bool
    IsSubMenu: bool
    IsSeparator: bool
    ValueMeaning: str
    SubMenuTitle: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    DependencyKey: str
    SubMenuItems: list[LOVStringItems2]

class SearchClassDescriptorResponse3:
    def __init__(self, ) -> None: ...
    SearchResults: list[Cla0.Services.Internal.Strong.Classificationcommon._2021_06.Classification.SearchClassDescriptorResults]
    ClassDescriptors: System.Collections.Hashtable
    Parents: System.Collections.Hashtable
    Children: System.Collections.Hashtable
    Blocks: System.Collections.Hashtable
    KeyLOVs: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class Classification:
    def __init__(self , *args: typing.Any) -> None: ...
    def SearchClassDescriptor3(self, SearchCriteria: list[Cla0.Services.Internal.Strong.Classificationcommon._2021_06.Classification.SearchCriteria], Options: int) -> SearchClassDescriptorResponse3: ...

