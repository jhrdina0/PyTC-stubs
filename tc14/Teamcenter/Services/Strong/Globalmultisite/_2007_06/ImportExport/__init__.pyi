import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateActionRuleInputData:
    """
    
            The CreateOrUpdateActionRuleInputData specifies
            complete data for creating an action rule.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the action rule which can be 32 characters long."""
    Description: str
    """The description of the action rule which can be 240 characters long."""
    Scope: str
    """The action rule is for import or export.  The value can be "IMPORT" or "EXPORT"."""
    SchemaFormat: str
    """The schema for the imported/exported xml file. The value can be "TCXML" or "PLMXML"."""
    ActionLocation: str
    """
            The  location where the action happens. The value could be "PREACTION", "DURINGACTION"
            or "POSTACTION".
            """
    ActionName: str
    """
            The Function handler which will be invoked when this rule is executed. For how to
            create a function for a action rule, please refer to PLM XML Import Export Administration
            Guide.
            """
    ActionRuleToUpdate: Teamcenter.Soa.Client.Model.Strong.PIEActionRule
    """Holds the reference of the action rule in case of modification."""

class CreateOrUpdateActionRuleResponse:
    """
    
            The CreateOrUpdateActionRuleResponse structure
            defines the response from createOrUpdateActionRules
            operation. It contains vector of action rule object references that were created
            on the server.
            
    """
    def __init__(self, ) -> None: ...
    ActionRuleObjects: list[Teamcenter.Soa.Client.Model.Strong.PIEActionRule]
    """A list of created or modified action rule objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class CreateOrUpdateClosureRuleInputData:
    """
    
            The CreateOrUpdateClosureRuleInputData specifies
            complete data for creating a closure rule.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the closure rule which can be 32 characters long."""
    Description: str
    """The description of the closure rule which can be 240 characters long."""
    Scope: str
    """The closure rule is for import or export.  The value can be "IMPORT" or "EXPORT"."""
    SchemaFormat: str
    """The schema for the imported/exported xml file. The value can be "TCXML" or "PLMXML"."""
    Comments: list[str]
    """The comments for every clause in this closure rule which can be 240 characters long."""
    Depth: list[int]
    """The depth for every clause in this closure rule."""
    Clauses: list[str]
    """The clause contents of closure rule which can be 240 characters long."""
    ClosureRuleToUpdate: Teamcenter.Soa.Client.Model.Strong.ClosureRule
    """Holds the reference of the closure rule in case of modification."""

class CreateOrUpdateClosureRuleResponse:
    """
    
            The CreateOrUpdateClosureRuleResponse structure
            defines the response from createOrUpdateClosureRules
            operation. It contains vector of closure rule object references that were created
            on the server.
            
    """
    def __init__(self, ) -> None: ...
    ClosureRuleObjects: list[Teamcenter.Soa.Client.Model.Strong.ClosureRule]
    """A list of created or modified closure rule objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class CreateOrUpdateFilterRuleInputData:
    """
    
            The CreateOrUpdateFilterRuleInputData specifies
            complete data for creating a filter rule.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the filter rule which can be 32 characters long."""
    Description: str
    """The description of the filter rule which can be 240 characers long."""
    Scope: str
    """The filter rule is for import or export. The value can be "IMPORT" or "EXPORT"."""
    SchemaFormat: str
    """The schema for the imported/exported xml file. The value can be "TCXML" or "PLMXML"."""
    Clauses: list[str]
    """The  clauses contents of filter rule which can be 128 characters long."""
    FilterRuleToUpdate: Teamcenter.Soa.Client.Model.Strong.Filter
    """Holds the reference of the filter rule in case of modification."""

