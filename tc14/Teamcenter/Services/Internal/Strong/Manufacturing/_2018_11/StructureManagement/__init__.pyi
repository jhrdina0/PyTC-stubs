import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement
import Teamcenter.Soa.Client.Model
import typing

class BrokenPartsCSIDToPropsInfo:
    def __init__(self, ) -> None: ...
    CsidValue: str
    PropTypes: list[str]
    PropValues: list[str]

class BrokenProductViewsData:
    def __init__(self, ) -> None: ...
    ProductView: Teamcenter.Soa.Client.Model.ModelObject
    AttachedToLine: Teamcenter.Soa.Client.Model.ModelObject
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class ContextGroup:
    def __init__(self, ) -> None: ...
    Contexts: list[OpenContextInfo]
    PersistentObject: Teamcenter.Soa.Client.Model.ModelObject
    ApplicationId: str
    CollaborationContext: Teamcenter.Soa.Client.Model.ModelObject

class EvaluateLinksData:
    def __init__(self, ) -> None: ...
    Link: str
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class EvaluateLinksResponse:
    def __init__(self, ) -> None: ...
    Output: list[ContextGroup]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AdditionaInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class FindBrokenPartsDetails:
    def __init__(self, ) -> None: ...
    TargetPV: Teamcenter.Soa.Client.Model.ModelObject
    FirstLevelChildrenCSID: list[str]
    PropertyInfo: BrokenPartsCSIDToPropsInfo
    ChildrenMap: System.Collections.Hashtable
    AdditonalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class FindBrokenPartsInPVInputInfo:
    def __init__(self, ) -> None: ...
    TargetDatasets: list[Teamcenter.Soa.Client.Model.ModelObject]
    TargetScope: Teamcenter.Soa.Client.Model.ModelObject
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class FindBrokenPartsInPVResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    BrokenPartsDetail: list[FindBrokenPartsDetails]

class FindBrokenProductViewsDetails:
    def __init__(self, ) -> None: ...
    Scope: Teamcenter.Soa.Client.Model.ModelObject
    BrokenProductViews: list[BrokenProductViewsData]

class FindBrokenProductViewsInputInfo:
    def __init__(self, ) -> None: ...
    UnnestedScopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    AdditionalInfo: Teamcenter.Services.Internal.Strong.Manufacturing._2015_10.StructureManagement.AdditionalInfo

class FindBrokenProductViewsResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    BrokenProductViewsDetails: list[FindBrokenProductViewsDetails]

class OpenContextInfo:
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    Object: Teamcenter.Soa.Client.Model.ModelObject
    Views: list[Teamcenter.Soa.Client.Model.ModelObject]
    StructureContext: Teamcenter.Soa.Client.Model.ModelObject

class StructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def EvaluateLinks(self, Input: list[EvaluateLinksData]) -> EvaluateLinksResponse: ...
    def FindBrokenPartsInProductView(self, Input: FindBrokenPartsInPVInputInfo) -> FindBrokenPartsInPVResponse: ...
    def FindBrokenProductViews(self, Input: FindBrokenProductViewsInputInfo) -> FindBrokenProductViewsResponse: ...

