import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CompareManagedSVItemRevReport:
    """
    
            Output input structure which reports first level configured structural difference
            between the Managed Solution Variant ItemRevision and input generic source
            BOMLine Object.
            
    """
    def __init__(self, ) -> None: ...
    ManagedSVItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Managed Solution Variant ItemRevision which is used for comparison."""
    GvCompareReportNodeList: list[CompareReportNode]
    """
            List of CompareReportNode, This is generic variant comparison report containing the
            generic variant child details. This can be child added in generic variant or child
            whose corresponding component from Solution Variant is removed.
            """
    SvCompareReportNodeList: list[CompareReportNode]
    """
            List of CompareReportNode, This is Solution Variant comparison report containing
            the Solution Variant child details. This can be child added in Solution Variant or
            child whose source component from generic assembly is removed.
            """

class CompareManagedSVItemRevResponse:
    """
    
            Response structure contains the list of output structure for the service and the
            service data.
            
    """
    def __init__(self, ) -> None: ...
    GenericSourceItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision of input generic source BOMLine object."""
    ListOfCompareManagedSVItemRevReport: list[CompareManagedSVItemRevReport]
    """
            List of CompareManagedSVItemRevReport, the details of the comparison differences
            between the Managed Solution Variant ItemRevision and generic source ItemRevision.
            """
    Servicedata: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class CompareReportNode:
    """
    
            Output input structure which reports first level configured structural difference
            between the Managed Solution Variant ItemRevision and generic source ItemRevision
            with its details. User can override only itemAction in CompareReportNode.
            
    """
    def __init__(self, ) -> None: ...
    OccPropNameValueMap: System.Collections.Hashtable
    """
            Map of Occurrence property with its property name and value. In update operation
            this map will be ignored.
            """
    PsOccChildItemUID: str
    """Item or ItemRevision UID of Occurrence."""
    PsOccThreadUID: str
    """The Occurrence thread UID."""
    ItemAction: int

class CreateMultilevelSVConfigParam:
    """
    
            Input to the service is a structure containing VariantRule object by which the structure
            is configured and the preferences which are consider during the creation of Solution
            Variant.
            
    """
    def __init__(self, ) -> None: ...
    PcaVariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """Variant Rule by which assembly gets configured"""
    ConfigPreferences: System.Collections.Hashtable
    """
            configPreferences A map (string/string) of config preferences.
            
            Supported key, values and meanings are:
            

            Key: "StopOnError "
            
            0, 1 : If 1, the creation of Solution Variants should be stopped when error encountered;
            otherwise, 0, if the creation should be continue after error on any stage.
            

            Key: "DryRun"
            
            0, 1: If 1, then we provide only the information of Auto Solution Variant creation
            information, but actual creation wont be done.
            

            Key: "NumberOfLinesToProcess"
            
            If the value of this is greater than 0, then those many lines are processed for Solution
            Variant createion in each iteration. On the basis on this value ExpandedBOMLineMap
            output will be presented to client.
            
            Else, no pagination is done.
            """

class CreateSVItemDescriptor:
    """
    
            Structure contains business object type and all type of business object properties
            which are used during creation of the object.
            
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business object type name."""
    StringProps: System.Collections.Hashtable
    """Map of string property names to values (string, string)"""
    StringListProps: System.Collections.Hashtable
    """Map of string array property names to values (string/list of strings)."""
    DoubleProps: System.Collections.Hashtable
    """Map of double property names to values (string, double)"""
    DoubleListProps: System.Collections.Hashtable
    """Map of double array property names to values (string/list of doubles)."""
    FloatProps: System.Collections.Hashtable
    """Map of float property names to values (string, float)"""
    FloatListProps: System.Collections.Hashtable
    """Map of float array property names to values (string/list of floats)."""
    IntProps: System.Collections.Hashtable
    """Map of int property names to values (string, int)"""
    IntListProps: System.Collections.Hashtable
    """Map of int array property names to values (string/list of ints)."""
    BoolProps: System.Collections.Hashtable
    """Map of boolean property names to values (string, bool)"""
    BoolListProps: System.Collections.Hashtable
    """Map of boolean array property names to values (string/list of bools)."""
    DateProps: System.Collections.Hashtable
    """Map of DateTime property names to values (string, date)"""
    DateListProps: System.Collections.Hashtable
    """Map of date array property names to values (string/list of DateTimes)."""
    BoProps: System.Collections.Hashtable
    """Map of BusinessObject property names to values (string, BusinessObject)"""
    BoListProps: System.Collections.Hashtable
    """Map of BusinessObject array property names to values (string/list of BusinessObjects)"""
    CompoundCreateSVItemDescriptor: System.Collections.Hashtable
    """
            Map of CreateSVItemDescriptor object array property names to values (string/list
            of CreateSVItemDescriptor objects).
            """

