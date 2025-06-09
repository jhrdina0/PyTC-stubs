import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ActionDefinitionInfo:
    """
    
            The input structure containing info about the associated ActionDefinition objects
            being created for the ActionSet.
            
    """
    def __init__(self, ) -> None: ...
    ActionDefId: str
    """
            The unique identifier for the ActionDefinition. The identifier is unique in context
            of the specification. If specified as empty string, the Id will be auto-generated.
            """
    ActionDefName: str
    """Name of the ActionDefinition object. An empty string cannot be specified."""
    ActionDefDesc: str
    """ActionDefinition description."""
    ActionDefType: str
    """
            The type of the ActionDefinition. The valid values are -

            Add - The Action definition type representing the 'add components' action.
            

"""
    Quantity: int
    """The quantity of components to be placed in design."""
    SpecRulesInfo: list[SpecificationRuleInfo]
    """
            The list of input structures to create Specification Rules for the ActionDefinition
            object.  The Specification Rule objects are to be used as Post-placement 'component
            selection rules'. These are used to configure the criteria based on which the Post-placement
            parts will be searched. The Specification Rules must of type 'Action'.
            """

class ActionSetInfo:
    """
    The structure containing the info about the ActionSet instances being created.
    """
    def __init__(self, ) -> None: ...
    ActionSetId: str
    """
            The unique identifier for the ActionSet. The identifier is unique in context of the
            specification. If specified as empty string, the Id will be auto-generated.
            """
    ActionSetName: str
    """Name of the ActionSet object. An empty string cannot be specified."""
    ActionSetDesc: str
    """ActionSet description."""
    ActionSetType: str
    """
            The type of the ActionSet. The valid values are -
            

PostPlacement - The ActionSet type representing the Generic
            post-placement data.
            
ConnectionCompatibility - The ActionSet type representing
            the connection compatibility data.
            

"""
    SrcConnectionType: str
    """
            The source connection type. This along with the target connection type defines the
            valid combination for the connection.
            
            For generic post-placement, this represents the source node id.
            

"""
    TrgtConnectionType: str
    """
            The target connection type. This along with the source connection type defines the
            valid combination for the connection.
            
            For generic post-placement, this must be specified as an empty string.
            """
    ActionDefInfos: list[ActionDefinitionInfo]
    """The list of structures containing ActionDefinition objects related info."""
    AppDatas: list[Teamcenter.Soa.Client.Model.Strong.Lbr0ApplicationData]
    """
            The list of ApplicationData objects to be associated to the ActionSet. This can be
            specified as empty, if user wants to use global Application Data.
            """

class ApplicationDataInfo:
    """
    Structure containing the info related to Application Data objects.
    """
    def __init__(self, ) -> None: ...
    AppDataId: str
    """
            The unique identifier for the Application data. The identifier is unique in context
            of the Specification. If specified as empty string, the Id will be auto generated.
            """
    AppDataName: str
    """The Application Data object's name. An empty string cannot be specified."""
    AppDataDesc: str
    """The Application data object's description."""
    IsGlobal: bool
    """
            Internally set to true by default. In future it will be used to indicate if the same
            ApplicationData is to be used globally (across the specification), or specific to
            an ActionSet.
            """
    AppDataReason: str
    """The reason string for the ApplicationData (e.g. "ReportInBOM", or "AdditionalOptions")."""
    AppDataEntries: list[EntryValuePair]
    """
            The list of structures containing the data entry-value pairs.(e.g. ModelGasket:True,
            ReportStud:false,  AdditionalStudLength:1.112 etc.).
            """

class CreateActionDefinitionOutput:
    """
    
            The structure containing the info regarding the ActionDefinition object created for
            the ActionSet.
            
            It also contains the SpecificationRule objects created and associated to the ActionDefinition
            object.
            
    """
    def __init__(self, ) -> None: ...
    ActionDefinition: Teamcenter.Soa.Client.Model.Strong.Lbr0ActionDefinition
    """The ActionDefinition object created for the ActionSet."""
    SpecRules: list[Teamcenter.Soa.Client.Model.Strong.Lbr0SpecificationRule]
    """The Specification Rules created for the ActionDefinition object."""

class CreateActionSetOutput:
    """
    The output structure containing the information about created ActionSet object.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification to which the created ActionSet is associated to."""
    ActionSet: Teamcenter.Soa.Client.Model.Strong.Lbr0ActionSet
    """The created ActionSet object."""
    ActionDefinitionOutputs: list[CreateActionDefinitionOutput]
    """The structure containing the info about created ActionDefinition objects."""

