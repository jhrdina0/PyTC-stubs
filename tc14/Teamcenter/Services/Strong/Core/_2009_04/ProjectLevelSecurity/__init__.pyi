import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class LoadProjectDataForUserResponse:
    """
    Object that holds applicable projects.
    """
    def __init__(self, ) -> None: ...
    ApplicableProjects: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """List of TC_project objects found."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """A  standard  ServicData."""

class ProjectLevelSecurity:
    """
    Interface ProjectLevelSecurity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def LoadProjectDataForUser(self, User: Teamcenter.Soa.Client.Model.Strong.User, Group: Teamcenter.Soa.Client.Model.Strong.Group, Role: Teamcenter.Soa.Client.Model.Strong.Role) -> LoadProjectDataForUserResponse:
        """    
             This operation returns list of projects for a given user, group and role combination.
             If no group and role is specified it obtains all the projects for the specified user.
             If any of the arguments passed are invalid an error is returned by the operation
             added as a partial error.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param User: 
                         The <b>User</b> object.
             
        :param Group: 
                         The <b>Group</b> object in which the user belongs to.
             
        :param Role: 
                         The <b>Role</b> object in which the user belongs to.
             
        :return: This operation returns a LoadProjectDataForUserResponse structure. Any error that
             occurred while finding the projects for the given arguments is added to the sandard
             ServiceData object.
        """
        ...

