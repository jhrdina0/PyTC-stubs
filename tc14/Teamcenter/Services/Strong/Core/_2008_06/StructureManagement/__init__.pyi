import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateInStructureAssociationResponse:
    """
    Return structure for createInStructureAssociations  operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData structure is used to return the updated objects and contains
            partial errors, if any, occurring in the operation.
            """

class GetPrimariesOfInStructureAssociationInfo:
    """
    Input structure for GetPrimariesOfInStructureAssociationInfo operation
    """
    def __init__(self, ) -> None: ...
    Secondary: Teamcenter.Soa.Client.Model.ModelObject
    """secondary object/BOMLine business object"""
    ContextBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Context object of association. This is generally the parent line of the primary object
            and is an optional parameter.
            """
    AssociationType: str
    """
            the created association type e.g. ConnectTo, ImplementedBy, RealizedBy, DeviceToConnector,
            RoutedBy, SignalToSource, SignalToTarget, SignalToTransmitter, ProcessVariable,
            RedundantSignal.
            """

class GetPrimariesOfInStructureAssociationResponse:
    """
    Return structure for GetPrimariesOfInStructureAssociationResponse  operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData structure is used to return the primary BOMLine business
            objects and partial errors if any occurring in the operation.
            """
    PrimariesInfo: list[PrimariesOfInStructureAssociation]
    """Context object of association. This is generally the parent line of the primary object."""

class GetSecondariesOfInStructureAssociationInfo:
    """
    Input structure for GetSecondariesOfInStructureAssociationInfo operation
    """
    def __init__(self, ) -> None: ...
    PrimaryBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """primary BOMLine"""
    ContextBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Context BOMLine business object of association (optional)"""
    AssociationType: str
    """Association type between the primary and secondary BOMLine business objects."""

class GetSecondariesOfInStructureAssociationResponse:
    """
    Return structure for GetSecondariesOfInStructureAssociationResponse  operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Secondary BOMLine business objects and Partial errors if any"""
    SecondariesInfo: list[SecondariesOfInStructureAssociation]
    """primary BOMLine and association type."""

class InStructureAssociationInfo:
    """
    Input structure for InstructureAssociationInfo operation
    """
    def __init__(self, ) -> None: ...
    PrimaryBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The primary object of association"""
    ContextBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            The context in which the association of the specified type between primaryBOMLine
            and secondaries is valid.
            """
    Secondaries: list[Teamcenter.Soa.Client.Model.ModelObject]
    """secondary objects of association."""
    AssociationType: str
    """association type to be created"""

class PrimariesOfInStructureAssociation:
    """
    Output structure for GetPrimariesOfInStructureAssociationInfo operation
    """
    def __init__(self, ) -> None: ...
    Secondary: Teamcenter.Soa.Client.Model.ModelObject
    """secondary object for which the primaries has been returned"""
    AssociationType: str
    """association type to be created"""
    PrimaryBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Primary object associated with the secondary"""

class RemoveInStructureAssociationsInfo:
    """
    Input structure for removeInStructureAssociations operation
    """
    def __init__(self, ) -> None: ...
    PrimaryBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """primary BOMLine object reference of association"""
    ContextBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Context BOMLine of association (optional)"""
    Secondaries: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Secondary BOMLines to be disassociated from the primary BOMLine."""
    AssociationType: str
    """Association type between primary and secondary BOMLines."""

class RemoveInStructureAssociationsResponse:
    """
    Return structure for GetSecondariesOfInStructureAssociationResponse  operation
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The updated objects and partial errors if any."""

class SecondariesOfInStructureAssociation:
    """
    Output structure for GetSecondariesOfInStructureAssociationInfo operation
    """
    def __init__(self, ) -> None: ...
    PrimaryBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Primary BOMLine associated with the secondary."""
    AssociationType: str
    """association type to be created"""
    Secondaries: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Secondary BOMLines associated with the primaries"""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateInStructureAssociations(self, Inputs: list[InStructureAssociationInfo]) -> CreateInStructureAssociationResponse:
        """    
             This operation creates the specified association between primary and secondary BOMLine
             objects in a structure.  As the name indicates, these associations are created in
             a specific context and are applicable only in that context. The context is specified
             as an additional input in the input structure, by the caller. Some examples of these
             associations are: the ConnectTo, ImplementedBy, RealizedBy, SignalToSource, SignalToTarget,
             SignalToTransmitter, ProcessVariable, RedundantSignal relations that are provided
             in Teamcenter [see Use case]. This operation takes a vector of InStructureAssociationInfo
             as input. The input structures contain information on the BOMLine objects
             that need to be associated, what context they need to be associated in and the type
             of association. Note that the associations created are only valid in the context
             specified.
             
             If input primary is Signal object's BOMLine, then for associating signal BOMLine
             to secondary as source or target, the association type is optional, and if input
             association type is empty, the secondary BOMLine objects GDE object direction
             attirbute value will be used for associating signal BOMLine to secondary as
             source or target.
             

