import System
import System.Collections
import Teamcenter.Services.Strong.Core._2018_11.ProjectLevelSecurity
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddOrRemoveProjectMemberInput:
    """
    The structure holds the TC_Project object and the nodes to add or remove.
    """
    def __init__(self, ) -> None: ...
    Project: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object which the members are added or removed."""
    Gms: list[Teamcenter.Soa.Client.Model.Strong.GroupMember]
    """The GroupMember objects to be added or removed."""
    Groups: list[Teamcenter.Soa.Client.Model.Strong.Group]
    """The Group objects to be added or removed."""
    GroupRoles: list[GroupRoleNode]
    """
            The GroupRole nodes to have the GroupMember objects under it added
            to or removed from the Project Team.
            """
    AddOrRemove: bool
    """
            Indicates if the members need to be added or removed from the TC_Project.
            If true, the members in the input are added to the project. If false,
            the members in the input are removed from the project.
            """

class ChildStructureResponse:
    """
    The structure to hold the children of a specific node in ProjectTeam.
    """
    def __init__(self, ) -> None: ...
    ChildGroups: list[GroupNodeWithChildren]
    """The child Groups."""
    ChildRoles: list[GroupRoleNodeWithChildren]
    """The child Roles."""
    ChildGroupMembers: list[GroupMemberPrivilege]
    """The child GroupMembers."""
    ChildGroupMap: System.Collections.Hashtable
    """Map the Group objects to their child Groups."""
    Sd: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class GroupMemberPrivilege:
    """
    
            The structure holds the GroupMember object and its privilege in the ProjectTeam
            of the input TC_Project.
            
    """
    def __init__(self, ) -> None: ...
    Groupmember: Teamcenter.Soa.Client.Model.Strong.GroupMember
    """The GroupMember object"""
    Privilege: int
    """
            The privilege status of the GroupMember in the ProjectTeam of the input
            TC_Project.
            
            0 = regular member
            
            1 = privileged member
            
            2 = project team administrator
            
            3 = project administrator
            """
    IsRemovable: bool
    """
            Indicates if the GroupMember is removable from the ProjectTeam. If
            true, it indicates the GroupMember is directly in the ProjectTeam,
            and it is removable from the ProjectTeam. If false, it indicates the GroupMember
            is under a Group in the ProjectTeam, and it is not removable from the
            ProjectTeam.
            """

class GroupNode:
    """
    
            The view model for Group, which contains the Group object itself and
            a flag to indicate if the Group is removable from the ProjectTeam.
            
    """
    def __init__(self, ) -> None: ...
    TcGroup: Teamcenter.Soa.Client.Model.Strong.Group
    """The Group node view model"""
    IsRemovable: bool
    """
            If true, the Group is directly in the ProjectTeam and is removable.
            If false, the Group is a child of another Group and is not removable.
            """

class GroupNodeWithChildren:
    """
    The structure of a Group node with its child nodes.
    """
    def __init__(self, ) -> None: ...
    GroupNode: GroupNode
    """The GroupNode."""
    ChildGroups: list[GroupNode]
    """The child Groups."""
    ChildRoles: list[GroupRoleNodeWithChildren]
    """The Roles under the Group."""

class GroupRoleNode:
    """
    
            The view model of a Role object, which contains the Role object it
            self, the Group object it is associated with, and a flag indicating if it
            is removable from the Project Team.
            
    """
    def __init__(self, ) -> None: ...
    TcGroup: Teamcenter.Soa.Client.Model.Strong.Group
    """The Group."""
    TcRole: Teamcenter.Soa.Client.Model.Strong.Role
    """The Role."""
    IsRemovable: bool
    """
            For the first level GroupRoleNode structures, they are removable because these
            are the parent node for the GroupMembers that are directly in the project
            members. Hence the values are true. For the GroupRoleNode structures under
            the Group objects in the ProjectTeam, the values are false.
            """

class GroupRoleNodeWithChildren:
    """
    
            The structure which holds the first level node (Group.Role) and the GroupMember
            objects along with their privilege in the Project Team.
            
    """
    def __init__(self, ) -> None: ...
    GroupRole: GroupRoleNode
    """The first level Group.Role node."""
    GroupmemberList: list[GroupMemberPrivilege]
    """
            The GroupMember objects that are in the Project Team with the same
            Group and Role, along with their privilege.
            """

class ProjectAndPrivilege:
    """
    The structure to hold the TC_Project object and the privilege of the user.
    """
    def __init__(self, ) -> None: ...
    Project: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object retrieved from DB."""
    Privilege: int
    """
            The User's privilege in the associated TC_Project.
            

-1 = User is not a member of the project (possible
            when having bypass for DBA users).
            
 0 = User is a regular member of the project.
            
 1 = User is a project author of the project.
            
 2 = User is a project team administrator of the project.
            
 3 = User is the owning user of the project.
            

"""