class CreateOrUpdateFilterRuleResponse:
    """
    
            The CreateOrUpdateFilterRuleResponse structure
            defines the response from createOrUpdateFilterRules
            operation. It contains vector of filter rule object references that were created
            on the server.
            
    """
    def __init__(self, ) -> None: ...
    FilterRuleObjects: list[Teamcenter.Soa.Client.Model.Strong.Filter]
    """A list of created or modified filter rule objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class CreateOrUpdatePropertySetInputData:
    """
    
            The CreateOrUpdatePropertySetInputData specifies
            complete data for creating a property set.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the property set which can be 32 characters long."""
    Description: str
    """The description of the property set which can be 240 characters long."""
    Scope: str
    """The property set is for import or export. The value can be "IMPORT" or "EXPORT"."""
    Clauses: list[str]
    """The clause contents of property set which can be 128 characters long."""
    PropertySetToUpdate: Teamcenter.Soa.Client.Model.Strong.PropertySet
    """Holds the reference of the property set in case of modification."""

class CreateOrUpdatePropertySetRuleResponse:
    """
    
            The CreateOrUpdatePropertySetResponse structure
            defines the response from createOrUpdatePropertySets operation. It contains vector
            of property sets object references that were created on the server.
            
    """
    def __init__(self, ) -> None: ...
    PropertySetObjects: list[Teamcenter.Soa.Client.Model.Strong.PropertySet]
    """A list of created or modified property set objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class CreateOrUpdateTransferModeInputData:
    """
    
            The CreateOrUpdateTransferModeInputData specifies
            complete data for creating a transfer mode.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the transfer mode which can be 128 characters long."""
    Description: str
    """The description of the transfer mode which can be 240 characters long."""
    ContextString: str
    """The context string used in export/import. The value can be 240 characters long."""
    Direction: str
    """
            Defines the transfer mode is for import or export.  The value can be "IMPORT" or
            "EXPORT".
            """
    SchemaFormat: str
    """The schema for the imported/exported xml file. The value can be "TCXML" or "PLMXML"."""
    IsIncremental: bool
    """Specifies whether transfermode can be used in incremental data transfer or not."""
    IsMultiSite: bool
    """Specifies whether transfermode is multisite or not."""
    Closurerule: Teamcenter.Soa.Client.Model.Strong.ClosureRule
    """The closure rule reference for the transfer mode."""
    Filter: Teamcenter.Soa.Client.Model.Strong.Filter
    """The filter rule reference for the transfer mode."""
    Propertyset: Teamcenter.Soa.Client.Model.Strong.PropertySet
    """The property set reference for the transfer mode."""
    XsltFiles: list[Teamcenter.Soa.Client.Model.Strong.ImanFile]
    """The style sheet file reference for the transfer mode."""
    ConfigObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The revision rule reference for the transfer mode."""
    ActionList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The action rule reference for the transfer mode."""
    TmToUpdate: Teamcenter.Soa.Client.Model.Strong.TransferMode
    """Holds the reference of the transfer mode in case of modification."""

class CreateOrUpdateTransferModeResponse:
    """
    
            The CreateOrUpdateTransferModeResponse structure
            defines the response from createOrUpdateTransferModes
            operation. It contains vector of transfer mode object references that were created
            on the server.
            
    """
    def __init__(self, ) -> None: ...
    TransferModeObjects: list[Teamcenter.Soa.Client.Model.Strong.TransferMode]
    """A list of created or modified transfer mode objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class CreateOrUpdateTransferOptionSetInputData:
    """
    
            The CreateOrUpdateTransferOptionSetInputData structure defines the input data for
            creating a TransferOptionSetObject.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the transfer opton set."""
    Description: str
    """The description of the transfer opton set."""
    PubliclyVisible: bool
    """
            Specifies whether it is public or private. If the value is true, the transfer option
            set will be visibale and used for all user.
            """
    SiteId: Teamcenter.Soa.Client.Model.Strong.POM_imc
    """Specifies the site reference (local site or remote site)."""
    Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode
    """Specifies the transfer mode reference."""
    Options: list[OptionInputData]
    """The vector of options (See OptionInputData structure)."""
    OptionSetObjectToModify: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet
    """This holds the reference to transfer option set object in case of modification."""

class CreateOrUpdateTransferOptionSetResponse:
    """
    
            The CreateOrUpdateTransferOptionSetResponse structure defines the response from createOrUpdateTransferOptionSets
            operation. It contains vector of TransferOptionSet object references that were created
            on the server.
            
    """
    def __init__(self, ) -> None: ...
    TransferOptionSets: list[Teamcenter.Soa.Client.Model.Strong.TransferOptionSet]
    """A list of created or modified transfer option set objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class GetActionRulesResponse:
    """
    
            The GetActionRulesResponse structure defines
            the response from getActionRules operation.
            It contains vector of action rule object references that were created on the server
            that satisfy the input criteria scope and schema format.
            
    """
    def __init__(self, ) -> None: ...
    ActionRuleObjects: list[Teamcenter.Soa.Client.Model.Strong.PIEActionRule]
    """A list of action rule objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class GetAllTransferOptionSetsResponse:
    """
    
            The GetAllTransferOptionSetsResponse structure
            defines the response from getAllTransferOptionSets
            operation. It contains vector of transfer option set object references that were
            present on the server.
            
    """
    def __init__(self, ) -> None: ...
    OptionSetObjects: list[Teamcenter.Soa.Client.Model.Strong.TransferOptionSet]
    """A list of transfer option sets."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class GetAvailableTransferOptionSetsInputData:
    """
    
            The structure GetAvailableTransferOptionSetsInputData
            defines input criteria for the operation getAvailableTransferOptionSets.
            The values of isPush, isExport are to be known before calling this operation.
            

            Case 1: Remote ExportÂ Â Â Â - on-line  --- isPush = True   isExport
            = True
            
            Case 2: Remote ImportÂ Â Â Â - on-line  --- isPush = False  isExport
            = True
            
            Case 3: Briefcase Export - off-line --- isPush
            = True   isExport = True
            
            case 4: Briefcase Import - off-line --- isPush = NAÂ Â Â Â  isExport
            = False
            

            For 2007.1, the site can not be more than one for the Push case. The access rules
            will be evaluated thru RBF (Rules Based Framework) for the given user, group, role
            and all the option sets that satisfy the criteria will be returned
            
    """
    def __init__(self, ) -> None: ...
    User: Teamcenter.Soa.Client.Model.Strong.User
    """The user reference that executing this API."""
    Group: Teamcenter.Soa.Client.Model.Strong.Group
    """The group reference that the executing user belongs to."""
    Role: Teamcenter.Soa.Client.Model.Strong.Role
    """The role reference that the executing user belongs to."""
    Site: list[Teamcenter.Soa.Client.Model.Strong.POM_imc]
    """The site that the user want to export to."""
    IsPush: bool
    """Option that control the online or offline."""
    IsExport: bool
    """Option that control the data transfer direction."""

