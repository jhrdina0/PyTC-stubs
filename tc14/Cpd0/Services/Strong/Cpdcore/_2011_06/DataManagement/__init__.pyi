import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AuxiliaryObjectInfo:
    """
    
            AuxiliaryObjectInfo is used as input for creating or updating auxiliary objects along
            with main objects. For example, it can be used to pass information about attribute
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
            Auxiliary object to be updated.  This field is empty when auxiliary object is being
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

class CompoundCreateInfo:
    """
    Generic CreateInfo construct to support compound object create
    """
    def __init__(self, ) -> None: ...
    BoType: str
    """The name of the Business Object type to be created."""
    AttrInfo: System.Collections.Hashtable
    """
            This contains property data for the newly created object. It is a map of property
            and values for the newly created object.  All property values are expressed in their
            string equivalent.  Object reference (tag) values can be passed using the client
            string representation (e.g. UID) of the referenced object.  Array values are always
            treated as replacement for entire array content.  Non array values are passed as
            first element in value list. It is basically a map of String (Property Name) to Property
            Value (List of Strings)\
            
attrInfo is object of AttributeInfoMap.
            
attrInfo parameter : Map of (std::string, std::string[])
            """
    CompoundInfo: System.Collections.Hashtable
    """
            Compound object data. CompoundCreateInfoMap
            is a map of property name to CompoundCreateInfo.
            It is basically a map of String (property Name) to property Value (CompoundCreateInfo) which in turn describes a different object
            to be created.
            """

class CompoundCreateInput:
    """
    Input for creating a new Shape design item.
    """
    def __init__(self, ) -> None: ...
    CreateInfo: CompoundCreateInfo
    """
            Input to create Shape Design Item, Shape Design Revision data and respective master
            forms
            """
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """NULL. This argument is not applicable for this operation."""

class ControlModelInfo:
    """
    
            ControlModelInfo is used as input to describe control model relations between a Cpd0DesignControlElement
            and the Cpd0DesignElements and the Cpd0DesignFeatures generated from
            the control model (e.g. mechanical routing or weld seam) managed by the design control
            element.
            

            At a minimum, applications must specify the secondaryObject (the DesignElement or DesignFeature).
            Normally, applications will want to keep track, internally, how this relation maps
            to the applications data model.   In that case, the application should set the clientId
            for new relations, the corresponding relation and csId will be returned to the application
            in a map based on the input clientId. (Note: the clientId values must unique within
            the entire input set).
            

            If the application is intending to replace a connected part relation with another
            relation having the same copy stable ID then the applicaiton may pass the original
            csId as input and Teamcenter will use that
            to remove and replace the relation having that csId.
            If the csId is not specified Teamcenter
            will generate them automatically.
            

    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended.  It is used for mapping server
            errors and for correlating data in the response to the inputs.  The caller should
            populate each ControlModelInfo with a value that is unique within the input
            set.   The value is not interpreted or manipulated internally by the server.
            """
    CsId: str
    """Copy stable ID; optional, except for replace requests"""
    SecondaryObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            specifies object to relelate.  If set to NULLTAG, csId must not be empty (nulltag
            signifies remove of control model relation for csId)
            """
    AttrInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify additional property data for the relation.
            All values are specified as strings, the caller is responsible for generating the
            correct string representation of each value passed.  For tag values, the UID of the
            tag is used.
            
attrInfo is object of AttributeInfoMap.
            
attrInfo parameter : Map of (std::string, std::string[])
            """

class CreateOrUpdateDesignControlElementsResponse:
    """
    
            It contains a map of input client ID to the objects that were created or updated.
            It also returns a map of the control element to the ShapeDesign
            created for it. It also returns a map of the secondaryObject listed in the ControlModelInfo
            to the corresponding copy stable ID of the control model relation that references
            it.
            
    """
    def __init__(self, ) -> None: ...
    ClientIDMap: System.Collections.Hashtable
    """
            map of client id to corresponding object (DesignControlElement)
            that was created
            
csIdMap is object of StringToBoMap.
            
StringToBoMap parameter : Map of(std::string ,Teamcenter::BusinessObject)
            """
    ShapeDesigns: System.Collections.Hashtable
    """
            map of DesignControlElement to  NewShapeDesignData.
            """
    CsIdMap: System.Collections.Hashtable
    """
            map of added controlled elements to their copy stable ID
            
