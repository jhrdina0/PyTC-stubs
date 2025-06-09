import System
import System.Collections
import Teamcenter.Services.Strong.Multisite._2007_06.ImportExport
import Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML
import Teamcenter.Services.Strong.Multisite._2019_06.ImportExportTCXML
import Teamcenter.Services.Strong.Multisite._2019_06.Search
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class ImportExportRestBindingStub(ImportExportService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def RemoteImport(self, Infos: list[Teamcenter.Services.Strong.Multisite._2007_06.ImportExport.RemoteImportInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RegisterItemId(self, ItemInfo: list[Teamcenter.Soa.Client.Model.Strong.Item]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnregisterItemId(self, ItemInfo: list[Teamcenter.Soa.Client.Model.Strong.Item]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class ImportExportService:
    """
    
            The ImportExport service provides operations
            to share the data within the sites in the Multi-Site federation.
Data sharing is
            achieved using the data replication, through import and export
operations. These
            are the foundation of Multi-Site Collaboration. Using this service
the participating
            sites in a Multi-Site federation get a reliable way of importing the
data from the
            rest of the site(s).

            This service also provides the operation to maintain the item id
uniqueness in the
            Multi-Site federation. In a Multi-Site federation item id uniqueness
is maintained
            using the central item id registry. This service provides the
operation for registering
            and unregistering item ids to and from the central item id registry.

Library Reference:

TcSoaMultisiteStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ImportExportService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def RemoteImport(self, Infos: list[Teamcenter.Services.Strong.Multisite._2007_06.ImportExport.RemoteImportInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The remoteImport operation is used to import
             given business objects from the target site to the source site. The import options
             supplied in the RemoteImportInfo structure
             influences the business object import.
             

             E.g. In case user supplies Include All revision
             as TRUE, from target site, source site will import all versions of the dataset.
             

             When option(s) are not specified in the RemoteImportInfo structure, by default user
             session preferences at the importing site are considered for import.  Default values
             are mentioned under the RIAttributeInfo structure.
             



Use Cases:


In the Multi-Site federation user can share the business objects
             among the participating sites, the client shares business object(s) using the remote
             import or remote export functionality. Incase of the remote import the source site
             need to publish the item to the object directory services.
             
To remote import the business object, first the source site user
             creates an Item and publishes it to the default ODS. The target site user performs
             remote search with the item id and imports it to the target site using the remote
             import operation. On successful completion of remote import operation, the item is
             imported to the target site database.
             
Also remote import of business objects can be achieved using the
             command line utility data_share f=remote_import.
             



Teamcenter Component:

             Import/Export - Import / export of Tc data model in a binary format that CMS uses.
             
        :param Infos: 

        :return: 
        """
        ...
    def RegisterItemId(self, ItemInfo: list[Teamcenter.Soa.Client.Model.Strong.Item]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The registerItemId operation is used to register
             the list of items at the central item registry.  The central registry holds all item
             ids from the Multi-Site federation. The item ID could be manually registered using
             Rich client, Command line utility data_share OR using this operation.
             

             Usage of this operation is influenced by the following preferences.
             

             The preference ITEM_id_registry activates/deactivates the central item registry.
             If the preference value is set to TRUE, during item creation, the system checks
             the item registry for duplicates. Creating the item fails if a duplicate is found.
             Setting ITEM_id_Registry to FALSE would make Item registry disabled. Thus,
             while creating a new item, the item registry is not checked for duplicates.
             

             The preference ITEM_id_registry_site identifies the site name at which the
             central item registry server is running. This must be set, if the preference ITEM_id_registry
             is set to TRUE and will be ignored otherwise.
             

             The preference ITEM_id_allow_if_registry_down determines if items can be created,
             if the registry server is not available. If the registry is not active (ITEM_id_registry
             = FALSE), this preference is ignored.
             

             The preference ITEM_id_always_register_on_creation determines if item IDs
             are automatically registered when items are created or the item ID is changed.
             

Use Cases:


Admin user(s) set the ITEM_id_always_register_on_creation
             to TRUE on all sites within a Multi-Site federation. On item creation the items created
             automatically registers with the central item registry.
             
Admin user(s) can register existing item(s) with the central item
             registry, using Register Item Id command in the Rich Client(RAC) or
             command line utility data_share f=register




Teamcenter Component:

             Import/Export - Import / export of Tc data model in a binary format that CMS uses.
             
        :param ItemInfo: 
                         List of Teamcenter <b>Item</b> which need to be registered with the central item
                         ID registry. These are the business objects of Class <b>Item</b> created in Teamcenter.
             
        :return: 
        """
        ...
    def UnregisterItemId(self, ItemInfo: list[Teamcenter.Soa.Client.Model.Strong.Item]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The central registry holds all item ids from the multisite federation. To unregister
             the item id(s), this operation is used, this unregisters supplied items from the
             central item registry. The item ID could be manually unregistered using Rich client,
             Command line utility data_share OR using this operation.
             

             The preference ITEM_id_registry activates/deactivates the central item registry.
             If the preference value set to TRUE, during item creation, the system checks the
             item registry for duplicates. Creating the item fails if a duplicate is found. Setting
             ITEM_id_Registry to FALSE would make item registry disabled. So while creating
             a new item, the item registry is not checked for duplicates.
             

             The preference ITEM_id_registry_site identifies the site name at which the
             central item registry server is running. This must be set, if the preference ITEM_id_registry
             is set to TRUE and will be ignored otherwise.
             

             The preference ITEM_id_unregister_on_delete determines if item Ids are automatically
             unregistered when items are deleted or the item ID is changed.
             



Use Cases:


Admin user(s) can unregister existing item(s) from the central item
             registry, using Unregister Item Id command in the Rich Client (RAC)
             or command line utility data_share f=unregister.
             



Teamcenter Component:

             Import/Export - Import / export of Tc data model in a binary format that CMS uses.
             
        :param ItemInfo: 
                         List of items which needs to be unregistered with the central item id registry. These
                         are the business objects of Class <b>Item</b> created in Teamcenter.
             
        :return: 
        """
        ...

class ImportExportTCXMLRestBindingStub(ImportExportTCXMLService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def RemoteExport(self, Rinfos: list[Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteExportInfo]) -> Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteExportResponse: ...
    def RemoteImport(self, Rinfos: list[Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteImportInfo]) -> Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteImportResponse: ...
    def RemoteImportByUID(self, Rinfos: list[Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteImportUIDInfo]) -> Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteImportResponse: ...
    def RemoteCheckin(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSetName: str, SessionOptions: System.Collections.Hashtable, OverrideOptions: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Multisite._2019_06.ImportExportTCXML.RemoteCheckinResponse: ...
    def RemoteCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSetName: str, SessionOptions: System.Collections.Hashtable, OverrideOptions: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Multisite._2019_06.ImportExportTCXML.RemoteCheckoutResponse: ...

class ImportExportTCXMLService:
    """
    
            The ImportExportTCXML service provides operations to share the data
within the sites
            in the Multi-Site federation. Data sharing is achieved using the
data replication,
            through import and export operations. These are the foundation of
Multi-Site Collaboration.
            Using this service the participating sites in a Multi-Site
federation get a reliable
            way of importing the data from the rest of the site(s).

Library Reference:

TcSoaMultisiteStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ImportExportTCXMLService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def RemoteExport(self, Rinfos: list[Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteExportInfo]) -> Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteExportResponse:
        """    
             This operation exports targeted objects from the local site to the target sites using
             the Multi-Site TCXML payload. The target objects are specified in the RemoteExportInfo
             structure. The options also specified in this structure affect the final state of
             the exported objects at the target sites. The objects must be owned at the local
             site.
             

Use Cases:

             In the Multi-Site federation user can share the business objects among the participating
             sites, the client shares business object(s) using the remote import or remote export
             functionality. This operation supports the following use case.
             
             The remote export (i.e. push) of business objects owned at the local site to the
             target site. The business object will exist at the target site either a replica or
             local object depending on options at the conclusion of the operation.
             

Teamcenter Component:

             Classic Multi-Site - Technology to replicate data across multiple instances of Tc.
             It allows for transfering the ownership of objects across different instance and
             tools to export and synchronize data.
             
        :param Rinfos: 
                         A list   objects along with information related to the export operation.
             
        :return: 95023Â Â Â Â  Multisite TIE import failures reported by some remote
             sites, please find details in the syslog.
        """
        ...
    def RemoteImport(self, Rinfos: list[Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteImportInfo]) -> Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteImportResponse:
        """    
             The remoteImport operation imports targeted objects from their source site to the
             local site using the Multi-Site TCXML payload. The inputs include various options
             which will affect the final state of the Business Objects at the local site.
             

Use Cases:

             In the Multi-Site federation user can share the business objects among the participating
             sites, the client shares business object(s) using the remote import or remote export
             functionality. This operation supports the following use case.
             
             The remote import (i.e. pull) of business objects owned at the target site to the
             local site. The business object will exist at the local site as either a replica
             or local object depending on options at the conclusion of the operation. They will
             be updated if they already exist in the local site.
             

Teamcenter Component:

             Classic Multi-Site - Technology to replicate data across multiple instances of Tc.
             It allows for transfering the ownership of objects across different instance and
             tools to export and synchronize data.
             
        :param Rinfos: 
                         A list of objects along with information related to the import operation.
             
        :return: 
        """
        ...
    def RemoteImportByUID(self, Rinfos: list[Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteImportUIDInfo]) -> Teamcenter.Services.Strong.Multisite._2014_10.ImportExportTCXML.RemoteImportResponse:
        """    
             The remoteImport operation imports targeted objects from their source site to the
             local site using the Multi-Site TCXML payload. The inputs include various options
             which will affect the final state of the Business Objects at the local site.
             

Use Cases:

             In the Multi-Site federation user can share the business objects among the participating
             sites, the client shares business object(s) using the remote import or remote export
             functionality. This operation supports the following use case.
             
             The remote import (i.e. pull) of business objects owned at the target site to the
             local site. The business object will exist at the local site as either a replica
             or local object depending on options at the conclusion of the operation. They will
             be updated if they already exist in the local site.
             


Teamcenter Component:

             Classic Multi-Site - Technology to replicate data across multiple instances of Tc.
             It allows for transfering the ownership of objects across different instance and
             tools to export and synchronize data.
             
        :param Rinfos: 
                         A list of objects along with information related to the import operation.
             
        :return: 
        """
        ...
    def RemoteCheckin(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSetName: str, SessionOptions: System.Collections.Hashtable, OverrideOptions: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Multisite._2019_06.ImportExportTCXML.RemoteCheckinResponse: ...
    def RemoteCheckout(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSetName: str, SessionOptions: System.Collections.Hashtable, OverrideOptions: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Multisite._2019_06.ImportExportTCXML.RemoteCheckoutResponse:
        """    
             The RemoteCheckout operation applies the Multi-Site check out operation to the business
             objects in the objects parameter.
             

Use Cases:

             In the Multi-Site federation, a user can share the business objects among the participating
             sites, the client shares business object(s) using the remote import or remote export
             functionality. This allows the creation of replica objects which are read-only copies
             of the master object. Multi-site supports a Remote Check-in Check-out feature which
             allows edits to replica objects. This operation supports the following use case.
             


The remote check out of replica business objects.  This allows edits
             to the replica objects. These changes are later saved to the owning site with the
             remote check in operation.
             



Teamcenter Component:

             Classic Multi-Site - Technology to replicate data across multiple instances of Tc.
             It allows for transfering the ownership of objects across different instance and
             tools to export and synchronize data.
             
        :param Objects: 
                         A list of replica <b>WorkspaceObject</b> class business objects.
             
        :param OptionSetName: 
                         The name of <b>TransferOptionSet</b> used for check out. The default option set is
                         used if not supplied.
             
        :param SessionOptions: 
                         checkOutDependentObject: Checks out additional dependent objects defined by the <b>TransferOptionSet</b>
                         if True. The default is False.
             
        :param OverrideOptions: 
                         A map (string, list of strings) of overrides to <b>TransferOptionSet</b>  specified
                         in optionSetName. The overrides available are specific to the <b>TransferOptionSet</b>.
                         The available <b>TransferOptionSet</b> overrides can be viewed in the PLMXML/TCXML
                         Export Import Administration application.
             
        :return: 
        """
        ...

class SearchRestBindingStub(SearchService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def Publish(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], TargetSites: list[str], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Multisite._2019_06.Search.SearchResponse: ...
    def Unpublish(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], TargetSites: list[str], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Multisite._2019_06.Search.SearchResponse: ...

class SearchService:
    """
    
            The Search service provides operations pertaining to data published
to Object Directory
            Services (ODS) at sites within a Multi-Site federation. This data
can subsequently
            be used to import data from one site to another.

Library Reference:

TcSoaMultisiteStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SearchService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def Publish(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], TargetSites: list[str], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Multisite._2019_06.Search.SearchResponse: ...
    def Unpublish(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], TargetSites: list[str], Options: System.Collections.Hashtable) -> Teamcenter.Services.Strong.Multisite._2019_06.Search.SearchResponse: ...

