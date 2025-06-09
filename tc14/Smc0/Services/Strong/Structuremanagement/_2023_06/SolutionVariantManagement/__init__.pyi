import Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateMultiLevelSVConfigParam:
    """
    
            Input to the service is a structure containing list of VariantRule object
            by which Solution Variant is created and the preferences which are considered during
            the creation of Solution Variant.
            
    """
    def __init__(self, ) -> None: ...
    PcaVariantRules: list[Teamcenter.Soa.Client.Model.Strong.VariantRule]
    """A list of VariantRule by which Solution Variant gets created."""
    ConfigPreferences: System.Collections.Hashtable
    """
            map (string/string) of config preferences.
            
            Supported key, values and meanings are:
            

            Key: "StopOnError "
            
            0, 1 : If 1, the creation of Solution Variants should be stopped when error encountered;
            otherwise, 0, if the creation should continue even if errors at any stage are encountered.
            

            Key: "DryRun"
            
            0, 1: If 1, then we provide only the information of Auto Solution Variant creation
            information, but actual creation wont be done.
            

            Key: "RunInBackground"
            
            0, 1: If not provided, the default behavior is run in foreground.
            """

class CreateMultilevelSVOutput:
    """
    
            Output structure contains BOMLine Solution Variant Item associated with the
            input BOMLine, along with the description related to the creation of Solution
            Variant status and error, if any.
            
    """
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMLine of generic assembly"""
    NewSVBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """BOMLine of Newly created Solution Variant Item"""
    StatusInfo: str
    BomLineLevel: int
    """BOMLine level of newly created Solution Variant"""
    ErrorCode: int
    """
            errorCode if any. Details for error code -
            

            178007: An invalid item type is provided for the creation of a Solution Variant.
            
            178008: The input BOMLine must be from the same BOMWindow.
            
            178012: An invalid variant rule is provided.
            
            178017: Invalid preference provided for the Multilevel Solution Variant creation.
            """

class CreateMultilevelSVResponse:
    """
    
            Response structure contains map of VariantRule and Solution Variant created
            by this. It also contains the service data.
            
    """
    def __init__(self, ) -> None: ...
    VariantRuleSolutionVariantMap: System.Collections.Hashtable
    """
            Map of VariantRule to Solution Variant and its associated information(VarinatRule,
            vector of CreateMultilevelSVOutput).
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""

class UpdateSVItemInput:
    """
    
            Input to the service is a structure containing the source BOMLine and solution
            Variant ItemRevision object list.
            
    """
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Source generic BomLine."""
    ReuseSVItemRevList: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """List of Solution Variant ItemRevision objects."""

class SolutionVariantManagement:
    """
    Interface SolutionVariantManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateMultilevelMultiVRSolVariant(self, CreateMultilevelSVInputList: list[Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.CreateMultilevelSVInput], CreateMultilevelSVConfigParam: CreateMultiLevelSVConfigParam) -> CreateMultilevelSVResponse:
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
    def UpdateMultilevelReuseSolVariants(self, UpdateSVItemInputList: list[UpdateSVItemInput], RevRuleToUseInUpdate: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ConfigPreferences: System.Collections.Hashtable) -> Smc0.Services.Strong.Structuremanagement._2018_11.SolutionVariantManagement.UpdateReuseSVItemRevResponse: ...