class CreateActionSetsIn:
    """
    Input structure containing the info about the ActionSets being created.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification to which the ActionSets will be associated to."""
    ActionSetInfo: ActionSetInfo
    """The structure containing the input info needed for creating the ActionSet objects."""

class CreateActionSetsResponse:
    """
    The response structure containing information about the ActionSet instances created.
    """
    def __init__(self, ) -> None: ...
    ActionSetsOutputs: list[CreateActionSetOutput]
    """The list of structures containing the information about the created ActionSet objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member containing created objects and partial errors, if any."""

class CreateApplicationDataIn:
    """
    Input structure for Application Data being created
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification for which the ApplicationData objects will be created."""
    AppDataInfo: ApplicationDataInfo
    """The stucture containing the Application Data input info."""

class CreateApplicationDataOutput:
    """
    Output structure for created Application Data instance.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """
            The Specification object to which the created ApplicationData instance is associated
            to.
            """
    AppDataObject: Teamcenter.Soa.Client.Model.Strong.Lbr0ApplicationData
    """The created ApplicationData Object."""

class CreateApplicationDataResponse:
    """
    Response structure for created Application Data objects.
    """
    def __init__(self, ) -> None: ...
    AppDataOutputs: list[CreateApplicationDataOutput]
    """List of structures containing the ApplicationData object info."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member containing created objects and partial errors, if any."""

class SearchAttribute:
    """
    Structure holding the attribute ID and expression.
    """
    def __init__(self, ) -> None: ...
    AttributeId: str
    """Attribute ID of the attribute."""
    Query: str
    """Query expression for this attribute e.g. >= 20.00."""

class SpecificationRuleInfo:
    """
    Structure containing info regarding the SpecificationRule objects.
    """
    def __init__(self, ) -> None: ...
    SpecRuleId: str
    """
            The unique identifier of the Specification Rule. If Id is specified as empty string,
            it will be autogenerated.
            """
    SpecRuleName: str
    """The name of the Specification Rule."""
    SpecRuleDescription: str
    """The description of the Specification Rule."""
    RuleType: str
    """
            The rule type. Following are the valid values -
            

Specification - The general rules. These rules are used to
            form the constraints based on which the design components will be searched. The type
            is used for creating Global rules and the rules pertaining to specific nodes. For
            Global rules, the node Id must be specified as empty string. For the rules associated
            to specific nodes, appropriate Library node must be specified.
            
Action - Rules representing the constraints specified for
            particular actions (defined by ActionSets). These rules are created for Action Sets
            (to represent the post-placement part search criteria).
            
InterfaceConstraint - Rules created for representing Interface
            Constraints (also called as Branch Compatibility).
            

"""
    LibraryNode: Teamcenter.Soa.Client.Model.Strong.Lbr0HierarchyNode
    """
            The Library node to which the specification rule is added. If specified as NULL,
            the specification rule created will be treated as a 'Global' Rule.
            """
    IsSpecRuleActive: bool
    """
            If set to True, it indicates that this rule is Active and will take part in filtering
            when search operations are performed.
            """
    RuleSetId: str
    """
            The Rule Set Identifier.
            
            The Specification Rules could be grouped together in RuleSets. Each RuleSet is identified
            by a unique Rule set Id.
            
            For two or more rules to be a part of a RuleSet, they need to have same RuleSet Id.
            
            Rules with ruleSetId specified as empty will be treated as independent rules, not
            belonging to any Sule Set.
            
            The rules of a single rule set are AND'ed in a query, while the different rule sets
            are OR'd in a query.
            
            Consider following example where, in Specification SpecA, for Library node - Blind_flange_1092,
            following Specification rules exist
            
            SpecRule1 ( CLASS = PN16 ) -> RuleSet Id : RuleSetIdA
            
            SpecRule2 ( NPS <= 125.00 ) -> RuleSet Id : RuleSetIdA
            
            The rules in Rule Sets are ANDed together when used in queries.
            

            e.g. In above example in addition to the existing Rules, there could be another rule
            set as follows -
            
            SpecRule3 ( CLASS = PN40 ) -> RuleSet Id : RuleSetIdB
            
            SpecRule4 ( NPS > 325.00 ) -> RuleSet Id : RuleSetIdB
            
            The two Rule sets will be OR'd when queries are formed. So the components having
            (CLASS = PN16 AND NPS<=125.00) OR (CLASS = PN40 AND NPS>325.00) will be searched.
            
"""
    SrcFilterCriteria: SearchAttribute
    """
            The source filter criteria. This is used to determine whether the Specification rule
            is applicable in given search Context.
            """
    TrgtFilterCriteria: SearchAttribute
    """
            The target filter criteria. This is used as the search criteria for the matching
            library elements for the given search context.
            """

