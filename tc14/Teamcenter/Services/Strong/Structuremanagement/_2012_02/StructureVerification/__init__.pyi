import System
import System.Collections
import Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ACInput:
    """
    provides a set of input values for the accountabilityCheck operation.
    """
    def __init__(self, ) -> None: ...
    SourceObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The source bom lines."""
    TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The target bom lines."""
    Options: int
    """mask of integer values representing different UI options."""
    SourceContextLine: Teamcenter.Soa.Client.Model.ModelObject
    """Optional source context line."""
    TargetContextLine: Teamcenter.Soa.Client.Model.ModelObject
    """optional target context line."""
    MatchType: int
    """Represents user choice of color display."""
    SourceFilteringRule: str
    """The source filtering rule."""
    TargetFilteringRule: str
    """The target filtering rule."""
    SourceDepth: int
    """the depth of source structure. -1 represents all depths."""
    TargetDepth: int
    """The depth of target structure from each target root. -1 to set it to any depth."""
    ResultName: str
    """Name of occurrenceGroup to be created - when report is generated."""
    ResultDesc: str
    """optional description of the OccurrenceGroup to be created."""
    ReportCriteria: Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.ReportCriteria
    """criteria for printable report."""
    ReportMode: int
    """
            Indicates which mode the accountability check report has to be generated. Occurrence
            group mode of excel report mode or coloring mode or a combination of those or batch
            report or batch propagate. This is a bit masked flag. 1 - coloring mode, 2 - generate
            report, 3 - color and generate report, 4 - occurrence group report, 8 - batch report,
            16 - batch propagate.
            """
    PartialMatchCriteria: System.Collections.Hashtable
    """
            the set of options to be used for comparison on equivalent lines. It is a map - with
            the key being the name of plugin or string to be used as a discriminator between
            various components.
            """
    IncludeScopeLines: bool
    """Flag to indicate whether  to include scope lines as part of result set."""

class AssignmentDetail:
    """
    
For each line in input equivalent set  holds the tag of the current assigned
objects
for that line.
    """
    def __init__(self, ) -> None: ...
    Assignments: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            size is same as the size of the input equivalent line. It is the list of assignments
            (one per line) - across the row.
            """
    MatchType: int
    """flag to indicate match of the current assignment."""

class AssignmentTypeDetail:
    """
    
a structure to pair the AssignmentTypeDetail Element with an index into the
input
vector of equivalent sets of objects.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """index into the input vector."""
    Details: list[AssignmentTypeDetailElement]
    """
            the size of the vector is same as maximum number of  assignmentTypes among the set
            equivalent lines. eg: if src1, target1 are equivalent and src1 has 3 manual assignments
            and target1 has 2 - this vector will have 3 elements. The first AssignmentTypeDetailElement
            will have src1_assign1, target1_assign1; the second AssignmentTypeDetailElement will
            have src1_assign2,target1_assign2; the third AssignmentTypeDetailElement will have
            src1_assign3, NULL
            """
    EquivalentLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            the set of all equivalent lines in input (all equivalent srcs in sequence and then
            all targets in sequence).
            """

class AssignmentTypeDetailElement:
    """
    a structure to capture the details for assignment comparison.
    """
    def __init__(self, ) -> None: ...
    AssignmentType: str
    """a string to indicate the type of assignment (MEConsumed, MEResource etc.)"""
    ManualAssignments: list[AssignmentDetail]
    """
            length of the vector will be the maximum number of assignments among all the equivalent
            lines for the given type. If there are 3 assigments for src1 and 1 for target1 -
            the size of this vector will be 3, with the first AssignmentDetails element having
            {src1assign1,target1assign1}, the second AssignmentDetail element having {src1assign2,NULLTAG},
            the third {src1assign3,NULLTAG}.
            """
    LogicalAssignments: list[LogicalAssignmentDetail]
    """
            length of the vector will be the maximum number of logical assignments among all
            the equivalent lines for the given type.
            """

class AsyncReportCriteria:
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

class AsyncACInput:
    """
    provides a set of input values for the accountabilityCheckAsync operation.
    """
    def __init__(self, ) -> None: ...
    SourceObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            persistent objects that can be converted to bomlines. Currently, the only supported
            object is VisStructureContext object, with the array length being 1.
            """
    TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            persistent objects (target) that can be converted to bomlines. Currently, the only
            supported object is VisStructureContext object, with the array length being 1.
            """
    Options: int
    """mask of integer values representing different UI options."""
    SourceContextLine: Teamcenter.Soa.Client.Model.ModelObject
    """Optional source context line. Currently unused."""
    TargetContextLine: Teamcenter.Soa.Client.Model.ModelObject
    """optional target context line. Currently, not used."""
    MatchType: int
    """Represents user choice of color display."""
    SourceFilteringRule: str
    """The source filtering rule."""
    TargetFilteringRule: str
    """The target filtering rule."""
    SourceDepth: int
    """the depth of source structure. -1 represents all depths."""
    TargetDepth: int
    """The depth of target structure from each target root. -1 to set it to any depth."""
    ResultName: str
    """Name of occurrenceGroup to be created - when report is generated."""
    ResultDesc: str
    """optional description of the OccurrenceGroup to be created."""
    ReportCriteria: AsyncReportCriteria
    """criteria for printable report."""
    ReportMode: int
    """
            Indicates which mode the accountability check report has to be generated.10 - batch
            report, 16 - batch propagate.
            """
    PartialMatchCriteria: System.Collections.Hashtable
    """
            the set of options to be used for comparison on equivalent lines. It is a map - with
            the key being the name of plugin or string to be used as a discriminator between
            various components.
            """
    IncludeScopeLines: bool
    """Flag to indicate whether  to include scope lines as part of result set."""

class AsyncDetails:
    """
    