class ProjectPrivilegeResponse:
    """
    
            This structure contains a list of ProjectAndPrivilege structure that has privilege
            of the login user in each TC_Project object, and the Service Data.
            
    """
    def __init__(self, ) -> None: ...
    ProjectPrivilege: list[ProjectAndPrivilege]
    """A list of TC_Project objects and the privileges of the login user in them."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class ProjectTeamPagedInput:
    """
    
            The paginated input to get the ProjectTeam for the given TC_Project
            object.
            
    """
    def __init__(self, ) -> None: ...
    Project: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object to get the ProjectTeam."""
    StartIndex: int
    """The start index"""
    PageSize: int
    """The page size"""
    QuickLoad: bool
    """
            If true, to retrieve the ProjectTeam data from the server memory. If false,
            the data is retrieved from the database.
            """

class ProjectTeamPagedResponse:
    """
    
            The structure holds the paginated first level nodes of ProjectTeam, starting
            with Group objects.
            
    """
    def __init__(self, ) -> None: ...
    TotalMemberCount: int
    """
            The total number of the project members in the ProjectTeam of the given TC_Project
            object.
            """
    EndIndex: int
    """The index of the last element returned for pagination."""
    Groups: list[GroupNode]
    """A list of Group objects that are in the project members of the input TC_Project."""
    StructuredGroupMembers: list[GroupRoleNode]
    """
            A list of structured GroupRoleNode which represents the first level node of
            the GroupMember objects in the ProjectTeam.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class SetPrivilegeForUserInput:
    """
    The input structure for setUserPrivilege operation
    """
    def __init__(self, ) -> None: ...
    Project: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object which the User privilege needs to be set."""
    Users: list[Teamcenter.Soa.Client.Model.Strong.User]
    """The User objects to set privilege."""
    GroupNode: list[GroupNode]
    """
            The Group node to set privilege on all the User objects under it. The
            privilege will be set for all the User objects under this Group, including
            subgroups.
            """
    GroupRoleNode: list[GroupRoleNode]
    """
            The GroupRole node to set privilege on all the User objects under it.
            The privilege will be set on all the User objects under this GroupRole
            node
            """
    PrivilegeStatus: int
    """

0 = regular member (non-privileged member)
            
1 = project author (privileged member)
            
2 = project team administrator
            

"""

class UserProjectsAndPrivilege:
    """
    
            The structure holds the User and the TC_Project objects that are associated
            with this User, along with the User's privilege status in each TC_Project.
            
    """
    def __init__(self, ) -> None: ...
    UserGroupRole: Teamcenter.Services.Strong.Core._2018_11.ProjectLevelSecurity.UserGroupRoleInfo
    """
            The given User or the given User with specific Group and Role
            that the TC_Project objects are associated with.
            """
    TotalProjectCount: int
    """The total number of TC_Project associtated with the User."""
    EndIndex: int
    """The end index of the paged response."""
    Projects: list[ProjectAndPrivilege]
    """
            All the TC_Project objects that are associated with the given User,
            along with the privilege status of the User.
            """