class CreateSVItemInfo:
    """
    
            Structure containing property details of Solution Variant Item and category of Solution
            Variant Item.
            
    """
    def __init__(self, ) -> None: ...
    CreateSVItemDesc: CreateSVItemDescriptor
    """The properties required for creation of Solution Variant Item."""
    SvCategoryType: int
    """
            Category of Solution Variant assembly.
            
            Unmanaged = 0,
            
            Update will not be handled by the system. If Required, user has to handle the update
            manually.
            
            Managed = 1,
            
            Solution Variant update is handled by the system.
            
            Reuse = 2,
            
            For a specific Variant Rule, only single Solution Variant is created and that solution
            variant will be reuse in different assemblies.
            """

class CreateSVItemInput:
    """
    
            Input to the service is a structure containing the selected BOMLine and property
            details for the creation of Solution Variant Item.
            
    """
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMLine of an assembly"""
    CreateSVItemInfo: CreateSVItemInfo
    """The property details for a new Solution Variant Item creation."""

class CreateMultilevelSVInput:
    def __init__(self, ) -> None: ...
    CreateSVItemInput: CreateSVItemInput
    """
            The BOMLine from a generic assembly with the property details for a new Solution
            Variant Item creation.
            """
    MappedSVBOMLineUID: str
    """The UID of mapped BOMLine object from the Solution Variant assembly."""
    BomLineLevel: int
    """BOMLine level in the structure."""

class CreateMultilevelSVOutput:
    """
    
            Output structure contains BOMLine Solution Variant Item associated with the input
            BOMLine, along with the description which describe the creation of Solution Variant
            status.
            
    """
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMLine of generic assembly."""
    NewSVBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMLine of Newly created Item."""
    StatusInfo: str
    BomLineLevel: int
    """BOMLine level of newly created Solution Variant."""

class CreateMultilevelSVResponse:
    def __init__(self, ) -> None: ...
    CreatMultilevelSVOutputList: list[CreateMultilevelSVOutput]
    """
            List of CreateAndReplaceSVOutput, the details for newly creted Solution Variant BOMLine
            and BOMLine of generic assembly.
            """
    ExpandedBOMLineMap: System.Collections.Hashtable
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class CreateSVItemOutput:
    """
    
            Output structure contains BOMLine Solution Variant Item associated with the input
            BOMLine, along with the description which describe the creation of Solution Variant
            status.
            
    """
    def __init__(self, ) -> None: ...
    GenericBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMLine of generic assembly"""
    NewVariantItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Item Revision of Newly created Item."""
    AlreadyExists: bool
    """
            True, if Solution Variant Item already exists; otherwise, false, if a new Solution
            Variant Item is created.
            """

class CreateSVItemResponse:
    """
    
            Response structure contains the output structure for the service and the service
            data.
            
    """
    def __init__(self, ) -> None: ...
    CreateSVItemOutput: list[CreateSVItemOutput]
    """
            List of CreateSVItemOutput, the details for newly creted Item Revision and BOMLine
            of generic assembly.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class LoadSVItemResponse:
    """
    
            Response structure conatins the list of output structure for the service and service
            data.
            
    """
    def __init__(self, ) -> None: ...
    LoadSVItemsOutputList: list[LoadSVItemsOutput]
    """
            List of LoadSVItemsOutput, it contains Solution Variant ItemRevision and property
            values of the Solution Variant Items.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class LoadSVItemsOutput:
    """
    
            LoadSVItemsOutput is a structure contains the objects as ItemRevision of a Solution
            Variant Item and properties. Also map of ( string, string ), which can passed as
            key-value pair for properties.
            
    """
    def __init__(self, ) -> None: ...
    SvItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision of a Solution Variant Item."""
    SvItemPropsMap: System.Collections.Hashtable
    """Map of string property names to values (string, string)"""

