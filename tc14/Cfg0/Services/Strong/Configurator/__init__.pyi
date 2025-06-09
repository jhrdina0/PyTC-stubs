import Cfg0.Services.Strong.Configurator._2014_12.ConfiguratorManagement
import Cfg0.Services.Strong.Configurator._2021_12.ConfiguratorManagement
import Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement
import Cfg0.Services.Strong.Configurator._2022_12.ConfiguratorManagement
import Cfg0.Services.Strong.Configurator._2023_06.ConfiguratorManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class ConfiguratorManagementRestBindingStub(ConfiguratorManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetAdmissibility(self, OperationConfigPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, AdmissibilityInputs: list[Cfg0.Services.Strong.Configurator._2014_12.ConfiguratorManagement.GetAdmissibilityInputStruct]) -> Cfg0.Services.Strong.Configurator._2014_12.ConfiguratorManagement.GetAdmissibilityResponse: ...
    def GetConditionPairCompatibility(self, VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule, ConditionPairs: list[Cfg0.Services.Strong.Configurator._2021_12.ConfiguratorManagement.ConditionPair], ClientCode: str) -> Cfg0.Services.Strong.Configurator._2021_12.ConfiguratorManagement.ConditionPairCompatibility: ...
    def BatchSolveConditions(self, VariantRules: list[Teamcenter.Soa.Client.Model.Strong.VariantRule], Conditions: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.Conditions], RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.BatchSolveConditionsResponse: ...
    def GetAvailableVariability(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str, Expression: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.Expression, Families: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.FamilyList, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.AvailableVariabilityResponse: ...
    def GetConfigurationInformation(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.VariantRule]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.GetConfigurationInformationResponse: ...
    def GetVariability(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.GetVariablityResponse: ...
    def SetConfigurationInformation(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.VariantRule], ConfigPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ValidateAndExpandExpressions(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str, Expressions: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.Expression], RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.ValidateAndExpandExprsResponse: ...
    def GetVariantInformation(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.VariantRule], RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_12.ConfiguratorManagement.GetVariantInformationResponse: ...
    def ConvertVariantExpressions(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, VariantExpressions: list[str], ExpressionFormat: str, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2023_06.ConfiguratorManagement.VariantExpressionsResponse: ...
    def GenerateBuildableCombinations(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str, LimitingExpression: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.ExpressionInfo, Families: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.FamilyList, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2023_06.ConfiguratorManagement.BuildableCombinationsResponse: ...

class ConfiguratorManagementService:
    """
    
            This Service contains operations related to variant configuration and variant configurator
            data. The createObjects operation in the
            DataManagementService can be used to create
            configurator or variability data such as feature (e.g. Cfg0LiteralOptionValue)
            and their families. The families can be arranged into family groups (e.g. Cfg0FamilyGroup).
            The features, families, and family groups need to be allocated to items in order
            to make them visible to these items.
            

            The configurator rules ( Cfg0AbsRule or subtypes) reference a set of product
            items and define the relationship among variant option values in the context of these
            product item(s). The configurator rules can be categorized broadly as   the default
            rules (e.g. Cfg0AbsDefaultRule) and the constraint rules (Cfg0AbsContraintRule).
            The constraint rule business object types can further be categorized as rule to validate
            (e.g. Cfg0AbsExcludeRule) and to modify (e.g. Cfg0AbsIncludeRule)
            the configuration criteria. All constraint rules are imperative in nature, while
            all default rules are suggestive.
            

            The configuration rules that derive from Cfg0AbsAssociation type define the
            relationship between the variability data (such as features, families or family groups)
            and a product configuration context. For example variability data is not visible
            in a product item until it is explicitly allocated to this product (e.g. with a Cfg0Allocation
            object). For product context items with positive biased variant availability (see
            Item property fnd0PosBiasedVariantAvail)
            all variability data is available by default. In this case explicit availability
            rules (e.g.Cfg0ValueAvailability) are only required if the corresponding variability
            data needs to be made unavailable.
            

            Most of the operations in this service needs the Configurator Perspective (Cfg0ConfiguratorPerspective)
            runtime business object as part of the input parameter. Cfg0ConfiguratorPerspective
            is a runtime business object that represents the configuration snapshot required
            for the Product Configurator in Teamcenter. Since constructing the configurator perspective
            runtime business object may take time, you should create it first time for a given
            Configurator context object and hold it for the subsequent calls. Hold the configurator
            perspective runtime business object for a configurator context if the configuration
            is unchanged. You always work on a snapshot or a frozen set of the configurator data
            and use that data to get consistent results for a period. These results are not impacted
            by subsequent changes, such as additions or updates of features and rules.
            
            Since getting the Cfg0ConfiguratorPerspective runtime business object for
            a configurator context may involve effort by the system in destroying and creating
            the snapshot, you should get it once for a given configurator context object and
            hold it as long as the configuration (revision rule, rule date and effectivity) is
            unchanged.
            
            The Cfg0ConfiguratorPerspective runtime object is a session recoverable object
            which means that the system will try to facilitate transparent recovery of the business
            object when a TcServer  instance crashes.
            
            The sample in soa_client.zip, com.teamcenter.productconfigurator.GetConfiguratorPerspectiveSampleTest.java
            shows the different ways the user can get the Cfg0ConfiguratorPerspective
            runtime object.
            

Dependencies:

            DataManagement
            


Library Reference:

Cfg0SoaConfiguratorStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ConfiguratorManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetAdmissibility(self, OperationConfigPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, AdmissibilityInputs: list[Cfg0.Services.Strong.Configurator._2014_12.ConfiguratorManagement.GetAdmissibilityInputStruct]) -> Cfg0.Services.Strong.Configurator._2014_12.ConfiguratorManagement.GetAdmissibilityResponse:
        """    
             This operation returns the admissibility statements for the variability data associated
             with a given set of context objects. The instance of Cfg0AbsAdmissibility object
             represents the relation and state between a configurator specific object and a non-configurator
             specific object. For example, the pair of a partition and an family is associated
             with state "Available". The admissibility states are defined by the LOV Cfg0AdmissibilityState.
             The allowed values for this property are "Available" and "Not Available".
             

Use Cases:

             Consider that following set of the data-
             

             Groups-
             
             Engine-Box (A Family Group) - It has families "Engine" and "Transmission".
             
             1. Engine- Petrol, Diesel
             
             2. Transmission - Manual, Auto
             
             Wheel (A Family Group) - It has families "Wheel-drive" and "Suspension".
             
             1. Wheel-drive - 2-Wheels, 4-Wheels
             
             2. Suspension - Full-Thrust, Full-Boom
             
             For the Engine partition object, the families, Engine & Transmission are "Available"
             and the families Wheel-drive & Suspension are "Not Available".
             
             The response of the operation for  the Engine partition object will have  the list
             of  Cfg0AbsAdmissibility objects for families Engine and Transmission, 1 for each
             and those will have admissibility state as "Available" and also the Cfg0AbsAdmissibility
             objects for the families Wheel-drive and Suspension, 1 for each and those will have
             admissibility state as "Not Available".
             

Teamcenter Component:

             Teamcenter Configurator - Teamcenter component for cfg0configurator template
             
        :param OperationConfigPerspective: 
                         The Cfg0ConfiguratorPerspective instance to specify the context and revision rule.
                         If configurator perspective is provided by each input structure in list admissibilityInputs,
                         then this operationConfigPerspective parameter can be NULL.
             
        :param AdmissibilityInputs: 
                         The list of target objects for which admissibility data should be returned.
             
        :return: 79010 - The operation expects one product item in the configuration perspective.
        """
        ...
    def GetConditionPairCompatibility(self, VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule, ConditionPairs: list[Cfg0.Services.Strong.Configurator._2021_12.ConfiguratorManagement.ConditionPair], ClientCode: str) -> Cfg0.Services.Strong.Configurator._2021_12.ConfiguratorManagement.ConditionPairCompatibility: ...
    def BatchSolveConditions(self, VariantRules: list[Teamcenter.Soa.Client.Model.Strong.VariantRule], Conditions: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.Conditions], RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.BatchSolveConditionsResponse: ...
    def GetAvailableVariability(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str, Expression: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.Expression, Families: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.FamilyList, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.AvailableVariabilityResponse: ...
    def GetConfigurationInformation(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.VariantRule]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.GetConfigurationInformationResponse: ...
    def GetVariability(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.GetVariablityResponse: ...
    def SetConfigurationInformation(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.VariantRule], ConfigPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ValidateAndExpandExpressions(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str, Expressions: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.Expression], RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.ValidateAndExpandExprsResponse: ...
    def GetVariantInformation(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.VariantRule], RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2022_12.ConfiguratorManagement.GetVariantInformationResponse: ...
    def ConvertVariantExpressions(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, VariantExpressions: list[str], ExpressionFormat: str, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2023_06.ConfiguratorManagement.VariantExpressionsResponse: ...
    def GenerateBuildableCombinations(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str, LimitingExpression: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.ExpressionInfo, Families: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.FamilyList, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> Cfg0.Services.Strong.Configurator._2023_06.ConfiguratorManagement.BuildableCombinationsResponse: ...

