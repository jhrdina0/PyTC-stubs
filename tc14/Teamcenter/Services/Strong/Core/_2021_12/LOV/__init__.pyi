import System
import System.Collections
import Teamcenter.Services.Strong.Core._2013_05.LOV
import Teamcenter.Soa.Client.Model
import typing

class ValidateLOVPropertyData:
    """
    
            The ValidateLOVPropertyData structure contains LOV property value validadity,
            dependentPropNames and updated property values.
            
    """
    def __init__(self, ) -> None: ...
    PropName: str
    """Input Property name to which the LOV is attached."""
    PropHasValidValues: bool
    """
            Names of dependent properties server modified to be updated by client as a results
            of dependency with input property selection. This can be empty.
            """
    DependentPropNames: list[str]
    """
            Names of dependent properties server modified to be updated by client as a results
            of dependency with input property selection. This can be empty.
            """
    UpdatedPropValues: Teamcenter.Services.Strong.Core._2013_05.LOV.LOVValueRow
    """
            Updated property values. It contains both internal and display values of the updated
            properties. It can be empty.
            """

class ValidatePropertyValuesForLOVInBulkInputData:
    """
    This represents the LOV property value validation input for the Business Object(s).
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """A unique string used to identify return data elements with this input structure."""
    OwningObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object for which this operation being invoked.
            
            a. Edit operation - Object to be edited.
            
            b. Save operation - Object to be saved.
            
            c. Revise operation - Object to be revised.
            
            d. SaveAs operation - Object to be copied.
            
            e. Search operation - Saved Query Object for searching.
            
            If an operation does not have an object, specify the value as null and ensure boName
            is not empty.
            
            For example, during creation, client does not have an object. Therefore specify the
            business object name of the object being created. For example, if Item object is
            being created, specify the boName as "Item" and operationName as "Create".
            """
    BoName: str
    """
            Name of the source business object. For example, Item is the source business
            object for Item Descriptors. If the owningObject is not null, then
            boName can be empty. Server can determine the business object name from the
            owningObject. It is mandatory for Create operation where owningObject
            is null.
            """
    OperationName: str
    PropNames: list[str]
    """
            Name of the properties for which LOV validation being done. If no properties are
            specified then no validation happens and partial error will be returned.
            """
    PropValues: System.Collections.Hashtable
    """
            A map (string, list) of property names and values that are being edited by User.
            The client is responsible for converting the values of the different property types
            (int, float, date .etc) to a string using the appropriate toXXXString functions in
            the service operation client framework's Property class. Single valued properties
            will have a single value in the value list while Multi-valued properties will have
            multiple values in the value list.
            """

class ValidatePropertyValuesForLOVInBulkOutput:
    """
    
            The ValidatePropertyValuesForLOVInBulkOutput contains clientID and LOV property
            value validation output.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            The unmodified value from the input clientId. This can be used by the caller
            to indentify this data structure with the source input.
            """
    ValidateLOVPropertyOutput: list[ValidateLOVPropertyData]
    """A list containing property names with list of ValidateLOVPropertyData."""

class ValidatePropertyValuesForLOVInBulkResponse:
    """
    
            The ValidatePropertyValuesForLOVInBulkResponse contains the output response
            structure for validatePropertyValuesForLOVInBulk service operation.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ValidatePropertyValuesForLOVInBulkOutput]
    """
            A list containing the clientID and list of ValidatePropertyValuesForLOVInBulkOutput.
            For each input, one ValidatePropertyValuesForLOVInBulkOutput will be returned.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data object associated with the operation."""

class LOV:
    """
    Interface LOV
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ValidatePropertyValuesForLOVInBulk(self, Inputs: list[ValidatePropertyValuesForLOVInBulkInputData]) -> ValidatePropertyValuesForLOVInBulkResponse: ...