class CreateSpecificationRulesIn:
    """
    Input structure containing the info about the SpecificationRule being created.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification for which the specification rules are being created."""
    SpecRuleInfo: SpecificationRuleInfo
    """The input structure containing the specification rules input info."""

class CreateSpecificationRulesOutput:
    """
    Output structure containing info related to created SpecificationRule instances.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """
            The Specification object to which the created Specification rules are associated
            with.
            """
    SpecRule: Teamcenter.Soa.Client.Model.Strong.Lbr0SpecificationRule
    """The Specification Rule instance created."""

class CreateSpecificationRulesResponse:
    """
    Output structure containing info related to created SpecificationRules.
    """
    def __init__(self, ) -> None: ...
    SpecRulesOutputs: list[CreateSpecificationRulesOutput]
    """
            The list of structure objects containing the information about created specification
            rule instances.
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData member containing created objects and partial errors, if any.
            
"""

class SpecificationInfo:
    """
    The structure containing info regarding the Specification object being created.
    """
    def __init__(self, ) -> None: ...
    SpecBOTypeName: str
    """
            Business Object (BO) type name. If not specified, the default BO type name - Lbr0Specification
            - will be assumed.
            """
    SpecId: str
    """
            The unique identifier of the Specification being created. If empty string is specified,
            the Id would be auto-generated.
            """
    SpecName: str
    """
            The name of the Specification being created. An empty string will be considered as
            invalid input.
            """
    SpecDescription: str
    """The short text describing the intent of the Specification being created."""
    SpecDiscipline: str
    """The discipline to which this Specification belongs to."""
    ChildRuleOverrideFlag: bool
    """
            Specifies if the Specification Rules defined on a child node will override all parent
            rules instead of extending them.
            
            If set to true, then rules search will be only done till the parent node where any
            rules are defined. The further parents in the hierarchy are not considered for search.(
            This emulates the current NX functionality )
            
            If set to false, then the rules will be searched in all parents in the hierarchy.
            All these rules will be considered for overriding and inheritance.
            
"""
    SpecAdmins: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            The list of users or groups in charge of administrating the Specification. This is
            an optional parameter and the data is currently used for informational purpose only.
            This could be a user, or a group.
            """
    AdditionalProps: System.Collections.Hashtable
    """
            A map of additional property names and their values (string,vector<string>) to
            be set for the Specifications. This can also be used for properties defined for custom
            Specification BO instances. The calling client is responsible for converting the
            different property types (int, float, date etc.) to a string using the appropriate
            toXXXString functions in the SOA client  framework's Property class.
            """
    SpecRuleInfos: list[SpecificationRuleInfo]
    """The information related to specification rules being created along with the specification."""
    ActionSetInfos: list[ActionSetInfo]
    """The information related to ActionSet objects being created along with the specification."""
    AppDataInfos: list[ApplicationDataInfo]
    """The information related to ApplicationData objects being created along with the specification."""

class CreateSpecificationsIn:
    """
    Input structure containing info regarding the Specifications being created.
    """
    def __init__(self, ) -> None: ...
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """
            The  Library input object, to which the Specification being created will be associated
            with.
            """
    SpecInput: SpecificationInfo
    """The Specification input structure object."""

class SpecificationsOutputInfo:
    """
    
            The structure containing info about created Specification instance and associated
            objects.
            
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification object created."""
    SpecRules: list[Teamcenter.Soa.Client.Model.Strong.Lbr0SpecificationRule]
    """The Specification Rules created for the specification."""
    ActionSetOutputs: list[CreateActionSetOutput]
    """The created ActionSet objects (and associated ActionDefinition objects) info."""
    AppDataObjects: list[Teamcenter.Soa.Client.Model.Strong.Lbr0ApplicationData]
    """The Application Data objects created for the specification."""

class CreateSpecificationsOutput:
    """
    Structure containing info about the created Specifications.
    """
    def __init__(self, ) -> None: ...
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """The Library to which the created Specification is associated with."""
    SpecOutputInfo: SpecificationsOutputInfo
    """
            The structure containing the info about the Specification (and the associated objects)
            created.
            """

class CreateSpecificationsResponse:
    """
    Response structure for created Specification instances.
    """
    def __init__(self, ) -> None: ...
    SpecsOutput: list[CreateSpecificationsOutput]
    """The list of structure objects containing the information about the created specifications."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member containing created objects and partial errors, if any."""

class EntryValuePair:
    """
    Generic structure used to store the data entries and corresponding values.
    """
    def __init__(self, ) -> None: ...
    DataEntry: str
    """The data entry string."""
    DataValue: str
    """The data value corresponding to the data entry specified."""

