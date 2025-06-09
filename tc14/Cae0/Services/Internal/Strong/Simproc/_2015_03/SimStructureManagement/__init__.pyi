import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ParentToChildCompositeStructure:
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.ModelObject
    ChildLines: list[ParentToChildCompositeStructure]
    AttachmentRelation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    IsRelation: bool

class CompositeViewResponse:
    def __init__(self, ) -> None: ...
    CompositeServiceData: Teamcenter.Soa.Client.Model.ServiceData
    CompositeLineNodes: ParentToChildCompositeStructure

class GenerateNodeXMLResponse:
    def __init__(self, ) -> None: ...
    NodeXML: str
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ParentToChildTargetReferenceStructure:
    def __init__(self, ) -> None: ...
    TargetReferenceLine: Teamcenter.Soa.Client.Model.ModelObject
    ChildLines: list[ParentToChildTargetReferenceStructure]
    UnderlyingComponent: Teamcenter.Soa.Client.Model.ModelObject
    IsRelation: bool
    HasMultipleRelations: bool

class TargetReferencesViewDataResponse:
    def __init__(self, ) -> None: ...
    TargetReferencesServiceData: Teamcenter.Soa.Client.Model.ServiceData
    TargetReferencesLineNodes: ParentToChildTargetReferenceStructure

class SimStructureManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateNodeXML(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], Domain: str) -> GenerateNodeXMLResponse: ...
    def GetCompositeLineNodes(self, Component: Teamcenter.Soa.Client.Model.ModelObject, FilterItemType: int, FilterRelationType: list[str], ShowRelatedAnalysisRootOnly: bool, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> CompositeViewResponse: ...
    def GetTargetReferencesLineNodes(self, TargetReferenceLine: Teamcenter.Soa.Client.Model.ModelObject, ModelConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, ProductCurrentLine: Teamcenter.Soa.Client.Model.ModelObject, ProductConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> TargetReferencesViewDataResponse: ...

