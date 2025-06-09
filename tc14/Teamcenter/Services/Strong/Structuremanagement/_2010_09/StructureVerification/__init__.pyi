import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AccountabilityCheckResponse:
    """
    Contains all the results from the accountabilityCheck operation
    """
    def __init__(self, ) -> None: ...
    AccountabilityCheckResults: list[AccountabilityCheckResult]
    """A vector of accountability check results"""
    ReachableTargets: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vector of reachable target lines"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""

class AccountabilityCheckResult:
    """
    Encapsulates one accountability check result
    """
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.ModelObject
    """The source bom line"""
    EquivalentSourceLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vector of equivalent source lines"""
    EquivalentTargetLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vector of equivalent target lines"""
    CheckResult: int
    """Accountability check result represented by a color value"""
    ResultViewTag: Teamcenter.Soa.Client.Model.ModelObject
    """If OccurrenceGroup report option is chosen, this will be the created OccurrenceGroup."""
    ReportFileInfo: list[TransientFileInfo]
    """details of report files generated in the transient volume."""

class ReportCriteria:
    """
    criteria for generating print report
    """
    def __init__(self, ) -> None: ...
    RdTag: Teamcenter.Soa.Client.Model.Strong.ReportDefinition
    """report definition Tag (required)"""
    ReportName: str
    """name of the report."""
    StylesheetTag: Teamcenter.Soa.Client.Model.ModelObject
    """stylesheet Tag (optional)"""
    StylesheetName: str
    """Name of the stylesheet."""
    DatasetName: str
    """name of containing DataSet (optional)"""
    CriteriaName: list[str]
    """
            a vector of strings containing the Names in a series of Name/Value pairs used to
            specify additional criteria (optional)
            """
    CriteriaValues: list[str]
    """
            a vector of strings containing the Values in a series of Name/Value pairs used to
            specify additional criteria (optional)
            """
    DatasetCtxUID: str
    """The uid for the context dataset"""
    DatasetCtxObj: Teamcenter.Soa.Client.Model.ModelObject
    """Dataset context tag"""
    RelationName: str
    """relation name to be used."""
    DatasetType: str
    """Dataset type to be used."""
    ReportOptionsNames: list[str]
    """
            StructElement name="reportOptionsNames" description="a vector of strings containing
            the Names in a series of Name/Value pairs used to specify additional criteria (optional)
            """
    ReportOptionsValues: list[str]
    """
            a vector of strings containing the Values in a series of Name/Value pairs used to
            specify additional criteria (optional)
            """
    ContextObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """a vector of Tags representing context object(s) (required for item reports)"""
    ContextObjectUIDs: list[str]
    """a vector of uids representing context objects"""

class ACInput:
    """
    Provides a set of input values for the accountabilityCheck operation
    """
    def __init__(self, ) -> None: ...
    SourceObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The source bom lines"""
    TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The target bom lines"""
    Options: int
    """Sum of integer values representing different UI options"""
    SourceContextLine: Teamcenter.Soa.Client.Model.ModelObject
    """The possible source context line"""
    TargetContextLine: Teamcenter.Soa.Client.Model.ModelObject
    """The possible target context line"""
    MatchType: int
    """Represents user choice in color display"""
    SourceFilteringRule: str
    """The source filtering rule"""
    TargetFilteringRule: str
    """The target filtering rule"""
    SourceDepth: int
    """The source structure search depth; -1 represents all depths"""
    TargetDepth: int
    """The target structure search depth; -1 represents all depths"""
    ResultName: str
    """Name of the OccurrenceGroup to be created."""
    ResultDesc: str
    """
            optional description of the OccurrenceGroup to be created - if OccurrenceGroup report
            option is chosen.
            """
    ReportCriteria: ReportCriteria
    """the criteria for printable report."""
    ReportMode: int
    """
            Indicates in what mode the accountability check is running. It can be occurrence
            group mode, excel report mode, coloring mode, or a combination of report and coloring.
            Valid values for        reportMode are: 1 - coloring mode, 2 - excel report mode,
            3 - coloring and excel report mode, 4 - occurrence group mode
            """

class BOMLineNetEffectivityDetail:
    """
    structure to encapsulate a BOMLine and the associated endItem effectivity
details.
    """
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The bomline for which the effectivity details will be added."""
    EffDetails: list[EndItemDetail]
    """The array of effectivity details for the bomline."""

class CompareNetEffectivityGroup:
    """
    structure to capture the response of CompareNetEffectivity method.
    """
    def __init__(self, ) -> None: ...
    SrcLineEffectivities: list[BOMLineNetEffectivityDetail]
    """effectivities of the source lines."""
    TargetLineEffectivities: list[BOMLineNetEffectivityDetail]
    """effectivities of targetLines."""
    MissingSrcDetails: list[EndItemAndUnitDetails]
    """details of missing src by effectivity comparison."""
    MissingTargetDetails: list[EndItemAndUnitDetails]
    """Details of missing target effectivities."""
    OverlappingEffectivities: list[EndItemAndUnitDetails]
    """
            Details of overlapping effectivities. Source lines that have overlapping units or
            target lines that have overlapping units will be listed.
            """
    MatchingEffectivities: list[EndItemAndUnitDetails]
    """Details of matching source and target effectivities"""
    IsMisMatch: bool
    """flag that is set to true if there is a mismatch."""

class CompareNetEffectivityResponse:
    """
    
