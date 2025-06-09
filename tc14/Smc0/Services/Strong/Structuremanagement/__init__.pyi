import Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement
import Smc0.Services.Strong.Structuremanagement._2023_06.SolutionVariantManagement
import System
import System.Collections
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model.Strong

class SolutionVariantManagementRestBindingStub(SolutionVariantManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CompareManagedSolutionVariantItems(self, GenericSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ManagedSVItemRevInputList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], ConfigPreferences: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CompareManagedSVItemRevResponse: ...
    def CreateMultilevelSolutionVariants3(self, CreateMultilevelSVInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateMultilevelSVInput], CreateMultilevelSVConfigParam: Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateMultilevelSVConfigParam) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateMultilevelSVResponse: ...
    def CreateSolutionVariantItems3(self, CreateSVItemInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateSVItemInput], PcaVariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateSVItemResponse: ...
    def LoadSolutionVariantItems2(self, SvItemObjectsToBeLoadedList: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.LoadSVItemResponse: ...
    def SearchSolutionVariantItems3(self, SearchSVItemInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.SearchSVItemInput], SearchParameter: Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.SearchParameter) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.SearchSVItemsResponse: ...
    def UpdateManagedSolutionVariantItems(self, GenericSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ListOfManagedSVItemRevReportInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CompareManagedSVItemRevReport], ConfigPreferences: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.UpdateManagedSVItemRevResponse: ...
    def UpdateReuseSolutionVariantItems(self, GenericSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ReuseSVItemRevInputList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], ConfigPreferences: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.UpdateReuseSVItemRevResponse: ...
    def CreateMultilevelMultiVRSolVariant(self, CreateMultilevelSVInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateMultilevelSVInput], CreateMultilevelSVConfigParam: Smc0.Services.Strong.Structuremanagement._2023_06.SolutionVariantManagement.CreateMultiLevelSVConfigParam) -> Smc0.Services.Strong.Structuremanagement._2023_06.SolutionVariantManagement.CreateMultilevelSVResponse: ...
    def UpdateMultilevelReuseSolVariants(self, UpdateSVItemInputList: list[Smc0.Services.Strong.Structuremanagement._2023_06.SolutionVariantManagement.UpdateSVItemInput], RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ConfigPreferences: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.UpdateReuseSVItemRevResponse: ...

class SolutionVariantManagementService:
    """
    
            Solution variant functionality provides Interfaces to create a fully configured assemblies
            from generic assemblies. This newly created assembly will have new part number, which
            represents the solution for a particular variant configuration.
            

            This service provides operations related to the Solution Variant Management on Collaborative
            and non-Collaborative structure. This service is applicable only for Product Structures
            that have variability defined in Product Configurator Application.
            


Library Reference:

Smc0SoaStructureManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SolutionVariantManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CompareManagedSolutionVariantItems(self, GenericSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ManagedSVItemRevInputList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], ConfigPreferences: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CompareManagedSVItemRevResponse: ...
    def CreateMultilevelSolutionVariants3(self, CreateMultilevelSVInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateMultilevelSVInput], CreateMultilevelSVConfigParam: Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateMultilevelSVConfigParam) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateMultilevelSVResponse: ...
    def CreateSolutionVariantItems3(self, CreateSVItemInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateSVItemInput], PcaVariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateSVItemResponse:
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
    def LoadSolutionVariantItems2(self, SvItemObjectsToBeLoadedList: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.LoadSVItemResponse: ...
    def SearchSolutionVariantItems3(self, SearchSVItemInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.SearchSVItemInput], SearchParameter: Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.SearchParameter) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.SearchSVItemsResponse:
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
    def UpdateManagedSolutionVariantItems(self, GenericSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ListOfManagedSVItemRevReportInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CompareManagedSVItemRevReport], ConfigPreferences: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.UpdateManagedSVItemRevResponse: ...
    def UpdateReuseSolutionVariantItems(self, GenericSourceBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine, RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ReuseSVItemRevInputList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], ConfigPreferences: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.UpdateReuseSVItemRevResponse: ...
    def CreateMultilevelMultiVRSolVariant(self, CreateMultilevelSVInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateMultilevelSVInput], CreateMultilevelSVConfigParam: Smc0.Services.Strong.Structuremanagement._2023_06.SolutionVariantManagement.CreateMultiLevelSVConfigParam) -> Smc0.Services.Strong.Structuremanagement._2023_06.SolutionVariantManagement.CreateMultilevelSVResponse:
        """    
             This operation creates fully configured Solution Variant assembly from generic assembly
             BOMLine object. This creation is done on input generic assembly BOMLine object
             who satisfy the Solution Variant Item creation criteria. It takes list of VariantRule
             and creates Solution Variant for each VariantRule.
             

Use Cases:

             This operation is suited to create a static snapshot of a configured product structure
             which represents particular variant from generic assembly after applying variant
             configuration.
             
             1.    Client opens a generic assembly in Active Workspace.
             
             2.    Client opens Solution Variant tab.
             
             3.    Client selects few Variant Rules.
             
             4.    Client invokes creation of multilevel solution variants
             to create a static snapshot of BOMLine objects for valid and complete Variant Rules.
             

Teamcenter Component:

             Product Configurator Support for Structure Manager - Smc0psmcfgsupport component
             provides ability to use Product Configurator application for working with new options
             and variants functionality within Structure Manager.
             
        :param CreateMultilevelSVInputList: 
                         A list of CreateMultilevelSVInput structure (which contains generic <b>BOMLine</b>
                         objects and Descriptor (CreateSVItemDescriptor structure).
             
        :param CreateMultilevelSVConfigParam: 
                         The <b>VariantRule</b> by which generic assembly gets configured and preferences
                         which are used while creation of Solution Variant.
             
        :return: &#61607;Â Â Â Â 178017: Invalid preference provided for the Multilevel
             Solution Variant creation.
        """
        ...
    def UpdateMultilevelReuseSolVariants(self, UpdateSVItemInputList: list[Smc0.Services.Strong.Structuremanagement._2023_06.SolutionVariantManagement.UpdateSVItemInput], RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ConfigPreferences: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.UpdateReuseSVItemRevResponse: ...