class GetAvailableTransferOptionSetsResponse:
    """
    
            The GetAvailableTransferOptionSetsResponse
            structure defines the response from getAvailableTransferOptionSets
            operation. It contains vector of transfer option set object references that satisfies
            the input criteria.
            
    """
    def __init__(self, ) -> None: ...
    OptionSetObjects: list[Teamcenter.Soa.Client.Model.Strong.TransferOptionSet]
    """A list of transfer option set objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class GetClosureRulesResponse:
    """
    
            The GetClosureRulesResponse structure defines
            the response from getClosureRules operation.
            It contains vector of closure rule object references that were created on the server
            that satisfy the input criteria scope and schema format.
            
    """
    def __init__(self, ) -> None: ...
    ClosureRuleObjects: list[Teamcenter.Soa.Client.Model.Strong.ClosureRule]
    """A list of closure rule objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class GetFilterRulesResponse:
    """
    
            The GetFilterRulesResponse structure defines
            the response from getFilterRules operation.
            It contains vector of filter rule object references that were created on the server
            that satisfy the input criteria scope and schema format.
            
    """
    def __init__(self, ) -> None: ...
    FilterRuleObjects: list[Teamcenter.Soa.Client.Model.Strong.Filter]
    """A list of filter rule objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class GetPLMXMLRuleInputData:
    """
    
            The structure GetPLMXMLRuleInputData is used
            for many operations related to PLMXML Admin application. This structure specifies
            input criteria for get list methods for Transfermode, closure rule, filter rule action
            rule. The get list operation is expected to return all rule objects based on the
            given scope and schema format.
            
    """
    def __init__(self, ) -> None: ...
    Scope: str
    """
            The direction that scope rule is used. The allowed values are"EXPORT", "IMPORT" or
            "ALL". When the value is "EXPORT", only export based scope rules will be queried.
            Value "ALL" implies both export and import scope rules will be queried.
            """
    SchemaFormat: str
    """
            The schema format associated with the scope rule. The allowed values are "PLMXML"
            or  "TCXML" or "ALL". When the value is "PLMXML", only PLMXML based scope rules will
            be queried. Value "ALL" implies both PLMXML and TCXML scope rules will be queried.
            """

class GetPropertySetsResponse:
    """
    
            The GetPropertySetsResponse structure defines
            the response from getPropertySets operation.
            It contains vector of property set object references that were created on the server
            that satisfy the input criteria scope. (Schema format is not applicable in input)
            
    """
    def __init__(self, ) -> None: ...
    PropertySetObjects: list[Teamcenter.Soa.Client.Model.Strong.PropertySet]
    """A list of property set objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class GetTransferModesResponse:
    """
    
            The GetTransferModesResponse structure defines
            the response from getTransferModes operation.
            It contains vector of transfer mode object references that were created on the server
            that satisfy the input criteria scope and schema format.
            
    """
    def __init__(self, ) -> None: ...
    TransferModeObjects: list[Teamcenter.Soa.Client.Model.Strong.TransferMode]
    """A list of transfer mode objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class NamesAndValue:
    """
    NameAndValue structure represents a generic name-value pair
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the name-value pair"""
    Value: str
    """The value of the name-value pair"""

class OptionInputData:
    """
    
            Transfer Option Set is a the object which holds complete configuration information
            about the data transfer. It is basically collection of options. Options are grouped
            in UI to give better readability for the options The options will be grouped in GUI
            based on the group name. The default values will be true or false for 2007.1. If
            the readOnlyFlag is set on a particular option only "dba" can override the value
            during transfer. it will be shown to the regular user but read-only  The OptionInputData
            structure defines complete data for one option (Symbol)
            
    """
    def __init__(self, ) -> None: ...
    RealName: str
    """The real variable name that used in code."""
    DisplayName: str
    """Specify the name that user see in the transfer option setting ."""
    Description: str
    """The description for the transfer option."""
    GroupName: str
    """The group that the tranfer option belongs to in the whole transfer option set."""
    DefaultValue: str
    """The default value for this transfer option."""
    ReadOnlyFlag: bool
    """
            Specify that wheter this transfer option is modified in transfer option setting.
            If the value is true, this option will be unmodifiable in the transfer option setting.
            """

class RequestImportFromOfflinePackageResponse:
    """
    
            RequestImportFromOfflinePackageResponse structure defines the response from requestImportFromOfflinePackage
            operation. It contains message Id of the request and partial errors and objects that
            are imported.
            
    """
    def __init__(self, ) -> None: ...
    MsgId: str
    """
            Message Id of this request, to be used to check the status import seesion run at
            Global Service.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors listed above in case of failure conditions.
            """

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateActionRules(self, Inputs: list[CreateOrUpdateActionRuleInputData]) -> CreateOrUpdateActionRuleResponse:
        """    
             Creates or updates an action rule based on input parameters. Action rule in the PLM
             XML framework is used to invoke additional actions before/during/after import/export.
             For more information on action rules, please refer to PLM XML Import Export Administration
             Guide.
             

