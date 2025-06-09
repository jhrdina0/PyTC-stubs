import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ProjectInfo:
    """
    This structure holds the TC_Project and a flag indicating the user's membership type.
    """
    def __init__(self, ) -> None: ...
    Project: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object."""
    IsUserPrivileged: bool
    """Flag indicating if the given  user is a privleged  member."""

class UserProjectsInfo:
    """
    This structure holds the projects for one of the given users.
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The User object of Teamcenter."""
    ActiveProjectsOnly: bool
    """
            Flag to indicate the status of projects  returned True indicates only active projects
            are returned. False indicates both active and inactive projects are returned.
            """
    PrivilegedProjectsOnly: bool
    """
            Flag to indicate if returned projects  are privleged or not.True indicates projects
            are privileged, false indicates all projects where the user is a member of regardless
            of privilege in the projects.
            """
    ProgramsOnly: bool
    """
            Flag Indicating if user wants to get program only pojects of the user, false indicates
            returning all projects where regardless of status program only  value of TC_Project.
            """
    ClientId: str
    """An id associated with a client."""
    ProjectsInfo: list[ProjectInfo]
    """A list of ProjectInfo structure."""

class UserProjectsInfoInput:
    """
    This structure holds the User object and criteria to find the user projects.
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The User object of Teamcenter."""
    ActiveProjectsOnly: bool
    """
            Flag Indicating if user wants to get active projects or
            
            not.True indicates return only active projects of the user, false indicates return
            both active and inactive projects of the user.
            """
    PrivilegedProjectsOnly: bool
    """
            Flag Indicating if user wants to get privleged projects
            
            or not.True indicates return privileged projects of the user, false indicates return
            all projects where the user is a member of regardless of status.
            """
    ProgramsOnly: bool
    """
            Flag Indicating if user wants to get program only projects of the user, false indicates
            return all projects regardless of status program only.
            """
    ClientId: str
    """An id associated with a client."""

class UserProjectsInfoResponse:
    """
    This structure holds the projects for all the given users.
    """
    def __init__(self, ) -> None: ...
    UserProjectInfos: list[UserProjectsInfo]
    """List of UserProjectsInfo structures one for each given user.."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """A  standard ServiceData."""

class ProjectLevelSecurity:
    """
    Interface ProjectLevelSecurity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetUserProjects(self, UserProjectsInfoInputs: list[UserProjectsInfoInput]) -> UserProjectsInfoResponse:
        """    
             This operation returns the list of  TC_Project objects for each of  the users
             in the input structure based on the additional criteria like active projects only,
             user privileged projects only and programs only. The output for this operation is
             a UserProjectsInfoResponse structure.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param UserProjectsInfoInputs: 
                         A list of UserProjectsInfoInput structures.
             
        :return: This operation returns a UserProjectsInfoResponse structure. Any error that occurred
             while finding the projects for the given user is added to the error list in ServiceData
             object against the user object.
        """
        ...

