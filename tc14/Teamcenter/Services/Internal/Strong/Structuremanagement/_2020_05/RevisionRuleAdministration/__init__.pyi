import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class RevisionRuleInfo:
    def __init__(self, ) -> None: ...
    Uid: str
    Name: str
    Description: str
    EntriesInfo: list[RevRuleEntryInfo]
    NestedEffectivity: bool
    IsPrivate: bool

class CreateOrUpdateRevRuleResp:
    def __init__(self, ) -> None: ...
    RevisionRuleInfo: RevisionRuleInfo
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class CreateUpdateRevRuleInput:
    def __init__(self, ) -> None: ...
    UpdateExisting: bool
    IsPrivate: bool
    RevisionRuleInfo: RevisionRuleInfo

class RevRuleGroupEntryInfo:
    def __init__(self, ) -> None: ...
    GroupByTypes: list[str]
    ListOfSubEntries: list[RevRuleSubEntryInfo]

class RevRuleEntryInfo:
    def __init__(self, ) -> None: ...
    EntryType: int
    DisplayText: str
    RevRuleEntryKeyToValue: System.Collections.Hashtable
    GroupEntryInfo: RevRuleGroupEntryInfo

class RevRuleInfoResponse:
    def __init__(self, ) -> None: ...
    EntriesInfo: list[RevRuleEntryInfo]
    NestedEffectivity: bool
    Description: str

class RevRuleSubEntryInfo:
    def __init__(self, ) -> None: ...
    MapOfSubEntryKeyToValue: System.Collections.Hashtable
    SubEntryType: int
    DisplayText: str

class RevisionRuleAdministration:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateRevisionRule(self, InputData: CreateUpdateRevRuleInput) -> CreateOrUpdateRevRuleResp: ...
    def GetRevisionRuleInfo(self, RevRule: str) -> RevRuleInfoResponse: ...

