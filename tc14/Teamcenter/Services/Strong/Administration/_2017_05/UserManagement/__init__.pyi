import System
import Teamcenter.Services.Strong.Administration._2015_07.UserManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddUsersAsGroupMembersStructure:
    """
    
            A structure of User object and the associated Role and Group
            objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Identifier that helps the client to track the object(s) created and modified, required;
            should be unique for the input set.
            """
    UsersToAdd: list[ExistingUserDetailsForGroupMember]
    """A list of existing users to be added to the Group with specified Role."""
    UsersToCreateAndAdd: list[NewUserDetailsForGroupMember]
    """A list of users to be created and added to the Group with specified Role."""
    Grp: Teamcenter.Soa.Client.Model.Strong.Group
    """Group for the group members."""
    Role: Teamcenter.Soa.Client.Model.Strong.Role
    """The Role for the group members."""

class UserAttributesStructure:
    """
    A structure of User attributes.
    """
    def __init__(self, ) -> None: ...
    IsGroupAdmin: bool
    """
            If true, user will be the group administrator; otherwise, user will not be the group
            administrator.
            """
    Status: bool
    """If true, user will be active GroupMember; otherwise, user will not be active GroupMember."""
    IsDefaultRole: bool
    """
            If true, the given role will be the default role for the user; otherwise the given
            role will not be the default role for the user.
            """

class ExistingUserDetailsForGroupMember:
    """
    A structure of User object and its attributes.
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """
            Existing User to be added. This User will be added to the Group
            with the specified Role.
            """
    UserAttributes: UserAttributesStructure
    """List of userAttributes associated with each User."""

class NewUserDetailsForGroupMember:
    """
    A structure of new User to be created with its attributes.
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Services.Strong.Administration._2015_07.UserManagement.CreateOrUpdateUserInputs
    """
            A list of User properties . Using these properties a new User will
            be created and added to the Group with specified Role.
            """
    UserAttributes: UserAttributesStructure
    """Additional GroupMember proeprties for the new User."""

class UserManagementResponse:
    """
    
            This structure holds a structure of User and associated Role and Group
            objects along with ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    UserRoleGrpStructs: list[UserRoleGroupStructure]
    """A list of structures of User and associated Role and Group objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data with the partial error information."""

class UserRoleGroupStructure:
    """
    A structure of User and associated Role and Group objects.
    """
    def __init__(self, ) -> None: ...
    Users: list[Teamcenter.Soa.Client.Model.Strong.User]
    """A list of User objects to be removed from given Group and Role."""
    Grp: Teamcenter.Soa.Client.Model.Strong.Group
    """A Group object from which User is to be removed."""
    Role: Teamcenter.Soa.Client.Model.Strong.Role
    """A Role object from which User is to be removed."""

class UserManagement:
    """
    Interface UserManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddUsersAsGroupMembers(self, UserRoleGroupStructs: list[AddUsersAsGroupMembersStructure]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Adds new Users and existing Users as Group Members under the given Group objects
             with specific Role object. If a User is new, it will be created first
             before it is added as GroupMember. This operation requires system administration
             privilege or Group administration privilege. Specified Role objects must be
             an existing Role in the Group.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param UserRoleGroupStructs: 
                         A list of <b>User</b> objects and their <b>GroupMember</b> roles in the <b>Group</b>.
             
        :return: 10528:  Create user failed - This error is shown when there is a failure creating
             new user due to any internal errors. Administrator will have to look at system log
             in order to find the root cause of the error.
        """
        ...
    def RemoveGroupMembers(self, UserRoleGroupStructs: list[UserRoleGroupStructure]) -> UserManagementResponse:
        """    
             This operation removes group members for specified User objects under given
             Group objects with specified Role objects. This operation requires
             system administration privilege or group administration privilege. Input should not
             have null User, Group and Role objects.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param UserRoleGroupStructs: 
                         List of structures of <b>User</b> and associated <b>Role</b> and <b>Group</b> objects.
             
        :return: ) are NULL.
        """
        ...

