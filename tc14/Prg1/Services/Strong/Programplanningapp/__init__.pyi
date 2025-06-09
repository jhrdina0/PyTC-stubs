import Prg1.Services.Strong.Programplanningapp._2016_05.AdvancedProgramManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model.Strong

class AdvancedProgramManagementRestBindingStub(AdvancedProgramManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetVariantOptions(self, PlanList: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan]) -> Prg1.Services.Strong.Programplanningapp._2016_05.AdvancedProgramManagement.GetVariantOptionsResponse: ...

class AdvancedProgramManagementService:
    """
    
            This service exposes operations related to Scope and Variability management for Plan
            objects in Teamcenter. Plan objects along with Configurator Context are used to perform
            Planning and management when designing large scale products.
            


Library Reference:

Prg1SoaProgramPlanningAppStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AdvancedProgramManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetVariantOptions(self, PlanList: list[Teamcenter.Soa.Client.Model.Strong.Prg0AbsPlan]) -> Prg1.Services.Strong.Programplanningapp._2016_05.AdvancedProgramManagement.GetVariantOptionsResponse:
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

