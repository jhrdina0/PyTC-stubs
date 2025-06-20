import System
import System.IO
import Teamcenter.Net.TcModelEventManager.Client.res.Msg
import typing

class ResponseStream:
    def __init__(self, ) -> None: ...
    def Read(self, data: list[System.Byte]) -> int: ...

class TcMEMConnectionImpl(TcMEMConnection):
    def __init__(self, ) -> None: ...
    def GetStatus(self) -> int: ...
    def RegisterClient(self, serverIDin: str, clientIDin: str, localestring: str) -> list[str]: ...
    def UnregisterClient(self) -> list[str]: ...
    def GetEvents(self, logCorrelationID: str, currentsharedClients: System.String[]&) -> str: ...
    def PutEvents(self, serviceDataXML: str, logCorrelationID: str) -> list[str]: ...
    def GetSharedClients(self) -> list[str]: ...

class tcmemMsgLocalizer(Teamcenter.Net.TcModelEventManager.Client.res.Msg.Msg):
    def __init__(self, ) -> None: ...

class TcMEMRequest:
    def __init__(self, ) -> None: ...
    @staticmethod
    def TcMem_Init(memoryAllocator: System.IntPtr, memoryDeallocator: System.IntPtr) -> int: ...
    @staticmethod
    def TcMem_Term() -> int: ...
    @staticmethod
    def TcMem_Send(pData: list[System.Byte]) -> int: ...
    @staticmethod
    def TcMem_SendNoAck(pData: list[System.Byte]) -> int: ...
    @staticmethod
    def TcMem_SendEOF() -> int: ...
    @staticmethod
    def TcMem_Receive(pData: System.IntPtr) -> int: ...
    @staticmethod
    def TcMem_GetLastError(localizedMessage: System.IntPtr&) -> int: ...
    @staticmethod
    def TcMem_Complete() -> int: ...
    @staticmethod
    def Init() -> None: ...
    @staticmethod
    def Term() -> None: ...
    @staticmethod
    def GetLastError() -> str: ...
    @staticmethod
    def GenerateLocalTcMEMException(errorCode: int, errorMsg: str) -> TcMEMException: ...
    @staticmethod
    def ThrowTcMemNetBindingException(majorCode: int) -> None: ...
    def SetHeader(self, header: str, value: str) -> None: ...
    def ClearHeaders(self) -> None: ...
    @typing.overload
    def SetBody(self, reqStream: System.IO.Stream) -> None: ...
    @typing.overload
    def SetBody(self, reqBody: str) -> None: ...
    def Execute(self) -> str: ...
    def WaitForTcMemInstruction(self) -> int: ...
    def readTcMemResponse(self) -> int: ...
    def SendCompleteRequest(self, msg: str) -> int: ...

class ResponseStream:
    def __init__(self, ) -> None: ...
    def Read(self, data: list[System.Byte]) -> int: ...

class TcMEMConnectionImpl(TcMEMConnection):
    def __init__(self, ) -> None: ...
    def GetStatus(self) -> int: ...
    def RegisterClient(self, serverIDin: str, clientIDin: str, localestring: str) -> list[str]: ...
    def UnregisterClient(self) -> list[str]: ...
    def GetEvents(self, logCorrelationID: str, currentsharedClients: System.String[]&) -> str: ...
    def PutEvents(self, serviceDataXML: str, logCorrelationID: str) -> list[str]: ...
    def GetSharedClients(self) -> list[str]: ...

class tcmemMsgLocalizer(Teamcenter.Net.TcModelEventManager.Client.res.Msg.Msg):
    def __init__(self, ) -> None: ...

