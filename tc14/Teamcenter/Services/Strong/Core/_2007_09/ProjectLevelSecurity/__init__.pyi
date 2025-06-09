import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssignedOrRemovedObjects:
    """
    This structure holds the projects and workspace objects.
    """
    def __init__(self, ) -> None: ...
    Projects: list[Teamcenter.Soa.Client.Model.Strong.TC_Project]
    """
            A list of TC_Project objects  to which the the given set of workspace objects
            need to be assigned or from which the objects need to be removed.
            """
    ObjectToAssign: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that needs to be assigned ( added ) to the given projects."""
    ObjectToRemove: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that needs to be removed  from the given projects."""

class ProjectLevelSecurity:
    """
    Interface ProjectLevelSecurity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AssignOrRemoveObjects(self, AssignedOrRemovedobjects: list[AssignedOrRemovedObjects]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation assigns the given set of workspace objects to the given projects.
             Similarly, it removes an additional set of given workspace objects from the same
             set of given projects. If user is not privileged to assign objects to any of the
             given projects then this operation will return the error 101014 : You have insufficient
             privilege to assign object to a project. Similarly, if user is not privileged to
             remove objects from any of the given projects then this operation will return error
             101015: You have insufficient privilege to remove object from a project.  These errors
             will not terminate processing of rest of the objects.
             

Teamcenter Component:

             Project Level Security Administration - Provide a mechanism for organizing data and
             implementing access control based on project membership. Data assigned to projects
             can be searched for and viewed in the context of the project and can be distributed
             across multiple sites.
             
        :param AssignedOrRemovedobjects: 
                         A list of AssignedOrRemovedObjects.
             
        :return: Are returned.
        """
        ...

