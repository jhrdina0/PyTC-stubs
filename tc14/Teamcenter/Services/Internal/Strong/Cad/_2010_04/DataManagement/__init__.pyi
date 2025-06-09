import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeepCopyData:
    def __init__(self, ) -> None: ...
    OtherSideObject: Teamcenter.Soa.Client.Model.ModelObject
    NRdeepCopyInfo: list[DeepCopyDataForNR]
    RelationTypeName: str
    NewName: str
    Action: int
    IsTargetPrimary: bool
    IsRequired: bool
    CopyRelations: bool

class DeepCopyDataForNR:
    def __init__(self, ) -> None: ...
    OtherSideObject: Teamcenter.Soa.Client.Model.ModelObject
    ReferenceName: str
    NewName: str
    Action: int

class MasterFormPropertiesInfo:
    def __init__(self, ) -> None: ...
    Form: Teamcenter.Soa.Client.Model.Strong.Form
    PropertyValueInfo: list[PropertyNameValueInfo]

class PropertyNameValueInfo:
    def __init__(self, ) -> None: ...
    PropertyName: str
    PropertyValues: list[str]

class RelatedObjectInfo:
    def __init__(self, ) -> None: ...
    RelatedObject: Teamcenter.Soa.Client.Model.ModelObject
    Action: int
    IsSecondary: bool
    NRdeepCopyOutput: list[RelatedObjectInfoForNR]

class RelatedObjectInfoForNR:
    def __init__(self, ) -> None: ...
    RelatedObject: Teamcenter.Soa.Client.Model.ModelObject
    Action: int
    IsSecondary: bool

class ReviseInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    BaseItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    NewRevId: str
    Name: str
    Description: str
    DeepCopyInfo: list[DeepCopyData]
    NewItemRevisionMasterProperties: MasterFormPropertiesInfo

class ReviseOutput:
    def __init__(self, ) -> None: ...
    NewItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    RelatedObjects: list[RelatedObjectInfo]

class ReviseResponse:
    def __init__(self, ) -> None: ...
    ReviseOutputMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class SaveAsNewItemInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    BaseItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ItemPropertyInfo: list[PropertyNameValueInfo]
    NewRevId: str
    Type: str
    DeepCopyInfo: list[DeepCopyData]
    NewItemMasterProperties: MasterFormPropertiesInfo
    NewItemRevisionMasterProperties: MasterFormPropertiesInfo
    ContainingFolder: Teamcenter.Soa.Client.Model.Strong.Folder

class SaveAsNewItemOutput:
    def __init__(self, ) -> None: ...
    NewItem: Teamcenter.Soa.Client.Model.Strong.Item
    NewItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    RelatedObjects: list[RelatedObjectInfo]

class SaveAsNewItemResponse:
    def __init__(self, ) -> None: ...
    SaveAsOutputMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def Revise(self, Info: list[ReviseInfo]) -> ReviseResponse: ...
    def SaveAsNewItem(self, Info: list[SaveAsNewItemInfo]) -> SaveAsNewItemResponse: ...