csIdMap is object of BoToStringMap.
            
BoToStringMap parameter : Map of(Teamcenter::BusinessObject, std::string )
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains list of added, updated, or deleted objects.  Also contains list of any errors
            which occurred within the call.
            """

class CreateOrUpdateDesignElementsInfo:
    """
    
            CreateOrUpdateDesignElementsInfo is used as input into createOrUpdateDesignElements.It
            contains a lists if input for creating or updating "shape", "reuse", "promissory"
            and "subordinate" DesignElement objects.
            
    """
    def __init__(self, ) -> None: ...
    ShapeDesignElements: list[ShapeDesignElementInfo]
    """shapeDesignElements"""
    ReuseDesignElements: list[ReuseDesignElementInfo]
    """reuseDesignElements"""
    PromissoryDesignElements: list[PromissoryDesignElementInfo]
    """promissoryDesignElements"""
    SubordinateDesignElements: list[SubordinateDesignElementInfo]
    """subordinateDesignElements"""

class CreateOrUpdateDesignElementsResponse:
    """
    
            It contains a map of input client ID to the objects that were created or updated.
            It also returns a map of returned subordinates; where key is reuse
            design components and value is a vector of subordinate design components.
            Number of subordinates returned is governed by the levelsOfSubordinatesToReturn
            value specified on input for each reuse design components. It also returns
            ShapeDesign and ShapeDesignRevision
            pair of objects for those newly created.
            
    """
    def __init__(self, ) -> None: ...
    ClientIDMap: System.Collections.Hashtable
    """
            map of client ID to corresponding object (Cpd0DesignElement) that was created
            
clientIDMap is object of StringToBoMap.
            
clientIDMap parameter: Map of (std::string,Teamcenter::BusinessObject)
            """
    ShapeDesigns: System.Collections.Hashtable
    """map of design components to  new shape design revision."""
    ShapeOverrideDesigns: System.Collections.Hashtable
    """This is for overrides geometry. Map of design components to  new shape design revision."""
    UnmappedEffectivityEncountered: list[Teamcenter.Soa.Client.Model.Strong.Cpd0DesignElement]
    """
            A list of reuse design components where effectivity conditions are encountered
            in the realized item structure.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains list of added, updated, or deleted objects.  Also contains list of any errors
            which occurred within the call.
            """
    SubordinateElements: System.Collections.Hashtable
    """
            A map of reuse design component(Key) and a list of its subordinate
            design components(Values). The list of subordinate designelements will be
            governed by the input argument levelsOfSubordinatesToReturn
            
subordinateElements is object of BoToBoVectorMap.
            
subordinateElements parameter : Map of (Teamcenter:BusinessObject,Teamcenter:Business Object[]
            )
            """

class CreateOrUpdateDesignFeaturesResponse:
    """
    
            The response contains  map of input caller specified client ID values and the corresponding
            objects that were created/updated features. The response also contains a map of caller
            specified client ID values for (connected element) relations and their corresponding
            copy stable ID values. The service data contains a list of added, updated, or deleted
            objects and it also contains a list of any errors which occurred within the call.
            
    """
    def __init__(self, ) -> None: ...
    ClientIDMap: System.Collections.Hashtable
    """
            Map of client ID to corresponding object (Cpd0DesignFeature) that was created.
            
clientIDMap is object of StringToBoMap.
            
clientIDMap parameter : Map of (std:string,Teamcenter:BusinessObject)
            """
    ConnectionIDMap: System.Collections.Hashtable
    """
            Map of client ID, specified in DesignFeatureConnectionInfo, to the copy stable ID
            of the corresponding relation.
            
connectionIDMap object of StringToStringMap

connectionIDMap parameter : Map of (std:string,std:string)
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains list of added, updated, or deleted objects.  Also contains list of any errors
            which occurred within the call.
            """

class CreateOrUpdateDesignSubsetElementsResponse:
    """
    
            Response to createOrUpdateDesignDSubsetElements.   It contains a list of design subset
            element data which is one to one correspondance with input subset element info.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """added, updated, deleted object data plus any error information"""
    DseData: list[DesignSubsetElementData]
    """
            A list of design subset element data which has one to one correpondance with input
            subset element info.
            """

