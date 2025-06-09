import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ProjectInformation:
    """
    Structure that holds the information required to create the destination project.
    """
    def __init__(self, ) -> None: ...
    ProjectId: str
    """The project ID of  the project  to be created."""
    ProjectName: str
    """The name of the project to be created."""
    ProjectDescription: str
    """The description of the project to be created."""
    UseProgramContext: bool
    """The value of useProgramContext attribute on TC_Project."""
    Active: bool
    """The value of active attribute on TC_Project."""
    Visible: bool
    """The value of visible attribute on TC_Project."""
    TeamMembers: list[TeamMemberInfo]
    """A list of TeamMemberInfo structures."""
    ClientId: str
    """Unique identifier used by the client to track any errors."""

class CopyProjectsInfo:
    """
    
            Structure that holds project information required to create a new TC_Project object
            using this operation.
            
    """
    def __init__(self, ) -> None: ...
    SourceProject: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project of  a project  to be copied."""
    ProjectInfo: ProjectInformation
    """A ProjectInformation structure containing the destination project details.."""
    ClientId: str
    """Unique identifier used by the client to track any errors."""

class ModifyProjectsInfo:
    """
    
            This structure holds the TC_Project object and the information required to
            modify the project.
            
    """
    def __init__(self, ) -> None: ...
    SourceProject: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object  to be modified."""
    ProjectInfo: ProjectInformation
    """A ProjectInformation structure."""
    ClientId: str
    """Unique identifier for the client to track any errors."""

class ProjectClientId:
    """
    This structure holds TC_Project object and corresponding client id.
    """
    def __init__(self, ) -> None: ...
    TcProject: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object whose team members need to be retrieved."""
    ClientId: str
    """Unique identifier used by the client to track any errors."""

class ProjectOpsOutput:
    """
    Structure that holds the TC_Project object.
    """
    def __init__(self, ) -> None: ...
    Project: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The created TC_Project object."""
    ClientId: str
    """Unique identifier used by the client to track any errors."""

class ProjectOpsResponse:
    """
    Response from the project create, modify operations.
    """
    def __init__(self, ) -> None: ...
    ProjectOpsOutputs: list[ProjectOpsOutput]
    """Vector of ProjectOpsOuput objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data with the partial error information"""

class ProjectTeamData:
    """
    This structure holds team member information for a single project.
    """
    def __init__(self, ) -> None: ...
    Project: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """The TC_Project object for which team members are obtained."""
    RegularMembers: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of non privileged members of the given project."""
    ProjectTeamAdmins: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A  list of project team adminstrators of the given project."""
    PrivMembers: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of privileged members of the given project."""

class ProjectTeamsResponse:
    """
    This structure holds team member information for all the given projects.
    """
    def __init__(self, ) -> None: ...
    ProjectTeams: list[ProjectTeamData]
    """List of ProjectTeamData objects one for each of the given projects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """A standard ServiceData object."""

class TeamMemberInfo:
    """
    A structure containing team member information.
    """
    def __init__(self, ) -> None: ...
    TeamMember: Teamcenter.Soa.Client.Model.ModelObject
    """The team member of a project."""
    TeamMemberType: int
    """
            A value indicating the teamMember type. Valid values are 0, 1 and 2.
            
            0 = Team member (teamMember is a GroupMember or Group object)
            
            1 = Privileged user (teamMember is a User object)
            
            2 = Team administrator (teamMember is a User object)
            """

class ProjectLevelSecurity:
    """
    Interface ProjectLevelSecurity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CopyProjects(self, CopyProjectsInfos: list[CopyProjectsInfo]) -> ProjectOpsResponse:
        """    
             This operation copies  the given list of TC_Project objects. The operation
             also copies any information which is in contained in the project. Data such as project
             team members and any objects assigned to the source project will also be copied to
             the new project. If a project with given project ID exists in the system then this
             operation will return error 101010.  The operation will continue with copying the
             other projects.
             


Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param CopyProjectsInfos: 
                         A list of CopyProjectsInfo structures.
             
        :return: This operation returns a ProjectOpsOutput structure.
        """
        ...
    def CreateProjects(self, ProjectInfos: list[ProjectInformation]) -> ProjectOpsResponse:
        """    
             This operation creates TC_Project objects using the given input information.
             If the project with given project ID exists in the system then this operation will
             return unique id violation error 101010.  However, creation of rest of the projects
             will continue.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ProjectInfos: 
                         A list of ProjectInformation objects.
             
        :return: This operation returns a ProjectOpsOutput structure.
        """
        ...
    def GetProjectTeams(self, ProjectObjs: list[ProjectClientId]) -> ProjectTeamsResponse:
        """    
             This operation returns team members for the given list of TC_Project objects.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ProjectObjs: 
                         A list of ProjectClientId structures one for each of the given projects.
             
        :return: This operation returns a ProjectTeamsResponse structure. Any partial errors that
             occur while getting the team for any given project will be returned in the error
             list in ServiceData against the unique client id given as input.
        """
        ...
    def ModifyProjects(self, ModifyProjectsInfos: list[ModifyProjectsInfo]) -> ProjectOpsResponse:
        """    
             This operation modifies the given list of TC_Project objects using the input
             specified. The input contains new values for all the project properties. Values for
             properties other than the project team are ignored unless the user is the Project
             Administrator.
             

             The entire Project Team, with the exception of the Project Administrator, is replaced
             with the specified team. Therefore, a Project Team Administrator must be specified.
             If the new Project Team is different than the current team, the user performing this
             operation must be either the Project Administrator or Project Team Administrator
             for the project being modified.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param ModifyProjectsInfos: 
                         Vector of ModifyProjectsInfo structures.
             
        :return: 
        """
        ...

