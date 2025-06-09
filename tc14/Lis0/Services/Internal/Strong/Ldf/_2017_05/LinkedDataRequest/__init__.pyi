import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class LdfTcTypesNames:
    def __init__(self, ) -> None: ...
    LdfTCTypesList: list[str]

class PropertiesRelationTypesStructure:
    def __init__(self, ) -> None: ...
    PropertiesMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class LinkedDataRequest:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLDFPropertiesAndRelationTypes(self, UidContextObject: str, Url: str, UidServiceProvider: str) -> PropertiesRelationTypesStructure: ...
    def GetLDFServiceProviderList(self, UidContextObject: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetTCTypesFromSemanticTypes(self, SemanticType: str) -> LdfTcTypesNames: ...

