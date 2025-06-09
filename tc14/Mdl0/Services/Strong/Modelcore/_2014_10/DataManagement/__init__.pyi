import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AuxObjectInfo:
    """
    
            Any special attributes to be set on to the newly created target object for a given
            source object can be supplied using this structure. This argument is optional.
            
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            Business object reference to source object for which custom attributes needs to copied
            over to its corresponding Target object
            """
    AttrInfo: System.Collections.Hashtable
    """
            Bag of Attributes to be set on the corresponding target object for a given source
            object
            """

class CloneModelContentInfo:
    """
    
CloneModelContentInfo is a construct used
            as input to support cloning of model elements from source model to target model.
            
    """
    def __init__(self, ) -> None: ...
    CreateInfo: list[SourceTargetContentInfo]
    """
            Specifies a list of source-target content information structures that is supplied
            as input to the Clone operation.
            """

class CloneModelContentResponse:
    """
    
            This response contains failed objects in the target application model along with
            the service data.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ModelContentOutputInfo]
    """
            List of model elements that failed to clone with appropriate error information and
            its corresponding application models. This will be empty when there are no failures
            during the operation.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains newly added data including the error information, if any."""

class ErrorValuesStruct:
    """
    
            contains error details which occurred on the business object. For each failed object
            this structure is populated with details such as error code, error message and error
            level.
            
    """
    def __init__(self, ) -> None: ...
    Code: int
    """integer value representing error code."""
    Message: str
    """string representing error message."""
    Level: str
    """Level represents the error criticality."""

class FailedObjsErrorStruct:
    """
    
FailedObjsErrorStruct structure represents the source objects that failed,
            and ErrorValuesStruct structure.
            
    """
    def __init__(self, ) -> None: ...
    SourceObject: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """Failed Business object to Clone."""
    ErrorValue: ErrorValuesStruct
    """Error details of the failed object."""

class ModelContentOutputInfo:
    """
    
modelContentOutputInfo contains the response information for a particular
            Clone operation, it contains information about the clientID of the input operation,
            failed objects structure and the string to string map of newly created objects.
            
    """
    def __init__(self, ) -> None: ...
    SourceToTargetMap: System.Collections.Hashtable
    """
            Map that contains UID References of source object to newly created target object
            (all enteries are subtypes of Mdl0ModelElements)
            """
    FailedObjects: list[FailedObjsErrorStruct]
    """List of structures containing failed source object and its error information."""
    ClientID: str
    """
            A unique string sent by the calling function, so that the output response could be
            mapped back to the input.
            """

class SourceModelInfo:
    """
    
SourceModelInfo is a construct that is used
            in the input for cloneModelContent operation
            to provide information about the source model elements.
            
    """
    def __init__(self, ) -> None: ...
    SourceModelObject: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            Business object reference to the source application model. It can be empty if subsetDef is supplied as input.
            
"""
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """Provides the configuration rules to be applied on source model content before clone."""
    SubsetDef: Teamcenter.Soa.Client.Model.Strong.Mdl0SubsetDefinition
    """
            Business object reference to the source Subset Definition. It can be empty if sourceModelObject is supplied as input.
            """
    IncludeSourceElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            Contains business object references to a list of objects to be included from Source
            Model into the Target Model. Applications can supply includeSourceElements as input,
            instead of supplying subset Definition as input. The configuration context provided
            as input to the clone SOA will be applied on this list as a pre-step before the actual
            clone operation.
            """
    AuxInfo: System.Collections.Hashtable
    """
            A set of name value pairs(string, string) used to specify additional information
            like sync variant expressions and sync effectivity expressions.
            """
    AuxObjectInfo: list[AuxObjectInfo]
    """
            This argument is applicable when special attributes are to be set on target object(during
            create) for a given source object.
            

