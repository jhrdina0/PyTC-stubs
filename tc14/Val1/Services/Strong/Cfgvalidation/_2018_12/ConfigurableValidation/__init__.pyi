import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateInput:
    """
    
CreateInput structure used to capture the
            inputs required for creation of a validation result object. This is
a recursive structure
            containing the CreateInput(s) for any secondary (compounded) objects
that might be
            created or updated.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    BoName: str
    """Business Object type name."""
    StringProps: System.Collections.Hashtable
    """Map of string property names to values (string, string)."""
    StringArrayProps: System.Collections.Hashtable
    """Map of string array property names to values (string, list(string))."""
    DoubleProps: System.Collections.Hashtable
    """Map of double property names to values (string, double)."""
    DoubleArrayProps: System.Collections.Hashtable
    """Map of double array property names to values (string, list(double))."""
    FloatProps: System.Collections.Hashtable
    """Map of float property names to values (string, float)."""
    FloatArrayProps: System.Collections.Hashtable
    """Map of float array property names to values (string, list(float))."""
    IntProps: System.Collections.Hashtable
    """Map of int property names to values (string, int)."""
    IntArrayProps: System.Collections.Hashtable
    """Map of int array property names to values (string, list(int))."""
    BoolProps: System.Collections.Hashtable
    """Map of boolean property names to values (string, bool)."""
    BoolArrayProps: System.Collections.Hashtable
    """Map of boolean array property names to values (string, list(bool))."""
    DateProps: System.Collections.Hashtable
    """Map of DateTime property names to values (string, DateTime)."""
    DateArrayProps: System.Collections.Hashtable
    """Map of DateTime array property names to values (string, list(DateTime))."""
    BusinessObjectProps: System.Collections.Hashtable
    """
            Map of BusinessObject property names to values (string, BusinessObject). The supported
            Business Object types are any POM_object types.
            """
    BusinessObjectArrayProps: System.Collections.Hashtable
    """
            Map of BusinessObject array property names to values (string, list(BusinessObject)
            ). The supported Business Object types are any POM_object types.
            """
    CompoundCreateInput: System.Collections.Hashtable
    """
            CreateInput(s) for compounded objects. Map of reference or relation property name
            to secondary CreateInput objects (string, list(CreateInput)).
            """

class ConfigurableValidation:
    """
    Interface ConfigurableValidation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateValidationResults(self, CreateOrUpdateInputs: list[CreateInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates and/or updates validation result objects with the given list
             of CreateInput data structures, and retrieves validation result objects after
             the create/update operations are completed. The values of the required properties
             (val0AgentRevName, val0CheckerClassName, Val0ValidationId,
             and val0TargetContext) in a CreateInput
             structure are used to identify a unique validation result object in the database.
             The values of the above properties are populated in each CreateInput structure
             of a validation result object and used by queries to find an existing validation
             result object. The value of val0TargetContext
             property is stored in the BOMap of a CreateInput structure. The property
             values for properties val0CheckerClassName, val0AgentRevName,
             and val0ValidationId  are stored in the StringMap
             of a  CreateInput structure. If no existing validation result object matches
             the given property values of val0TargetContext,
             val0CheckerClassName, val0AgentRevName, and val0ValidationId
             in the CreateInput structure, a new validation result object is created. If
             an existing validation result object is found, the existing validation result object
             is updated.
             

Teamcenter Component:

             Configurable Validation - Component for the template - val1cfgvalidation
             
        :param CreateOrUpdateInputs: 
                         A list of data structures that contain validation data for creating and/or updating
                         validation result objects.
             
        :return: 
        """
        ...
    def GetValidationResults(self, ValAgentRevObjects: list[Teamcenter.Soa.Client.Model.Strong.ValidationAgentRevision], ValDataObjects: list[Teamcenter.Soa.Client.Model.Strong.ValDataRevision], ResultOwningObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation retrieves configurable validation result objects that are found with
             the given input data. This operation will take the given configurable validation
             agents, validation data objects, and ItemRevision and/or Component business objects
             that logically owns validation results to build the search criteria to find the associated
             validation result objects. Configurable validation agents represent applications
             that were used to generate the configurable validation result objects. Validation
             data objects represent the specialized validation checks that are referenced by the
             configurable validation result objects.
             

Use Cases:

             A configurable validaiton result object is generated for a business object by a configurable
             validation agent using the specialized validation logic that is defined by a validation
             data object. This operation will be used to search for the configurable validation
             result objects that a user will be interested in by reducing the search scope using
             the given input objects.
             

Teamcenter Component:

             Configurable Validation - Component for the template - val1cfgvalidation
             
        :param ValAgentRevObjects: 
                         A list of ValidationAgentRevision objects.
             
        :param ValDataObjects: 
                         A list of ValDataRevision objects.
             
        :param ResultOwningObjects: 
                         A list of ItemRevision and/or Design Element business objects.
             
        :return: This operation returns the found ValidationResult business objects in the plain object
             list of the ServiceData structure.
        """
        ...

