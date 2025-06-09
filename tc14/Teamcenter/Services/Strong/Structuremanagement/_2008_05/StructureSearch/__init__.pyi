import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeValues:
    """
    
AttributeValues data structure specifies data values to be bound to the various
search
expressions for execution of the search. It encapsulates the values to be
specified
for each of the data types that can occur in any of the attribute search
expressions.
    """
    def __init__(self, ) -> None: ...
    BoolValues: list[bool]
    """
            A list of boolean values that any of the accompanying set of search expressions may
            use.
            """
    IntValues: list[int]
    """
            A list of integer values that any of the accompanying set of search expressions may
            use.
            """
    DoubleValues: list[float]
    """
            A list of double values that any of the accompanying set of search expressions may
            use.
            """
    StringValues: list[str]
    """
            A list of string values that any of the accompanying set of search expressions may
            use.
            """
    DateValues: System.DateTime
    """Date values that any of the accompanying set of search expressions may use."""
    TagValues: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that any of the accompanying set of search expressions may use."""

class AttributeExpression:
    """
    
AttributeExpression encapsulates information to build a query on the attribute
of
an Item or ItemRevision or their sub-classes in the structure search
scope. A set of these attribute expressions is contained inside a
SearchExpressionInfo
object. Search on multiple values specified within one AttributeExpression are
combined
with a logical 'OR' operation.
    """
    def __init__(self, ) -> None: ...
    ClassName: str
    """Name of class, Item or ItemRevision or any of their sub-classes."""
    AttributeName: str
    """The attribute of the above 'className' to be searched on."""
    AttributeType: str
    """
            The type of the attribute to be searched on. The supported AttributeType are:
            BooleanType, IntegerType, DoubleType, StringType, DateType and TagType.
            """
    QueryOperator: str
    """
            Operator to use for search value comparison . The supported QueryOperator
            are: Equal, GreaterThan, GreaterThanOrEqual, LessThan, LessThanOrEqual, NotEqual,
            IsNull, IsNotNull, Like and NotLike.
            """
    Values: AttributeValues
    """Values to be searched."""

class BoxZoneExpression:
    """
    
BoxZoneExpression specifies one set of Box zone criteria. The search results
from
each SearchBox are combined together using an 'OR' operation.
    """
    def __init__(self, ) -> None: ...
    SearchBoxes: list[SearchBox]
    """
            List of SearchBox, specifying box(s) around
            which to search.
            """
    BoxOperator: str
    """
            Operator to use for expression. The supported BoxOperator are: Inside, Outside,
            Intersects, InsideOrIntersects and OutsideOrIntersects.
            """

class FormAttributeExpression:
    """
    
FormAttributeExpression contains information to search on a single Form
Attribute
within a containing SearchExpressionInfo object. The search on the multiple
values
specified within one FormAttributeExpression are combined with a logical 'OR'
operation.
    """
    def __init__(self, ) -> None: ...
    IsItemForm: bool
    """
            If true, Form associted with Item is to be searched; otherwise, Form
            associted with ItemRevision is searched.
            """
    RelationType: Teamcenter.Soa.Client.Model.ModelObject
    """
            Relation type object with which the Form is associated with the source Item
            or ItemRevision.
            """
    FormType: Teamcenter.Soa.Client.Model.ModelObject
    """Form type object to be searched."""
    AttributeName: str
    """The attribute of the above Form type to be searched."""
    AttributeType: str
    """
            The type of the attribute to be searched on. The supported AttributeType are:
            BooleanType, IntegerType, DoubleType, StringType, DateType and TagType.
            """
    QueryOperator: str
    """
            Operator to use for search value comparison .  The supported QueryOperator
            are: Equal, GreaterThan, GreaterThanOrEqual, LessThan, LessThanOrEqual, NotEqual,
            IsNull, IsNotNull, Like and NotLike.
            """
    Values: AttributeValues
    """The values of the attribute to be searched."""

class InClassExpression:
    """
    InClassExpression
    """
    def __init__(self, ) -> None: ...
    InClassClassNames: list[str]
    """A list of class names of the classification class used for search."""
    InClassAttributeIDs: list[int]
    """
            A list of attribute ID(s) of the class selected for classification search on which
            search needs to be performed.
            """
    InClassAttributeValues: list[str]
    """A list of values specified for search comparison."""

class OccurrenceNoteExpression:
    """
    
