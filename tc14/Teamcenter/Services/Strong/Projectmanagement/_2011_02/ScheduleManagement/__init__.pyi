import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SchMgtOptions:
    """
    Special copy-paste options
    """
    def __init__(self, ) -> None: ...
    LogicalOptions: list[SchMgtLogicalOption]
    """List of logical options"""
    IntegerOptions: list[SchMgtIntegerOption]
    """List of integer options"""
    StringOptions: list[SchMgtStringOption]
    """List of string options"""

class FromSchedule:
    """
    The information regarding a schedule to copy from.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule to copy from."""
    Tasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """The list of tasks in that schedule to copy."""
    SchmgtOptions: SchMgtOptions
    """
            Option structure for list of logical, integer and string options IntegerOptions {
            numberOfCopies - the number of copies } LogicalOptions { includeAssignments - copy
            assignments,includeDependencies - copy dependencies,includeDeliverables - copy deliverables,useExistingDeliverables
            - link copied to existing (by name), createMembership - copy missing members, resetDeliverableInstances
            - reset the instance of Schedule Deliverables, copyWorkflowTemplate - copy workflow
            template information, copyCostOfTask - copy costs, offsetBasedOnPositionInTemplate
            - shift tasks relative of original offset, recalcAsyncDispatcher - recalculate in
            asynchronously }
            """

class MultiSchSpecialCopyResponse:
    """
    Return type of SOA for special paste
    """
    def __init__(self, ) -> None: ...
    CreatedTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """Created Tasks"""
    ModifiedTasks: list[Teamcenter.Soa.Client.Model.Strong.ScheduleTask]
    """Modified Tasks"""
    CreatedMembers: list[Teamcenter.Soa.Client.Model.Strong.ScheduleMember]
    """Created Members"""
    CreatedDeliverables: list[Teamcenter.Soa.Client.Model.Strong.SchDeliverable]
    """Created Schedule Deliverables"""
    CreatedDependencies: list[Teamcenter.Soa.Client.Model.Strong.TaskDependency]
    """Created Dependencies"""
    CreatedAssignments: list[Teamcenter.Soa.Client.Model.Strong.ResourceAssignment]
    """Created Assignments"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data"""

class SchMgtIntegerOption:
    """
    Integer Options for special copy-paste
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the option."""
    Value: int
    """The integer value of the option."""

class SchMgtLogicalOption:
    """
    Logical options for special copy-paste
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the option."""
    Value: bool
    """The value of logical option (True or False)."""

class SchMgtStringOption:
    """
    String Options for special copy-paste
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the option."""
    Value: str
    """The string value of the option"""

class ToSchedule:
    """
    Target Schedule under which tasks will be pasted.
    """
    def __init__(self, ) -> None: ...
    TargetSchedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The target Schedule"""
    Task: Teamcenter.Soa.Client.Model.Strong.ScheduleTask
    """The target Task"""
    PasteType: str
    """Paste Type - PasteBeforeTask/PasteUnderTask/PasteAfterTask"""

class SpecialCopyContainer:
    """
    Input container
    """
    def __init__(self, ) -> None: ...
    FromSchedule: list[FromSchedule]
    """List of FromSchedules"""
    ToSchedule: ToSchedule
    """Target Schedule"""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SpecialPasteScheduleTasks(self, CopyContainer: SpecialCopyContainer) -> MultiSchSpecialCopyResponse:
        """    
             Gets the selected Schedule and their tasks and paste it to target task as specified
             by the options.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param CopyContainer: 
                         Container which consists of list of <font face="courier" height="10">FromSchedule</font>
                         and a <font face="courier" height="10">ToSchedule</font>

        :return: 
        """
        ...

