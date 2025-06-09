import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetClassificationHierarchiesResponse:
    def __init__(self, ) -> None: ...
    Hierarchies: System.Collections.Hashtable
    Ids: System.Collections.Hashtable
    Data: Teamcenter.Soa.Client.Model.ServiceData

class GetClassificationPropertiesResponse:
    def __init__(self, ) -> None: ...
    Propnames: System.Collections.Hashtable
    Propvalues: System.Collections.Hashtable
    Hierarchies: System.Collections.Hashtable
    PropDeprecatedflags: System.Collections.Hashtable
    Data: Teamcenter.Soa.Client.Model.ServiceData

class Classification:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetClassificationHierarchies(self, Wsos: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> GetClassificationHierarchiesResponse: ...
    def GetClassificationProperties(self, Wsos: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> GetClassificationPropertiesResponse: ...