details that are to be specified if an operation is to be performed
asynchronously.
This is same as the BatchUtils parameters that is (optionally) passed to
accountabilityCheck.
Duplicated as structures are not to be shared in soa framework.
    """
    def __init__(self, ) -> None: ...
    Identifier: str
    """any user defined string for recognizing the request"""
    Mode: str
    """
            processing mode on server. Possible values are "BackGround", "Blocking" and "InProcess"
            (case sensitive). Currently, the only supported value is BackGround. In this mode
            the Dispatcher services must be installed, or the server will default to InProcess
            (meaning same tcserver as the one the client connects to will be used for accountability).
            """
    Site: int
    """
            processing site. 0 - local. This information is used in the blocking mode to get
            the http url.
            """
    Priority: int
    """possible values - 0-3, 0 being the lowest."""
    StartTime: System.DateTime
    """start date/time of scheduled dispatcher request"""
    EndTime: System.DateTime
    """end date/time of scheduled dispatcher request"""
    DaysOfWeek: list[bool]
    """
            on which day of the week translator (async process) has to be run. Should have 7
            entries and a true indicates should be run on that day. Starting on Sunday (1st entry).
            """
    EndAfterOccurrences: int
    """number of times the async process has to run."""
    PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """objects used directly or indirectly for the asynchronous processing."""
    SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            any auxiliary objects to be used as additional info during processing of asynchronous
            request. Example - a folder to add some datasets to.
            """

class AsyncPartialMatchCriteria:
    """
    a structure to capture generic Partial Match criteria
    """
    def __init__(self, ) -> None: ...
    IntMap: System.Collections.Hashtable
    """map of string to vector or integers."""
    DblMap: System.Collections.Hashtable
    """map of string to vector of doubles."""
    StrMap: System.Collections.Hashtable
    """map of string to vector of strings."""
    ObjMap: System.Collections.Hashtable
    """map of string to vector of objects."""

class BatchDetails:
    """
    details that are to be specified if an operation is to be performed
asynchronously.
    """
    def __init__(self, ) -> None: ...
    Identifier: str
    """any user defined string for recognizing the request"""
    Mode: str
    """
            processing mode on server. Possible values are "BackGround", "Blocking" and "InProcess"
            (case sensitive). Currently, the only supported value is BackGround. In this mode
            the Dispatcher services must be installed, or the server will default to InProcess
            (meaning same tcserver as the one the client connects to will be used for accountability).
            """
    Site: int
    """
            processing site. 0 - local. This information is used in the blocking mode to get
            the http url.
            """
    Priority: int
    """possible values - 0-3, 0 being the lowest."""
    StartTime: System.DateTime
    """start date/time of scheduled dispatcher request"""
    EndTime: System.DateTime
    """end date/time of scheduled dispatcher request"""
    DaysOfWeek: list[bool]
    """
            on which day of the week translator (async process) has to be run. Should have 7
            entries and a true indicates should be run on that day. Starting on Sunday (1st entry).
            """
    EndAfterOccurrences: int
    """number of times the async process has to run."""
    PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """objects used directly or indirectly for the asynchronous processing."""
    SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            any auxiliary objects to be used as additional info during processing of asynchronous
            request. Example - a folder to add some datasets to.
            """

class BOMLineNetEffectivityDetail:
    """
    structure to encapsulate a BOMLine and the associated endItem effectivity
