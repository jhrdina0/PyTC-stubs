import System
import System.Runtime.Serialization
import typing

class ConnectionException(InternalServerException):
    """
     
            The Connection exception is used to catch any network or I/O
            errors while marshalling a service request. These exception
            usually be recovered from, that is after the problem with the
            network has been fixed, the last service request can be retried.
            
    """
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, msg: str, code: int, level: int) -> None: ...
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, code: int, level: int, inner: System.Exception) -> None: ...
    Localpart: str
    def get_Localpart(self) -> str: ...

class InternalServerException(SoaException):
    """
    
            The internal server exception is used to catch any exceptions while
            processing a service across the different tiers.
            
    """
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, msg: str, code: int, level: int) -> None: ...
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, code: int, level: int, inner: System.Exception) -> None: ...
    Localpart: str
    Error: Error
    Errors: list[Error]
    """
             Returns  an array of contributing Errors, each with a
             message, error code and severity level.
             """
    def get_Localpart(self) -> str: ...
    def get_Error(self) -> Error: ...
    def get_Errors(self) -> list[Error]: ...
    def AddMessage(self, msg: str, code: int, level: int) -> None:
        """    
            Add the error message.
            
        :param msg: error message.
        :param code: error code.
        :param level: error level.
        :return: 
        """
        ...

class InvalidCredentialsException(Exception, SoaException):
    """
    
            Invalid Credential Exception is used to catch the exception which occurs when
            user supplied wrong username/password.
            
    """
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, msg: str, code: int, level: int) -> None: ...
    @typing.overload
    def __init__(self, message: str, code: int, level: int, ssoServerURL: str, ssoAppID: str) -> None: ...
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, code: int, level: int, inner: System.Exception) -> None: ...
    Localpart: str
    Error: Error
    """
            Return error.
            """
    SsoServerURL: str
    """
             Get the URL of the SSO server. This is only set when the system is configured in SSO mode.
             As of Teamcenter server 12.0.
            """
    SsoAppID: str
    """
             Get the SSO application ID. This is only set when the system is configured in SSO mode.
             As of Teamcenter server 12.0.
            """
    def get_Localpart(self) -> str: ...
    def get_Error(self) -> Error: ...
    def get_SsoServerURL(self) -> str: ...
    def get_SsoAppID(self) -> str: ...

class InvalidUserException(SoaException):
    """
    
            Used to catch when user is not valid user.
            
    """
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @typing.overload
    def __init__(self, code: int, level: int, msg: str, tcResponse: str) -> None: ...
    @typing.overload
    def __init__(self, code: int, level: int, msg: str, tcResponse: str, ssoServerURL: str, ssoAppID: str) -> None: ...
    @typing.overload
    def __init__(self, code: int, level: int, msg: str, tcResponse: str, inner: System.Exception) -> None: ...
    Code: int
    """
            Get the error code.
            """
    Level: int
    """
            Get the level.
            """
    TcResponse: str
    """
            Get the tcresponse.
            """
    Localpart: str
    SsoServerURL: str
    """
             Get the URL of the SSO server. This is only set when the system is configured in SSO mode.
             As of Teamcenter server 12.0.
            """
    SsoAppID: str
    """
             Get the SSO application ID. This is only set when the system is configured in SSO mode.
             As of Teamcenter server 12.0.
            """
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None: ...
    def get_Code(self) -> int: ...
    def get_Level(self) -> int: ...
    def get_TcResponse(self) -> str: ...
    def get_Localpart(self) -> str: ...
    def get_SsoServerURL(self) -> str: ...
    def get_SsoAppID(self) -> str: ...

class ProtocolException(InternalServerException):
    """
    
             The Protocol excetpion is used to catch and errors in the content
             of a service request. These errors are generally a result of a
             programming error and can not be recovered from.
            
    """
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, msg: str, code: int, level: int) -> None: ...
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, code: int, level: int, inner: System.Exception) -> None: ...
    Localpart: str
    def get_Localpart(self) -> str: ...

class ServiceException(SoaException):
    """
    
            Used to catch when the soa service fails.
            
    """
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, msg: str, code: int, level: int) -> None: ...
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str, code: int, level: int, inner: System.Exception) -> None: ...
    @typing.overload
    def __init__(self, msgs: list[str]) -> None: ...
    @typing.overload
    def __init__(self, msgs: list[str], inner: System.Exception) -> None: ...
    Messages: list[str]
    """
            Returns the array of string messages.
            """
    Errors: list[Error]
    """
            Returns the array of errors.
            """
    Uid: str
    """
            Returns the UIDs.
            """
    ClientId: str
    """
            Returns the client Id.
            """
    Localpart: str
    """
            LocalPart.
            """
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """    
            for serialization support
            
        :param info: 
        :param context: 
        :return: 
        """
        ...
    @typing.overload
    def AddMessage(self, msg: str) -> None: ...
    @typing.overload
    def AddMessage(self, msg: str, code: int, level: int) -> None: ...
    def get_Messages(self) -> list[str]: ...
    def get_Errors(self) -> list[Error]: ...
    def get_Uid(self) -> str: ...
    def set_Uid(self, value: str) -> None: ...
    def IsUidSet(self) -> bool:
        """    
            Check if uid is set.
            
        :return: 
        """
        ...
    def get_ClientId(self) -> str: ...
    def set_ClientId(self, value: str) -> None: ...
    def isClientIdSet(self) -> bool:
        """    
            True, if clientId is set else false.
            
        :return: 
        """
        ...
    def get_Localpart(self) -> str: ...

class Error:
    def __init__(self, iMessage: str, iCode: int, iLevel: int) -> None: ...
    Message: str
    """
            Get Message.
            """
    Code: int
    """
            Get Code.
            """
    Level: int
    """
            Get Level.
            """
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """    
            for serialization support
            
        :param info: 
        :param context: 
        :return: 
        """
        ...
    def get_Message(self) -> str: ...
    def get_Code(self) -> int: ...
    def get_Level(self) -> int: ...

class SoaException(System.Exception):
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    Localpart: str
    NamespaceURI: str
    def get_Localpart(self) -> str: ...
    def get_NamespaceURI(self) -> str: ...

