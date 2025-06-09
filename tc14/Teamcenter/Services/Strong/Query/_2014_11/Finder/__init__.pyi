import System
import System.Collections
import Teamcenter.Services.Strong.Query._2012_10.Finder
import Teamcenter.Soa.Client.Model
import typing

class ObjectPropertyGroupInput:
    """
    
A structure containing an internal property name, a list of
PropertyGroupingValue
objects and a list of Business Objects.
    """
    def __init__(self, ) -> None: ...
    InternalPropertyName: str
    """The internal name for the property used for grouping"""
    PropertyValues: list[PropertyGroupingValue]
    """List of start and end property values for the internalPropertyName."""
    ObjectList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of business objects to be grouped. This is typically a subset of search results
            that need to be grouped.
            """

class ObjectsGroupedByProperty:
    """
    
A structure containing an internal property name and a map of objects to the
property
group id. It also contains a list of unmatched objects which dont match any
group.
    """
    def __init__(self, ) -> None: ...
    InternalPropertyName: str
    """The internal name of the property."""
    GroupedObjectsMap: System.Collections.Hashtable
    """
            Map  (business object, list of strings) of selected business object and its associated
            grouping names.
            """
    UnmatchedObjectList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of unmatched business objects."""

class ObjectsGroupedByPropertyResponse:
    """
    A structure containing list of ObjectPropertyGrouping objects and service data.
    """
    def __init__(self, ) -> None: ...
    GroupedObjectsList: list[ObjectsGroupedByProperty]
    """List of ObjectPropertyGrouping objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class PropertyGroupingValue:
    """
    
A structure containing start and end values for a specific property.  The end
value
is used for range comparisons if populated
    """
    def __init__(self, ) -> None: ...
    PropertyGroupID: str
    """Unique Identifier used by client to identify the group."""
    StartValue: str
    """
            String representation of the value for the property. For ranges, this is the start
            value for the range. If the client code is dealing with specific value types (int,
            double, etc.) the client code can use the appropriate client APIs to convert values
            to a string representation e.g Property::toFloatString, Property::toIntString, Property::toDateString,
            etc. On the server side, they can be converted back to the appropriate value types
            using the corresponding APIs e.g Property::parseFloat, Property::parseInt, Property::parseDate,
            etc.
            """
    EndValue: str
    """
            String representation of the end value for the property. This is optional and is
            populated only for ranges. It represents the end value of the range.See the startValue
            description for how the client and server code can convert from and to the specific
            value types.
            """

class SearchFilter2:
    """
    A structure representing a string, date or numeric type of search filter.
    """
    def __init__(self, ) -> None: ...
    SearchFilterType: str
    """The type of search filter. Valid values are "StringFilter", "DateFilter", "NumericFilter""""
    StringValue: str
    """
            The value for a string filter. This field is applicable only if the "searchFilterType"
            field is set to "StringFilter".
            """
    StringDisplayValue: str
    """
            The display value for a string filter. This field is applicable only if the "searchFilterType"
            field is set to "StringFilter".
            """
    StartDateValue: System.DateTime
    """
            The starting value for a date filter. This field is applicable only if the "searchFilterType"
            field is set to "DateFilter";.
            """
    EndDateValue: System.DateTime
    """
            The ending value for a date filter. This field is applicable only if the "searchFilterType"
            field is set to "DateFilter".
            """
    StartNumericValue: float
    """
            The starting value for a numeric filter. This field is applicable only if the "searchFilterType"
            field is set to "NumericFilter".
            """
    EndNumericValue: float
    """
            The ending value for a numeric filter. This field is applicable only if the "searchFilterType"
            field is set to "NumericFilter".
            """
    Count: int
    """
            The number of values in the filter. This field is populated on the service response
            and is ignored on the service input.
            """
    Selected: bool
    """
            A flag that indicates if the filter was previously selected and used to filter the
            results.
            """
    StartEndRange: str
    """The 'gap' used to generate the start and end values"""

class SearchInput2:
    """
    A structure containing input search criteria.
    """
    def __init__(self, ) -> None: ...
    ProviderName: str
    """The name of the search provider.  This is the RuntimeBusinessObject type name."""
    SearchCriteria: System.Collections.Hashtable
    """
            The criteria used to perform search (string/string). For example, for object set
            search, the search criteria are parentUid and object set source string.
            """
    StartIndex: int
    """The start index to return the search results"""
    MaxToReturn: int
    """
            The maximum number of search results to return. If value is  zero, no search results
            are returned; however, other information such as total results found and filters
            details are returned.
            """
    MaxToLoad: int
    """The maximum number of search results to load"""
    SearchFilterMap: System.Collections.Hashtable
    """
            The map (string,list of SearchFilter )containing the list of search filters for each
            search filter field.
            """
    SearchSortCriteria: list[Teamcenter.Services.Strong.Query._2012_10.Finder.SearchSortCriteria]
    """The criteria to use to sort the results."""
    SearchFilterFieldSortType: str
    """
            The sorting type to use to order the search filter categories in the response. The
            acceptable values are: "Alphabetical","Priority".
            """
    AttributesToInflate: list[str]
    """A list of attributes to inflate."""
    InternalPropertyName: str
    """The internal name of the property used for grouping."""

class SearchResponse2:
    """
    A service response structure containing search results
    """
    def __init__(self, ) -> None: ...
    SearchResults: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of business objects obtained after performing a search."""
    TotalFound: int
    """The total number of business objects found"""
    TotalLoaded: int
    """The total number of business objects loaded"""
    SearchFilterMap: System.Collections.Hashtable
    """
            The map (string,list of SearchFilter )containing the list of search filters for each
            search filter field
            """
    SearchFilterCategories: list[Teamcenter.Services.Strong.Query._2012_10.Finder.SearchFilterField]
    """A list of search filter categories ordered by filter priority."""
    DefaultFilterFieldDisplayCount: int
    """The default number of search filter categories to display."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data object."""
    ObjectsGroupedByProperty: ObjectsGroupedByProperty
    """
            The structure containing an internal property name and a map of objects to the property
            group id. It also contains a list of unmatched objects which don't match any group.
            """

