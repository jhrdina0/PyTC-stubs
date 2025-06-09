import System
import Teamcenter.Soa.Client.Model
import typing

class GlobalConstantValue2:
    """
    Holds the name of the global constant and corresponding global constant value.
    """
    def __init__(self, ) -> None: ...
    Key: str
    """Name of the global constant."""
    Value: list[str]
    """The global constant value(s) corresponding to the specified constant."""

class GlobalConstantValueResponse2:
    """
    
            Holds the response for the getGlobalConstantValues
            operation.
            
    """
    def __init__(self, ) -> None: ...
    ConstantValues: list[GlobalConstantValue2]
    """The requested global constants."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This contains the status of the operation. A partial error is returned If the name
            global constant cannot be added to the global default cache (74502).
            """

class Constants:
    """
    Interface Constants
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetGlobalConstantValues2(self, Keys: list[str]) -> GlobalConstantValueResponse2:
        """    
             Global constants provide consistent definitions that can be used throughout the system.
             These constants have one or multiple values.  User can retrieve the values of global
             constants to determine the system behavior based on values. This operation gets the
             values of the named global constants (keys).
             This operation supports single value and multi valued global constants. This operation
             replaces deprecated operation getGlobalConstantValues.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         A list of the desired global constant names.
             
        :return: The values of the requested global constants. A partial error is returned If the
             name global constant cannot be added to the global default cache (74502).
        """
        ...

