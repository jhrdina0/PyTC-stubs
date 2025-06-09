import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class EngineeringDataLoad:
    """
    Interface EngineeringDataLoad
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateRelBwDsRoutineRev(self, XlsbDs: Teamcenter.Soa.Client.Model.Strong.Dataset, RoutineRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates a Dpv0CustomRoutineRuleset  relationship between a
             Dpv0ruleset  and a routine revision (MEInspection_Revison). The operation
             determines the Dpv0ruleset from the xlsbDs,
             which is associated to any revision of the Dpv0ruleset.
             

Use Cases:

             In the Manufacturing Process Planner (MPP) application in the Teamcenter rich client,
             a user can associate a Dpv0ruleset  with  a routine revision via Tools|"Import
             Feature Data" after a routine revision is selected.
             

             In the MPP application, a user can associate a Dpv0ruleset  with  a routine
             revision by right-clicking the routine revision and selecting "Apply Rule Set" from
             the ensuing context menu.
             


Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param XlsbDs: 
                         The <b>Dpv0RuleSetDataset</b> dataset attached to a<b> Dpv0rulesetRevision</b>

        :param RoutineRev: 
                         A routine revision of type <b>MEInspection_Revison</b>

        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...

