import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetAttributeValuesInputData:
    def __init__(self, ) -> None: ...
    ClassName: str
    AttributeName: str

class GetAttributeValuesOutputData:
    def __init__(self, ) -> None: ...
    ClassAttribute: GetAttributeValuesInputData
    Values: list[str]

class GetAttributeValuesResponse:
    def __init__(self, ) -> None: ...
    Output: list[GetAttributeValuesOutputData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GetOrganizationInformationInputData:
    def __init__(self, ) -> None: ...
    GroupName: str
    OnlyFirstLevelSubGroups: bool
    IncludeRoleInGroupInfo: bool
    IncludeUsersInGroupRoleInfo: bool

class GetOrganizationInformationResponse:
    def __init__(self, ) -> None: ...
    HierDataMap: System.Collections.Hashtable
    RootLevelGroups: list[GroupHierarchyData]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GroupHierarchyData:
    def __init__(self, ) -> None: ...
    Group: Teamcenter.Soa.Client.Model.Strong.Group
    SubGroups: list[Teamcenter.Soa.Client.Model.Strong.Group]
    Parent: Teamcenter.Soa.Client.Model.Strong.Group
    RoleUsers: list[RoleUsers]

class RoleUsers:
    def __init__(self, ) -> None: ...
    Role: Teamcenter.Soa.Client.Model.Strong.Role
    Users: list[Teamcenter.Soa.Client.Model.Strong.User]

class DataManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAttributeValues(self, ClassAttributeValues: list[GetAttributeValuesInputData]) -> GetAttributeValuesResponse: ...
    def GetOrganizationInformation(self, Options: list[GetOrganizationInformationInputData]) -> GetOrganizationInformationResponse: ...