OccurrenceNoteExpression contains information to search on a single occurrence
note
type within a containing SearchExpressionInfo object. The search on the multiple
values specified within one OccurrenceNoteExpression are combined with a logical
'OR' operation.
    """
    def __init__(self, ) -> None: ...
    NoteType: str
    """Occurrence note type to be search."""
    QueryOperator: str
    """
            Operator to use for search value comparison .  The supported QueryOperator
            are: Equal, GreaterThan, GreaterThanOrEqual, LessThan, LessThanOrEqual, NotEqual,
            IsNull, IsNotNull, Like and NotLike.
            """
    Values: list[str]
    """A list of occurrance note values to be searched."""

class PlaneZone:
    """
    Planezone defines a single plane to search against.
    """
    def __init__(self, ) -> None: ...
    XValue: float
    """X value of the direction unit vector of the plane."""
    YValue: float
    """Y value of the direction unit vector of the plane."""
    ZValue: float
    """Z value of the direction unit vector of the plane."""
    Displacement: float
    """Plane displacement in metres along the direction vector specified above."""

class PlaneZoneExpression:
    """
    
PlaneZoneExpression represents a 3D plane to search against. It may define a
search
for all parts that intersect with the plane, or a search for all parts on one
side
of the plane.
    """
    def __init__(self, ) -> None: ...
    PlanzeZone: PlaneZone
    """It defines a plane to search against."""
    PlaneZoneOperator: str
    """
            Operator to use for expression. The supported PlaneZoneOperator are: PlaneZone_above,
            PlaneZone_below, PlaneZone_intersects, PlaneZone_aboveOrIntersects and PlaneZone_belowOrIntersects.
            """

class ProximityExpression:
    """
    
ProximityExpression specifies one set of proximity criteria. The search results
from
each bomLine are combined together using an 'OR' operation.
    """
    def __init__(self, ) -> None: ...
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of source BOMLine(s) for proximity search"""
    Distance: float
    """Proximity distance in metres from the outer surface of the BOMLine geometry"""
    IncludeChildBomLines: bool
    """
            If true, all child BOMLines of source bom lines are considered for proximity
            search
            """

class SavedQueryExpression:
    """
    
SavedQueryExpression defines a search expression encapsulated as a Teamcenter
saved-query
that returns an Item, ItemRevision or any of their sub-types. The saved query
may
be a pre-defined out of the box saved query or one created using the Teamcenter
QueryBuilder
application.
    """
    def __init__(self, ) -> None: ...
    SavedQuery: Teamcenter.Soa.Client.Model.ModelObject
    """Object of an existing saved query."""
    Entries: list[str]
    """A list of attribute entries that needs to be searched."""
    Values: list[str]
    """A list of values of the above entries to be searched."""

class SearchBox:
    """
    
SearchBox defines a single box zone to search in. It contains the definition of
an
axis-aligned box and an accompanying transform to describe it orientation.
    """
    def __init__(self, ) -> None: ...
    Xmin: float
    """Point defining the minimum extent along the x-axis."""
    Ymin: float
    """Point defining the minimum extent along the y-axis."""
    Zmin: float
    """Point defining the minimum extent along the z-axis."""
    Xmax: float
    """Point defining the maximum extent along the x-axis."""
    Ymax: float
    """Point defining the maximum extent along the y-axis."""
    Zmax: float
    """Point defining the maximum extent along the z-axis."""
    Transform: list[float]
    """
            Transform defining the orientation of the box ( empty vector denotes identity transform
            ).
            """

class SearchBySizeExpression:
    """
    
SearchBySizeExpression defines a search for parts with bounding boxes that are
larger
than or smaller than a specified size.
    """
    def __init__(self, ) -> None: ...
    LargerThan: bool
    """
            If true, it searches for larger than the length specified; otherwise, searches for
            smaller.
            """
    DiagonalLength: float
    """The length of the largest bounding box diagonal, in metres."""