class DesignControlElementsInfo:
    """
    
DesignControlElementsInfo is used as input
            to describe create or update request for a Cpd0DesignControlElement. New Cpd0DesignControlElement
            objects require creation of a new Cpd0ShapeDesign objects.
            
            Transform and bounding box can be optionally specified. Note: Changing the
            transform of a control model in Teamcenter does not affect a change in position of
            the elements that it produced.
            
            Changes to Cpd0ControlModel relations are passed as a set of delta (adds,removed,replace,
            delete) requests.
            

The add requests from new relations.
            
The remove requests discard existing relations.
            
The replace requests do a remove and an add retaining the same csIS
            on the new relation that existed on the old;the copy stable ID(csId) must be specified
            in the ControlModelInfo for any requests.
            
The delete requests discard the existing relation and then attempts
            to delete the object it referenced.
            


            Effectivity is specified in attrInfo in its string form via the mdl0effectivity_formula property.  Effectivity is applied after
            control model relation updates.  The effectivity condition can be cascaded to the
            design components and features that were generated/updated by the design control
            element. The cascade of effectivity takes into considerations the fact that the controlled
            elements may be shared between (revisions of) design control elements and, in that
            case, applies a combined effectivity of each revision to the shared elements.There
            may be cases when effectivity cannot be cascaded to a design component or feature
            (e.g. it may be owned by a different site). In that case, a warning is generated
            and the change will need to be reconciled manually.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended.  It is used for mapping server
            errors and for correlating data in the response to the inputs. The caller should
            populate each DesignControlElementInfo with
            a value that is unique within the input set. The value is not interpreted or manipulated
            internally by the server.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignControlElement
    """
            A design control element to be updated.  Required for updating an existing DesignControlElement, empty otherwise
            """
    BoType: str
    """
            required for creating new DesignControlElement,
            empty otherwise
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The product design which will contain the new design control element; required for
            new DesignControlElement, empty otherwise
            """
    CompoundCreateInput: CompoundCreateInput
    """
            Creation input for corresponding Cpd0ShapeDesignRevison; required for creating
            new DesignControlElement, empty otherwise
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
            = no box.  Order of values is { x min, y min, z min, x max, y max, zmax }.
            """
    AttrInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify additional property data for design control
            elements.  All values are specified as strings, the caller is responsible for generating
            the correct string representation of each value passed.  For tag values, the UID
            of the tag is used.
            
attrInfo parameter : Map of (std::string, std::string[])
            """
    AddControlledElements: list[ControlModelInfo]
    """
            Specifies the set of objects (design components and design features) this control
            model manages. Control model (Cpd0ControlModel) relations in Teamcenter will
            be created such that they match the entries in the addControlledElements
            list.
            """
    RemoveControlledElements: list[ControlModelInfo]
    """
            Specifies the set of objects (design components and design features) this control
            model no longer manages. The corresponding Control model (Cpd0ControlModel)
            relations Teamcenter will be deleted; the design components and design features will
            not be deleted.
            """
    ReplaceControlledElements: list[ControlModelInfo]
    """
            Specifies the set of objects (design components and design features) this control
            model that are replaced by another object. The corresponding Control model (Cpd0ControlModel)
            relations in Teamcenter will be deleted then re created referencing the replacing
            object; the copy stable ID from the old relation will be reused for the new relation.
            The replaced design components and design features will not be deleted.
            """
    DeleteControlledElements: list[ControlModelInfo]
    """
            Specifies the set of objects (design components and design features) this control
            model no longer manages. The corresponding Control model (Cpd0ControlModel)
            relations Teamcenter will be deleted; once the relations are deleted, Teamcenter
            will attempt to delete the corresponding design components and design features.
            """
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            Reference to a DirectModel dataset to associate with the design feature.
            Value can be null.
            """
    TrueshapeDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            Reference to a dataset, containing Trushape information, to associate with the design
            feature.  Typically this will be a UGMASTER or DirectModel dataset.
            Optional.
            """
    GuardObjLastModifiedDate: bool
    """
            Flag, if set to true, causes the update of design feature to check last modified
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
            Information about auxiliary objects (attribute groups) attached to the design feature
            to be created or updated.
            
auxiliarObjects is object of AuxiliaryObjectInfoMap.
            
axiliaryObject paramter: Map of (std:string,AuxiliaryObjectInfo[])
            """

