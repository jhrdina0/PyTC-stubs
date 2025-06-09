import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BomLineInfo:
    """
    This structure holds the source and the target BOMLine objects.
    """
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The source BOMLine."""
    TargetLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The target BOMLine."""

class IncrementalChange:
    """
    Interface IncrementalChange
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CarryOver(self, BomLineInfos: list[BomLineInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation carries the IncrementalChangeElement (ICE) object(s) from the
             source line to the corresponding target line by cloning them.
             
             There are two BMIDE constants that were introduced for this functionality
             

             Type Constant Fnd0EnableIceCarryOver

             Property Constant Fnd0AttrIcesToExclude


             - New IncrementalChangeElement object(s) are attached to the original incremental
             change revision.
             

             - Add changes on the occurrence are ignored - It does not make sense to have two
             occurrences appearing at the same time at different locations.


             - GDELine objects are not supported.
             

             - For attribute changes the context of the absolute occurrence data is the new parent
             BOMView Revision.
             

             - If there is no write access on incremental change revision, the carryover is allowed
             with a programmatic bypass.
             
             - If there is any failure while cloning any IncrementalChangeElement object
             that is being carried over, the entire operation will rollback.
             

             - Carryover is not possible if we have the following two conditions:
             

Both source and target BomView Revision item type are not
             available in the BMIDE Type Constant Fnd0EnableIceCarryOver.
             
BOM-BOP case - If the source line is a BOMLine and the target
             line is a BOP (Bill of Process) line or vice versa
             



Use Cases:

             User wants to carry over IncrementalChangeElement object(s) when doing a Copy-Paste
             or a Cut-Paste of a BOMLine having IncrementalChangeElement object(s),
             from one structure partition to another partition within the Plant BOP.
             
             User wants to carry over IncrementalChangeElement object(s) when doing a Copy-Paste
             or a Cut-Paste of a BOMLine having IncrementalChangeElement object(s),
             from Product BOP and to another partition in the Plant BOP.
             



Teamcenter Component:

             Incremental Change - An incremental change collects a number of structure changes
             to a component such as add or remove of components or changes to attachments (data).
             Incremental change is an alternative to revision-based effectivity configuration.
             
        :param BomLineInfos: 
                         A list of source and their corresponding target <b>BOMLine</b> objects
             
        :return: 
        """
        ...

