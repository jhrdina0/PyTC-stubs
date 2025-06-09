import System
import Teamcenter.Soa.Client.Model
import typing

class SetExecutionIdAndRevRuleInput:
    """
    
            This is input data to set orderid property value on Execution Plan.
            
            It has unit effectivity, date effectivity and end item information to update on revision
            rule once order id has been set to execution plan.
            
    """
    def __init__(self, ) -> None: ...
    ExecutionPlan: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object of type Mei0ExecutionPlan whose order ID property and RevisionRule
            needs to be updated.
            
"""
    OrderId: str
    """Order ID property value to be set on Mei0ExecutionPlan"""
    UnitEffectivity: int
    """Value for unit effectivity to be set on RevisionRule"""
    DateEffectivity: System.DateTime
    """
            Value for date effectivity to be set on RevisionRule


"""
    IsDateEffToday: bool
    """
            If true, the RevisionRule would be updated with dateEffectivity value as today.
            If false RevisionRule would be updated with supplied value of dateEffectivity
            parameter
            
"""
    EndItem: Teamcenter.Soa.Client.Model.ModelObject
    """
            end item of type Item or its subtype to be set on RevisionRule


"""
    TopLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of BOMLine whose BOMWindow needs to be updated with new or updated
            RevisionRule


"""

class SetExecutionIdAndRevRuleResponse:
    """
    
            The updated RevisionRule  and the following partial error may be returned:300069:If
            an object of wrong type is passed to the operation210006:Specified value is not an
            integer
            
    """
    def __init__(self, ) -> None: ...
    UpdatedRevRule: Teamcenter.Soa.Client.Model.ModelObject
    """Updated RevisionRule after applying unit, date and end item effectivity."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data to handle partial errors"""

class Release:
    """
    Interface Release
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetExecutionIdAndRevisionRule(self, Input: SetExecutionIdAndRevRuleInput) -> SetExecutionIdAndRevRuleResponse:
        """    
             The service operation sets order ID to Mei0ExecutionPlan. Along with that
             it sets unit effectivity, date effectivity and end item to RevisionRule of
             ConfigurationContext


Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         SetExecutionIDAndRevisionRule structure which contains the information for creating
                         or updating <b>RevisionRule</b> of <b>ConfigurationContext</b> and setting order
                         id value on <b>Mei0ExecutionPlan</b>

        :return: and the following partial error may be returned:300069:If
             an object of wrong type is passed to the operation210006:Specified value is not an
             integer
        """
        ...