class TcMEMRequest:
    def __init__(self, ) -> None: ...
    @staticmethod
    def TcMem_Init(memoryAllocator: System.IntPtr, memoryDeallocator: System.IntPtr) -> int: ...
    @staticmethod
    def TcMem_Term() -> int: ...
    @staticmethod
    def TcMem_Send(pData: list[System.Byte]) -> int: ...
    @staticmethod
    def TcMem_SendNoAck(pData: list[System.Byte]) -> int: ...
    @staticmethod
    def TcMem_SendEOF() -> int: ...
    @staticmethod
    def TcMem_Receive(pData: System.IntPtr) -> int: ...
    @staticmethod
    def TcMem_GetLastError(localizedMessage: System.IntPtr&) -> int: ...
    @staticmethod
    def TcMem_Complete() -> int: ...
    @staticmethod
    def Init() -> None: ...
    @staticmethod
    def Term() -> None: ...
    @staticmethod
    def GetLastError() -> str: ...
    @staticmethod
    def GenerateLocalTcMEMException(errorCode: int, errorMsg: str) -> TcMEMException: ...
    @staticmethod
    def ThrowTcMemNetBindingException(majorCode: int) -> None: ...
    def SetHeader(self, header: str, value: str) -> None: ...
    def ClearHeaders(self) -> None: ...
    @typing.overload
    def SetBody(self, reqStream: System.IO.Stream) -> None: ...
    @typing.overload
    def SetBody(self, reqBody: str) -> None: ...
    def Execute(self) -> str: ...
    def WaitForTcMemInstruction(self) -> int: ...
    def readTcMemResponse(self) -> int: ...
    def SendCompleteRequest(self, msg: str) -> int: ...

class TcMEMConnectionException(TcMEMException):
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, message: str) -> None: ...

class TcMEMException(System.Exception):
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, msg: str) -> None: ...
    def getErrorCode(self) -> int: ...

class TcMEMConnection:
    TCMEM_CONNECTION_STATUS_CHECK_OK: int
    TCMEM_CONNECTION_STATUS_CHECK_FAILED: int
    TCMEM_CONNECTION_STATUS_CHECK_BAD_RESPONSE: int
    def GetStatus(self) -> int: ...
    def RegisterClient(self, serverIDin: str, clientIDin: str, localestring: str) -> list[str]: ...
    def UnregisterClient(self) -> list[str]: ...
    def GetEvents(self, logCorrelationID: str, currentsharedClients: System.String[]&) -> str: ...
    def PutEvents(self, serviceDataXML: str, logCorrelationID: str) -> list[str]: ...
    def GetSharedClients(self) -> list[str]: ...

class TcMEMNetBindingLoader:
    def __init__(self, ) -> None: ...
    @staticmethod
    def GetTcMemNetBinding() -> None: ...
    @staticmethod
    def GetTcMEMConnectionInstance() -> TcMEMConnection: ...

class TcMEMProtocolException(TcMEMException):
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, msg: str) -> None: ...

class TcMEMRuntimeException(TcMEMException):
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, msg: str) -> None: ...

class TcMEMUnrecognisedException(TcMEMException):
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, msg: str) -> None: ...

class TcMEMConnectionException(TcMEMException):
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, message: str) -> None: ...

class TcMEMException(System.Exception):
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, msg: str) -> None: ...
    def getErrorCode(self) -> int: ...

class TcMEMProtocolException(TcMEMException):
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, msg: str) -> None: ...

class TcMEMRuntimeException(TcMEMException):
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, msg: str) -> None: ...

class TcMEMUnrecognisedException(TcMEMException):
    @typing.overload
    def __init__(self, msg: str) -> None: ...
    @typing.overload
    def __init__(self, errorNum: int, msg: str) -> None: ...

class TcMEMConnection:
    TCMEM_CONNECTION_STATUS_CHECK_OK: int
    TCMEM_CONNECTION_STATUS_CHECK_FAILED: int
    TCMEM_CONNECTION_STATUS_CHECK_BAD_RESPONSE: int
    def GetStatus(self) -> int: ...
    def RegisterClient(self, serverIDin: str, clientIDin: str, localestring: str) -> list[str]: ...
    def UnregisterClient(self) -> list[str]: ...
    def GetEvents(self, logCorrelationID: str, currentsharedClients: System.String[]&) -> str: ...
    def PutEvents(self, serviceDataXML: str, logCorrelationID: str) -> list[str]: ...
    def GetSharedClients(self) -> list[str]: ...

class TcMEMNetBindingLoader:
    def __init__(self, ) -> None: ...
    @staticmethod
    def GetTcMemNetBinding() -> None: ...
    @staticmethod
    def GetTcMEMConnectionInstance() -> TcMEMConnection: ...

