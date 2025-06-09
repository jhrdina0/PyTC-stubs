import Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AuxiliaryObjectInfo3:
    """
    
            AuxiliaryObjectInfo3 is used as input for creating or updating auxiliary objects
            along with main objects. For example, it can be used to pass information about attribute
            group objects to be created along with DesignElement.
            

    """
    def __init__(self, ) -> None: ...
    BoType: str
    """
            Type of the auxiliary object used for creation. For update of auxiliary object, this
            field is ignored.
            """
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            Auxiliary object to be updated. This field is empty when auxiliary object is being
            created.
            """
    AttrInfo: System.Collections.Hashtable
    """
            Contains information about attributes of the auxiliary objects. This is used during
            creation and updating auxiliary object.
            
            attrInfo parameter : Map of (std::string, std::string[])
            """
    SubObjects: System.Collections.Hashtable
    """
            Contains information about sub-objects to be created for auxiliary object. This field
            is ignored when auxiliary object is being updated.
            
"""

class CompoundCreateInfo3:
    """
    Generic CreateInfo construct to support compound object create
    """
    def __init__(self, ) -> None: ...
    BoType: str
    """The name of the Business Object type to be created"""
    AttrInfo: System.Collections.Hashtable
    """
            This contains property data for the newly created object. It is a map of property
            and values for the newly created object. All property values are expressed in their
            string equivalent. Object reference (tag) values can be passed using the client string
            representation (e.g. UID) of the referenced object. Array values are always treated
            as replacement for entire array content. Non array values are passed as first element
            in value list. It is basically a map of String (Property Name) to Property Value
            (List of Strings)\
            
            attrInfo is object of AttributeInfoMap3.
            
            attrInfo parameter : Map of (std::string, std::string[])
            """
    CompoundInfo: System.Collections.Hashtable
    """
            Compound object data. CompoundCreateInfoMap3 is a map of property name to CompoundCreateInfo3.
            It is basically a map of String (property Name) to property Value (CompoundCreateInfo3)
            which in turn describes a different object to be created.
            
"""

class CreateOrUpdateDesignSubsetResponse:
    """
    
            Response to createOrUpdateDesignSubsets.   It contains a list of design subset element
            data which is one to one correspondance with input subset element info.
            
    """
    def __init__(self, ) -> None: ...
    DseData: list[DesignSubsetsData]
    """
            A list of design subset element data which has one to one correpondance with input
            subset element info.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """added, updated, deleted object data plus any error information"""

class DesignFeatureConnectionInfo:
    """
    
            DesignFeatureConnectionInfo is used as input for creating or updating the set of
            design components connected to the design feature.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended.  It is used for mapping server
            errors and for correlating data in the response to the inputs.  The caller should
            populate each DesignFeatureConnectionInfo with a value that is unique within the
            input set. The value is not interpreted or manipulated internally by the server.
            """
    DesignElement: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignModelElement
    """
            Connected design component. The design component must exist in the same product design
            as the design feature.
            """
    CsId: str
    """
            Copy stable ID, required when replacing an already connected element with another,
            otherwise optional. Also, if designElement is not set  during a replace, the connected
            info is removed from Teamcenter.
            """
    AttrInfo: System.Collections.Hashtable
    """
            A Map(string, list(string)) of name-value pairs used to specify additional property
            data for the relation.  All values are specified as strings, the caller is responsible
            for generating the correct string representation of each value passed. For tag values,
            the UID of the tag is used.
            """

