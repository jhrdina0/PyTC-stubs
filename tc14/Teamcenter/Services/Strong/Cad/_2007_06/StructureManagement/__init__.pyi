import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClassicOptionInfo:
    """
    Contains the information about classic variant option.
    """
    def __init__(self, ) -> None: ...
    OptionName: str
    """Refers to classic variant option name."""
    OptionDesc: str
    """Refers to classic variant option description."""
    Values: list[str]
    """
            Refers to list of classic variant option values. This input is given for new or update
            scenarios.
            """
    ExistingValues: list[str]
    """Refers to list of existing classic variant option values."""

class CreateOrUpdateVariantCondInput:
    """
    
            Contains the input for create/update variant condition associated with a BOMLine
            object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created."""
    Operation: str
    """
            This indicates the operation type which can be create or update variant condition.
            Legal values are: Create and Update.
            """
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Refers to BOMLine object on which variant condition has been defined."""
    VariantCondInfo: list[VariantCondInfo]
    """
            Refers to a list of VariantCondInfo struct,
            and contains the information needed to create/update a variant condition.
            """

class CreateUpdateClassicOptionsInput:
    """
    
            Contains the input for creating or updating classic variant options associated with
            a BOMLine object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Refers to clientId attribute."""
    Operation: str
    """
            Refers to operation type, as defined in OptionOperation.
            The operation could be CreateOption, AddValue, RemoveValue
            or ReplaceValue.
            """
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Refers to BOMLine object on which classic variant options are created or updated."""
    Options: list[ClassicOptionInfo]
    """
            Refers to list of ClassicOptionInfo structure
            which needs to be updated.
            """

class DelClassicOptionsInput:
    """
    
            Contains the input for deleting variant condition associated with a BOMLine
            object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created."""
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Refers to BOMLine object on which classic variant options are defined, which
            needs to be deleted.
            """
    OptionNames: list[str]
    """Refers to list of classic variant option names which are needs to be deleted."""

class DeleteVariantCondInput:
    """
    
            This contains the input for deleting variant condition associated with a BOMLine
            object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created."""
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            Refers to BOMLine object on which variant conditions are defined, which needs
            to be deleted.
            """

class GetConfiguredItemRevisionInfo:
    """
    
            Contains the item/item revision object reference and revision rule object reference
            to find the configured itemRevision.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """object reference of the item / item revision"""
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """Teamcenter::RevisionRuleImpl object reference"""

class GetConfiguredItemRevisionOutput:
    """
    The response for the getConfiguredItemRevision operation.
    """
    def __init__(self, ) -> None: ...
    InputInfo: GetConfiguredItemRevisionInfo
    """Member of type GetConfiguredItemRevisionInfo, copy of input data"""
    ConfiguredItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision object reference found"""

class GetConfiguredItemRevisionResponse:
    """
    The response for the getConfiguredItemRevision call.
    """
    def __init__(self, ) -> None: ...
    Output: list[GetConfiguredItemRevisionOutput]
    """A List of type GetConfiguredItemRevisionOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The SOA framework object containing plain objects and error information."""

class VariantCondInfo:
    """
    Contains the information neede to create/update a variant condition.
    """
    def __init__(self, ) -> None: ...
    OptionName: str
    """optionName"""
    JoinOperator: str
    """
            joinOperator  Legal values are: AND, OR, OPEN_BRACKET
            and CLOSE_BRACKET.
            """
    CompOperator: str
    """
            compOperator. Legal values are: EQ, NEQ, LT,
            GT, GTEQ
            and LTEQ.
            """
    Value: str
    """value"""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetConfiguredItemRevision(self, Inputs: list[GetConfiguredItemRevisionInfo]) -> GetConfiguredItemRevisionResponse:
        """    
             Finds the revision of the given item / item revision that is configured when the
             given revision rule is used to configure the given item / item revision.
             

Teamcenter Component:

             MCAD Integration - The set of capabilities that allow MCAD applications to integrate
             with the Tc server.
             
        :param Inputs: 
                         A list of GetConfiguredItemRevisionInfo structures, each of which contain a item
                         or item revision object and revision rule.
             
        :return: contains a ServiceData and a list of GetConfiguredItemRevisionOutput, each of which
             contain the configured item revision and list of GetConfiguredItemRevisionInfo structures,
             each of which contain the input object and revision rule. Any failure will be returned
             via ServiceData with original input object mapped to error message.
        """
        ...
    def CreateOrUpdateClassicOptions(self, InputObjects: list[CreateUpdateClassicOptionsInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             In the Create mode this operation creates a new option(s), with given option values,
             and declares them against the given ItemRevision object. In the update mode
             following operations can be performed with the given option
             

1.    Replace the current text value for the
             specified index with a new string from option revision.
             
2.    Add a new value to the option revision.
             
3.    Remove an existing value from the option
             revision.
             



Use Cases:

             This operation will be used when user wants to create classic variant options for
             a given BOMLine object(s). This also can be used to update an Option
             

a) adding a new value
             
b) removing an existing value
             
c) replace an existing value by new value.
             



Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         Refers to the list of CreateUpdateClassicOptionsInput struct, which are used to create
                         a new variant option or update an existing variant option.
             
        :return: 
        """
        ...
    def CreateOrUpdateVariantConditions(self, InputObjects: list[CreateOrUpdateVariantCondInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is to create or update (depending on the Operation) a variantCondition ( which
             is variant expression of type load if) for a BOMLine object.
             

Use Cases:

             This operation will be used when user wants to create a new or update an existing
             classic variant condition for a given BOMLine objects.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         This has the list of <font face="courier" height="10">CreateOrUpdateVariantCondInput</font>
                         struct, which are used to create a new variant condition or update an existing variant
                         condition.
             
        :return: 
        """
        ...
    def DeleteClassicOptions(self, InputObjects: list[DelClassicOptionsInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Delete option deletes the option and all the values associated with it.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         A list of DelClassicOptionsInput structures, each of which contains a bomline tag,
                         and list of options. If the option exists then it will be deleted.
             
        :return: ServiceData:Any failure will be returned via ServiceData with original input object
             mapped to error message.
        """
        ...
    def DeleteVariantConditions(self, InputObjects: list[DeleteVariantCondInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service will be used to delete the variant Condition(load_if) associated with
             a BOMLine If the variant condition exists then it will be deleted. Failure will be
             with client id and error message in the ServiceData.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         Consists of the clientId and the BOMLine for which we need to delete the variant
                         Condition
             
        :return: ServiceData
        """
        ...

