import Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class EffectivityConditionInfo:
    """
    
            This structure provides input data for the operation such as the list of the objects
            which are affected and the effectivity expressions to be processed.
            
    """
    def __init__(self, ) -> None: ...
    TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            A list of all affected business objects on which effectivity is to be set. Any POM_object
            or subtype supporting effectivity behavior is the valid input for this parameter.
            """
    Expression: Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression
    """
            The effectivity expression that should be set on the affected objects. Effectivity
            is set using either ConfigFormula, nested ConfigExpressions or EffectivityTableRow
            in this structure
            """

class EffectivityConditionSource:
    """
    
            This structure contains sourceObject and sourceExpression for which the effectivity
            is to be obtained.
            
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            The business object which should be used to extract the effectivity expression. Any
            POM_object or  subtype supporting effectivity behavior is the valid input for this
            parameter.
            """
    SourceExpression: Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression
    """
            This is ConfigExpression contains effectivity expression that should be used as source
            effectivity expression to process. When both fields are populated, sourceObject will
            be used and sourceExpression will be ignored.
            """

class EffectivityManagement:
    """
    Interface EffectivityManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetEffectivitySubsetTables(self, ProductName: str, ProductNamespace: str, SubsetCriteria: Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression, EffectivityConditions: list[EffectivityConditionSource]) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityTablesResponse: ...
    def SetEffectivityConditionSubsets(self, ProductName: str, ProductNamespace: str, SubsetCriteria: Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression, ActionCode: int, EffectivityConditions: list[EffectivityConditionInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