details.
    """
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.ModelObject
    """The bomline for which the effectivity details will added."""
    EffDetails: list[Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.EndItemDetail]
    """The array of effectivity details for the bomline"""

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
    """Details of missing target effectivities"""
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
            lines
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData to return any partial errors"""

class DescendentDetail:
    """
    the list of DescendentDetailElements for each set of input equivalent objects.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """position in the input vector."""
    Details: list[DescendentDetailElement]
    """
            The size of the vector matches the maximum number of descendents for each line in
            input equivalent set at index above (given now by equivalentLines - src lines being
            followed by targetlines). Eg: equivalentset(src1,target1) - src1 has 3 children,
            target1 has 1 child. details element vector size will be 3. The first DescendentDetailElement
            will contain 2 children: SrcChild1,targetChild1. The second DescendentDetailElement
            will have SrcChild2,NULLTAG, and 3rd DescendentDetailElement will have SrcChild3,NULLTAG.
            """
    EquivalentLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            the set of all equivalent lines in input (all equivalent srcs in sequence and then
            all targets in sequence).
            """

class DescendentDetailElement:
    """
    the list of DescendentDetailElements for each set of input equivalent objects.
    """
    def __init__(self, ) -> None: ...
    Children: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The size of the vector will match the size of the equivalent lines at input index
            i. This array represents one predecessor per input line (row in a table, and not
            a column). . Eg: SrcChild1, NULLTAG, TargetChild1, NULLTAG (assuming 4 eqv. lines)
            """
    MatchType: int
    """0 means fullmatch, 1 means match, 2 means multiple match"""

class EndItemAndUnitDetails:
    """
    
endItem (item used to specify the unit effectivity) tag and the associated
UnitAndLineDetails
structure.
    """
    def __init__(self, ) -> None: ...
    EndItem: Teamcenter.Soa.Client.Model.ModelObject
    """Teamcenter::BusinessObject The endItem object to be associated with the Unit details"""
    Details: list[UnitAndLineDetails]
    """structure capturing the details of line(s) and effectivities."""

class EquivalentLines:
    """
    
Lines from a Source Window and a Target Window that are equivalent. For example
-
having the same ID in Context or other criteria.
    """
    def __init__(self, ) -> None: ...
    EqvSrcLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            set of source BOMLine objects that are equivalent based on some criteria like
            ID in context.
            """
    EqvTargetLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            set of target BOMLine objects (not the same window as source lines) that are
            equivalent in a manner consistent with the source lines.
            """

class EquivalentSetElement:
    """
    
a structure to capture the equivalent src and target lines along with the
partial
match criteria.
    """
    def __init__(self, ) -> None: ...
    EqvSrcLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """the src lines which are equivalent (currently only id in context)"""
    EqvTargetLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            equivalent target lines - based on In context id (absoccid) or apn or ebop criteria
            (origin link, logical designator, uid )
            """
    Criteria: System.Collections.Hashtable
    """input map for specifying criteria, the key being server extension id."""

class GetAssignmentComparisonDetailsResponse:
    """
    
response of method getAssignmentComparisonDetails - a vector of
AssignmentTypeDetail
element and serviceData
    """
    def __init__(self, ) -> None: ...
    Details: list[AssignmentTypeDetail]
    """a list of AssignmentType detail elements - for all the input equivalent sets."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData element to capture any partial errors."""

class GetDescendentComparisonDetailsResponse:
    """
    
structure to capture the response of getDescendentComparisonDetails method. Has
the
list of details for each input set and serviceData to capture partial errors.
    """
    def __init__(self, ) -> None: ...
    Details: list[DescendentDetail]
    """detail list."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData member to capture any partial errors."""

class GetPartitionComparisonDetailsResponse:
    """
    
structure to capture the vector of PartitionDetail elements and serviceData for
partial
errors.
    """
    def __init__(self, ) -> None: ...
    Details: list[PartitionDetail]
    """vector of partitionDetail elements."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData member to capture partial errors."""

class GetPredecessorComparisonDetailsResponse:
    """
    return the list of predecessor detail elements and service data for partial
errors.
    """
    def __init__(self, ) -> None: ...
    Details: list[PredecessorDetail]
    """details about the predecessor detail for each element."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData to capture any partial errors."""

class GetPropertyComparisonDetailsResponse:
    """
    response of getPropertyComparisonDetails method.
    """
    def __init__(self, ) -> None: ...
    Details: list[PropertyDetail]
    """the list of elements that have the details for each property in the input."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData element to capture any partial errors."""

