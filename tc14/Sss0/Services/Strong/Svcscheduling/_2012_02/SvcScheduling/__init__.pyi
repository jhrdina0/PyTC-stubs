import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CharacteristicValueInputInfo:
    """
    Characteristic Value input
    """
    def __init__(self, ) -> None: ...
    CharDef: Teamcenter.Soa.Client.Model.Strong.CharacteristicDefinition
    """Characteristics definition"""
    Value: float
    """Value recorded for the characteristics"""
    DateValue: System.DateTime
    """Date Value recorded for the characteristics"""
    ForPhysicalPart: bool
    """Record on physical part"""

class RecordUtilizationInputInfo:
    """
    
RecordUtilizationInputInfo will be used to
            capture characteristic values for the Job Activity and the Physical Part.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique client identifier. This is a unique string supplied by the caller. This
            ID
            
            is used to identify return data elements and partial errors associated with this
            input structure.
            
"""
    JobActivityRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Job Card Revision or Job Task Revision. The user captures and records the
            
            characteristics values during the execution of this selected Job Card or
            
            Job Task Revision.
            
"""
    LogBook: Teamcenter.Soa.Client.Model.Strong.LogBook
    """
            Log Book. The log book is used to record the utilization information. It
            
            represents a collection of log entries recorded against a specific physical asset
            or utilization details for a Job Activity Revision. The selected object may have
            more than one associated log book. A log entry denotes a record of data collected
            about a specific object in context, such as a physical asset and recorded by a certain
            person at a certain point of time. The log entry value is associated with a single
            asset but may record characteristic values for several components within that asset.
            
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
    ValueInput: list[CharacteristicValueInputInfo]
    """The structure indicating the values recorded."""

class UpdateConfigurationInputInfo:
    """
    
UpdateConfigurationInputInfo will be used
            to capture the Job Activity Revision and the Date of Configuration update.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique client identifier. This is a unique string supplied by the caller.
            
            This ID is used to identify return data elements and partial errors associated with
            this input structure.
            
"""
    JobActivityRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Job Card Revision or Job Task Revision. The user updates the physical
            
            configuration based on Part Movements and Job Card Upgrades defined on the Job Activity
            Revision during the execution of this selected Job Card or Job Task Revision.
            
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
             This operation will record utilization for the selected Job Activity based on the
             input RecordUtilizationInputInfo supplied.
             A Job Activity comprises of Job Cards and Job Tasks. The RecordUtilizationInputInfo
             contains information for properties such as jobActivityRev, logBook, recordedAt,
             capturedBy, propagate and valueInput that indicates the values recorded for the selected
             object. A user can track and record utilization information based on life, observation,
             and date characteristic definitions for the following objects:
             

Job Cards
             
Job Tasks
             
Physical Part
             


             When a user captures the utilization values for a Job Card or Job Task, the user
             has the option of recording the characteristic definition values for the impacted
             part related to the Job Card. If the Job Card does not have a related impacted part,
             the physical asset related to the Job Card is used. The user recording values for
             a physical asset will need to ensure that characteristic definitions are already
             assigned to the related realized neutral item before the physical part was generated.
             During execution of a Job Card or Job Task, validation ensures that the user cannot
             record characteristic values under three conditions:
             

The selected Job Card is marked for upgrade.
             
The Job Activity is a non leaf level Job Card or Job Task.
             
Part Movements exist on the Job Card or Job Task.
             


             Execution of a Job Activity Revision validates that all characteristic definitions
             assigned to the object are captured. A configurable condition will determine if the
             completion of the task is not permitted and appropriate warning message is issued.
             

Use Cases:

Use Case 1: Record Collected Characteristics

             Record Utilization allows the user to capture characteristic values that are recorded
             during the execution of the Job Card or Job Task. The values recorded do not need
             to be defined as required characteristics. If the characteristics being recorded
             are the same as a characteristic that can be recorded on the impacted physical part,
             then that value could also be recorded on that physical part. This action can be
             performed directly from the object or a Worklist assignment.
             
Use Case 2: Validate Characteristics Recorded

             Validations are performed to ensure that all of the characteristics defined for a
             Job Card or Job Task have been recorded prior to completion. The system can be configured
             to either provide a warning, or prevent completion of the task if this validation
             fails.
             


Teamcenter Component:

             BOM Grading - Functionality for grading a BOM structure
             
        :param Inputs: 
<font face="courier" height="10">RecordUtilizationInputInfo</font> that will be used
                         to record values for the assigned characteristics defined for the selected Job Activity
                         or Physical Part.
             
        :return: .
        """
        ...
    def UpdateConfiguration(self, Inputs: list[UpdateConfigurationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates physical asset configuration of the impacted part on Job Activity
             Revision based on the Part Movements and Upgrades defined on it. The configuration
             gets updated upon the completion of the Job Activity. A Job Activity encompasses
             of Job Card and Job Task. The user updates the physical configuration from a Job
             Card or Job Task to perform the following tasks:
             

Execute the physical structure Part Movements related to the Job
             Activity.
             
Rebase the impacted physical asset for a Job Card, if the Job Card
             is of type Upgrade.
             


             A Part Movement is a record of each physical part that is installed, replaced or
             uninstalled as a result of the execution of a Job Card or Job Task. Each install
             or uninstall of a physical part must have a unique part movement record. A user can
             create three types of Part Movements, Uninstall, Install and Replace.
             
             To ensure the correct physical configuration is set, validations are performed where
             Part Movements cannot be added to a Job Activity under the following three circumstances:
             

Job Cards or Job Tasks with related assigned characteristic values.
             
Job Cards designated as upgrades.
             
Job Cards or Job Tasks which are not at the leaf level.
             


             A user can define Upgrade Job Cards to primarily handle upgrades by identifying a
             different neutral configuration assigned to the impacted physical asset related to
             the Job Card. If the selected Job Card does not have an impacted part, the physical
             part defined for the Job Card is used. Update Configuration is used to rebase the
             physical asset to a new configuration, part number or revision after the user has
             set up an Upgrade on the Job Card. To confirm that the correct physical configuration
             is used, validations are carried out and Upgrades cannot be defined on the Job Card
             under the following three conditions:
             

The Job Card has Part Movements defined.
             
The Job Card has characteristic definitions assigned.
             
The Job Card is a non leaf level Job Activity.
             


             The input parameter, UpdateConfigurationInputInfo
             is supplied to the operation which contains information for properties such as jobActivityRev
             and configUpdateDate that represents the date the physical configuration was updated.
             

Use Cases:

             This operation provides the ability to update the configuration of the physical structure
             based on the recorded Part Movement or Job Card Upgrade. This action occurs upon
             completion and closure of the Job Card or Job Task.
             

Teamcenter Component:

             BOM Grading - Functionality for grading a BOM structure
             
        :param Inputs: 
<font face="courier" height="10">UpdateConfigurationInputInfo</font> that will be
                         used to update the physical configuration for the defined Job Card Upgrades and Part
                         Movements on the selected Job Activity.
             
        :return: .
        """
        ...

