import Teamcenter.Soa.Client.Model
import typing

class FeatureAttributesData:
    def __init__(self, ) -> None: ...
    AttributeCode: str
    Significance: str
    MeasurementApproach: str
    Need: str
    Nominal: str
    Formula: str
    Mmc: str
    SpecLimitsData: list[SpecLimit]

class FeatureBasicData:
    def __init__(self, ) -> None: ...
    FeatureID: str
    FeatureType: str
    FeatureLabel: str
    ParentID: str
    FeatureDescription: str
    AlternateLabel: str
    Active: str
    Need: str
    LoadingSplitID: str

class FeatureNominals:
    def __init__(self, ) -> None: ...
    X: str
    Y: str
    Z: str
    I: str
    J: str
    K: str
    I2: str
    J2: str
    K2: str
    X2: str
    Y2: str
    Z2: str

class Features:
    def __init__(self, ) -> None: ...
    BasicFeatureData: FeatureBasicData
    BasicNominalData: FeatureNominals
    FtrAttributeData: list[FeatureAttributesData]

class SpecLimit:
    def __init__(self, ) -> None: ...
    CodeName: str
    Upper: str
    Lower: str
    Target: str

class EngineeringDataLoad:
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateEngineeringExcel(self, RoutineID: str, RoutineRev: str, FeatureRows: list[Features]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

