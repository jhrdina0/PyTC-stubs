import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class ClosureRuleTraversalInput:
    def __init__(self, ) -> None: ...
    TopBOMLine: Teamcenter.Soa.Client.Model.ModelObject
    ClosureRuleName: str

class ClosureRuleTraversalResponse:
    def __init__(self, ) -> None: ...
    TraversalInfo: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class TraversedSecondaryObjectInfo:
    def __init__(self, ) -> None: ...
    SecondaryObjectType: str
    ImanRelationType: str
    ImanRelationDescription: str
    IsSecondaryIncluded: bool
    IsSecondaryEditable: bool
    IsPrimaryIncluded: bool
    IsPrimaryEditable: bool

class ClosureRuleEditor:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetClosureRuleTraversalInfo(self, Input: ClosureRuleTraversalInput) -> ClosureRuleTraversalResponse: ...
    def SetClosureRuleTraversalInfo(self, UpdatedTraversalInfo: System.Collections.Hashtable, ClosureRuleName: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...