class DesignFeatureInfo:
    """
    
            DesignFeatureInfo is used as input for creating or updating design feature objects
            and their connection to design component objects.  When creating a new design feature,
            the caller must specify the business object type (boType) of the new design feature.
            During update, boType is left empty and a reference to the design feature (feature)
            is specified.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended.  It is used for mapping server
            errors and for correlating data in the response to the inputs.  The caller should
            populate each DesignFeatureInfo with a value that is unique within the input set.
            The value is not interpreted or manipulated internally by the server.
            """
    Feature: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignFeature
    """
            The  Cpd0DesignFeature to be updated.  A value is required for update, otherwise
            (create case) this value should be empty.
            """
    BoType: str
    """
            The business object type of a design feature to be created.  This value is required
            for creating a new design feature, and must be a valid subtype of Cpd0DesignFeature.
            For update of an existing design feature, this value should be empty.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The product design which will contain the new design feature; required for creating
            a new design feature.  If an existing design feature is being updated, then this
            value should be empty.
            """
    Transform: list[float]
    """
            Absolute transform (units in meters) positioning the design feature in the coordinate
            space of the product design.  This is a vector of 16 double precision values; order
            of values corresponds to PLMXML standard.   An empty vector is interpreted as an
            identity matrix.
            """
    BoundingBox: list[float]
    """
            Bounding box data (units in meters) in coordinate space of the product design; empty
            = no box.  Order of values is { x-min, y-min, z-min, x-max, y-max, z-max }.
            """
    AttrInfo: System.Collections.Hashtable
    """
            A Map(string, list(string)) of name-value pairs used to specify additional property
            data for design features.  All values are specified as strings, the caller is responsible
            for generating the correct string representation of each value passed.  For tag values,
            the UID of the tag is used.
            """
    ConnectedInfo: list[DesignFeatureConnectionInfo]
    """
            List objects to which the design feature is connected. The connected-element (Cpd0ConnectedElement)
            relations in Teamcenter will be created/updated/removed such that they match the
            entries in the connectedInfo list, unless the mergeConnected option is set to true.
            If mergeConnected option is false, relations not referenced in the input will be
            automatically removed from the feature.
            """
    MergeConnected: bool
    """
            If true, indicates that connectedInfo should be merged with existing content in Teamcenter;
            otherwise all connected data is replaced for the feature.  If no connected information
            for this feature currently exists in Teamcenter, then merge and replace have the
            same effect.
            """
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The DirectModel dataset to associate with the design feature. Value can be
            null.
            """
    TrueshapeDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The Dateset, containing Trushape information, to associate with the design
            feature. Typically this will be a UGMASTER or DirectModel dataset. Optional.
            """
    AssociatedDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The Dataset to associate with the design feature. Value can be null. This
            Dataset will connect to Design Feature using Cpd0AssociatedRelation.
            """
    ThumbnailDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The Dataset to associate with the design feature. Value can be null."""
    GuardObjLastModifiedDate: bool
    """
            If true, causes the update of design feature to check last modified date to avoid
            data overwrite.
            """
    ObjLastModifiedDateGuard: System.DateTime
    """
            Modification date guard is used if guardObjLastModifiedDate is set to true. Object
            update will abort if the last modified date of the object is greater than objLastModifiedDateGuard.
            """
    AuxiliaryObjects: System.Collections.Hashtable
    """
            Information about auxiliary objects (attribute groups) attached to the design feature
            to be created or updated.
            
            auxiliarObjects is object of AuxiliaryObjectInfoMap3 which is map of relation property
            name to AuxiliaryObjectInfo .
            
            axiliaryObject paramter: Map of (std:string,AuxiliaryObjectInfo[])
            """

class DesignSubsetsData:
    """
    
            Response to createOrUpdateDesignSubsets contains information about DesignSubsetElements
            created or updated, its clientId, its CopyStable Id.  It also contains a list of
            appended and removed DesignElements from the workSetModel. It also contains map of
            input DEs and its corresponding Attribute Group objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. It can be empty if DesignSubsetElementInfo
            do not have Client ID populated.
            """
    SubsetElement: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignSubsetElement
    """Business Object reference to Cpd0DesignSubsetElement created."""
    SubsetInstance: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignSubsetInstance
    """Business Object reference to Cpd0DesignSubsetInstance created."""
    DseCsID: str
    """copy stable ID of design subset element."""
    SubordinateMap: System.Collections.Hashtable
    """
            Map of (Teamcenter::AppModel::Mdl0ModelElement, Teamcenter::AppModel::Mdl0ModelElement).
            This is for override mapping. Not supported currently. Reserved for future development.
            """
    CsIDMap: System.Collections.Hashtable
    """
            Map of (Teamcenter::AppModel::Mdl0ModelElement, std::string ) giving new  source
            design component to its copy stable id.
            """
    AppendedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """Contains list of appended source elements."""
    RemovedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """Contains list of removed source elements."""
    ContentObjInfoInContextMap: System.Collections.Hashtable
    """
            Map of (Teamcenter::AppModel::Mdl0ModelElement, Teamcenter::AppModel::Mdl0ModelElement)
            giving the Cpd0InfoInContext attribute group for each of the Design Subset Element's
            content. The content object is the key, attribute group object is the value.
            """

