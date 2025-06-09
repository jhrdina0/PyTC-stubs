import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class LOVInput:
    """
    
            This represents the operation data.  Operations such as Create, Edit, Revise, Save
            As, Search or any other operation that requires the data to be passed generically
            to the LOV service operations  have the property values represented through the LOVInput
            for computing a LOV.
            
    """
    def __init__(self, ) -> None: ...
    OwningObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Owning object for the operation in context. a. Edit operation - Object being edited.
            b. Save operation - Object being saved. c. Revise operation - Object being revised.
            d. SaveAs operation - Object being copied. e. Search operation - Saved Query Object
            for searching. f. If an operation does not have an object, specify the value as null
            and ensure boName is passed for the same. For example, during creation, client does
            not have an object. Therefore specify the business object name of the object being
            created.  For example, if Item object is being created, specify the boName as "Item"
            and operationName as "Create".
            """
    BoName: str
    """
            Name of the source business object. For example, Item is the source business object
            for Item Descriptors. If the owningObject is not null, then it can be empty. Server
            can determine the business object name from the owningObject. It is mandatory for
            Create operation where owningObject is null
            """
    OperationName: str
    """
            Name of the operation  being performed. Valid names are Create, Revise, SaveAs, Edit,
            Search, Save
            """
    PropertyValues: System.Collections.Hashtable
    """
            A map of property names and values (string, vector<string>). The client is responsible
            for converting the values of the different property types (int, float, date .etc)
            to a string using the appropriate toXXXString functions in the SOA client  framework's
            Property class. Single valued properties will have a single value in the value vector,
            while Multi-valued properties will have multiple values in the value vector.
            """

class LovFilterData:
    """
    Filter Data used in InitialLOVData.
    """
    def __init__(self, ) -> None: ...
    FilterString: str
    """
            The desired string used to filter the search results. For example, if "Green" is
            entered as a filter string, the results returned for LOV values will include the
            LOV values that match the query criteria AND contain the string "Green" in the LOV
            Description or any of the filter attributes. Case sensitive nature is honoured based
            on TC_ignore_case_on_search preference.
            """
    MaxResults: int
    """Maximum number of LOV results that server should retrieve from the database"""
    NumberToReturn: int
    """
            Number of objects to be processed in case of dynamic LOVs to return LOV values and
            in other LOV cases it is to return the number of LOV values from the LOV results.
            This number must be less than or equal to maxResults
            """
    SortPropertyName: str
    """Property name on which to sort the results. This is optional"""
    Order: int
    """
            1=sort in ascending order, 2=sort in descending order. Ignored if sortPropertyName
            is null.
            """

class InitialLovData:
    """
    Initial LOV Data sent to the server during an LOV query.
    """
    def __init__(self, ) -> None: ...
    Lov: Teamcenter.Soa.Client.Model.Strong.ListOfValues
    """
            The ListOfValues that is being evaluated;Use this when the lovInput is not possible
            to construct and need to get the values of specified Lov, otherwise pass as null.
            """
    LovInput: LOVInput
    """
            This is a container of key-value pairs representing the desired entries for different
            property fields for different operations (Create, SaveAs, Revise, etc.). It is used
            for context-based evaluation of the LOV values where the property values are substituted
            into query criteria. It is also used for interdependent LOV evaluation e.g to evaluate
            interdependent LOV values at dependent levels given the values at the higher levels
            that are populated on the lovInput
            """
    PropertyName: str
    """The name of the Property for which LOV is being evaluated."""
    FilterData: LovFilterData
    """Filter critieria and other search data."""

class LOVColumnNames:
    """
    
            Structure containing column names for the LOV value property, LOV description property
            and the filter attributes
            
    """
    def __init__(self, ) -> None: ...
    LovValueProp: str
    """
            The attribute on the object to be used as the LOV value. When the user selects a
            row from the list of values in the dynamic LOV widget (an item for example), this
            configuration point tells the system which attribute to use as the LOV value. In
            case of Static LOVs, the name of the property is returned as "lov_value". In case
            of Dynamic LOVs, it is a name as specified in BMIDE.
            """
    LovDescrProp: str
    """
            The attribute on the object to be used as the LOV value description. When the user
            selects a row from the list of values in the dynamic LOV widget (an item for example),
            this configuration point tells the system which attribute to use as the LOV value
            description. In case of Static LOVs, the name of the property is returned as "lov_value_description".
            In case of Dynamic LOVs, it is a name as specified in BMIDE. It can be have empty
            value if it is not specified by BMIDE administrator.
            """
    FilterProperties: list[str]
    """
            The filter properties would appear as additional columns along with the LOV Value
            and LOV description in the Dynamic LOV
            """
    DisplayNames: System.Collections.Hashtable
    """
            Displayable names for each of lovValueProp, lovDescrProp, filterProperties that clients
            can use to display the same
            """
    ColumnManagementFlags: System.Collections.Hashtable
    """
            Specifies the UI characteristics such as sortability and filterability, of the filter
            columns along with the LOV Value and LOV Description columns. The values of these
            characteristics are provided as bit values. At present, only the first two bits are
            populated, as listed below. Rest of the bits are reserved for future use.
            
            The first bit indicates sortability of the column. Value "0" indicates it is not
            sortable, while value "1" indicates it is sortable.
            
            The second bit indicates if the column is filterable. Value "0" indicates it is not
            filterable, while value "1" indicates it can be filtered.
            """

class LOVBehaviorData:
    """
    
            Container of data such as LOV usage, Style, Lov Column Names. Additionally it  contains
            interdependent properties that can be used for optimization by the client
            
    """
    def __init__(self, ) -> None: ...
    LovUsage: int
    """Indicates if LOV is exhaustive (=1) or suggestive(=2) or Range (=3)"""
    Style: str
    """
            Possible values are Standard, Range, Hierarchical, Interdependent and Coordinated
            Standard          - A simple list of values Interdependent - An interdependent  list
            of values, where each value has a  nested list of values. A list of States would
            have a list of Cities for each State. For this style of LOV the dependentProps will
            have a list of property names that are associated with each level of the LOV hierarchy
            Hierarchical      - Same as the Interdependent, but only the last level of values
            is associated with a property Coordinated    - This is similar to Interdependent;
            however levels 2-N will only have a single value. When the user selects a value from
            the first level LOV, the system can then fill property values for all levels Range
            - Subset (ranges) of valid values in terms of upper and lower ranges
            """
    ColumnNames: LOVColumnNames
    """Names of the columns when displayed in clients"""
    DescriptionsAttached: list[bool]
    """
            This is a list of Boolean values that indicates if the description for each of the
            column properties is attached
            """
    DependendProps: list[str]
    """
            Names of interdependent properties. If the LOV is not an interdependent or coordinated
            LOV, this list will be empty
            """
    RangeUpperLimit: str
    """Upper limit for Range LOV. This is not applicable to any other style of LOV"""
    RangeLowerLimit: str
    """Lower limit for Range LOV. This is not applicable to any other style of LOV"""

class LOVData:
    """
    
            This data structure is not for end user consumption. Data in this structure will
            be used by server for returning the next set of LOV values
            
    """
    def __init__(self, ) -> None: ...
    Style: str
    """Possible values are Standard, Dynamic, Range, Hierarchical, Interdependent and Coordinated"""
    FilterData: LovFilterData
    """Filter critieria and other search data."""
    UnProcessedObjects: list[str]
    """
            These are the list of UIDs that will be processed by the server in subsequent calls
            to get next set of LOV values
            """
    AdditionalValuesSkipped: bool
    """
            Boolean flag to indicate if additional UIDs (Values in static LOV) are skipped or
            not
            """
    CurrentIndex: int
    """Current index of the LOV results that have been processed."""
    Lovs: list[Teamcenter.Soa.Client.Model.Strong.ListOfValues]
    """LOVs of Dynamic LOV which is being evaluated"""

class LOVSearchResults:
    """
    
            This structure contains the LOV results from the getInitialLOVValues or getNextLOVValues
            operations
            
    """
    def __init__(self, ) -> None: ...
    LovValues: list[LOVValueRow]
    """
            This is a list of LOVValueRow objects. Each LOVValueRow object represents a single
            row of the LOV results. It includes the LOV value property, the description property
            and all the filter properties (the filter properties are the ones whose values are
            used for filtering the search results based on user input)
            """
    MoreValuesExist: bool
    """
            true indicates there are more values available which will can be retrieved by a call
            to the getNextValues operation
            """
    BehaviorData: LOVBehaviorData
    """
            LOV data used to define the UI component behavior. This includes data such as LOV
            usage, Style, Lov Column Names. Additionally it  contains interdependent properties
            that can be used for optimization by the client
            """
    LovData: LOVData
    """
            If moreValuesExist is true, this object is passed as input to the getNextValues operation
            to get the next list of LOV search results
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData"""

class LOVValueRow:
    """
    
            This represents a row of LOV values. It includes the internal and display values
            for the various columns for each LOV value
            
    """
    def __init__(self, ) -> None: ...
    Uid: str
    """
            UID of the object. This applies to dynamic LOVs.  Server sends valid UID for dynamic
            LOV and empty in other LOV cases.. Client can send the same UID when a value is selected
            to validateLOVValueSelection operation for effective validation. This is empty for
            for non dynamic LOVs
            """
    PropInternalValues: System.Collections.Hashtable
    """
            The internal values of all the properties on a single row of the LOV search results.
            The parseXXX functions in the SOA framework class can be used to retrieve the values
            for the specific property types
            """
    PropInternalValueTypes: System.Collections.Hashtable
    """
            value type map for each property which has internal values, PROP_untyped (0) No Value
            type PROP_char (1) Value is a single character PROP_date (2) Value is a date PROP_double
            (3) Value is a double PROP_float (4) Value is a float PROP_int (5) Value is an integer
            PROP_logical (6) Value is a logical PROP_short (7) Value is a short PROP_string (8)
            Value is a character string PROP_typed_reference (9) Value is a typed reference PROP_untyped_reference
            (10) Value is an untyped reference PROP_external_reference (11) Value is an external
            reference PROP_note (12) Value is a note PROP_typed_relation (13) Value is a typed
            relation PROP_untyped_relation (14) Value is an untyped relation
            """
    PropDisplayValues: System.Collections.Hashtable
    """The display values of all the properties on a single row of the LOV search results"""
    ChildRows: list[LOVValueRow]
    """
            Next level of row values in case of hierarchical LOV. This is recursive and can go
            down multiple levels in the hierarchy
            """

class ValidateLOVValueSelectionsResponse:
    """
    
            Response structure indicating validity of LOV value selection and containing updated
            property values and interdependent LOV values
            
    """
    def __init__(self, ) -> None: ...
    PropHasValidValues: bool
    """Indicates whether input property has valid values."""
    DependentPropNames: list[str]
    """
            Names of dependent properties server modified to be updated by client as a results
            of dependency with input property selection. This can be empty.
            """
    UpdatedPropValues: LOVValueRow
    """
            Updated property values. It contains both internal and display values of the updated
            properties.  It can be empty.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class LOV:
    """
    Interface LOV
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetInitialLOVValues(self, InitialData: InitialLovData) -> LOVSearchResults:
        """    
             This operation is invoked to query the data for a property having an LOV attachment.
             The results returned from the server also take into consideration any filter string
             that is in the input.  This operation returns both LOV meta data as necessary for
             the client to render the LOV and partial LOV values list as specified.  The operation
             will return the results in the LOVSearchResults data structure. Maximum number of
             results to be returned are specified in the InitialLOVData data structure. If there
             are more results, the moreValuesExist flag in the LOVSearchResults data structure
             will be true. If the flag is true, more values can be retrieved with a call to the
             getNextLOVValues operation.
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param InitialData: 
                         Input data to get LOV results for any LOV
             
        :return: 
        """
        ...
    def GetNextLOVValues(self, LovData: LOVData) -> LOVSearchResults:
        """    
             This operation is invoked after a call to getInitialLOVValues if the moreValuesExist
             flag is true in the LOVSearchResults output returned from a call to the getInitialLOVValues
             operation. The operation will retrieve the next set of LOV values
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param LovData: 
                         Input data to get next set of LOV results for Dynamic LOV. This is returned as part
                         of the LOVSearchResults output from the call to getInitialLOVValues operation
             
        :return: LOV Search Results (LOVSearchResults instance). The LOV Search Results contains LOV
             metadata information (LOV usage, LOV style, etc.). It also contains the instance
             data (LOV values) that the client can use to render the LOV UI widget. The output
             also contains information as to whether there are more results to be processed in
             which case a user can page to get next set of values (this triggers a call to the
             subsequent getNextLOVValues operation).  Partial errors are returned in the ServiceData
             field in the LOV Search Results. Possible errors are:
        """
        ...
    def ValidateLOVValueSelections(self, LovInput: LOVInput, PropName: str, UidOfSelectedRows: list[str]) -> ValidateLOVValueSelectionsResponse:
        """    
             This operation can be invoked after selecting a value from the LOV.  Use this operation
             to do additional validation to be done on server such as validating Range value,
             getting the dependent properties values in case of interdependent LOV (resetting
             the dependendent property values), Coordinated LOVs ( populating dependent property
             values )
             

Teamcenter Component:

             List of Values (LOV) - Component to define lists of values and to associate them
             with attributes and properties.  Associations can be stored in the database (persistent)
             or independently associated for each Teamcenter session (run time).
             
        :param LovInput: 
                         updated LOV input with new selection
             
        :param PropName: 
                         It is the name of the Property for which LOV is being evaluated
             
        :param UidOfSelectedRows: 
                         Pass the uids from the selected rows. Every LovValueRow returned from server is designated
                         with valid UID for dynamic LOV. That is the value need to be passed to the server
                         for effective validation. For other LOVs it is empty
             
        :return: The response data indicating validity of LOV value selections and containing updated
             property values and interdependent property values
        """
        ...

