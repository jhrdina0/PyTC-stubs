import System
import Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification
import Teamcenter.Soa.Client.Model
import typing

class AssignmentTypeDetail:
    """
    
a structure to pair the AssignmentTypeDetail Element with an index into the
input
vector of equivalent sets of objects.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """Index of equivalent set in the input vector for which these details were calculated."""
    EquivalentLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of all equivalent lines in the input equivalent set (all equivalent sources
            in sequence and then all targets in sequence).
            """
    AssignmentDetails: list[ExtensionAssignmentTypeDetails]
    """Assignment type details of this equivalent set."""

class ComparisonSummaries:
    """
    the  ExtensionComparisonSummary for each extension per input vector element
    """
    def __init__(self, ) -> None: ...
    Index: int
    """Index of equivalent set in the input vector for which these results were calculated."""
    Summaries: list[ExtensionComparisonSummary]
    """The list of elements that capture the result of an extension comparison."""

class ExtensionAssignmentTypeDetails:
    """
    Structure that keeps assignment types details for each extension name.
    """
    def __init__(self, ) -> None: ...
    ExtensionName: str
    """Extension name that was compared."""
    AssignmentTypesDetails: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.AssignmentTypeDetailElement]
    """A list of details for each assignment type."""

class ExtensionComparisonSummary:
    """
    an element to capture the result of an extension comparison
    """
    def __init__(self, ) -> None: ...
    ExtensionName: str
    """Extension name that was compared."""
    IsDifferent: bool
    """
            True if there is a difference in comparison of this equivalent set for this extension,
            false otherwise.
            """

class GetAssignmentComparisonDetailsResponse:
    """
    
response of method getAssignmentComparisonDetails - a vector of
AssignmentTypeDetail
element and serviceData
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Object that captures any partial errors."""
    Details: list[AssignmentTypeDetail]
    """The list of AssignmentType detail elements - one for each input equivalent set."""

class GetComparisonSummariesResponse:
    """
    
response of method getComparisonSummaries - a vector of ComparisonSummaries
element
and serviceData
    """
    def __init__(self, ) -> None: ...
    ComparisonSummaries: list[ComparisonSummaries]
    """The list of extension summaries elements - one for each input equivalent set."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Object that captures any partial errors."""

class StringToPartialMatchCriteria:
    """
    Holds PartialMatchCriteria object for each extension name.
    """
    def __init__(self, ) -> None: ...
    ExtensionName: str
    ExtensionCriteria: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.PartialMatchCriteria
    """The comparison criteria of this extension."""

class StructureVerification:
    """
    Interface StructureVerification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAssignmentComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartialMatchCriteria: list[StringToPartialMatchCriteria]) -> GetAssignmentComparisonDetailsResponse:
        """    
             This operation returns the details of any differences between assignments for the
             supplied source and target BOMLine objects. Assignments can be parts or tools, manual
             or resolved by logical assignments. The operation takes the source and target BOMLine
             objects and compares their assignments according to their types - manual assignments
             are compared with manual, resolved with resolved, parts with parts and tools with
             tools. The source and target assignments are returned by this operation in the form
             of a table that is created by the output structures.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         The list of source and target BOMLine objects that were deemed equivalent by some
                         method, for which any differences in assignments is required.
             
        :param PartialMatchCriteria: 
                         The list of partial match criteria for comparison. For each extension name it holds
                         a PartialMatchCriteria object with comparison criteria of this extension.
             
        :return: The differences between the source and target asssignments in the form of a table,
             where the columns represent the input equivalent BOMLines, and the rows are the assignments
             themselves. All the equivalent assignments are returned together on the same row.
             Assignments that are missing from the source or target are represented by "nulls".
             The following partial errors may be returned:  - 253001 This error can only be returned
             if there is some kind of environment issue or a bug in the code, it will never happen
             during normal execution.
        """
        ...
    def GetComparisonSummaries(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartialMatchCriteria: list[StringToPartialMatchCriteria]) -> GetComparisonSummariesResponse:
        """    
             This operation retrieves comparison summaries for supplied extensions on the provided
             equivalent sets of objects. The source objects in each set can be BOMLines, Cpd0DesignElements
             or Cpd0DesignFeatures. The target objects in each set can be only BOMLines. For each
             received extension on each received equivalent set it performs comparison of objects
             in the equivalent set for this extension according to received criteria. For each
             such comparison only the result is returned - a flag indicating whether the input
             objects were determined different or not. This operation returns comparison results
             for any number of extensions simultaneously.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         The list of source and target objects that were deemed equivalent by some method,
                         for which extensions comparison results are required. The source objects can be BOMLines,
                         Cpd0DesignElements or Cpd0DesignFeatures. The target objects can be only BOMLines.
             
        :param PartialMatchCriteria: 
                         The list of partial match criteria for comparison. For each extension name it holds
                         a PartialMatchCriteria object with comparison criteria of this extension.
             
        :return: The operation returns the extensions comparison results for each supplied equivalent
             set. For each extension on each equivalent set it returns a boolean flag which is
             "true" if there is any difference in comparison of this equivalent set for this extension,
             and "false" otherwise. The following partial errors may be returned:  - 253049 The
             input equivalent set of lines doesn't contain any source lines or any target lines.
             - 253001 This error can only be returned if there is some kind of environment issue
             or a bug in the code, it will never happen during normal execution.
        """
        ...