Use Cases:

             Use Case 1: Modify an Action Rule

             The following types of modifications can be done on existing action rule using createOrUpdateActionRules operation:
             

Change the rule description.
             
Change the action handler. This means that we can change the action
             rule's clause to invoke a different action than what was initially assigned.
             
Change the action location. This means we can change action location
             from pre-action to post-action etc.
             
Change the schema format. This means we can change the action rule
             from PLM XML schema based one to TC XML schema.
             
Change data transfer direction scope. This means we can change the
             direction from export to import and vice-versa.
             



Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Vector containing data for creation or modification of action rule.
             
        :return: 203413Â Â Â Â If the operation fails to modify the given action rule.
        """
        ...
    def CreateOrUpdateClosureRules(self, Inputs: list[CreateOrUpdateClosureRuleInputData]) -> CreateOrUpdateClosureRuleResponse:
        """    
             Creates or updates a closure rule based on input parameters. Closure rule specify
             how the data structure is traversed by specifying which relationships are of interest
             and what should be done when these relationships are encountered. For more information,
             please refer to PLM XML Import Export Administration Guide.
             

Use Cases:

             Use Case 1: Modify a Closure Rule

             The following types of modifications can be done on existing closure rule using createOrUpdateClosureRules operation:
             

Change the closure rule description.
             
Change schema format. This means we can change the closure rule from
             PLM XML schema based one to TC XML schema.
             
Change transfer direction. This means we can change the direction
             from export to import and vice-versa.
             