"""

class SourceTargetContentInfo:
    """
    
            This structure contains information about the source model content to be cloned into
            the target model, that include subset definition, include list, configuration context
            and others.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            A unique string supplied by the caller. This ID is used to identify returned elements
            and Partial Errors associated with this input. This is an optional argument.
            """
    SourceModelInfo: SourceModelInfo
    """
            SourceModelInfo is a input construct that is used in cloneModelContent operation
            to provide information about the source model elements to be cloned.
            """
    TargetModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            Business object reference to the application model in which the objects are to be
            cloned. It is required during create and cannot be NULL.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CloneModelContent(self, Info: CloneModelContentInfo) -> CloneModelContentResponse:
        """    
             The operation clones (Deep copy) model elements from an application model ( referred
             as source model ) into another application model or within the same application model
             ( referred as target model ). Elements come from source application model, either
             manually or via search criteria to be copied into a second application model. The
             same source content may be cloned multiple times into the same or different target
             model. No associations are maintained between related objects in the source and target
             models, therefore there is no capacity to update any cloned content in the target
             model.
             

             The newly created objects in the target model are fully populated meaning they are
             persistently created in the context of the target model. The object type and category
             of the newly created objects will remain same in the target model. For example, a
             Design Component (Cpd0DesignElement) of category
             Shape from a source model is cloned into a target model, the category and the object
             type of the newly created object in the target model will still be the same as the
             object in the source model. Model elements when cloned across two different source
             models will be re-identified in the target model. For example, upon cloning new IDs
             will be assigned to the Design Component objects in the target model.
             

             The elements to be included from the source to the target model can be either an
             explicit list of elements or results from a recipe. List of elements from the source
             model to be explicitly included (via multi-select action) can be passed to this operation
             for cloning the content into the target model.
             

             Note: Internally BMIDE deep copy rules will be used to traverse and clone the source
             objects.
             



             Preconditions: 

             1)    The source application model is with some pre-existing
             model content.
             
             2)    Target application model already exists.
             
             3)    Partitions (Member owns the membership) are pre created
             in target model if memberships are expected to be copied over to target model.
             



             Cloning in the context of Partitions:


             Note: Partitions are not cloned as part of this operation.
             

             Application must leverage on Partition clone functionality to clone partition from
             one application model into another application model but the model content that resides
             in the source application model are cloned into the new application model using cloneModelContent Operation.
             

             In order to create Partition breakdowns also in the target model, the applications
             must follow a two-step process.
             
             1)    Perform Partition Template Clone using existing clonePartitions service operation to copy partitions from one
             model to another.
             
             2)    Perform Template Clone with model content using the cloneModelContent service operation.



             If the initial elements would reference partitions (member owned partitions) in the
             source application model, membership objects will be also be cloned if the target
             models have the same partitions else the model elements will be cloned as unassigned
             members. If same Partition memberships exist both in source model and target model
             then they are not recreated instead the existing memberships are retained.
             

             Note:
             
             1)    If the source model contains a reuse design component,
             then all its subordinate design components will be cloned. The system will warn and
             stop if the user is trying to clone only subordinate design component without its
             reuse design component.
             
             2)    Delete on cloned content in the target model deletes the
             selected object alone. If the selected object to delete is a reuse Design Component,
             then all its subordinates will also be deleted.
             
             3)    If the category of the newly created target object has
             to be different from source object types then it is Application's/Customer's responsibility
             to manage any such mappings through extension points provided by the infrastructure.
             


             Note:
             

             1) If the source model contain a reuse design component, then all its subordinate
             design components will be cloned. This is control by a business object contants called
             "cloneReuseAlongWithSubordinates". If the value of this constant is true, then reuse
             and its full chain of subordinates will be cloned togther, else reuse or the selected
             subordinate will be ignore.
             

             2) Delete on cloned content in the target model deletes the selected object alone.
             If the selected object to delete is a reuse Design Component , then all its subordinates
             will also be deleted.
             

             3) Variants and Effectivity conditions will not be carry forwarded onto the target
             objects in the target model by default alternatively this behavior can be controlled
             by a business object constant "cloneObjectsWithVariantExpr" , "cloneObjectsWithEffectivityExpr"
             . If the value of the contant is "true" then Variants or effectivity expressions
             will copied from source object.
             

             Refer to TDOC for more information on prerequisites on Variant and effectivity expression
             carry over from source application model to target application model.
             


Use Cases:

             This operation supports the most common Clone Template use case for applications
             to re-use project work as part of their knowledge capture for future projects.
             

             Templates shall be creatable in three different ways:
             
             1)    An extract from an existing model.
             
             2)    Authored from Scratch.
             
             3)    Derived from another template (a.k.a. model). This derivation
             shall keep a relation to the original template.
             
             From 4GD standpoint template is a specialization of an Application model which can
             contain explicit content, parameterized content and place holders.
             

             Applications can clone the source template into target application model.. During
             clone operation, a configurable set of relationships will also be copied over from
             the selected elements to the new initial elements in the second application model.
             Once the cloning is completed the initial elements may be modified to fit better
             with the second application model's requirements.
             

             Note: Re-cloning, revise and update on the source model content has no effect on
             the cloned content in the target model.
             

Dependencies:

             autoAssignValues, getSaveAsDesc
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Info: 
                         Data on <font face="courier" height="10">CloneModelContentInfo</font> used for the
                         cloning of the model content from one application model (source) to another application
                         model (target).
             
        :return: 
        """
        ...