class UserProjectsAndPrivilegeResponse:
    """
    
            The structure holds the User objects, the associated TC_Project objects,
            and their privilege status in each TC_Project objects.
            
    """
    def __init__(self, ) -> None: ...
    UserProjects: list[UserProjectsAndPrivilege]
    """
            The Users and their associated TC_Projects, along with the privilege
            status of each User.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class ProjectLevelSecurity:
    """
    Interface ProjectLevelSecurity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddOrRemoveProjectMembers(self, Inputs: list[AddOrRemoveProjectMemberInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Adds or removes GroupMember objects or Group objects to/from the ProjectTeam
             of the given TC_Project.
             

Use Cases:

             Use Case 1: The login user selects a TC_Project and adds some Group
             or GroupMember objects to the ProjectTeam.
             
             Use Case 2: The login user selects a TC_Project and removes some Group
             or GroupMember objects from the ProjectTeam.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Inputs: 
                         A list of <b>AddOrRemoveProjectMemberInput</b> structures which consists of the <b>TC_Project</b>
                         object to add or remove, a flag that indicates to add or to remove, and lists of
                         nodes to be added or removed.
             
        :return: 
        """
        ...
    def GetFirstLevelProjectTeamStructure(self, Input: ProjectTeamPagedInput) -> ProjectTeamPagedResponse:
        """    
             This operations returns the paginated output of the first level nodes of the ProjectTeam
             for the given TC_Project object.
             

Use Cases:

             Select a TC_Project object to display all first level nodes in the ProjectTeam
             tree.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Input: 
                         The <b>TC_Project</b> and the pagination configuration to return <b>ProjectTeam</b>
                         first level nodes and configuration input to load <b>ProjectTeam</b> from server
                         cache.
             
        :return: members with their privilege status.
        """
        ...
    def GetModifiableProjects(self, StartIndex: int, PageSize: int) -> UserProjectsAndPrivilegeResponse:
        """    
             This operation returns the TC_Project objects that the login user can modify.
             The TC_Project objects in the response are based on the pagination input.
             

Use Cases:

             A User loads all modifiable project.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param StartIndex: 
                         The start index for pagination.
             
        :param PageSize: 
                         The size of a page.
             
        :return: objects that are modifiable.
        """
        ...
    def SetUserPrivilege(self, Inputs: list[SetPrivilegeForUserInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set the privilege of the given User objects in ProjectTeam of the given
             TC_Project.
             

Use Cases:

             This service allows the project team administrator to achieve the following use cases.
             

             Use Case 1: The project team administrator sets a list of User objects to
             be non-privileged in the ProjectTeam of a TC_Project.
             
             Use Case 2: The project team administrator sets a list of User objects to
             be privileged in the ProjectTeam of a TC_Project.
             
             Use Case 3: The project team administrator sets a list of User objects to
             be project team administrator in the ProjectTeam of a TC_Project.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Inputs: 
                         A list of <b>SetPrivilegeForUserInput</b> structures. The structure holds the <b>TC_Project</b>,
                         a list of <b>User</b> objects, a list of <b>Group</b> nodes, and a list of <b>GroupRole</b>
                         nodes which the privileges to be set, as well as the type of privilege to set.
             
        :return: 
        """
        ...
    def GetPrivilegeInProjects(self, Projects: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]) -> ProjectPrivilegeResponse:
        """    
             This operation returns the privilege of the current user in each TC_Project
             object in the input.
             

Use Cases:

             When the login user checks the privilege in a list of TC_Project objects,
             the operation returns the privilege value of the login user of each project.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Projects: 
                         A list of <b>TC_Project</b> objects to check the current user's privilege.
             
        :return: 
        """
        ...
    def GetProjectTeamChildNodes(self, Project: Teamcenter.Soa.Client.Model.Strong.TC_Project, Node: GroupRoleNode, Depth: int) -> ChildStructureResponse:
        """    
             The operation returns child nodes for the given Group node or a Role
             node in the ProjectTeam tree based on the given depth.
             

Use Cases:

             Expanding a Group or a Role node in a Project Team tree, the
             child nodes are returned.
             

Dependencies:

             getFirstLevelProjectTeamStructure
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param Project: 
                         The <b>TC_Project</b> object which associated with the <b>ProjectTeam</b> to load
                         child nodes.
             
        :param Node: 
                         If the <i>isRemovable</i> field is true, and <i>tcRole</i> is not NULL or empty,
                         then load the direct members in the <b>ProjectTeam</b> that is associated with the
                         given <b>GroupRole</b>.
             
        :param Depth: 
                         The depth of the tree to load children.
             
        :return: .
        """
        ...

