import System
import Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssignmentCreateContainer:
    """
    AssignResource SOA
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """ScheduleTask."""
    Resource: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Resource."""
    Discipline: Teamcenter.Soa.Client.Model.Strong.Discipline
    """Discipline."""
    AssignedPercent: float
    """Percent"""
    PlaceholderAssignment: Teamcenter.Soa.Client.Model.Strong.ResourcePool
    """PlaceHolder assignment."""
    IsPlaceHolder: bool
    """isPlaceHolder"""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AssignResources(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, CreateAssignments: list[AssignmentCreateContainer]) -> Teamcenter.Services.Strong.Projectmanagement._2012_02.ScheduleManagement.CreatedObjectsContainer:
        """    
             Assign Resource.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         Schedule.
             
        :param CreateAssignments: 
                         AssignmentCreateContainer
             
        :return: Created Objects
        """
        ...
    def ShiftSchedule(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDate: System.DateTime, IsNewFinishDate: bool, RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

