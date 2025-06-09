import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class ImportUnmanagedDataResponse:
    def __init__(self, ) -> None: ...
    TransientFileReadTickets: list[str]
    ModifiedObjectList: list[str]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RelativeStructureChildInfo:
    def __init__(self, ) -> None: ...
    ChildID: str
    ObjectType: str
    RefDesignator: str
    ChildAttrList: System.Collections.Hashtable
    AttrListRel: System.Collections.Hashtable
    RelationType: str
    ActionRequired: str
    StructModification: System.Collections.Hashtable
    ChildChangeType: System.Collections.Hashtable

class RelativeStructureParentInfo:
    def __init__(self, ) -> None: ...
    ParentID: str
    ObjectType: str
    ParentAttrList: System.Collections.Hashtable
    ChildInfo: list[RelativeStructureChildInfo]
    ActionRequired: str
    ParentChangeType: System.Collections.Hashtable

class RequirementsManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportUnmanagedData(self, RelativeStructParent: list[RelativeStructureParentInfo], ImportOptions: list[str]) -> ImportUnmanagedDataResponse: ...

