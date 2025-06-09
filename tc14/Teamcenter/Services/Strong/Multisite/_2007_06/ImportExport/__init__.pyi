import System
import Teamcenter.Soa.Client.Model
import typing

class RemoteImportInfo:
    """
    
The RemoteImportInfo holds the business object
and related information meant for remote import.

    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Object for the remote import service"""
    Reason: str
    """
            User input to explain, why the remote import of business object required. Its not
            a mandatory input and user can pass empty string.
            """
    ImportOptions: list[RIAttributeInfo]
    """Import options that influence, how the Business Objects are imported to target site."""

class RIAttributeInfo:
    """
    
The RIAttributeInfo structures holds the
name/value pairs of import option. Value can be single or multiple valued. The
import
options influences the business object export and has default value.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """
            Import option name for remote import.
            
"""
    Value: list[str]
    """Values for remote import option (can be multi-valued strings)."""

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RemoteImport(self, Infos: list[RemoteImportInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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

