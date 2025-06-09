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
    CharacterisitcValue: Teamcenter.Soa.Client.Model.Strong.CharacteristicValue
    """
            The CharacteristicValue  object which is being invalidated. If recording a
            new record set to NULL.
            """
    DoubleValue: float
    """
            Numeric Characteristic value to be recorded for the part. It is considered if CharacteristicDefinition
            is for numeric value.
            """
    IsValueNull: bool
    """
            If true, doubleValue/boolValue/stringValue is considered as null; else, the doubleValues/boolValue/stringValues
            are used.
            """
    BoolValue: bool
    """
            Boolean Characteristic value to be recorded for the part. It is considered if CharacteristicDefinition
            is of Boolean type.
            """
    StringValue: str
    """
            String Characteristic value to be recorded for the part. It is considered if CharacteristicDefinition
            is of String type. User can input any String value they want to record for the characteristic.
            """
    DateValue: System.DateTime
    """
            Date Characteristic value to be recorded for the part. It may be different than current
            date. It is considered if CharacteristicDefinition is for date value.
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
    """The LogBook object for which utlization entry is to be recorded."""
    LogEntry: Teamcenter.Soa.Client.Model.Strong.LogEntry
    """
            The LogEntry object against which a record is being invalidated. If recording
            a new record set to NULL.
            """
    LogEntryDesc: str
    """The description for LogEntry. Ignored in case of invalidation."""
    RecordedAt: System.DateTime
    """The time at which utilization is recorded. Ignored in case of invalidation."""
    CapturedBy: str
    """
            Name of the person who captured the LogEntry and/or CharacteristicValue
            on the part.
            """
    Propagate: bool
    """
            Wheather the CharacteristicValue is to be propagated to child PhysicalPart
            objects. If true, the value is propagated. In case of invalidation, if propagate
            is true for exiting characterstic value then it is ignored.
            """
    ValueInput: list[CharacteristicValueInfo]
    """A list of CharacteristicValueInfo  specifying the data to be recorded or invalidated."""

class UtilizationLogEntry:
    """
    The UtilizationLogEntry structure holds recorded or invalidated LogEntry
    """
    def __init__(self, ) -> None: ...
    LogEntry: Teamcenter.Soa.Client.Model.Strong.LogEntry
    """Created or invalidated LogEntry object."""
    ValueOutput: list[Teamcenter.Soa.Client.Model.Strong.CharacteristicValue]
    """A list of CharacteristicValue specifying recorded or invalidated data."""

class UtilizationResponse:
    """
    The UtilizationResponse structure is returned as output
    """
    def __init__(self, ) -> None: ...
    OutputInfo: list[UtilizationLogEntry]
    """A list of UtilizationLogEntry specifying recorded or invalidated LogEntry."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class MROCore:
    """
    Interface MROCore
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RecordAndInvalidateUtilization(self, Info: list[UtilizationInputInfo]) -> UtilizationResponse: ...