Use Cases:

             Use this operation to create an association between BOMLine objects. This is a generic
             Teamcenter service to create various types of associations. The type of the association
             that gets created depends on the Association Type specified in the input structure.
             
             The ConnectTo  functionality establishes an association between 1 or more BOMLine
             objects and a Connection BOMLine. The association signifies that the BOMLine objects
             are connected to the Connection BOMLine in a certain context.  Outside of that context
             the association is not valid. The caller of this operation provides as input, one
             or more BOMLine objects, and a Connection BOMLine. The associationType should be
             set in the input structure to ConnectTo and specifies a BOMLine that will act as
             a context line within which the association is valid.
             

Dependencies:

             createBOMWindows
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a vector of InStructureAssociationInfo structure. Each element shall consist
                         of a primary <b>BOMLine</b>, the secondary <b>BOMLine</b> objects to be associated
                         with the primary, the line in whose context the association takes place and the association
                         type.
             
        :return: 
        """
        ...
    def GetPrimariesOfInStructureAssociation(self, Inputs: list[GetPrimariesOfInStructureAssociationInfo]) -> GetPrimariesOfInStructureAssociationResponse:
        """    
             This operation gets the primary BOMLines like PSConnection, Signal
             of an association given the secondary object and association type.  Examples of these
             associations are: ConnectTo, ImplementedBy, RealizedBy, RoutedBy, FixingToSegment,
             DeviceToConnector, SignalToTransmitter, SignalToSource, SignalToTarget, ProcessVariable,
             RedundantSignal. This operation takes a vector of GetPrimariesOfInStructureAssociationInfo
             as input.
             

Use Cases:

             A typical usecase for this operation is where callers would like to obtain primary
             BOMLine objects by providing the association type and the corresponding secondary
             BOMLine associated.  In a SignalToTransmitter association for example,
             if the transmitting BOMLine  is provided, callers can get the corresponding
             Signal which is the primary BOMLine in this relation.
             

Dependencies:

             createBOMWindows
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a vector of <i>GetPrimariesOfInStructureAssociationInfo</i> structure. Each
                         element consists of a secondary <b>BOMLine</b>, the context <b>BOMLine</b> of the
                         association and the association type.
             
        :return: 
        """
        ...
    def GetSecondariesOfInStructureAssociation(self, Inputs: list[GetSecondariesOfInStructureAssociationInfo]) -> GetSecondariesOfInStructureAssociationResponse:
        """    
             Given the primary object and association type, returns the secondary BOMLine
             business objects of in structure associations. These associations can be ConnectTo,
             ImplementedBy, RealizedBy, RoutedBy, FixingToSegment, DeviceToConnector, SignalToSource,
             SignalToTarget, SignalToTransmitter, ProcessVariable or RedundantSignal.
             It takes a vector of GetSecondariesOfInStructureAssociationInfo as input.
             

Use Cases:

             Users shall use this operation to get secondary BOMLine business objects for
             a given association type and the primary object associated with it.
             
             For instance, this operation could be used to get all the secondary GDE lines connected
             to a PSConnection by passing the association type as ConnectTo. Similarly,
             it can be used to get the connector lines connected to the Device Line by
             passing appropriate primary Device and the association type as DeviceToConnector.
             

Dependencies:

             createBOMWindows
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a vector of <i>GetSecondariesOfInStructureAssociationInfo</i> structure.
                         Each element shall consist of a primary <b>BOMLine</b>, the parent line in whose
                         context the association takes place and the association type.
             
        :return: 
        """
        ...
    def RemoveInStructureAssociations(self, Inputs: list[RemoveInStructureAssociationsInfo]) -> RemoveInStructureAssociationsResponse:
        """    
             Given the primary BOMLine, the association type, and the secondary BOMLines
             this operation removes the instructure associations between the BOMLines.
             These associations can be ConnectTo, ImplementedBy, RealizedBy, RoutedBy, FixingToSegment,
             DeviceToConnector, SignalToSource, SignalToTarget, SignalToTransmitter, ProcessVariable
             or RedundantSignal. The operation takes a vector of RemoveInStructureAssociationsInfo
             as Input.
             
             If input primary is Signal object's BOMLine, then for associatiion type input
             between signal and secondary as source or target can be optional, and if input association
             type is empty, then the secondary BOMLine association to input primary Signal
             BOMLine  as source and target will be removed.
             

Use Cases:

             Developers shall use this operation when an association has to be removed between
             the BOMLines. This is a generic Teamcenter service to remove various types
             of associations.
             
             In the case of ConnectTo, if the secondary BOMLines are passed as null
             then all the secondary associations with the primary BOMLine shall be removed.
             


Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         This is a vector of <i>RemoveInStructureAssociationsInfo</i> structure. Each element
                         shall consist of a primary <b>BOMLine</b>, the secondary <b>BOMLines</b> to be removed,
                         the parent line in whose context the association takes place and the association
                         type.
             
        :return: 
        """
        ...

