import System
import System.Collections.Generic
import System.Net
import System.Xml
import Teamcenter.Schemas.Soa.Objectpropertypolicy
import Teamcenter.Schemas.Soa._2006_03.Base
import Teamcenter.Soa.Common
import typing

class Monitor:
    @staticmethod
    def IsEnabled() -> bool: ...
    @staticmethod
    def Enable(enable: bool) -> None: ...
    @staticmethod
    def MarkStart(label: str) -> None: ...
    @staticmethod
    @typing.overload
    def MarkEnd(label: str) -> None: ...
    @staticmethod
    @typing.overload
    def MarkEnd() -> None: ...
    @staticmethod
    def CommandStart(label: str) -> None: ...
    @staticmethod
    def CommandEnd(label: str) -> None: ...

class AnyCredentials:
    def __init__(self, ) -> None: ...
    User: str
    Password: str
    Group: str
    Role: str
    Locale: str
    Descrimator: str

class NoDTDResolver(System.Xml.XmlResolver):
    def __init__(self, ) -> None: ...
    Credentials: System.Net.ICredentials
    def set_Credentials(self, value: System.Net.ICredentials) -> None: ...
    def GetEntity(self, absoluteUri: System.Uri, role: str, ofObjectToReturn: System.Type) -> typing.Any: ...

class AuthUtils:
    def __init__(self, ) -> None: ...
    ARG_USER: str
    ARG_USERNAME: str
    ARG_SPONSER: str
    ARG_SPONSERED: str
    ARG_PASSWORD: str
    ARG_SSO_PASSWORD: str
    ARG_GROUP: str
    ARG_SPONSERED_GROUP: str
    ARG_ROLE: str
    ARG_SPONSERED_ROLE: str
    ARG_LOCALE: str
    ARG_SESSION_DISCRIMINATOR: str
    ARG_DESCRIMATOR: str
    @staticmethod
    def IsLoginOperation(service: str, operation: str) -> bool: ...
    @staticmethod
    @typing.overload
    def GetUserCredentials(service: str, operation: str, xmlDocument: str) -> AnyCredentials: ...
    @staticmethod
    @typing.overload
    def GetUserCredentials(inputArgs: list[typing.Any]) -> AnyCredentials: ...
    @staticmethod
    def SetDescriminator(inputArgs: list[typing.Any], descriminator: str) -> list[typing.Any]: ...
    @staticmethod
    def SetGroupRoleToDefault(inputArgs: list[typing.Any]) -> list[typing.Any]: ...

class PolicyMarshaller:
    def __init__(self, ) -> None: ...
    @staticmethod
    @typing.overload
    def ToWire(policyProperty: Teamcenter.Soa.Common.PolicyProperty) -> Teamcenter.Schemas.Soa._2006_03.Base.PolicyProperty: ...
    @staticmethod
    @typing.overload
    def ToWire(policyType: Teamcenter.Soa.Common.PolicyType) -> Teamcenter.Schemas.Soa._2006_03.Base.PolicyType: ...
    @staticmethod
    @typing.overload
    def ToWire(objectPropertyPolicy: Teamcenter.Soa.Common.ObjectPropertyPolicy) -> Teamcenter.Schemas.Soa._2006_03.Base.ObjectPropertyPolicy: ...
    @staticmethod
    @typing.overload
    def ToLocal(xsdProperty: Teamcenter.Schemas.Soa._2006_03.Base.PolicyProperty) -> Teamcenter.Soa.Common.PolicyProperty: ...
    @staticmethod
    @typing.overload
    def ToLocal(xsdType: Teamcenter.Schemas.Soa._2006_03.Base.PolicyType) -> Teamcenter.Soa.Common.PolicyType: ...
    @staticmethod
    @typing.overload
    def ToLocal(wire: Teamcenter.Schemas.Soa._2006_03.Base.ObjectPropertyPolicy) -> Teamcenter.Soa.Common.ObjectPropertyPolicy: ...
    @staticmethod
    def ParseProperty(typeNode: System.Xml.XmlNode) -> Teamcenter.Soa.Common.PolicyProperty: ...
    @staticmethod
    def ParseType(typeNode: System.Xml.XmlNode) -> Teamcenter.Soa.Common.PolicyType: ...
    @staticmethod
    @typing.overload
    def Serialize(objProperty: typing.Any, modifiers: dict[str, str]) -> None: ...
    @staticmethod
    @typing.overload
    def Serialize(policyProperty: Teamcenter.Soa.Common.PolicyProperty) -> Teamcenter.Schemas.Soa.Objectpropertypolicy.Property: ...
    @staticmethod
    @typing.overload
    def Serialize(policyType: Teamcenter.Soa.Common.PolicyType) -> Teamcenter.Schemas.Soa.Objectpropertypolicy.ObjectType: ...

