import System
import System.Collections.Generic
import System.Collections.Specialized
import System.Net.Sockets
import com.teamcenter._ss.util.xml
import com.teamcenter.ss.util
import typing

class ClientSocketIOException(com.teamcenter.ss.util.CompatibleCausallyException):
    @typing.overload
    def __init__(self, message: str, cause: System.Exception) -> None: ...
    @typing.overload
    def __init__(self, cause: System.Exception) -> None: ...

class InitialLoginHandler:
    def __init__(self , *args: typing.Any) -> None: ...
    def login(self, loginURL: str, prefs: System.Collections.Specialized.NameValueCollection) -> None: ...

class LoginSocketProtocol:
    @typing.overload
    def __init__(self, listeningSocket: System.Net.Sockets.TcpListener) -> None: ...
    @typing.overload
    def __init__(self, loginPort: int) -> None: ...
    def waitForLoginToFinish(self, timeoutSeconds: int) -> None: ...
    def loginSucceeded(self) -> None: ...
    def loginFailed(self) -> None: ...
    def loginCancelled(self) -> None: ...
    def sessionAgentDisabled(self) -> None: ...
    def sessionAgentFailed(self) -> None: ...
    def beginUserInteraction(self) -> None: ...
    def endUserInteraction(self) -> None: ...

class MaliciousClientException(System.Exception):
    def __init__(self, client: System.Net.Sockets.TcpClient) -> None: ...
    def getMaliciousClient(self) -> System.Net.Sockets.TcpClient: ...

class ServerSocketIOException(com.teamcenter.ss.util.CompatibleCausallyException):
    @typing.overload
    def __init__(self, message: str, cause: System.Exception) -> None: ...
    @typing.overload
    def __init__(self, cause: System.Exception) -> None: ...

class TccsLogin:
    def __init__(self, ) -> None: ...
    def login(self, loginURL: str, prefs: System.Collections.Specialized.NameValueCollection) -> None: ...

class TccsUtil:
    def __init__(self, ) -> None: ...
    @staticmethod
    def invokeTccs(loginURL: str, reqData: dict[str, typing.Any]) -> dict[str, typing.Any]: ...

class XmlRpcSocketBinding:
    @typing.overload
    def __init__(self, s: System.Net.Sockets.TcpClient) -> None: ...
    @typing.overload
    def __init__(self, host: str, port: int) -> None: ...
    def getXmlRpcRequest(self) -> com.teamcenter._ss.util.xml.XmlRpcRequest: ...
    def getXmlRpcResponse(self) -> com.teamcenter._ss.util.xml.XmlRpcResponse: ...
    def sendXmlRpcRequest(self, req: com.teamcenter._ss.util.xml.XmlRpcRequest) -> None: ...
    def sendXmlRpcResponse(self, resp: com.teamcenter._ss.util.xml.XmlRpcResponse) -> None: ...
    def shutdownIO(self) -> None: ...
    def shutdown(self) -> None: ...

