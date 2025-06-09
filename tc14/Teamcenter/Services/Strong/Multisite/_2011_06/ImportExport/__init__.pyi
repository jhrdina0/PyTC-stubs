import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
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

