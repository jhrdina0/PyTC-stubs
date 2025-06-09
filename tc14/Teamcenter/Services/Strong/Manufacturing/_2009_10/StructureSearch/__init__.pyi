import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeValues:
    """
    
            AttributeValues data structure specifies data values to be bound to the various search
            expressions for execution of the search. It encapsulates the values to be specified
            for each of the data types that can occur in any of the attribute search expressions.
            
    """
    def __init__(self, ) -> None: ...
    BoolValues: list[bool]
    """boolean values that any of the accompanying set of search expressions may use"""
    IntValues: list[int]
    """integer values that any of the accompanying set of search expressions may use"""
    DoubleValues: list[float]
    """double values that any of the accompanying set of search expressions may use"""
    StringValues: list[str]
    """string values that any of the accompanying set of search expressions may use"""
    DateValues: System.DateTime
    """date values that any of the accompanying set of search expressions may use"""
    TagValues: list[Teamcenter.Soa.Client.Model.ModelObject]
    """tag values that any of the accompanying set of search expressions may use"""

class AttributeExpression:
    """
    
            AttributeExpression encapsulates information to build a query on the attribute of
            an Item or ItemRevision or their sub-classes in the structure search scope. * A set
            of these attribute expressions is contained inside a SearchExpressionInfo object.
            Search on multiple values specified within one AttributeExpression are combined with
            a logical 'OR' operation.
            
    """
    def __init__(self, ) -> None: ...
    ClassName: str
    """Item or ItemRevision or their sub-classes"""
    AttributeName: str
    """The attribute of the above 'className' to be searched on"""
    AttributeType: str
    """The type of the attribute to be searched on"""
    QueryOperator: str
    """operator to use for search value comparison"""
    Values: AttributeValues
    """values"""

class BoxZoneExpression:
    """
    
            BoxZoneExpression specifies one set of Box zone criteria. The search results from
            each SearchBox are combined together using an 'OR' operation. The spatial search
            returns a match with the search expression if a object either lies inside or intersects
            the search boxes
            
    """
    def __init__(self, ) -> None: ...
    SearchBoxes: list[SearchBox]
    """Boxes around which to search"""
    BoxOperator: str
    """Operator to use for expression"""

class FormAttributeExpression:
    """
    
            FormAttributeExpression contains information to search on a single Form Attribute
            within a containing SearchExpressionInfo object. The search on the multiple values
            specified within one FormAttributeExpression are combined with a logical 'OR' operation.
            
    """
    def __init__(self, ) -> None: ...
    IsItemForm: bool
    """Item or ItemRevision form"""
    RelationType: Teamcenter.Soa.Client.Model.ModelObject
    """The Form relation type"""
    FormType: Teamcenter.Soa.Client.Model.ModelObject
    """Form type to be searched"""
    AttributeName: str
    """The attribute of the above Form type to be searched"""
    AttributeType: str
    """The type of the attribute to be searched on"""
    QueryOperator: str
    """operator to use for search value comparison"""
    Values: AttributeValues
    """The values to test for"""

class InClassExpression:
    """
    InClassExpression
    """
    def __init__(self, ) -> None: ...
    InClassClassNames: list[str]
    """inClassClassNames"""
    InClassAttributeIDs: list[int]
    """inClassAttributeIDs"""
    InClassAttributeValues: list[str]
    """inClassAttributeValues"""

class LogicalDesignatorAttribute:
    """
    
            an object that represents a single LD attribute. This type will be used in a vector
            that will represent a Logical Designator .
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """the attribute name"""
    Value: str
    """the attribute value"""

class MFGSearchCriteria:
    """
    TBD
    """
    def __init__(self, ) -> None: ...
    ObjectTypes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """the types of objects to search"""
    LogicalDesignator: list[LogicalDesignatorAttribute]
    """logical designator data"""
    Refinements: list[MFGSearchRefinementSet]
    """refinements on the search"""

class MFGSearchRefinement:
    """
    refinement on the search
    """
    def __init__(self, ) -> None: ...
    RelatedScopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            a vector of additional scopes. These are not the scopes in which we expect to find
            the results. These are the scopes from which we start to impose the limitations.
            """
    Relations: list[RelationInfo]
    """
            a vector specifying the list of relations between the related scopes to the "searched"
            objects
            """

class MFGSearchRefinementSet:
    """
    TBD
    """
    def __init__(self, ) -> None: ...
    Refinements: list[MFGSearchRefinement]
    """a vector of refinements. The refinements are combined with logical 'OR' between them"""

class OccurrenceNoteExpression:
    """
    
            OccurrenceNoteExpression contains information to search on a single occurrence note
            type within a containing SearchExpressionInfo object. The search on the multiple
            values specified within one OccurrenceNoteExpression are combined with a logical
            'OR' operation.
            
    """
    def __init__(self, ) -> None: ...
    NoteType: str
    """Occurrence note type to search"""
    QueryOperator: str
    """operator to use for search value comparison"""
    Values: list[str]
    """The list of values to search for"""