class LogicalAssignmentDetail:
    """
    
For each line in input equivalent set  holds the tag of the current assigned
objects
for that line.
    """
    def __init__(self, ) -> None: ...
    Criteria: list[str]
    """
            for each line in input equivalent set holds the criteria of the current line's LA
            - across the row.
            """
    ResolvedAssignments: list[AssignmentDetail]
    """
            length of the vector will be the maximum number of resolved assignments among all
            the equivalent lines for the given type.
            """
    MatchType: int
    """flag to indicate match of the current assignment."""
    LogicalAssignments: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            For each line in input equivalent set holds the logical assignment or tool requirement
            object.
            """

class PartialMatchCriteria:
    """
    a structure to capture generic Partial Match criteria
    """
    def __init__(self, ) -> None: ...
    IntMap: System.Collections.Hashtable
    """map of string to vector or integers."""
    DblMap: System.Collections.Hashtable
    """map of string to vector of doubles."""
    StrMap: System.Collections.Hashtable
    """map of string to vector of strings."""
    ObjMap: System.Collections.Hashtable
    """map of string to vector of objects."""
    DateMap: System.Collections.Hashtable
    """map of string to vector of dates"""

class PartitionDetail:
    """
    
structure to capture the position(index) in the input equivalence set and the
partition
elements vector.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """position in the input vector."""
    Partitions: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The size of the vector matches the equivalent lines. This list the partition per
            input equivalent line as a row.
            """
    IsDifferent: bool
    """flag to indicate whether any of the partitions in a single row is different."""
    EquivalentLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            the set of all equivalent lines in input (all equivalent srcs in sequence and then
            all targets in sequence).
            """

class PredecessorDetail:
    """
    the list of PredecessorDetailElements for each set of input equivalent objects.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """position in the input vector."""
    Details: list[PredecessorDetailElement]
    """
            The size of the vector matches the maximum number of predecessors for each line in
            input equivalent set at index above (given now by equivalentLines - src lines being
            followed by targetlines). The PredecessorDetailElement will be the size of the input
            lines. Eg: equivalentset(src1,target1) - src1 has 3 predecessors, target1 has 1 predecessor.
            details element vector size will be 3. The first PredecessorDetailElement will contain
            2 predecessors: SrcPred1,targetPred1. The second PredecessorDetailElement will have
            SrcPred2,NULLTAG, and 3rd PredecessorDetailElement will have SrcPred3,NULLTAG.
            """
    EquivalentLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            the set of all equivalent lines in input (all equivalent srcs in sequence and then
            all targets in sequence).
            """

class PredecessorDetailElement:
    """
    the list of PredecessorDetailElements for each set of input equivalent objects.
    """
    def __init__(self, ) -> None: ...
    Predecessors: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The size of the vector will match the size of the equivalent lines at input index
            i. This array represents one predecessor per input line (row in a table, and not
            a column). . Eg: SrcPred1, NULLTAG, TargetPred1, NULLTAG (assuming 4 eqv. lines)
            """
    MatchType: int
    """0 means fullmatch, 1 means match, 2 means multiple match"""

class PropagationInput:
    """
    the input structure for propagateProperties.
    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """the target object to which the changes will be propagated."""
    Sources: list[Teamcenter.Soa.Client.Model.ModelObject]
    """the source object(s) from which the changes will be propagated to target."""
    Criteria: System.Collections.Hashtable
    """
            the partialMatchCriteria structure to be used for change propagation. This is a map
            of a string (a client id) to that client's properties/criteria.
            """

class PropagationResponse:
    """
    The response of Propagation Service.
    """
    def __init__(self, ) -> None: ...
    Results: list[PropagationResult]
    """a vector of propagationResults."""
    LogFileTicket: str
    """a fms ticket for the transient file that captures the log of propagation service."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data object"""

class PropagationResult:
    """
    
a structure to capture a single result for an object that is being propagated
from
one context to another.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """a integer representing the position in input vector."""
    PropagationResults: System.Collections.Hashtable
    """
            a map of string to vector of propagationResultElements. The key of the map would
            indicate the client id corresponding to what is passed in PropagationInput.
            """

class PropagationResultElement:
    """
    
a structure to capture a single result for an object that is being propagated
from
one context to another.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """an object which is participating in the propagation."""
    PropagatedProperties: list[str]
    """successfully propagatedProperties."""
    LogFileTicket: str
    """
            an optional log file ticket. If the extension/server generates a specific logfile
            - this will be the fms ticket for that file (transient).
            """

