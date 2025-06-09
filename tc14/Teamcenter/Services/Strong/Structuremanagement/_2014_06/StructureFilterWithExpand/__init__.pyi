import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExpandAndSearchOutput:
    """
    
ExpandAndSearchOutput contains the result BOMLine with the satisfied search
condition indexes.
    """
    def __init__(self, ) -> None: ...
    ResultLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The result BOMLine."""
    SatisfiedConditions: list[int]
    """
            The indexes of search conditions satisfied by result line. Index will start from
            0.
            """

class ExpandAndSearchResponse:
    """
    
This structure provides output for the expandAndSearch operation.
ExpandAndSearchResponse
contains the list of a structure which contains result BOMLine with the
satisfied
search condition indexes.
    """
    def __init__(self, ) -> None: ...
    OutputLines: list[ExpandAndSearchOutput]
    """Structure with result BOMLine with the satisfied search condition indexes."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class SearchCondition:
    """
    
Search condition contains the information of search criteria. This will form a
condion
as "bl_item_item_id = 000016" where bl_item_item_id is a property and 000016
is input value given by a user for search. User can combine more than one
conditions
with logical operator 'AND' and 'OR' like "bl_item_item_id = 000016 AND
bl_level_starting_0
!= 4 AND bl_is_precise == false" .

Allowed relational operators:

= Â Â Â Â   Use this operator for wild card search. This operator
will do a wild card search for given value, Â Â Â Â   no need to
give a '*'.

==  Use this operator to search exact match of search value

!=Â Â Â Â   Use this operator to search other values except search
value

>Â Â Â Â   Use this operator to search greater value than search
value

>=  Use this operator to search greater and equal value than search value

<Â Â Â Â   Use this operator to search lesser value than search
value

<=  Use this operator to search lesser and equal value than search value

Note: Comparison will be done on the basis of BOMLine property type only.

    """
    def __init__(self, ) -> None: ...
    LogicalOperator: str
    """
            The logical operator for combining multiple search conditions. Only 'AND' and 'OR'
            can be used for combining the multiple conditions.
            """
    PropertyName: str
    """The property name to use for search."""
    RelationalOperator: str
    """The relational operator to use for search value comparison."""
    InputValue: str
    """The property value to use for search."""

class StructureFilterWithExpand:
    """
    Interface StructureFilterWithExpand
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandAndSearch(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], SearchConditions: list[SearchCondition]) -> ExpandAndSearchResponse:
        """    
             This operation does a full expansion of the given lines, then performs the search
             on the expanded structure with the given search conditions. The lines of a structure
             and search criteria as BOMLine property value are required. This operation
             returns the result BOMLines with satisfied condition indexes.
             
             A user can search for BOMLine with multiple search criteria by separating
             those criteria with an "OR" operator. The output line contains the information
             about the search conditions in the form of indexes which are satisfied by a particular
             BOMLine.
             
             Logical operator for the first condition is ignored
             
             This service will support search criterias like "find no = 10 and quantity = 1
             or quantity = 20 and AbsOccId = CFG". In this criteria "AND" has precedence
             over "OR" operator.
             

             Comparison are done on the basis of BOMLine property type only.
             

Valid inputs for Date type property : A user must give input in a specific
             date format that is defined in timelocal.xml If the date format is not defined in
             timelocal.xml then default format will be considered as "dd-mmm-yyyy hh:mm"
             .
             
Example. "01-jan-2010 12:23"
             

             Invalid inputs for Date type property :    "01-jan-201012:23", "01-january-2010
             12:23", "32-jan-2010 12:23", "32-jan-20112 12:23"
             


Valid inputs for String values : A user must give a valid string for search
             it should not contain spaces until u meant to find a string with spaces. Leading
             and trailing spaces will be taken care.
             
Example: "validInput" , "validInput  ", "   validInput", "  validInput   "
             
             Invalid Input : "valid   Input"
             
Note: Since Comparison is done on the basis of BOMLine property type
             only. There are some integer and double type properties which is defined as string
             on BOMLine so you need to pass the exact value in that case that will be a
             string comparison.
             
Example : "010" and "10" will be considered as different values
             

Valid inputs for Boolean type property : only true and false is allowed. For
             those properties which is shown as Y and N in Rich Client you should pass
             the value as Y and N only.
             

Valid inputs for Double and Integer type property : A user must provide a
             valid value which could be parsed successfully to specified type.
             
Example : "12334" , "234.456", "007854", "0088.675"
             
Invalid Input : "345fg", "fr4567", "456.54er"
             

Note: 1) If a condition contains a invalid inputValue than comparison
             for that property will be skipped. Results will be returned for valid values only.
             
             2) Equal operator(=) will be used for wild card search by default. User must
             not pass a wild card character('*' or '?') in a string value. Search
             will be case insensitive for all relational operators except "==" operator.
             
             3) Only "AND" and "OR" logical operators are supported.
             
             4) For integer, double and Date types "=" and "==" operators have same
             behavior.
             


Use Cases:

             Search for BOMLine with their properties - A User can search for BOMLine in a collapsed
             structure by giving criteria as their property values like "bl_item_item_id = 000016"
             where bl_item_item_id is a property and 000016 is input value given by user for search.
             
Example1: A User searches for some BOMLines by giving the criteria "find
             no. =10 OR quantity > 1" and BOMLine1 satisfies the condition "find
             no. =10" and BOMLine2 satisfies the condition "quantity > 1" then
             the first output line will contain the BOMLine1 and search condition index
             as 0 and the second output line will contain the BOMLine2 and search condition
             index as 1.
             

Example2: A User searches for some BOMLines by giving the criteria
             "find no = 10 and quantity > 1 or Find No = 20 and quantity = 1" and BOMLine1
             satisfies the condition "find no = 10 and quantity > 1" and BOMLine2
             satisfies the condition "Find No = 20 and quantity = 1" then the first output
             line will contain the BOMLine1 and search condition index  as 0,1 and the
             second output line will contain the BOMLine2 and search condition index as
             

Teamcenter Component:

             BOM Expand - Set of core services that allow to efficiently solve a product structure
             based on revision rules; effectivities etc.
             
        :param Lines: 
                         The lines of a structure where search is to be performed.
             
        :param SearchConditions: 

        :return: 
        """
        ...

