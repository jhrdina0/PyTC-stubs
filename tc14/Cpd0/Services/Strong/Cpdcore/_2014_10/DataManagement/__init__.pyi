import Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AuxiliaryObjectInfo2:
    """
    
            AuxiliaryObjectInfo2 is used as input for creating or updating auxiliary objects
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

class CompoundCreateInfo2:
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
            
            attrInfo is object of AttributeInfoMap.
            
            attrInfo parameter : Map of (std::string, std::string[])
            """
    CompoundInfo: System.Collections.Hashtable
    """
            Compound object data. CompoundCreateInfoMap is a map of property name to CompoundCreateInfo.
            It is basically a map of String (property Name) to property Value (CompoundCreateInfo)
            which in turn describes a different object to be created.
            
"""

class CreateOrUpdateDesignElementsInfo:
    """
    
            CreateOrUpdateDesignElementsInfo2 is used as input into createOrUpdateDesignElements.It
            contains a lists if input for creating or updating "shape", "reuse", "promissory"
            and "subordinate" DesignElement objects.
            
    """
    def __init__(self, ) -> None: ...
    ShapeDesignElementInfo: list[ShapeDesignElementInfo]
    """ShapeDesignElementInfo."""
    ReuseDesignElementInfo: list[ReuseDesignElementInfo]
    """ReuseDesignElementInfo"""
    PromissoryDesignElementInfo: list[PromissoryDesignElementInfo]
    """PromissoryDesignElementInfo"""
    SubordinateDesignElementInfo: list[SubordinateDesignElementInfo]
    """SubordinateDesignElementInfo."""

class CreateOrUpdateDesignSubsetElementsResponse2:
    """
    
            Response to createOrUpdateDesignSubsetElements2.   It contains a list of design subset
            element data which is one to one correspondance with input subset element info.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """added, updated, deleted object data plus any error information"""
    DseData: list[DesignSubsetElementData2]
    """
            A list of design subset element data which has one to one correpondance with input
            subset element info.
            """

class DesignFeatureConnectionInfo:
    """
    
DesignFeatureConnectionInfo is used as input
            for creating or updating the set of design components connected to the design feature.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended. It is used for mapping server
            errors and for correlating data in the response to the inputs. The caller should
            populate each DesignFeatureInfo with a value
            that is unique within the input set. The value is not interpreted or manipulated
            internally by the server.
            """
    DesignElement: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignModelElement
    """
            Connected design component, required. The design component must exist in the same
            product design as the design feature
            """
    CsId: str
    """
            Copy stable ID, required when replacing once connected with another, otherwise optional.
            Also, if designElement is not set to during
            a replace, the connected info is removed from Teamcenter.
            """
    AttrInfo: System.Collections.Hashtable
    """
            A map (string,list(string)) of name-value
            pairs used to specify additional property data for the relation. All values are specified
            as strings, the caller is responsible for generating the correct string representation
            of each value passed.For tag values, the UID of the tag is used.
            """

class DesignFeatureInfo:
    """
    