structure to capture the response of compareNetEffectivityGroup method.  Vector
of
CompareNetEffectivityGroup structures one per input set based equivalent lines
and
a serviceData member to report partial errors.
    """
    def __init__(self, ) -> None: ...
    CompareGroups: list[CompareNetEffectivityGroup]
    """
            vector of the compare results for each corresponding set of input vector of equivalent
            lines.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData to return any partial errors."""

class EndItemAndUnitDetails:
    """
    
endItem (item used to specify the unit effectivity) tag and the associated
UnitAndLineDetails
structure.
    """
    def __init__(self, ) -> None: ...
    EndItem: Teamcenter.Soa.Client.Model.ModelObject
    """The endItem object to be associated with the Unit details."""
    Details: list[UnitAndLineDetails]
    """structure capturing the details of line(s) and effectivities."""

class EndItemDetail:
    """
    
structure to capture the details of enditem - the identifier, effectivity units
associated
with that enditem and dates (future).
    """
    def __init__(self, ) -> None: ...
    EndItem: Teamcenter.Soa.Client.Model.ModelObject
    """the endItem to be associated with the units."""
    Units: list[int]
    """
            unit ranges for the endItem. The units are in pairs - meaning - if you have unit
            effectivtiy like:1-7,10 - this array will be 1,7,10,10.
            """
    Dates: list[System.DateTime]
    """date ranges. Currently not supported. Meaning - will be empty."""

class EquivalentLines:
    """
    
Lines from a Source Window and a Target Window that are equivalent. For example
-
having the same ID in Context or other criteria.
    """
    def __init__(self, ) -> None: ...
    EqvSrcLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """set of source bomlines that are equivalent based on some criteria like ID in context."""
    EqvTargetLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            set of target bomlines (not the same window as source lines) that are equivalent
            in a manner consistent with the source lines.
            """

class TransientFileInfo:
    """
    info about any transient report files that are generated.
    """
    def __init__(self, ) -> None: ...
    FileName: str
    """Name of the file generated in transient volume."""
    IsText: bool
    """Flag to indicate whether the file is a text file or binary file."""
    Ticket: str
    """transient file ticket string."""

class UnitAndLineDetails:
    """
    
Structure to capture the Equivalent BomLines (potentially from 2 windows - a
source
and target window) along with their matched units or dates.
    """
    def __init__(self, ) -> None: ...
    Units: list[int]
    """
            all or a subset of Unit numbers/dates associated with the source and targetlines.
            The units are in pairs - meaning - if you have unit effectivtiy like:1-7,10 - this
            array will be 1,7,10,10.
            """
    Dates: list[System.DateTime]
    """
            If date effectivity is  used - this will have the date ranges for the equivalent
            lines. Current implementation does not support this.
            """
    SrcLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """list of of srclines that satisfy the units/dates in this structure."""
    TargetLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            list of of target lines ( lines from another window  that are equivalent in some
            way to the src lines - eg: ID in context) that satisfy the units/dates in this structure.
            """

class StructureVerification:
    """
    Interface StructureVerification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AccountabilityCheck(self, Input: ACInput) -> AccountabilityCheckResponse:
        """    
             The operation will call the existing accountability check functions, which will generate
             a check result for report in the colored display.
             
        :param Input: 
                         Input values to the operation
             
        :return: Results from the accountability check
        """
        ...
    def CompareNetEffectivity(self, Lines: list[EquivalentLines], IgnoreOverlapErrors: bool, UseStructureConfiguration: bool, ReturnOnFirstMismatch: bool) -> CompareNetEffectivityResponse:
        """    effectivity of 2 sets of lines that are deemed equivalent in some form.
        :param Lines: 
                         Set of lines from a source and target structure that are deemed equivalent  (either
                         by ID in context or some other criteria). Vector to support set based approach.
             
        :param IgnoreOverlapErrors: 
                         flag to indicate that the compare proceed even if there are overlapping effectivities
                         in source or in target lines.
             
        :param UseStructureConfiguration: 
                         flag to indicate whether to use the revision rule and effectivity groups in computing
                         net effectivity - for use during comparison.
             
        :param ReturnOnFirstMismatch: 
                         Flag to indicate that compareNetEffectivity method should return on first mismatch
                         and not process further. In this case the response will not have much information
                         - other than the mismatch flag - and partial errors if any.
             
        :return: returns CompareNetEffectivityResponse which has details of matching/missing and overlapping
             effectivities for the set of input equivalent lines (source and target).
        """
        ...