class FilterExpression:
    """
    
            Structure containing info to specify the filter criteria for searching objects based
            on property values.
            
    """
    def __init__(self, ) -> None: ...
    PropertyName: str
    """The internal property name to filter(e.g. 'diameter')."""
    Expression: str
    """
            The expression for the Property (e.g. ">= 10.0")
            
            An expression is of the form:
            
operator value : used for '=,!=,>,>=,<,<='
            
value operator value : used for range(-)
            
            valid operators are: =,!=,>,>=,<,<=, -(range).
            
"""

class GenericPostPlacementData:
    """
    
            The list of structures containing the input information for creating Generic Post-placement
            data definition.
            
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The specification object on which the Generic Post-placement data is being added."""
    SourceLibraryNode: Teamcenter.Soa.Client.Model.ModelObject
    """
            The source Library node for the Generic post-placement. The post-placement part will
            be searched when a library element belonging to this node is selected and placed
            in design. The node could be of type Lbr0HierarchyNode or Lbr0Hierarchy.
            """
    TargetLibraryNode: Teamcenter.Soa.Client.Model.ModelObject
    """
            The target Library node for the Generic post-placement. The post-placement part will
            be searched in this node. The node could be of type Lbr0HierarchyNode or Lbr0Hierarchy.
            """
    Quantity: int
    """The desired quantity of the matching post-placement parts."""
    GenPPAttrExprs: list[FilterExpression]
    """
            The list of attribute expressions, to be used as the criteria to find the post-placement
            parts.
            """

class GenericPostPlacementDataIn:
    """
    Input structure containing criteria for searching the post-placement data.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The specification in which the generic post-placement data is to be searched."""
    SourceNode: Teamcenter.Soa.Client.Model.Strong.Lbr0HierarchyNode
    """
            The source node for which the associated post-placement data is to be searched.
            
            Can be specified as null, if user wants to search all the post-placement data belonging
            to the specified specification.
            """

class GetActionSetsInfoIn:
    """
    Input structure containing info about the ActionSet objects to be found.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification in which the ActionSets are being searched."""
    ActionSetExprs: list[FilterExpression]
    """The additional filter expressions based on ActionSet properties."""

class GetActionSetsInfoOutput:
    """
    Structure containing info about the found ActionSet objects.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification to which the found ActionSet object belongs to."""
    ActionSet: Teamcenter.Soa.Client.Model.Strong.Lbr0ActionSet
    """The ActionSet object found."""
    ActionDefs: list[Teamcenter.Soa.Client.Model.Strong.Lbr0ActionDefinition]
    """The list of ActionDefinition objects associated to the ActionSet object found."""
    AppDatas: list[Teamcenter.Soa.Client.Model.Strong.Lbr0ApplicationData]
    """The list of ApplicationData objects associated to the ActionSet found."""

class GetActionSetsInfoResponse:
    """
    The response structure containing info about the found ActionSet objects.
    """
    def __init__(self, ) -> None: ...
    ActionSetOutputs: list[GetActionSetsInfoOutput]
    """
            The list of structures containing the info about found action sets and other associated
            objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member containing found objects and partial errors, if any."""

class GetApplicationDataIn:
    """
    
            Input structure containing the info based on which the ApplicationData objects will
            be searched.
            
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification in which the ApplicationData objects are being searched."""
    AppDataExprs: list[FilterExpression]
    """The filter expressions based on ApplicationData object properties."""

class GetApplicationDataOutput:
    """
    The structure stores the info about found Application data object(s).
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification object to which the found ApplicationData objects belong to."""
    AppDataObjects: list[Teamcenter.Soa.Client.Model.Strong.Lbr0ApplicationData]
    """The vector of ApplicationData objects found."""

class GetApplicationDataResponse:
    """
    Response structure containing the info about the found application data objects.
    """
    def __init__(self, ) -> None: ...
    AppDataOutputs: list[GetApplicationDataOutput]
    """Vector of structures containing the info about the found ApplicationData objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData member containing objects and partial errors, if any.
            
"""

class GetPostPlacementDataResponse:
    """
    .
    """
    def __init__(self, ) -> None: ...
    GenPPDatas: list[GenericPostPlacementData]
    """The list of structures containing the Generic Post-placement data."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member containing created objects and partial errors, if any."""

class GetSpecificationRulesIn:
    """
    Input structure containing info about the SpecificationRules to be searched.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification in which the specification rules are being searched."""
    RuleExprs: list[FilterExpression]
    """The additional filter expressions based on Specification Rule properties."""

