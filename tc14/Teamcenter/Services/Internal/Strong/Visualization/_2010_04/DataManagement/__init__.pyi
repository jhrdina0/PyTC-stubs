import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GatherMarkupControlObject:
    def __init__(self, ) -> None: ...
    Uid: str
    Name: str
    AdditionalInfo: System.Collections.Hashtable

class GatherBasedDatasetInfo:
    def __init__(self, ) -> None: ...
    Uid: str
    Name: str
    AdditionalInfo: System.Collections.Hashtable
    NamedRefInfos: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.NamedRefsInDataset]
    ControlObj: GatherMarkupControlObject
    MarkupList: list[GatherMarkupInfo]

class GatherBasedDatasetTypeInfo:
    def __init__(self, ) -> None: ...
    RelatedDatasets: list[GatherBasedDatasetInfo]
    ToolPreferences: list[str]
    Name: str

class GatherItemInfo:
    def __init__(self, ) -> None: ...
    ItemUid: str
    ItemName: str
    ItemRevUid: str
    ItemRevName: str
    ToolPreferences: list[str]

class GatherBusinessDataInfo:
    def __init__(self, ) -> None: ...
    GatherItemInfo: GatherItemInfo
    GatherDatasetTypeInfos: list[GatherBasedDatasetTypeInfo]

class GatherInputInfo:
    def __init__(self, ) -> None: ...
    Id: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ControlObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    IdAdditionalInfo: System.Collections.Hashtable

class GatherMarkupInfo:
    def __init__(self, ) -> None: ...
    Uid: str
    Name: str
    AdditionalInfo: System.Collections.Hashtable
    NamedRefInfos: list[Teamcenter.Services.Internal.Strong.Visualization._2008_06.DataManagement.NamedRefsInDataset]

class GatherResponse:
    def __init__(self, ) -> None: ...
    BusinessDataList: list[GatherBusinessDataInfo]
    SvcData: Teamcenter.Soa.Client.Model.ServiceData

class GatherSsoInfo:
    def __init__(self, ) -> None: ...
    LoginServiceUrl: str
    AppId: str

class GatherServerInfo:
    def __init__(self, ) -> None: ...
    Protocol: str
    HostPath: str
    ServerMode: str
    UseSso: bool
    TccsEnvironment: str
    SsoInfo: GatherSsoInfo
    AdditionalInfo: System.Collections.Hashtable

class GatherSessionInfo:
    def __init__(self, ) -> None: ...
    SessionDescriminator: str
    SessionAdditionalInfo: System.Collections.Hashtable

class GatherUserAgentDataInfo:
    def __init__(self, ) -> None: ...
    UserApplication: str
    UserAppVersion: str
    UserAdditionalInfo: System.Collections.Hashtable

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GatherMarkups(self, SelectedInputInfos: list[GatherInputInfo], ServerInfo: GatherServerInfo, SessionInfo: GatherSessionInfo, UserDataAgentInfo: GatherUserAgentDataInfo) -> GatherResponse: ...

