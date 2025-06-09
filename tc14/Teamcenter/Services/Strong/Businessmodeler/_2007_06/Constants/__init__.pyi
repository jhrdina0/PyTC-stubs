import System
import Teamcenter.Soa.Client.Model
import typing

class GlobalConstantValue:
    """
    
            The GlobalConstantValue data structure holds
            a the name of the global constant corresponding global constant value
            
    """
    def __init__(self, ) -> None: ...
    Key: str
    """Name of the global constant."""
    Value: str
    """The global constant value corresponding to the specified constant."""

class GlobalConstantValueResponse:
    """
    Holds the response for the getGlobalConstantValues operation.
    """
    def __init__(self, ) -> None: ...
    ConstantValues: list[GlobalConstantValue]
    """The requested global constants."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This contains the status of the operation. A partial error is returned if the name
            global constant cannot be added to the global default cache (74502), or if the named
            constant is multivalued(74528) .
            """

class PropertyConstantKey:
    """
    
            Holds the name of the constant, name of the type and name of the property which are
            required to get the value of a property constant.
            
    """
    def __init__(self, ) -> None: ...
    ConstantName: str
    """Name of the constant."""
    TypeName: str
    """Name of the type."""
    PropertyName: str
    """Name of the property."""

class PropertyConstantValue:
    """
    Holds a the name of the property constant and corresponding property constant value
    """
    def __init__(self, ) -> None: ...
    Key: PropertyConstantKey
    """The requested property constant."""
    Value: str
    """The property constant value corresponding to the specified constant"""

class PropertyConstantValueResponse:
    """
    
            The PropertyConstantValueResponse data structure
            holds the response for the getPropertyConstantValues
            method.
            
    """
    def __init__(self, ) -> None: ...
    ConstantValues: list[PropertyConstantValue]
    """
            The resultant property constant values are returned as keyvalue pairs using PropertyConstantValue structure.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This contains the status of the operation."""

class TypeConstantKey:
    """
    
            Holds the name of the constant, name of the type which are required to get the value
            of a type constant.
            
    """
    def __init__(self, ) -> None: ...
    ConstantName: str
    """Name of the constant."""
    TypeName: str
    """Name of the type."""

class TypeConstantValue:
    """
    Holds a the name of the type constant and corresponding type constant value.
    """
    def __init__(self, ) -> None: ...
    Key: TypeConstantKey
    """The requested type constant."""
    Value: str
    """The type constant value corresponding to the specified constant."""

class TypeConstantValueResponse:
    """
    
            Holds the response for the getTypeConstantValues
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ConstantValues: list[TypeConstantValue]
    """
            The resultant type constant values are returned as key/value pairs using TypeConstantValue structure.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This contains the status of the operation."""

class Constants:
    """
    Interface Constants
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetGlobalConstantValues(self, Keys: list[str]) -> GlobalConstantValueResponse:
        """    
             Global constants provide consistent definitions that can be used throughout the system.
             These constants have one or multiple values.  User can retrieve the values of global
             constants to determine the system behavior based on values. This operation gets the
             values of the named global constants (keys).
             This operation only supports single valued global constants, for multivalued constants
             use the getGlobalConstantValues2 operation.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         A list of the desired global constant names.
             
        :return: The values of the requested global constants. A partial error is returned if the
             name global constant cannot be added to the global default cache (74502), or if the
             named constant is multivalued(74528)
        """
        ...
    def GetPropertyConstantValues(self, Keys: list[PropertyConstantKey]) -> PropertyConstantValueResponse:
        """    
             This operation gets the values of the named property constants (keys).
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         A list of the desired property constant names.
             
        :return: The values of the requested propoerty constants. A partial error is returned if the
             name prooperty constant cannot be added to the type attach cache (74507), or if the
             prooperty constant value cannot be retrieved (74521)
        """
        ...
    def GetTypeConstantValues(self, Keys: list[TypeConstantKey]) -> TypeConstantValueResponse:
        """    
             This operation gets the values of the named type constants (keys).
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         A list of the desired type constants.
             
        :return: The values of the requested type constants. A partial error is returned if the name
             type constant cannot be added to the type attach cache (74505), or if the type constant
             value cannot be retrieved (74515)
        """
        ...

