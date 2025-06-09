import Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement
import Cpd0.Services.Strong.Cpdcore._2011_06.Realization
import Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand
import Cpd0.Services.Strong.Cpdcore._2012_06.DataManagement
import Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement
import Cpd0.Services.Strong.Cpdcore._2014_10.StructureExpand
import Cpd0.Services.Strong.Cpdcore._2015_07.DataManagement
import Cpd0.Services.Strong.Cpdcore._2016_05.StructureExpand
import Cpd0.Services.Strong.Cpdcore._2016_10.DataManagement
import Cpd0.Services.Strong.Cpdcore._2017_05.DataManagement
import Cpd0.Services.Strong.Cpdcore._2017_05.Realization
import Cpd0.Services.Strong.Cpdcore._2017_05.StructureExpand
import Cpd0.Services.Strong.Cpdcore._2020_01.DataManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DataManagementRestBindingStub(DataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateDesignControlElements(self, ElementInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.DesignControlElementsInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignControlElementsResponse: ...
    @typing.overload
    def CreateOrUpdateDesignElements(self, Input: Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignElementsInfo) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignElementsResponse: ...
    @typing.overload
    def CreateOrUpdateDesignElements(self, Input: Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.CreateOrUpdateDesignElementsInfo) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignElementsResponse: ...
    @typing.overload
    def CreateOrUpdateDesignFeatures(self, FeatureInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.DesignFeatureInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignFeaturesResponse: ...
    @typing.overload
    def CreateOrUpdateDesignFeatures(self, FeatureInfos: list[Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.DesignFeatureInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignFeaturesResponse: ...
    @typing.overload
    def CreateOrUpdateDesignFeatures(self, FeatureInfos: list[Cpd0.Services.Strong.Cpdcore._2015_07.DataManagement.DesignFeatureInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignFeaturesResponse: ...
    def CreateOrUpdateDesignSubsetElements(self, SubsetInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.DesignSubsetElementInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignSubsetElementsResponse: ...
    def QueryRelatedPrimaryObjects(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, InputObjects: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.RelatedObjectInput]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.RelatedObjectsResponse: ...
    def QueryRelatedSecondaryObjects(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, InputObjects: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.RelatedObjectInput]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.RelatedObjectsResponse: ...
    def SubstituteAsReuseDesignElement(self, SubstituteInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.ReuseDesignElementInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.SubstituteAsReuseDesignElementResponse: ...
    def SubstituteAsShapeDesignElement(self, SubstituteInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.ShapeDesignElementInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.SubstituteAsShapeDesignElementResponse: ...
    def CreateOrUpdateDesignControlElements2(self, ElementInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.DesignControlElementsInfo]) -> Cpd0.Services.Strong.Cpdcore._2012_06.DataManagement.CreateOrUpdateDesignControlElementsResponse2: ...
    def SubstituteAsReuseDesignElement2(self, SubstituteInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.ReuseDesignElementInfo]) -> Cpd0.Services.Strong.Cpdcore._2012_06.DataManagement.SubstituteAsReuseDesignElementResponse: ...
    def CreateOrUpdateDesignSubsetElements2(self, SubsetInfos: list[Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.DesignSubsetElementInfo2]) -> Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.CreateOrUpdateDesignSubsetElementsResponse2: ...
    def CreateOrUpdateModelToModelInstantiation(self, InstantiationInfo: Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.ModelToModelInstantiationInfo) -> Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.ModelToModelInstantiationResponse: ...
    def CreateOrUpdateDesignSubsets(self, SubsetInfos: list[Cpd0.Services.Strong.Cpdcore._2015_07.DataManagement.DesignSubsetsInfo]) -> Cpd0.Services.Strong.Cpdcore._2015_07.DataManagement.CreateOrUpdateDesignSubsetResponse: ...
    def GetProductConfigurations(self, ProductName: str, ProductNameSpace: str) -> Cpd0.Services.Strong.Cpdcore._2015_07.DataManagement.VariantCriteriaResponse: ...
    def Create4GDPreviewFromMapping(self, Input: Cpd0.Services.Strong.Cpdcore._2016_10.DataManagement.Create4GDPreviewFromMappingInfo) -> Cpd0.Services.Strong.Cpdcore._2016_10.DataManagement.Create4GDPreviewFromMappingResponse: ...
    def Create4GObjectsFromPreview(self, PreviewDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateSubsetItems(self, SubsetItemInfos: list[Cpd0.Services.Strong.Cpdcore._2017_05.DataManagement.SubsetItemInfo]) -> Cpd0.Services.Strong.Cpdcore._2017_05.DataManagement.SubsetItemsResponse: ...
    def GenerateDesignContext(self, DesignContextInfos: list[Cpd0.Services.Strong.Cpdcore._2020_01.DataManagement.GenerateDesignContextInfo]) -> Cpd0.Services.Strong.Cpdcore._2020_01.DataManagement.GenerateDesignContextResponse: ...

class DataManagementService:
    """
    
            This service contains operations for creating and editing content within a Cpd0CollaborativeDesign.
            Operations are provided for the following:
            

Create and update of Cpd0DesignElements, Cpd0DesignFeatures,
            Cpd0DesignControlElements and Cpd0DesignSubsetElements within Cpd0Worksets.
            
Create and update of Cpd0SubsetItemRevision.
            
Substitution of Cpd0DesignElement source objects (and resulting
            transition of design component category)
            
Configured navigation of relationships.
            
Generate design context.
            




Library Reference:

Cpd0SoaCpdCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DataManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateDesignControlElements(self, ElementInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.DesignControlElementsInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignControlElementsResponse:
        """    
             Creates or updates a set of design control element (Cpd0DesignControlElement)
             objects and their relations to the design components and design features that they
             conntrol.  Design control elements are used to represent welds seams (made up of
             multiple individual welds), and mechanical routings (such as piping system) which
             follow a path and are manifested by multiple design components and design features
             (welds) that make up the physical implementation of the routing.   Design control
             elements are related to the design components and design features they control via
             a relation (Cpd0ControlModel).
             
             Using this API, applications can create and update design control element (and relation)
             information in bulk, giving better through put that might not otherwise be achieved
             using standard object create and update API.
             

Cpd0ControlModel relationships have a copy stable ID which is unique within
             the scope of the design feature.  The copy stable ID can be specified on create;
             if not specified, they will be automatically generated by Teamcenter.  As their name
             suggests, when a design feature is copied the connected element relationships are
             also copied and the copy stable ID of the copied relations remains the same. The
             copy stable ID is used by external applications, like CAD, to correlate internal
             data to the related objects.
             



Use Cases:

             This API supports the design control element authoring use cases. Design control
             elements (weld seams, mechanical routings, etc.) are authored by users in a CAD application
             (versus being authored in Teamcenter RAC UI).  When the user directs the CAD system
             to save their session data, the CAD tool will invoke this API to populate
             or update the design control element information in the Teamcenter database.
             
             Note: standard delete API are used to destroy or obsolete design control elements
             that are no longer required.
             
             Use Case 1: Creation of new design control element 

             The following operation can be used for creating design control element (e.g. weld
             seams and mechanical routings) in a product design.
             

Design control elements are created always in the context of a product
             design (Cpd0CollaborativeDesign). Generally, in a production environment,
             a product design will be created ahead of time by an authorized user using the Collaborative
             Product Development application in Teamcenter RAC UI.  Applications will generally
             find an existing product design, using the Product Design saved query (provided
             OOTB in Teamcenter) or through a custom query.
             
However, for testing purposes, an application may wish to create
             a product design programmatically. To do this the createObjects operation should
             be used.
             
New design control elements can be created using operation createOrUpdateDesignControlElements.
             The application specifies the business object type for each new design control element,
             and sets the product design (found or created previously) as its modelObject.  Additional
             property and controlled element information is given and the operation invoked.
             
Design control elements have a ID which is unique within the system.
             Applications can assign their own value using the cpd0design_control_element_id
             property. If this value is not specified in the input to createOrUpdateDeisgnControlElements,
             then Teamcenter will automatically assign an ID when it creates a new design control
             element.
             
During the operation, the server creates and saves the new design
             control elements in context of the product design.  It also creates and saves the
             relationship(Cpd0ControlModel) between the design control element and the
             design components and design features it controls. The operation returns the new
             objects to the caller.
             



             Use Case 2: Update of existing design control element 

             The following operation can be used for updating existing design control element
             (e.g. weld seams and mechanical routings) in a product design.
             

Design control elements are found by the application through search
             or by navigating from a design component (Cpd0DesignElement) or design feature
             (Cpd0DesignFeature) via the control model (Cpd0ControlModel) relation.
             Note: the design control element is always the primary object of the Cpd0ConnectedElement
             relation and the design component or design feature is always the secondary object.
             
Existing design control elements can be updated using operation createOrUpdateDesignControlElements.
             The application specifies which design control elements are to be updated.  Note:
             the business object type and product design (modelObject) are not set on the input
             because they are already known to the design control element and cannot be changed.
             The application sets changed property values and specifies connected element information
             for the feature.
             
During the operation, the server updates and saves the design control
             elements and adds or removes Cpd0ConnectedElement relations to be consistent
             with the input.
             



Dependencies:

             autoAssignValues, getCreateDesc
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ElementInfos: 
                         The input set of information describing the design control elements to be created
                         or updated.
             
        :return: The response contains a map of input caller specified client ID values and the corresponding
             objects that were created/updated features ( String/Business Object reference). The
             response also contains a map of caller specified client ID values for (connected
             element) relations and their corresponding copy stable ID values. The service data
             contains a list of added, updated, or deleted objects and it also contains a list
             of any errors which occurred within the call.
        """
        ...
    @typing.overload
    def CreateOrUpdateDesignElements(self, Input: Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignElementsInfo) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignElementsResponse: ...
    @typing.overload
    def CreateOrUpdateDesignElements(self, Input: Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.CreateOrUpdateDesignElementsInfo) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignElementsResponse: ...
    @typing.overload
    def CreateOrUpdateDesignFeatures(self, FeatureInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.DesignFeatureInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignFeaturesResponse: ...
    @typing.overload
    def CreateOrUpdateDesignFeatures(self, FeatureInfos: list[Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.DesignFeatureInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignFeaturesResponse: ...
    @typing.overload
    def CreateOrUpdateDesignFeatures(self, FeatureInfos: list[Cpd0.Services.Strong.Cpdcore._2015_07.DataManagement.DesignFeatureInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignFeaturesResponse: ...
    def CreateOrUpdateDesignSubsetElements(self, SubsetInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.DesignSubsetElementInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignSubsetElementsResponse:
        """    
             This operation is used to create or update workset Subset and Design Subset Elements
             (Cpd0DesignSubsetElements) in a workset (Cpd0Workset). A Workset acts
             as a collector of design components (Cpd0DesignElements) instantiated from
             one or more Product Designs (Cpd0CollaborativeDesigns). It allows creating
             local copies of  workset subsets to update. It can contain subsets or item assemblies
             as its direct children. The subset design component content is precise and Teamcenter
             does not automatically update it with changes to the source data.
             
                         
             
             The elements to be appended or removed to/from the Workset subset can be either an
             explicit list of elements or results from a Recipe.
             

             When a designelement from a Product Design is realized into a subset in a
             
             workset, the same design component is referenced in both the Product Design and
             
             the workset. Changes made to this design component in a workset are visible in
             
             the Product Design and vice versa.
             

             Once workset subset is created using this operation, Realization Service operation
             like updateWorksetSubsetContent can be used
             to update workset subset content.
             



Use Cases:

             A design subset element is used to represent a subset of product design in a workset.
             Design Components  may be created by CAD applications or directly in the Teamcenter
             RAC UI using the Collaborative Product Development application.
             

             This API supports the workset authoring use cases. When the user directs the CAD
             system to save their session data, the CAD tool will invoke this API to populate
             or update the design subset element information in the Teamcenter database.  Similary
             RAC will call this API when search results or subset definitions are added to a workset.
             
             Note: standard delete API are used to destroy or obsolete design subset elements
             that are no longer required in the workset revision.
             

             Use Case 1: Creation of new design subset elements 


             Pre condition:  Design Components or design features exist in a product design.
             A workset revision has been created or found in Teamcenter.
             
             The following operation can be used for creating design subset elements in a workset.
             

Design subset elements are always created in the context of a workset
             revison (Cpd0WorksetRevision).  Users can create a new workset or open an
             existing workset in a CAD tool or in the Collaborative Product Development application
             in the RAC User Interface.
             
However, for testing purposes, an application may wish to create
             a workset programmatically.To do this the createObjects
             operation should be used.
             
New design subset elements can be created using the createOrUpdateDesignSubsetElements
             operation. The application specifies a workset revision which will contain the design
             subset element.Optionally, the application can specify a BOMView type; if
             none is specified the system will use the default BOM view type.
             
After the design subset element is created, the application may save
             a search recipe on the subset using the setRecipes
             operation.
             



             Use Case 2: Update of existing design subset element 


             The following operation can be used for updating an existing design subset element
             in a workset
             

Design subset elements are found by the application by expanding
             a workset (see startStructureExpand operation).
             
Design subset elements can be updated using the createOrUpdateDesignSubsetElements operation.  The application
             specifies which design subset elements are to be updated.  Note: the business object
             type, workset revision, and BOM view type are not set on the input because they are
             already known to the design subset element and cannot be changed.
             
The application sets changed property values.
             
During the createOrUpdateDesignElements
             operation, the server updates and saves the design components along with its auxiliary
             objects if any.
             


             Note: The search recipe on design subset elements is normally changed using the setRecipes operation. The createOrUpdateDesignElements supports limited recipe modification
             indirectly by adding lists of design components for inclusion or exclusion from the
             current search recipe stored on the design subset element.
             

Dependencies:

             createOrUpdateDesignElements, updateWorksetSubsetContent
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubsetInfos: 
                         Data on <font face="courier" height="10">DesignSubsetElementInfo</font> used to create
                         or update <font face="courier" height="10">DesignSubsetElements</font> in a workset.
             
        :return: .
        """
        ...
    def QueryRelatedPrimaryObjects(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, InputObjects: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.RelatedObjectInput]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.RelatedObjectsResponse:
        """    
             Query, filter, and configure all primary objects attached to the given input set
             of secondary objects.  Filter criteria are provided through the RelatedObjectInput construct.  Filtering can be based on the type
             of the relation, the type of the related object, and relation attribute values.
             Configuration conditions are specified by a ConfigurationContext object, which
             provides revision and unit effectivity rule information.
             
             Returned objects are configured by the given configuration context and are access
             checked before being returned. An empty vector of RelatedObjectInput
             results in an invalid input exception being thrown.
             
RESTRICTION:  Currently this API is only supported for navigation of Mdl0CopyStableRelation
             and its subtypes.
             



Use Cases:

             This API supports configured navigation of relationship. Some applications, such
             as CAD tools, need to navigate relationships and return results only if they match
             certain configuration criteria. An example is the navigation from a design component
             to a design control element.  A design component  may be related to multiple revisions
             of a design control element, however within a configured view of the system, only
             one of the design control elements may actually be relevant.  This API helps find
             the primary object (e.g. Cpd0DesignControlElement) of a relation (e.g. Cpd0ControlModel)
             given a secondary object (e.g. Cpd0DesignElement).
             

             Use Case 1: Navigate to Configured Design Control Elements from Design Component
             



Perform a configured search to find design components (Cpd0DesignElement)
             in a product design
             
Using operation queryRelatedPrimaryObjects
             to find the design control elements (Cpd0DesignControlElement) that are related
             to the found design components and match the same configuration criteria used to
             find the design components.
             


             Use Case 2: Navigate to Configured Design Features from Design Component 



Perform a configured search to find design components (Cpd0DesignElement)
             in a product design
             
Using operation queryRelatedPrimaryObjects to find the design features
             (Cpd0DesignFeature) that are related (via Cpd0ConnectedElement) to
             the found design components and match the same configuration criteria used to find
             the design components.
             



Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ConfigurationContext: 
                         Configuration criteria to apply to the filtered set of related primary objects.
                         Objects not satisfying the configuration criteria will not be returned.
             
        :param InputObjects: 
                         A set of secondary objects and the filter criteria.
             
        :return: results in an invalid
             input exception being thrown.
        """
        ...
    def QueryRelatedSecondaryObjects(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, InputObjects: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.RelatedObjectInput]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.RelatedObjectsResponse:
        """    
             Query, filter, and configure all secondary objects attached to the given input set
             of primary objects.  Filter criteria are provided through the RelatedObjectInput construct.  Filtering can be based on the type
             of the relation, the type of the related object, and relation property values. Configuration
             conditions are specified by a ConfigurationContext object, which provides
             revision and unit effectivity rule information.
             
             Returned objects are configured by the given configuration context and are access
             checked before being returned. An empty vector of RelatedObjectInput
             results in an invalid input exception being thrown.
             
RESTRICTION:  Currently this API is only supported for navigation of Mdl0CopyStableRelation
             and its subtypes.
             


Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ConfigurationContext: 
                         Configuration criteria to apply to the filtered set of related secondary objects.
                         Objects not satisfying the configuration criteria will not be returned.
             
        :param InputObjects: 
                         A set of primary objects and the filter criteria.
             
        :return: 
        """
        ...
    def SubstituteAsReuseDesignElement(self, SubstituteInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.ReuseDesignElementInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.SubstituteAsReuseDesignElementResponse:
        """    
             Transforms an existing shape or promissory Design Components (Cpd0DesignElement
             or its subclasses) to reuse Design Components (Cpd0DesignElement or
             its subtypes).This operation doesnt replace the existing Design Component business
             object reference with a new one rather, changes category to reuse.The business
             object reference still remains the same. In other words, the object identity (UID)
             and the cpd0design_element_id property value
             on Design Component remain the same after the substitution.
             

Use Cases:

             Use Case 1: This operation can be used when a promissory Design Component
             is to be transformed into a reuse Design Component.
             
             Use Case 2: This operation can be used when a shape Design Component is to
             be transformed into a reuse Design Component.
             


Dependencies:

             createOrUpdateDesignElements
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubstituteInfos: 
                         substituteInfos: A vector of <b>ReuseDesignElementInfo</b> structures. Each structure
                         specifies the Design Component to be substituted. Each would have inputs on Item
                         Revision to be realized for substitution.
             
        :return: 
        """
        ...
    def SubstituteAsShapeDesignElement(self, SubstituteInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.ShapeDesignElementInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.SubstituteAsShapeDesignElementResponse:
        """    
             Transforms an existing reuse or promissory design components ( Cpd0DesignElement
             or its subtypes) to shape design components ( Cpd0DesignElement or
             its subtypes) .Substitute operation doesnt replace the existing design component
             with a new one. The existing design component gets morphed. The category is changed
             from reuse (or promissory) to shape. In other words, the object
             identity (UID) and the cpd0design_element_id property value on Design Component remain
             the same after the substitution.
             

Use Cases:

             Use Case 1: This operation can be used when a promissory Design Component
             is to be transformed into a shape Design Component.
             
             Use Case 2: This operation can be used when a reuse Design Component is to
             be transformed into a shape Design Component. In this case any of its subordinate
             Design Components are discarded as part of the substitution.
             


Dependencies:

             createOrUpdateDesignElements
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubstituteInfos: 
                         A list of <font face="courier" height="10">ShapeDesignElementInfo</font> structures.
                         Each structure specifies the Design Component to substitute and also the new shape
                         information for the substitution.
             
        :return: SubstituteAsShapeDesignElementResponse contains a map of client id (provided in input)
             to the Shape Design Component. It has a map of Shape Design Components to the corresponding
             Shape Design and Shape Design Revision objects. It has Service Data with created/updated/deleted
             objects along with any partial errors.
        """
        ...
    def CreateOrUpdateDesignControlElements2(self, ElementInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.DesignControlElementsInfo]) -> Cpd0.Services.Strong.Cpdcore._2012_06.DataManagement.CreateOrUpdateDesignControlElementsResponse2:
        """    
             Creates or updates a set of design control element (Cpd0DesignControlElement)
             objects and their relations to the design components and design features that they
             conntrol.  Design control elements are used to represent welds seams (made up of
             multiple individual welds), and mechanical routings (such as piping system) which
             follow a path and are manifested by multiple design components and design features
             (welds) that make up the physical implementation of the routing.   Design control
             elements are related to the design components and design features they control via
             a relation (Cpd0ControlModel).     Using this API, applications can create
             and update design control element (and relation) information in bulk, giving better
             through put that might otherwise be achieved using standard object create and update
             API. Cpd0ControlModel relationships have a copy-stable ID which is unique
             within the scope of the design feature.  The copy-stable ID can be specified on create;
             if not specified, they will be automatically generated by Teamcenter.  As their name
             suggests, when a design feature is copied the connected element relationships are
             also copied and the copy-stable ID of the copied relations remains the same.  The
             copy-stable ID is used by external applications, like CAD, to correlate internal
             data to the related objects.@param elementInfos The input set of information describing
             the design control elements to be created or updated.@return response containing
             maps of input information to the created/updated objects (see description of CreateOrUpdateDesignControlElementsResponse
             for more details).
             

Use Cases:

             This API supports the design control element authoring use cases. Design control
             elements (weld seams, mechanical routings, etc.) are authored by users in a CAD application
             (versus being authored in Teamcenter RAC UI).  When the user directs the CAD system
             to save their session data, the CAD tool will invoke this API to populate or update
             the design control element information in the Teamcenter database.
             
             Note: standard delete API are used to destroy or obsolete design control elements
             that are no longer required.
             
             Use Case 1: Creation of new design control element
             
             The following operation can be used for creating design control element (e.g. weld
             seams and mechanical routings) in a product design.
             
             Design control elements are created always in the context of a product design (Cpd0CollaborativeDesign).
             Generally, in a production environment, a product design will be created ahead of
             time by an authorized user using the Collaborative Product Development application
             in Teamcenter RAC UI.  Applications will generally find an existing product design,
             using the Product Design saved query (provided OOTB in Teamcenter) or through a custom
             query.
             
             However, for testing purposes, an application may wish to create a product design
             programmatically. To do this the createObjects operation should be used.
             
             New design control elements can be created using operation createOrUpdateDesignControlElements.
             The application specifies the business object type for each new design control element,
             and sets the product design (found or created previously) as its modelObject.  Additional
             property and controlled element information is given and the operation invoked.
             
             Design control elements have a ID which is unique within the system.  Applications
             can assign their own value using the cpd0design_control_element_id property. If this
             value is not specified in the input to createOrUpdateDeisgnControlElements, then
             Teamcenter will automatically assign an ID when it creates a new design control element.
             
             During the operation, the server creates and saves the new design control elements
             in context of the product design.  It also creates and saves the relationship(Cpd0ControlModel)
             between the design control element and the design components and design features
             it controls. The operation returns the new objects to the caller.
             

             Use Case 2: Update of existing design control element
             
             The following operation can be used for updating existing design control element
             (e.g. weld seams and mechanical routings) in a product design.
             
             Design control elements are found by the application through search or by navigating
             from a design component (Cpd0DesignElement) or design feature (Cpd0DesignFeature)
             via the control model (Cpd0ControlModel) relation.  Note: the design control element
             is always the primary object of the Cpd0ConnectedElement relation and the design
             component or design feature is always the secondary object.
             
             Existing design control elements can be updated using operation createOrUpdateDesignControlElements.
             The application specifies which design control elements are to be updated.  Note:
             the business object type and product design (modelObject) are not set on the input
             because they are already known to the design control element and cannot be changed.
             The application sets changed property values and specifies connected element information
             for the feature.
             
             During the operation, the server updates and saves the design control elements and
             adds or removes Cpd0ConnectedElement relations to be consistent with the input.
             

Dependencies:

             autoAssignValues, getCreateDesc
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ElementInfos: 
                         The input set of information describing the design control elements to be created
                         or updated.
             
        :return: The response contains a map of input caller specified client ID values and the corresponding
             <tt>CreateOrUpdateDesignControlElementOutput</tt>. The service data contains
             a list of added, updated, or deleted objects and it also contains a list of any errors
             which occurred within the call.  See the description of <tt>CreateOrUpdateDesignControlElementsResponse2</tt>
             for additional details.
        """
        ...
    def SubstituteAsReuseDesignElement2(self, SubstituteInfos: list[Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.ReuseDesignElementInfo]) -> Cpd0.Services.Strong.Cpdcore._2012_06.DataManagement.SubstituteAsReuseDesignElementResponse:
        """    
             Transforms an existing reuse or promissory design components ( Cpd0DesignElement
             or its subtypes) to shape design components ( Cpd0DesignElement or its subtypes)
             .Substitute operation doesnt replace the existing design component with a new one.
             The existing design component gets morphed. The category is changed from reuse (or
             promissory) to shape. In other words, the object identity (UID) and the cpd0design_element_id
             property value on Design Component remain the same after the substitution.
             

Use Cases:

             Use Case 1: This operation can be used when a promissory Design Component is to be
             transformed into a shape Design Component.
             
             Use Case 2: This operation can be used when a reuse Design Component is to be transformed
             into a shape Design Component. In this case any of its subordinate Design Components
             are discarded as part of the substitution.
             


Dependencies:

             createOrUpdateDesignControlElements2
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubstituteInfos: 
                         A vector of ReuseDesignElementInfo structures. Each structure specifies the Design
                         Component to be substituted. Each would have inputs on Item Revision to be realized
                         for substitution.
             
        :return: SubstituteAsShapeDesignElementResponse contains a map of client id (provided in input)
             to the Shape Design Component. It has a map of Shape Design Components to the corresponding
             Shape Design and Shape Design Revision objects. It has Service Data with created/updated/deleted
             objects along with any partial errors.
        """
        ...
    def CreateOrUpdateDesignSubsetElements2(self, SubsetInfos: list[Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.DesignSubsetElementInfo2]) -> Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.CreateOrUpdateDesignSubsetElementsResponse2:
        """    
             The differences between this operation and createOrUpdateDesignSubsetElements
             are:
             
             1) The input structures relaxes the restriction on appendSourceElements,
             removeSourceElements, and subordinateSourceElements to be Mdl0ConditionalElement
             objects instead of Mdl0PositionedModelElement.  Same restriction is removed
             from the returned output data.
             
             2) The sourceModel can be specified to be
             a Baseline Revision in place of the usual Product Design. In this case the content
             of the Design Subset Element will scoped by the Baseline content.
             

             This operation is used to create or update workset Subset and Design Subset Elements
             (Cpd0DesignSubsetElements) in a workset (Cpd0Workset). A Workset acts
             as a collector of design components (Cpd0DesignElements) instantiated from
             one or more Product Designs (Cpd0CollaborativeDesigns). It allows creating
             local copies of  workset subsets to update. It can contain subsets or item assemblies
             as its direct children. The subset design component content is precise and Teamcenter
             does not automatically update it with changes to the source data.
             
                         
             
             The elements to be appended or removed to/from the Workset subset can be either an
             explicit list of elements or results from a Recipe.
             

             When a designelement from a Product Design is realized into a subset in a
             
             workset, the same design component is referenced in both the Product Design and
             
             the workset. Changes made to this design component in a workset are visible in
             
             the Product Design and vice versa.
             

             Once workset subset is created using this operation, Realization Service operation
             like updateWorksetSubsetContent can be used to update workset subset content.
             



Use Cases:

             A design subset element is used to represent a subset of product design in a workset.
             Design Components  may be created by CAD applications or directly in the Teamcenter
             RAC UI using the Collaborative Product Development application.
             

             This API supports the workset authoring use cases. When the user directs the CAD
             system to save their session data, the CAD tool will invoke this API to populate
             or update the design subset element information in the Teamcenter database.  Similary
             RAC will call this API when search results or subset definitions are added to a workset.
             
             Note: standard delete API are used to destroy or obsolete design subset elements
             that are no longer required in the workset revision.
             

             Use Case 1: Creation of new design subset elements 


             Pre condition:  Design Components or design features exist in a product design.
             A workset revision has been created or found in Teamcenter.
             
             The following operation can be used for creating design subset elements in a workset.
             

Design subset elements are always created in the context of a workset
             revison (Cpd0WorksetRevision).  Users can create a new workset or open an
             existing workset in a CAD tool or in the Collaborative Product Development application
             in the RAC User Interface.
             
However, for testing purposes, an application may wish to create
             a workset programmatically.To do this the createObjects operation should be used.
             
New design subset elements can be created using the createOrUpdateDesignSubsetElements
             operation. The application specifies a workset revision which will contain the design
             subset element.Optionally, the application can specify a BOMView type; if
             none is specified the system will use the default BOM view type.
             
After the design subset element is created, the application may save
             a search recipe on the subset using the setRecipes operation.
             



             Use Case 2: Update of existing design subset element 


             The following operation can be used for updating an existing design subset element
             in a workset
             

Design subset elements are found by the application by expanding
             a workset (see startStructureExpand operation).
             
Design subset elements can be updated using the createOrUpdateDesignSubsetElements
             operation.  The application specifies which design subset elements are to be updated.
             Note: the business object type, workset revision, and BOM view type are not set
             on the input because they are already known to the design subset element and cannot
             be changed.
             
The application sets changed property values.
             
During the createOrUpdateDesignElements operation, the server updates
             and saves the design components along with its auxiliary objects if any.
             


             Note: The search recipe on design subset elements is normally changed using the setRecipes
             operation. The createOrUpdateDesignElements supports limited recipe modification
             indirectly by adding lists of design components for inclusion or exclusion from the
             current search recipe stored on the design subset element.
             

Dependencies:

             createOrUpdateDesignElements, updateWorksetSubsetContent
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubsetInfos: 
                         Data on <font face="courier" height="10">DesignSubsetElementInfo</font> used to create
                         or update <font face="courier" height="10">DesignSubsetElements</font> in a workset.
             
        :return: A list of DesignSubsetElementData2 which is one to one correspondence with input
             subsetInfos.
        """
        ...
    def CreateOrUpdateModelToModelInstantiation(self, InstantiationInfo: Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.ModelToModelInstantiationInfo) -> Cpd0.Services.Strong.Cpdcore._2014_10.DataManagement.ModelToModelInstantiationResponse:
        """    
             The operation Instantiates model content (Design Model Elements) from one application
             model into another application model thereby creating a new "modelreuse" and "subordinate"
             states of subtypes of design model elements (Cpd0DesignModelElement) in the target
             model. Source model can be an Application Model (Mdl0ApplicationModel) or a Subset
             Definition (Mdl0SubsetDefinition). Each Target object (subordinate) in target model
             refers to a corresponding source object in the source model, allowing for an update
             of the target model.
             

             The newly created objects in the target model are fully populated meaning they are
             persistently created in the context of the source model and will have a different
             life cycle than the related objects in the source model. The category of the realized
             model elements in the target model is always "subordinate". For example, a Design
             Component (Cpd0DesignElement) of category shape from a source model is realized into
             a target model,  the category of the newly created object in the target model will
             be set to 'subordinate'.
             



Use Cases:

             Model to Model Instantiation use case supports applications to re-use a smaller models
             to build larger models.  For example, instantiating an engine assembly into a car
             assembly.
             

             Note:
             
             1. If the object type of the newly created target object has to be different from
             source object types then it is application's responsibility to manage any such mappings
             through extension points provided by the infrastructure.
             
             2.    If the source model contain a "reuse" design component,
             then all its subordinate design components will be instanced. This behaviour is controlled
             by a business object contants called "instReuseAlongWithSubordinates". If the value
             of this constant is true, then reuse and its full chain of subordinates will be cloned
             togther, else reuse or the selected subordinate will be ignored.
             

             Limitations:
             

             1. Partitions are not supported types for Model to Model Instantiation.
             
             2.    Subordinate elements (without its chain of parenst and
             its reuse) are not supported to be realized into the target model independently.
             






Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param InstantiationInfo: 
                         A structure of <i>ModelToModelInstantiationInfo</i> representing the vector of InstantiationObjectInfo
                         for the instantiation of model content from source Application Model (source) to
                         target Application Model and a vector of <i>UpdateInstantiationContentInfo</i> used
                         to update the reuse DesignElement. OR Data on <i>ModelToModelInstantiationInfo</i>
                         used to create or update Model to Model Instantiation across different Application
                         Models.
             
        :return: Response from the service SOA which can be used to store and return the 'InstantiatedObjectsData'
             and the common 'ServiceData' to the caller of the service. Please see the description
             for more information on 'InstantiatedObjectsData'.
        """
        ...
    def CreateOrUpdateDesignSubsets(self, SubsetInfos: list[Cpd0.Services.Strong.Cpdcore._2015_07.DataManagement.DesignSubsetsInfo]) -> Cpd0.Services.Strong.Cpdcore._2015_07.DataManagement.CreateOrUpdateDesignSubsetResponse:
        """    
             The difference between createOrUpdateDesignSubsets and createOrUpdateDesignSubsetElements2
             is:
             
             1) The input structure has an additional applyTargetPropertiesToElements attribute,
             which contains list of elements on which target properties needs to be applied from
             subset default. Following target properties on Subset Defaults will be read: Effectivity,
             Variant and Partitions.
             
             2) The response contains contentObjInfoInContextMap, a map of (Model Element, Model
             Element) giving the Cpd0InfoInContext attribute group for each of the Design
             Subset Element's content. The content object is the key, its corresponding attribute
             group object is the value.
             

             This operation creates or updates Design Subset Elements (Cpd0DesignSubsetElements)
             in a workset (Cpd0Workset). A Workset acts as a collector of design components
             (Cpd0DesignElements) instantiated from one or more Product Designs (Cpd0CollaborativeDesigns).
             It allows creating local copies of workset subsets to update. It can contain subsets
             or item assemblies as its direct children. The subset design component content is
             precise and Teamcenter does not automatically update it with changes to the source
             data.
             

             The elements to be appended or removed to/from the subset can be either an explicit
             list of elements or results from a Recipe.
             

             Once a subset is created using this operation, Realization Service operations like
             updateWorksetSubsetContent can be used to update the subset content of a workset.
             


Use Cases:

             A design subset element is used to represent a subset of product design in a workset.
             Design Components  may be created by CAD applications or directly in the Teamcenter
             RAC UI using the Collaborative Product Development application.
             

             This API supports the workset authoring use cases. When the user directs the CAD
             system to save their session data, the CAD tool will invoke this API to populate
             or update the design subset element information in the Teamcenter database.  Similary
             RAC will call this API when search results or subset definitions are added to a workset.
             
             Note: standard delete API are used to destroy or obsolete design subset elements
             that are no longer required in the workset revision.
             

             Use Case 1: Creation of new design subset elements 


             Pre condition:  Design Components or design features exist in a product design.
             A workset revision has been created or found in Teamcenter.
             
             The following operation can be used for creating design subset elements in a workset.
             

Design subset elements are always created in the context of a workset
             revison (Cpd0WorksetRevision).  Users can create a new workset or open an
             existing workset in a CAD tool or in the Collaborative Product Development application
             in the RAC User Interface.
             
However, for testing purposes, an application may wish to create
             a workset programmatically.To do this the createObjects operation should be used.
             
New design subset elements can be created using the createOrUpdateDesignSubsetElements
             operation. The application specifies a workset revision which will contain the design
             subset element.Optionally, the application can specify a BOMView type; if
             none is specified the system will use the default BOM view type.
             
After the design subset element is created, the application may save
             a search recipe on the subset using the setRecipes operation.
             



             Use Case 2: Update of existing design subset element 


             The following operation can be used for updating an existing design subset element
             in a workset
             

Design subset elements are found by the application by expanding
             a workset (see startStructureExpand operation).
             
Design subset elements can be updated using the createOrUpdateDesignSubsetElements
             operation.  The application specifies which design subset elements are to be updated.
             Note: the business object type, workset revision, and BOM view type are not set
             on the input because they are already known to the design subset element and cannot
             be changed.
             
The application sets changed property values.
             
During the createOrUpdateDesignElements operation, the server updates
             and saves the design components along with its auxiliary objects if any.
             


             Note: The search recipe on design subset elements is normally changed using the setRecipes
             operation. The createOrUpdateDesignElements supports limited recipe modification
             indirectly by adding lists of design components for inclusion or exclusion from the
             current search recipe stored on the design subset element.
             

Dependencies:

             createOrUpdateDesignElements, updateWorksetSubsetContent
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubsetInfos: 
                         Data on DesignSubsetsInfo used to create or update DesignSubsetElements in a workset.
             
        :return: 
        """
        ...
    def GetProductConfigurations(self, ProductName: str, ProductNameSpace: str) -> Cpd0.Services.Strong.Cpdcore._2015_07.DataManagement.VariantCriteriaResponse:
        """    
             This operation returns a set of product configurations managed at the configurator
             level, e.g. for product tracking or reporting purposes.
             
             Teamcenter variant configurators manage product configurations as VariantRules
             which are attached to an ItemRevision representing the product using any relationship
             type (see also preference TC_Default_SVR_Relationship). The product is identified
             by productName and productNameSpace parameters. Teamcenter configurators
             use the ID of the product item for productName, and the revision ID for productNameSpace.
             The identifiers of the product associated with a Product Design (Cpd0CollaborativeDesign)
             can be obtained from properties Mdl0ApplicationModel::get_mdl0var_conf_prod_name
             and Mdl0ApplicationModel::get_mdl0var_conf_prod_namespace.
             
getProductConfigurations returns both the old style and the new style variant
             rules attached to the item
             

Use Cases:

             An engineering project administrator has created a product ItemRevision. A
             manufacturing engineering user creates and maintains VariantRules that represent
             a set of configurations for prototype builds. The project administrator attaches
             these VariantRules to the product ItemRevision. Product engineering
             users can use operation getProductConfigurations to review existing prototype
             configurations. The user can then chose one of the configurations to initialize variant
             configuration criteria with operation setVariantCriteria.
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ProductName: 
                         Identifies the product. It is used in conjunction with parameter <i>productNameSpace</i>
                         to resolve potential ambiguity in variant option value names, and to identify product
                         context specific constraints. Teamcenter configurators use a Multiple Field Key (MFK)
                         stable identifier (see property Item::fnd0VariantNamespace) of the product item for
                         productName. The productName value for a Product Design (<b>Cpd0CollaborativeDesign</b>)
                         can be obtained from property <i>Mdl0ApplicationModel::mdl0config_product_name</i>.
             
        :param ProductNameSpace: 
                         Specifies the namespace for the product identifier. It is used in conjunction with
                         parameter <i>productName</i> to resolve potential ambiguity in variant option value
                         names, and to identify product context specific constraints. Teamcenter configurators
                         use the Revision ID of the product ItemRevision for productNameSpace. The productNameSpace
                         value for a Product Design (<b>Cpd0CollaborativeDesign</b>) can be obtained from
                         property <i>Mdl0ApplicationModel::mdl0config_prod_namespace</i>.
             
        :return: :  The Product Name and Product Namespace must not be empty.
        """
        ...
    def Create4GDPreviewFromMapping(self, Input: Cpd0.Services.Strong.Cpdcore._2016_10.DataManagement.Create4GDPreviewFromMappingInfo) -> Cpd0.Services.Strong.Cpdcore._2016_10.DataManagement.Create4GDPreviewFromMappingResponse: ...
    def Create4GObjectsFromPreview(self, PreviewDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateOrUpdateSubsetItems(self, SubsetItemInfos: list[Cpd0.Services.Strong.Cpdcore._2017_05.DataManagement.SubsetItemInfo]) -> Cpd0.Services.Strong.Cpdcore._2017_05.DataManagement.SubsetItemsResponse:
        """    
             This operation creates or updates Cpd0SubsetItemRevision based on input structure
             SubsetItemInfo. A Cpd0SubsetItemRevision
             is a subclass of ItemRevision used to represent a subset of Cpd0CollaborativeDesign.
             

             A Cpd0DesignElement represents the use of a standard part design, a design
             component, or a design assembly in a product. A reuse Cpd0DesignElement
             instances the assembly into a Cpd0CollaborativeDesign and the subordinates
             which result by the realization process using the Collaborative Product Development
             application.
             

Reuse, subordinate, and shape Cpd0DesignElement classes
             all represent occurrences of Items in the Cpd0CollaborativeDesign.
             As such they can be mapped to PSOccurrence in a structure below the new Cpd0SubsetItemRevision.
             Cpd0DesignFeature and Cpd0DesignElement having a categories promissory and modelreuse are not supported.
             

Cpd0SubsetItem can be created independent of Cpd0Workset. It cannot
             be a child of Cpd0Workset but it can be child of an Item.
             

             The content in a Cpd0SubsetItemRevision will be manifested as traditional
             BOMViewRevision structure upon recipe execution. The mapping functionality
             creates occurrences below the Cpd0SubsetItemRevision in one-to-one correspondence
             with Cpd0DesignElement corresponding to content selected by Cpd0SubsetItemRevision.    
             

             The search recipe on Cpd0SubsetItemRevision is normally changed using the
             setRecipes operation. The createOrUpdateSubsetItems supports limited recipe modification
             indirectly by adding lists of Cpd0DesignElements for inclusion or exclusion
             from the current search recipe stored on the  Cpd0SubsetItem.
             

Use Cases:

             This API supports the Cpd0SubsetItemRevision authoring use cases. New Cpd0SubsetItemRevision
             objects require creation of a new Cpd0SubsetItem and Cpd0SubsetItemInstance
             objects.
             

             Use Case 1: Creation of new Cpd0SubsetItem


             Pre condition: Cpd0DesignElement exist in a Cpd0CollaborativeDesign.
             
             The following operation can be used for creating Cpd0SubsetItems


New Cpd0SubsetItem can be created using the createOrUpdateSubsetItems operation.
             
After the Cpd0SubsetItem is created, the application may save
             a search recipe on the Cpd0SubsetItemRevision using the setRecipes operation.
             



             Use Case 2: Update of existing Cpd0SubsetItemRevision


             The following operation can be used for updating an existing Cpd0SubsetItemRevision.
             

Cpd0SubsetItemRevision can be updated using the createOrUpdateSubsetItems operation. The application specifies
             which Cpd0SubsetItemRevisions are to be updated.
             
The application sets changed property values.
             



Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubsetItemInfos: 
                         A list of <font face="courier" height="10">SubsetItemInfo</font> structure. Each
                         structure specifies the <b>Cpd0SubsetItemRevision</b> to be created or updated.
             
        :return: 
        """
        ...
    def GenerateDesignContext(self, DesignContextInfos: list[Cpd0.Services.Strong.Cpdcore._2020_01.DataManagement.GenerateDesignContextInfo]) -> Cpd0.Services.Strong.Cpdcore._2020_01.DataManagement.GenerateDesignContextResponse:
        """    
             This operation creates a Cpd0Workset or Item with a list of Cpd0DesignSubsetElements
             for each GenerateDesignContextInfo and returns
             the Cpd0Workset or Item objects.
             

Use Cases:

Generate Design Context:

             Generates design contexts for a list of ItemRevision objects and Cpd0DesignElement
             objects.
             

Application finds the source ItemRevision objects of the input
             Cpd0DesignElement objects.
             
Application finds the corresponding Item object for each of the input
             ItemRevision objects and the above source ItemRevision objects.
             
Application finds all the ItemRevision objects of the above
             Item objects.
             
Application finds the realized Cpd0DesignElement objects of
             above ItemRevision objects.
             
Application performs a proximity search on the input subordinate
             Cpd0DesignElement objects.
             
All Cpd0DesignElement objects are grouped based on unique
             configuration per collaborative design.
             
For each group of Cpd0DesignElement objects, a subset is created.
             A recipe is also created and set on the subset. The recipe adds all Cpd0DesignElement
             objects in the group to the subset.
             
Application creates a Cpd0Workset or Item object and
             puts all newly created Cpd0DesignSubsetElement objects in it.
             
Application returns the Cpd0Workset or Item.
             




Generate Design Context for Change Item Revision:

             Generates design context for a list of ChangeItemRevisions:
             

Application finds the ItemRevision objects and Cpd0DesignElement
             objects attached to ChangeItemRevision objects through a relation defined
             by the preference ChangeItemRevision_Design_Item_default_relation.
             
Application finds source ItemRevision objects of above Cpd0DesignElement
             objects.
             
Application finds the Item objects of above ItemRevision objects
             and source ItemRevision objects.
             
Application finds all ItemRevision objects of the above Item
             objects.
             
Application finds the realized Cpd0DesignElement objects of
             above ItemRevision objects.
             
Application performs a proximity search on the input subordinate
             Cpd0DesignElement objects.
             
All Cpd0DesignElement objects are grouped based on unique
             configuration per collaborative design.
             
For each group of Cpd0DesignElement objects, a subset is created.
             A recipe is also created and set on the subset. The recipe adds all Cpd0DesignElement
             objects in the group to the subset.
             
Application creates a Cpd0Workset or Item object and puts
             all newly created Cpd0DesignSubsetElement objects in it.
             
Application returns the Cpd0Workset or Item object.
             



Generate Design Context with Reuse Cpd0DesignElements:

             Generates design context for a list of ItemRevision and Cpd0DesignElement
             objects.
             

Application finds the realized Cpd0DesignElement objects of
             the ItemRevision objects.
             
Application finds the reuse Cpd0DesignElement objects of the
             above Cpd0DesignElement objects and the input Cpd0DesignElement objects.
             
Application finds the source ItemRevision objects of the reuse
             Cpd0DesignElement objects.
             
Application finds the Item objects of the above ItemRevision
             objects.
             
Application finds all ItemRevision objects of the above Item
             objects.
             
Application finds reuse Cpd0DesignElement objects of the above
             ItemRevision objects and subordinate Cpd0DesignElement objects for
             the reuse.
             
All Cpd0DesignElement objects are grouped based on unique
             configuration per collaborative design.
             
For each group of Cpd0DesignElement objects, a subset is created.
             A recipe is also created and set on the subset. The recipe adds all Cpd0DesignElement
             objects in the group to the subset.
             
Application creates a Cpd0Workset or Item object and puts
             all newly created Cpd0DesignSubsetElement objects in it.
             
Application returns the Cpd0Workset or Item object.
             



Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param DesignContextInfos: 
                         The operation takes in a list of GenerateDesignContextInfo, creates a workset or
                         item with a list of subsets in it each GenerateDesignContextInfo and returns the
                         worksets and items.
             
        :return: 
        """
        ...

class RealizationRestBindingStub(RealizationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def UpdateWorksetSubsetContent(self, Input: list[Cpd0.Services.Strong.Cpdcore._2011_06.Realization.UpdateWorksetSubsetContentInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.Realization.UpdateWorksetSubsetContentResponse: ...
    def UpdateSubsetsContent(self, SubsetContentInfos: list[Cpd0.Services.Strong.Cpdcore._2017_05.Realization.SubsetContentInfo]) -> Cpd0.Services.Strong.Cpdcore._2017_05.Realization.SubsetContentsResponse: ...

class RealizationService:
    """
    
            This service exposes operations pertaining to update Realization of objects instantiated
            under workset revision.
            
            It contains model configuration statements needed to specify how a source model (e.g.
            product design) should be configured prior to being realized.   It also contains
            a recipe which describes what content from the source model should be selected for
            processing.  The recipe can contain criteria for object attributes, spatial proximity,
            and for partition membership.
            
            .
            

Dependencies:

            DataManagement
            


Library Reference:

Cpd0SoaCpdCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> RealizationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def UpdateWorksetSubsetContent(self, Input: list[Cpd0.Services.Strong.Cpdcore._2011_06.Realization.UpdateWorksetSubsetContentInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.Realization.UpdateWorksetSubsetContentResponse:
        """    
             This operation is used to check for any updates in the source model(Product Design)
             that have occurred since the last realization update and reflects any of those changes
             correspondingly in the target model( Workset Model).  The list of added, updated,
             and removed content will be returned for each realization input.  If the executeRecipe flag is set to false, the recipe will not
             be reexecuted for a recipe based realizations.
             

Use Cases:

             A design subset element is used to represent a subset of product design in a workset.
             Design Components may be created by CAD applications or directly in the Teamcenter
             RAC user interface using the Collaborative Product Development application.
             

             This API supports workset authoring use cases; specifically, it is used when the
             user wishes to update the content of a subset by reexecuting its search recipe.
             

             Use Case : Update selected content of existing design subset elements 


             The following operation can be used for updating an existing design subset element
             in a workset
             

Design subset elements are found by the application by expanding
             a workset (see startStructureExpand operation).
             
The set of content referenced by design subset elements can be updated
             by reexecuting the search recipe. This is done by using the updateWorksetSubsetContent operation. The application specifies
             which design subset elements should have their set of selected content updated.
             
During the updateWorksetSubsetContent
             operation, the server will find the set of product design content that satisfies
             the search criteria.This set of objects will be updated on the design subset element,
             and will remain static until the next call to updateWorksetSubsetContent.
             
Note: The search recipe on design subset elements is normally changed
             using the setRecipes operation. The updateWorksetSubsetContent can be called after
             setRecipes in order to update the workset
             based on the new/modified search recipe.
             



Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param Input: 
                         set of realizations to update.
             
        :return: UpdateWorksetSubsetContentResponse contains a vector of set of design model elements.
        """
        ...
    def UpdateSubsetsContent(self, SubsetContentInfos: list[Cpd0.Services.Strong.Cpdcore._2017_05.Realization.SubsetContentInfo]) -> Cpd0.Services.Strong.Cpdcore._2017_05.Realization.SubsetContentsResponse:
        """    
             This operation is used to check for any updates in the source model i.e. Cpd0CollaborativeDesign
             that have occurred since the last realization update. The list of added, updated,
             and removed content will be returned for each realization input. If the executeRecipe flag is false, the recipe will not be re-executed
             for a recipe based realizations.
             

             This API supports updating content of Cpd0SubsetItemRevision or Cpd0DesignSubsetElement.
             

Cpd0DesignSubsetElement is used to represent a subset of Cpd0CollaborativeDesign
             in a Cpd0Workset. Cpd0DesignSubsetElement objects may be created by
             CAD applications or directly in the Teamcenter RAC user interface using the Collaborative
             Product Development application.
             

Cpd0SubsetItemRevision is a subclass of ItemRevision used to represent
             a subset of Cpd0CollaborativeDesign. Cpd0SubsetItem can be created
             independent of Cpd0Workset. It cannot be a child of Cpd0Workset but
             it can be child of an Item.
             

             The content in a Cpd0SubsetItemRevision will be manifested as traditional
             BOMViewRevision structure upon recipe execution. The mapping functionality
             creates occurrences below the Cpd0SubsetItemRevision in one-to-one correspondence
             with Cpd0DesignElement corresponding to content selected by Cpd0SubsetItemRevision.
             

Use Cases:

             It is used when the user wishes to update the content of a Cpd0SubsetItemRevision
             or Cpd0DesignSubsetElement objects by re-executing its search recipe.
             

             Use Case1 : Update selected content of existing Cpd0SubsetItemRevision or
             Cpd0DesignSubsetElement objects.
             

             The following operation can be used for updating an existing WorkspaceObject
             objects.
             

             The set of content referenced by WorkspaceObject objects can be updated by
             re-executing the search recipe. The application specifies which WorkspaceObject
             objects should have their set of selected content updated.
             
             During the updateSubsetsContent operation,
             the server will find the set of Cpd0CollaborativeDesign content that satisfies
             the search criteria.This set of objects will be updated on the WorkspaceObject
             objects and will remain static until the next call to updateSubsetsContent
             operation.
             
             The search recipe on WorkspaceObject objects is normally changed using the
             setRecipes operation. The updateSubsetsContent can be called after setRecipes in order to update the WorkspaceObject based
             on the new or modified search recipe.
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param SubsetContentInfos: 
                         A list of <font face="courier" height="10">SubsetContentInfo</font> structure. Each
                         structure specifies the <b>WorkspaceObject</b> to be updated.
             
        :return: 
        """
        ...

class StructureExpandRestBindingStub(StructureExpandService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def NextExpandStructure(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.ExpandStructureResponse: ...
    def StartExpandStructure(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.ExpandStructureControls) -> Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.ExpandStructureResponse: ...
    def StopExpandStructure(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> bool: ...
    def NextExpandStructure2(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Cpd0.Services.Strong.Cpdcore._2014_10.StructureExpand.ExpandStructureResponse2: ...
    def StartExpandStructure2(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.ExpandStructureControls) -> Cpd0.Services.Strong.Cpdcore._2014_10.StructureExpand.ExpandStructureResponse2: ...
    def NextExpandStructure3(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Cpd0.Services.Strong.Cpdcore._2016_05.StructureExpand.ExpandStructureResponse3: ...
    def StartExpandStructure3(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: Cpd0.Services.Strong.Cpdcore._2016_05.StructureExpand.ExpandStructureControls3) -> Cpd0.Services.Strong.Cpdcore._2016_05.StructureExpand.ExpandStructureResponse3: ...
    def NextExpandStructure4(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Cpd0.Services.Strong.Cpdcore._2017_05.StructureExpand.ExpandStructureResponse4: ...
    def StartExpandStructure4(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: Cpd0.Services.Strong.Cpdcore._2017_05.StructureExpand.ExpandStructureControls4) -> Cpd0.Services.Strong.Cpdcore._2017_05.StructureExpand.ExpandStructureResponse4: ...

class StructureExpandService:
    """
    
            This service handles expansion of worksets, their subsets, and subordinate
            design components.   This service is used mainly when opening a workset in a CAD
            tool or displaying the content of a workset in the Teamcenter client.  The main operation
            supported by this service is startExpandStructure.
            There are two supporting operations nextExpandStructure
            and stopExpandStructure which complement
            startExpandStructure.
            


Library Reference:

Cpd0SoaCpdCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureExpandService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def NextExpandStructure(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.ExpandStructureResponse:
        """    
             Continues the expansion of one or more worksets, subsets, or design components using
             an expand cursor initially returned from startExpandStructure.
             Results are paged back to the client, and subsequent calls to nextExpandStructure may be required to get the entire set of expanded
             results.  Note: Applications should call stopExpandStructure
             if they wish to no longer fetch additional remaining expand results (e.g. after user
             termination of expand).
             

Use Cases:

             See SOA documentation for startExpandStructure for details about ExpandStructureResponse.
             

Dependencies:

             startExpandStructure
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ExpandCursor: 
                         An expand cursor returns from <font face="courier" height="10">startExpandStructure</font>

        :return: .
        """
        ...
    def StartExpandStructure(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.ExpandStructureControls) -> Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.ExpandStructureResponse:
        """    
             Start an expansion of one or more worksets, subsets, or design components.   Objects
             are expanded in the order listed.  Results are paged back to the client and subsequent
             calls to nextExpandStructure may be required
             to get the entire set of expanded results.  Note: Applications should call stopExpandStructure if they wish to no longer fetch
             additional remaining expand results (e.g. after user termination of expand).
             

Use Cases:

             This API supports the navigation of workset content and presented children of design
             components. Expanded workset content includes item sub structure, subsets, and subset
             content. Subset content is made up of design components and design features previously
             configured and selected from a product design by execution of the subsets search
             recipe. Presented children of design components (Cpd0DesignElement) are found
             by reverse navigation of their presented parent (cpd0presented_parent)
             property.
             

Use Case 1: Expand Workset One Level 

             Get the first level children of a workset. The results include any immediate occurrences
             of items in the workset and any subsets in the workset. All results are returned
             as BOMLine objects (note: subsets are returned via Cpd0SubsetLine objects).
             

             Get the configuration to be used on the workset. This is accomplished by the following
             steps::
             

Open a BOM window (BOMWindow);
             
Apply a revision rule to the window
             
Set the workset or workset revision as the top line in the window
             
Use the top line as a starting scope of startStructureExpand





Set the number of levels to expand (levelsToExpand)
             to 1
             
Set other expansion control flags, as needed
             
Initiate the expand using the startStructureExpand
             operation
             
Determine if the expansion is complete by testing the finished flag
             in the response.
             
If the expansion is not complete, use the nextStructureExpand
             operation to retrieve the next batch of expansion results from the Teamcenter; or
             use the stopStructureExpand operation if
             no more results of the expand are desired (e.g. user initiated abort).
             



Use Case 2: Get Presented Children of a Design Component 


             Get the first level presented children of a design component. The results include
             all design components that reference the input design components as their presented
             parent. All results are returned as design component objects.
             

Set the design components of interest as the starting scope of the
             expand
             
Set any expansion control flags, as needed
             
Initiate the expand using the startStructureExpand
             operation
             
Determine if the expansion is complete by testing the finished flag
             in the response.
             
If the expansion is not complete, use the nextStructureExpand
             operation to retrieve the next batch of expansion results from the Teamcenter; or
             use the stopStructureExpand operation if
             no more results of the expand are desired (e.g. user initiated abort).
             




Use Case 3: Expand a Subset to get its Design Components and Design Features


             Get the content of a subset. The results include all design components and design
             features that were configured and selected last time the subset recipe was executed
             (replayed). All results are returned as design component or design feature objects.
             
             Set the subset(s) of interest as the starting scope of the expand; this can be done
             in two ways
             

Method 1: via a subset line (Cpd0SubsetLine)
             

Get a Cpd0SubsetLine object from a previous expansion.
             
Set it as a starting scope for an expand.
             


Method 2: via a direct reference


Get a reference to a subset (Cpd0DesignSubsetElement)
             
Set it as a starting scope for an expand.
             


             Note: Method 1 is the more commonly used scenario.
             


Set any expansion control flags, as needed
             
Initiate the expand using the startStructureExpand
             operation
             
Determine if the expansion is complete by testing the finished flag
             in the response.
             
If the expansion is not complete, use the nextStructureExpand
             operation to retrieve the next batch of expansion results from the Teamcenter; or
             use the stopStructureExpand operation if
             no more results of the expand are desired (e.g. user initiated abort).
             



Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param StartingScope: 

        :param Controls: 
                         A set of controls (<font face="courier" height="10">ExpandStructureControls</font>)
                         which govern the expansion of objects.
             
        :return: ).
        """
        ...
    def StopExpandStructure(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> bool:
        """    
             Terminates an expansion initially started by a call to startExpandStructure.
             Clients should only call this operation when there are still results to return, as
             indicated by the finished flag being set
             to false in the last response from either startExpandStructure or nextExpandStructure operations.
             

Use Cases:

             See SOA documentation for startExpandStructure for use cases involving this
             operation.
             

Dependencies:

             startExpandStructure
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ExpandCursor: 
                         An expand cursor initially returned from <font face="courier" height="10">startExpandStructure</font>

        :return: Return value is always false.
        """
        ...
    def NextExpandStructure2(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Cpd0.Services.Strong.Cpdcore._2014_10.StructureExpand.ExpandStructureResponse2:
        """    
             Continues the expansion of one or more worksets, subsets, or design components using
             an expand cursor initially returned from startExpandStructure.
             Results are paged back to the client, and subsequent calls to nextExpandStructure may be required to get the entire set of expanded
             results.  Note: Applications should call stopExpandStructure
             if they wish to no longer fetch additional remaining expand results (e.g. after user
             termination of expand).
             

Use Cases:

             See SOA documentation for startExpandStructure
             for details about ExpandStructureResponse.
             

Dependencies:

             startExpandStructure2
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ExpandCursor: 
                         An expand cursor returns from <font face="courier" height="10">startExpandStructure</font>

        :return: .
        """
        ...
    def StartExpandStructure2(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: Cpd0.Services.Strong.Cpdcore._2011_06.StructureExpand.ExpandStructureControls) -> Cpd0.Services.Strong.Cpdcore._2014_10.StructureExpand.ExpandStructureResponse2: ...
    def NextExpandStructure3(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Cpd0.Services.Strong.Cpdcore._2016_05.StructureExpand.ExpandStructureResponse3:
        """    
             Continues the expansion of one or more worksets, subclasses of compositions,subsets,
             or design components using an expand cursor initially returned from startExpandStructure3. Results are paged back to the client, and
             subsequent calls to nextExpandStructure3
             may be required to get the entire set of expanded results. Note: Applications should
             call stopExpandStructure if they wish to
             no longer fetch additional remaining expand results (e.g. after user termination
             of expand).
             

Use Cases:

             See SOA documentation for startExpandStructure3
             for details about the usecase.
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ExpandCursor: 
                         An expand cursor returns from nextExpandStructure3
             
        :return: .
        """
        ...
    def StartExpandStructure3(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: Cpd0.Services.Strong.Cpdcore._2016_05.StructureExpand.ExpandStructureControls3) -> Cpd0.Services.Strong.Cpdcore._2016_05.StructureExpand.ExpandStructureResponse3:
        """    
             Start an expansion of one or more worksets,subclasses of compositions, subsets, or
             design components. Objects are expanded in the order listed. Results are paged back
             to the client and subsequent calls to nextExpandStructure3 may be required
             to get the entire set of expanded results. Note: Applications should call stopExpandStructure3
             if they wish to no longer fetch additional remaining expand results (e.g. after user
             termination of expand).
             

Use Cases:

             This API supports the navigation of workset content and presented children of design
             components. Expanded workset content includes item sub structure, subsets, and subset
             content. Subset content is made up of design components and design features previously
             configured and selected from a product design by execution of the subsets search
             recipe. Presented children of design components (Cpd0DesignElement) are found
             by reverse navigation of their presented parent (cpd0presented_parent)
             property.
             

Use Case 1: Expand Workset One Level
             
             Get the first level children of a workset. The results include any immediate occurrences
             of items in the workset and any subsets in the workset. All results are returned
             as BOMLine objects (note: subsets are returned via Cpd0SubsetLine objects).
             

Use Case 2: Get Presented Children of a Design Component
             

             Get the first level presented children of a design component. The results include
             all design components that reference the input design components as their presented
             parent. All results are returned as design component objects.
             

Use Case 3: Expand a Subset to get its Design Components and Design Features
             

             Get the content of a subset. The results include all design components and design
             features that were configured and selected last time the subset recipe was executed
             (replayed). All results are returned as design component or design feature objects.
             
             Set the subset(s) of interest as the starting scope of the expand; this can be done
             in two ways
             

             Method 1: via a subset line (Cpd0SubsetLine)
             
             Method 2: via a direct reference
             
             Note: Method 1 is the more commonly used scenario.
             

Use Case 4: Expand a subclass of Rlz0Composition object.
             

             Expansion of an Rlz0Composition object returns all the Rlz0Subset objects that it
             contains.
             

Use Case 5: Expand a Rlz0Subset object.
             

             Expansion of an Rlz0Subset object returns sparsely or dynamically realized
             model elements (Mdl0ModelElement) from source application model (Mdl0ApplicationModel).
             Unlike the concept of Full or Static Realization, model elements (Mdl0ModelElement)
             in the target application model (Mdl0ApplicationModel) are not new copies
             rather simple references to objects in source application model.
             

             Also, this API provides the support to expand appropriate sparse elements by applying
             effectivity and variant overlay strings for input Mdl0ApplicationModel that
             are used during the expansion of composition (Rlz0Composition) or subset (Rlz0Subset).
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param StartingScope: 
                         Note: <b>ImanItemLine</b> objects (other than Cpd0WorksetLine) are not a supported
                         type for starting scope. Application should use normal BOM expand API to process
                         <b>ImanItemLines</b>.
             
        :param Controls: 
                         A set of controls (<font face="courier" height="10">ExpandStructureControls3</font>)
                         which govern the expansion of objects.This includes expansion of objects which are
                         subclasses of <b>Rlz0Composition</b>.
             
        :return: 2. 279055 - The provided number of levels to expand is invalid. Valid values are
             0 or 1 for this operation.
        """
        ...
    def NextExpandStructure4(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Cpd0.Services.Strong.Cpdcore._2017_05.StructureExpand.ExpandStructureResponse4:
        """    
             Continues the expansion of one or more worksets, composition,subsets, or design components
             using an expand cursor initially returned from startExpandStructure4.
             Results are paged back to the client, and subsequent calls to nextExpandStructure4 may be required to get the entire set of
             expanded results. Note: Applications should call stopExpandStructure
             if they wish to no longer fetch additional remaining expand results (e.g. after user
             termination of expand).
             

Use Cases:

             See SOA documentation for startExpandStructure4
             for details about the use case.
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param ExpandCursor: 
                         An expand cursor returns from <font face="courier" height="10">nextExpandStructure4</font>.
             
        :return: .
        """
        ...
    def StartExpandStructure4(self, StartingScope: list[Teamcenter.Soa.Client.Model.ModelObject], Controls: Cpd0.Services.Strong.Cpdcore._2017_05.StructureExpand.ExpandStructureControls4) -> Cpd0.Services.Strong.Cpdcore._2017_05.StructureExpand.ExpandStructureResponse4:
        """    
             Start an expansion of one or more worksets, subclasses of compositions, subsets,
             or design components. Objects are expanded in the order listed. Results are paged
             back to the client and subsequent calls to nextExpandStructure4 may be required to
             get the entire set of expanded results. Note: Applications should call stopExpandStructure
             if they wish to no longer fetch additional remaining expand results (e.g. after user
             termination of expand).
             

Use Cases:

             This API supports the navigation of workset content and presented children of design
             components. Expanded workset content includes item sub structure, subsets, and subset
             content. Subset content is made up of design components and design features previously
             configured and selected from a product design by execution of the subsets search
             recipe. Presented children of design components (Cpd0DesignElement) are found
             by reverse navigation of their presented parent (cpd0presented_parent)
             property.
             

Use Case 1: Expand Workset One Level
             
             Get the first level children of a workset. The results include any immediate occurrences
             of items in the workset and any subsets in the workset. All results are returned
             as BOMLine objects (note: subsets are returned via Cpd0SubsetLine objects).
             

Use Case 2: Get Presented Children of a Design Component
             

             Get the first level presented children of a design component. The results include
             all design components that reference the input design components as their presented
             parent. All results are returned as design component objects.
             

Use Case 3: Expand a Subset to get its Design Components and Design Features
             

             Get the content of a subset. The results include all design components and design
             features that were configured and selected last time the subset recipe was executed
             (replayed). All results are returned as design component or design feature objects.
             
             Set the subset(s) of interest as the starting scope of the expand; this can be done
             in two ways
             

             Method 1: via a subset line (Cpd0SubsetLine)
             
             Method 2: via a direct reference
             
             Note: Method 1 is the more commonly used scenario.
             

Use Case 4: Expand a subclass of Rlz0Composition object.
             

             Expansion of an Rlz0Composition object returns all the Rlz0Subset objects
             that it contains.
             

Use Case 5: Expand a Rlz0Subset object.
             

             Expansion of an Rlz0Subset object returns sparsely or dynamically realized
             model elements (Mdl0ModelElement) from source application model (Mdl0ApplicationModel).
             Unlike the concept of Full or Static Realization, model elements (Mdl0ModelElement)
             in the target application model (Mdl0ApplicationModel) are not new copies
             rather simple references to objects in source application model.
             

             Also, this API provides the support to expand appropriate sparse elements by applying
             effectivity and variant overlay strings for input Mdl0ApplicationModel that
             are used during the expansion of composition (Rlz0Composition) or subset (Rlz0Subset).
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param StartingScope: 
                         Note: <b>ImanItemLine</b> objects (other than <b>Cpd0WorksetLine</b>) are not a supported
                         type for starting scope. Application should use normal BOM expand API to process
                         <b>ImanItemLine </b>objects.
             
        :param Controls: 
                         A set of controls (ExpandStructureControls4) which govern the expansion of objects.
             
        :return: 283004 - An invalid parameter level is specified for the workset expansion. Only
             levels 0 and 1 are supported.
        """
        ...