class DesignSubsetsInfo:
    """
    
            Data on DesignSubsetsInfo used to create or update DesignSubsetElements in a workset.
            


    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned CreatedItemsOutput
            elements and Partial Errors associated with this input ItemProperties. This is an
            optional argument.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignSubsetElement
    """
            A Business Object reference to an existing Cpd0DesignSubsetElement that needs
            to be updated. If none supplied, it is assumed to create a new DesignSubsetElement.
            """
    BoType: str
    """
            If specified a new DesignSubsetElement is
            created. This value is required for creating new a DesignSubsetElement, and must
            be a valid subtype of Cpd0DesignSubsetElement.  For update of an existing
            DesignSubsetElement, this value should be
            empty.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Business object reference to the workset Revision in which the objects to be created
            or updated.
            """
    ViewType: str
    """BOMView type. Optional if modelObject is WorksetRevision, empty otherwise."""
    SourceModel: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Business object reference to the Product Design or Baseline Revision from which content
            is being instanced. Optional for update use case.
            """
    Transform: list[float]
    """
            Absolute transform which positions the shape in the coordinate system of the product
            design (units in meters), empty = identity, otherwise contains 16 doubles in the
            following order: { r00, r10, r20, p0, r01, r11, r21, p1, r02, r12, r22, p2, t0, t1,
            t2, s }, where the letter prefix signifies the following:
            

    r    a rotation component
            
    p   a perspective component
            
    t    a translation component
            
    s   the inverse scale.
            

"""
    AttrInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify additional property data for design control
            elements. All values are specified as strings, the caller is responsible for generating
            the correct string representation of each value passed.  For tag values, the UID
            of the tag is used.
            
attrInfo parameter : Map of (std::string, std::string[])
            """
    ApplyTargetPropertiesToElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            A list of business object references of the object to which target properties needs
            to be applied from the associated subet default object.
            """
    AppendSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            A list of business object references of the object to be append from sourceModel into the modelObject
            i.e the list of objects to be Appended from sourceModel into worksetModel.
            """
    RemoveSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            A list of business object references of the object to be removed from the modelObject  i.e the list of objects to be removed  from Workset
            Model. It is expected that this parameter contains the complete list of presented
            parent design components and the actual design components to be removed unless removechildrenautomicatlly is set to true.
            """
    UpdateRecipeForAppendsAndRemoves: bool
    """
            If this is set to true, then the recipe include/exclude elements criteria
            will be modified acoordingly based on  appendSourcElements
            and removeSourceElements input arguments.
            """
    SubordinateSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """
            Specify the source objects for which there must be a persistant subordinate design
            component to be created. Only supported when subset is part of a Workset.
            """
    Subset: Teamcenter.Soa.Client.Model.Strong.Mdl0SubsetDefinition
    """
            Business Object reference to the Cpd0Subset business object.This is used when
            a subset is instantiated into a worksetrevision. Instead of explicitly passing design
            component to be added or removed in a workset revision,user can choose to pass a
            subset as an input such that all the design components fulfilling the recipe criteria
            will be instanced into worksetrevision.
            """
    RemoveChildrenAutomatically: bool
    """
            If true, the children of design components specified in removeSourceElements input
            parameter will be removed from worksetModel also. If false, it is expected that removeSourceElements
            contains complete hierachy of design components to be removed.
            """
    ReplaceSourceElements: System.Collections.Hashtable
    """
            This designElements in this list will replace the designElements from workset model
            while retaining csId. If no designElement is found corresponding to key csId, a case
            of change in csId is assumed. In case of change in csId, csId of existing design
            component in workset model is changed.Input must contain all elements which complete
            valid and logical structure .Invalid
            
            input may result into inconsistent data model.
            """
    GuardObjLastModifiedDate: bool
    """
            Flag, if set to true, causes the update of DesignElement to check last modified date
            to avoid data overwrite.
            """
    ObjLastModifiedDateGuard: System.DateTime
    """
            Modification date guard is used if guardObjLastModifiedDate
            is set to true. Object update will abort if the last modified date of the object
            is greater than objLastModifiedDateGuard.
            """
    AuxiliaryObjects: System.Collections.Hashtable
    """
            Information about auxiliary objects (attribute groups) attached to the design feature
            to be created or updated.
            
auxiliarObjects is object of AuxiliaryObjectInfoMap which is map of relation property name
            to  AuxiliaryObjectInfo .
            
axiliaryObject paramter: Map of (std:string,AuxiliaryObjectInfo[])
            """

class VariantCriteriaResponse:
    """
    
            This operation returns a list of Variant Criteria (Variant Rules) associated with
            the product. This operation may raise Teamcenter::Soa::Server::ServiceException wrapping
            around following Teamcenter errors:

            92002: The Product Name and Product Namespace must not be empty.
            
    """
    def __init__(self, ) -> None: ...
    VariantCriteria: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """List of configurations associated with the product"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateDesignFeatures(self, FeatureInfos: list[DesignFeatureInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignFeaturesResponse: ...
    def CreateOrUpdateDesignSubsets(self, SubsetInfos: list[DesignSubsetsInfo]) -> CreateOrUpdateDesignSubsetResponse:
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
    def GetProductConfigurations(self, ProductName: str, ProductNameSpace: str) -> VariantCriteriaResponse:
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

