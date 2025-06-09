import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetBOMLineInfo:
    """
    Structure represents the parameters required to get BOMLine after create.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    SelectedBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Parent BOMLine under which newly created BOMLine will be attached."""
    NewComp: Teamcenter.Soa.Client.Model.ModelObject
    """Item for which BOMLine needs to be created."""

class RequirementsManagement:
    """
    Interface RequirementsManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetBomlineAfterCreate(self, Inputs: list[GetBOMLineInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates a BOMLine for a newly created  Item and adds it to the selected
             parent BOMLine and checks out the latest revision of newly created Item based on
             a check-out preference. The inputs structure for this operation contains selected
             parent BOMLine and newly created Item (e.g. Functionality or Logical Block).
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         This argument contains parent BOMLine and newly created business object of the Item.
                         The newly created Item is used to create the BOMLine and to get the latest ItemRevision
                         for the checkout. The parent BOMLine in the input list is used to attach the newly
                         created BOMLine.
             
        :return: A GetBOMLineResponse with ServiceData element containing the newly created BOMLine.
             The following partial error may be returned: 515024  Specified object tag is not
             a valid.
        """
        ...

