import Sss0.Services.Strong.Svcscheduling._2012_02.SvcScheduling
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class RecordUtilizationInputInfo:
    """
    
            RecordUtilizationInputInfo will be used to capture characteristic values for the
            Job Activity and the Physical Part.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique client identifier. This is a unique string supplied by the caller. This
            ID
            
            is used to identify return data elements and partial errors associated with this
            input structure.
            """
    JobActivity: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Job Card  or Job Task . The user captures and records the
            
            characteristics values during the execution of this selected Job Card or
            
            Job Task .
            """
    LogBook: Teamcenter.Soa.Client.Model.Strong.LogBook
    """
            Log Book. The log book is used to record the utilization information. It
            
            represents a collection of log entries recorded against a specific physical asset
            or utilization details for a Job Activity . The selected object may have more than
            one associated log book. A log entry denotes a record of data collected about a specific
            object in context, such as a physical asset and recorded by a certain person at a
            certain point of time. The log entry value is associated with a single asset but
            may record characteristic values for several components within that asset.
            
"""
    LogEntryDesc: str
    """
            Log entry description. It denotes the description of the logbook and the related
            
            utilization information recorded by the log book.
            """
    RecordedAt: System.DateTime
    """
            Recorded Date. This parameter represents the date the utilization values were
            
            recorded. If a user does not enter a value for the recording time, the date is set
            from the current date/time on the server.
            """
    CapturedBy: str
    """
            The string indicating the user who captured the values for the characteristic
            
            definitions. This parameter takes a string of upto 128 alphanumeric characters in
            size.
            
"""
    Propagate: bool
    """
            Indicates if the values are to be propagated to its child physical parts. This
            
            parameter takes in a true or false value.
            """
    ValueInput: list[Sss0.Services.Strong.Svcscheduling._2012_02.SvcScheduling.CharacteristicValueInputInfo]
    """The structure indicating the values recorded."""

class UpdateConfigurationInputInfo:
    """
    
            UpdateConfigurationInputInfo will be used to capture the Job Activity and the Date
            of Configuration update.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique client identifier. This is a unique string supplied by the caller.
            
            This ID is used to identify return data elements and partial errors associated with
            this input structure.
            """
    JobActivity: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Job Card  or Job Task . The user updates the physical
            
            configuration based on Part Movements and Job Card Upgrades defined on the Job Activity
            during the execution of this selected Job Card or Job Task.
            
"""
    ConfigUpdateDate: System.DateTime
    """
            This parameter represents the date the physical configuration was
            
            updated. If a user does not enter a value for this element, the date is set from
            the current date/time on the server.
            """

class SvcScheduling:
    """
    Interface SvcScheduling
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RecordUtilization(self, Inputs: list[RecordUtilizationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation records utilization for the selected JobActivity. A JobActivity
             encompasses both the JobCard and the JobTasks. The operation takes
             as input the information for properties that indicates the values recorded for the
             selected object. You can track and record utilization information based on life,
             observation, and date characteristic definitions for the following objects:
             
JobCard

JobTask

PhysicalPart

             When you capture the utilization values for a JobCard or JobTask, you
             have the option of recording the characteristic definition values for the impacted
             part related to the JobCard. If the JobCard does not have a related
             impacted part, the physical asset related to the JobCard is used. Recording
             values for a physical asset will need to ensure that characteristic definitions are
             already assigned to the related realized neutral item before the physical part was
             generated. During execution of a JobCard or JobTask, validation ensures
             that the user cannot record characteristic values under three conditions:
             
             The JobCard is designated as upgrade.
             
             The JobActivity is not at the leaf level.
             
             The JobActivity has PartMovement defined.
             
             Execution of a JobActivity validates that all characteristic definitions assigned
             to the object are captured. A configurable condition will determine if the completion
             of the task is not permitted and an appropriate warning message is issued.
             


Use Cases:

             Use Case 1: Record Collected Characteristics
             
             Record Utilization captures characteristic values that are recorded during the execution
             of the JobActivity. The values recorded do not need to be defined as required
             characteristics. If the characteristics being recorded are the same as a characteristic
             that can be recorded on the impacted physical part, then that value could also be
             recorded on that physical part. This action can be performed directly from the object
             or a worklist assignment.
             
             Use Case 2: Validate Characteristics Recorded
             
             Validations are performed to ensure that all of the characteristics defined for a
             JobActivity have been recorded prior to completion. The system can be configured
             to either provide a warning, or prevent completion of the task if this validation
             fails.
             


Teamcenter Component:

             Service Scheduling - This Component is intended to identify all Operations and Services
             under Service Scheduling.
             
        :param Inputs: 

        :return: 
        """
        ...
    def UpdateConfiguration(self, Inputs: list[UpdateConfigurationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates the physical asset configuration of the impacted part on a
             JobActivity based on the part movements or upgrades defined on it. The configuration
             gets updated upon the completion of the JobActivity. A JobActivity
             encompasses both the JobCard and the JobTask.
             
             You can update the physical configuration by performing the following tasks:
             

Execution of the part movements related to the JobActivity.
             
Rebase the impacted physical asset for a JobCard, if the JobCard
             is of type upgrade.
             


             A PartMovement is a record of each physical part that is installed, replaced
             or uninstalled as a result of the execution of a JobCard or JobTask.
             Each part movement of a physical part must have a unique part movement record. You
             can create three types of PartMovement objects:
             

Uninstall
             
Install
             
Replace
             


             To ensure the correct physical configuration is set, validations are performed when
             creating a PartMovement. PartMovement cannot be added to a JobActivity
             under the following three circumstances:
             

The JobActivity has assigned characteristic values.
             
The JobCard is designated as upgrade.
             
The JobActivity is not at the leaf level.
             


             You can designate a JobCard as an Upgrade. This primarily handles upgrades
             by identifying a different neutral configuration, part number or revision that you
             want assigned to the impacted physical part related to the JobCard. If the
             selected JobCard does not have an impacted part, the physical asset defined
             for the JobCard is used. After the JobCard is set as an Upgrade
             the Update Configuration operation is used to rebase the physical part or asset to
             a new configuration, part number or revision.
             
             To ensure that the correct physical configuration is set, validations are performed
             when designating a JobCard as an Upgrade.  JobCard cannot be
             designated as an Upgrade under the following three conditions:
             

The JobCard has PartMovement defined.
             
The JobCard has assigned Characteristic values.
             
The JobCard is not at the level.
             



Use Cases:

             This operation updates the configuration of the physical structure based on the recorded
             PartMovement or JobCard Upgrade. This action occurs upon completion
             and closure of the JobCard or JobTask



Teamcenter Component:

             Service Scheduling - This Component is intended to identify all Operations and Services
             under Service Scheduling.
             
        :param Inputs: 

        :return: 
        """
        ...

