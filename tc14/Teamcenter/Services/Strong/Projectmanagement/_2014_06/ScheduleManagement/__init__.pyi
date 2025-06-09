import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FilterCriteria:
    """
    The filter criteria for retrieving the list of matching Users.
    """
    def __init__(self, ) -> None: ...
    Disciplines: list[Teamcenter.Soa.Client.Model.Strong.Discipline]
    """A list of Discipline object for which User needs to be filtered."""
    Grouprole: list[Teamcenter.Soa.Client.Model.Strong.ResourcePool]
    """
            A list of ResourcePool objects from which the Group and Role
            information is taken for filtering the User.
            """
    Qualifications: list[QualificationInfo]
    """
            List of  criteria specifying detailed information of the Fnd0Qualification
            assignments for which the user needs to be filtered.
            """

class FilteredUser:
    """
    
Individual User objects which match the input filter criteria of Discipline,
Group, Role and Fnd0Qualification.
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The User matching the filter criteria."""
    Discipline: Teamcenter.Soa.Client.Model.Strong.Discipline
    """The Discipline that the user is a part of."""
    GroupRole: Teamcenter.Soa.Client.Model.Strong.ResourcePool
    """The Group/Role that the user is a part of."""
    QualificationRel: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    """The Fnd0Qualification which is assigned to the User."""

class FilteredUsersInfo:
    """
    
The structure which contains list of User objects which match the input filter
criteria
of Discipline, Group, Role and Fnd0Qualification. If
there are no User objects found which match the input filter criteria, an empty
response
is returned.
    """
    def __init__(self, ) -> None: ...
    Filtereduserinfo: list[FilteredUser]
    """A list containing information about the filtered Users."""
    Servicedata: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data"""

class QualificationInfo:
    """
    
List of  criteria specifying detailed information of the Fnd0Qualification
assignments for which the user needs to be filtered

    """
    def __init__(self, ) -> None: ...
    Qualification: Teamcenter.Soa.Client.Model.Strong.Fnd0Qualification
    """The Fnd0Qualification object for which User needs to be filtered."""
    Level: str
    """
            Level of Fnd0Qualification at which Users needs to be filtered.Level
            is defined on Fnd0Qualification object by the Administrator who creates the
            Fnd0Qualification objects.
            
            (for example "Advanced" , "Beginner").
            
"""
    IsfindAlternates: bool
    """
            If true the operation returns all the Users who are on the same level as specified
            in the input and also the Users who are on a higher level than the level specified
            in the input.
            
            If false the operation returns only the Users who are on the exact level as
            specified in the input.
            
"""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FilterUsers(self, Filteringcriteria: FilterCriteria) -> FilteredUsersInfo:
        """    
             In Schedule Manager, Discipline, Group, Role and Fnd0Qualification
             can be assigned to the ScheduleTask as placeholder assignments. These placeholder
             assignments can then be assigned to specific users who are a part of the placeholder
             assignment.
             

             The operation returns a list of Users which match the input filter criteria of Discipline,
             Group, Role and Fnd0Qualification.
             


Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Filteringcriteria: 
                         The filter criteria for retrieving the list of matching <b>Users</b>.
             
        :return: 
        """
        ...

