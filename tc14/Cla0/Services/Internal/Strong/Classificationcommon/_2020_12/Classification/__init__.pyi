import System
import Teamcenter.Soa.Client.Model
import typing

class AdditionalProperties:
    def __init__(self, ) -> None: ...
    PropertyName: str
    Index: int
    PropertyValue: str

class AttributeFormat:
    def __init__(self, ) -> None: ...
    Precision: int
    Scale: int
    Unit: str
    KeyLOV: str
    NumberOfDigits: int
    NxUnitID: str

class AttributeDataType:
    def __init__(self, ) -> None: ...
    Type: str
    NumberOfDigits: int
    MaxLength: int
    IsLocalizable: bool
    IsPolymorphicController: bool
    BlockReference: str
    CardinalityController: str
    NonMetricFormat: AttributeFormat
    MetricFormat: AttributeFormat

class AxisValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    PosX: float
    PosY: float
    PosZ: float
    RotX: float
    RotY: float
    RotZ: float
    Unit: str

class BlockPropertyValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    ClassDefinitionIRDI: str
    Properties: list[ClassificationProperty]

class BooleanValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    BoolVal: bool

class L10NProperty:
    def __init__(self, ) -> None: ...
    Locale: str
    IsMasterLocale: bool
    TranslationStatus: str
    StrValue: str
    Translations: list[L10NTranslation]

class ClassAttribute:
    def __init__(self, ) -> None: ...
    AttributeIndex: int
    DbIndex: int
    Type: str
    Reference: str
    Cardinality: int
    Annotation: L10NProperty
    Name: L10NProperty
    DataType: AttributeDataType
    UserData: list[UserDataEntry]
    AdditionalProperties: list[AdditionalProperties]

class ClassDefinition:
    def __init__(self, ) -> None: ...
    Irdi: str
    ClassNamespace: str
    Id: str
    Revision: str
    Status: str
    ClassType: str
    IsAbstract: bool
    UnitSystem: int
    Name: L10NProperty
    ShortName: L10NProperty
    Definition: L10NProperty
    Note: L10NProperty
    Remark: L10NProperty
    ClassAttributes: list[ClassAttribute]
    AdditionalProperties: list[AdditionalProperties]

class ClassificationObject:
    def __init__(self, ) -> None: ...
    ClassificationObjectUID: str
    ObjectID: str
    ClassifiedObjectUID: str
    NodeID: str
    UnitSystem: int
    Properties: list[ClassificationProperty]

class ClassificationProperty:
    def __init__(self, ) -> None: ...
    Id: str
    Datatype: str
    StringValues: list[StringValue]
    IntegerValues: list[IntegerValue]
    DoubleValues: list[DoubleValue]
    DateValues: list[DateValue]
    BooleanValues: list[BooleanValue]
    ValueRangeValues: list[ValueRangeValue]
    ValueWithToleranceValues: list[ValueWithToleranceValue]
    LevelValues: list[LevelValue]
    PositionValues: list[PositionValue]
    AxisValues: list[AxisValue]
    BlockValues: list[BlockPropertyValue]

class Context:
    def __init__(self, ) -> None: ...
    Type: str
    Id: str
    Hierarchy: str

class DateValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    DateVal: System.DateTime

class DoubleValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    DoubleVal: float
    Unit: str

class GetClassDescriptorResponse:
    def __init__(self, ) -> None: ...
    BaseClasses: list[ClassDefinition]
    Blocks: list[ClassDefinition]
    KeyLOVDefinitions: list[KeyLOVDefinition]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetClassificationObjectsResponse:
    def __init__(self, ) -> None: ...
    ObjectDefinitions: list[ClassificationObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class IntegerValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    IntVal: int
    Unit: str

class LOVItems:
    def __init__(self, ) -> None: ...
    DataType: str
    IntegerItems: list[LOVIntegerItems]
    DoubleItems: list[LOVDoubleItems]
    StringItems: list[LOVStringItems]
    BoolItems: list[LOVBooleanItems]
    DateItems: list[LOVDateItems]
    ReferenceItems: list[LOVReferenceItems]

class KeyLOVDefinition:
    def __init__(self, ) -> None: ...
    ObjectType: str
    Irdi: str
    KeyLOVNamespace: str
    Id: str
    Revision: str
    Status: str
    KeyLOVItems: LOVItems
    Name: L10NProperty

class L10NTranslation:
    def __init__(self, ) -> None: ...
    StrVal: str
    TranslationStatus: str
    Locale: str
    IsMasterLocale: bool

class LevelValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    Min: float
    Max: float
    Nominal: float
    Typical: float
    Unit: str

class LOVBooleanItems:
    def __init__(self, ) -> None: ...
    BoolValue: bool
    DisplayValue: L10NProperty

class LOVDateItems:
    def __init__(self, ) -> None: ...
    DateValue: str
    ValueMeaning: str
    IsSubMenu: bool
    SubMenuTitle: L10NProperty
    DependencyKey: str
    SubMenuItems: list[LOVDateItems]

class LOVDoubleItems:
    def __init__(self, ) -> None: ...
    ValueMeaning: str
    DoubleValue: float
    IsSuMenu: bool
    SubMenuTitle: L10NProperty
    DependencyKey: str
    SubMenuItems: list[LOVDoubleItems]

class LOVIntegerItems:
    def __init__(self, ) -> None: ...
    IntegerValue: int
    ValueMeaning: str
    IsSubMenu: bool
    SubMenuTitle: L10NProperty
    DependencyKey: str
    SubMenuItems: list[LOVIntegerItems]

class LOVReferenceItems:
    def __init__(self, ) -> None: ...
    StringValue: str
    DisplayValue: L10NProperty
    ValueMeaning: str
    BlockReference: str

class LOVStringItems:
    def __init__(self, ) -> None: ...
    StringValue: str
    DisplayValue: L10NProperty
    IsSubMenu: bool
    SubMenuTitle: L10NProperty
    DependencyKey: str
    SubMenuItems: list[LOVStringItems]

class PositionValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    PosX: float
    PosY: float
    PosZ: float
    Unit: str

class SaveClassificationObjectsResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ObjectDefinitions: list[ClassificationObject]

class StringValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    StrVal: L10NTranslation
    Translations: list[L10NTranslation]

class UserDataEntry:
    def __init__(self, ) -> None: ...
    Name: str
    Sequence: int
    Val: str

class ValueRangeValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    Min: float
    Max: float
    Unit: str

class ValueWithToleranceValue:
    def __init__(self, ) -> None: ...
    HasValue: bool
    Min: float
    Max: float
    Nominal: float
    Unit: str

class Classification:
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteClassificationObjects(self, Context: Context, ObjectIDs: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetClassDescriptor(self, NodeIDs: list[str], Options: int) -> GetClassDescriptorResponse: ...
    def GetClassificationObjects(self, Context: Context, ObjectIDs: list[str]) -> GetClassificationObjectsResponse: ...
    def SaveClassificationObjects(self, Context: Context, ClassificationObjects: list[ClassificationObject]) -> SaveClassificationObjectsResponse: ...

