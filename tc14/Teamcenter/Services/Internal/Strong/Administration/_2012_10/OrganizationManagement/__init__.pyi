import System
import System.Collections
import Teamcenter.Services.Internal.Strong.Administration._2011_06.OrganizationManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetOrganizationUserMembersResponse:
    def __init__(self, ) -> None: ...
    GroupElementMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GroupElement:
    def __init__(self, ) -> None: ...
    Group: Teamcenter.Soa.Client.Model.Strong.Group
    Parent: Teamcenter.Soa.Client.Model.Strong.Group
    SubGroups: list[Teamcenter.Soa.Client.Model.Strong.Group]
    Roles: list[Teamcenter.Soa.Client.Model.Strong.Role]
    Members: list[Teamcenter.Services.Internal.Strong.Administration._2011_06.OrganizationManagement.RoleUsers]

class OrganizationMembersInput:
    def __init__(self, ) -> None: ...
    UserID: str
    UserName: str
    GroupName: str
    RoleName: str
    IncludeInactive: bool
    IncludeSubGroups: bool

class OrganizationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetOrganizationGroupMembers(self, Input: OrganizationMembersInput) -> GetOrganizationUserMembersResponse: ...

