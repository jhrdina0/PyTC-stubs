import System
import Teamcenter.Soa.Client.Model
import typing

class AttrInfoForSpec:
    """
    This indicates information about specification limits for a feature attribute
code.
    """
    def __init__(self, ) -> None: ...
    FtrAttrCode: str
    """
            Feature Attribute Codes are the deviations to measures; eg: X_DEV(X Deviation),Y_DEV(Y
            Deviation), Z_DEV( Z Deviation) , Z_DEV(Z Deviation).
            """
    LowerSpecLimit: float
    """Lower Specification Limit value for corresponding Feature Attribute Code."""
    UpperSpecLimit: float
    """Upper Specification Limit value for corresponding Feature Attribute Code."""
    Target: float
    """Target value for corresponding Feature Attribute Code."""

class FtrAttrbs:
    """
    This indicates information about Features as part of search criteria.
    """
    def __init__(self, ) -> None: ...
    FeatureId: str
    """Id of the feature defined in the engineering excel file of type DPVExcel."""
    FeatureName: str
    """Name of the feature defined in the engineering excel file of type DPVExcel."""
    FeatureAttribCode: list[str]
    """List of feature attribute codes."""

class FtrInfoForSpec:
    """
    This indications information about features and specification limits.
    """
    def __init__(self, ) -> None: ...
    FeatureId: str
    """Id of the feature defined in the Engineering excel file of type DPVExcel."""
    FeatureName: str
    """Name of the feature defined in the Engineering excel file of type DPVExcel."""
    SpecInfo: list[AttrInfoForSpec]
    """List of specification limits and feature attribute code info."""

class GetFtrAttResponse:
    """
    This indicates information about output of features and partial errors if any.
    """
    def __init__(self, ) -> None: ...
    FeatureInfo: list[FtrInfoForSpec]
    """List of Feature Id,Feature Name and corresponding Specification limits information."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This returns partial errors if any."""

class GetSpecLimitInfoResponse:
    """
    
This indicates information about output for given search criterial and lists
partial
errors if any.
    """
    def __init__(self, ) -> None: ...
    SpecLimits: list[MainSpecLimitOutPut]
    """Specification Limits of a particular feature attribute code."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This returns partial errors if any."""

class GetSpecLimitInput:
    """
    This indicates information about input to get the Specification Limits.
    """
    def __init__(self, ) -> None: ...
    PlantId: str
    """Plant ID of type MEPrPlantProcess."""
    RoutineId: str
    """
            Routine ID of type MEInspection or its subtypes(MECMMInspection,MEVisInspection
            and MEHHInspection).
            """
    RoutineRev: str
    """
            Routine Revision of type MEInspectionRevision or its subtypes(MECMMInspectionRevision,MEVisInspectionRevision
            and MEHHInspectionRevision).
            """
    SpecSheetName: str
    """Specification sheet name to get Feature Attributes Codes."""
    FtrAttribCodeInfo: list[FtrAttrbs]
    """List of feature attribute codes given in above spec sheet name."""
    LastNumOfJobs: int
    """This indicates to get last n number of jobs data from whole processed data."""
    FromDate: str
    """Another search criteria based on date range; this is from date."""
    ToDate: str
    """To date to use in date range search criteria."""

class InputToGetAttrCode:
    """
    This indicates information about input to get the Feature Attribute Codes.
    """
    def __init__(self, ) -> None: ...
    PlantId: str
    """Plant ID of type MEPrPlantProcess."""
    RoutineId: str
    """
            Routine ID of type MEInspection or its subtypes(MECMMInspection,MEVisInspection
            and MEHHInspection).
            """
    RoutineRev: str
    """
            Routine revision of type MEInspectionRevision or its subtypes(MECMMInspectionRevision,MEVisInspectionRevision
            and MEHHInspectionRevision).
            """
    SpecSheetName: str
    """Specification sheet name to get Feature Attributes Codes."""
    ConsiderActiveSignificance: bool
    """
            If trueall the Feature Attributes Codes irrespective of Active Status and Significance
            values are reteturned.
            
            If false, only the Feature Attributes Codes where Active Status value is 'Y' and
            Significance value is '1' are returned.
            
"""

