import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CharacteristicValueInfo:
    """
    The CharacteristicValueInfo structure.
    """
    def __init__(self, ) -> None: ...
    CharacteristicDefinition: Teamcenter.Soa.Client.Model.Strong.CharacteristicDefinition
    """Recorded or invalidated CharacteristicDefinition object."""
    CharacteristicValue: Teamcenter.Soa.Client.Model.Strong.CharacteristicValue
    """
            Null if recording a new record else the CharacteristicValue which is being
            invalidated.
            """
    CapturedBy: str
    """Name of the user that captured/invalidated the characteristic value"""
    DoubleValue: float
    """
            Numeric charecteristic value to be recorded for the part. It is considered if CharacteristicDefinition
            is for numeric value
            """
    IsDoubleValueNull: bool
    """
            If true, doubleValue is considered as null; otherwise, the doubleValues
            is used
            """
    DateValue: System.DateTime
    """
            Date charecteristic value to be recorded for the part. It may be different than current
            date. It is considered if CharacteristicDefinition is for date value
            """

class UtilizationInputInfo:
    """
    
The UtilizationInputInfo structure holds the required information to
record/invalidate
the utilization for the PhysicalPart.
    """
    def __init__(self, ) -> None: ...
    PhysicalPart: Teamcenter.Soa.Client.Model.ModelObject
    """
            The physical part for which utilization is recorded/invalidated. The valid object
            type is PhysicalBOMLine.
            """
    LogBook: Teamcenter.Soa.Client.Model.Strong.LogBook
    """The LogBook for which utlization entry is to be recorded."""
    LogEntry: Teamcenter.Soa.Client.Model.Strong.LogEntry
    """
            NULL if recording a new record else the LogEntry object against which a record
            is being invalidated.
            """
    LogEntryDesc: str
    """The description for LogEntry. Ignored in case of invalidation"""
    RecordedAt: System.DateTime
    """The time at which utilization is recorded. Ignored in case of invalidation."""
    CapturedBy: str
    """
            Name of the person who captured the characteristic value on the part. It may not
            be a TC user
            """
    Propagate: bool
    """
            Wheather the CharacteristicValue is to be propagated to child PhysicalPart
            objects. If true, the value is propagated. In case of invalidation, if propagate
            is true for exiting characterstic value then it is ignored
            """
    ValueInput: list[CharacteristicValueInfo]
    """
            The list of CharacteristicValueInfo  specifying the data to be recorded or
            invalidated
            """

class UtilizationLogEntry:
    """
    The UtilizationLogEntry structure holds recorded or invalidated LogEntry.
    """
    def __init__(self, ) -> None: ...
    LogEntry: Teamcenter.Soa.Client.Model.Strong.LogEntry
    """Created or invalidated LogEntry object."""
    ValueOutput: list[Teamcenter.Soa.Client.Model.Strong.CharacteristicValue]
    """The list of CharacteristicValue specifying recorded or invalidated data."""

class UtilizationResponse:
    """
    The UtilizationResponse structure is returned as output.
    """
    def __init__(self, ) -> None: ...
    OutputInfo: list[UtilizationLogEntry]
    """The list of UtilizationLogEntry specifying recorded or invalidated LogEntry."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""

class MROCore:
    """
    Interface MROCore
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RecordAndInvalidateUtilization(self, Info: list[UtilizationInputInfo]) -> UtilizationResponse:
        """    
             This operation records/invalidate the utilization for the PhysicalPart. Utilization
             can be recorded/ invalidated for the CharacteristicsDefinition associated
             to neutral Item from which the PhysicalPart is realized. Record will create
             a new LogEntry and CharacteristicValue. Invalidate will set existing
             CharacteristicValue as invalid and creates new CharacteristicValue
             for the same LogEntry. The invalidation is restrictied to the users as defined
             in Access Manager (AM) rule by admin in Teamcenter.
             

             Use Cases:
             
             Use Case 1 : Record new data for physical part.
             
             User can record utilization for a physical part using the context menu option on
             the selected PhysicalBOMLine. The result is displayed in log entries view.
             

             Use Case 2 : Invalidate existing record.
             
             User can invalidate the existing record in log entries view by selecting a CharacteristicValue
             and using an edit option. As a result invalidated and new data will be visible in
             the view.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param Info: 
                         a list of <i>UtilizationInputInfo</i> structure, which hold the required information
                         to record/invalidate the utilization for the <b>PhysicalPart</b>.
             
        :return: 
        """
        ...

