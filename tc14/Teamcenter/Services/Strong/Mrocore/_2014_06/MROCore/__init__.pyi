import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AssignLotInfo:
    """
    
This operation assigns the Lot to the PhysicalPart and deducts the
quantity by the specified size. If the Size is greater than the lot usage or the
PhysicalPart quantity then the error is thrown. If the physicalBOMLine is
not provided then the specified quantity is deducted from the Lot assigned to
PhysicalPartRevision.
If the physicalBOMLine is provided then the specified quantity is deducted from
the
Lot that is assigned to PhysicalPartRevision from the PhysicalBomLine, if the
quantity
is less than the expected quantity then the missing PhysicalPart is created with
the remaning quantity.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PhysicalBOMLine: Teamcenter.Soa.Client.Model.Strong.PhysicalBOMLine
    """The physicalBOMLine object to which the lot will be assigned."""
    PhysicalPartRevision: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """The PhysicalPartRevision object to which the lot will be assigned."""
    Lot: Teamcenter.Soa.Client.Model.Strong.Lot
    """The Lot object which will be assigned."""
    Quantity: int
    """Integer quantity that will be deducted from the lot after the assignment."""

class MROCore:
    """
    Interface MROCore
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AssignLot(self, Info: list[AssignLotInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation assigns the Lot to the PhysicalPart and deducts the
             quantity by the specified size. If the Size is greater than the lot usage or the
             PhysicalPart quantity then the error is thrown.
             

Teamcenter Component:

             MRO Core - MRO Core
             
        :param Info: 
                         A list of AssignLotInfo structures which hold the information to assign the <b>Lot</b>
                         to the <b>PhysicalPart</b>.
             
        :return: 
        """
        ...

