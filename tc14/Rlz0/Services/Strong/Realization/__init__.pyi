import Rlz0.Services.Strong.Realization._2014_10.RealizationManagement
import Rlz0.Services.Strong.Realization._2015_07.ModelStructureExpand
import Rlz0.Services.Strong.Realization._2015_07.RealizationManagement
import Rlz0.Services.Strong.Realization._2016_05.ModelStructureExpand
import Rlz0.Services.Strong.Realization._2016_05.RealizationManagement
import Rlz0.Services.Strong.Realization._2018_06.RealizationManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ModelStructureExpandRestBindingStub(ModelStructureExpandService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExpandModelStructure(self, Input: list[Rlz0.Services.Strong.Realization._2015_07.ModelStructureExpand.ModelExpandControls]) -> Rlz0.Services.Strong.Realization._2015_07.ModelStructureExpand.ModelStructureExpandResponse: ...
    def ExpandModelStructure2(self, Input: list[Rlz0.Services.Strong.Realization._2016_05.ModelStructureExpand.ModelExpandControls2]) -> Rlz0.Services.Strong.Realization._2015_07.ModelStructureExpand.ModelStructureExpandResponse: ...

class ModelStructureExpandService:
    """
    
            This service handles expansion of compositions and subsets. This service is mainly
            used while opening a composition or displaying the content of a composition in Teamcenter
            client. The main operation supported by this service is expandModelStructure.
            


Library Reference:

Rlz0SoaRealizationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ModelStructureExpandService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExpandModelStructure(self, Input: list[Rlz0.Services.Strong.Realization._2015_07.ModelStructureExpand.ModelExpandControls]) -> Rlz0.Services.Strong.Realization._2015_07.ModelStructureExpand.ModelStructureExpandResponse:
        """    
             This is a generic operation to expand instances of Mdl0ConditionalElement
             or Mdl0ConditionalArtifact. Currently, this operation supports expand of objects
             which are instances of subclass of Rlz0Composition or  instances of Rlz0Subset
             Class. Objects are expanded in the order of the input list and results are paged
             back to the client.
             

             Pre-Conditions:
             
             1. The source application model has some pre-existing model content.
             
             2. Target application model already exists and has composition and subsets.
             

             Limitations:
             
             Current expansion support is available only for the following classes:-
             
             1. Subclasses of Rlz0Composition.(Rlz0Composition is an abstract class)
             
             2. Rlz0Subset.
             


Use Cases:

             This API supports the navigation of contents of Rlz0Composition object or
             Rlz0Subset object.
             

             General use cases are:-
             
             1. Expansion of an Rlz0Composition object: - Expansion of an Rlz0Composition
             object returns all the Rlz0Subset objects that it contains.
             
             2. Expansion of an Rlz0Subset object: - Expansion of an Rlz0Subset
             object returns sparsely or dynamically realized model elements (Mdl0ModelElement)
             from source application model (Mdl0ApplicationModel). Unlike the concept of
             Full or Static Realization, model elements (Mdl0ModelElement) in the target
             application model (Mdl0ApplicationModel) are not new copies rather simple
             references to objects in source application model.
             

             Also, this API provides the support to expand appropriate sparse elements by applying
             filters like Purpose (rlz0purpose on Rlz0Subset object) and SourceModel
             (Mdl0ApplicationModel)   that are used during the expansion of composition
             (Rlz0Composition) or subset (Rlz0Subset).
             



Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         List of controls (<font face="courier" height="10">ModelExpandControls</font>) which
                         govern the expansion of objects.
             
        :return: 
        """
        ...
    def ExpandModelStructure2(self, Input: list[Rlz0.Services.Strong.Realization._2016_05.ModelStructureExpand.ModelExpandControls2]) -> Rlz0.Services.Strong.Realization._2015_07.ModelStructureExpand.ModelStructureExpandResponse:
        """    
             This is a generic operation to expand instances of Mdl0ConditionalElement
             or Mdl0ConditionalArtifact. Currently, this operation supports expansion of
             objects which are instances of subclass of Rlz0Composition or instances of
             Rlz0Subset Class. Objects are expanded in the order of the input list and
             results are paged back to the client.
             

             Pre-Conditions:
             
             1. The source application model has some pre-existing model content.
             
             2. Target application model already exists and has composition and subsets.
             

             Limitations:
             
             Current expansion support is available only for the following classes:-
             
             1. Subclasses of Rlz0Composition.(Rlz0Composition is an abstract class)
             
             2. Rlz0Subset.
             

Use Cases:

             This API supports the navigation of contents of Rlz0Composition object or
             Rlz0Subset object with effectivity and variant overlays.
             

             General use cases are:-
             
             1. Expansion of an Rlz0Composition object: - Expansion of an Rlz0Composition
             object returns all the Rlz0Subset objects that it contains.
             
             2. Expansion of an Rlz0Subset object: - Expansion of an Rlz0Subset
             object returns sparsely or dynamically realized model elements (Mdl0ModelElement)
             from source application model (Mdl0ApplicationModel). Unlike the concept of
             Full or Static Realization, model elements (Mdl0ModelElement) in the target
             application model (Mdl0ApplicationModel) are not new copies rather simple
             references to objects in source application model.
             

             This API provides the support to expand appropriate sparse elements by applying filters
             like Purpose (rlz0purpose on Rlz0Subset object) and SourceModel (Mdl0ApplicationModel)
             that are used during the expansion of composition (Rlz0Composition) or subset
             (Rlz0Subset).
             

             Also,this API provides the support to expand appropriate sparse elements by applying
             effectivity and variant overlay strings for input Mdl0ApplicationModel that
             are used during the expansion of composition (Rlz0Composition) or subset (Rlz0Subset).
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         List of controls (<font face="courier" height="10">ModelExpandControls2</font>) which
                         govern the expansion of objects.
             
        :return: 2. 279055 - The provided number of levels to expand is invalid. Valid values are
             0 or 1 for this operation.
        """
        ...

class RealizationManagementRestBindingStub(RealizationManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateModelToModelRealization(self, Input: Rlz0.Services.Strong.Realization._2014_10.RealizationManagement.RealizeModelContentInfo) -> Rlz0.Services.Strong.Realization._2014_10.RealizationManagement.ModelToModelRealizationContentResponse: ...
    def GetSourceModelConfigInfo(self, TargetModelObjects: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]) -> Rlz0.Services.Strong.Realization._2014_10.RealizationManagement.SourceModelConfigResponse: ...
    @typing.overload
    def CreateOrUpdateCompositionSubset(self, Input: Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.CompositionSubsetModelContentInfo) -> Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.M2MCompositionSubsetContentResponse: ...
    @typing.overload
    def CreateOrUpdateCompositionSubset(self, Input: Rlz0.Services.Strong.Realization._2016_05.RealizationManagement.CompositionSubsetModelContentInfo) -> Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.M2MCompositionSubsetContentResponse: ...
    def UncoupleModelRealization(self, Input: list[Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.UncoupleModelRealizationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetSourceItemConfigInfo(self, ElementInfos: list[Rlz0.Services.Strong.Realization._2018_06.RealizationManagement.ModelElementInfo]) -> Rlz0.Services.Strong.Realization._2018_06.RealizationManagement.SourceItemConfigResponse: ...

class RealizationManagementService:
    """
    
            This service provides operations that enable copying of model content from one application
            model (Mdl0ApplicationModel) into another
            application model in a static fashion, i.e. new objects are always created in the
            target model.
            

            Model Elements within the source application model must be subtypes of Positioned
            model element (Mdl0PositionedModelElement).
            

            Currently two operations are provided by this service namely createOrUpdateModelToModelRealization and getSourceModelConfigInfo.
            

            Realization between application models is a process of allowing model content from
            one application model to be copied into another application model. All or a portion
            of the source model can be realized into the target model. Associations are maintained
            between related objects in the source and target models, allowing for update of the
            target. The category of the realized model elements in the target model is always
            Subordinate. Principal use case for realization is MBOM.
            


Use case:


createOrUpdateModelToModelRealization:
            
            This SOA operation provides a service to Realize one Application Model (objects)
            to another Application Model. This SOA can be used for Realization and update Realized
            objects. For Realization the user will provide source information and get list of
            objects that has been newly created at target Application objects along with realization
            container objects. For update of realized objects the user should provide container
            object and source object and will get list of objects updated, deleted and created
            during update.
            
            Note: Please see operation Use case section for more details.
            

getSourceModelConfigInfo:
            
            This operation gets the configuration information of the source model element that
            was used during realization or instantiation. The input objects could be any of Reuse
            Design Component,
            
            Subordinate of a Reuse Design Component, Realization container object or Realized
            content
            
            The operation returns the list of source model object configuration information as
            a response or fails in case of error condition.
            
            Note: Please see operation Use case section for more details.
            

getSourceItemConfigInfo:
            
            This operation gets configuration information used to configure a source item assembly
            for realization.   This is useful for application that need to expand the underlying
            item assembly structure in a manner consistent with its realized representation in
            the model.
            
            Note: Please see operation Use case section for more details.
            


Library Reference:

Rlz0SoaRealizationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> RealizationManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateModelToModelRealization(self, Input: Rlz0.Services.Strong.Realization._2014_10.RealizationManagement.RealizeModelContentInfo) -> Rlz0.Services.Strong.Realization._2014_10.RealizationManagement.ModelToModelRealizationContentResponse:
        """    
             This operation creates or updates realization content from an application model (
             referred as source model ) into another application model ( referred as target model
             ). For each realization create operation, a new realizationContainer is created,
             under which the target realized content resides. Internally each Realization will
             remember the search criteria and the configuration rules that were used on source
             model to collect a set of objects that are now being realized into the target model.
             

             The newly created objects in the target model are fully populated meaning they are
             created in persistent or static fashion. The realized model elements in the target
             model will be of same type and category as the source model objects.
             
             For example, if a Design Component (Cpd0DesignElement) of category Shape from a source
             model is realized into a target model, the object type and category of the newly
             created object in the target model will still be the same as the object in the source
             model.
             

             In case the realization content (list of model elements or a subset definition object)
             is not provided for create operation, then an empty realizationContainer object is
             created and populated in the SOA response. This realizationContainer object can be
             updated later to get the realization content.
             

             Note: Internally BMIDE deep copy rules are used to traverse and realize the source
             objects and its corresponding secondary objects. For any special behaviour on object
             traversal and action type existing deep copy rules can be updated or new deep copy
             rules can be created.
             

             Pre-Conditions:
             
             1) The source application model is with some pre-existing model content.
             
             2) Target application model already exists.
             

             Limitations:
             
             1) Partitions (Ptn0Partition) are not supported/Realized using this operation.
             

             Applications/Customers should use existing Partition Template Realization capability
             to realize partitions from one model to another.
             

Use Cases:

             To realize model elements ( coming from a Product definition application model )
             into the manufacturing application model and maintain associations between related
             objects in the source and target models for updating realized content. The cross
             domain realization or Model- Model Realization use case supports different aspects
             of the common content across different domain models. The most typical cross domain
             realization or Model- Model Realization use case supports assignment of model elements
             ( coming from a Product definition ) into the manufacturing model.
             

             The basic idea is that the realized model elements draw on all information from the
             source model elements and then add additional or override information in the realized
             model context. In terms of maturity propagation, the expectation is that this is
             controlled and when the user makes a deliberate decision to move forward to a newer
             maturity status of is source model elements, he will also make a decision to update
             the realization on the realized model elements. This allows both domains to proceed
             on their own path but still be collaborative in nature.
             

             Realizing a reuse design component, will realize all its chain of subordinate design
             components by default. This is controlled by a business object constant called RealizeReuseAndSubordinates.
             If the value of this constant is true, then reuse and its full chain of subordinates
             will be realized together, else reuse or the selected subordinate will be ignored.
             Similarly realizing a subordinate design component will realize its reuse design
             component and full chain of subordinates for that reuse design component by default.
             The same preference can be used to control this behaviour.
             

             Delete on the realization container will delete the container and its content.
             


Dependencies:

             autoAssignValues, getSaveAsDesc
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         Data on <font face="courier" height="10">RealizeModelContentInfo</font> used to create
                         or update Model to Model Realization across different application models
             
        :return: 
        """
        ...
    def GetSourceModelConfigInfo(self, TargetModelObjects: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]) -> Rlz0.Services.Strong.Realization._2014_10.RealizationManagement.SourceModelConfigResponse:
        """    
             This operation gets the configuration information of the source model element that
             was used during realization or instantiation. The input objects could be any of the
             following:
             
             1) Reuse Design Component (Rlz0ReuseDesignModelElement)
             
             2) Subordinate of a Reuse Design Component (Rlz0ReuseDesignModelElement)
             
             3) Realization container object (Rlz0ReuseModelElementInstance)
             
             4) Realized content
             

             The operation returns the list of source model object configuration information as
             a response or fails in case of error condition.
             

Use Cases:

             The getSourceModelConfigInfo operation could
             be called when user wants to fetch the Source Model Configuration information that
             was applicable during realization or instantiation. User can specify the input as
             a list of realized model elements.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param TargetModelObjects: 
                         List of the target model objects that were realized or instantiated. The operation
                         checks for the sopport of the supplied objects. This parameter is mandatory for the
                         operation and cannot be null.
             
        :return: object and returned as a partial error.
        """
        ...
    @typing.overload
    def CreateOrUpdateCompositionSubset(self, Input: Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.CompositionSubsetModelContentInfo) -> Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.M2MCompositionSubsetContentResponse: ...
    @typing.overload
    def CreateOrUpdateCompositionSubset(self, Input: Rlz0.Services.Strong.Realization._2016_05.RealizationManagement.CompositionSubsetModelContentInfo) -> Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.M2MCompositionSubsetContentResponse: ...
    def UncoupleModelRealization(self, Input: list[Rlz0.Services.Strong.Realization._2015_07.RealizationManagement.UncoupleModelRealizationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation uncouple realized  design model content from an application model
             referred as source model into another application model referred as target model.
             For each input object delete the objects in the following order Rlz0ModelRealizationMap,
             Rlz0RealizationContainer and Rlz0M2MSubsetRealization to uncouple the
             model realization.
             

Use Cases:

             To uncouple realized model elements coming from a Product definition application
             model from manufacturing application model and remove associations between related
             objects in the source and target models to avoide updating realized content.
             

             The basic idea is that the realized model elements draw on all information from the
             source model elements and then add additional or override information in the realized
             model context. In terms of maturity propagation, the expectation is that this is
             controlled and when the user makes a deliberate decision to move forward to a newer
             maturity status of is source model elements, he can also make a decision not to update
             the realization in the realized model elements using decoupling. This allows both
             domains to proceed on their own path.
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         List of UncoupleModelRealizationInputInfo objects containing the <b>Mdl0ModelElement</b>
                         or SourceModel and TargetModel  object and information stored by the caller such
                         as <font face="courier" height="10">clientID</font> for specific session.
             
        :return: 
        """
        ...
    def GetSourceItemConfigInfo(self, ElementInfos: list[Rlz0.Services.Strong.Realization._2018_06.RealizationManagement.ModelElementInfo]) -> Rlz0.Services.Strong.Realization._2018_06.RealizationManagement.SourceItemConfigResponse: ...

