import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class RevisionRuleInfo2:
    def __init__(self, ) -> None: ...
    Uid: str
    Name: str
    Description: str
    EntriesInfo: list[RevRuleEntryInfo2]
    NestedEffectivity: bool
    IsPrivate: bool

class CreateOrUpdateRevRuleInput2:
    def __init__(self, ) -> None: ...
    UpdateExisting: bool
    RevisionRuleInfo: RevisionRuleInfo2

class CreateOrUpdateRevRuleResp2:
    def __init__(self, ) -> None: ...
    RevisionRuleInfo: RevisionRuleInfo2
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class RevRuleGroupEntryInfo2:
    def __init__(self, ) -> None: ...
    GroupByTypes: list[str]
    ListOfSubEntries: list[RevRuleEntryInfo2]

class RevRuleEntryInfo2:
    def __init__(self, ) -> None: ...
    EntryType: int
    DisplayText: str
    RevRuleEntryKeyToValue: System.Collections.Hashtable
    GroupEntryInfo: RevRuleGroupEntryInfo2

class RevRuleInfoResponse2:
    def __init__(self, ) -> None: ...
    RevisionRuleInfo: RevisionRuleInfo2

class RevisionRuleAdministration:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateRevisionRule2(self, InputData: CreateOrUpdateRevRuleInput2) -> CreateOrUpdateRevRuleResp2: ...
    def GetRevisionRuleInfo2(self, RevRule: str) -> RevRuleInfoResponse2: ...

