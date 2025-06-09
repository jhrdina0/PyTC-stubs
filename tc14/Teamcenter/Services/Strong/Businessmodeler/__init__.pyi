import System
import Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants
import Teamcenter.Services.Strong.Businessmodeler._2007_06.RulesBasedFramework
import Teamcenter.Services.Strong.Businessmodeler._2008_06.ConditionEngine
import Teamcenter.Services.Strong.Businessmodeler._2008_06.DeepCopyRules
import Teamcenter.Services.Strong.Businessmodeler._2010_04.BusinessRules
import Teamcenter.Services.Strong.Businessmodeler._2011_06.Constants
import Teamcenter.Soa.Client

class BusinessRulesRestBindingStub(BusinessRulesService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetVerificationRules(self, Input: list[Teamcenter.Services.Strong.Businessmodeler._2010_04.BusinessRules.VerificationRuleInput]) -> Teamcenter.Services.Strong.Businessmodeler._2010_04.BusinessRules.GetVerificationRulesResponse: ...

class BusinessRulesService:
    """
    
            The BusinessRules service exposes operations that are used to fetch or maintain
            BusinessRule objects. Common use includes Teamcenter Rich Client applications
            require BusinessRule objects administrator creates in Business Modeler IDE.
            
            This service provides following use case to deal with BusinessRule objects.
            

Query a set of VerificationRule objects defined in Business Modeler
            IDE with given search criteria
            




Library Reference:

TcSoaBusinessModelerStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> BusinessRulesService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetVerificationRules(self, Input: list[Teamcenter.Services.Strong.Businessmodeler._2010_04.BusinessRules.VerificationRuleInput]) -> Teamcenter.Services.Strong.Businessmodeler._2010_04.BusinessRules.GetVerificationRulesResponse:
        """    
             This operation gets a list of VerificationRule objects which match the given
             criteria each VerificationRuleInput supplied and its context_filter
             attribute which refers to a Condition object defined in Business Modeler
             IDE equals to true; Wild cards can be specified in strings using * in VerificationRuleInput
             which mean to match all cases for the criteria strings. This operation not only returns
             all VerificationRule objects which full match criteria in VerificationRuleInput,
             it also returns VerificationRule objects whose type attribute is the
             parent of the typeName defined in the VerificationRuleInput, meanwhile
             other criteria are matched.
             

Use Cases:

             4 samples Verification Rules created in Business Modeler IDE

             {Functionality= Fnd0BOMGrading, Business Object=Item, Context Filter =isTrue, Condition
             Rule=Condition1, Sub Group=*}
             
             {Functionality= Fnd0BOMGrading, Business Object=Part, Context Filter = isEngineeringGroup,
             Condition Rule=Condition1, Sub Group=*}
             
             {Functionality= Fnd0BOMGrading, Business Object= CommericalPart, Context Filter =isTrue,
             Condition Rule=Condition2, Sub Group= Americas}
             
             {Functionality= Fnd0APS, Business Object=Item, Context Filter =isTrue, Condition
             Rule=Condition1, Sub Group= *}
             
             Login Teamcenter as dba group and get VerificationRule objects by setting
             functionality as Fnd0BOMGrading and typeName as CommericalPart. Following
             VerificationRule objects in will be returned.
             
             {Functionality= Fnd0BOMGrading, Business Object=Item, Context Filter =isTrue, Condition
             Rule=Condition1, Sub Group=*}
             
             {Functionality= Fnd0BOMGrading, Business Object= CommericalPart, Context Filter =isTrue,
             Condition Rule=Condition2, Sub Group=Americas}
             
             The first rule applies to Item, if Condition1 could check Item, it
             could check CommericalPart, since CommericalPart is a sub type of Item
             and it is sure that CommericalPart contains all properties checked in Condition1,
             so it is valid. The second rule applies to all CommericalPart, so it is also
             valid. The other VerificationRule objects either do not match functionality
             or typeName, or else context_filter equals to false.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Input: 
                         The criteria for filtering the list of <b>VericationRule</b> objects.
             
        :return: objects.
        """
        ...

class ConditionEngineRestBindingStub(ConditionEngineService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def EvaluateConditions(self, Inputs: list[Teamcenter.Services.Strong.Businessmodeler._2008_06.ConditionEngine.ConditionInput]) -> Teamcenter.Services.Strong.Businessmodeler._2008_06.ConditionEngine.EvaluateConditionsResponse: ...

class ConditionEngineService:
    """
    
            The ConditionEngine service provides an operation
            to evaluate a Condition expression.  A Condition signature defines
            parameters (ConditionParameter) that are required (and are order dependent)
            to evaluate a specific Condition.  These parameters represent object instances
            from the Teamcenter database that can be used within the expression during evaluation.
            The evaluation of a Condition is performed by the CLIPS (3rd party) rules
            engine.  The evaluation of a Condition expression will always provide either a True or False
            result.  All of these Condition components are maintained in the BMIDE.
            

            Use case:
            

The ConditionEngine service can be used for supporting the following
            usecases:
            
Determine what List of Value (LOV) is applied when attaching
            an LOV to a property.
            
Determine when various kinds of rules (deep copy, naming, business
            object display, extension) are applied.
            
Determine when an Item Revision Definition Configuration (IRDC)
            applies to an item revision to control how document management processes affect item
            revision behavior in a document management system.
            
Configure Bill of Material (BOM) grading for part validation.
            
Configure user based access to project data.
            
Determine when a property renderer attachment is applied.
            
Determine when a business object constant is applied.
            




Library Reference:

TcSoaBusinessModelerStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ConditionEngineService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def EvaluateConditions(self, Inputs: list[Teamcenter.Services.Strong.Businessmodeler._2008_06.ConditionEngine.ConditionInput]) -> Teamcenter.Services.Strong.Businessmodeler._2008_06.ConditionEngine.EvaluateConditionsResponse:
        """    
             This operation tells the CLIPS rules engine to evaluate the expression defined on
             the specified Condition using the specified input parameter(s) defined on
             the ConditionParameter.  This operation takes as input a set of conditions
             along with parameters for each condition and returns a set of outputs containing
             the result (true/false) and exit code of each condition evaluation. There is a one
             to one correspondence between the elements in the input set and the elements in the
             output set.  This allows for evaluation of multiple conditions in one operation call.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Inputs: 
                         This is a set of condition(s) along with the corresponding input parameter value(s)
                         for each condition.
             
        :return: 
        """
        ...

class ConstantsRestBindingStub(ConstantsService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetGlobalConstantValues(self, Keys: list[str]) -> Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.GlobalConstantValueResponse: ...
    def GetPropertyConstantValues(self, Keys: list[Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.PropertyConstantKey]) -> Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.PropertyConstantValueResponse: ...
    def GetTypeConstantValues(self, Keys: list[Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.TypeConstantKey]) -> Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.TypeConstantValueResponse: ...
    def GetGlobalConstantValues2(self, Keys: list[str]) -> Teamcenter.Services.Strong.Businessmodeler._2011_06.Constants.GlobalConstantValueResponse2: ...

class ConstantsService:
    """
    
            Constants are a configuration point within the data model. There are three kinds
            of constants global, business object and property. Global constants provide
            consistent definitions that can be used throughout the system. These constants have
            one value, either the default value or the value user set. You can also provide multi
            value global constants.  Business object constant provide default values to
            business objects. Because these constants are attached to business objects, they
            are inherited and can be overridden in the hierarchy. Property constants are
            a configuration point within the data model that provides default values to business
            object properties. You can define a property constant to have a specific scope so
            that it is available only on certain properties on certain business objects.
            

            The Constants service provides operation
            to query the value of global, property, and type constants. The user will need to
            use these operations to retrieve the values of the constants and determine the system
            behavior based on the values.
            

            Use case
            
            The Constants service can be used for supporting following usecases
            

Query value of global constants
            
Query value of property constant
            
Query value of type constant
            




Library Reference:

TcSoaBusinessModelerStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ConstantsService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetGlobalConstantValues(self, Keys: list[str]) -> Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.GlobalConstantValueResponse:
        """    
             Global constants provide consistent definitions that can be used throughout the system.
             These constants have one or multiple values.  User can retrieve the values of global
             constants to determine the system behavior based on values. This operation gets the
             values of the named global constants (keys).
             This operation only supports single valued global constants, for multivalued constants
             use the getGlobalConstantValues2 operation.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         A list of the desired global constant names.
             
        :return: The values of the requested global constants. A partial error is returned if the
             name global constant cannot be added to the global default cache (74502), or if the
             named constant is multivalued(74528)
        """
        ...
    def GetPropertyConstantValues(self, Keys: list[Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.PropertyConstantKey]) -> Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.PropertyConstantValueResponse:
        """    
             This operation gets the values of the named property constants (keys).
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         A list of the desired property constant names.
             
        :return: The values of the requested propoerty constants. A partial error is returned if the
             name prooperty constant cannot be added to the type attach cache (74507), or if the
             prooperty constant value cannot be retrieved (74521)
        """
        ...
    def GetTypeConstantValues(self, Keys: list[Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.TypeConstantKey]) -> Teamcenter.Services.Strong.Businessmodeler._2007_06.Constants.TypeConstantValueResponse:
        """    
             This operation gets the values of the named type constants (keys).
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         A list of the desired type constants.
             
        :return: The values of the requested type constants. A partial error is returned if the name
             type constant cannot be added to the type attach cache (74505), or if the type constant
             value cannot be retrieved (74515)
        """
        ...
    def GetGlobalConstantValues2(self, Keys: list[str]) -> Teamcenter.Services.Strong.Businessmodeler._2011_06.Constants.GlobalConstantValueResponse2:
        """    
             Global constants provide consistent definitions that can be used throughout the system.
             These constants have one or multiple values.  User can retrieve the values of global
             constants to determine the system behavior based on values. This operation gets the
             values of the named global constants (keys).
             This operation supports single value and multi valued global constants. This operation
             replaces deprecated operation getGlobalConstantValues.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         A list of the desired global constant names.
             
        :return: The values of the requested global constants. A partial error is returned If the
             name global constant cannot be added to the global default cache (74502).
        """
        ...

class DeepCopyRulesRestBindingStub(DeepCopyRulesService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetDeepCopyInfo(self, Keys: list[Teamcenter.Services.Strong.Businessmodeler._2008_06.DeepCopyRules.DeepCopyInfoKey]) -> Teamcenter.Services.Strong.Businessmodeler._2008_06.DeepCopyRules.DeepCopyInfoResponse: ...

class DeepCopyRulesService:
    """
    
            The DeepCopyRules service exposes the operations
            that are used to perform revise or saveas operation on item revision objects. Deep
            copy rules define whether objects belonging to an item revision can be copied when
            a user performs a save as or revise operation on an item revision. Deep copy rules
            are applied only to item revision business objects and are inherited by children
            business objects.
            


Library Reference:

TcSoaBusinessModelerStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DeepCopyRulesService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetDeepCopyInfo(self, Keys: list[Teamcenter.Services.Strong.Businessmodeler._2008_06.DeepCopyRules.DeepCopyInfoKey]) -> Teamcenter.Services.Strong.Businessmodeler._2008_06.DeepCopyRules.DeepCopyInfoResponse:
        """    
             Deep copy rules define whether objects belonging to a business object instance can
             be copied when a user performs a save as or revise operation on that instance. Deep
             copy rules can be applied to any business object type, and are inherited by children
             business object types. This operation gets the applicable deep copy rules for the
             given list of objects and the operation specified for each object.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Keys: 
                         List of itemRevision object tag and the operation name for which deep copy information
                         is needed.
             
        :return: A structure containing the values of the applicable deep copy rules and status of
             the operation. This operation does not return any error other than propagating the
             errors received from low level functions which are called from within the operation.
        """
        ...

class RulesBasedFrameworkRestBindingStub(RulesBasedFrameworkService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExecuteRbfRules(self, Id: str, Inputs: list[Teamcenter.Services.Strong.Businessmodeler._2007_06.RulesBasedFramework.RbfNameValue]) -> Teamcenter.Services.Strong.Businessmodeler._2007_06.RulesBasedFramework.ExecuteRbfRulesResponse: ...

class RulesBasedFrameworkService:
    """
    
            The RulesBasedFramework (RBF) service provides
            an operation to evaluate an application extension rule (AppExtensionRule).
            The application extension rules are based on the definition of an application extension
            point (AppExtensionPoint) in a specified business context (BusinessContext).
            The evaluation of an application extension rule is performed by the CLIPS (3rd party)
            rules engine.  All of these RBF components are maintained in the BMIDE.
            

An application extension point exposes a point of configurability
            in Teamcenter using a decision table.  The decision table defines inputs and outputs
            that can be configured.
            
An application extension rule defines a set of input and output values
            based on the application extension point configuration.  It also defines a set of
            business contexts in which the rule can be applied.
            
A business context constrains an application extension rule to a
            specific environment in which a user works (organizational groups and roles).
            




Library Reference:

TcSoaBusinessModelerStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> RulesBasedFrameworkService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExecuteRbfRules(self, Id: str, Inputs: list[Teamcenter.Services.Strong.Businessmodeler._2007_06.RulesBasedFramework.RbfNameValue]) -> Teamcenter.Services.Strong.Businessmodeler._2007_06.RulesBasedFramework.ExecuteRbfRulesResponse:
        """    
             This operation invokes the CLIPS rules engine to apply the set of application extension
             rules that belong to the specified application extension point for the specified
             input name/value pairs.  The result of the execution is returned in the output name/value
             pairs.
             

Teamcenter Component:

             BMIDE (Server) - Set of services provided by BMIDE that allow efficiently underyling
             capabilities to develop/modify business objects
             
        :param Id: 
                         The application extension point ID for which this application extension rule is configured.
             
        :param Inputs: 
                         A set of input name/value pairs for the rules engine execution.
             
        :return: 
        """
        ...

