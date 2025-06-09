import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ChangeOwningProgInput:
    """
    
            A list of Item objects and TC_Project to be the new owning program
            of the Items
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique identifier supplied by the caller. This ID is used to identify ChangeOwningProgInput
            and partial errors associated with this input structure. This is optional, provide
            empty String for null or optional.
            """
    OwningProgram: Teamcenter.Soa.Client.Model.Strong.TC_Project
    """
            The Business object (TC_Project) is passed to set the Owning Program
            of the items. This is a required parameter.
            """
    InputItemObjects: list[Teamcenter.Soa.Client.Model.Strong.Item]
    """
            The business object items (Item) passed for which the Owning Program is to
            be changed. This is a required parameter.
            """

class AdsFoundation:
    """
    Interface AdsFoundation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ChangeOwningProgramOfItems(self, ChangeOwningProgInput: list[ChangeOwningProgInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation changes the owning program of  the Item objects. Owning Program
             (owning_project attribute of item) is changed to the new value passed in.
             

Teamcenter Component:

             Aerospace and Defense Foundation - A set of capabilities/functionality (data model
             and behaviours)required for Aerospace and Defense Foundation extension.  This component
             defines Aerospace and Defense Foundation extension behavior.
             
        :param ChangeOwningProgInput: 
                         A list of <b>Item</b> objects and <b>TC_Project</b> to be the new owning program
                         of the Items
             
        :return: 900041 Only the selected Item and the latest Item Revision are updated with the new
             Owning Program, because no propagation rule is defined for Owning Programs.
        """
        ...