class SearchParameter:
    """
    
            Input to the service is a structure containing the search parameters which are consider
            during search opearation for Solution Variant Items. This criteria is commmon to
            all input source BOMLine objects.
            
    """
    def __init__(self, ) -> None: ...
    SearchVariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """The search VariantRule criteria."""
    SvCategories: int
    """
            0 : Search all SV category.
            
            1 : Search SV category is Unmanaged
            
            2 : Search SV category is Managed.
            
            3 : Search SV category is Managed & Unmanaged.
            
            4 : Search SV category is Reuse
            
            5 : Search SV category is Reuse & Unmanaged.
            
            6 : Search SV category is Reuse & Managed.
            
            7 : Search all SV category.
            """
    SearchPreferences: System.Collections.Hashtable

class SearchSVItemInput:
    """
    
            Input to the service is a structure containing the selected ItemRevision and search
            ItemRevision with selected PSViewType
            
    """
    def __init__(self, ) -> None: ...
    SelectedItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Selected ItemRevision object."""
    SearchItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision as input for search."""

class SearchSVItemOutput:
    """
    
            Output to the service is a structure containing input ItemRevision of generic assembly,
            list of loaded Solution Variant Item related objects and list of UID (Unique Identifier)
            of the unloaded objects.
            
    """
    def __init__(self, ) -> None: ...
    SearchItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Source ItemRevision given as a input to search."""
    UnloadedSVItemObjectsUIDList: System.Collections.Hashtable
    IntialSVItemOutputList: list[LoadSVItemsOutput]
    """
            A list of LoadSVtemsOutput, contains the Solution Variant ItemRevision object and
            properties of the Solution Variant Item.
            """

class SearchSVItemsResponse:
    """
    
            Response structure contains the output structure for the service and the service
            data.
            
    """
    def __init__(self, ) -> None: ...
    SearchSVItemOutputList: list[SearchSVItemOutput]
    """
            A list of SearchSVItemResponse, the source ItemRevision objects and Solution Variants
            ItemRevision and properties.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class UpdateManagedSVItemRevOutput:
    """
    
            Output structure contains updated Managed Solution Variant ItemRevision associated
            to input Managed Solution Variant ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    InputManagedSVItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Input Managed Solution Variant ItemRevision which is to be updated."""
    UpdatedManagedSVItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Updated Managed Solution Variant ItemRevision."""

class UpdateManagedSVItemRevResponse:
    """
    
            Response structure contains the list output structure for the service and the service
            data.
            
    """
    def __init__(self, ) -> None: ...
    UpdatedManagedSVItemRevOutputList: list[UpdateManagedSVItemRevOutput]
    """
            List of UpdateManagedSVItemRevOutput, the details for updated Managed Solution Variant
            ItemRevision and input Managed Solution Variant ItemRevision.
            """
    Servicedata: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class UpdateReuseSVItemRevOutput:
    """
    
            Output structure contains updated Reuse Solution Variant ItemRevision associated
            to input Reuse Solution Variant ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    InputReuseSVItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Input Reuse Solution Variant ItemRevision which is to be updated."""
    UpdatedReuseSVItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Updated Reuse Solution Variant ItemRevision."""

class UpdateReuseSVItemRevResponse:
    """
    
            Response structure contains the list output structure for the service and the service
            data.
            
    """
    def __init__(self, ) -> None: ...
    UpdatedReuseSVIROutputList: list[UpdateReuseSVItemRevOutput]
    """
            A list of UpdateReuseSVItemRevOutput, the details for updated Reuse Solution Variant
            ItemRevision and input Reuse Solution Variant ItemRevision.
            """
    Servicedata: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class SolutionVariantManagement:
    """
    Interface SolutionVariantManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CompareManagedSolutionVariantItems(self, GenericSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ManagedSVItemRevInputList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], ConfigPreferences: System.Collections.Hashtable) -> CompareManagedSVItemRevResponse: ...
    def CreateMultilevelSolutionVariants3(self, CreateMultilevelSVInputList: list[CreateMultilevelSVInput], CreateMultilevelSVConfigParam: CreateMultilevelSVConfigParam) -> CreateMultilevelSVResponse: ...
    def CreateSolutionVariantItems3(self, CreateSVItemInputList: list[CreateSVItemInput], PcaVariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule) -> CreateSVItemResponse:
        """    
             This operation creates a snapshot of fully configured assembly called as Solution
             Variant Item from generic source assembly BOMLine objects. The Solution Variant Item
             is a static snapshot of only first level configured BOMLine objects of the generic
             assembly in context.  This newly created assembly considers only configured BOMLine
             objects which are configured based on the variant configuration.
             

