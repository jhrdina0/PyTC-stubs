import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetVariantOptionsResponse:
    """
    
            The structure contains a list of VariantOptionsOfPlanResponse
            structures encapsulating the input
            
Prg0AbsPlan object along with the list of Cfg0ProductModel objects.
            
    """
    def __init__(self, ) -> None: ...
    ResponseStructList: list[VariantOptionsOfPlanResponse]
    """
            The list of VariantOptionsOfPlanResponse
            Structure.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """An object of serviceData for any error information."""

class VariantOptionsOfPlanResponse:
    """
    
            This structure contains the input Prg0AbsPlan object along with a list of
            Cfg0ProductModel objects.
            
    """
    def __init__(self, ) -> None: ...
    Plan: Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan
    """The input Prg0AbsPlan object."""
    ProductVariantVector: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsValue]
    """List of Cfg0ProductModel objects."""

class AdvancedProgramManagement:
    """
    Interface AdvancedProgramManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetVariantOptions(self, PlanList: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan]) -> GetVariantOptionsResponse:
        """    
             This operation returns a list of Cfg0ProductModel  objects from Configurator
             Context associated with root Prg0ProgramPlan of the input Prg0AbsPlan
             objects. The Cfg0ProductModel  objects directly associated with any Prg0AbsPlan
             object are filtered out.
             

             This operation accepts a vector of Prg0AbsPlan objects, each of which can
             be a Prg0ProgramPlan, Prg0ProjectPlan or Prg0SubProjectPlan.
             

Uses Cases:
             
             The user can pass a Prg0ProgramPlan, Prg0ProjectPlan or Prg0SubProjectPlan
             object as input.
             
             Configurator Context1
             
             |
             
             |.......................&hellip; Model Family1
             
             &hellip;.................................................|..&hellip;Product
             Model1
             
             ..............................................&hellip;...|..&hellip;Product
             Model2
             

             Configurator Context2
             
             |
             
             |.......................&hellip; Model Family2
             
             &hellip;.................................................|..&hellip;Product
             Model5
             
             ..............................................&hellip;...|..&hellip;Product
             Model6
             
             .....................................................|......Product Model7
             
             .....................................................|......Product Model8
             

             Program1 has Configurator Context1 associated with it. Currently no Product Models
             are directly associated with Program1.
             

             Program2 has Configurator Context2 associated with it. Currently Product Model6 is
             directly associated with Program2 and Product Model7 and Product Model8 are associated
             with SubProject1.
             

Plan Hierarchy


             Program1
             
             |
             
             |.........................Project1
             

             Program2..............................................................................>Product
             Model6
             
             |
             
             |.........................Project2
             
             ..........................|
             
             ..........................|......................SubProject2.........................>Product
             Model7, Product Model8
             

Use case 1: Prg0ProgramPlan object is passed as input.
             
             If the user passes a Prg0ProgramPlan as input, this operation returns a list
             of Product Models in the Configurator context associated with the input Prg0ProgramPlan.
             Product Models directly associated with any Prg0AbsPlan are filtered.
             

             Assuming user passes Program1 as input, the output would be a structure containing
             Program1 and a list containing Product Model1 and Product Model2.
             

Use Case 2: Prg0ProjectPlan object is passed as input.
             
             If the user passes a Prg0ProjectPlan as input, the operation would return
             a list of Cfg0ProductModel objects from the Configurator Context associated
             with the root Prg0ProgramPlan object for the input Prg0ProjectPlan
             object. Product Models directly associated with any Prg0AbsPlan are filtered.
             

             Assuming user passes Project2 as input, the output would be a structure containing
             Project2 and a list containing Product Model1 and Product Model2.
             

Use Case 3: Prg0SubProjectPlan object is passed as input.
             
             If the user passes a Prg0SubProjectPlan as input, the operation would return
             a list of Cfg0ProductModel objects from the Configurator Context associated
             with the root Prg0ProgramPlan object for the input Prg0SubProjectPlan
             object. Product Models directly associated with any Prg0AbsPlan are filtered.
             

             Assuming user passes SubProject1 as input, the output would be a structure containing
             SubProject1 and a list containing Product Model5.
             
             Product Model7 and Product Model8 are associated with SubProject1. Product Model5
             is associated with Program2; hence they are filtered and are not part of the output.
             

Teamcenter Component:

             Advanced Program Management - Defines the Advanced Program Management component.
             
        :param PlanList: 
                         A list of Prg0AbsPlan objects.
             
        :return: 190021 : The parent Plan "%1$" does not contain any associated Product Models.
        """
        ...