class DesignFeatureConnectionInfo:
    """
    
DesignFeatureConnectionInfo is used as input
            for creating or updating the set of design components connected to the design feature.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended.  It is used for mapping server
            errors and for correlating data in the response to the inputs.  The caller should
            populate each DesignFeatureConnectionInfo
            with a value that is unique within the input set. The value is not interpreted or
            manipulated internally by the server.
            """
    DesignElement: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignModelElement
    """
            Connected design component, required.  The design component must exist in the same
            product design as the design feature.
            """
    CsId: str
    """
            Copy stable ID, required when replacing once connected with another, otherwise optional.
            Also, if designElement is set to NULLTAG
            during a replace, the connected info is removed from Teamcenter.
            """
    AttrInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify additional property data for the relation.
            All values are specified as strings, the caller is responsible for generating the
            correct string representation of each value passed.  For tag values, the UID of the
            tag is used.
            
attrInfo parameter : Map of (std::string, std::string[])
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
            The use of this value is optional, but recommended.  It is used for mapping server
            errors and for correlating data in the response to the inputs. The caller should
            populate each DesignFeatureInfo with a value
            that is unique within the input set. The value is not interpreted or manipulated
            internally by the server.
            """
    Feature: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignFeature
    """
            A reference to a design feature to be updated.  A value is required for update, otherwise
            (create case) this value should be empty
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
            of values corresponds to PLMXML standard. An empty vector is interpreted as an identity
            matrix.
            """
    AttrInfo: System.Collections.Hashtable
    """
            A set of name value pairs used to specify additional property data for design features.
            All values are specified as strings, the caller is responsible for generating the
            correct string representation of each value passed.  For tag values, the UID of the
            tag is used.
            
attrInfo parameter : Map of (std::string, std::string[])
            """
    ConnectedInfo: list[DesignFeatureConnectionInfo]
    """
            List  of objects to which the design feature is connected. The connected element
            (Cpd0ConnectedElement) relations in Teamcenter will be created/updated/removed
            such that they match the entries in the connectedInfo
            list, unless the mergeConnected option is set to true.  If mergeConnected option
            is false, relations not referenced in the input will not be automatically removed
            from the feature.
            """
    MergeConnected: bool
    """
            flag, when set to true, indicates that connected info should be merged with existing
            content in Teamcenter; otherwise all connected data is replaced for the feature.
            If no connected information for this feature currently exists in Teamcenter, then
            merge and replace have the same effect.
            """
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            Reference to a DirectModel dataset to associate with the design feature.Value
            can be null.
            """
    TrueshapeDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            Reference to a dataset, containing Trushape information, to associate with the design
            feature.  Typically this will be a UGMASTER or DirectModel dataset.
            Optional.
            """
    GuardObjLastModifiedDate: bool
    """
            Flag, if set to true, causes the update of design feature to check last modified
            date to avoid data overwrite.
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

class DesignSubsetElementData:
    """
    
            Response to createOrUpdateDesignSubsetElements
            contains information about DesignSubsetElements
            created or updated, its clientId, its CopyStable Id.  It also contains a list of
            appended and removed DesignElements from
            the workSetModel.
            
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
    AppendedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement]
    """Contains list of appended source elements."""
    RemovedSourceElementList: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement]
    """Contains list of removed source elements."""

class DesignSubsetElementInfo:
    """
    
            Data on DesignSubsetElementInfo used to create
            or update DesignSubsetElements in a workset.
            


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
            Business Object reference to an existing DesignSubsetElements
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
            Business object reference to the Product Design from which contect is being instanced,
            optional for update usecase.
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
    AppendSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement]
    """
            A list of business object references of the object to be append from sourceModel into the modelObject
            i.e the list of objects to be Appended from sourceModel into worksetModel.
            """
    RemoveSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement]
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
    SubordinateSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement]
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
            This flag specifies if the children of  design components  specified in removeSourceElements input parameter must also be removed  from
            worksetModel. It is set to false by
            default. It this is false, it is expected that removeSourceElements
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