class PropertyDetail:
    """
    the  propertyDetailElement for each of the properties per input vector element.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """index of the input vector of equivalent set of obejcts."""
    Details: list[PropertyDetailsElement]
    """the list of PropertyDetailsElement"""

class PropertyDetailsElement:
    """
    a element to capture the details of a property for an object(s).
    """
    def __init__(self, ) -> None: ...
    PropertyName: str
    """the name of the property."""
    IsDifferent: bool
    """flag to indicate if any of the objects have a value(s) that is different."""

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
            lines. Current implementation does not support thi
            """
    SrcLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """list of of srclines that satisfy the units/dates in this structure."""
    TargetLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            list of of target lines ( lines from another window  that are equivalent in some
            way to the src lines - eg: ID in context) that satisfy the units/dates in this structure.
            """

class StructureVerification:
    """
    Interface StructureVerification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAssignmentComparisonDetails(self, EquivalentObjects: list[EquivalentLines], PartRelationTypes: list[str], ToolRelationTypes: list[str], CompareLA: int, CompareManual: bool) -> GetAssignmentComparisonDetailsResponse:
        """    
             get the details of any differences between assignments for the supplied src and target
             objects.
             
        :param EquivalentObjects: 
                         The source and target objects that were deemed equivalent by some method, for which
                         any differences in assignments is required.
             
        :param PartRelationTypes: 
                         past assignments to be considered for equivalence.
             
        :param ToolRelationTypes: 
                         tool assignments to be considered for equivalence - eg:weld
             
        :param CompareLA: 
                         LogicalAssignment consideration for comparison: 0  means NO_COMPARE, 1means DEFINITION_ONLY,
                         2 means DEFINITION_AND_RESOLVED
             
        :param CompareManual: 
                         flag to indicate whether to compare manual assignments or not.
             
        :return: a vector of AssignmentTypeDetail elements and serviceData
        """
        ...
    def AccountabilityCheck(self, Input: ACInput, BatchDetails: BatchDetails) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.AccountabilityCheckResponse:
        """    
             The operation will call the existing accountability check functions, which will generate
             a check result for report in the colored display.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         Input values to the operation
             
        :param BatchDetails: 
                         In case the operation has to be performed asynchronously, this parameter can be used
                         to pass that information. Pass NULL for second parameter if unused.
             
        :return: Results from the accountability check
        """
        ...
    def CompareNetEffectivity(self, Lines: list[EquivalentLines], IgnoreOverlapErrors: bool, UseStructureConfiguration: bool, ReturnOnFirstMismatch: bool) -> CompareNetEffectivityResponse:
        """    
             effectivity of 2 sets of lines that are deemed equivalent in some form.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
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
             effectivities for the set of input equivalent lines.
        """
        ...
    def GetDescendentComparisonDetails(self, Input: list[EquivalentLines], IgnoreStructureSpecific: bool) -> GetDescendentComparisonDetailsResponse:
        """    
             for each input equivalent set capture the response of getDescendentComparisonDetails
             method. Has the list of details for each input set and serviceData to capture partial
             errors.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         list of equivalent sets of lines.
             
        :param IgnoreStructureSpecific: 
                         flag to indicate if non-allocated lines are to be ignored.
             
        :return: structure to capture the response of getDescendentComparisonDetails method. Has the
             list of details for each input set and serviceData to capture partial errors.
        """
        ...
    def GetPartitionComparisonDetails(self, Input: list[EquivalentLines]) -> GetPartitionComparisonDetailsResponse:
        """    
             service to get details on a mismatch of parititions.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         equivalent sets of src/targets objects.
             
        :return: details of a mismatch of partitions.
        """
        ...
    def GetPredecessorComparisonDetails(self, Input: list[EquivalentLines], IgnoreStructureSpecific: bool) -> GetPredecessorComparisonDetailsResponse:
        """    
             for a given equivalent set of lines/object, compute and return the list of predecessor
             detail elements and flag if different.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         list of input equivalent objects.
             
        :param IgnoreStructureSpecific: 
                         flag to indicate if non-allocated lines are to be ignored.
             
        :return: return the list of predecessor detail elements and service data for partial errors.
        """
        ...
    def GetPropertyComparisonDetails(self, EquivalentObjects: list[EquivalentSetElement]) -> GetPropertyComparisonDetailsResponse:
        """    
             method to retrieve details for supplied properties on the provided equivalent sets
             of lines.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         the list of equivalent objects and the property names supplied in the string map
                         of strings.
             
        :return: return the property values for each supplied equivalent set and any partial errors.
        """
        ...
    def PropagateProperties(self, Input: list[PropagationInput]) -> PropagationResponse:
        """    
             method to propagate properties.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The list of PropagationInput structures - one for each target which needs the changes
                         propagated to.
             
        :return: a map of string to vector of PropagationResultElement structure. The string key will
             match to the input PartialMatchCriteria.
        """
        ...

