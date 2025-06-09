import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class SearchFilter:
    """
    A structure representing a string, date or numeric type of search filter.
    """
    def __init__(self, ) -> None: ...
    SearchFilterType: str
    """The type of search filter. Valid values are "StringFilter", "DateFilter", "NumericFilter"."""
    StringValue: str
    """
            The value for a string filter. This field is applicable only if the "searchFilterType"
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
            search results. This field is populated on the service response and is ignored on
            the service input.
            """
    StartEndRange: str
    """The 'gap' used to generate the start and end values"""

class SearchFilterField:
    """
    A structure containing details about a search filter field.
    """
    def __init__(self, ) -> None: ...
    InternalName: str
    """The internal name for the search filter field."""
    DisplayName: str
    """The display name for the search filter field."""
    DefaultFilterValueDisplayCount: int
    """The default number of search filter values to display within the search filter field."""

class SearchInput:
    """
    A structure containing input search criteria
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
    """The maximum number of search results to return"""
    MaxToLoad: int
    """The maximum number of search results to load"""
    SearchFilterMap: System.Collections.Hashtable
    """
            The map (string,list of SearchFilter) containing the list of search filters for each
            search filter field.
            """
    SearchSortCriteria: list[SearchSortCriteria]
    """The criteria to use to sort the results."""
    SearchFilterFieldSortType: str
    """
            The sorting type to use to order the search filter categories in the response. The
            acceptable values are: "Alphabetical","Priority".
            """
    AttributesToInflate: list[str]
    """The list of attributes to inflate."""

class SearchResponse:
    """
    A service response structure containing search results.
    """
    def __init__(self, ) -> None: ...
    SearchResults: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of business objects obtained after performing a search."""
    TotalFound: int
    """The total number of business objects found."""
    TotalLoaded: int
    """The total number of business objects loaded."""
    SearchFilterMap: System.Collections.Hashtable
    """
            The map (string,list of SearchFilter) containing the list of search filters for each
            search filter field based on the search results.
            """
    SearchFilterCategories: list[SearchFilterField]
    """A list of search filter categories ordered by filter priority."""
    DefaultFilterFieldDisplayCount: int
    """The default number of search filter categories to display."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data object."""

class SearchSortCriteria:
    """
    The criteria to use to sort the results.
    """
    def __init__(self, ) -> None: ...
    FieldName: str
    """The name of the field on which to perform the sorting."""
    SortDirection: str
    """The direction in which the sorting needs to be perfomed - 'ASC' or 'DESC'."""

class Finder:
    """
    Interface Finder
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def PerformSearch(self, SearchInput: SearchInput) -> SearchResponse:
        """    
             This operation routes search request to a specific provider specified as providerName
             in the searchInput structures.  A framework will allow custom solution to be able
             to provide a new specific provider to collect data, perform sorting and filtering.
             Such provider can be a User Inbox retriever, or Full Text searcher. The new data
             provider can be encapsulated via a new runtime business object from Fnd0BaseProvider
             class. The implementation is done using its fnd0performSearch operation.  RuntimeBusinessObject
             ---- Fnd0BaseProvider (foundation template) -------- Fnd0GetChildrenProvider(foundation
             template) -------- Awp0FullTextSearchProvider (aws template) -------- Awp0TaskSearchProvider
             (aws template) -------- Aos0TestProvider (aosinternal template) -------- etc.  This
             operation provides a common interface to send the request to and receive the response
             from a new data provider. Ultimately it allows common framework in UI to support
             filter, pagination, and sorting.  This operation allows user to send the search input,
             filter values, and sorting data.  These input values will then be passed to the fnd0performSearch
             operation input values, which then use to collect, sort, and filter its results.
             The first two input parameters are important.  The first input is provider name.
             This is a string to represent the type name of RuntimeBusinessObject to which this
             request should be routed to.  If the template that contains the class is not installed,
             a partial error is returned in the service data. The second input is the search input
             map.  The key will be different per each provider.  For example, for Full Text searcher,
             the input key would be searchString.  For User Inbox retriever, the input key would
             be Inbox Type.  The fnd0performSearch implementation for each provider shall take
             into account on the key name as it is used to store the values in OperationInput
             object.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchInput: 
                         The search input
             
        :return: The search results, search filters for each search filter field based on the search
             results, and search filter categories ordered by filter priority.  The following
             partial errors may be returned: 217016     Invalid search provider name. When invalid
             search provider name is passed in
        """
        ...