class NewShapeDesignData:
    """
    
NewShapeDesignData is used for returning
            the pair of new Cpd0ShapeDesign and Cpd0ShapeDesignRevision objects
            newly created by a service.
            
    """
    def __init__(self, ) -> None: ...
    ShapeDesign: Teamcenter.Soa.Client.Model.Strong.Cpd0ShapeDesign
    """New Cpd0ShapeDesign object"""
    ShapeDesignRevsion: Teamcenter.Soa.Client.Model.Strong.Cpd0ShapeDesignRevision
    """New Cpd0ShapeDesignRevision object"""

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
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignElement
    """
            The promissory  design component to be updated or substituted. Can be empty
            otherwise.
            """
    BoType: str
    """
            The business object type of a design component to be created.  This value is required
            for creating a new design component, and must be a valid subtype of Cpd0DesignElement.
            For update of an existing design component, this value should be empty.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Product Design for creating a new promissory  design component. Can be empty
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
            elements.  All values are specified as strings, the caller is responsible for generating
            the correct string representation of each value passed.  For tag values, the UID
            of the tag is used.
            
attrInfo parameter : Map of (std::string, std::string[])
            """
    GuardObjLastModifiedDate: bool
    """
            Flag, if set to true, causes the update of DesignElement
            to check last modified date to avoid data overwrite.
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

class RelatedObjectFilter:
    """
    
            This filter can specify a combination of the type of the relation to traverse, the
            possible attributes on the relation, and the type of Business Object at the other
            end of that relation. An empty string denotes no filter (acts as a wildcard returning
            all objects without filtering the particular aspect that is not specified).
            

            The combination of filters specified by relatedTypeName,
            all filters and otherSideObjectTypeName
            are combined together with a logical AND operation, meaning all criteria must be
            met for the related object to be returned to the caller.
            

WARNING:  Any attribute filter other than mdl0cs_id,
            if passed in, will cause a not mplemented error and a service exception.  This service
            may be extended in the future to support filtering on any relation attribute.
            

    """
    def __init__(self, ) -> None: ...
    RelationTypeName: str
    """
            Filters based on the type of relation between the sourceObject and the related object.
            If not specified, then all relations from the source object are evaluated.
            """
    Filters: list[RelationAttributeFilter]
    """
            Filters based on a list of relation attribute values.  If the list is empty, then
            no relationship attribute filtering is applied.  NOTE: Currently only one attribute
            (mdl0cd_id) is supported
            """
    OtherSideObjectTypeName: str
    """
            Filters based on the type of the object related to the sourceObject.  If not specified,
            then all related objects are evaluated, irrespective of their type.
            """

class RelatedObjectInput:
    """
    
            The RelatedObjectInput construct expresses
            a set of filter criteria to be applied to objects related to a sourceObject.  Multiple
            instances of RelatedObjectFilter are combined
            together with a logical OR, meaning if a related object matches any of the filter
            criteria, it will be returned to the caller.
            
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            The input (source) object for which related objects are to be found.  This value
            is required; an empty sourceObject results in an exception being thrown.
            """
    Filters: list[RelatedObjectFilter]
    """
            A set of filters to apply to the objects related to the sourceObject.  An empty filter
            list denotes no filter ( acts as a wildcard returning all objects without filtering).
            """

class RelatedObjectOutput:
    """
    
RelatedObjectOutput contains the result corresponding
            to one source object. It returns the input source object itself, the related object
            at the other end of the relation, and the relation itself.
            
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.ModelObject
    """source object specified in RelatedObjectInput"""
    RelationInfos: list[RelationInfo]
    """
            A list of relationInfo which contains the
            filtered and configured results of the query.
            """

class RelatedObjectsResponse:
    """
    
RelatedObjectsResponse is used to return
            the results of a call to either queryRelatedPrimaryObjects
            or queryRelatedSecondaryObjects.  It contains
            a set of all objects that satisfy any one or more of the input filter criteria and
            that satisfy the input configuration criteria.
            
    """
    def __init__(self, ) -> None: ...
    OutputObjects: list[RelatedObjectOutput]
    """
            A list of RelatedObjectOutput which correspond
            to the inputs.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains a  list of any errors which occurred within the call."""

