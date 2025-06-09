import System
import Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport
import Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport
import Teamcenter.Services.Strong.Globalmultisite._2008_06.ImportExport
import Teamcenter.Services.Strong.Globalmultisite._2010_04.ImportExport
import Teamcenter.Services.Strong.Globalmultisite._2011_06.ImportExport
import Teamcenter.Services.Strong.Globalmultisite._2020_04.ImportExport
import Teamcenter.Services.Strong.Globalmultisite._2021_06.ImportExport
import Teamcenter.Services.Strong.Globalmultisite._2022_06.ImportExport
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class ImportExportRestBindingStub(ImportExportService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateActionRules(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateActionRuleInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateActionRuleResponse: ...
    def CreateOrUpdateClosureRules(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateClosureRuleInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateClosureRuleResponse: ...
    def CreateOrUpdateFilterRules(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateFilterRuleInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateFilterRuleResponse: ...
    def CreateOrUpdatePropertySets(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdatePropertySetInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdatePropertySetRuleResponse: ...
    def CreateOrUpdateTransferModes(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateTransferModeInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateTransferModeResponse: ...
    def CreateOrUpdateTransferOptionSets(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateTransferOptionSetInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateTransferOptionSetResponse: ...
    def GetActionRules(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetActionRulesResponse: ...
    def GetAllTransferOptionSets(self) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetAllTransferOptionSetsResponse: ...
    def GetAvailableTransferOptionSets(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetAvailableTransferOptionSetsInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetAvailableTransferOptionSetsResponse: ...
    def GetClosureRules(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetClosureRulesResponse: ...
    def GetFilterRules(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetFilterRulesResponse: ...
    def GetPropertySets(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPropertySetsResponse: ...
    def GetTransferModes(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetTransferModesResponse: ...
    def RequestImportFromOfflinePackage(self, FmsTicket: str, OptionSetTag: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue], SessionOptionAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.RequestImportFromOfflinePackageResponse: ...
    def GetRemoteSites(self, SiteType: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RequestExportToRemoteSites(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNameAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues], SessionOptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.CallToRemoteSiteResponse: ...
    def RequestImportFromRemoteSites(self, Reason: str, OwningSitesAndObjs: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.OwningSiteAndObjs], OptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues], SessionOptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.CallToRemoteSiteResponse: ...
    def ExportObjectsToOfflinePackage(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSetTag: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue], SessionOptionAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2008_06.ImportExport.ExportObjectsToOfflinePackageResponse: ...
    def ImportObjectsFromOfflinePackage(self, FmsTicket: str, OptionSetTag: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue], SessionOptionAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2008_06.ImportExport.ImportObjectsFromOfflinePackageResponse: ...
    def ExportObjectsToPLMXML(self, ExportObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, Languages: list[str], XmlFileName: str, SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2010_04.ImportExport.ExportObjectsToPLMXMLResponse: ...
    def ImportObjectsFromPLMXML(self, XmlFileTicket: str, NamedRefFileTickets: list[str], Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode, IcRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2010_04.ImportExport.ImportObjectsFromPLMXMLResponse: ...
    def CreateGSIdentities(self, GsIdVect: list[Teamcenter.Services.Strong.Globalmultisite._2011_06.ImportExport.TIEGSIdentityInput]) -> Teamcenter.Services.Strong.Globalmultisite._2011_06.ImportExport.CreateGSIdentitiesResponse: ...
    def GetHashedUID(self, OwnSiteId: int, HashKey: str) -> Teamcenter.Services.Strong.Globalmultisite._2011_06.ImportExport.GetHashedUIDResponse: ...
    def ImportObjectsFromPLMXMLWithDSM(self, XmlFileTicket: str, NamedRefFolderPath: str, Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode, IcRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2020_04.ImportExport.ImportObjectsFromPLMXMLWithDSMResp: ...
    def ExportFilesOffline(self, Uids: list[str], Options: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2021_06.ImportExport.ExportFilesOfflineResponse: ...
    def ImportNXFiles(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2021_06.ImportExport.ImportNXFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ExportFilesOffline2(self, Input: list[Teamcenter.Services.Strong.Globalmultisite._2022_06.ImportExport.ExportFilesOfflineInput], Options: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2021_06.ImportExport.ExportFilesOfflineResponse: ...

class ImportExportService:
    """
    
            The ImportExport service exposes operations that are used to execute PLMXML import
            and export operations along with create, update and delete operations of related
            objects such as transfer mode, filter rule, action rule, closure rule, property set
            and transfer option set.
            

            This service provides following import export use case for the specified Teamcenter
            objects or PLMXML administration object.
            


Creation or update transfer modes, closure rules, filter rules, property
            sets...
            
Import xml file to Teamcenter.
            
Export Teamcenter objects to xml file.
            




Library Reference:

TcSoaGlobalMultiSiteStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ImportExportService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateActionRules(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateActionRuleInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateActionRuleResponse:
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
    def CreateOrUpdateClosureRules(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateClosureRuleInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateClosureRuleResponse:
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
    def CreateOrUpdateFilterRules(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateFilterRuleInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateFilterRuleResponse:
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
    def CreateOrUpdatePropertySets(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdatePropertySetInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdatePropertySetRuleResponse:
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
    def CreateOrUpdateTransferModes(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateTransferModeInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateTransferModeResponse:
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
    def CreateOrUpdateTransferOptionSets(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateTransferOptionSetInputData]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.CreateOrUpdateTransferOptionSetResponse:
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
    def GetActionRules(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetActionRulesResponse:
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
    def GetAllTransferOptionSets(self) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetAllTransferOptionSetsResponse:
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
    def GetAvailableTransferOptionSets(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetAvailableTransferOptionSetsInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetAvailableTransferOptionSetsResponse:
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
    def GetClosureRules(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetClosureRulesResponse:
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
    def GetFilterRules(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetFilterRulesResponse:
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
    def GetPropertySets(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPropertySetsResponse:
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
    def GetTransferModes(self, Inputs: Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetPLMXMLRuleInputData) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.GetTransferModesResponse:
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
    def RequestImportFromOfflinePackage(self, FmsTicket: str, OptionSetTag: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue], SessionOptionAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.RequestImportFromOfflinePackageResponse:
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
    def GetRemoteSites(self, SiteType: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation returns a list of sites registered for the requested type of transfer.
             

Teamcenter Component:

             TcXMLimportexportengine - Capability to import and export XML that follows the TC
             Business Object Model. No hardcoded transformation is done. Transformations when
             needed are supported by the mapper component
             
        :param SiteType: 
<ul>
<li type="disc"> Offline       GMS Sites participating in briefcase transfer
                         </li>
</ul>

        :return: List of sites of particular type is returned in the plain list of the ServiceData.
        """
        ...
    def RequestExportToRemoteSites(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNameAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues], SessionOptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.CallToRemoteSiteResponse:
        """    
             This operation exports objects to specified sites using Global Multisite.
             

Use Cases:

             This operation gets invoked from RAC when user does following actions from Navigator
             or structure manager
             
             1>    Tools->Export->To Remote Site Via Global Services.
             
             2>    Tools->Export->To PDX
             
             3>    Tools->Export->To Briefcase
             


Teamcenter Component:

             TcXMLimportexportengine - Capability to import and export XML that follows the TC
             Business Object Model. No hardcoded transformation is done. Transformations when
             needed are supported by the mapper component
             
        :param Reason: 
                         The reason for remote export. This has limit of 240.
             
        :param Sites: 
                         A list of sites to which object(s) need to be exported.
             
        :param Objects: 
                         Objects to be exported
             
        :param OptionSet: 
                         A reference to <b>TransferOptionSet</b> object which is selected by the user. This
                         object holds the list of options and their default values which can influence the
                         contents of the exported briefcase or PDX or on-line export.
             
        :param OptionNameAndValues: 
                         This is the list of options and values that user has overridden from the <b>TransferOptionSet</b>
                         object specified above. E.g option name 'opt_all_ds_files' (Export all dataset files)
                         has default value as True in Transfer option set. If use does not want to export
                         all dataset he can override it to false.
             
        :param SessionOptionNamesAndValues: 
                         This is the list of session options and values (options which are not part of the
                         option set). E.g 1) If user wants to run export in dry run mode then session option
                         'dry_run' needs to be specified and its value should be 'True'. 2)If user wants to
                         export unconfigured variants then 'processUnconfiguredVariants' should be set to
                         'True'.
             
        :return: 
        """
        ...
    def RequestImportFromRemoteSites(self, Reason: str, OwningSitesAndObjs: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.OwningSiteAndObjs], OptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues], SessionOptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.CallToRemoteSiteResponse:
        """    
             This operation imports objects to specified sites using Global Multisite.
             

Use Cases:

             This operation is not in use.
             

Teamcenter Component:

             TcXMLimportexportengine - Capability to import and export XML that follows the TC
             Business Object Model. No hardcoded transformation is done. Transformations when
             needed are supported by the mapper component
             
        :param Reason: 
                         The reason of Import. This has limit of 240 characters.
             
        :param OwningSitesAndObjs: 
                         A list of owning site and corresponding objects that need to be imported.
             
        :param OptionSet: 
                         A reference to <b>TransferOptionSet</b> object which is selected by the user. This
                         object holds the list of options and their default values which can influence the
                         result of import.
             
        :param OptionNamesAndValues: 
                         This is the list of options and values that user has overridden from the <b>TransferOptionSet</b>
                         object specified above.
             
        :param SessionOptionNamesAndValues: 
                         This is the list of session options and values (options which are not part of the
                         option set).
             
        :return: 
        """
        ...
    def ExportObjectsToOfflinePackage(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSetTag: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue], SessionOptionAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2008_06.ImportExport.ExportObjectsToOfflinePackageResponse:
        """    
             Exports the objects to an offline package called briefcase. This operation returns
             a structure which includes the briefcase's FMS file ticket and exporter log file's
             FMS ticket. The briefcase ticket is used for downloading the briefcase file from
             the server to the client side by using FMS utility. Exporter log ticket is used for
             downloading the exporter log.
             
             The briefcase is a package contains an exported TC XML file and a set of physical
             dataset files. The TC XML file holds the exported objects traversed by TC XML Export
             framework with the input TransferOptionSet and options, session options.
             
             Exporter log include the exporting status of the related objects.
             


Use Cases:

             User can set a list of root objects, a destination site, a transfer option set, a
             list of traverse options and a list of session options. All the objects which can
             be traversed by the option set and options will be exported into an output TC XML
             file. The physical Iman files related exported dataset objects will be downloaded
             and packed into the briefcase file along with the TC XML file.
             

Teamcenter Component:

             Briefcase - Offline GMS capabilitiy tailored to support the disconnected supplier
             use case for data transfer and synchronization.
             
        :param Reason: 
                         The reason for the export, the size is limited to 240 characters.
             
        :param Sites: 
                         The destination sites, only one site is supported as of now. The site should be marked
                         as offline in Organization application to perform a Briefcase export.
             
        :param Objects: 
                         List of root objects to be exported.
             
        :param OptionSetTag: 
                         A reference to the <b>TransferOptionSet</b> object, this object holds the list of
                         options and their default values which can influence the contents of the exported
                         briefcase.
             
        :param OptionNamesAndValues: 

        :param SessionOptionAndValues: 

        :return: 
        """
        ...
    def ImportObjectsFromOfflinePackage(self, FmsTicket: str, OptionSetTag: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue], SessionOptionAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2008_06.ImportExport.ImportObjectsFromOfflinePackageResponse:
        """    
             This operation imports the data of a briefcase into Teamcenter. A packed briefcase
             contains a TC XML file which holds a number of Teamcenter objects and related physical
             dataset files. After import, those objects will be replica in the importing site.
             

Use Cases:

             In data exchange, user may transfer a briefcase file from the source site to a remote
             site. In the importing site, user can use this operation to import the briefcase
             file into Teamcenter. After import, the objects held in the TC XML file will be created
             or updated if they have been imported before, physical dataset files will uploaded
             and attached to the related datasets.
             

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
    def ExportObjectsToPLMXML(self, ExportObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, Languages: list[str], XmlFileName: str, SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2010_04.ImportExport.ExportObjectsToPLMXMLResponse:
        """    
             The exportObjectsToPLMXML operation will
             generate a PLMXML file and a export log file for the input object list, transfer
             mode, revision rule and language set.
             

Use Cases:

             Use Case 1: Export object to PLMXML file

             You can export any business object by specify:
             
             1)    The objects that you want to exported.
             
             2)    Transfer mode and revision rule.
             
             3)    Languages that for localization value.
             
             4)    Xml file name.
             
             5)    Session options.
             


Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param ExportObjects: 
                         Objects to be exported.
             
        :param Transfermode: 
                         The transfermode which you want to use to traverse from the objects.
             
        :param RevRule: 
                         Revision Rule that you want to use to traverse bom structure.
             
        :param Languages: 
                         The languages to export with.The language code is used to identify a langauge. It
                         follows the Java locale naming conventions: 2letterlanguage_2LETTERAREA (e.g: en_US,
                         fr_FR, de_DE). The language order will be honored and the site master language will
                         always be included.
             
        :param XmlFileName: 
                         The file name with extension .xml or .plmxml that you want the xml to be exported
                         to. Full path is not allowed.
             
        :param SessionOptions: 
                         The session options to control export behavior as name-value pairs. This is in place
                         for future use to pass additional flags to the PLM XML export which can control the
                         behavior.
             
        :return: with the generated PLMXML file ticket, export log file ticket, dataset named reference
             file tickets if any and soa service data.
        """
        ...
    def ImportObjectsFromPLMXML(self, XmlFileTicket: str, NamedRefFileTickets: list[str], Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode, IcRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2010_04.ImportExport.ImportObjectsFromPLMXMLResponse:
        """    
             The importObjectsFromPLMXML operation will import the objects from a PLMXML file.
             The XML file and the named reference files for datasets should be uploaded to transient
             volume before the calling of this operation. User can use getTransientFileTicketsForUpload
             operation from core.FileManagementService to generate the ticket and then call putFileViaTicket
             operation from soa.client.FileManagementUtility to perform the file upload to transient
             volume.
             

Use Cases:

             Use Case 1: Import PLMXML file to database

             You can import PLMXML file by specify:
             
             1)    The xml file that you want to import.
             
             2)    The related dataset file you want to import.
             
             3)    Transfer mode that you want to traverse to the xml.
             
             4)    The incremental change context.
             
             5)    Session options.
             


Teamcenter Component:

             PLMXML Import/Export - Capability to export and import PLM XML from/to Teamcenter.
             It can transform Teamcenter data to PLM XML model and it can transform PLM XML model
             to Teamcenter business objects using PIE engine and traversal rules.
             
        :param XmlFileTicket: 
                         The FMS file ticket for the input XML file to be imported.
             
        :param NamedRefFileTickets: 
                         The FMS file tickets for dataset named reference files.
             
        :param Transfermode: 
                         The transfer mode used to control the import process.
             
        :param IcRev: 
                         The incremental change context for the import restuls. The ItemRevision is used to
                         represent its sub-calss EngChange.
             
        :param SessionOptions: 
                         The session options to control export behavior as name-value pairs. This is in place
                         for future use to pass additional flags to the PLM XML export which can control the
                         behavior.
             
        :return: with the import log and soa service data.
        """
        ...
    def CreateGSIdentities(self, GsIdVect: list[Teamcenter.Services.Strong.Globalmultisite._2011_06.ImportExport.TIEGSIdentityInput]) -> Teamcenter.Services.Strong.Globalmultisite._2011_06.ImportExport.CreateGSIdentitiesResponse:
        """    
             This operation takes array of GSIdentityInput structure as input and creates GSIdentity
             objects in Teamcenter. This operation allows for creation of GSIdentities in bulk
             which is required for GMS co-existence scenarios following bulk load import of legacy
             data into Teamcenter.Whenever an object is exported from a source site the record
             of each imported object is stored in GSIdentity object,which has some basic information
             of the site that owns the object,the type of the class of imported object and 14
             digit Unique Identifier string (UID) represtening the object.Every imported object
             will have a corresponding entry in GSIdentity object.This entry will be used later
             during a re-import or sychronize operations internally by importer module.
             

Use Cases:

             This operation is used by user to create GSIds for objects imported by bulk loader.It
             creates GSIds for non GSId based TcXML objects.
             


Teamcenter Component:

             TcXMLimportexportengine - Capability to import and export XML that follows the TC
             Business Object Model. No hardcoded transformation is done. Transformations when
             needed are supported by the mapper component
             
        :param GsIdVect: 
                         Input to CreateGSIdentities. The GS identity input structure contains the fields
                         required to create a GS identity object.
             
        :return: A list of GS identity object references.Any failure will be returned as partial errors.
        """
        ...
    def GetHashedUID(self, OwnSiteId: int, HashKey: str) -> Teamcenter.Services.Strong.Globalmultisite._2011_06.ImportExport.GetHashedUIDResponse:
        """    
             This operation takes a hash key as input and generates a valid Teamcenter Unique
             Identifier  a 14 character long unique string UID based on it. For migrating data
             from legacy systems to Teamcenter using bulk load import of TC XML, this operation
             can be used to generate UIDs for legacy objects. The UID is composed by using Fowler
             Noll Vo (FNV) hash algorithm for an arbitrary and unique input string.
             

Use Cases:

             This is used during data migration between legacy system such as Enterpise to Teamcenter
             .
             
             Used by the importer to generate a UID.
             

Teamcenter Component:

             TcXMLimportexportengine - Capability to import and export XML that follows the TC
             Business Object Model. No hardcoded transformation is done. Transformations when
             needed are supported by the mapper component
             
        :param OwnSiteId: 
                         The owning site-id or source site Id
             
        :param HashKey: 
                         The input hash key,arbitary unique input string.
             
        :return: A unique hashed uid generated by taking the hash key and site id as input.Any failure
             will be returned as partial errors.
        """
        ...
    def ImportObjectsFromPLMXMLWithDSM(self, XmlFileTicket: str, NamedRefFolderPath: str, Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode, IcRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> Teamcenter.Services.Strong.Globalmultisite._2020_04.ImportExport.ImportObjectsFromPLMXMLWithDSMResp: ...
    def ExportFilesOffline(self, Uids: list[str], Options: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2021_06.ImportExport.ExportFilesOfflineResponse: ...
    def ImportNXFiles(self, Inputs: list[Teamcenter.Services.Strong.Globalmultisite._2021_06.ImportExport.ImportNXFileInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ExportFilesOffline2(self, Input: list[Teamcenter.Services.Strong.Globalmultisite._2022_06.ImportExport.ExportFilesOfflineInput], Options: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> Teamcenter.Services.Strong.Globalmultisite._2021_06.ImportExport.ExportFilesOfflineResponse: ...

class SiteReservationRestBindingStub(SiteReservationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CancelSiteCheckOut(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SiteCheckIn(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SiteCheckOut(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], SiteId: int, Comment: str, ChangeId: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class SiteReservationService:
    """
    
            This service provides operations to transfer modification privilege for offline use
            cases. It is used for offline GMS using Briefcase as the data exchange mechanism.
            In offline GMS, the ownership cannot be transferred. So only the source site holds
            the objects ownership. This service provides the operations to allow the user to
            modify the data at a remote site.
            
            The SiteReservation service supports the following usecases for modification at remote
            site.
            

Site check out the objects to a remote site.
            
Site check in the objects at the remote site after modification.
            
Cancel site check out if user will not do site check out.
            


            Only these six types and their sub types are supported to be site checked out: Item,
            ItemRevision, Form, Dataset, BOMView, BOMViewRevision.
            When site check out is performed on Item, ItemRevision or Dataset,
            related objects will be site checked out also:
            

ItemÂ Â Â Â Â Â Â Â Â Â Â Â Related
            Master Form(s).
            
ItemRevision  Related Master Form(s).
            
DatasetÂ Â Â Â Â Â Â Â All namedReference
            objects which are WorkspaceObject.
            

            .
            

Dependencies:

            Reservation, ImportExport
            


Library Reference:

TcSoaGlobalMultiSiteStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SiteReservationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CancelSiteCheckOut(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used in offline GMS. It is used to cancel site check out objects
             which has been site checked out to another site and removes the reservation objects.
             If errors occur, they are returned in the ServiceData structure.
             

Use Cases:

             User can pass a list of objects which have been in site checked out status to do
             cancel site check in.
             

Dependencies:

             siteCheckOut
             

Teamcenter Component:

             Briefcase - Offline GMS capabilitiy tailored to support the disconnected supplier
             use case for data transfer and synchronization.
             
        :param Objects: 
<ul>
<li type="disc"><b>Item</b>
</li>
<li type="disc"><b>ItemRevision</b>
</li>
<li type="disc"><b>PSBOMView</b>
</li>
<li type="disc"><b>PSBOMViewRevision</b>
</li>
<li type="disc"><b>Form</b>
</li>
<li type="disc"><b>Dataset</b>
</li>
</ul>

        :return: 
        """
        ...
    def SiteCheckIn(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used in offline GMS. It is used to check in objects that were checked
             out to another site and removes the reservation objects. If errors occur, they are
             returned in the ServiceData structure.
             

Use Cases:

             User can pass a list of objects which have been in site checked out status to do
             site check in. A series of related objects will be site checked in along with the
             input objects Item, ItemRevision or Dataset:
             

Item        Related Master
             Form(s)
             
ItemRevision    Related Master Form(s)
             
Dataset        All namedReference
             objects which are WorkspaceObject




Dependencies:

             siteCheckOut
             

Teamcenter Component:

             Briefcase - Offline GMS capabilitiy tailored to support the disconnected supplier
             use case for data transfer and synchronization.
             
        :param Objects: 
<ul>
<li type="disc"><b>Item</b>
</li>
<li type="disc"><b>ItemRevision</b>
</li>
<li type="disc"><b>PSBOMView</b>
</li>
<li type="disc"><b>PSBOMViewRevision</b>
</li>
<li type="disc"><b>Form</b>
</li>
<li type="disc"><b>Dataset</b>
</li>
</ul>

        :return: 
        """
        ...
    def SiteCheckOut(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], SiteId: int, Comment: str, ChangeId: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used in offline GMS. It is used to checkout objects to another
             site, so that after the objects are imported into that site, they are modifiable.
             If errors occur, they are returned in the ServiceData structure.
             

Use Cases:

             User can pass a list of objects (only these six types and their sub types are supported:
             Item, ItemRevision, Form, Dataset, BOMView, BOMViewRevision)
             to do site check out. A series of related objects will be site checked out along
             with the input objects Item, ItemRevision or Dataset:
             

Item        Related Master
             Form(s)
             
ItemRevision    Related Master Form(s)
             
Dataset        All namedReference
             objects which are WorkspaceObject




Teamcenter Component:

             Briefcase - Offline GMS capabilitiy tailored to support the disconnected supplier
             use case for data transfer and synchronization.
             
        :param Objects: 
<ul>
<li type="disc"><b>Item</b>
</li>
<li type="disc"><b>ItemRevision</b>
</li>
<li type="disc"><b>PSBOMView</b>
</li>
<li type="disc"><b>PSBOMViewRevision</b>
</li>
<li type="disc"><b>Form</b>
</li>
<li type="disc"><b>Dataset</b>
</li>
</ul>

        :param SiteId: 
                         Id of the site that the objects are to be checked out to.
             
        :param Comment: 
                         Check out comment, the reason for the site check out.
             
        :param ChangeId: 
                         The mark for this site check out process.
             
        :return: 
        """
        ...