Change clause contents, depth and comments for each clause. You can
             change detailed clauses in this closure rule. For more information to how to write
             clauses, please refer to PLM XML Import Export Administration Guide.
             



Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Vector containing data for creation or modification of closure rule.
             
        :return: 203411Â Â Â Â If the operation fails to modify closure rule.
        """
        ...
    def CreateOrUpdateFilterRules(self, Inputs: list[CreateOrUpdateFilterRuleInputData]) -> CreateOrUpdateFilterRuleResponse:
        """    
             Creates or updates a filter rule based on input parameters. Filter rules allow a
             finer level of control over the data that gets translated along with the primary
             objects by specifying that a user-written function is called to determine the operation
             applied against a given object. For more information, please refer to PLM XML Import
             Export Administration Guide.
             

Use Cases:

             Use Case 1: Modify a Filter Rule

             The following types of modifications can be done on existing filter rule using createOrUpdateFilterRules operation:
             

Change the filter rule description.
             
Change clauses. For more information about how to write clause, please
             refer to PLM XML Import Export Administration Guide.
             
Change schema format. This means we can change the filter rule from
             PLM XML schema based one to TC XML schema.
             
Change data transfer direction scope. This means we can change the
             direction from export to import and vice-versa.
             



Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Vector containing data for creation or modification of filter rule.
             
        :return: 203416Â Â Â Â If the operation fails to modify filter rule.
        """
        ...
    def CreateOrUpdatePropertySets(self, Inputs: list[CreateOrUpdatePropertySetInputData]) -> CreateOrUpdatePropertySetRuleResponse:
        """    
             Creates or updates a property set based on input parameters. Property sets provide
             a non-programmatic way to control what is placed in the UserData element.
             For more information, please refer to PLM XML Import Export Administration Guide.
             

Use Cases:

             Use Case 1: Modify a Property Set

             The following types of modifications can be done on existing property set using createOrUpdatePropertySets operation:
             

Change the property set description.
             
Change data transfer direction scope. This means we can change the
             direction from export to import and vice-versa.
             
Change clauses. For more information about how to write clause, please
             refer to PLM XML Import Export Administration Guide.
             



Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Vector containing data for creation or modification of property set.
             
        :return: 203417Â Â Â Â If the operation fails to modify property set.
        """
        ...
    def CreateOrUpdateTransferModes(self, Inputs: list[CreateOrUpdateTransferModeInputData]) -> CreateOrUpdateTransferModeResponse:
        """    
             Creates or updates a transfer mode based on input parameters. Transfer modes are
             created in the PLMXML application. Transfer modes define how to import/export data
             between PLMXML file and sites. For more information, please refer to PLM XML Import
             Export Administration Guide.
             

Use Cases:

             Use Case 1: Modify a Transfer Mode

             The following types of modifications can be done on existing transfer mode using
             createOrUpdateTransferModes operation.
             

Change the transfer mode description
             
Change context string. Context string is used to map the transfer
             mode object to a customized processor for the given object type. For more information,
             please refer to PLM XML Import Export Administration Guide.
             
Change data transfer direction scope. This means we can change the
             direction from export to import and vice-versa.
             
Change schema format. This means we can change the closure rule from
             PLM XML schema based one to TC XML schema.
             
Change Incremental setting.  This option allows updates to existing
             data during PLM XML import. For example, if an item being imported from an .xml file
             already exists in the database and "support incremental" is selected, the PLM XML
             import updates the item. If "support incremental" is not selected, the updates from
             the .xml file are ignored.
             
Change closure rule, filter rule, property set, revision rule and
             action rule which are used by this transfer mode.
             



Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Vector containing data for creation or modification of transfer mode.
             
        :return: 203410Â Â Â Â If the operation fails to modify transfer mode.
        """
        ...
    def CreateOrUpdateTransferOptionSets(self, Inputs: list[CreateOrUpdateTransferOptionSetInputData]) -> CreateOrUpdateTransferOptionSetResponse:
        """    
             Creates or update a list of transfer option sets based on the input properties structure.
             The transfer option set contains a set of variables which will control the export/import
             behavior. For more information, please refer to PLM XML Import Export Administration
             Guide.
             

Use Cases:

             Use Case 1: Modify a Transfer Option Set

             The following types of modifications can be done on existing transfer option set
             using createOrUpdateTransferOptionSets operation:
             

Change the transfer option set description
             
Change referenced site id. It shows whether the transfer option set
             is for a remote site, thus an import. If so, its remote site ID is included.
             
Change the attached transfer mode id.
             