DesignFeatureInfo is used as input for creating
            or updating design feature objects and their connection to design component objects.
            When creating a new design feature, the caller must specify the business object
            type (boType) of the new design feature.  During update, boType is left empty and
            a reference to the design feature (feature) is specified.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended. It is used for mapping server
            errors and for correlating data in the response to the inputs.The caller should populate
            each DesignFeatureInfo with a value that
            is unique within the input set. The value is not interpreted or manipulated internally
            by the server
            """
    Feature: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignFeature
    """
            The Cpd0DesignFeature to be updated. A value is required for update, otherwise
            (create case) this value should be empty
            """
    BoType: str
    """
            The business object type of a design feature to be created. This value is required
            for creating a new design feature, and must be a valid subtype of Cpd0DesignFeature.
            For update of an existing design feature, this value should be empty.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The product design which will contain the new design feature; required for creating
            a new design feature. If an existing design feature is being updated, then this value
            should be empty.
            """
    Transform: list[float]
    """
            Absolute transform (units in meters) positioning the design feature in the coordinate
            space of the product design.This is a vector of 16 double precision values; order
            of values corresponds to PLMXML standard. An empty vector is interpreted as an identity
            matrix.
            """
    BoundingBox: list[float]
    """
            Bounding box data (units in meters) in coordinate space of the Product Design; empty
            = no box. Order of values is { x-min, y-min, z-min, x-max, y-max, z-max
            """
    AttrInfo: System.Collections.Hashtable
    """
            A map of (string,list(string)) of name value
            pairs used to specify additional property data for design features. All values are
            specified as strings, the caller is responsible for generating the correct string
            representation of each value passed.  For tag values, the UID of the tag is used.
            
"""
    ConnectedInfo: list[DesignFeatureConnectionInfo]
    """
            List of objects to which the design feature is connected. The connected-element (Cpd0ConnectedElement)
            relations in Teamcenter will be created/updated/removed such that they match the
            entries in the connectedInfo list, unless the mergeConnected option is set to true.
            If mergeConnected option is false, relations not referenced in the input will not
            be automatically removed from the feature
            """
    MergeConnected: bool
    """
            When set to true, indicates that connected info should be merged with existing content
            in Teamcenter; otherwise all connected data is replaced for the feature. If no connected
            information for this feature currently exists in Teamcenter, then merge and replace
            have the same effect.
            """
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The DirectModel dataset to associate with the design feature.Value can be
            null.
            """
    TrueshapeDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The Dataset, containing Trushape information, to associate with the design feature.
            Typically this will be a UGMASTER or DirectModel dataset.Optional.
            """
    GuardObjLastModifiedDate: bool
    """
            if true, causes the update of design feature to check last modified date to avoid
            data overwrite.
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
            to AuxiliaryObjectInfo .
            
            axiliaryObject paramter: Map of (std:string,AuxiliaryObjectInfo[])
            """

class DesignSubsetElementData2:
    """
    
            Response to createOrUpdateDesignSubsetElements2 contains information about DesignSubsetElements
            created or updated, its clientId, its CopyStable Id.  It also contains a list of
            appended and removed DesignElements from the workSetModel.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            map of client ID to corresponding object that was created. It can be empty if  DesignSubsetElementInfo do not have Client ID populated.
            """
    SubsetElement: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignSubsetElement
    """
            Business Object reference to DesignSubsetElement
            created.
            """
    SubsetInstance: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignSubsetInstance
    """
            Business Object reference to DesignSubsetInstance
            created.
            """
    DseCsID: str
    """copy stable ID of design subset element."""
    SubordinateMap: System.Collections.Hashtable
    """
            This is for override mapping. Not supported currently. Reserved for future development.
            
subordinateMap is object of BoToBoMap

subordinateMap parameter :Map of (Teamcenter::BusinessObject, Teamcenter::BusinessObject)
            """
    CsIDMap: System.Collections.Hashtable
    """
            Map of new source design component to its copy stable id.
            
csIdMap is object of BoToStringMap

BoToStringMap parameter : Map of(Teamcenter::BusinessObject, std::string )
            """
    AppendedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """Contains list of appended source elements."""
    RemovedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ConditionalElement]
    """Contains list of removed source elements."""

class DesignSubsetElementInfo2:
    """
    
            Data on DesignSubsetElementInfo2 used to create or update DesignSubsetElements in
            a workset.
            


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
            A Business Object reference to an existing Cpd0DesignSubsetElement object
            that needs to be updated. If  none supplied, it is assumed to create a new DesignSubsetElement.
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
            elements. Map of (std::string, std::string[]). Property name is the key. All
            values are specified as strings,  the caller is responsible for generating the correct
            string representation of each value passed. For tag values, the UID of the tag is
            used.
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
            Map of (String, AuxiliaryObjectInfo[]) giving information about auxiliary objects
            (attribute groups) attached to the design feature to be created or updated.
            """

class InstantiatedObjectsData:
    """
    
            This structure contains the required information that can be returned to service
            caller such as Instantiated objects, deleted objects and updated objects for a particular
            container object provided/created.
            
    """
    def __init__(self, ) -> None: ...
    ClientIDMap: System.Collections.Hashtable
    """
            map of client ID to corresponding source object  that was created
            
            clientIDMap is object of StringToBoMap.
            
            clientIDMap parameter: Map of (std::string,Teamcenter::BusinessObject)
            """
    ModelReuse: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignModelElement
    """Business Object reference to ModelReuse catgeory of type Cpd0DesignModelElement created."""
    IncludeSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """Contains a list of objects to be include from sourceModel into the targetModel."""
    UpdatedObjectsList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """ModelElements which are being updated."""

class SourceModelInfo:
    """
    
            This structure contains complete source information along with configuration context.
            This structure provides what objects need to include and what needs to delete at
            target Application Model. An optional boolean variable 'updateRecipeOnTargetforIncludesAndExclude'
            that will tell whether the recipe on target needs to update.
            
    """
    def __init__(self, ) -> None: ...
    SourceModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            Business object reference to the source Application Model. Can be empty if source
            Partition or source scheme is supplied as input.
            """
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """Configuration rules to be applied on source models."""
    SubsetDefinition: Teamcenter.Soa.Client.Model.Strong.Mdl0SubsetDefinition
    """Business object reference to the source Subset Definition."""
    IncludeSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            Contains a list of business object references of the object to be include from sourceModel
            into the targetModel.
            """

class ReuseModelMiscInfo:
    """
    
            This structure contains information about the required transforms, bounding box information,
            attached direct datasets, and trueshape datasets if any.
            
    """
    def __init__(self, ) -> None: ...
    Transforms: list[float]
    """
            Absolute transform (units in meters)  positioning the design feature in the coordinate
            space of the product design. This is a vector of 16 double precision values; order
            of values corresponds to PLMXML standard. An empty vector is interpreted as an identity
            matrix.
            """
    BoundingBox: list[float]
    """
            Bounding box data (units in meters) in coordinate space of the product design; empty
            = no box. Order of values is { x min, y min, z min, x max, y max, zmax }.
            """
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            Reference to a DirectModel dataset to associate with the design feature. Value can
            be null.
            """
    TrueshapeDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            Reference to a dataset, containing Trushape information, to associate with the design
            feature. Typically this will be a UGMASTER or DirectModel dataset. This is an optional
            parameter.
            """

class InstantiationObjectInfo:
    """
    
            This structure especially used to instantiate source model objects into target Application
            Model. InstantiationObjectInfo will contain information about source model, target
            model, miscellaneous, and auxiliary object info that will be needed to create new
            instantiation of objects.
            
    """
    def __init__(self, ) -> None: ...
    BoType: str
    """
            This specifies the Business Object Type of the modelreuse which holds the model elements
            after Instantiation.This value is required in creation scenario and must be a  valid
            subtype of Cpd0DesignModelElement. For update of an existing Instantiation, this
            value must be empty.
            """
    SourceModelData: SourceModelInfo
    """Information about the source content to be instantiated into the target model."""
    TargetModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            This is where the new copies after Instantiation are created. TargetModel can be
            a Product Design or WorksetRevision. This is required only for create.
            """
    MiscInfo: ReuseModelMiscInfo
    """
            This applies the additional information like information about the transforms, directModelDataset,trueshapeDataset
            and bounding box on the newly created reuse in the target model. This is optional
            parameter.
            """
    AttrInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify additional property data for design control
            elements. All values are specified as strings, the caller is responsible for generating
            the correct string representation of each value passed. For tag values, the UID of
            the tag is used.
            
"""
    AuxObjectInfo: Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.AuxiliaryObjectInfo
    """
            Information about auxiliary objects ( attribute groups ) attached to the design feature
            to be created or updated. auxiliaryObjects is object of AuxiliaryObjectInfoMap which
            is map of relation property name to AuxiliaryObjectInfo.
            """

class ModelToModelInstantiationInfo:
    """
    
            This structure contains the information stored by caller such as clientId for specific
            session, list of InstantiationObjectInfo if the service called for instantiation,
            and list of UpdateInstantiationContentInfo if the service called for update of instantiated
            objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify the newly created
            or updated elements and partial errors associated with the input. This is an optional
            argument.
            """
    ObjInfo: list[InstantiationObjectInfo]
    """
            A Vector of information on source application model to be instantiated into target
            application model.
            """
    UpdateInfo: list[UpdateInstantiationContentInfo]
    """A vector of  information on Instantiations to be updated."""

class ModelToModelInstantiationResponse:
    """
    
            Response from the service SOA which can be used to store and return the InstantiatedObjectsData
            and the common ServiceData to the caller of the service. Please see the description
            for more information on InstantiatedObjectsData.
            
    """
    def __init__(self, ) -> None: ...
    InstantiatedObjects: list[InstantiatedObjectsData]
    """
            Represents the list of InstantiatedObjectsData which has one to one correspondence
            with input ModelToModelInstantiationInfo.
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains newly added , updated object data including the error information, if any."""

class PromissoryDesignElementInfo:
    """
    
PromissoryDesignElementInfo is used as input
            for creating promissory DesignElement objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned CreatedItemsOutput elements and Partial Errors
            associated with this input ItemProperties.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignModelElement
    """
            The promissory design component to be updated or substituted. Can be empty
            otherwise.
            """
    BoType: str
    """
            The business object type of a design component to be created. This value is required
            for creating a new design component, and must be a valid subtype of Cpd0DesignModelElement.
            For update of an existing design component, this value should be empty.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Product Design for creating a new promissory design component. Can be empty
            otherwise.
            """
    BoundingBox: list[float]
    """
            Bounding box data (units in meters), empty = no box, otherwise contains 6 doubles
            in the following order:{ x min, y min, z min, z max, y max, z max }
            

"""
    AttrInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify additional property data for design control
            elements. All values are specified as strings, the caller is responsible for generating
            the correct string representation of each value passed. For tag values, the UID of
            the tag is used.
            
attrInfo parameter : Map of (std::string, std::string[])
            
"""
    GuardObjLastModifiedDate: bool
    """
            Flag, if set to true, causes the update of DesignElement
            to check last modified date to avoid data overwrite
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
            to AuxiliaryObjectInfo .
            
axiliaryObject paramter: Map of (std:string,AuxiliaryObjectInfo[])
            """

class ShapeOverrideInfo:
    """
    ShapeOverrideInfo contains inforamtion for overriden geometry.
    """
    def __init__(self, ) -> None: ...
    ThumbnailDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Thumbnail dataset for override geometry."""
    GeometryOverrideDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """NX specific dataset for overriden geometry."""
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Direct model dataset for overriden geometry."""
    TrueShapeDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """True shape dataset for overriden geometry."""
    BoundingBox: list[float]
    """Bounding box for overriden geometry."""
    AttrInfo: System.Collections.Hashtable
    """Other relatde attribute/values for overriden geometry. This field is for future use."""

class ReuseDesignElementInfo:
    """
    
ReuseDesignElementInfo is used as input for
            creating reuse Design Component and for substituting a reuse in an
            existing a shape or promissory Design Component.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned CreatedItemsOutput elements and Partial Errors
            associated with this input ItemProperties.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignModelElement
    """
            Business object reference to the Design Component to be substituted. It can be either
            a shape Design Component or a priomisorry
            Design Component.
            """
    BoType: str
    """This argument is not applicable for this operation."""
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The argument is not applicable for this operation"""
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Source Item revision to be realized to create a reuse. Any Item type other
            than ShapeDesign and its subtypes can be used for substitution.
            """
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """
RevisionRule to be applied to configure the structure of the source object
            (should it be an assembly). The configured structure objects will be realized in
            to the Product Design. If empty, the value will be defaulted based on the value set
            in the Cpd0DefaultDERevRule business constant.
            """
    BomView: str
    """
BomView type to be used to configure the structure of the source object. If
            empty, then it will be defaulted to the value set in the Cpd0DefaultBomViewPreference
            business constant. This argument is only required for creation of  reuse
            and  subordinate design components.
            """
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """Reserved for future."""
    Sos: Teamcenter.Soa.Client.Model.Strong.StoredOptionSet
    """Reserved for future."""
    UpdateSubordinates: bool
    """The argument is not applicable for this operation."""
    GuardLastModifiedDate: bool
    """The argument is not applicable for this operation"""
    LastModifiedDateGuard: System.DateTime
    """The argument is not applicable for this operation"""
    Transform: list[float]
    """
            Absolute transform which positions the source object in the coordinate system of
            the product design (units in meters), empty = identity, otherwise contains 16 doubles
            in the following order: { r00, r10, r20, p0, r01, r11, r21, p1, r02, r12, r22, p2,
            t0, t1, t2, s }, where the letter prefix signifies the following:
            

    r   a rotation component
            
    p  a perspective component
            
    t   the inverse scale.
            

"""
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            Reference to a DirectModel dataset to attach to reuse design component.
            This argument is optional.
            """
    BoundingBox: list[float]
    """
            Bounding box data (units in meters) in coordinate space of the product design; empty
            = no box.  Order of values is { x min, y min, z min, x max, y max, z max }.This is
            an optional argument.
            """
    AttrInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify additional property data for design control
            elements.  All values are specified as strings, the caller is responsible for generating
            the correct string representation of each value passed.  For tag values, the UID
            of the tag is used. To carry Variant expressions and Occurrence Effectivity expressions
            from source objects to corresponding subordinate design components during realization,
            the properties rlz0sync_variant_exprs and rlz0sync_effectivity_exprs
            must be set to true  accordingly. If closure rule is expected to be used as
            part of Item Realization, rlz0ClosureRule attribute should contain closure rule name.
            Closure rule will need to respect below validations.
            

Closure rule validation details:

            1.    Closure rule name is valid (closure rule object with that
            name exists)
            
            2.    Closure rule have associated closure rule clause(s)
            
            3.    Closure rule is self-sufficient i.e. it does not require
            any parameterized information for evaluation.
            

attrInfo parameter : Map of (std::string, std::string[])
            """
    LevelsOfSubordinatesToReturn: int
    """
            Number of levels of subordinate design components to be returned. Valid values
            are
            
            Negative 1  (return all subordinates of the reuse)
            
            0  (dont return any subordinate for the reuse)
            
            1  (return first level of subordinates only)
            

            Note: subordinate design components are created when the source object is an assembly.
            
"""
    GuardObjLastModifiedDate: bool
    """
            Flag, if set to true, causes the update of DesignControlElement to check last modified
            date to avoid data overwrite.
            """
    ObjLastModifiedDateGuard: System.DateTime
    """
            Modification date guard is used if guardObjLastModifiedDate
            is set to true. Object update will abort if the last modified date of the object
            is not same as objLastModifiedDateGuard.
            """
    AuxiliaryObjects: System.Collections.Hashtable
    """
            Information about auxiliary objects (attribute groups) attached to the design component
            to be created or updated.
            
auxiliarObjects is object of AuxiliaryObjectInfoMap which is map of relation property name
            to  AuxiliaryObjectInfo .
            
axiliaryObject paramter: Map of (std:string,AuxiliaryObjectInfo[])
            """
    RemoveOverride: int
    """
            Bitmask indicates which override to remove.  Reuse design component only has shape
            override. When it is set to 3(010), the shape override will be removed from the design
            component and member geometryOverrideDataset will be ingored.
            """
    ShapeOverrideInput: ShapeOverrideInfo
    """Input the overriden geometry."""

class ShapeDesignElementInfo:
    """
    
ShapeDesignElementInfo is used as input for creating shape Design Components
            and for substituting a shape in an existing a reuse or promissory Design
            Component.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned in CreatedItemsOutput elements and Partial Errors
            associated with this input ItemProperties.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignModelElement
    """
            The cpd0DesignElement business object reference to be substituted. It must
            be of category reuse or promissory
"""
    BoType: str
    """Empty string value .This argument is not applicable for this operation."""
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """This argument is not applicable for this operation."""
    CompoundCreateInput: Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CompoundCreateInput
    """
            Required for creating a new shape design component; otherwise, it should be
            empty.CompountCreateInput is a Map of relation
            property name to AuxiliaryObjectInfo. The property name must be the relation
            property on the main object which will be used to attach the auxiliary objects. AuxiliaryObjectInfo
            is used as input for creating or updating auxiliary objects along with main objects.
            For example, it can be used to pass information about attribute group objects to
            be created along with DesignElement


"""
    Transform: list[float]
    """
            Absolute transform which positions the shape in the coordinate system of the product
            design (units in meters), empty = identity, otherwise contains 16 doubles in the
            following order: { r00, r10, r20, p0, r01, r11, r21, p1, r02, r12, r22, p2, t0, t1,
            t2, s }, where the letter prefix signifies the following:
            

r     a rotation component
            
p     a perspective component
            
t     a translation component
            
s     the inverse scale.
            

"""
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            This is an optional argument. It is a DirectModel dataset to attach to shape
            design component.
            """
    TrueshapeDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            This is an optional argument . It is a reference to a dataset, containing Trushape
            information, to associate with the design component.Typically this will be a UGMASTER
            or DirectModel dataset.
            """
    BoundingBox: list[float]
    """
            Bounding box data (units in meters) in coordinate space of the Product Design; empty
            = no box. Order of values is { x min, y min, z min, x max, y max, z max }.
            """
    AttrInfo: System.Collections.Hashtable
    """
            This argument is not applicable for this operation.
            
attrInfo parameter : Map of (std::string, std::string[]) 


"""
    GuardObjLastModifiedDate: bool
    """
            This argument is not applicable for this operation.
            

"""
    ObjLastModifiedDateGuard: System.DateTime
    """This argument is not applicable for this operation."""
    AuxiliaryObjects: System.Collections.Hashtable
    """
            This argument is not applicable for this operation.
            
auxiliaryObjects is object of AuxiliaryObjectInfoMap
            which is map of relation property name to AuxiliaryObjectInfo .
            
axiliaryObject paramter: Map of (std:string,AuxiliaryObjectInfo[])
            """

class SubordinateDesignElementInfo:
    """
    
            SubordinateDesignElementInfo is used as input for applying overrides on "subordinate"
            DesignElement objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """client id"""
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignModelElement
    """required"""
    Transform: list[float]
    """Absolute transform (units in meters), empty vector == identity"""
    AttrInfo: System.Collections.Hashtable
    """
            extra attribute data for DE
            
attrInfo parameter : Map of (std::string, std::string[])
            """
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """DirectModel dataset to attach to SubordinateDesignElement as override"""
    BoundingBox: list[float]
    """
            Bounding box data (units in meters), empty = no box, otherwise contains 6 doubles
            in the following order:{ x-min, y-min, z-min, z-max, y-max, z-max }
            """
    GuardObjLastModifiedDate: bool
    """
            Flag, if set to true, causes the update of DesignControlElement to check last modified
            date to avoid data overwrite.
            """
    ObjLastModifiedDateGuard: System.DateTime
    """
            Modification date guard is used if guardObjLastModifiedDate is set to true. Object
            update will abort if the last modified date of the object is not same as objLastModifiedDateGuard.
            """
    AuxiliaryObjects: System.Collections.Hashtable
    """
            information about auxiliary objects to be created or updated.
            
auxiliarObjects is object of AuxiliaryObjectInfoMap which is map of relation property name
            to  AuxiliaryObjectInfo .
            
axiliaryObject paramter: Map of (std:string,AuxiliaryObjectInfo[])
            """
    RemoveOverride: int
    """
            Bitmask indicates which override to remove.  Subordiante design component can have
            position and shape override. When the first bit (01) is set to 1, the shape override
            will be removed from the design component and input Dataset geometryOverrideDataset
            will be ingored.  When the second bit ( 10) is set to 1, the position override will
            be removed and input memebers transform and boundingBox will be ignored. When both
            bit (11) is set to 1, both position and shape override will be removed and input
            memebers transform, boundingBox and geometryOverrideDataset will be ignored.
            """
    ShapeOverrideInput: ShapeOverrideInfo
    """Input the overriden geometry."""

class UpdateInstantiationContentInfo:
    """
    
            This structure is used for update scenirio on instantiated objects at target
            
            Application Model. Reuse DesignElement type and source model are required paramaters.
            This structure also contains attribute info that can be used to compare source and
            target properties for update, any miscellaneous info, and auxiliary object that are
            attached to suordinate Model Elements.
            
    """
    def __init__(self, ) -> None: ...
    ModelReuse: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignElement
    """
            Business Object Reference to an existing ModelReuse Container that needs to be updated.
            If none, supplied, it is assumed to create a new ModelContainer object in the targetModel;
            This is require parameter during Update. This acts as a Instantiation container object.
            """
    SourceModel: SourceModelInfo
    """
            Information on source model and configuration criteria to be applied to Instantiate
            a precise set of source objects in to the target model. If NULL, information used
            during instantiation create will be reused to configure the same model; In case of
            update, the user can chose a different source model instead of reusing the initial
            source model.
            """
    AttrInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify additional property data for design control
            elements. All values are specified as strings, the caller is responsible for generating
            the correct string representation of each value passed. For tag values, the UID of
            the tag is used.
            """
    MiscInfo: ReuseModelMiscInfo
    """
            This applies the additional information like information about the transforms, directModelDataset,trueshapeDataset
            and bounding box on the newly created reuse in the target model.  It is optional.
            """
    AuxiliaryObjects: Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.AuxiliaryObjectInfo
    """
            Information about auxiliary objects ( attribute groups ) attached to the design feature
            to be created or updated. AuxiliaryObjects is object of AuxiliaryObjectInfoMap which
            is map of relation property name to AuxiliaryObjectInfo.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateDesignElements(self, Input: CreateOrUpdateDesignElementsInfo) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignElementsResponse:
        """    
             Create or update  Design Components(Cpd0DesignElement) of categories "shape",
             "promissory",  "reuse" and "subordinate"  in an application
             model (Cpd0CollaborativeDesign) based on input structure.
             
             Creation of new "shape" design components includes creation of new ShapeDesign
             and ShapeDesignRevision objects. Creation of "reuse" design component forces
             creation of "subordinate" design components if the source item revision has
             structure.  Position and effectivity information for new or updated design components
             can be set using this operation. For subordinate design component, if position information
             is present for updated design component, a position override will be created on the
             surbodinate design component. For reuse and subordinate design component, shape override
             will created/updated when geometryOverrideDatasetInput is present.Override added
             to reuse and subordinate design component can be removed by this operation.
             


Use Cases:

             A design component represents the use of a standard part design, a design component,
             or a design assembly in a product. Design Components may be created by CAD applications
             or directly in the Teamcenter RAC UI using the Collaborative Product Development
             application.
             
             Design Components fall into one of the following categories:
             

shape design component
             
             The shape element represents a product specific design or other model specific design
             shape. A shape design component may become a reuse design component if the business
             standardizes on an existing product specific design. This change of purpose does
             not change the identity of the design component or affect its revision history.
             

reuse design component
             
             The reuse design component represents an instance of a component or assembly (e.g.
             standard part) in a product design.
             

subordinate design component
             
             The subordinate design component is created as the result of a reuse design
             component, when the source object has structure.
             

promissory design component
             
             The promissory design component is a placeholder that can later becomes a reuse
             or shape  design component.  A promissory design component does not
             have a source object.
             

             This API supports the design component authoring use cases. When the user directs
             the CAD system to save their session data, the CAD tool will invoke this API
             to populate or update the design component information in the Teamcenter database.
             
             
             Note: standard delete API are used to destroy or obsolete design components that
             are nolonger required.
             



             Use Case 1: Creation of new design components 

             Precondition: Any assembly to be realized into product design (as a reuse) must have
             a precise structure.
             

             The following operation can be used for creating design component in a product design.
             


Design Components are always created in the context of a product
             design (Cpd0CollaborativeDesign). Generally, in a production environment,
             a product design will be created ahead of time by an authorized user using the Collaborative
             Product Development application in Teamcenter RAC UI.  Applications will generally
             find an existing product design, using the Product Design saved query (provided
             OOTB in Teamcenter) or through a custom query.
             
However, for testing purposes, an application may wish to create
             a product design programmatically.To do this the createObjects
             operation should be used.
             
New design components can be created using operation createOrUpdateDesignElements. The application specifies the business
             object type for each new design component, and sets the product design (found or
             created previously) as its modelObject.  Additional property and positional element
             information is given and the operation invoked.
             
Design Components have a design component ID which is unique within
             the system. Applications can assign their own value using the cpd0design_element_id property. If this value is not specified
             in the input to createOrUpdateDesignElements,
             then Teamcenter will automatically assign an ID when it creates a new design control
             element.
             
During the operation, the server creates and saves the new design
             components in context of the product design. The operation returns the new objects
             to the caller.
             




             Use Case 2: Update of existing design component 

             The following operation can be used for updating existing design component in a
             product design.
             


Design Components are found by the application through search.
             
Existing design components can be updated using operation createOrUpdateDesignElements. The application specifies which
             design components are to be updated.  Note: the business object type and product
             design (modelObject) are not set on the input because they are already known to the
             design component and cannot be changed.
             
The application sets changed property values.
             
During the createOrUpdateDesignElements
             operation, the server updates and saves the design components along with its auxilliary
             objects if any.
             



Dependencies:

             autoAssignValues, getCreateDesc
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param Input: 

        :return: pair of objects for those newly created.
        """
        ...
    def CreateOrUpdateDesignFeatures(self, FeatureInfos: list[DesignFeatureInfo]) -> Cpd0.Services.Strong.Cpdcore._2011_06.DataManagement.CreateOrUpdateDesignFeaturesResponse:
        """    
             Creates or updates a list of design feature (Cpd0DesignFeature) objects and
             their relations to the design components they connect. Design features are used to
             represent welds (arc and spot), adhesive beads, etc. Design features are related
             to the design components they connect via a relation (Cpd0ConnectedElement).
             

             Using this API, applications can create and update design feature information in
             bulk, giving better through put that might not otherwise be achieved using standard
             object create and update API.
             

Cpd0ConnectedElement relationships have a copy stable ID which is unique within
             the scope of the design feature. The copy stable ID can be specified on create; if
             not specified, they will be automatically generated by Teamcenter. As their name
             suggests, when a design feature is copied the connected element relationships are
             also copied and the copy stable ID of the copied relations remains the same. The
             copy stable ID is used by external applications, like CAD, to correlate internal
             data to the related items.
             


Use Cases:

             This API supports the design feature authoring use cases. Design features (welds,
             etc.) are authored by users in a CAD application (versus being authored in Teamcenter
             RAC UI). When the user directs the CAD system to save their session data, the CAD
             tool will invoke this API to populate or update the design feature information in
             the Teamcenter database.
             

             Note: standard delete API (Core.DatamanagementService.deleteObjects(list(Cpd0DesignFeature)))
             is used to destroy or obsolete design features that are no longer required.
             

             Use Case 1: Creation of new design feature


             The following operation can be used for creating design features (e.g. welds) in
             a product design.
             

             Design features are created always in the context of a product design (Cpd0CollaborativeDesign.
             Generally, in a production environment, a product design will be created ahead of
             time by an authorized user using the Collaborative Product Development application
             in Teamcenter RAC UI. Applications will generally find an existing product design,
             using the Product Design saved query (provided OOTB in Teamcenter) or through a custom
             query.
             
             However, for testing purposes, an application may wish to create a product design
             programmatically. To do this the createObjects operation should be used.
             
             New design features can be created using operation createOrUpdateDesignFeatures.
             The application specifies the business object type for each new design feature, and
             sets the product design (found or created previously) as its modelObject. Additional
             property and connected element information is given and the operation invoked.
             
             Design features have a ID which is unique within the system. Applications can assign
             their own value using the cpd0design_feature_id
             property. If this value is not specified in the input to createOrUpdateDesignFeatures,
             then Teamcenter will automatically assign an ID when it creates of new design feature.
             
             During the operation, the server creates and saves the new design features in context
             of the product design. It also creates and saves the relationship between the design
             features and their connected design components. The operation returns the new objects
             to the caller.
             

             Use Case 2: Update of existing design feature


             The following operation can be used for updating existing design features (e.g. welds)
             in a product design.
             

             Design features are found by the application through search or by navigating from
             a design component (Cpd0DesignElement) via the connected element (Cpd0ConnectedElement)
             relation. Note: the design feature is always the primary object of the Cpd0ConnectedElement
             relation and the design component is always the secondary object.
             
             The existing design features can be updated using operation createOrUpdateDesignFeatures. The application specifies which
             design features are to be updated. Note: the business object type and product design
             (modelObject) are not set on the input because
             they are already know to the design feature and cannot be changed. The application
             sets changed property values and specifies connected element information for the
             feature.
             
             During the operation, the server updates and saves the design features and adds or
             removes Cpd0ConnectedElement relations to
             be consistent with the input..
             



Dependencies:

             autoAssignValues, getCreateDesc
             

Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param FeatureInfos: 
                         The input list of design feature information describing the features to be created
                         or updated.
             
        :return: 
        """
        ...
    def CreateOrUpdateDesignSubsetElements2(self, SubsetInfos: list[DesignSubsetElementInfo2]) -> CreateOrUpdateDesignSubsetElementsResponse2:
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
    def CreateOrUpdateModelToModelInstantiation(self, InstantiationInfo: ModelToModelInstantiationInfo) -> ModelToModelInstantiationResponse:
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

