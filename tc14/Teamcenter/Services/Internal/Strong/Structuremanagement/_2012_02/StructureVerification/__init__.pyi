import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class ActivityDetailsElement:
    def __init__(self, ) -> None: ...
    IsDifferent: bool
    Children: list[ActivityDetailsElement]
    Activities: list[Teamcenter.Soa.Client.Model.ModelObject]

class ActivitiesDetails:
    def __init__(self, ) -> None: ...
    Index: int
    Details: ActivityDetailsElement
    EquivalentLines: list[Teamcenter.Soa.Client.Model.ModelObject]

class EquivalentLines2:
    def __init__(self, ) -> None: ...
    EqvSrcLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    EqvTargetLines: list[Teamcenter.Soa.Client.Model.ModelObject]

class GetActivitiesComparisonDetailsResponse:
    def __init__(self, ) -> None: ...
    Details: list[ActivitiesDetails]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class PartialMatchCriteria2:
    def __init__(self, ) -> None: ...
    IntMap: System.Collections.Hashtable
    DblMap: System.Collections.Hashtable
    StrMap: System.Collections.Hashtable
    ObjMap: System.Collections.Hashtable
    DateMap: System.Collections.Hashtable

class ToolRequirementComparisonData:
    def __init__(self, ) -> None: ...
    FieldName: str
    Values: list[str]
    IsDifferent: bool

class ToolRequirementComparisonResult:
    def __init__(self, ) -> None: ...
    ComparisonData: list[ToolRequirementComparisonData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class StructureVerification:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetActivitiesComparisonDetails(self, EquivalentObjects: list[EquivalentLines2], ComparisonCriteria: PartialMatchCriteria2) -> GetActivitiesComparisonDetailsResponse: ...
    def GetToolRequirementComparisonDetails(self, SourceObjects: list[Teamcenter.Soa.Client.Model.ModelObject], TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> ToolRequirementComparisonResult: ...

