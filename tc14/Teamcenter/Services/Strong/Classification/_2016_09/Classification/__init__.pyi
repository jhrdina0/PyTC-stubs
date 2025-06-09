import Teamcenter.Soa.Client.Model
import typing

class AttributeValue:
    """
    This structure contains the attribute ID and the corresponding value.
    """
    def __init__(self, ) -> None: ...
    Id: int
    """The ID of the attribute."""
    Value: str
    """
            The value of the attribute.
            
            The calling client is responsible for converting the different property types (int,
            float, date etc) to a string using the appropriate functions in the SOA client framework's
            Property class.
            """

class FindValueInput:
    """
    
            Structure containing the additional criteria value(s) and unit systems which should
            be used to find the values for a certain attribute.
            
    """
    def __init__(self, ) -> None: ...
    AttributeID: int
    """The attribute ID to find the values for."""
    ClassID: str
    """
            The unique ID of the classification class in which to search (can be empty to find
            all values in all classes).
            """
    SearchInBothUnitSystems: bool
    """
            Indicates to search for values stored in both unit systems. True to find the values
            stored in both the unit system, false otherwise.
            """
    ActiveUnitsystem: int
    """The current unit system, 0 for metric, 1 for non-metric."""
    AttributeValues: list[AttributeValue]
    """
            A vector of AttributeValue structures containing attribute Ids and their corresponding
            UI values to use additionally to find the values for attributeID.
            """

class FindValuesOutput:
    """
    Structure containing the value(s) which have been found for the attribute.
    """
    def __init__(self, ) -> None: ...
    FoundValues: list[FoundValue]
    """The found values."""

class FindValuesResponse:
    """
    
            Structure containing the vector of found values. Any failures with the conversion
            will be mapped to the error message in the ServiceData list of partial errors.
            
    """
    def __init__(self, ) -> None: ...
    FindValuesOutputs: list[FindValuesOutput]
    """The found values."""
    SvcData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failures with the operation will be mapped to the error message in the ServiceData
            list of partial errors.
            """

class FoundValue:
    """
    
            Structure containing the existing values, the count how many times the value is used
            and in which unit system.
            
    """
    def __init__(self, ) -> None: ...
    UnitSystem: int
    """The unit system in which the value was found. 0 for metric, 1 for non-metric."""
    Value: str
    """The found value."""
    Count: int
    """The count how many times the value was found."""

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindValues(self, FindValueInputs: list[FindValueInput]) -> FindValuesResponse:
        """    
             This operation returns all values available for an attribute in the context of where
             it is called.
             
             For example, it returns all the values of a particular attribute in a given class
             or in the entire database.  Some examples are:
             

Find all the available length values in the Sheet Metal Screw class.
             It will return responses such as 5mm, 6mm, 7.5 mm, etc.
             
Find all the values for the Supplier attribute. It will return all
             values in all classes providing a list of all used suppliers stored in the classification.
             



             The operation can take other attribute values into consideration to narrow the results,
             for example:
             

Find all the available length values in the Sheet Metal Screw class
             where the diameter is 4mm. It will return responses such as 5mm, 6mm, etc.
             



Use Cases:

             Teamcenter Classification displays the List of Values dialog box containing a list
             of attribute values stored for the input attribute, their count and unit system in
             which those values are stored. This operation helps user to search for such stored
             values for multiple input attributes.
             
             The search can be constrained by setting other attribute values, the operations returns
             only the attribute values that are valid given the current search criteria (helping
             the user to efficiently narrow down the search and choose valid values that will
             find classified objects).
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param FindValueInputs: 
                         The input to find the values for.
             
        :return: 
        """
        ...

