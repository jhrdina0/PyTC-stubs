import Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement
import Fnd0.Services.Strong.Configfiltercriteria._2013_05.EffectivityManagement
import Fnd0.Services.Strong.Configfiltercriteria._2013_05.VariantManagement
import Fnd0.Services.Strong.Configfiltercriteria._2017_05.EffectivityManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class EffectivityManagementRestBindingStub(EffectivityManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ConvertEffectivityExpressions(self, Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityFormulaeResponse: ...
    def ConvertEffectivityTables(self, EffectivityTables: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityTable], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityFormulaeResponse: ...
    def GetAvailableProductEffectivity(self, RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ExprsToTest: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], FamiliesToTest: list[Teamcenter.Soa.Client.Model.Strong.ConfigurationFamily], SubstituteDependentVariables: int, ApplyConstraints: int, ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.AvailableProductEffectivityResponse: ...
    def GetConfigurableProducts(self, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigurableProductsResponse: ...
    def GetEffectivityConditions(self, AffectedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityFormulaeResponse: ...
    def GetEffectivityExpressions(self, Formulae: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigFormula], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityExpressionsResponse: ...
    def GetEffectivityTables(self, Formulae: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigFormula], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityTablesResponse: ...
    def GetRevRuleEffectivityCriteria(self, RevisionRules: list[Teamcenter.Soa.Client.Model.Strong.RevisionRule], SubstituteDependentVariables: int, ApplyConstraints: int, ApplyDefaults: int, ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.RevRuleEffectivityCriteriaResponse: ...
    def SetEffectivityConditions(self, SampleObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], Formulae: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigFormula], Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], OpCode: int, ActionCode: int, AffectedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], ReplacedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityConditionResponse: ...
    def SetRevRuleEffectivityCriteria(self, SampleObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], Formulae: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigFormula], Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], OpCode: int, SubstituteDependentVariables: int, ApplyConstraints: int, ApplyDefault: int, ActionCode: int, SolveType: int, SaveNow: bool, CreatePrivateCopy: bool, AffectedRevRules: list[Teamcenter.Soa.Client.Model.Strong.RevisionRule], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.RevRuleEffectivityCriteriaResponse: ...
    def GetEffectivityDisplayString(self, Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2013_05.EffectivityManagement.EffectivityDisplayStringResponse: ...
    def GetEffectivityOverlapStates(self, ReferenceExpressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2013_05.EffectivityManagement.EffectivityOverlapStateResponse: ...
    def GetEffectivitySubsetTables(self, ProductName: str, ProductNamespace: str, SubsetCriteria: Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression, EffectivityConditions: list[Fnd0.Services.Strong.Configfiltercriteria._2017_05.EffectivityManagement.EffectivityConditionSource]) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityTablesResponse: ...
    def SetEffectivityConditionSubsets(self, ProductName: str, ProductNamespace: str, SubsetCriteria: Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression, ActionCode: int, EffectivityConditions: list[Fnd0.Services.Strong.Configfiltercriteria._2017_05.EffectivityManagement.EffectivityConditionInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class EffectivityManagementService:
    """
    
EffectivityManagement  service provides operations
            to manage effectivity conditions on product data, and effectivity criteria on revision
            rules. RevisionRule  objects that are associated with effectivity configuration
            criteria can be used to filter search results if the objects in the search result
            have effectivity conditions (see operation Mdl0::Soa::ModelCore::Search::createOrUpdateConfigurations)
            


Library Reference:

Fnd0SoaConfigFilterCriteriaStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> EffectivityManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ConvertEffectivityExpressions(self, Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityFormulaeResponse:
        """    
             This operation returns string representations (formulae) for a given set of effectivity
             expressions. This operation connects to the effectivity configurator service whose
             service endpoint is specified by the configuratorURL
             parameter. The actual conversion to formula strings is performed by this configurator
             service. The result may vary depending on the choice of service endpoint and the
             product identified by parameters productName
             and productNameSpace. For example a given
             configurator might return shorthand representations for formulae if these are unique
             in the context of the specified product. Teamcenter 9 only supports local built in
             Teamcenter configurators where parameters productName,
             productNameSpace, and configuratorURL can be set to an empty string.
             


Use Cases:

             Obtain a formula string representation (ConfigFormula)
             in the context of a Collaborative Design model (Cpd0CollaborativeDesign) for
             an effectivity expression (ConfigExpression)
             when these expression do not already reference a formula.
             

             When effectivity expressions are returned from effectivity SOA operations, e.g. getAvailableProductEffectivity for a given RevisionRule,
             they usually already contain a corresponding formula string representation. However,
             there is no guarantee they always do, e.g. if the configurator link is temporarily
             down.
             

             Another scenario in which effectivity expressions exist without a corresponding formula
             string representation is when these expressions are constructed in the SOA client.
             

Identifiers for the product associated with the Collaborative Design
             model (CD) are obtained from CD properties  mdl0config_product_name,
             and mdl0config_prod_namespace.
             
Operation convertEffectivityExpressions
             is used to convert the effectivity conditions into formula strings.
             



Dependencies:

             getProperties
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param Expressions: 
                         Vector of effectivity expressions (<font face="courier" height="10">ConfigExpression</font>)
                         where these expression do not yet contain a corresponding formula string representation
                         (<font face="courier" height="10">ConfigFormula</font>).
             
        :param ProductName: 
                         Specifies a product. A (<font face="courier" height="10">productName</font><i>,</i><font face="courier" height="10">productNamespace</font>) tuple is used as a parameter
                         in configurator service calls so to allow the configurator to resolve any ambiguity
                         in effectivity condition parameters. Applications using this <font face="courier" height="10">EffectivityManagement</font> service should define a mechanism to obtain
                         an appropriate value for this parameter. For example, <font face="courier" height="10">ApplicationModel</font>
                         objects like Collaborative Design models (<b>Cpd0CollaborativeDesign</b>) make them
                         available via properties <font face="courier" height="10">mdl0config_product_name</font>,
                         and <font face="courier" height="10">mdl0config_prod_namespace</font>.
             
        :param ProductNameSpace: 
                         Specifies a namespace in which parameter <font face="courier" height="10">productName</font>
                         has a unique definition, e.g. a specific model year, or product type. A (<font face="courier" height="10">productName</font><i>,</i><font face="courier" height="10">productNamespace</font>)
                         tuple is used as a parameter in configurator service calls so to allow the configurator
                         to resolve any ambiguity in effectivity condition parameters. Applications using
                         this <font face="courier" height="10">EffectivityManagement</font> service should
                         define a mechanism to obtain an appropriate value for this parameter. For example,
                         <font face="courier" height="10">ApplicationModel</font> objects like Collaborative
                         Design models (<b>Cpd0CollaborativeDesign</b>) make them available via properties
                         <font face="courier" height="10">mdl0config_product_name</font>, and <font face="courier" height="10">mdl0config_prod_namespace</font>.
             
        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: ,
             e.g. if the service fails to connect to the configurator, or if an error was returned
             from the configurator.
        """
        ...
    def ConvertEffectivityTables(self, EffectivityTables: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityTable], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityFormulaeResponse:
        """    
             This operation returns string representations (formulae) for a given set of effectivity
             tables where each table describes a separate set of effectivity ranges. This operation
             connects to the effectivity configurator service whose service endpoint is specified
             by the configuratorURL parameter. The actual
             conversion to formula strings is performed by this configurator service. The result
             may vary depending on the choice of service endpoint and the product identified by
             parameters productName and productNameSpace. For example a given configurator might return
             shorthand representations for formulae if these are unique in the context of the
             specified product. Teamcenter 9 only supports local built in Teamcenter configurators
             where parameters productName, productNameSpace, and configuratorURL
             can be set to an empty string.
             

Use Cases:

             Review the configurator encoded formula string representation for a table of effectivity
             ranges before assigning the effectivity ranges to a Revision Rule.
             

An application displays a dialog that collects a set of effectivity
             ranges in form of(unit in ,unit out ) and/or (date in ,date out) tuples
             from the user with the intent to eventually use these effectivity ranges as configuration
             criteria to be assigned to a RevisionRule.
             
The user wants to review the configurator encoding of the corresponding
             effectivity expression
             
Operation convertEffectivityTables
             is used to convert the effectivity table of effect in and effect out points into
             a formula string.
             



Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param EffectivityTables: 
                         Vector of effectivity tables representing validity ranges as rows of (<i>effect in,effect
                         out</i>) tuples.
             
        :param ProductName: 
                         Specifies a product. A (<font face="courier" height="10">productName,productNamespace</font>)
                         tuple is used as a parameter in configurator service calls so to allow the configurator
                         to resolve any ambiguity in effectivity condition parameters. Applications using
                         this <font face="courier" height="10">EffectivityManagement</font> service should
                         define a mechanism to obtain an appropriate value for this parameter. For example,
                         <font face="courier" height="10">ApplicationModel</font> objects like Collaborative
                         Design models (<b>Cpd0CollaborativeDesign</b>) make them available via properties
                         <b>mdl0config_product_name</b>, and <b>mdl0config_prod_namespace</b>.
             
        :param ProductNameSpace: 
                         Specifies a namespace in which parameter <font face="courier" height="10">productName</font>
                         has a unique definition, e.g. a specific model year, or product type. A (<font face="courier" height="10">productName,productNamespace</font>) tuple is used as a parameter in
                         configurator service calls so to allow the configurator to resolve any ambiguity
                         in effectivity condition parameters. Applications using this <font face="courier" height="10">EffectivityManagement</font> service should define a mechanism to obtain
                         an appropriate value for this parameter. For example, <font face="courier" height="10">ApplicationModel</font>
                         objects like Collaborative Design models (<b>Cpd0CollaborativeDesign</b>) make them
                         available via properties <b>mdl0config_product_name</b>, and <b>mdl0config_prod_namespace</b>.
             
        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: , e.g.
             if the service fails to connect to the configurator.
        """
        ...
    def GetAvailableProductEffectivity(self, RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, ExprsToTest: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], FamiliesToTest: list[Teamcenter.Soa.Client.Model.Strong.ConfigurationFamily], SubstituteDependentVariables: int, ApplyConstraints: int, ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.AvailableProductEffectivityResponse:
        """    
             This operation returns available effectivity that could be used to satisfy the specified
             RevisionRule, or the subset of the RevisionRule as defined by parameters
             exprsToTest and familiesToTest.
             Parameters productName and productNameSpace can be used to identify a product whose effectivity
             constraints will be considered in this operation. No product effectivity constraints
             are considered if these parameters are empty. If parameters exprsToTest and familiesToTest
are empty and no product context is given the unmodified basic range of effectivity
             represented by the given RevisionRule is returned. If exprsToTest or familiesToTest
             are provided, then the available range of effectivity for these expressions and /or
             families will be returned.
             

             The operation forms a config expression from the provided input parameters
             by ORing the expressions in parameter exprsToTest
             (resulting in TRUE if exprsToTest was empty),
             and ANDing the result with the effectivity associated with the RevisionRule
             (using TRUE if none was specified). The response will return available effectivity
             for the union set of families used in this config expression with the families
             listed in familiesToTest. If the resulting
             list is empty, available effectivity for all families will be returned. Effectivity
             is considered available if it neither conflicts with the config expression
             nor with the effectivity validation rules defined in the product identified by parameters
             productName and productNameSpace
             (if present). Because of the way the config expression is formed the operation
             can only return meaningful results if either a RevisionRule, or a list of
             exprsToTest, or a list of familiesToTest (or a combination of the above) are provided. If
             all parameters are NULL the response will return no effectivity.
             

             Operation getRevRuleEffectivityCriteria should
             be used if symbolic variable substitution and/or constraint processing is required
             for *all* variant option families, or if validation records are required that specify
             violated constraints.
             

             Operation setEffectivityConditions should
             be used if assigning the combined effectivity range covering a set of existing objects
             does not require the evaluation of configurator constraints. The difference is that
             getAvailableProductEffectivity supports parameters
             that enable effectivity configurator validation rules, which can be used to eliminate
             effectivity combinations from the combined range that are not available according
             to the current set of validation rules. Eliminating invalid combinations reduces
             the number of false positive results detected by automated collision detection systems
             such as Teamcenter Clearance Analysis. On the other hand persisting such expressions
             causes the condition to be out of date if the set of configurator validation rules
             changes.
             
             This operation connects to the effectivity configurator service whose service endpoint
             is specified by the configuratorURL parameter.
             The actual evaluation of configurator rules to trim available effectivity, and conversions
             to and from formula strings, are performed by this configurator service. The resulting
             formula string conversions may vary depending on the choice of service endpoint.
             For example a given configurator might return shorthand representations for formulae
             if these are unique in the context of the specified product. Teamcenter 9 only supports
             local builtin Teamcenter configurators where parameter configuratorURL
             can be set to an empty string. Teamcenter configurators used in the EffectivityManagement service interface encode configuration formulae
             in Explicit Teamcenter Language for which no product context is required (see
             operation getEffectivityExpressions for more
             details on Explicit Teamcenter Language and productName
             and productNameSpace).
             

Use Cases:

             Use case 1:Initialize an effectivity criteria dialog for a given RevisionRule.
             

The application uses operation getAvailableProductEffectivity
             with productName=, productNameSpace=, exprsToTest={},
             and familiesToTest={}, substituteDependentVariables=0, applyConstraints=0.

The response will contain effectivity ranges as they are stored on
             the RevisionRule without additional configurator processing. References to
             effectivity configuration families (ConfigurationFamily) are returned in ServiceData.
             



             Use case 2:
             
             Initialize an effectivity criteria dialog for a product that was created using the
             Teamcenter effectivity configurator with the intent to setup a new RevisionRule.
             

The application uses operation getAvailableProductEffectivity
             with productName=MyProductItemID, productNameSpace=MyProductRevID,
             exprsToTest={}, and familiesToTest={}, substituteDependentVariables=0, applyConstraints=0.

The response will contain all nominal effectivity ranges in this
             product. No constraint processing is required. References to effectivity configuration
             families (ConfigurationFamily) are returned in ServiceData.
             


             Use case 3:
             
             Initialize an effectivity criteria dialog for a product that is associated with a
             Collaborative Design (CD) model with the intent to setup a new RevisionRule.
             

Identifiers for the product associated with the CD (Cpd0CollaborativeDesign)
             are obtained from CD properties mdl0config_product_name,
             and mdl0config_prod_namespace.
             
The application uses operation getAvailableProductEffectivity
             with productName= and productNameSpace=  as obtained in the previous step, exprsToTest={}, and familiesToTest={}, substituteDependentVariables=0,
             applyConstraints=0.

The response will contain all nominal effectivity ranges in this
             product. No constraint processing is required. References to effectivity configuration
             families (ConfigurationFamily) are returned in ServiceData.
             


             Use case 4:
             
             Iterate through all available configuration families (ConfigurationFamily)
             with the intent to assign values to each configuration family in an iterative process
             while dynamically requesting the remaining available range of values for a given
             configuration family.
             

The application uses operation getAvailableProductEffectivity
             with the same values for productName, and
             productNameSpace that was used in the initialization
             step (see above use cases). Parameter exprsToTest is used to accumulate the choices
             that were made in previous iteration steps. Parameter familiesToTest={nextFamilyInList}
             is used to specify the family for which available value ranges are requested
             in this iteration step. The remaining parameter values are substituteDependentVariables=0,
             and applyConstraints=1.
             
The response will contain the available value range for the specified
             familiesToTest.
             



             Use case 5:
             
             Request the effectivity configuration criteria in which at least one of multiple
             objects configures and eliminate criteria from this result that violate any current
             validation rules in the context of a Collaborative Design (CD) model.
             

A radar cable design shall be given an effectivity condition such
             that it configures whenever any of a given set of radar systems and radar screens
             configures.
             
Identifiers for the product associated with the CD (Cpd0CollaborativeDesign)
             are obtained from CD  properties mdl0config_product_name,
             and mdl0config_prod_namespace.
             
The application uses operation getEffectivityConditions
             to obtain the set of conditions associated with the radar systems and screens.
             
The application uses operation getAvailableProductEffectivity
             where parameter exprsToTest is used to pass
             the effectivity conditions associated with the radar systems and screens. Parameter
             familiesToTest is left empty. The remaining parameter values are substituteDependentVariables=0, and applyConstraints=1.
             
The response will contain the actually available effectivity range
             for the listed radar systems and screens according to the current set of effectivity
             configurator validation rules.
             



Dependencies:

             getProperties, findWorkspaceObjects
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param RevisionRule: 
<b>RevisionRule</b> in which context availability is requested. If present it will
                         be used to filter available values. If no <b>RevisionRule</b> is specified all configuration
                         criteria are expected to be defined in <font face="courier" height="10">exprsToTest</font>.
             
        :param ExprsToTest: 
                         Specifies additional effectivity expressions in which context availability is requested.
             
        :param FamiliesToTest: 
                         Specifies configuration families for which available values are requested in addition
                         to those referenced from <font face="courier" height="10">exprsToTest</font> and
                         <b>RevisionRule</b>.
             
        :param SubstituteDependentVariables: 
                         Indicates whether or not to substitute dependent variables, such as <font face="courier" height="10">PlantVacationShutdown</font>. Value <i>0</i> will indicate no substitution
                         is required. A value of <i>1</i> will enable substitution of dependent variables
             
        :param ApplyConstraints: 
                         Indicates whether or not to apply the constraints. Value <i>0</i> will indicate constraint
                         application is not required. A value of <i>1</i> will enable application of constraints
             
        :param ProductName: 
                         Specifies a product. A (<font face="courier" height="10">productName,productNamespace</font>)
                         tuple is used as a parameter in configurator service calls so to allow the configurator
                         to resolve any ambiguity in effectivity condition parameters. Applications using
                         this <font face="courier" height="10">EffectivityManagement</font> service should
                         define a mechanism to obtain an appropriate value for this parameter. For example,
                         <font face="courier" height="10">ApplicationModel</font> objects like Collaborative
                         Design models (<b>Cpd0CollaborativeDesign</b>) make them available via properties
                         <font face="courier" height="10">mdl0config_product_name</font>, and <font face="courier" height="10">mdl0config_prod_namespace</font>.
             
        :param ProductNameSpace: 
                         Specifies a namespace in which parameter <font face="courier" height="10">productName</font>
                         has a unique definition, e.g. a specific model year, or product type. A (<font face="courier" height="10">productName,productNamespace</font>) tuple is used as a parameter in
                         configurator service calls so to allow the configurator to resolve any ambiguity
                         in effectivity condition parameters. Applications using this <font face="courier" height="10">EffectivityManagement</font> service should define a mechanism to obtain
                         an appropriate value for this parameter. For example, <font face="courier" height="10">ApplicationModel</font>
                         objects like Collaborative Design models (<b>Cpd0CollaborativeDesign</b>) make them
                         available via properties <font face="courier" height="10">mdl0config_product_name</font>,
                         and <font face="courier" height="10">mdl0config_prod_namespace</font>.
             
        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: ,
             e.g. if the service fails to connect to the configurator, or if an error was returned
             from the configurator.
        """
        ...
    def GetConfigurableProducts(self, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigurableProductsResponse:
        """    
             This operation returns all effectivity configurable products from the effectivity
             configurator identified by parameter configuratorURL.
             The operation connects to the effectivity configurator service whose service endpoint
             is specified by the configuratorURL parameter.
             The query for available effectivity configurable products is performed by this configurator
             service. Teamcenter 9 only supports local builtin Teamcenter configurators where
             parameter configuratorURL can be set to an
             empty string. Teamcenter configurators use an Item ID for productName
             and an Item Revision ID or RDV  Product Context Identifier for productNameSpace. Teamcenter configurators return all ItemRevision
             objects that allocate effectivity configuration families as effectivity configurable
             products.
             

Use Cases:

             Associate a product item with a Collaborative Design (CD) model so that effectivity
             configurator rules associated with this product are also associated with the CD.
             The assumption is that the CD is an application model (Mdl0ApplicationModel)
             for the product represented by this product item.
             

Operation getConfigurableProducts
             is used to obtain a list of all effectivity configurable products.
             
User reviews the list of available (productName,
             productNameSpace) and selects one.
             
Operation findWorkspaceObjects
             is used to locate the product ItemRevision that corresponds to the given (productName, productNameSpace) tuple.
             
Operation createRelations
             is used to attach the product ItemRevision to the CD using primaryObject=CD, secondaryObject=MyProductItemRevision, and relationType=Mdl0HasConfiguratorContext.

Operation refreshObjects
             is used to refresh the CD.
             
Identifiers for the product associated with the CD (Cpd0CollaborativeDesign)
             are obtained from CD properties mdl0config_product_name,
             and mdl0config_prod_namespace.




Dependencies:

             createObjects, createRelations, refreshObjects, findWorkspaceObjects
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: ,
             e.g. if the service fails to connect to the configurator, or if an error was returned
             from the configurator.
        """
        ...
    def GetEffectivityConditions(self, AffectedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityFormulaeResponse:
        """    
             This operation returns the effectivity conditions associated with the objects specified
             in affectedObjects in form of a configurator
             specific formula string. This operation connects to the effectivity configurator
             service whose service endpoint is specified by the configuratorURL
             parameter. The actual conversion to formula strings is performed by this configurator
             service. The result may vary depending on the choice of service endpoint. For example
             a given configurator might return shorthand representations for formulae if these
             are unique in the context of the specified product. Teamcenter 9 only supports local
             built in Teamcenter configurators where parameter configuratorURL
             can be set to an empty string.
             

Use Cases:

             Obtain a formula string representation for the effectivity configuration conditions
             associated with set of design elements (Cpd0DesignModelElement) in a Collaborative
             Design model (Cpd0CollaborativeDesign).
             

Multiple weld points (Cpd0DesignFeature) exist in the context
             of a Design Control Element (Cpd0DesignControlElement).
             
The effectivity range for each weld point is therefore equivalent
             to the intersection between their own effectivity range and the range of effectivity
             for the Design Control Element (DCE).
             
In order to review the effectivity ranges an application requests
             the effectivity condition for each weld point using operation getEffectivityConditions.
             



Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param AffectedObjects: 
                         Contains objects for which effectivity conditions are requested. Only objects with
                         <font face="courier" height="10">EffectivityConfigurable</font> behavior such as
                         <b>Mdl0ConditionalArtifact</b> (e.g. <b>Ptn0ChildParentLink</b> or <b>Ptn0Membership</b>)
                         or <b>Mdl0ConditionalElement</b> (e.g. <b>Cpd0DesignControlElement</b>, <b>Cpd0DesignElement</b>,
                         <b>Cpd0DesignSubsetElement</b>, or <b>Cpd0ArcFilletWeld</b> and <b>Cpd0ArcGrooveWeld</b>)
                         can have effectivity conditions. For objects that either dont have <font face="courier" height="10">EffectivityConfigurable</font> behavior, or which are not associated
                         with an effectivity condition, a <i>NULL</i> configuration formula struct is returned.
             
        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: ,
             e.g. if the service fails to connect to the configurator, or if an error was returned
             from the configurator.
        """
        ...
    def GetEffectivityExpressions(self, Formulae: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigFormula], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityExpressionsResponse:
        """    
             This operation returns effectivity expressions for a given set of effectivity formulae
             in the context of the given productName and productNameSpace combination. This operation
             connects to the effectivity configurator service whose service endpoint is specified
             by the configuratorURL parameter. Any conversion from formula strings is performed
             by this configurator service. Depending on the (configurator specific) encoding the
             operation might require the specification of a product context using parameters productName
             and productNameSpace. For example, a given configurator might recognize shorthand
             representations for formulae if these are unique in the context of the specified
             product. Teamcenter 9 only supports local built in Teamcenter configurators where
             parameter configuratorURL can be set to an empty string. Teamcenter configurators
             dont require a product context if the formulae are in Explicit Teamcenter Language.
             The encoding is explicit if all lexemes are uniquely identified, e.g. [OptionNamespace]FamilyName
             = UniqueValue, where no product context is required to determine the family name
             for a value, or the option namespace for the family. A variant formula is in Explicit
Teamcenter Language if its form is explicit and comprised of the lexemes documented
             for the Teamcenter Variant Formula property. Teamcenter configurators support shorthand
             encodings like FamilyName = UniqueValue or UniqueValue if the lexemes
             used in the shorthand encoding are unique in the specified product context.
             

Use Cases:

             Obtain an effectivity expression (ConfigExpression) for a formula string representation
             (ConfigFormula) in the context of a Collaborative Design model (Cpd0CollaborativeDesign).
             
             Some effectivity SOA operations, e.g. getEffectivityConditions,
             formula string representations, which might be easier to review if presented in expression
             format.
             

A weld point (Cpd0DesignFeature) exists in the context of
             a Design Control Element (Cpd0DesignControlElement).
             
Effectivity Unit=10..UP is assigned to the weld point using operation
             setEffectivityConditions.
             
The same operation is then used to assign effectivity Unit=1..5 to
             Design Control Element (DCE), which reduces the effectivity range of all model elements
             controlled by this DCE. The result is that the weld point above is no longer effective
             since its effectivity range has no overlap with the DCE that controls it.
             
In order to understand why the weld point is not effective an application
             requests the effectivity condition for the weld point using operation getEffectivityConditions.
             
Depending on the number of control elements associated with this
             weld point the effectivity condition formula in the response might be difficult to
             comprehend. Therefore the application requests a conversion into an effectivity expression
             using operation getEffectivityExpressions.
             



Dependencies:

             getEffectivityConditions, setEffectivityConditions
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param Formulae: 
                         Vector of effectivity formulae in a configurator specific encoding.
             
        :param ProductName: 
                         Specifies a product. A (<font face="courier" height="10">productName,productNamespace</font>)
                         tuple is used as a parameter in configurator service calls so to allow the configurator
                         to resolve any ambiguity in effectivity condition parameters. Applications using
                         this <font face="courier" height="10">EffectivityManagement</font> service should
                         define a mechanism to obtain an appropriate value for this parameter. For example,
                         <font face="courier" height="10">ApplicationModel</font> objects like Collaborative
                         Design models (<b>Cpd0CollaborativeDesign</b>) make them available via properties
                         <font face="courier" height="10">mdl0config_product_name</font>, and <font face="courier" height="10">mdl0config_prod_namespace.</font>

        :param ProductNameSpace: 
                         Specifies a namespace in which parameter <font face="courier" height="10">productName</font>
                         has a unique definition, e.g. a specific model year, or product type. A (<font face="courier" height="10">productName,productNamespace</font>) tuple is used as a parameter in
                         configurator service calls so to allow the configurator to resolve any ambiguity
                         in effectivity condition parameters. Applications using this <font face="courier" height="10">EffectivityManagement</font> service should define a mechanism to obtain
                         an appropriate value for this parameter. For example, <font face="courier" height="10">ApplicationModel</font>
                         objects like Collaborative Design models (<b>Cpd0CollaborativeDesign</b>) make them
                         available via properties <font face="courier" height="10">mdl0config_product_name</font>,
                         and <font face="courier" height="10">mdl0config_prod_namespace.</font>

        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: , e.g. if the
             service fails to connect to the configurator, or if an error was returned from the
             configurator.
        """
        ...
    def GetEffectivityTables(self, Formulae: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigFormula], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityTablesResponse:
        """    
             This operation returns effectivity table representations in form of rows consisting
             of
             
             (effect in,effect out) tuples for a given set of effectivity condition formulae.
             This operation connects to the effectivity configurator service whose service endpoint
             is specified by the configuratorURL parameter. Any conversion from formula strings
             is performed by this configurator service. Depending on the (configurator specific)
             encoding the operation might require the specification of a product context using
             parameters productName and productNameSpace. For example, a given configurator might
             recognize shorthand representations for formulae if these are unique in the context
             of the specified product. Teamcenter 9 only supports local built in Teamcenter configurators
             where parameter configuratorURL can be set to an empty string. Teamcenter configurators
             dont require a product context if the formulae are in Explicit Teamcenter Language.
             The encoding is explicit if all lexemes are uniquely identified, e.g. [OptionNamespace]FamilyName
             = UniqueValue, where no product context is required to determine the family name
             for a value, or the option namespace for the family. A variant formula is in Explicit
             Teamcenter Language if its form is explicit and comprised of the lexemes documented
             for the Teamcenter Variant Formula property. Teamcenter configurators support
             shorthand encodings like FamilyName = UniqueValue or UniqueValue  if
             the lexemes used in the shorthand encoding are unique in the specified product context.
             

Use Cases:

             Obtain an effectivity table (EffectivityTable) for a formula string representation
             (ConfigFormula) in the context of a Collaborative Design model (Cpd0CollaborativeDesign).
             
             Some effectivity SOA operations, e.g. getEffectivityConditions,
             return formula string representations, which might be easier to review if presented
             in a table of rows consisting of (effect in,effect out) tuples.
             

Two weld points (Cpd0DesignFeature) exists, each in the context
             of multiple different Design Control Elements (Cpd0DesignControlElement).
             
The effectivity range for each weld point is therefore equivalent
             to the intersection between their own effectivity range and the combined range of
             effectivity for their respective set of Design Control Elements (DCE).
             
In order to compare the effectivity ranges for the 2 weld points
             an application requests the effectivity condition for each weld point using operation
             getEffectivityConditions.
             
Depending on the number of control elements associated with each
             weld point the effectivity condition formula in the response can be different even
             if their ranges are logically equivalent. Therefore the application requests a conversion
             to effectivity tables using operation getEffectivityTables
             so that the two effectivity ranges can be compared.
             



Dependencies:

             getEffectivityConditions
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param Formulae: 
                         Vector of effectivity formulae in a configurator specific encoding.
             
        :param ProductName: 
                         Specifies a product. A (<font face="courier" height="10">productName,productNamespace</font>)
                         tuple is used as a parameter in configurator service calls so to allow the configurator
                         to resolve any ambiguity in effectivity condition parameters. Applications using
                         this <font face="courier" height="10">EffectivityManagement</font> service should
                         define a mechanism to obtain an appropriate value for this parameter. For example,
                         <font face="courier" height="10">ApplicationModel</font> objects like Collaborative
                         Design models (<b>Cpd0CollaborativeDesign</b>) make them available via properties
                         <font face="courier" height="10">mdl0config_product_name</font>, and <font face="courier" height="10">mdl0config_prod_namespace.</font>

        :param ProductNameSpace: 
                         Specifies a namespace in which parameter <font face="courier" height="10">productName</font>
                         has a unique definition, e.g. a specific model year, or product type. A (<font face="courier" height="10">productName</font><i>,</i><font face="courier" height="10">productNamespace</font>)
                         tuple is used as a parameter in configurator service calls so to allow the configurator
                         to resolve any ambiguity in effectivity condition parameters. Applications using
                         this <font face="courier" height="10">EffectivityManagement</font> service should
                         define a mechanism to obtain an appropriate value for this parameter. For example,
                         <font face="courier" height="10">ApplicationModel</font> objects like Collaborative
                         Design models (<b>Cpd0CollaborativeDesign</b>) make them available via properties
                         <font face="courier" height="10">mdl0config_product_name</font>, and<font face="courier" height="10"> mdl0config_prod_namespace.</font>

        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: , e.g. if the service fails to connect
             to the configurator, or if an error was returned from the configurator.
        """
        ...
    def GetRevRuleEffectivityCriteria(self, RevisionRules: list[Teamcenter.Soa.Client.Model.Strong.RevisionRule], SubstituteDependentVariables: int, ApplyConstraints: int, ApplyDefaults: int, ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.RevRuleEffectivityCriteriaResponse:
        """    
             This operation returns the effectivity criteria associated with a set of RevisionRule
             objects. If a non zero value is specified for parameters substituteDependentVariables,
             applyConstraints, and/or applyDefaults, the operation will connect to the effectivity configurator
             specified by parameter configuratorURL. The
             actual evaluation of configurator rules, and conversions to and from formula strings,
             are performed by this configurator service. The resulting formula string conversions
             may vary depending on the choice of service endpoint. For example a given configurator
             might return shorthand representations for formulae if these are unique in the context
             of the specified product. Teamcenter 9 only supports local builtin Teamcenter configurators
             where parameter configuratorURL can be set
             to an empty string. Teamcenter configurators used in the EffectivityManagement service
             interface encode configuration formulae in Explicit Teamcenter Language for
             which no product context is required (see operation getEffectivityExpressions
             for more details on Explicit Teamcenter Language and productName and productNameSpace.
             

             Operation getRevRuleEffectivityCriteria should
             be used if symbolic variable substitution and/or constraint processing is required
             for *all* variant option families, or if validation records are required that specify
             violated constraints.
             


Use Cases:

             Use case 1:
             
             Initialize an effectivity criteria dialog for a given RevisionRule.
             

The application uses operation getRevRuleEffectivityCriteria
             with revisionRules={myRevRule}, productName=, productNameSpace=,
             substituteDependentVariables=0, applyConstraints=0.

The response will contain effectivity ranges as they are stored on
             RevisionRule myRevRule  without additional
             configurator processing. References to effectivity configuration families (ConfigurationFamily)
             are returned in ServiceData.
             



             Use case 2:
             
             Initialize an effectivity criteria dialog for a product that was created using the
             Teamcenter effectivity configurator with the intent to setup a new RevisionRule.
             

The application uses operation getRevRuleEffectivityCriteria
             with productName=MyProductItemID, productNameSpace=MyProductRevID,
             substituteDependentVariables=0, applyConstraints=0.

The response will contain all nominal effectivity ranges in this
             product. No constraint processing is required. References to effectivity configuration
             families (ConfigurationFamily) are returned in ServiceData.
             



             Use case 3:
             
             Initialize an effectivity criteria dialog for a product that is associated with a
             Collaborative Design (CD) model with the intent to setup a new RevisionRule.
             

Identifiers for the product associated with the CD (Cpd0CollaborativeDesign)
             are obtained from CD  properties mdl0config_product_name,
             and mdl0config_prod_namespace.
             
The application uses operation getRevRuleEffectivityCriteria
             with productName= , productNameSpace=  as obtained
             in the previous step, substituteDependentVariables=0, applyConstraints=0.

The response will contain all nominal effectivity ranges in this
             product. No constraint processing is required. References to effectivity configuration
             families (ConfigurationFamily) are returned in ServiceData.
             



Dependencies:

             findWorkspaceObjects
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param RevisionRules: 
                         A vector of <b>RevisionRule</b> objects for which effectivity criteria are requested.
             
        :param SubstituteDependentVariables: 
                         Indicates whether or not to substitute dependent variables, such as <font face="courier" height="10">PlantVacationShutdown</font>. Value <i>0</i> will indicate no substitution
                         is required. A value of <i>1</i> will enable substitution of dependent variables
             
        :param ApplyConstraints: 
                         Indicates whether or not to apply the constraints. Value <i>0</i> will indicate constraint
                         application is not required. A value of <i>1</i> will enable application of constraints.
             
        :param ApplyDefaults: 
                         Indicates whether or not to apply defaults. Value <i>0</i> will indicate that defaults
                         should not be applied. A value of <i>1</i> will enable application of defaults.
             
        :param ProductName: 
                         Specifies a product. A (<font face="courier" height="10">productName,productNamespace</font>)
                         tuple is used as a parameter in configurator service calls so to allow the configurator
                         to resolve any ambiguity in effectivity condition parameters. Applications using
                         this <font face="courier" height="10">EffectivityManagement</font> service should
                         define a mechanism to obtain an appropriate value for this parameter. For example,
                         <font face="courier" height="10">ApplicationModel</font> objects like Collaborative
                         Design models (<b>Cpd0CollaborativeDesign</b>) make them available via properties
                         <font face="courier" height="10">mdl0config_product_name</font>, and <font face="courier" height="10">mdl0config_prod_namespace.</font>

        :param ProductNameSpace: 
                         Specifies a namespace in which parameter <font face="courier" height="10">productName</font>
                         has a unique definition, e.g. a specific model year, or product type. A (<font face="courier" height="10">productName,productNamespace</font>) tuple is used as a parameter in
                         configurator service calls so to allow the configurator to resolve any ambiguity
                         in effectivity condition parameters. Applications using this <font face="courier" height="10">EffectivityManagement</font> service should define a mechanism to obtain
                         an appropriate value for this parameter. For example, <font face="courier" height="10">ApplicationModel</font>
                         objects like Collaborative Design models (<b>Cpd0CollaborativeDesign</b>) make them
                         available via properties <font face="courier" height="10">mdl0config_product_name</font>,
                         and <font face="courier" height="10">mdl0config_prod_namespace.</font>

        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: 
        """
        ...
    def SetEffectivityConditions(self, SampleObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], Formulae: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigFormula], Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], OpCode: int, ActionCode: int, AffectedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], ReplacedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityConditionResponse:
        """    
             This operation applies the specified effectivity condition to all objects listed
             in affectedObjects and their sub objects
             (where applicable) in the context of the given (productName,productNameSpace)
             combination.
             
             The operation returns formulae for created/modified effectivity conditions in a configurator
             specific encoding along with a reference to the modified objects. This operation
             connects to the effectivity configurator service whose service endpoint is specified
             by the configuratorURL parameter. The actual
             conversion to and from formula strings is performed by this configurator service.
             The result may vary depending on the choice of service endpoint. For example a given
             configurator might return shorthand representations for formulae if these are unique
             in the context of the specified product. Teamcenter 9 only supports local built in
             Teamcenter configurators where parameter configuratorURL
             can be set to an empty string. Teamcenter configurators used in the EffectivityManagement service interface encode configuration formulae
             in Explicit Teamcenter Language for which no product context is required (see
             operation getEffectivityExpressions for more
             details on Explicit Teamcenter Language  and productName
             and productNameSpace).
             

             If the effectivity condition are propagated to sub elements (e.g. sub ordinate elements
             associated with a DesignElement of category Reuse, or design features such as weld
             points associated with a Design Control Element), then these sub elements are returned
             as modified objects in the ServiceData.
             


Use Cases:

             Use case 1:
             
             Assign an effectivity condition to a design feature (Cpd0DesignFeature) in
             a Collaborative Design model (Cpd0CollaborativeDesign).
             

Two alternative weld points exist in the context of a common Design
             Control Element (DCE).
             
Effectivity Unit=1..9 is assigned to the first weld point
             using operation setEffectivityConditions.
             
Effectivity Unit=10..UP  is assigned to the second weld point
             using the same service operation.
             
Then effectivity Unit=5..15 is assigned to the DCE (Cpd0DesignControlElement),
             which reduces the effectivity range of all elements controlled by this DCE. The result
             is that the first weld point is effective for Unit=5..9, while the second
             is effective Unit=10..15.

Finally a NULL effectivity range is assigned to the DCE, which removes
             the effectivity condition from the DCE, and extends the effectivity range of all
             elements controlled by this DCE to their original values. The result is that the
             first weld point is again effective for Unit=1..9, while the second is effective
             Unit=10..UP.




             Use case 2:
             
             Assign an effectivity condition to a Design Element (DE) such that its effectivity
             range covers the combined range of effectivity of multiple other DEs in a Collaborative
             Design (CD) model.
             

Multiple alternative radar systems and radar screens exist in a CD
             (Cpd0CollaborativeDesign). Radar system R1 is effective for Unit=1..10,
             while radar system R2 is effective for Unit=11..UP. Radar display unit
             D1 is effective for Unit=1..5, while radar display unit D2 is
             effective for Unit=6..UP. I.e. every product unit has exactly one radar system
             and one radar screen, but the combination of radar systems and screens varies for
             different product units.
             
The same radar cable C1 connects all radar units with their
             display screens. C1 is effective for Unit=1..UP.

Effective Unit=3..UP a new radar cable C2 shall replace
             C1 such that it covers the combined effectivity range for R1, R2, D1,
             and D2.
             
To achieve this goal, operation setEffectivityConditions is used
             to assign the combined effectivity range of R1, R2, D1, and D2, to
             the new radar cable C2 with affectedObjects={C2}, sampleObjects={R1,
             R2, D1, D2}, opCode=11 (OR), and actionCode=1 (OVERWRITE). C2s
             effectivity range is now Unit=1..UP, while its effectivity configuration
             formula is Unit=1..10 or Unit=11..UP or Unit=1..5 or Unit=6..UP.

C2s design is completed and reviewed in this state.
             
Finally operation setEffectivityConditions
             is used with affectedObjects={C2}, replacedObjects={C1}, formulae={Unit>=3},
             opCode=11 (OR), and actionCode=4 (REDUCE). C2s effectivity range
             is now Unit=3..UP, while C1s effectivity range is now Unit=1..2.




             Use case 3:
             
             Extend the effectivity range for a set of Design Elements (DE) such that their effectivity
             range also covers the combined effectivity configuration criteria attached to two
             RevisionRules.
             

Multiple alternative radar systems and radar screens exist in a CD
             (Cpd0CollaborativeDesign). Radar system R1 is effective for Unit={1, 3},
             while radar system R2 is effective for Unit={2, 4}. Radar display unit
             D1 is effective for Unit={1, 2}, while radar display unit D2
             is effective for Unit={3, 4}. I.e. all product units 1..4 have exactly
             one radar system and one radar screen, but the combination of radar systems and screens
             varies for different product units.
             
Field tests have shown that the combination between R1 and
             D2 is best. Therefore this combination shall be made effective for the upcoming
             new product units 5 and 6, represented by RevisionRules Rule1:Unit=5 and
             Rule2:Unit=6.

To achieve this goal, operation setEffectivityConditions is
             used to assign the combined effectivity configuration criteria associated to Rule1
             and Rule2, to affectedObjects={R1,D2} by using sampleObjects={Rule1,
             Rule2 }, opCode=11 (OR), and actionCode=2 (EXTEND). The result
             is that R1s effectivity range is now Unit={1, 3, 5, 6}, while D2s
             effectivity range is now Unit={3, 4, 5, 6}.




Dependencies:

             setEffectivityConditions
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param SampleObjects: 
                         Effectivity conditions on objects in this list are combined with <font face="courier" height="10">opCode</font> to form the effectivity condition to be set on <font face="courier" height="10">affectedObjects</font>. These may also include <b>RevisionRule</b> objects.
                         Can be empty.
             
        :param Formulae: 
                         Configuration formulae in this list are combined with <i>opCode</i> to form the effectivity
                         condition to be set on <font face="courier" height="10">affectedObjects</font>. Can
                         be empty.
             
        :param Expressions: 
                         Configuration expressions in this list are combined with <font face="courier" height="10">opCode</font>
                         to form the effectivity condition to be set on <font face="courier" height="10">affectedObjects</font>.
                         Can be empty.
             
        :param OpCode: 
                         Specifies how to combine the inputs given in <i>sampleObjects</i>, <i>formulae</i>,
                         and <i>expression</i>, e.g. 10 for <i>AND</i>, or <i>11</i> for <i>OR</i>. See<i>
</i><font face="courier" height="10">$TC_INCLUDE/ps/ps_tokens.h.</font>

        :param ActionCode: 
<ul>
<li type="disc">1 : Overwrite   SET
                         </li>
<li type="disc">2 : ExtendÂ Â Â Â   OR
                         </li>
<li type="disc">4 : ReduceÂ Â Â Â  AND
                         </li>
</ul>

        :param AffectedObjects: 
                         Lists objects to which the new effectivity condition sill be assigned.
             
        :param ReplacedObjects: 
                         Lists objects that will be replaced by corresponding elements in <font face="courier" height="10">affectedObjects</font> vector where <font face="courier" height="10">affectedObjects[index]
                         </font>replaces <font face="courier" height="10">replacedObjects[index] </font>if
                         and only if <font face="courier" height="10">replacedObjects[index] </font>is not
                         a <i>NULL</i> object, and <i>index</i> <font face="courier" height="10">replacedObjects.length().</font>
                         In this context replacing one object with another means that the effectivity range
                         of the replaced object will be reduced to no longer overlap with the effectivity
                         of the replacing object.
             
        :param ProductName: 
                         Specifies a product. A (<font face="courier" height="10">productName,productNamespace</font>)
                         tuple is used as a parameter in configurator service calls so to allow the configurator
                         to resolve any ambiguity in effectivity condition parameters. Applications using
                         this <font face="courier" height="10">EffectivityManagement</font> service should
                         define a mechanism to obtain an appropriate value for this parameter. For example,
                         <font face="courier" height="10">ApplicationModel</font> objects like Collaborative
                         Design models (<b>Cpd0CollaborativeDesign</b>) make them available via properties
                         <font face="courier" height="10">mdl0config_product_name</font>, and <font face="courier" height="10">mdl0config_prod_namespace.</font>

        :param ProductNameSpace: 
                         Specifies a namespace in which parameter <font face="courier" height="10">productName</font>
                         has a unique definition, e.g. a specific model year, or product type. A (<font face="courier" height="10">productName,productNamespace</font>) tuple is used as a parameter in
                         configurator service calls so to allow the configurator to resolve any ambiguity
                         in effectivity condition parameters. Applications using this <font face="courier" height="10">EffectivityManagement</font> service should define a mechanism to obtain
                         an appropriate value for this parameter. For example, <font face="courier" height="10">ApplicationModel</font>
                         objects like Collaborative Design models (<b>Cpd0CollaborativeDesign</b>) make them
                         available via properties <font face="courier" height="10">mdl0config_product_name</font>,
                         and <font face="courier" height="10">mdl0config_prod_namespace.</font>

        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: , e.g.
             if the service fails to connect to the configurator, or if an error was returned
             from the configurator.
        """
        ...
    def SetRevRuleEffectivityCriteria(self, SampleObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object], Formulae: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigFormula], Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], OpCode: int, SubstituteDependentVariables: int, ApplyConstraints: int, ApplyDefault: int, ActionCode: int, SolveType: int, SaveNow: bool, CreatePrivateCopy: bool, AffectedRevRules: list[Teamcenter.Soa.Client.Model.Strong.RevisionRule], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.RevRuleEffectivityCriteriaResponse:
        """    
             This operation assigns the specified effectivity criteria to the revision rules listed
             in affectedRevRules. If a (productName,productNameSpace)
             combination is specified, then existing validation records associated with this product
             will be added to the response. If a non zero value is specified for parameters substituteDependentVariables, applyConstraints, and/or applyDefaults,
             then corresponding effectivity configurator rules will be applied to the effectivity
             criteria and the corresponding validation records will be returned in the response
             structure. Runtime copies of the RevisionRules listed in affectedRevRules are created with the requested effectivity configuration
             criteria if parameter createPrivateCopy is
             set to true. In that case the response structure will reference the new runtime copies.
             Otherwise WRITE or REVISE privileges for affectedRevRules
             are required. If parameter saveNow is set to true and createPrivateCopy
             is set to false, then RevisionRule modifications are saved. Otherwise, affectedRevRules are updated, but not saved.
             

             This operation connects to the effectivity configurator service whose service endpoint
             is specified by the configuratorURL parameter. The actual conversion to and from
             formula strings is performed by this configurator service. The result may vary depending
             on the choice of service endpoint. For example a given configurator might return
             shorthand representations for formulae if these are unique in the context of the
             specified product. Teamcenter 9 only supports local built in Teamcenter configurators
             where parameter configuratorURL can be set to an empty string. Teamcenter
             configurators used in the EffectivityManagement service interface encode configuration
             formulae in Explicit Teamcenter Language for which no product context is required
             (see operation getEffectivityExpressions
             for more details on Explicit Teamcenter Language  and productName and productNameSpace).
             

             Parameter solveType can be used to specify a filter strategy when evalutating
             the effectivity configuration criteria. This parameter is used to combine one or
             more of the following with binary OR:
             


MISMATCH                    1: objects conflicting
             with the solve criteria
             
EXPLICIT                        2: objects explicitly
             satisfying the solve criteria
             
COPRIME                        4: objects potentially
             satisfying the solve criteria
             
TRUE                            8: objects having
             an effectivity condition = TRUE
             
FALSE                            16: objects
             having an effectivity condition = FALSE
             
CONDITION                    32: objects having
             a non constant effectivity condition
             
ERROR_CHECK                64: objects having
             effectivity conditions returning an error
             
NO_CONDITION            128: objects with configurable
             behavior without a condition
             
NO_CONFIG_BEHAVIOR    256: objects without configurable
             behavior
             
INVERT                        512: inverts the
             filter results
             



             For example a solveType value of 398=256+128+8+4+2 produces the same filter
             results as 529= 512+16+1, but is more efficient if most objects are expected to fail
             the filter. On the other hand if most objects are expected to pass the filter than
             529 is more efficient. If in doubt a value of 529 is recommended in most cases.
             

Use Cases:

             Setup a RevisionRule to define effectivity configuration criteria that cover
             the combined effectivity ranges of a set of Design Elements (DE) in a Collaborative
             Design (CD) model.
             


Multiple alternative radar systems and radar screens exist in a CD
             (Cpd0CollaborativeDesign). Radar system R1 is effective for Unit={1, 3}, while
             radar system R2 is effective for Unit={2, 4}. Radar display unit D1 is effective
             for Unit={1, 2}, while radar display unit D2 is effective for Unit={3, 4}.
             
A radar cable C1 shall be added to the CD suitable to connect any
             radar system with any radar screen. To find DEs that can exist together with any
             radar system and screen a RevisionRule shall be defined that covers their combined
             effectivity range.
             
To achieve this goal, operation setRevRuleEffectivityCriteria is
             used to assign the combined effectivity range for R1, R2, D1, and D2, to a transient
             RevisionRule copy of the system RevisionRule Rule1 Working; Any Status.
             
affectedRevRules={Rule1}
             
sampleObjects={R1, R2, D1, D2}
             
opCode=11 (OR)
             
actionCode=1 (SET)
             
substituteDependentVariables=0 (DISABLE)
             
applyConstraints=1 (ENABLE)
             
applyDefault=0 (DISABE)
             
solveType=529 (MISMATCH|FALSE|INVERT)
             
saveNow=false
             
createPrivateCopy=true
             
The result is that a new transient RevisionRule Rule1 is created
             with effectivity configuration criteria Unit=1..4.
             



Dependencies:

             setEffectivityConditions
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param SampleObjects: 
                         Effectivity conditions on objects in this list are combined with <font face="courier" height="10">opCode</font> to form the effectivity condition to be set on <font face="courier" height="10">affectedObjects</font>. These may also include <b>RevisionRule</b> objects.
                         Can be empty.
             
        :param Formulae: 
                         Configuration formulae in this list are combined with <font face="courier" height="10">opCode</font>
                         to form the effectivity condition to be set on <font face="courier" height="10">affectedObjects</font>.
                         Can be empty.
             
        :param Expressions: 
                         Configuration expressions in this list are combined with opCode to form the effectivity
                         condition to be set on <font face="courier" height="10">affectedObjects</font>. Can
                         be empty.
             
        :param OpCode: 
                         Specifies how to combine the inputs given in <i>sampleObjects</i>, <i>formulae</i>,
                         and <i>expression</i>, e.g. 10 for <i>AND, </i>or<i> 11 for OR. </i>See<i> $TC_INCLUDE/ps/ps_tokens.h.</i>

        :param SubstituteDependentVariables: 
                         Indicates whether or not to substitute dependent variables, such as <font face="courier" height="10">PlantVacationShutdown</font>. Value 0 will indicate no substitution is
                         required. A value of 1 will enable substitution of dependent variables. If this feature
                         is not supported by the selected configurator the value is ignored.
             
        :param ApplyConstraints: 
                         Indicates whether or not to apply the constraints. Value 0 will indicate constraint
                         application is not required. A value of 1 will enable application of constraints.
             
        :param ApplyDefault: 
                         Indicates whether or not to apply defaults. Value "0" will indicate that defaults
                         should not be applied. A value of "1" will enable application of defaults.
             
        :param ActionCode: 
<ul>
<li type="disc">1 : Overwrite  SET
                         </li>
<li type="disc">2 : Extend      OR
                         </li>
<li type="disc">4 : Reduce     AND
                         </li>
</ul>

        :param SolveType: 
<ul>
<li type="disc">1 : MISMATCH
                         </li>
<li type="disc">2 : EXPLICIT
                         </li>
<li type="disc">4 : COPRIME
                         </li>
<li type="disc">8 : TRUE
                         </li>
<li type="disc">16 : FALSE
                         </li>
<li type="disc">32 : CONDITION
                         </li>
<li type="disc">64 : ERROR_CHECK
                         </li>
<li type="disc">128 : NO_CONDITION
                         </li>
<li type="disc">256 : NO_CONFIG_BEHAVIOR
                         </li>
<li type="disc">512 : INVERT
                         </li>
</ul>

        :param SaveNow: 
                         Indicates whether the input revision rules should be saved in database. A true value
                         for this parameter takes effect only if <font face="courier" height="10">createPrivateCopy</font>
                         parameter is set to false.
             
        :param CreatePrivateCopy: 
                         Indicates whether runtime private copies of the revision rules need to be created
                         based on given revision rules and effectivity criteria.
             
        :param AffectedRevRules: 
                         Lists Revision Rules to which the new effectivity criteria will be assigned.
             
        :param ProductName: 
                         Specifies a product. A (<font face="courier" height="10">productName</font>,<font face="courier" height="10">productNamespace</font>) tuple is used as a parameter
                         in configurator service calls so to allow the configurator to resolve any ambiguity
                         in effectivity condition parameters. Applications using this <font face="courier" height="10">EffectivityManagement</font> service should define a mechanism to obtain
                         an appropriate value for this parameter. For example, <font face="courier" height="10">ApplicationModel</font>
                         objects like Collaborative Design models (<b>Cpd0CollaborativeDesign</b>) make them
                         available via properties <font face="courier" height="10">mdl0config_product_name</font>,
                         and <font face="courier" height="10">mdl0config_prod_namespace</font>.
             
        :param ProductNameSpace: 
                         Specifies a namespace in which parameter <font face="courier" height="10">productName</font>
                         has a unique definition, e.g. a specific model year, or product type. A (<font face="courier" height="10">productName</font>,<font face="courier" height="10">productNamespace</font>)
                         tuple is used as a parameter in configurator service calls so to allow the configurator
                         to resolve any ambiguity in effectivity condition parameters. Applications using
                         this <i>EffectivityManagement</i> service should define a mechanism to obtain an
                         appropriate value for this parameter. For example, <font face="courier" height="10">ApplicationModel</font>
                         objects like Collaborative Design models (<b>Cpd0CollaborativeDesign</b>) make them
                         available via properties <font face="courier" height="10">mdl0config_product_name</font>,
                         and <font face="courier" height="10">mdl0config_prod_namespace</font>.
             
        :param ConfiguratorURL: 
                         URL for the Effectivity Configurator service endpoint to connect to.
             
        :return: , e.g.
             if the service fails to connect to the configurator, or if an error was returned
             from the configurator.
        """
        ...
    def GetEffectivityDisplayString(self, Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2013_05.EffectivityManagement.EffectivityDisplayStringResponse:
        """    
             This operation returns a localized string representation for effectivity expressions.
             This string representation is the same that is used for display values of effectivity
             formula properties mdl0effectivity_formula and mdl0allowed_eff_formula.
             Applications can use this API to display effectivity conditions for objects that
             have not yet been saved with this effectivity, e.g. if multiple effectivity modifications
             are accumulated in a client session before they are saved. In this scenario effectivity
             properties are not (yet) available prior to saving modified objects.
             
             This operation connects to the effectivity configurator service whose service endpoint
             is specified by the configuratorURL parameter.
             The actual conversion to formula strings is performed by this configurator service.
             Depending on the (configurator specific) encoding the operation might require the
             specification of a product context using parameters productName
             and productNameSpace. For example, a given
             configurator might use  shorthand representations for formulae if these are unique
             in the context of the specified product. Teamcenter 10.1 only supports local built
             in Teamcenter configurators where parameter configuratorURL
             can be set to an empty string. Teamcenter configurators don't require a product context
             if the formulae are in Explicit Teamcenter Language. The encoding is explicit
             if all lexemes are uniquely identified, e.g. [OptionNamespace]FamilyName
             = UniqueValue, where no product context is required to determine the family
             name for a value, or the option namespace for the family. A configuration condition
             formula is in Explicit Teamcenter Language if its form is explicit and comprised
             of the lexemes documented for the Teamcenter Variant Formula property. Teamcenter
             configurators support shorthand encodings like FamilyName = UniqueValue
             or UniqueValue if the lexemes used in the shorthand encoding are unique in
             the specified product context.
             

Use Cases:

             An application prepares several effectivity conditions with the intent to save them
             to a set of objects using operation setEffectivityConditions. The application
             wants to display the effectivity display string that would get saved with setEffectivityConditions
             before actually saving them.
             

Dependencies:

             setEffectivityConditions
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param Expressions: 
                         Configuration expressions for which the effectivity display string is requested.
             
        :param ProductName: 
                         Identifies the product. It is used in conjunction with parameter <font face="courier" height="10">productNameSpace</font> to resolve potential ambiguity in variant option
                         value names, and to identify product context specific constraints. Teamcenter configurators
                         use a Multiple Field Key (MFK) stable identifier (see property <font face="courier" height="10">Item::fnd0VariantNamespace</font>) of the product item for <font face="courier" height="10">productName</font>. The <font face="courier" height="10">productName</font>
                         value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>) can be obtained
                         from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_product_name.</font>

        :param ProductNameSpace: 
                         Specifies the namespace for the product identifier. It is used in conjunction with
                         parameter <font face="courier" height="10">productName</font> to resolve potential
                         ambiguity in variant option value names, and to identify product context specific
                         constraints. Teamcenter configurators use the Revision ID of the product ItemRevision
                         for <font face="courier" height="10">productNameSpace</font>. The productNameSpace
                         value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>) can be obtained
                         from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_prod_namespace.</font>

        :param ConfiguratorURL: 

        :return: Response object containing effectivity display values.
        """
        ...
    def GetEffectivityOverlapStates(self, ReferenceExpressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], Expressions: list[Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression], ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2013_05.EffectivityManagement.EffectivityOverlapStateResponse:
        """    
             This operation determines and returns the degree of overlap between a set of effectivity
             expressions and a set of reference effectivity criteria expressions. When applications
             create or update DesignElements (DE) and assign effectivity, the UI may want to qualify
             the degree of overlap between the effectivity of the DE and the currently active
             RevRule effectivity criteria.
             
             The following example illustrates the overlap states for a set of expressions:
             
RevisionRule:     |---------------|
             
             Object 0:  |----|                            : OverlapStateNone
             
             Object 1:     |------|                       : OverlapStateIntersect
             
             Object 2:                |----|              : OverlapStateSubset
             
             Object 3:                    |------|        : OverlapStateIntersect
             
             Object 4:  |-----------------------------|   : OverlapStateSuperset
             
             Object 5:         |---------------|          : OverlapStateMatch
             
             Object 6:         |-------------------|      : OverlapStateSuperset
             
             Object 7:     |-------------------|          :
             OverlapStateSuperset

             This operation connects to the effectivity configurator service whose service endpoint
             is specified by the configuratorURL parameter.
             Any conversion from formula strings is performed by this configurator service. Depending
             on the (configurator specific) encoding the operation might require the specification
             of a product context using parameters productName
             and productNameSpace. For example, a given
             configurator might recognize shorthand representations for formulae if these are
             unique in the context of the specified product. Teamcenter 10.1 only supports local
             built in Teamcenter configurators where parameter configuratorURL
             can be set to an empty string. Teamcenter configurators don't require a product context
             if the formulae are in Explicit Teamcenter Language. The encoding is explicit
             if all lexemes are uniquely identified, e.g. [OptionNamespace]FamilyName
             = UniqueValue, where no product context is required to determine the family
             name for a value, or the option namespace for the family. A configuration expression
             formula is in Explicit Teamcenter Language if its form is explicit and comprised
             of the lexemes documented for the Teamcenter Variant Formula property. Teamcenter
             configurators support shorthand encodings like FamilyName = UniqueValue or
             UniqueValue if the lexemes used in the shorthand encoding are unique in the
             specified product context.
             

Use Cases:

             An application wants to qualify effectivity conditions that were retrieved with getEffectivityConditions
             as to whether the condition is equal to, intersects with, or is a subset or superset
             of the effectivity criteria associated with one or more RevisionRules. This
             cannot be achieved with properties on effectivity conditions or RevisionRules because
             the result depends on the combination of an effectivity condition and the effectivity
             configuration criteria on a RevisionRule. One and the same condition may have
             different overlap states with different RevisionRules.
             
             The application calls getEffectivityOverlapStates and passes the effectivity
             criteria (as obtained from a RevisionRule using getRevRuleEffectivityCriteria)
             as referenceExpressions, and the effectivity
             conditions (as obtained from a set of product data elements using getEffectivityConditions)
             as expressions.
             


Dependencies:

             getEffectivityConditions, getRevRuleEffectivityCriteria
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param ReferenceExpressions: 
                         The vector of reference effectivity criteria expressions.
             
        :param Expressions: 
                         Vector of effectivity expressions. The response returns the overlap state of each
                         expression in this vector, with each of the reference effectivity criteria expressions
                         given in the <font face="courier" height="10">referenceExpressions</font> parameter.
             
        :param ProductName: 
                         Identifies the product. It is used in conjunction with parameter <font face="courier" height="10">productNameSpace</font> to resolve potential ambiguity in variant option
                         value names, and to identify product context specific constraints. Teamcenter configurators
                         use a Multiple Field Key (MFK) stable identifier (see property <font face="courier" height="10">Item::fnd0VariantNamespace</font>) of the product item for <font face="courier" height="10">productName</font>. The <font face="courier" height="10">productName</font>
                         value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>) can be obtained
                         from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_product_name.</font>

        :param ProductNameSpace: 
                         Specifies the namespace for the product identifier. It is used in conjunction with
                         parameter <font face="courier" height="10">productName</font> to resolve potential
                         ambiguity in variant option value names, and to identify product context specific
                         constraints. Teamcenter configurators use the Revision ID of the product <b>ItemRevision</b>
                         for <font face="courier" height="10">productNameSpace</font>. The <font face="courier" height="10">productNameSpace</font> value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>)
                         can be obtained from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_prod_namespace.</font>

        :param ConfiguratorURL: 
                         The service end point for the effectivity configurator service. If empty the local
                         Teamcenter configurator is used. Tc10.1 only supports local Teamcenter configurators.
                         In Tc10.1 a non-empty <font face="courier" height="10">configuratorURL</font> parameter
                         will cause an error.
             
        :return: Compares each effectivity expressions with each reference expression and returns
             the degreee of overlap
        """
        ...
    def GetEffectivitySubsetTables(self, ProductName: str, ProductNamespace: str, SubsetCriteria: Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression, EffectivityConditions: list[Fnd0.Services.Strong.Configfiltercriteria._2017_05.EffectivityManagement.EffectivityConditionSource]) -> Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.EffectivityTablesResponse: ...
    def SetEffectivityConditionSubsets(self, ProductName: str, ProductNamespace: str, SubsetCriteria: Fnd0.Services.Strong.Configfiltercriteria._2011_06.EffectivityManagement.ConfigExpression, ActionCode: int, EffectivityConditions: list[Fnd0.Services.Strong.Configfiltercriteria._2017_05.EffectivityManagement.EffectivityConditionInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class VariantManagementRestBindingStub(VariantManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetProductConfigurations(self, ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2013_05.VariantManagement.VariantCriteriaResponse: ...

class VariantManagementService:
    """
    
            The VariantManagement service interface provides operations to manage variant conditions
            on product data, and variant criteria on VariantRule and StoredOptionSet objects.
            


Library Reference:

Fnd0SoaConfigFilterCriteriaStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> VariantManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetProductConfigurations(self, ProductName: str, ProductNameSpace: str, ConfiguratorURL: str) -> Fnd0.Services.Strong.Configfiltercriteria._2013_05.VariantManagement.VariantCriteriaResponse:
        """    
             This operation returns a set of product configurations managed at the configurator
             level, say for product tracking or reporting purposes.
             
             Teamcenter variant configurators manage product configurations as VariantRules
             which are attached to an ItemRevision representing the product using any relationship
             type (see also preference TC_Default_SVR_Relationship).
             The product is identified by productName
             and productNameSpace parameters. Teamcenter
             configurators use a Multiple Field Key (MFK) stable identifier (see property Item::fnd0VariantNamespace) of the product item
             for productName, and the revision ID for
             productNameSpace. The identifiers of the
             product associated with a Collaborative Design (Cpd0CollaborativeDesign) can
             be obtained from properties Mdl0ApplicationModel::mdl0config_product_name,
             and Mdl0ApplicationModel::mdl0config_prod_namespace.
             

Use Cases:

             An engineering project administrator has created a product ItemRevision. A
             manufacturing engineering user creates and maintains VariantRules that represent
             a set of configurations for prototype builds. The project administrator attaches
             these VariantRules to the product ItemRevision. Product engineering
             users can use operation getProductConfigurations
             to review existing prototype configurations. The user can then chose one of the configurations
             to initialize variant configuration criteria with operation setVariantCriteria.
             

Dependencies:

             setVariantCriteria
             

Teamcenter Component:

             Configuration Management - Capability to configure structured data based on revsion
             rules; effectivities; Status etc.
             
        :param ProductName: 
                         Identifies the product. It is used in conjunction with parameter <font face="courier" height="10">productNameSpace</font> to resolve potential ambiguity in variant option
                         value names, and to identify product context specific constraints. Teamcenter configurators
                         use a Multiple Field Key (MFK) stable identifier (see property <font face="courier" height="10">Item::fnd0VariantNamespace</font>) of the product item for <font face="courier" height="10">productName</font>. The <font face="courier" height="10">productName</font>
                         value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>) can be obtained
                         from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_product_name</font>.
             
        :param ProductNameSpace: 
                         Specifies the namespace for the product identifier. It is used in conjunction with
                         parameter <font face="courier" height="10">productName</font> to resolve potential
                         ambiguity in variant option value names, and to identify product context specific
                         constraints. Teamcenter configurators use the Revision ID of the product <b>ItemRevision</b>
                         for <font face="courier" height="10">productNameSpace</font>. The <font face="courier" height="10">productNameSpace</font> value for a Collaborative Design (<b>Cpd0CollaborativeDesign</b>)
                         can be obtained from property <font face="courier" height="10">Mdl0ApplicationModel::mdl0config_prod_namespace</font>.
             
        :param ConfiguratorURL: 
                         The service end point for the variant configurator service. If empty the local Teamcenter
                         configurator is used. Tc10.1 only supports local Teamcenter configurators. In Tc10.1
                         a non-empty <font face="courier" height="10">configuratorURL</font> parameter will
                         cause an error.
             
        :return: Response object containing variant criateria list.
        """
        ...

