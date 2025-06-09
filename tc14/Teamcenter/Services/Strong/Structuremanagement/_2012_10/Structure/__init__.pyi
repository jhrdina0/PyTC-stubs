import System
import Teamcenter.Soa.Client.Model
import typing

class CutItemParam:
    """
    
Structure contains the item revision to be deleted and the BOMWindow that is
using
it.
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """The BOMWindow where the selected items to be deleted appear."""
    Objs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of selected items to be deleted."""

class Structure:
    """
    Interface Structure
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CutItems(self, Input: list[CutItemParam]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Cut lines of the selected Item Revisions in a window and delete the Item
             Revisions.
             
             If the selected Item Revision is the last revision of the Item , then
             the Item will be deleted.
             

Use Cases:

Use case1: Simple Cut

             A user wants to delete some Item Revisions in a structure which are not referenced
             anywhere else. The user calls the operation with the BOMWindow and the
             Item Revisions. The BOMLine for the selected Item Revisions will
             be removed from the structure and the Item Revisions will be deleted.
             

Use case2: Cut with partial errors

             A user wants to delete some Item Revisions in a structure which are referenced
             in My Teamcenter and lines of some of the Item Revisions are in released
             structure. The user calls the operation with the BOMWindow and the Item
             revisions. The Item Revisions for the lines that are in released structure
             will fail to be deleted but the other Item Revisions will be deleted and the
             entries in My Teamcenter will also be removed.
             

Use case3: Cut the last revision of the item

             A user wants to delete an Item Revision, which is the last revision of the
             Item. The user calls the operation with the BOMWindow and the Item
             Revision. The BOMLine for the selected Item Revision will be removed
             from the structure and the Item will be deleted
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         A structure that contains the input information for cut items.
             
        :return: 
        """
        ...

