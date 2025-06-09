import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CharacteristicValueInputInfo:
    """
    Structure contains the value to be recorded for characteristics definition.
    """
    def __init__(self, ) -> None: ...
    CharDef: Teamcenter.Soa.Client.Model.Strong.CharacteristicDefinition
    """A characteristics definition object  for which the value is being recorded."""
    Value: float
    """The value to be recorded."""
    DateValue: System.DateTime
    """The date value to be recorded."""

class RecordUtilizationInputInfo:
    """
    
            Structure represents the parameters required to record utilization for physical part
            revision.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique ID value used to identify return data elements and partial errors associated
            with this input structure.
            """
    AsmPhyPartRev: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """The physical part revision for which the utilization is recorded."""
    Logbook: Teamcenter.Soa.Client.Model.Strong.LogBook
    """The log book where the entry of this recording is associated."""
    LogEntryDesc: str
    """The description of the log entry."""
    RecordedAt: System.DateTime
    """The time at which the utilization is recorded."""
    CapturedBy: str
    """The identification of who captured the characteristics value."""
    Propagate: bool
    """
            If true, the values are propagated to child physical part revision objects.  If false,
            the values are recorded only against the identified physical part revision.
            """
    ValueInput: list[CharacteristicValueInputInfo]
    """
            List of CharacteristicValueInputInfo structure indicating values to be recorded against
            a characteristic defination.
            """

class RecordUtilizationOutput:
    """
    Structure represents the output parameters of recordUtilization operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input RecordUtilizationInputInfo

            element. This value is unchanged from the input, and can be used to identify this
            response element with the corresponding input element
            
"""
    LogEntry: Teamcenter.Soa.Client.Model.Strong.LogEntry
    """The created LogEntry object."""

class RecordUtilizationResponse:
    """
    Structures containing the created LogEntry along with the ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[RecordUtilizationOutput]
    """List of LogEntry objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class AsMaintained:
    """
    Interface AsMaintained
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RecordUtilization(self, RecordUtilizationInfo: list[RecordUtilizationInputInfo]) -> RecordUtilizationResponse:
        """    
             Maintenance Repair and Overhaul (MRO) introduces physical parts and structures of
             physical parts which are generated from a neutral structure of part(s).  Either As-Built
             or As-Maintained physical structures may be generated. As-Built physical parts do
             not support utilization recording. All references to physical parts and physical
             part revisions in this operation are for As-Maintained physical parts only.
             
             Characteristic definitions describe usage characteristics that can be recorded or
             measured against a physical part.  Characteristic definitions may be created and
             related to parts before the As-Maintained physical part is generated
             
             This operation records utilization for a physical part revision.  Utilization may
             be recorded against any characteristic definition associated to a neutral part from
             which the physical part is realized.
             


Teamcenter Component:

             MRO As-Maintained - This component provides capabilities to generate and perform
             actions on As-Maintained structures.
             
        :param RecordUtilizationInfo: 
                         The information to record the utilization for the physical part revision.
             
        :return: 
        """
        ...

