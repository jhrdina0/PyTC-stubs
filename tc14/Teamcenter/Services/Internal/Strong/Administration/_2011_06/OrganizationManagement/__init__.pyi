import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetGroupsForRoleInput:
    def __init__(self, ) -> None: ...
    Role: Teamcenter.Soa.Client.Model.Strong.Role
    IncludeOrgTree: bool

class OrganizationTree:
    def __init__(self, ) -> None: ...
    RootLevelGroups: list[GroupStructure]
    GroupStructureMap: System.Collections.Hashtable

class GetOrganizationGroupOutput:
    def __init__(self, ) -> None: ...
    Groups: list[Teamcenter.Soa.Client.Model.Strong.Group]
    OrgTree: OrganizationTree

class GetOrganizationGroupResponse:
    def __init__(self, ) -> None: ...
    Outputs: list[GetOrganizationGroupOutput]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class GroupStructure:
    def __init__(self, ) -> None: ...
    Group: Teamcenter.Soa.Client.Model.Strong.Group
    Parent: Teamcenter.Soa.Client.Model.Strong.Group
    Subgroups: list[Teamcenter.Soa.Client.Model.Strong.Group]
    GroupRoles: list[RoleUsers]

class RoleUsers:
    def __init__(self, ) -> None: ...
    Role: Teamcenter.Soa.Client.Model.Strong.Role
    Members: list[Teamcenter.Soa.Client.Model.Strong.GroupMember]

class OrganizationManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetOrganizationGroups(self, Inputs: list[GetGroupsForRoleInput]) -> GetOrganizationGroupResponse: ...

