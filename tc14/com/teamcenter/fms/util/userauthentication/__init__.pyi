import System
import com.teamcenter.fms.servercache.proxy
import com.teamcenter.fms.servercache.proxy.HTTPCommonsEmulator
import com.teamcenter.fms.ticket.ticketinternal
import typing

class AuthenticationConfig:
    def isAuthenticationEnabled(self) -> bool: ...
    def toString(self) -> str: ...

class AuthenticationException(com.teamcenter.fms.servercache.proxy.FSCException):
    @typing.overload
    def __init__(self, lm: com.teamcenter.fms.ticket.ticketinternal.LocaleMessage, cause: System.Exception, aServerURI: str, httpStatus: int, rawText: str) -> None: ...
    @typing.overload
    def __init__(self, lm: com.teamcenter.fms.ticket.ticketinternal.LocaleMessage, aServerURI: str, httpStatus: int, rawText: str) -> None: ...

class AuthenticationToken:
    def setToRequest(self, request: com.teamcenter.fms.servercache.proxy.HTTPCommonsEmulator.HttpMethodBase) -> None: ...
    def toString(self) -> str: ...

class AuthenticationUtil:
    def __init__(self, ) -> None: ...
    @staticmethod
    def isAuthenticationEnabled(config: AuthenticationConfig) -> bool: ...

class ClientAuthenticatorInterface:
    def __init__(self , *args: typing.Any) -> None: ...
    def getAuthenticatedToken(self, authConfig: AuthenticationConfig) -> AuthenticationToken: ...
    def authenticateUser(self, authConfig: AuthenticationConfig) -> AuthenticationToken: ...
    def setTicketAuthenticationHeaders(self, token: AuthenticationToken, request: com.teamcenter.fms.servercache.proxy.HTTPCommonsEmulator.HttpMethodBase) -> None: ...

class NetAuthenticationUtil(AuthenticationUtil):
    def __init__(self, ) -> None: ...
    @staticmethod
    def getAuthenticatorInstance() -> NetTcSSAuthenticator: ...
    @staticmethod
    def processUserAuthenticationResponse(response: com.teamcenter.fms.servercache.proxy.HTTPCommonsEmulator.HttpMethodBase) -> TcSSConfiguration: ...
    @staticmethod
    def throwAuthenticationRequiredException() -> None: ...

class NetTcSSAuthenticator:
    def __init__(self, ) -> None: ...
    @staticmethod
    def getInstance() -> NetTcSSAuthenticator: ...
    def setTicketAuthenticationHeaders(self, token: AuthenticationToken, request: com.teamcenter.fms.servercache.proxy.HTTPCommonsEmulator.HttpMethodBase) -> None: ...
    def getAuthenticatedToken(self, authConfig: AuthenticationConfig) -> AuthenticationToken: ...
    def authenticateUser(self, authConfig: AuthenticationConfig) -> AuthenticationToken: ...

class SSOLoginService:
    def __init__(self, ) -> None: ...
    @staticmethod
    def getAuthenticatedToken(config: TcSSConfiguration) -> SSOToken: ...

class SSOToken(AuthenticationToken):
    def __init__(self, userId: str, sessionKey: str) -> None: ...
    def toString(self) -> str: ...
    def setToRequest(self, request: com.teamcenter.fms.servercache.proxy.HTTPCommonsEmulator.HttpMethodBase) -> None: ...

class TcSSConfiguration(AuthenticationConfig):
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, newAppId: str, newLoginServiceUrl: str) -> None: ...
    def toString(self) -> str: ...
    def getAppId(self) -> str: ...
    def getLoginServiceUrl(self) -> str: ...

