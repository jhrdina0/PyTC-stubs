import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CharacteristicValueInputInfo:
    """
    Structure contains the value to be recorded for CharacteristicsDefinition.
    """
    def __init__(self, ) -> None: ...
    CharDef: Teamcenter.Soa.Client.Model.Strong.CharacteristicDefinition
    """A object  for which the value is recorded."""
    Value: float
    """The value to be recorded."""
    DateValue: System.DateTime
    """The date value to be recorded."""

class RebasePhysPartInputInfo:
    """
    Structure represents the parameters required to rebase the PhysicalPartRevision.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PhysicalBOMLine: Teamcenter.Soa.Client.Model.Strong.PhysicalBOMLine
    """The object to be rebased."""
    NeutralBOMLine: Teamcenter.Soa.Client.Model.Strong.NeutralBOMLine
    """The object to rebase to."""
    RebaseDate: System.DateTime
    """The rebase date."""
    ContextName: str
    """The structure context name with which new structure context is to be saved."""

class RebasePhysPartOutput:
    """
    Structure represents the output parameters of rebase operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input RebasePhysPartInputInfo element. This value is unchanged from
            the input, and can be used to identify this response element with the corresponding
            input element.
            """
    PhysicalBOMLine: Teamcenter.Soa.Client.Model.Strong.PhysicalBOMLine
    """The modified object."""

class RebasePhysPartResponse:
    """
    
Structure represents BOMWindow containing the modified PhysicalBOMLine
object along with the ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[RebasePhysPartOutput]
    """A modified PhysicalBOMLine object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class RecordUtilizationInputInfo:
    """
    Structure represents the parameters required to record utilization for
PhysicalPart.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PhysBOMLine: Teamcenter.Soa.Client.Model.Strong.PhysicalBOMLine
    """The PhysicalBOMLine for which the utilization is recorded."""
    LogBook: Teamcenter.Soa.Client.Model.Strong.LogBook
    """The LogBook where the entry of this recording is associated."""
    LogEntryDesc: str
    """The PhysicalBOMLine for which the utilization is recorded."""
    RecordedAt: System.DateTime
    """The time at which the utilization is recorded."""
    CapturedBy: str
    """The string indicating who captured the characteristics value."""
    Propagate: bool
    """If true, the values are propagated to child PhysicalPart objects."""
    ValueInput: list[CharacteristicValueInputInfo]
    """The structure indicating the values to be recorded."""

class RecordUtilizationOutput:
    """
    Structure represents the output parameters of recordUtilization operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The clientId from the input RecordUtilizationInputInfo element. This value is unchanged from
            the input, and can be used to identify this response element with the corresponding
            input element.
            """
    LogEntry: Teamcenter.Soa.Client.Model.Strong.LogEntry
    """The created object."""

class RecordUtilizationResponse:
    """
    
Structures containing the created LogEntry along with the ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[RecordUtilizationOutput]
    """A LogEntry object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class MROCore:
    """
    Interface MROCore
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RebasePhysicalPart(self, InputData: list[RebasePhysPartInputInfo]) -> RebasePhysPartResponse:
        """    
             This operation allows rebasing the PhysicalPartRevision associated with the
             PhysicalBOMLine to the Neutral ItemRevision associated with the NeutralBOMLine.
             It also saves StructureContext associated with the Neutral Structure, with
             PhysicalPartRevision. You can rebase the PhysicalPartRevision to the
             different revision of the Item than the existing.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param InputData: 
                         Structures which holds the required information to rebase the <b>PhysicalPartRevision</b>.
             
        :return: 
        """
        ...
    def RecordUtilization(self, Info: list[RecordUtilizationInputInfo]) -> RecordUtilizationResponse:
        """    
             This operation records the utilization for the PhysicalPart. Utilization
             can be recorded for the CharacteristicsDefinition associated to neutral Item
             for which the PhysicalPart is realized from.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param Info: 
                         Structures which hold the required information to record the utilization for the
                         <b>PhysicalPart</b>.
             
        :return: 
        """
        ...

