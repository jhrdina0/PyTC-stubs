import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddRolesToGroupStructure:
    """
    Roles to be added to a Group object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    RolesToAdd: list[Teamcenter.Soa.Client.Model.Strong.Role]
    """A list of Role objects to be added to the Group."""
    RolesToCreateAndAdd: list[RoleStructure]
    """
            A list of Role properties. A new Role will be created for each RoleStructure
            in the list and added to the Group.
            """
    Grp: Teamcenter.Soa.Client.Model.Strong.Group
    """Group for the roles to be added to."""

class RoleGroupStructure:
    """
    A structure of Role objects and the associated Group object.
    """
    def __init__(self, ) -> None: ...
    Roles: list[Teamcenter.Soa.Client.Model.Strong.Role]
    """A list of Role objects to be removed."""
    Grp: Teamcenter.Soa.Client.Model.Strong.Group
    """The Group object from which Role objects are to be removed."""

class RoleStructure:
    """
    Properties for the new Role to be created and added to the Group.
    """
    def __init__(self, ) -> None: ...
    RoleName: str
    """Name of the Role to be created."""
    RoleDescription: str
    """The Role description."""

class RoleManagement:
    """
    Interface RoleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddRolesToGroup(self, RoleGroupStructs: list[AddRolesToGroupStructure]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Adds new Roles and existing Roles to the specified Group objects. If the roles
             are new, it will create them first before they are added.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param RoleGroupStructs: 
                         A list of structures of <b>Role</b> object to be created and/or to be added to a
                         <b>Group</b> object.
             
        :return: 10182: The role name is used by another role.
        """
        ...
    def RemoveRolesFromGroup(self, RoleGroupStructs: list[RoleGroupStructure]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

