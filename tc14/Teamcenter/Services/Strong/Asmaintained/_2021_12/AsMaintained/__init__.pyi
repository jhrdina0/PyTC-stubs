import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CharacteristicValueInfo:
    """
    The Characteristic Value Information Structure
    """
    def __init__(self, ) -> None: ...
    CharacteristicDefinition: Teamcenter.Soa.Client.Model.Strong.CharacteristicDefinition
    """Recorded or invalidated CharacteristicDefinition object."""
    CharacteristicValue: Teamcenter.Soa.Client.Model.Strong.CharacteristicValue
    """
            The CharacteristicValue  object which is being invalidated. If recording a new record
            set to NULL.
            """
    CapturedBy: str
    """Name of the user that captured or invalidated the characteristic value."""
    DoubleValue: float
    """
            Numeric Characteristic value to be recorded for the part. It is considered if CharacteristicDefinition
            is for numeric value.
            """
    IsValueNull: bool
    """
            If true, doubleValue, boolValue, and stringValue are considered as null; othewise,
            doubleValues, boolValue, and stringValues are used.
            """
    BoolValue: bool
    """
            Boolean Characteristic value to be recorded for the part. It is considered if CharacteristicDefinition
            is of Boolean type. For e.g. isPumpRunning kind of characteristics.
            """
    StringValue: str
    """
            String Characteristic value to be recorded for the part. It is considered if CharacteristicDefinition
            is of String type. It is a user supplied value.
            """
    DateValue: System.DateTime
    """
            Date Characteristic value to be recorded for the part. It may be different than current
            date. It is considered if CharacteristicDefinition is for date value.
            """

class UtilizationInputInfo:
    """
    The Utilization Input Information structure.
    """
    def __init__(self, ) -> None: ...
    PhysicalPart: Teamcenter.Soa.Client.Model.ModelObject
    """
            The physical part for which utilization is recorded/invalidated. The valid object
            type is PhysicalBOMLine or PhysicalPartRevision.
            """
    LogBook: Teamcenter.Soa.Client.Model.Strong.LogBook
    """The LogBook object for which utlization entry is to be recorded."""
    LogEntry: Teamcenter.Soa.Client.Model.Strong.LogEntry
    """
            The LogEntry object against which a record is being invalidated. When recording a
            new record set to NULL.
            """
    LogEntryDesc: str
    """The description for LogEntry. Ignored in case of invalidation."""
    RecordedAt: System.DateTime
    """The time at which utilization is recorded. Ignored in case of invalidation."""
    CapturedBy: str
    """
            Name of the person who captured the characteristic value on the part. It may not
            be a TC user. Record Utilization is captured by field engineer or service technician
            who might not have teamcenter license. This is a free text field.
            """
    Propagate: bool
    """
            If true, the value is propagated to child PhysicalPart objects.. In case of invalidation,
            exiting charactristics values of children are not updated.
            """
    ValueInput: list[CharacteristicValueInfo]
    """A list of CharacteristicValueInfo  specifying the data to be recorded or invalidated."""

class UtilizationLogEntry:
    """
    The Utilization Log Entry Structure
    """
    def __init__(self, ) -> None: ...
    LogEntry: Teamcenter.Soa.Client.Model.Strong.LogEntry
    """Created or invalidated LogEntry object."""
    ValueOutput: list[Teamcenter.Soa.Client.Model.Strong.CharacteristicValue]
    """A list of CharacteristicValue specifying recorded or invalidated data."""

class UtilizationResponse:
    """
    The Utilization Response structure.
    """
    def __init__(self, ) -> None: ...
    OutputInfo: list[UtilizationLogEntry]
    """A list of UtilizationLogEntry specifying recorded or invalidated LogEntry."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class AsMaintained:
    """
    Interface AsMaintained
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RecordAndInvalidateUtilization(self, Info: list[UtilizationInputInfo]) -> UtilizationResponse: ...

