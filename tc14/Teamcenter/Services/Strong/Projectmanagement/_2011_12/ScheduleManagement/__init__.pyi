import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreatedDependenciesContainer:
    """
    The created dependencies
    """
    def __init__(self, ) -> None: ...
    CreatedDependencies: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    """The new dependencies"""
    UpdatedTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """The updated tasks"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""

class DependencyCreateContainer:
    """
    Creates Dependencies between tasks in the same schedule.
    """
    def __init__(self, ) -> None: ...
    PredTask: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The predecessor task for the dependency"""
    SuccTask: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The successor task for the dependency"""
    DepType: int
    """The type of dependency: 0-FS, 1-FF, 2-SS, 3-SF"""
    LagTime: int
    """The lag time in minutes (480 ~ 1 day)"""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateDependencies(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, NewDependencies: list[DependencyCreateContainer]) -> CreatedDependenciesContainer:
        """    
             Creates Dependencies between tasks in the same schedule, between a task and a proxy
             task in the same schedule, or between a tasks in different schedules (but in the
             same master schedule).  It returns the created dependencies, created proxy tasks
             (if any), and the ob
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The schedule where these dependencies will exist.
             
        :param NewDependencies: 
                         The new dependencies
             
        :return: The created dependencies
        """
        ...

