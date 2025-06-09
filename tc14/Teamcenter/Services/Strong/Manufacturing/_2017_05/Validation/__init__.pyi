import Teamcenter.Soa.Client.Model
import typing

class RegisteredCallbackObjectsResponse:
    """
    
The response is the object containing registered callback function details and
the
service data
    """
    def __init__(self, ) -> None: ...
    Parameters: list[RegisteredCallbackParam]
    """The registered callback functions details for given input type."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member."""

class RegisteredCallbackParam:
    """
    The data objects which contains the  details of customized registered callback
functions.
    """
    def __init__(self, ) -> None: ...
    Type: str
    Library: str
    """The customization DLL name."""
    Name: str
    """The customization callback name."""
    FunctionName: str
    """The registered callback function name."""

class Validation:
    """
    Interface Validation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAllRegisteredCallbacks(self, CallbackType: str) -> RegisteredCallbackObjectsResponse:
        """    
             This operation returns all the registered customized callbacks for the given callback
             type.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param CallbackType: 
                         The type of customized registered callback functions to retrieve.
             
        :return: The response is the object containing callback function details and the service data
        """
        ...

