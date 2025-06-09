import Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification
import Cla0.Services.Internal.Strong.Classificationcommon._2021_06.Classification
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AttributeFormat2:
    def __init__(self, ) -> None: ...
    IsUnsigned: bool
    Precision: int
    Scale: int
    Unit: str
    KeyLOV: str
    NumberOfDigits: int
    NxUnitID: str

class AttributeDataType2:
    def __init__(self, ) -> None: ...
    Type: str
    IsLocalizable: bool
    IsOptimized: bool
    IsProtected: bool
    IsRequired: bool
    IsPolymorphicController: bool
    BlockReference: str
    CardinalityController: str
    NonMetricFormat: AttributeFormat2
    MetricFormat: AttributeFormat2

class ClassAttribute2:
    def __init__(self, ) -> None: ...
    AttributeIndex: int
    DbIndex: int
    Type: str
    Reference: str
    Cardinality: int
    Annotation: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Name: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    DataType: AttributeDataType2
    UserData: list[Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.UserDataEntry]
    AdditionalProperties: list[Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.AdditionalProperties]

class ClassDescriptor2:
    def __init__(self, ) -> None: ...
    Irdi: str
    ClassNamespace: str
    Id: str
    Revision: str
    Status: str
    ClassType: str
    IsAbstract: bool
    HasChildren: bool
    UnitSystem: int
    Name: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    ShortName: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Definition: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Note: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    Remark: Cla0.Services.Internal.Strong.Classificationcommon._2020_12.Classification.L10NProperty
    ClassAttributes: list[ClassAttribute2]
    AdditionalProperties: System.Collections.Hashtable

class ClassificationDataFilesResponse:
    def __init__(self, ) -> None: ...
    ClassificationDataFiles: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SearchClassDescriptorResponse2:
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
    def ListClassificationDataFiles(self, FileTicket: str) -> ClassificationDataFilesResponse: ...
    def SearchClassDescriptor2(self, SearchCriteria: list[Cla0.Services.Internal.Strong.Classificationcommon._2021_06.Classification.SearchCriteria], Options: int) -> SearchClassDescriptorResponse2: ...