Use Cases:

             This operation is suited to create a static snapshot of a configured assembly which
             represents particular variant from generic assembly after applying variant configuration.
             
             1.    Client opens a generic assembly in Structure Manager.
             
             2.    Client opens Variant Configuration view.
             
             3.    Client selects criteria and apply the variant rule on the
             opened assembly.
             
             4.    Client invokes createSolutionVariantItems3 operation for
             selected BOMLine objects to create a static snapshot of BOMLine objects configured
             by the variant configuration only.
             
             5.    Client uses response from createSolutionVariantItems3 operation
             to display newly created configured assembly.
             

Teamcenter Component:

             Product Configurator Support for Structure Manager - Smc0psmcfgsupport component
             provides ability to use Product Configurator application for working with new options
             and variants functionality within Structure Manager.
             
        :param CreateSVItemInputList: 
                         List of CreateSVItemInput structure (which contains generic BOMLine objects and Descriptor
                         (CreateSVItemDescriptor structure)).
             
        :param PcaVariantRule: 
                         The VariantRule contains configuration details by which generic assembly gets configured.
             
        :return: &#61607;Â Â Â Â 178012: An invalid variant rule is provided.
        """
        ...
    def LoadSolutionVariantItems2(self, SvItemObjectsToBeLoadedList: System.Collections.Hashtable) -> LoadSVItemResponse: ...
    def SearchSolutionVariantItems3(self, SearchSVItemInputList: list[SearchSVItemInput], SearchParameter: SearchParameter) -> SearchSVItemsResponse:
        """    
             The Solution Variant ItemRevision and the source assembly ItemRevision are connected
             with the relation Smc0SolutionVariantSource during the Solution Variant Item creation.
             
             This operation performs a search on the Solution Variant Item, which are linked with
             the source assembly ItemRevision objects. The search criteria is includes category
             of Solution Variant Item and VariantRule.
             

Use Cases:

             This operation is suited to search Solution Variant Item, which have a link with
             generic Assembly for the given search criteria.
             
             1.    Client opens a structure in Structure Manager.
             
             2.    Client open Variant Configuration view.
             
             3.    Client selects criteria and use the variant rule as a criteria
             for search parameter.
             
             4.    Client invokes searchSolutionVariantItems3 operation for
             selected generic assembly ItemRevision.
             
             5.    Client uses response from searchSolutionVariantItems3 operation
             to display Solution Variant Item list.
             

Teamcenter Component:

             Product Configurator Support for Structure Manager - Smc0psmcfgsupport component
             provides ability to use Product Configurator application for working with new options
             and variants functionality within Structure Manager.
             
        :param SearchSVItemInputList: 
                         List of SearchSVItemInput structure ( which contains the selected ItemRevision and
                         ItemRevision which will be used for search).
             
        :param SearchParameter: 
                         The SearchParameter structure contains the parameter which are consider as a search
                         parameters for Solution Variant Items.
             
        :return: &#61607;Â Â Â Â 1780016: Invalid Key string provided for the
             search preferences.
        """
        ...
    def UpdateManagedSolutionVariantItems(self, GenericSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ListOfManagedSVItemRevReportInputList: list[CompareManagedSVItemRevReport], ConfigPreferences: System.Collections.Hashtable) -> UpdateManagedSVItemRevResponse: ...
    def UpdateReuseSolutionVariantItems(self, GenericSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ReuseSVItemRevInputList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], ConfigPreferences: System.Collections.Hashtable) -> UpdateReuseSVItemRevResponse: ...

