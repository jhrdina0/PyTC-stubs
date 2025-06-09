import System.Collections
import typing

class SupportedHandlerArgumentsInfoOutput:
    """
    
SupportedHandlerArgumentsInfoOutput structure represents handler Data with
dynamic
hints.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """A unique string used to identify return data elements."""
    HandlerData: str
    AdditionalData: System.Collections.Hashtable
    """
            This is a map that will point to a list of strings. It can be used incase there is
            a need to send any additional data.
            """

class SupportedHandlerArgumentsInput:
    """
    SupportedHandlerArgumentsInput stucture represent the input handler name and
clientId.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """A unique string supplied by the caller. This ID is used to identify return data elements."""
    HandlerName: str
    """Name of the handler."""
    AdditionalData: System.Collections.Hashtable
    """
            This is a map that will point to a list of strings. It can be used incase there is
            a need to send any additional data as input to this operation.
            """

class SupportedHandlerArgumentsReponse:
    """
    
SupportedHandlerArgumentsReponse represents list of
SupportedHandlerArgumentsInfoOutput
which contains information about handlerData and clientId.
    """
    def __init__(self, ) -> None: ...
    Output: list[SupportedHandlerArgumentsInfoOutput]
    """
            List of SupportedHandlerArgumentsInfoOutput structure which contains handler data
            info.
            """

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetSupportedHandlerArguments(self, Input: list[SupportedHandlerArgumentsInput]) -> SupportedHandlerArgumentsReponse: ...

