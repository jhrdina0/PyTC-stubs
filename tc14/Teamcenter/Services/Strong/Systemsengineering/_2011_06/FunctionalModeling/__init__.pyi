import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeleteFunctionStructInfo:
    """
    
DeleteFunctionStructInfo structure represents the parameters required to delete
            a BOM line or BOM structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    FuncBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The line to be deleted."""
    IsDeleteChildren: bool
    """If true, the entire BOM structure will be deleted."""

class FunctionalModeling:
    """
    Interface FunctionalModeling
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteFunctionStructure(self, Input: list[DeleteFunctionStructInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes a BOMLine object and optionally deletes its entire
             BOM structure. It not only deletes the structure relations but also deletes the objects
             underlying the BOM lines. If user chooses to delete the entire BOM structure, the
             structure is traversed and every node is validated for deletion. If the Teamcenter
             business object is released or referenced or there are more than one revisions of
             it, it cannot be deleted.
             

Teamcenter Component:

             Systems Engineering - Application to construct Systems Engineering view of the product
             
        :param Input: 
                         holds the required information to delete a line or structure.
             
        :return: 
        """
        ...

