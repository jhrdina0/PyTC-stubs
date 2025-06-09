import System
import Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2013_05.StructureVerification
import Teamcenter.Soa.Client.Model
import typing

class AccountabilityCheckResponse:
    """
    Contains all the results from the accountabilityCheck operation
    """
    def __init__(self, ) -> None: ...
    AccountabilityCheckResults: list[Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.AccountabilityCheckResult]
    """A vector of accountability check results"""
    ReachableTargets: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vector of reachable target lines"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""
    SourceConfigContext: Teamcenter.Soa.Client.Model.ModelObject
    """The source configuration context for an equivalent source object."""
    TargetConfigContext: Teamcenter.Soa.Client.Model.ModelObject
    """The target configuration context for an equivalent target object."""

class StructureVerification:
    """
    Interface StructureVerification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AccountabilityCheck2(self, Input: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.ACInput, BatchDetails: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.BatchDetails) -> AccountabilityCheckResponse:
        """    
             The operation will call the existing accountability check functions, which will generate
             a check result for report in the colored display.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         Input values to the operation
             
        :param BatchDetails: 
                         In case the operation has to be performed asynchronously, this parameter can be used
                         to pass that information. Pass NULL for second parameter if unused
             
        :return: Returns the results from the accountability check and the source and target configuration
             context for source and target object.
        """
        ...
    def GetAttrGrpsAndFormsComparisonDetail(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], AttributeGroupsNames: list[str], SourceConfigContext: Teamcenter.Soa.Client.Model.ModelObject, TargetConfigContext: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.StructureVerification.AttributeGroupAndFormComparisonResponse:
        """    
             This operation returns the details of differences between the supplied Attribute
             Groups for the supplied equivalent objects (that can be Cpd0DesignElement, Cpd0DesignFeature,
             or BOMLine objects) and the supplied configuration contexts for source equivalent
             object and target equivalent object respectively.For 4gd to 4gd compare, attribute
             group names includes attribute groups and managed attribute groups.Source and target
             configuration context is needed if the attribute group names include Managed attribute
             group properties.For each supplied attribute group the operation returns the list
             of its attributes, the attributes values for each supplied source and target, and
             the result of comparing each attribute on all supplied sources and targets.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         The list of Cpd0DesignElement, Cpd0DesignFeature or BOMLine objects that were deemed
                         equivalent by some method, for which any differences in attribute groups is required.
                         This list also contains correspo0nding configuration context for source equivalent
                         and target equivalent object.
             
        :param AttributeGroupsNames: 
                         The list of attribute groups names that need to be compared.
             
        :param SourceConfigContext: 
                         The source configuration context of source equivalent object.
             
        :param TargetConfigContext: 
                         The target configuration context of target equivalent object
             
        :return: For each supplied attribute group the operation returns the list of its attributes,
             the attributes' values for each supplied source and target, and the result of comparing
             each attribute on all supplied sources and targets. The following partial errors
             may be returned: - 253049 The input equivalent set doesn't contain any sources or
             any targets. - 253001 This error can only be returned if there is some kind of environment
             issue or a bug in the code, it will never happen during normal execution
        """
        ...

