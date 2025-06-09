import System
import Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement
import Teamcenter.Soa.Client.Model
import typing

class GenericAttributesContainer:
    """
    
A collection of KeyValContainers or StringValContainers reprenting the create or
updates for a single object, such as Schedule, ScheduleTask, TaskDependency, or
ResourceAssignment
    """
    def __init__(self, ) -> None: ...
    ServiceType: str
    """The service type. Valid values are "GET" or "POST","VALIDATE" or "PERSIST""""
    OperationType: str
    """The operation type (may be set by the system if the API does not have multiple contracts)"""
    ScheduleUid: str
    """the schedule uid. This is required for batch updates in multiple schedules."""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The tag to the object being updated"""
    StringValContainer: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.StringValContainer]
    """
            A collection of updates. Valid values are  key = property name which is to be updated
            eg "priority"  value = value of the property eg. "2"
            """
    TypedAttributesContainer: list[Teamcenter.Services.Strong.Projectmanagement._2008_06.ScheduleManagement.TypedAttributeContainer]
    """A collection of updates for extended properties if there are any (optional)"""

class GenericResponseContainer:
    """
    This is the generic response container
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData"""
    ObjectUids: list[str]
    """The list of objects uid"""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of objects"""

class ScheduleModifyContainer:
    """
    
The information necessary to update a schedule.  It contains information about
new,
updated, and deleted tasks, resource assignments, and task dependencies.
    """
    def __init__(self, ) -> None: ...
    ScheduleUid: str
    """the schedule uid"""
    ServiceType: str
    """The service action"""
    ScheduleUpdates: GenericAttributesContainer
    """the schedule updates"""
    DeleteAllTasks: bool
    """Delete all tasks flag"""
    NewTasks: list[GenericAttributesContainer]
    """The new tasks to add"""
    NewDependencies: list[GenericAttributesContainer]
    """The new dependencies"""
    NewAssignments: list[GenericAttributesContainer]
    """The new assignments"""
    TaskUpdates: list[GenericAttributesContainer]
    """The existing task updates"""
    DependenciesUpdate: list[GenericAttributesContainer]
    """The existing dependencies updates"""
    AssignmentUpdates: list[GenericAttributesContainer]
    """The existing assignment updates"""
    DeletedTasks: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The deleted tasks"""
    DeletedDependencies: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The deleted dependencies"""
    DeletedAssignments: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The deleted assignments"""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ModifySchedules(self, ScheduleModifyContainers: list[ScheduleModifyContainer]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Not Implemented.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param ScheduleModifyContainers: 
                         Not Implemented
             
        :return: Not Implemented
        """
        ...
    def UpdateTasks(self, Updates: list[GenericAttributesContainer], ScheduleUid: list[str]) -> GenericResponseContainer:
        """    
             Updates Schedule Tasks. Note: You must use PERSIST for the ServiceType and ScheduleTaskUpdate
             for the operationType inside the GenericAttributesContainers which are passed.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Updates: 
                         vector of task updates
             
        :param ScheduleUid: 
                         Vector of scheduleUids. For batch updates, the scheduleUid attribute in the generic
                         container must be provided.
             
        :return: GenericResponseContainer structure: contains service data and updated schedule task
        """
        ...

