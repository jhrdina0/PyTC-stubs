import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ParentToChildCompositeStructure2:
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.ModelObject
    ChildLines: list[ParentToChildCompositeStructure2]
    AttachmentRelation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    IsRelation: bool
    PropValueInfo: System.Collections.Hashtable

class CompositeViewResponse2:
    def __init__(self, ) -> None: ...
    CompositeServiceData: Teamcenter.Soa.Client.Model.ServiceData
    CompositeLineNodes: ParentToChildCompositeStructure2

class ParentToChildTargetReferenceStructure2:
    def __init__(self, ) -> None: ...
    TargetReferenceLine: Teamcenter.Soa.Client.Model.ModelObject
    ChildLines: list[ParentToChildTargetReferenceStructure2]
    UnderlyingComponent: Teamcenter.Soa.Client.Model.ModelObject
    IsRelation: bool
    HasMultipleRelations: bool
    PropValueInfo: System.Collections.Hashtable

class TargetReferencesViewDataResponse2:
    def __init__(self, ) -> None: ...
    TargetReferencesServiceData: Teamcenter.Soa.Client.Model.ServiceData
    TargetReferencesLineNodes: ParentToChildTargetReferenceStructure2

class SimStructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetCompositeLineNodesExpandBelow2(self, Component: Teamcenter.Soa.Client.Model.ModelObject, FilterItemType: int, FilterRelationType: list[str], ShowRelatedAnalysisAll: bool, ShowRelatedAnalysisRootOnly: bool, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ColumnNames: list[str]) -> CompositeViewResponse2: ...
    def GetTargetRefLineNodesExpandBelow2(self, TargetReferenceLine: Teamcenter.Soa.Client.Model.ModelObject, ModelConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ProductCurrentLine: Teamcenter.Soa.Client.Model.ModelObject, ProductConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ColumnNames: list[str]) -> TargetReferencesViewDataResponse2: ...