class RelationAttributeValues:
    """
    
            This structure contains the values to filter a relation attribute by.  Only one of
            the fields in RelationAttributeValues should
            be populated, the field populated must correspond to the value of RelationAttributeDataType in the RelationAttributeFilter.
            Multiple values, if passed in, are logically grouped with OR, meaning if any of
            the values match, the relation will pass through the filter.
            
    """
    def __init__(self, ) -> None: ...
    BooleanValues: list[bool]
    """A list of boolean values"""
    IntegerValues: list[int]
    """A list of integer values"""
    StringValues: list[str]
    """A list of string values; string value comparisions are case sensitive."""
    DoubleValues: list[float]
    """A list of double values"""
    DateValues: list[System.DateTime]
    """A list of date values"""
    TagValues: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of tag values"""

class RelationAttributeFilter:
    """
    
            This structure specifies a filter on one attribute of a relation.  A mismatch between
            the attributeType and the attributeValues data type results in an invalid input error and
            an SOA exception.  Any attribute other than mdl0cs_id,
            if passed in, will cause a not mplemented error and an SOA exception.
            
    """
    def __init__(self, ) -> None: ...
    AttributeName: str
    """Name of the attribute to be filtered. Cannot be an empty stringFilters"""
    AttributeType: str
    """
            The data type of the attribute to be filtered.  Supported values are:
            

BooleanType
            
IntegerType
            
StringType
            
DoubleType
            
DateType
            
TagType
            

"""
    AttributeValues: RelationAttributeValues
    """A list of values to filter by.  At least one value of the proper type must be specified."""

class RelationInfo:
    """
    
RelationInfo contains the result data for
            one related object in the output, for a given relation.
            
    """
    def __init__(self, ) -> None: ...
    OtherSideObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object found on the other side of the relation."""
    RelationObject: Teamcenter.Soa.Client.Model.Strong.Mdl0CopyStableRelation
    """
            The relation object which relates otherSideObject
            to the sourceObject.
            """

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
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignElement
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
            part of Item Realization, rlz0ClosureRule attribute should contain closure
            rule name. Closure rule will need to respect below validations.
            

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
    GeometryOverrideShapeCreateInput: CompoundCreateInput
    """geometryOverrideShapeCreateInput"""
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

class ShapeDesignElementInfo:
    """
    
ShapeDesignElementInfo is used as input for creating shape Design Components
            and for substituting a shape in an existing a reuse or promissory
            Design Component.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned in CreatedItemsOutput elements and Partial Errors
            associated with this input ItemProperties.
            """
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignElement
    """
            The cpd0DesignElement business object reference to be substituted. It must
            be of category reuse or promissory.
            """
    BoType: str
    """Empty string value .This argument is not applicable for this operation."""
    ModelObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """This argument is not applicable for this operation."""
    CompoundCreateInput: CompoundCreateInput
    """
            Required for creating a new shape design component; otherwise, it should be
            empty.CompountCreateInput is a Map of relation
            property name to AuxiliaryObjectInfo. The
            property name must be the relation property on the main object which will be used
            to attach the auxiliary objects. AuxiliaryObjectInfo is used as input for creating
            or updating auxiliary objects along with main objects. For example, it can be used
            to pass information about attribute group objects to be created along with DesignElement
"""
    Transform: list[float]
    """
            Absolute transform which positions the shape in the coordinate system of the product
            design (units in meters), empty = identity, otherwise contains 16 doubles in the
            following order: { r00, r10, r20, p0, r01, r11, r21, p1, r02, r12, r22, p2, t0, t1,
            t2, s }, where the letter prefix signifies the following:
            

 r      a rotation component
            
 p      a perspective component
            
 t      a translation component
            
 s      the inverse scale.
            

"""
    DirectModelDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            This is an optional argument. It is a DirectModel dataset to attach to shape
            design component.
            """
    TrueshapeDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            This is an optional argument . It is a  reference to a dataset, containing Trushape
            information, to associate with the design component.Typically this will be a UGMASTER
            or DirectModel dataset.
            """
    BoundingBox: list[float]
    """
            Bounding box data (units in meters) in coordinate space of the Product Design; empty
            = no box.  Order of values is { x min, y min, z min, x max, y max, z max }.
            """
    AttrInfo: System.Collections.Hashtable
    """
            This argument is not applicable for this operation.
            
attrInfo parameter : Map of (std::string, std::string[])
            """
    GuardObjLastModifiedDate: bool
    """This argument is not applicable for this operation."""
    ObjLastModifiedDateGuard: System.DateTime
    """This argument is not applicable for this operation."""
    AuxiliaryObjects: System.Collections.Hashtable
    """
            This argument is not applicable for this operation.
            
auxiliarObjects is object of AuxiliaryObjectInfoMap which is map of relation property name
            to  AuxiliaryObjectInfo .
            
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
    Element: Teamcenter.Soa.Client.Model.Strong.Cpd0DesignElement
    """required"""
    Transform: list[float]
    """Absolute transform (units in meters), empty vector == identity"""
    AttrInfo: System.Collections.Hashtable
    """
            extra attribute data for DE
            
