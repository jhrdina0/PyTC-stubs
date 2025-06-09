import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ChangeOwningProgramInput2:
    """
    Contains data used for changing the owning program for the  given set of objects.
    """
    def __init__(self, ) -> None: ...
    OwningProgram: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The project (TC_Project) to set as the Owning Program of the target objects."""
    InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of WorkspaceObject for which the Owning Program is to be changed."""

class UserGroupRoleInfo:
    """
    
            The UserGroupRoleInfo structure contains the user, the group, and the role. The group
            and the role are optional.
            
    """
    def __init__(self, ) -> None: ...
    TcUser: Teamcenter.Soa.Client.Model.Strong.User
    """The User object."""
    TcGroup: Teamcenter.Soa.Client.Model.Strong.Group
    """The Group object."""
    TcRole: Teamcenter.Soa.Client.Model.Strong.Role
    """The Role object."""

class UserProjects:
    """
    
            The structure which holds the TC_Project objects for the associated
            UserGroupRoleInfo structure
            
    """
    def __init__(self, ) -> None: ...
    UserGroupRole: UserGroupRoleInfo
    """The UserGroupRoleInfo structure."""
    Projects: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """The TC_Project objects that's associated with the UserGroupRoleInfo."""

class UserProjectsResponse:
    """
    
            The structure which holds the ServiceData and all the TC_Project objects
            that are associated with the given UserGroupRoleInfo

    """
    def __init__(self, ) -> None: ...
    UserProjectList: list[UserProjects]
    """A list of UserProjects structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class ProjectLevelSecurity:
    """
    Interface ProjectLevelSecurity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ChangeOwningProgram(self, ChgOwnProgramInput: list[ChangeOwningProgramInput2]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation changes the owning program of the given set of objects. Owning Program
             (owning_project attribute ) is changed to the new value passed in.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ChgOwnProgramInput: 
                         The list of ChangeOwningProgramInput2 structure.
             
        :return: 
        """
        ...
    def GetUserProjects2(self, UserInfoList: list[UserGroupRoleInfo], ActiveProjectsOnly: bool, VisibleProjectsOnly: bool, PrivilegedProjectsOnly: bool, ProgramsOnly: bool, ProgramsAndTheChildProjects: bool) -> UserProjectsResponse: ...

