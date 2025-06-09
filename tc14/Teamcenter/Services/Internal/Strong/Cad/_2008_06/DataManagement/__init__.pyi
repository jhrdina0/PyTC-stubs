import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2007_01.StructureManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FeatureQueryData:
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    OccNote: Teamcenter.Services.Strong.Cad._2007_01.StructureManagement.OccNote
    FeatureTypes: list[str]
    GdeOccurrence: Teamcenter.Soa.Client.Model.Strong.GDEOccurrence
    GdeBVR: Teamcenter.Soa.Client.Model.Strong.GDEbvr

class FeatureReturnFilter:
    def __init__(self, ) -> None: ...
    ReturnFeatureForms: bool
    RelatedItems: bool
    ReturnGDEs: bool
    ReturnGDELinks: bool
    Recursive: bool
    FeatureTypes: list[str]
    ConfigRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule

class FeatureQueryInfo:
    def __init__(self, ) -> None: ...
    ClientID: str
    FeatureQueryData: FeatureQueryData
    FeatureReturnFilter: FeatureReturnFilter

class GDEItem:
    def __init__(self, ) -> None: ...
    Gde: Teamcenter.Soa.Client.Model.Strong.GeneralDesignElement
    GdeLinks: list[RefedGDELinkItem]
    FeatureForm: Teamcenter.Soa.Client.Model.Strong.Form

class GDELinkItem:
    def __init__(self, ) -> None: ...
    GdeLink: Teamcenter.Soa.Client.Model.Strong.GeneralDesignElementLink
    Gdes: list[RefedGDEItem]
    FeatureForm: Teamcenter.Soa.Client.Model.Strong.Form

class QueryRelatedFeaturesOutput:
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    GdeItems: list[GDEItem]
    GdeLinkItems: list[GDELinkItem]

class QueryRelatedFeaturesResponse:
    def __init__(self, ) -> None: ...
    ReturnQueryRelatedFeature: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RefedGDEItem:
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    Gde: Teamcenter.Soa.Client.Model.Strong.GeneralDesignElement
    FeatureForm: Teamcenter.Soa.Client.Model.Strong.Form
    GdeLinks: list[RefedGDELinkItem]

class RefedGDELinkItem:
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    GdeLink: Teamcenter.Soa.Client.Model.Strong.GeneralDesignElementLink
    FeatureForm: Teamcenter.Soa.Client.Model.Strong.Form
    Gdes: list[RefedGDEItem]

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryRelatedFeatures(self, FeatureQueryInfos: list[FeatureQueryInfo]) -> QueryRelatedFeaturesResponse: ...

