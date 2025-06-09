import Ptn0.Services.Strong.Partition._2011_06.PartitionManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClonePartitionsFailedObjsErrorStruct:
    """
    
ClonePartitionsFailedObjsErrorStruct structure
            represents the source Partitions that failed, source Partition Scheme and ErrorValuesStruct structure.
            
    """
    def __init__(self, ) -> None: ...
    SourceScheme: Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme
    """The source Partition scheme business object of the partition that failed to clone."""
    SourcePartition: Teamcenter.Soa.Client.Model.Strong.Ptn0Partition
    """The source Partition business object that failed to clone."""
    ErrorValue: Ptn0.Services.Strong.Partition._2011_06.PartitionManagement.ErrorValuesStruct
    """List containing error detail."""

class ClonePartitionsInputInfo:
    """
    
ClonePartitionsInputInfo structure contains
            the target Application Model, clone input options and source Application Model or
            source Partition schemes.
            
    """
    def __init__(self, ) -> None: ...
    SourceModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            The source Partition Template business object from where partition breakdowns are
            to be cloned. Partitions from all schemes from a model, can be cloned by giving business
            object as input. sourceSchemes should be
            null to clone entire partition breakdown of the given Application Model.
            """
    SourceSchemes: list[Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme]
    """
            A list of source Partition schemes from where partition breakdowns are to be cloned.
            Partitions from given schemes  can be cloned by giving Partition schemes as input.
            Application Model of the given Partition schemes are known hence sourceModel input will be ignored.
            """
    InputOptions: list[StringBoolMapStruct]
    """
            A list containing map of option names and flag values (string/boolean). Valid option
            names are:
            
checkOutOnCreate - if true, the cloned partitions
            are checked-out on create.
            
includeVariantExpressions - if true, the
            variant expressions are carried forward from source partitions to target partitions.
            
includeAttributeGroups - if true, the attribute
            groups are carried forward from source partitions to target partitions.
            
"""
    TargetModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            The target Application Model business object where the cloned partition breakdowns
            are to be created.
            """

class ClonePartitionsOutputInfo:
    """
    
ClonePartitionsOutputInfo structure represents
            the source Application Model for which failed partitions are reported and the list
            of ClonePartitionsFailedObjsErrorStruct strucutre
            containing source Partition scheme, source Partitions and ErrorValuesStruct
            structure.
            
    """
    def __init__(self, ) -> None: ...
    SourceModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """The source ApplicationModel business object for which failed partitions are reported."""
    FailedPartitions: list[ClonePartitionsFailedObjsErrorStruct]
    """
            List of structure containing source Partition scheme, source Partition and its error
            structure.
            """

class ClonePartitionsResponse:
    """
    
ClonePartitionsResponse structure represents
            vector of ClonePartitionsOutputInfo and the
            errors via serviceData if invalid input parameters
            are supplied.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contatins list of newly created Partition objects. Also contains list of any errors
            occurred during the operation.
            """
    Output: list[ClonePartitionsOutputInfo]
    """
            List containing partitions that failed to clone, Partition schemes of the failed
            partitions, and source Application Model of the failed Partitions and the corresponding
            failure detail. This will be empty when there is no failure in partition cloning.
            """

class CreateOrUpdateRealizedPartitionsInputInfo:
    """
    
CreateOrUpdateRealizedPartitionsInputInfo
            structure contains target Application Model, instantiation input options, Revision
            Rule, Variant Rule and source Application Model or source Partition Schemes or source
            Partitions
            
    """
    def __init__(self, ) -> None: ...
    TargetModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            The target Application Model business object where the realized partition breakdowns
            are to be created.
            """
    InputOptions: list[StringBoolMapStruct]
    """
            A list containing map of option names and flag values (String/Boolean).
            
            Valid option names for createOrUpdateRealizedPartitions operation are:
            
includeVariantExpressions - if true, the
            variant expressions are carried forward from source partitions to target partitions.
            
includeAttributeGroups - if true, the attribute
            groups are carried forward from source partitions to target partitions.
            
includeChildPartitions - if true, the child
            Partitions are carried forward from source partitions to target partitions.
            
updateRealizedPartition - if true, updates
            the realized partitions from source partitions.
            

            Valid option names for clonePartitions operation are:
            
checkOutOnCreate - if true, the cloned partitions
            are checked-out on create. This option is ignored if the copyRealizationReferences
            option is selected.
            
includeVariantExpressions - if true, the
            variant expressions are carried forward from source partitions to target partitions.
            
includeAttributeGroups - if true, the attribute
            groups are carried forward from source partitions to target partitions.
            
excludeLocalPartitions - if true, the locally
            created (unrealized) Partitions would not be copied to the target Application Model.
            The option is valid only if the source Application Model is a Product Design or Product
            Architecture Model.
            