attrInfo parameter : Map of (std::string, std::string[])
            """
    GeometryOverrideShapeCreateInput: CompoundCreateInput
    """
            geometryOverrideShapeCreateInput is used by applications that required items for
            managing their data files.  Specifying this input creates a ShapeDesign to hold override
            geometry for the subordinate design component.
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

class SubstituteAsReuseDesignElementResponse:
    """
    
            Contains a map of client id (provided in input) to the reuse Design Component. It
            has Service Data with created/updated/deleted objects along with any partial errors.
            
    """
    def __init__(self, ) -> None: ...
    ClientIDMap: System.Collections.Hashtable
    """
            This is a map of client id to corresponding object (Cpd0DesignElement) that was substituted
            (String/Business object).
            
clientIDMap is object of StringToBoMap

clientIDMap parameter : Map of (std:string, Teamcenter:BusinessObject)
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This contains added and updated objects. It also contains partial errors, if any"""

class SubstituteAsShapeDesignElementResponse:
    """
    
            Contains a map of client id (provided in input) to the Shape Design Component. It
            has a map of Shape Design Components to the corresponding Shape Design and Shape
            Design Revision objects. It has Service Data with created/updated/deleted objects
            along with any partial errors.
            
    """
    def __init__(self, ) -> None: ...
    ClientIDMap: System.Collections.Hashtable
    """
            This is a map of client id to corresponding business object reference (Cpd0DesignElement)
            that was substituted.
            
clientIDMap is object of StringToBoMap

clientIDMap parameter : Map of (std:string, Teamcenter:BusinessObject)
            """
    ShapeDesigns: System.Collections.Hashtable
    """
            This is a map of Cpd0DesignElement business object reference to newly created shape
            designs.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """This contains added and updated objects. It also contains partial errors, if any"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateDesignControlElements(self, ElementInfos: list[DesignControlElementsInfo]) -> CreateOrUpdateDesignControlElementsResponse:
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
    def CreateOrUpdateDesignElements(self, Input: CreateOrUpdateDesignElementsInfo) -> CreateOrUpdateDesignElementsResponse:
        """    
             Create or update  Design Components(Cpd0DesignElement) of categories shape,
             promissory,  reuse  and subordinate  in an application  model
             (Cpd0CollaborativeDesign) based on input structure.
             
             Creation of new shape design components includes creation of new ShapeDesign and ShapeDesignRevision
             objects. Creation of reuse design component forces creation of subordinate
             design components if the source item revision has structure.  Position and effectivity
             information for new or updated design components can be set using this operation.
             


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
<ul>
<li type="disc"><font face="courier" height="10">ShapeDesignElementInfo</font> is
                         to create or update <i>shape</i> design components.
                         </li>
<li type="disc"><font face="courier" height="10">PromissoryDesignElementInfo</font>
                         is to create or update <i>promissory</i> design components.
                         </li>
<li type="disc"><font face="courier" height="10">ReuseDesignElementInfo</font> is
                         to create or update <i>reuse</i> and <i>subordinate</i> design components.
                         </li>
</ul>

        :return: 
        """
        ...
    def CreateOrUpdateDesignFeatures(self, FeatureInfos: list[DesignFeatureInfo]) -> CreateOrUpdateDesignFeaturesResponse:
        """    
             Creates or updates a list of design feature (Cpd0DesignFeature) objects and
             their relations to the design components they connect.  Design features are used
             to represent welds (arc and spot), adhesive beads, etc.   Design features are related
             to the design components they connect via a relation (Cpd0ConnectedElement).
             

             Using this API, applications can create and update design feature information in
             bulk, giving better through put that might not otherwise be achieved using standard
             object create and update API.
             

Cpd0ConnectedElement relationships have a copy stable ID which is unique within
             the scope of the design feature.  The copy stable ID can be specified on create;
             if not specified, they will be automatically generated by Teamcenter.  As their name
             suggests, when a design feature is copied the connected element relationships are
             also copied and the copy stable ID of the copied relations remains the same.  The
             copy stable ID is used by external applications, like CAD, to correlate internal
             data to the related items.
             


Use Cases:

             This API supports the design feature authoring use cases.   Design features (welds,
             etc.) are authored by users in a CAD application (versus being authored in Teamcenter
             RAC UI).  When the user directs the CAD system to save their session data,
             the CAD tool will invoke this API to populate or update the design feature information
             in the Teamcenter database.
             
             Note: standard delete API are used to destroy or obsolete design features that are
             no longer required.
             
             Use Case 1: Creation of new design feature 


             The following operation can be used for creating design features (e.g. welds) in
             a product design.
             

Design features are  created always in the context of a product design
             (Cpd0CollaborativeDesign. Generally, in a production environment, a product design
             will be created ahead of time by an authorized user using the Collaborative Product
             Development application in Teamcenter RAC UI. Applications will generally find an
             existing product design, using the Product Design saved query (provided OOTB
             in Teamcenter) or through a custom query.
             
However, for testing purposes, an application may wish to create
             a product design programmatically. To do this the createObjects
             operation should be used.
             
New design features can be created using operation createOrUpdateDesignFeatures. The application specifies the business
             object type for each new design feature, and sets the product design (found or created
             previously) as its modelObject. Additional property and connected element information
             is given and the operation invoked.
             
Design features have a ID which is unique within the system. Applications
             can assign their own value using the cpd0design_feature_id
             property.  If this value is not specified in the input to createOrUpdateDesignFeatures,
             then Teamcenter will automatically assign an ID when it creates of new design feature.
             
During the operation, the server creates and saves the new design
             features in context of the product design. It also creates and saves the relationship
             between the design features and their connected design components. The operation
             returns the new objects to the caller.
             



             Use Case 2: Update of existing design feature


             The following operation can be used for updating existing design features (e.g.
             welds) in a product design.
             

Design features are found by the application through search or by
             navigating from a design component (Cpd0DesignElement) via the connected element
             (Cpd0ConnectedElement) relation.  Note: the design feature is always the primary
             object of the Cpd0ConnectedElement relation and the design component is always the
             secondary object.
             
The existing design features can be updated using operation createOrUpdateDesignFeatures. The application specifies
             which design features are to be updated.  Note: the business object type and product
             design (modelObject) are not set on the input
             because they are already know to the design feature and cannot be changed. The application
             sets changed property values and specifies connected element information for the
             feature.
             
During the operation, the server updates and saves the design features
             and adds or removes Cpd0ConnectedElement
             relations to be consistent with the input..
             



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
    def CreateOrUpdateDesignSubsetElements(self, SubsetInfos: list[DesignSubsetElementInfo]) -> CreateOrUpdateDesignSubsetElementsResponse:
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
    def QueryRelatedPrimaryObjects(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, InputObjects: list[RelatedObjectInput]) -> RelatedObjectsResponse:
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
    def QueryRelatedSecondaryObjects(self, ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, InputObjects: list[RelatedObjectInput]) -> RelatedObjectsResponse:
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
    def SubstituteAsReuseDesignElement(self, SubstituteInfos: list[ReuseDesignElementInfo]) -> SubstituteAsReuseDesignElementResponse:
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
    def SubstituteAsShapeDesignElement(self, SubstituteInfos: list[ShapeDesignElementInfo]) -> SubstituteAsShapeDesignElementResponse:
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