Change the detail options for the transfer option set. For more information
             to the options, please refer to PLM XML Import Export Administration Guide.
             



Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Vector containing data for creation or modification of transfer option set.
             
        :return: 1. A List of created or modified transfer option set objects 2. Failure will be returned
             via the ServiceData. For details please refer to ServiceException Description.
        """
        ...
    def GetActionRules(self, Inputs: GetPLMXMLRuleInputData) -> GetActionRulesResponse:
        """    
             This operation return a set of action rule objects depending upon input query parameters.
             

Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Data that contains info to query action rule objects from the database.
             
        :return: 1. A List of action rule objects 2. Failure will be returned via the ServiceData.
             For details please refer to ServiceException Description.
        """
        ...
    def GetAllTransferOptionSets(self) -> GetAllTransferOptionSetsResponse:
        """    
             This operation return a set of transfer option set objects that were created with
             scope - public.
             

Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :return: 
        """
        ...
    def GetAvailableTransferOptionSets(self, Inputs: GetAvailableTransferOptionSetsInputData) -> GetAvailableTransferOptionSetsResponse:
        """    
             This operation return a set of transfer option set object depending upon input query
             parameters.
             

Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Data that contains info to query transfer option set from the database.
             
        :return: 203409Â Â Â Â If the query  fails to get any transfer option set.
        """
        ...
    def GetClosureRules(self, Inputs: GetPLMXMLRuleInputData) -> GetClosureRulesResponse:
        """    
             This operation return a set of closure rule objects depending upon input query parameters.
             

Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Data that contains info to query closure rule objects from the database.
             
        :return: 203425Â Â Â Â If the query cannot find closure rules.
        """
        ...
    def GetFilterRules(self, Inputs: GetPLMXMLRuleInputData) -> GetFilterRulesResponse:
        """    
             This operation return a set of filter rule objects depending upon input query parameters.
             

Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Data that contains info to query filter rule objects from the database.
             
        :return: 203423Â Â Â Â If the query cannot find filter rules.
        """
        ...
    def GetPropertySets(self, Inputs: GetPLMXMLRuleInputData) -> GetPropertySetsResponse:
        """    
             This operation return a set of property set objects depending upon input query parameters.
             

Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Data that contains info to query property set objects from the database.
             
        :return: 203422Â Â Â Â If the query cannot find property sets.
        """
        ...
    def GetTransferModes(self, Inputs: GetPLMXMLRuleInputData) -> GetTransferModesResponse:
        """    
             This operation returns a set of transfer mode objects depending upon input query
             parameters.
             

Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param Inputs: 
                         Data that contains info to query transfer mode objects from the database.
             
        :return: 203422Â Â Â Â If the query cannot find transfer mode.
        """
        ...
    def RequestImportFromOfflinePackage(self, FmsTicket: str, OptionSetTag: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet, OptionNamesAndValues: list[NamesAndValue], SessionOptionAndValues: list[NamesAndValue]) -> RequestImportFromOfflinePackageResponse:
        """    
             This operation imports the contents of the briefcase container into database by placing
             a request to the Global Services (GS) components. This operation is very much similar
             to importObjectsFromOfflinePackage with the exception that this operation
             is used in GS enabled environment whereas importObjectsFromOfflinePackage
             operation is used in Non GS environment. A packed briefcase contains a TC XML file
             which holds a serious of Teamcenter objects and related physical dataset files. After
             import, those objects will be replica in the importing site.
             

Use Cases:

             In data exchange, user may transfer a briefcase file from the source site to a remote
             site. In the importing site, user can use this operation to import the briefcase
             file into the Teamcenter. After import, the objects held in the TC XML file will
             be created or updated if they have been imported before, physical dataset files will
             uploaded and attached to the related datasets.
             
             The SOA needs the GS (Global Service) been configured for the importing site.
             

Teamcenter Component:

             Briefcase - Offline GMS capabilitiy tailored to support the disconnected supplier
             use case for data transfer and synchronization.
             
        :param FmsTicket: 
                         The FMS file ticket for the briefcase file, the file should be uploaded to the server
                         before calling this operation.
             
        :param OptionSetTag: 
                         A reference to the <b>TransferOptionSet</b> object, this object holds the list of
                         options and their default values which can influence importing briefcase.
             
        :param OptionNamesAndValues: 

        :param SessionOptionAndValues: 

        :return: 
        """
        ...