class GetSpecificationRulesOutput:
    """
    Output structure containing the info about the found SpecificationRule objects.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification to which the found Specification Rules belong to."""
    SpecRules: list[Teamcenter.Soa.Client.Model.Strong.Lbr0SpecificationRule]
    """The list of Specification Rule objects found."""

class GetSpecificationRulesResponse:
    """
    The response structure containing the info about found Specification Rules.
    """
    def __init__(self, ) -> None: ...
    SpecRulesOutputs: list[GetSpecificationRulesOutput]
    """
            The vector of structures containing the found Specification Rule info.
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData member containing found objects and partial errors, if any.
            
"""

class GetSpecificationsIn:
    """
    
            Input structure containing the info based on which the Specifications objects will
            be searched.
            
    """
    def __init__(self, ) -> None: ...
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """
            The Library object for which the Specification is being searched.
            
            If specified empty, then all the Specifications in the database will be searched.
            """
    SpecExprs: list[FilterExpression]
    """
            Expressions for searching the Specifications. The expressions could be formed using
            the Specification object properties like id, name, discipline etc.
            """

class GetSpecificationsOutput:
    """
    Output structure containing the Specification objects found for the specified Library.
    """
    def __init__(self, ) -> None: ...
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """
            The input Library object to which the Specification objects searched are associated
            to.
            """
    Specifications: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Specification]
    """
            The list of Specification objects found for the specified Library.
            
"""

class GetSpecificationsResponse:
    """
    Response structure containing the info about the Specification objects found.
    """
    def __init__(self, ) -> None: ...
    SpecOutputs: list[GetSpecificationsOutput]
    """The list of output structures containing the Specification objects found by the search."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member containing found objects and partial errors, if any."""

class InterfaceConstraintData:
    """
    The structure containing the details of Interface Constraints data.
    """
    def __init__(self, ) -> None: ...
    SourceAttributeId: str
    """The unique identifier for the source attribute."""
    DestAttributeId: str
    """The unique identifier for the destination attribute."""
    CompatibleConstraintValues: list[EntryValuePair]
    """
            The list of compatible values for source and destination attributes. While creation,
            each value must be specified as a non-empty string.
            
"""

class InterfaceConstraintDataInput:
    """
    The input structure containing data for creation of the interface constraints.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """
            The Specification for which the interface constraints need to be set.
            
"""
    OverwriteExistingData: bool
    """
            The boolean flag to indicate whether to add to the existing data, or override it
            completely.
            

True - The existing data will get overwritten completely.
            
False - The new data will be added to the existing data.
            

"""
    InterfaceConstraintDatas: list[InterfaceConstraintData]
    """
            The list of structures containing interface constraints data     definitions.
            
"""

class InterfaceConstraintDataOutput:
    """
    The list of structures containing interface constraints data for given specification.
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """
            The specification to which the interface constraints belong to.
            
"""
    InterfaceConstraintDatas: list[InterfaceConstraintData]
    """
            The list of interface constraint data structures for the given specification.
            
"""

class InterfaceConstraintDataResponse:
    """
    
            The response structure containing the interface constraints data obtained for the
            specification(s) specified as input.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServiceData member containing the partial errors, if any.
            
"""
    InterfaceConstraintDataOutputs: list[InterfaceConstraintDataOutput]
    """
            List of structures containing the interface constraints data for each input specification.
            

"""

class SearchGenericPostPlacementPartsResp:
    """
    .
    """
    def __init__(self, ) -> None: ...
    GenPPPartsOutputs: list[SearchPostPlacementPartsOutput]
    """The list of the structures containing info aboute the matching library elements found."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member containing created objects and partial errors, if any."""

class SearchGenericPostPlacementsIn:
    """
    .
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification in which the post-placements are being searched."""
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """The library to search for generic post-placements."""
    LibraryElement: Teamcenter.Soa.Client.Model.ModelObject
    """The source design component for which the post-placement part(s) needs to be searched."""

class SearchPostPartsForCompConnsIn:
    """
    .
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """
            The Specification in which the post-placement parts are being searched.
            
"""
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """The library to search for the compatible post-placement parts."""
    SourceConnectionType: str
    """
            The connection type of the source design component of the connection.
            
"""
    TargetConnectionType: str
    """
            The connection type of the target design component of the connection.
            
"""

class SearchPostPartsForCompConnsOutput:
    """
    .
    """
    def __init__(self, ) -> None: ...
    Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification
    """The Specification in which the post-placement parts (library elements) are found."""
    LibraryElements: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of the matching library elements found."""
    Library: Teamcenter.Soa.Client.Model.Strong.Lbr0Library
    """The library to search for the compatible post-placement parts."""