class PlaneZone:
    """
    Planezone defines a single plane to search against.
    """
    def __init__(self, ) -> None: ...
    Xvalue: float
    """X value of the direction unit vector of the plane"""
    Yvalue: float
    """Y value of the direction unit vector of the plane"""
    Zvalue: float
    """Z value of the direction unit vector of the plane"""
    Displacement: float
    """Plane displacement in metres along the direction vector specified above"""

class PlaneZoneExpression:
    """
    
            PlaneZoneExpression represents a 3D plane to search against. It may define a search
            for all parts that intersect with the plane, or a search for all parts on one side
            of the plane.
            
    """
    def __init__(self, ) -> None: ...
    PlanzeZone: PlaneZone
    """planzeZone"""
    PlaneZoneOperator: str
    """Operator to use for expression"""

class ProximityExpression:
    """
    
            ProximityExpression specifies one set of proximity criteria. The search results from
            each bomLine are combined together using an 'OR' operation.
            
    """
    def __init__(self, ) -> None: ...
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """BOM lines around which to search"""
    Distance: float
    """Proximity distance in metres from the outer surface of the BomLine geometry"""
    IncludeChildBomLines: bool
    """includeChildBomLines"""

class RelationInfo:
    """
    information about the relation
    """
    def __init__(self, ) -> None: ...
    RelationName: str
    """the name of the relation"""
    MatchType: str
    """the match type"""
    ObjectClass: str
    """the class from which the relation starts (e.g. MfgOperation)"""

class SavedQueryExpression:
    """
    
            SavedQueryExpression defines a search expression encapsulated as a Teamcenter saved-query
            that returns an Item, ItemRevision or any of their sub-types. The saved query may
            be a pre-defined out of the box saved query or one created using the Teamcenter QueryBuilder
            application
            
    """
    def __init__(self, ) -> None: ...
    SavedQuery: Teamcenter.Soa.Client.Model.ModelObject
    """Tag of an existing saved query"""
    Entries: list[str]
    """Attribute entries that are to be searched for"""
    Values: list[str]
    """Values of the above entries to be searched for"""

class SearchBox:
    """
    
            SearchBox defines a single box zone to search in. It contains the definition of an
            axis-aligned box and an accompanying transform to describe it orientation.
            
    """
    def __init__(self, ) -> None: ...
    Xmin: float
    """Plane defining the minimum extent along the x-axis"""
    Ymin: float
    """Plane defining the minimum extent along the y-axis"""
    Zmin: float
    """Plane defining the minimum extent along the z-axis"""
    Xmax: float
    """Plane defining the maximum extent along the x-axis"""
    Ymax: float
    """Plane defining the maximum extent along the y-axis"""
    Zmax: float
    """Plane defining the maximum extent along the z-axis"""
    Transform: list[float]
    """
            Transform defining the orientation of the box ( empty vector denotes identity transform
            )
            """

class SearchBySizeExpression:
    """
    
            SearchBySizeExpression defines a search for parts with bounding boxes that are larger
            than or smaller than a specified size
            
    """
    def __init__(self, ) -> None: ...
    LargerThan: bool
    """Search for larger than if this is set to true, smaller than if set to false"""
    DiagonalLength: bool
    """Length of the largest bounding box diagonal in metres"""

class SearchExpressionSet:
    """
    
            SearchExpression data structure specifies the full set of search expressions that
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

class StructureSearchResultResponse:
    """
    
            StructureSearchResultResponse is the result set received from a single step in a
            structure search.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A batch of Objects that satisfy the search criteria for this search"""
    ObjectDone: int
    """The number of objects in the structure that have been processed so far"""
    EstimatedObjectsLeft: int
    """An estimate of the number of lines yet to be processed"""
    PercentComplete: float
    """percentComplete"""
    SearchCursor: Teamcenter.Soa.Client.Model.ModelObject
    """Search cursor object that holds the current state of the search in the BOM session"""
    Finished: bool
    """A boolean value which when 'true' specifies the search is finished"""

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def NextSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> StructureSearchResultResponse:
        """    Process one additional step of the search identified by the cursor.
        :param SearchCursor: 
                         searchCursor
             
        :return: - result of next search step
        """
        ...
    def StartSearch(self, Scope: list[Teamcenter.Soa.Client.Model.ModelObject], SearchExpression: SearchExpressionSet, MfgSearchCriteria: MFGSearchCriteria) -> StructureSearchResultResponse:
        """    
             Start searching a structure for a given search expression within the scope specified.
             search can also be narrowed to a specific object type, item name, and logical designator
             
        :param Scope: 
                         scope lines within which to search
             
        :param SearchExpression: 
                         generic search expression
             
        :param MfgSearchCriteria: 
                         The MFG addition search criteria
             
        :return: - result of search startup
        """
        ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> StructureSearchResultResponse:
        """    
             Stop and close down a search identified by a cursor. Throws SearchAlreadyStoppedException
             if the search has already been stopped.
             
        :param SearchCursor: 
                         the search identifier
             
        :return: StructureSearchResultResponse
        """
        ...

