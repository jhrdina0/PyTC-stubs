import System
import com.teamcenter._ss.util.xml
import com.teamcenter.ss

class XmlRpcBinding:
    def getXmlRpcRequest(self) -> com.teamcenter._ss.util.xml.XmlRpcRequest: ...
    def getXmlRpcResponse(self) -> com.teamcenter._ss.util.xml.XmlRpcResponse: ...
    @staticmethod
    def getBinding() -> XmlRpcBinding: ...
    @staticmethod
    def setBinding(binding: XmlRpcBinding) -> None: ...
    def sendXmlRpcRequest(self, req: com.teamcenter._ss.util.xml.XmlRpcRequest) -> None: ...
    def sendXmlRpcResponse(self, resp: com.teamcenter._ss.util.xml.XmlRpcResponse) -> None: ...
    def invoke(self, req: com.teamcenter._ss.util.xml.XmlRpcRequest) -> com.teamcenter._ss.util.xml.XmlRpcResponse: ...
    def init(self, URLstr: str, commsTokens: list[com.teamcenter.ss.SSOToken]) -> None: ...

class XmlRpcHttpBinding(XmlRpcBinding):
    def __init__(self, ) -> None: ...
    def getXmlRpcResponse(self) -> com.teamcenter._ss.util.xml.XmlRpcResponse: ...
    def getXmlRpcRequest(self) -> com.teamcenter._ss.util.xml.XmlRpcRequest: ...
    def init(self, URLstr: str, commsTokens: list[com.teamcenter.ss.SSOToken]) -> None: ...
    def sendXmlRpcRequest(self, req: com.teamcenter._ss.util.xml.XmlRpcRequest) -> None: ...
    def sendXmlRpcResponse(self, resp: com.teamcenter._ss.util.xml.XmlRpcResponse) -> None: ...