class InputToGetSpecSheetNames:
    """
    This indicates information about input to get the spec sheet names.
    """
    def __init__(self, ) -> None: ...
    PlantId: str
    """Plant ID of type MEPrPlantProcess"""
    RoutineId: str
    """
            Routine ID of type MEInspection or its subtypes(MECMMInspection,MEVisInspection
            and MEHHInspection).
            """
    RoutineRev: str
    """
            Routine revision of type MEInspectionRevision or its subtypes(MECMMInspectionRevision,MEVisInspectionRevision
            and MEHHInspectionRevision).
            """

class MainSpecLimitOutPut:
    """
    This indicates information about specification limits for given search criteria.
    """
    def __init__(self, ) -> None: ...
    PlantId: str
    """Plant Id of type MEPrPlantProcess."""
    RoutineId: str
    """
            Routine Id of type MEInspection or its subtypes(MECMMInspection,MEVisInspection
            and MEHHInspection).
            """
    SpecLimitOutPut: list[SpecLimitInfo]
    """List of specification limits info."""

class SpecInfo:
    """
    This indicates information about output after getting the spec sheet names.
    """
    def __init__(self, ) -> None: ...
    SpecSheetName: str
    """Spec sheet name from excel sheet; examples of spec sheet names are ENGG,1MM,2MM"""

class SpecInfoForQuery:
    """
    This indicates information about event's from measurement database.
    """
    def __init__(self, ) -> None: ...
    ActualValue: float
    """Value which we get from measurement database."""
    BuildLabel: str
    """Job name of a particular event."""
    EventDateTime: str
    """Date and time of a particular event which with measurements in shop floor."""

class SpecInfoResponse:
    """
    
This indicates information about output with spec sheet names and partial errors
if any.
    """
    def __init__(self, ) -> None: ...
    SpecInfoRes: list[SpecInfo]
    """A list of spec sheet names."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This returns partial errors if any."""

class SpecLimitInfo:
    """
    
This indicates information about feature and specification limit of a particular
feature.
    """
    def __init__(self, ) -> None: ...
    FeatureId: str
    """Id of the feature defined in the Engineering excel file of type DPVExcel."""
    FeatureName: str
    """Name of the feature defined in the Engineering excel file of type DPVExcel."""
    FeatureAttribCode: str
    """
            Feature attribute codes are the deviations to measures; eg: X_DEV(X Deviation),Y_DEV(Y
            Deviation), Z_DEV( Z Deviation).
            """
    LowerSpecLimit: float
    """Lower specification limit value for corresponding feature attribute code."""
    Target: float
    """Target value for corresponding feature attribute code."""
    UpperSpecLimit: float
    """Upper specification limit value for corresponding feature attribute code."""
    AttributeInfo: list[SpecInfoForQuery]
    """List of events information."""

class EngineeringDataQuery:
    """
    Interface EngineeringDataQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetFeatureAttributesForSpec(self, InputToGetFtrAtt: list[InputToGetAttrCode]) -> GetFtrAttResponse:
        """    
             This operation gets all feature attribute codes (X deviation (X_DEV),Y deviation
             (Y_DEV) Z deviation( Z_DEV)) from a given specification sheet.
             

             The feature attribute codes are further used to query corresponding measurement data
             and engineering data based on search criteria
             


Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param InputToGetFtrAtt: 
                         This data is used as a search criteria to get the corresponding feature attributes
                         from a given specification sheet.
             
        :return: 
        """
        ...
    def GetSpecificationLimits(self, SpecLimitInput: list[GetSpecLimitInput]) -> GetSpecLimitInfoResponse:
        """    
             This operation gets all specification limits for a given feature attributes codes
             based on given search criteria.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param SpecLimitInput: 
                         This data is used as a search criteria to get the corresponding specification limits.
                         It includes date based and last number of processed jobs criteria.
             
        :return: 
        """
        ...
    def GetSpecSheetNames(self, PlantAndRtnInfo: list[InputToGetSpecSheetNames]) -> SpecInfoResponse:
        """    
             This operation is using to get all spec sheet names available in an excel dataset
             of type DPVExcel attached to the given Operation Revision.
             

             The spec sheet names are further used to get all the defined data specific to that
             sheet. These sheets consist of Lower Specification Limit (LSL), Upper Specification
             Limit (USL) and Target values of a particular feature.
             


Use Cases:

Use Case 1: To know Available spec sheets for an excel sheet.

             Excel sheet might have 10's of spec sheets and user wants to know what they are so
             that he/she can choose any spec sheet to get further data from it to analyze it.
             


Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param PlantAndRtnInfo: 
                         This data is used as a search criteria to get all available specification sheet names.
             
        :return: 
        """
        ...

