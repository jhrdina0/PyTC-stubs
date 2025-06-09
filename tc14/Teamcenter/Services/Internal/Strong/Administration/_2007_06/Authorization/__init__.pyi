import System
import Teamcenter.Soa.Client.Model
import typing

class AccessorAccessibleNamesList:
    def __init__(self, ) -> None: ...
    Output: list[AccessorAccessibleNamesResponse]
    PartialErrors: Teamcenter.Soa.Client.Model.ServiceData

class AccessorAccessibleNamesResponse:
    def __init__(self, ) -> None: ...
    AccessorTag: Teamcenter.Soa.Client.Model.ModelObject
    RuleDomain: str
    AccessibleNames: list[str]

class AccessorInfo:
    def __init__(self, ) -> None: ...
    AccessorTag: Teamcenter.Soa.Client.Model.ModelObject
    RuleDomain: str

class AuthorizationInfo:
    def __init__(self, ) -> None: ...
    AccessorTag: Teamcenter.Soa.Client.Model.ModelObject
    RuleDomain: str
    Names: list[str]

class Authorization:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAuthorization(self, InputAccessors: list[AccessorInfo]) -> AccessorAccessibleNamesList: ...
    def SetAuthorization(self, InputAuthorization: list[AuthorizationInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