class Finder:
    """
    Interface Finder
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GroupObjectsByProperties(self, ObjectPropertyGroupInputList: list[ObjectPropertyGroupInput]) -> ObjectsGroupedByPropertyResponse:
        """    
             This operation classifies business objects into groups. In the list of ObjectPropertyGroupInput
             objects, each object containing an internal property name, list of PropertyGroupingValue
             objects identifying groups and a list of business objects to be classified into the
             groups. Each PropertyGroupingValue object contains a start and an end value. The
             end value is used for range values if populated. Unclassified business objects are
             retuned back in a list.
             

Use Cases:

             In Active Workspace client, a user navigates to a new filter category on the filter
             panel. The cells in the visible view for the search results (e.g. list view or table
             view) need to be colored to match the colors on the bar chart for the objects in
             the search results. The client invokes this operation, which identifies the property
             group (or bar on the chart) the objects belong to. The client can then color the
             cells corresponding to the objects appropriately based on the grouping information
             that is returned.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param ObjectPropertyGroupInputList: 
                         A list containing ObjectPropertyGroupInput objects that represents property name
                         and property value information to group a list of input business objects
             
        :return: A structure containing a vector of ObjectPropertyGrouping object and  service data.
        """
        ...
    def PerformSearch(self, SearchInput: SearchInput2) -> SearchResponse2:
        """    
             This operation routes search request to a specific provider specified as providerName
             in the searchInput structures.
             
             A framework allows custom solution to be able to provide a new specific provider
             to collect data, perform sorting and filtering. Such provider can be a User Inbox
             retriever, or Full Text searcher. The new data provider can be encapsulated via a
             new runtime business object from Fnd0BaseProvider class. The implementation
             is done using its fnd0performSearch operation.
             

RuntimeBusinessObject

             ---- Fnd0BaseProvider (foundation template)
             
             -------- Fnd0GetChildrenProvider(foundation template)
             
             -------- Awp0FullTextSearchProvider (aws template)
             
             -------- Awp0TaskSearchProvider (aws template)
             
             -------- Aos0TestProvider (aosinternal template)
             
             -------- etc.
             

             This operation provides a common interface to send the request to and receive the
             response from a new data provider. Ultimately it allows common framework in UI to
             support filter, pagination, and sorting.
             
             This operation allows user to send the search input, filter values, and sorting data.
             These input values then be passed to the fnd0performSearch operation input values,
             which then use to collect, sort, and filter its results.
             
             The first two input parameters are important.  The first input is provider name.
             This is a string to represent the type name of RuntimeBusinessObject to which
             this request should be routed to.  If the template that contains the class is not
             installed, a partial error 217016 is returned. The second input is the search input
             map.  The key is different per each provider.  For example, for Full Text searcher,
             the input key would be searchString.  For User Inbox retriever, the input key would
             be Inbox Type.  The fnd0performSearch implementation for each provider shall take
             into account on the key name as it is used to store the values in OperationInput
             object.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchInput: 
                         A structure containing input search criteria
             
        :return: 217018     An invalid object is passed in the parameter "groupedObjectsMapList".
             Please report this error to your system administrator.
        """
        ...