class SearchPostPartsForCompConnsResp:
    """
    .
    """
    def __init__(self, ) -> None: ...
    ResultOutputs: list[SearchPostPartsForCompConnsOutput]
    """The list of the structures containing info aboute the matching library elements found."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member containing created objects  and partial errors, if any."""

class SearchPostPlacementPartsOutput:
    """
    .
    """
    def __init__(self, ) -> None: ...
    SourcelibraryElement: Teamcenter.Soa.Client.Model.ModelObject
    """
            The design component for which the Generic Post-placement parts are searched.
            
"""
    MatchingLibraryElements: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The matching design components found as per the     inputs provided
            and the generic post-placement data defined for specified Specification.
            
"""

class LibrarySpecificationManagement:
    """
    Interface LibrarySpecificationManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateActionSets(self, ActionSetInputs: list[CreateActionSetsIn]) -> CreateActionSetsResponse:
        """    
             The operation creates ActionSet (Lbr0ActionSet) objects for the specified
             Specification object(s).
             
             This data is used to define the criteria for compatibility between two connections
             based on Connection types.
             
             (The types defined as the Source and target connection type make a valid combination
             for the connection).
             
             The operation should also be used to create and associate ActionDefinition (Lbr0ActionDefinition)
             objects to the ActionSets being created. The ActionDefinition objects define the
             action to find the additional parts that should be placed in the design when a connection
             is made as per definition in ActionSet.
             
             This data is defined using Specification Rules, and specifies the criteria to find
             the appropriate additional part. The ActionDefinition objects hold the reference
             to this information. Specification Rule objects created for this are added to the
             ActionDefinition objects.
             
             The operation could optionally also associate existing ApplicationData objects to
             the ActionSet being created.
             
             Consider following example -
             
             Suppose, in a design, if the designer wants to allow connection to be made between
             a 'Valve' and a 'Flange' part, only when both have connection type defined as "FLANGE",
             he can set the connection compatibility combination accordingly.
             
             ----------------------------------------------------------------
             
             Conn Type Source    |    Conn Type destination
             
             -----------------------------------------------------------------
             
             FLANGE                
             |     FLANGE
             
             -----------------------------------------------------------------
             
             For above data, user may want to define "Gasket" and "Bolt" as the parts to be placed
             in design, after the connection is made (post-placement parts).
             
             This operation provides a convenient mechanism to create a large set of connection
             compatibility definition data, and to set the post-placements data definition.
             
             Steps to be typically followed for creating data for above example -
             
             1.    Create Specification
             
             2.    Create Specification rules defining the constraints for
             the objects to be added as post-placement parts.
             
             3.    Using this info, create ActionSets and ActionDefinition
             objects, and pass in the Specification rules info as part of the input structure
             for creating ActionDefinition.
             

             Related operations:
             

getActionSetsInfo
             
createSpecifications
             
createSpecificationRules
             
createApplicationData
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ActionSetInputs: 
                         The list of structures containing the input information for creating the ActionSet
                         objects.
             
        :return: 143336 - The type specified for action set object is invalid.
        """
        ...
    def CreateApplicationData(self, AppDataInputs: list[CreateApplicationDataIn]) -> CreateApplicationDataResponse:
        """    
             The operation creates the ApplicationData (Lbr0ApplicationData) objects.
             
             The objects represent the application specific data to be stored, along with other
             connection compatibility and post-placement information.
             

             Related operations:
             

getApplicationDataInfo
             
createActionSets
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param AppDataInputs: 
                         The list of structure objects containing the input information for creating the ApplicationData
                         objects.
             
        :return: 
        """
        ...
    def CreateSpecificationRules(self, SpecRulesInputs: list[CreateSpecificationRulesIn]) -> CreateSpecificationRulesResponse:
        """    
             This operation creates the Specification Rule (Lbr0SpecificationRule) objects
             for the given Specification.
             
             A Specification can have multiple Specification Rule objects associated with it.
             The Specification Rules define the constraints on the design which help to filter
             and find the right design components matching to the criteria defined by the rules.
             
             The specification rules (of type 'Specification') could be associated to the library
             nodes and the filter criteria of such specification rules is formed from the attributes
             of the library node on which they are added.
             
             When not associated with library nodes, they are treated as 'Global' rules (the rules
             applicable over complete library).
             

             Following are the valid Specification types -
             

Specification - The general node rules. These rules are used
             to form the constraints based on which the design components will be searched.
             


             This type is used for creating Global rules and the rules pertaining to specific
             nodes.
             
             For Global rules, the node Id must be specified as empty string.
             
             For the rules associated to specific rules, appropriate Library node must be specified.
             

Action - Rules representing the constraints specified for
             particular actions (defined by ActionSets). These rules are created for Action Sets.
             
InterfaceConstraint - Rules created for representing Interface
             Constraints, also called as Branch Compatibility. This type is used as an internal
             type.
             




             Related operations -
             

getSpecificationRules
             
createSpecifications
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param SpecRulesInputs: 
                         The list of Specification Rules input structure objects.
             
        :return: 
        """
        ...
    def CreateSpecifications(self, CreateSpecInputs: list[CreateSpecificationsIn]) -> CreateSpecificationsResponse:
        """    
             This operation creates the specification (Lbr0Specification) objects.
             
             The Specifications are created in context of the specified Library object(s).
             
             The Specification objects could be associated with multiple Specification Rules,
             and Action sets, and Application data objects which help define the various constraints.
             
             The API also provides the capability to create those associated objects, and return
             them as part of the output.
             

             A specification defines constraints to configure and control which design components
             to be returned during the search operations.
             

             Related operations -
             

getSpecifications
             
createSpecificationRules
             
createActionSets
             
createApplicationData
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param CreateSpecInputs: 
                         The input structure containing the details of the Specifications to be created.
             
        :return: 
        """
        ...
    def GetActionSetsInfo(self, ActionSetInputs: list[GetActionSetsInfoIn]) -> GetActionSetsInfoResponse:
        """    
             The operation returns the ActionSet (Lbr0ActionSet) objects found for the
             specified specification.
             
             Further filtering could be done based on the ActionSet property info (like id, name,
             description etc.) provided in the input search expressions.
             
             Information about the ActionDefinition objects and ApplicationData objects associated
             to the found ActionSet is also returned.
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ActionSetInputs: 
                         The list of structures containing the input information for searching the ActionSet
                         objects.
             
        :return: 
        """
        ...
    def GetApplicationData(self, AppDataInputs: list[GetApplicationDataIn]) -> GetApplicationDataResponse: ...
    def GetGenericPostPlacementData(self, GenPPDataInputs: list[GenericPostPlacementDataIn]) -> GetPostPlacementDataResponse:
        """    
             The operation returns the Generic Post placement data definition for the given Specification(s)
             and other criteria.
             
             This 'Generic post-placement data' concept defines the constraints for helping to
             search such components in design, which need to be automatically post-placed based
             on adding some specific design components.
             
             The generic post-placement data is stored in the database as a combination of ActionSet,
             ActionDefinition and SpecificationRule(s).
             
             This operation provides a convenient mechanism to get this data.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param GenPPDataInputs: 
                         The structure containing the input criteria to search the post-placement data.
             
        :return: 
        """
        ...
    def GetSpecificationRules(self, SpecRulesInputs: list[GetSpecificationRulesIn]) -> GetSpecificationRulesResponse:
        """    
             This operation searches the Specification Rule (Lbr0SpecificationRule) objects
             for the given Specifications.
             
             Further filtering could be done based on the Specification Rule property info (like
             rule id, name, description etc.) provided in the input search expressions.
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param SpecRulesInputs: 
                         The list of structures containing the info about Specification Rules being searched.
             
        :return: 
        """
        ...
    def GetSpecifications(self, GetSpecsInputs: list[GetSpecificationsIn], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> GetSpecificationsResponse:
        """    
             This operation searches for available Specification objects in the specified libraries.
             Further filtering could be done based on the specification properties info (like
             Specification id, name, discipline etc.) provided in the input search expressions.
             

             The configured revision of the Specification will be returned based on the specified
             Configuration Context object. If Configuration Context object is not specified, all
             the revisions belonging to the specified library (and matching the filter criteria)
             will be returned.
             

             Related operations -
             
                 createSpecifications().
             


Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param GetSpecsInputs: 
                         The list of structures containing the input information. If this is specified empty,
                         then all the Specifications in the database will be searched and returned.
             
        :param ConfigContext: 
                         The Configuration Context object containing the configuration info based on the revision
                         rule. This info is used to identify the correct revision of the Specification object
                         to be used.
             
        :return: 143303 - Invalid number of inputs specified in the search criteria.
        """
        ...
    def SearchGenericPostPlacementParts(self, GenPPInputs: list[SearchGenericPostPlacementsIn]) -> SearchGenericPostPlacementPartsResp:
        """    
             The operation returns the valid and matching design parts (Library Elements) found
             based on the generic post-placement data definition for the given component (Library
             Element) in the specified Specification(s).
             
             This 'Generic post-placement data' concept defines the constraints for helping to
             search such components in design, which need to be automatically post-placed based
             on adding some specific design components.
             
             The generic post-placement data is stored in the database as a combination of ActionSet,
             ActionDefinition and SpecificationRule(s).
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param GenPPInputs: 
                         The list of input structures containing the source element info, for which the generic
                         post-placement parts are to be searched.
             
        :return: 
        """
        ...
    def SearchPostPartsForCompConns(self, SearchPPInputs: list[SearchPostPartsForCompConnsIn]) -> SearchPostPartsForCompConnsResp:
        """    
             This operation returns the matching design components (Library Elements) for the
             specified compatible types.
             
             The found design components will be used as post-placement part(s) for the compatible
             connection(s).
             
             Based on the input connection types, first the compatibility will be checked between
             these types.
             
             If found compatible, then based on the connection compatibility data stored, the
             library elements will be searched.
             

             Example: Consider scenario where in a design, the designer makes a connection between
             a 'Valve' and a 'Flange' part, consider both have connection types defined as 'FLANGE',
             and the connection compatibility for this combination is already set in database.
             The post placement part defined for this FLANGE - FLANGE compatibility is set as,
             say, 'Gasket'.
             
             This API takes in inputs the connection types of the Valve and Flange part, checks
             the compatibility between them, and searches for the matching Gaskets based on the
             criteria stored. The matching Gaskets thus found will be placed on the Flange part
             (target) of the above connection.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param SearchPPInputs: 
                         The list of structures containing the input information for creating or updating
                         the ActionSet objects.
             
        :return: 
        """
        ...
    def SetGenericPostPlacementData(self, GenPPDatas: list[GenericPostPlacementData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets or updates the definition for Generic Post-placement data for
             the given Specification.
             
             This concept defines the constraints for helping to search such components in design,
             which need to be automatically post-placed based on adding some specific design components.
             
             The generic post-placement data is stored in the database as a combination of ActionSet,
             ActionDefinition and SpecificationRule(s).
             
             This operation provides a convenient mechanism to create this data.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param GenPPDatas: 
                         The list of structures containing the input information for creating Generic Post-placement
                         data definition.
             
        :return: 
        """
        ...
    def SetInterfaceConstraintData(self, InterfaceConstraintInputs: list[InterfaceConstraintDataInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation sets the interface constraints (also called as Branch Compatibility
             data) data for the specified Specification object(s).
             
             The interface constraints data is used for identifying the compatible values for
             specified attributes.
             
             E.g. In a design, a Pipe with NPS=25 can only have a reducing Tee object which has
             NPS_BRANCH=10, 15 or 20, as valid match.
             
             Example of an interface constraints data set -
             
             --------------------------------------------------------------
             
             NPS (source)            |    NPS_BRANCH
             (destination)
             
             (Attribute Id=1001)    |    (Attribute Id=1008)
             
             --------------------------------------------------------------
             
             10                        |    4
             
             10                        |    2
             
             20                        |    2
             
             30                        |    30
             
             ---------------------------------------------------------------
             
             This data can be stored and used while searching the matching components during search
             operations, through interface constraints data definition.
             
             This data is stored in database as specification rules.
             
             This operation provides a convenient mechanism to create a large set of compatibility
             definition data.
             

             Related operations -
             
             getInterfaceConstraintData
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param InterfaceConstraintInputs: 

        :return: 
        """
        ...
    def AttachSpecificationToLibraries(self, Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification, Libraries: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Library]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation attaches the given Library (Lbr0Library) objects to the specified
             Specification (Lbr0Specification) object.
             
             This is used to share the Specification between multiple libraries.
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param Specification: 
                         The Specification to which the specified Libraries will be attached to.
             
        :param Libraries: 
                         The list of libraries which will be attached to the specified Specification.
             
        :return: 
        """
        ...
    def DetachSpecificationFromLibraries(self, Specification: Teamcenter.Soa.Client.Model.Strong.Lbr0Specification, Libraries: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Library]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation detaches the given Library(Lbr0Library) objects from specified Specification(Lbr0Specification)
             object.
             
             If no library is specified, then the given specification will be detached from all
             the associated Libraries.
             



Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param Specification: 
                         The Specification which the specified Libraries will be detached from.
             
        :param Libraries: 
                         The libraries to be detached. If no library is specified, then the Specification
                         will be detached from all the associated libraries.
             
        :return: 143101 - Invalid library object is passed as an input.
        """
        ...
    def GetInterfaceConstraintData(self, Specifications: list[Teamcenter.Soa.Client.Model.Strong.Lbr0Specification]) -> InterfaceConstraintDataResponse:
        """    
             The operation returns the details of the interface constraints (also called as branch
             compatibility data), set for the Specification object(s) specified.
             

             Related operation:
             
             setInterfaceConstraintData
             


Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param Specifications: 
                         The list of the specifications for which the interface constraints data is requested.
             
        :return: 
        """
        ...