class SearchExpressionSet:
    """
    
SearchExpression data structure specifies the full set of search expressions
that
are to be used to perform a single structure search. Each one of the expressions
provided are combined together using a logical 'AND' between them.
    """
    def __init__(self, ) -> None: ...
    ItemAndRevisionAttributeExpressions: list[AttributeExpression]
    """itemAndRevisionAttributeExpressions"""
    OccurrenceNoteExpressions: list[OccurrenceNoteExpression]
    """A collection of Occurrence Note attribute search expressions"""
    FormAttributeExpressions: list[FormAttributeExpression]
    """A collection of Form attribute search expressions"""
    ProximitySearchExpressions: list[ProximityExpression]
    """A collection of spatial proximity search expressions"""
    BoxZoneExpressions: list[BoxZoneExpression]
    """A collection of spatial box zone expressions"""
    PlaneZoneExpressions: list[PlaneZoneExpression]
    """A collection of spatial plane zone search expressions"""
    SavedQueryExpressions: list[SavedQueryExpression]
    """A collection of saved query search expressions"""
    InClassQueryExpressions: list[InClassExpression]
    """inClassQueryExpressions"""
    SizeSearchExpression: SearchBySizeExpression
    """sizeSearchExpression"""
    DoTrushapeRefinement: bool
    """Specifies whether to perform trueshape refinement on the spatial search or not"""
    ReturnScopedSubTreesHit: bool
    """
            Specifies whether the search result should return only the sub-set of scopeBomLines
            given as input as part of the SearchScope
            """

class SearchScope:
    """
    The SearchScope specifies the scope of a search
    """
    def __init__(self, ) -> None: ...
    Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """BOM window object specifying a structure context within which to perform search"""
    ScopeBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of BOMLine objects, specifying scope of the search"""
    IgnoreOccurrenceTypes: list[str]
    """List of strings, specifying occurrence types to be ignored from search results"""

class StructureSearchResultResponse:
    """
    
StructureSearchResultResponse is the result set received from a single step in a
structure search.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains any
            exceptions if occurred during search.
            """
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            A batch of BOMLine(s) that satisfy the search criteria for this search. Not
            used for stopSearch.
            """
    LinesDone: int
    """The number of lines returned in the response. Not used for stopSearch."""
    EstimatedLinesLeft: int
    """
            An estimate of the number of lines yet to be processed. Not used for startSearch, nextSearch and stopSearch.
            """
    PercentComplete: float
    """
            Not used for startSearch, nextSearch and stopSearch.
            """
    SearchCursor: Teamcenter.Soa.Client.Model.ModelObject
    """
            Search cursor object that holds the current state of the search in the BOM session.
            Not used for stopSearch.
            """
    Finished: bool
    """A boolean value 'true' specifies that the search has stopped."""

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def StartSearch(self, Scope: SearchScope, SearchExpression: SearchExpressionSet) -> StructureSearchResultResponse:
        """    Start searching a structure for a given search expression within the scope specified.
        :param Scope: 
                         - scope within which to search
             
        :param SearchExpression: 
                         searchExpression  data structure specifies the full set of search expressions that
                         are to be used to perform this structure search
             
        :return: - result of search startup
        """
        ...
    def NextSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> StructureSearchResultResponse:
        """    
             This operation gets the next set of search results, which was initialized by the
             startSearch operation. This operation returns
             the results in batches and needs to be called repeatedly until the flag for search
             complete is true in the response. Input to this operation is the search cursor object
             which was returned by the startSearch or
             a previous call to nexSearch operation.
             

Use Cases:

             A user wants to perform structure search within a particular scope. The user needs
             to select search criteria(s), from the supported list to create search expression
             and start search operation. Once the initial set of a search result is returned,
             this operation will be used to get the next set of search result.
             

Dependencies:

             startSearch
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchCursor: 
                         Search cursor identifies a search session which was started by calling <font face="courier" height="10">startSearch</font> operation. This object is returned from the <font face="courier" height="10">startSearch</font> or previous call to <font face="courier" height="10">nextSearch</font> operation. Same should be passed as input to current
                         operation.
             
        :return: 
        """
        ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> StructureSearchResultResponse:
        """    
             This operation stops the current search identified by the search cursor object. The
             input to the operation is the search cursor object which was returned by the startSearch or previous call to nextSearch operation.
             

Use Cases:

             A user wants to perform Cacheless search within a particular scope. The user needs
             to select  search criteria(s) from the supported list to create search expression
             and start search operation. Once the initial batch of search result is returned,
             this operation can be used to stop the search.
             

Dependencies:

             nextSearch, startSearch
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchCursor: 
<b>SearchCursor</b> holds the current state of the search session which was created
                         in the <font face="courier" height="10">startSearch</font> or <font face="courier" height="10">nextSearch</font> operation. This is used as a handle to identify this
                         search when executing the next step of the search or stopping the search.
             
        :return: A flag to indicate the search is complete and service data. This operation does not
             return any partial errors.
        """
        ...