copyRealizationReferences - if true, the
            realization references to the template Partitions are copied to the Partition breakdown
            in the target Application Model. This option is valid only when neither the source
            Application Model nor target Application Model is Partition Template.
            
copyMappings - if true, the associated Partition
            mappings are carried forward from source Partitions to target Partitions.
            """
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """
            The Revision Rule to be applied to configure the partition breakdowns at source Application
            Model.
            """
    VarRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """
            The Variant Rule to be applied to configure the partition breakdowns at source Application
            Model.
            """
    SourceModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            The source Application Model business object reference from where partition breakdowns
            are to be realized. Partitions from all schemes from a model, can be realized by
            giving Application Model business object as input. Both sourceSchemes
            and sourcePartitions elements should be null
            to realize entire partition breakdown of the given Application Model.
            """
    SourceSchemes: list[Teamcenter.Soa.Client.Model.Strong.Ptn0PartitionScheme]
    """
            A list of source Ptn0PartitionScheme business object references from where
            partition breakdowns are to be realized. Partitions from different Partition schemes
            can be realized by giving Partition schemes as input. Application Model of the given
            Partition schemes are known, hence sourceModel
            input will be ignored. sourcePartitions elements
            should be null to realize entire partition breakdown of the given Partition schemes.
            """
    SourcePartitions: list[Teamcenter.Soa.Client.Model.Strong.Ptn0Partition]
    """
            A list of source Ptn0Partition business object references from where partition
            breakdowns are to be realized. Partitions from different schemes and different models
            can be realized selectively by giving Partitions as input. Application Models and
            Partition schemes of the given Partitions are known, hence both sourceModel and sourceSchemes
            inputs will be ignored.
            """

class StringBoolMapStruct:
    """
    
StringBoolMapStruct represent the structure
            of StringBoolMap.
            
    """
    def __init__(self, ) -> None: ...
    BoolMap: System.Collections.Hashtable
    """
            A Map that contains option name and flag value (string/Boolean).
            

            Valid option names for _2013_05::PartitionManagement::clonePartitions operation
            are:
            
checkOutOnCreate - if true, the cloned Partitions
            are checked-out on create.
            
includeVariantExpressions - if true, the
            variant expressions are carried forward from source partitions to target Partitions.
            
includeAttributeGroups - if true, the attribute
            groups are carried forward from source Partitions to target Partitions.
            

            Valid option names for createOrUpdateRealizedPartitions operation are:
            
includeVariantExpressions - if true, the
            variant expressions are carried forward from source Partitions to target Partitions.
            
includeAttributeGroups - if true, the attribute
            groups are carried forward from source Partitions to target Partitions.
            
includeChildPartitions - if true, the child
            Partitions are carried forward from source Partitions to target Partitions.
            
updateRealizedPartition - if true, updates
            the realized partitions from source Partitions.
            
overrideDefaultUpdateOptions - if true, overrides
            the default carry over options of update( carry over options that are selected during
            realization ) and considers the user input option values provided in this Map. Once
            overrideDefaultUpdateOptions is set to true, only the options with true values in
            this Map are updated for the Partition ignoring the default carry over options selected
            during realization. For example, if user has not selected carry over options during
            realization but want to update attribute groups and child Partitions during update,
            following input options values must be supplied.
            
            includeVariantExpressions - false
            
            includeAttributeGroups - true
            
            includeChildPartitions - true
            
            updateRealizedPartition - true
            
            overrideDefaultUpdateOptions - true.
            

            Valid option names for _2014_12::PartitionManagement::clonePartitions operation
            are:
            
checkOutOnCreate - if true, the cloned Partitions
            are checked-out on create. This option is ignored if the copyRealizationReferences
            option is selected.
            
includeVariantExpressions - if true, the
            variant expressions are carried forward from source Partitions to target Partitions.
            
includeAttributeGroups - if true, the attribute
            groups are carried forward from source Partitions to target Partitions.
            
excludeLocalPartitions - if true, the locally
            created (unrealized) Partitions would not be copied to the target Application Model.
            
copyRealizationReferences - if true, the
            realization references to the template Partitions are copied to the target Partitions.
            """

