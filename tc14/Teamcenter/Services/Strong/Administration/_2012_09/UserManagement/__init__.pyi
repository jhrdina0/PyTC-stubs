import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetUserGroupMembersInputData:
    """
    
            This structure holds the input data to retrieve the group member information of a
            given user.
            
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The given user object."""
    IncludeInactive: bool
    """The option flag to include inactive group memers in returned group members data."""
    IncludeUser: bool
    """The option flag to include User objects in returned group member data."""
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """

class GetUserGroupMembersOutput:
    """
    This structure holds all user group member data for a given user.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Unmodified value from the GetUserGroupMembersInputData.clientId. This can be used
            by the caller to indentify this data structure with the source input data.
            """
    Memebrs: list[UserGroupMemberData]
    """All user group member data for a specific user."""

class GetUserGroupMembersResponse:
    """
    A list of user group members outputs, one for each of the given User object.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[GetUserGroupMembersOutput]
    """List of group member information, one for each User object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The object which holds the partial errors that occurred during retrieving user group
            member data.
            """

class GroupMemberInput:
    """
    
            This structure holds a GroupMember object, whose properties need to be updated and
            a map of property names and their corresponding values.
            
    """
    def __init__(self, ) -> None: ...
    GroupMember: Teamcenter.Soa.Client.Model.Strong.GroupMember
    """The GroupMember business object whose propeties  need to be updated."""
    GroupMemberPropValuesMap: System.Collections.Hashtable
    """A map of  property names and desired value(string/string)."""

class RoleUser:
    """
    
            This structure holds role, user, group member status, default role flag and group
            admin privilege for a group member.
            
    """
    def __init__(self, ) -> None: ...
    Role: Teamcenter.Soa.Client.Model.Strong.Role
    """The Role of a group member."""
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The User of a group member."""
    IsActive: bool
    """True if the group member is active."""
    IsDefaultRole: bool
    """True if the this Role is the default in the group member."""
    IsGroupAdmin: bool
    """True if the group member has administrative privilege"""

class UserGroupMemberData:
    """
    This structure holds the all group member data under a group for the given user.
    """
    def __init__(self, ) -> None: ...
    Group: Teamcenter.Soa.Client.Model.Strong.Group
    """The group of the group members in the RoleUser list."""
    RoleUsers: list[RoleUser]
    """The list of RoleUser objects which belong to the same group."""

class UserManagement:
    """
    Interface UserManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetUserGroupMembers(self, InputObjects: list[GetUserGroupMembersInputData]) -> GetUserGroupMembersResponse:
        """    
             This operation retrieves information of all group members for a list of users specified
             in the list of GetUserGroupMembersInputData inputs. The information includes Group
             object, Role object, User object, status, group admin privilege, and default role
             flag of the user group members. The returned results could contain information only
             for the active group members of the user or both active and inactive group members
             of the user depending on option includeInactive setting in GetUserGroupMembersInputData.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param InputObjects: 
                         A list of GetUserGroupMembersInputData objects. Each GetUserGroupMembersInputData
                         specifies the specified matching User object and option flag to include inactive
                         group members.
             
        :return: A list of group member information for each requested User object. The following
             partial errors may be returned. - 10214 The source User object is null. - 10034 Fails
             to get  group members for a given user.
        """
        ...
    def SetGroupMemberProperties(self, InputObjects: list[GroupMemberInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates the properties on one or more GroupMembers.The following properties
             may be updated: membership_data_source, ga,default_role, status.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param InputObjects: 
                         A list of GroupMember objects and the desired property values.
             
        :return: The modified GroupMember objects are returned in the Updated list of the ServiceData.
        """
        ...

