import Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssignmentCreateContainer:
    """
    The information needed to create a new assignment to a task.
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The task to assign the resource."""
    Resource: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The resource (User, Group, Role, Resource Pool) being assigned (or null if discipline
            assignment).
            """
    Discipline: Teamcenter.Soa.Client.Model.Strong.Discipline
    """The discipline of the assignee (if User) or the discipline for the assignment."""
    AssignedPercent: float
    """The percentage effort being assigned (I.E. 50.0 == 50%)"""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AssignResources(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateAssignments: list[AssignmentCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer:
        """    
             Assigns resources to tasks.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule containing the tasks to be assigned.
             
        :param CreateAssignments: 
                         The new assignments to be created.
             
        :return: It returns the created assignments as well as objects affected by the change.
        """
        ...
    def ClaimAssignment(self, Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask, Assignment: Teamcenter.Soa.Client.Model.Strong.ResourceAssignment) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer:
        """    
             Claims an assignment.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Task: 
                         The task containing the assignment.
             
        :param Assignment: 
                         The assignment to claim.
             
        :return: The new assignment and any cascading updates.
        """
        ...

