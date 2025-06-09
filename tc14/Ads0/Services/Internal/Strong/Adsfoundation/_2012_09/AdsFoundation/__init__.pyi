import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ResolveSourceDocumentResponse:
    def __init__(self, ) -> None: ...
    MatchingObjects: list[Teamcenter.Soa.Client.Model.Strong.Item]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AdsFoundation:
    def __init__(self , *args: typing.Any) -> None: ...
    def ResolveSourceDocument(self, ObjectType: str, CompId: str, AttrValueMap: System.Collections.Hashtable, SrcRevId: str, SrcOwnOrg: str) -> ResolveSourceDocumentResponse: ...

