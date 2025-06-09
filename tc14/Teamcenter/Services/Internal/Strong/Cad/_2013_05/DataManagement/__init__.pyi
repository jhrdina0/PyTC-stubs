import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FeatureReturnFilter:
    def __init__(self, ) -> None: ...
    RelationTypes: list[str]
    LevelsForward: int
    LevelsBackward: int
    FeatureTypes: list[str]
    ConfigurationType: str
    ConfigRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    PsNotesWanted: list[str]

class FeatureQueryInfo:
    def __init__(self, ) -> None: ...
    ClientId: str
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ViewType: str
    FeatureReturnFilter: FeatureReturnFilter

class GDEItem:
    def __init__(self, ) -> None: ...
    Gde: Teamcenter.Soa.Client.Model.Strong.GeneralDesignElement
    GdeOccurrence: Teamcenter.Soa.Client.Model.Strong.GDEOccurrence
    PsOccNotes: list[GDEOccNote]
    Apns: list[Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode]
    FeatureForm: Teamcenter.Soa.Client.Model.Strong.Form
    NumberOfGDELinks: int
    GdeLinks: list[Teamcenter.Soa.Client.Model.Strong.GeneralDesignElementLink]

class GDELinkItem:
    def __init__(self, ) -> None: ...
    GdeLink: Teamcenter.Soa.Client.Model.Strong.GeneralDesignElementLink
    GdeLinkOccurrence: Teamcenter.Soa.Client.Model.Strong.GDEOccurrence
    PsOccNotes: list[GDEOccNote]
    Apns: list[Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode]
    FeatureForm: Teamcenter.Soa.Client.Model.Strong.Form
    NumberOfGDEs: int
    Gdes: list[Teamcenter.Soa.Client.Model.Strong.GeneralDesignElement]
    ConnectedTos: list[Teamcenter.Soa.Client.Model.Strong.ImanRelation]

class GDEOccNote:
    def __init__(self, ) -> None: ...
    Name: str
    Value: str

class PartToPartData:
    def __init__(self, ) -> None: ...
    PrimaryRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    SecondaryRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    PartToPartRelation: Teamcenter.Soa.Client.Model.Strong.ImanRelation

class QueryPartRelatedFeaturesResponse:
    def __init__(self, ) -> None: ...
    ClientIdToFeatureMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RevisionData:
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    MasterDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    GdeItems: list[GDEItem]
    GdeLinkItems: list[GDELinkItem]
    PartToPartList: list[PartToPartData]
    EndOfChain: bool
    NumberOfParents: int
    NumberOfChildren: int

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryPartRelatedFeatures(self, FeatureQueryInfo: list[FeatureQueryInfo]) -> QueryPartRelatedFeaturesResponse: ...