class PartitionManagement:
    """
    Interface PartitionManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ClonePartitions(self, Inputs: list[ClonePartitionsInputInfo]) -> ClonePartitionsResponse:
        """    
             This operation clones partition breakdowns (Ptn0Partition) from a source Application
             Model (Mdl0ApplicationModel) to a target Application Model. Source Application
             Model may be a Partition Template (Ptn0PartitionTemplateModel) or Product
             Design (Cpd0CollaborativeDesign). This operation can optionally carry forward
             variant expressions (Fnd0VariantExpression), effectivity expressions (Fnd0EffectivityExpression)
             and attribute groups (Mdl0AttributeGroup) from source partitions to target
             partitions.
             

             Partition breakdowns from a source Application Model can be used as a template to
             create similar partition breakdowns in target Application Model. After cloning the
             user could re-orient or modify partition breakdown in the target Application Model.
             Cloned partitions do not maintain any references to source partitions in source Application
             Model.
             

             When partition breakdowns are cloned in to an existing scheme in target model, and
             if there are already Partitions present in this scheme with the same Multi Field
             Key attributes then there will be a MFK uniqueness violation error reported for that
             duplicate Partitions, but this error is presented to the user only after saving of
             all non-duplicate Partitions.
             

             Note: createOrUpdateRealizedPartitions operation
             should be used if one wants to strictly maintain the child parent hierarchy of partitions
             in target Application Model.
             


Use Cases:

             Partition breakdowns from an Application Model can be used to create similar Partition
             schemes (Ptn0PartitionScheme) and partition breakdowns in other Application
             Model. This can be done by cloning partitions from selected Partition schemes of
             different Application Models or cloning the entire partition breakdown of the given
             source Application Model. The user may also optionally carry over the variant expressions,
             effectivity expressions and attribute groups optionally from source Application Model
             to target Application Model. Since the cloned partition breakdowns in target Application
             Model do not have any reference to source Application Model, it can be modified after
             cloning.
             

             Variant Expressions are carried forward only when dictionary of options and values
             required for the Variant Expression are available for the target Partition otherwise
             an error message will be thrown.
             

Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         List of target Application Model, clone input options and source Application Model
                         or source Partition schemes.
             
        :return: List of partitions failed to clone, Partition schemes of the failed partitions, source
             Application Model of the failed partitions and the corresponding failure detail will
             be returned. Partial errors are returned in ServiceData
        """
        ...
    def CreateOrUpdateRealizedPartitions(self, Inputs: list[CreateOrUpdateRealizedPartitionsInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation realizes partition breakdowns (Ptn0Partition) from Partition
             Template (Ptn0PartitionTemplateModel) to a target Application Model (Mdl0ApplicationModel)
             and updates partition breakdowns from source Partition Templates. This operation
             can optionally carry forward variant expressions (Fnd0VariantExpression),
             effectivity expressions (Fnd0EffectivityExpression), attribute groups (Mdl0AttributeGroup)
             and child Partitions from source Application Model to target Application Model. Realized
             partitions in the target Application Model can be updated to reflect the changes
             from source partitions. During this operation realization/update of realized Partitions
             the associated mappings are carried forward from source Applciation Model to target
             Application Model.
             

             Instantiated or realized partition breakdowns maintains reference to source partitions
             in Partition Template. User can add a new partition to realized partition structure
             in target application model. However, deleting an instantiated partition after realization
             is allowed in target application model. Realization of a Partition maintains a strict
             child parent hierarchy and will be same as that of its source Partition parent hierarchy.
             Realization of Partition also maintains the mappings relationships and will be same
             as that of its source Partition in parent hierarchy. During update of realized partitions
             Child-parent links and Partition mappings are automatically established in target
             application model wherever possible. Duplicate partitions will not be created during
             update of realized partitions. But the partitions are updated with Variant conditions
             and other related objects (based on Deep copy rules) from the source Partition Template
             to the target application model.
             

             Note: clonePartitions operation should be
             used if one wants to modify the child parent hierarchy of partitions in target Application
             Model.
             

Use Cases:


             Use Case1:
             
             Partition Templates can be used as blue print which can be reused to create partition
             breakdowns in other Application Models (Product Design (Cpd0CollaborativeDesign)
             or Partition Template (Ptn0PartitionTemplateModel)). This enables users to
             reuse Partition Templates and create similar Partition schemes (Ptn0PartitionScheme)
             and partition breakdowns in other Application Models.  This can be done by copy/pasting
             or drag/drop of Partitions from Partition Template to another Application Model in
             RAC. The user may also want to optionally carry over the child Partitions, variant
             expressions, and effectivity expressions and attribute groups.
             

             Variant Expressions are carried forward only when dictionary of options and values
             required for the Variant Expression are available for the target Partition otherwise
             an error message will be thrown.
             

             Use case2:
             
             Once Partitions are realized from a Partition Template to other Application Model,
             Partitions in source Partition Template may undergo changes and user may want to
             bring these updates from Partition Template in to the target model.
             


Teamcenter Component:

             Partition Management - Defines Partition Management operation (add/modify/remove
             members and child partitions),Partition Template creation and management and cloning
             functionality and extends the search services in the AppModel component.
             
        :param Inputs: 
                         List containing target Application Model, instantiation input options, Revision Rule,
                         Variant Rule and source Application Model or source Partition schemes or source Partitions.
             
        :return: Partial errors are returned in ServiceData when the operation failed to update given
             partitions.
        """
        ...

