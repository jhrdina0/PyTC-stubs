import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class MfgImportFromBriefcaseResponse:
    """
    
MfgImportFromBriefcaseResponse structure defines the response from
importFromBriefcase
operation. It contains FMS ticket of the log file, error file, and partial
errors
and objects that are imported.
    """
    def __init__(self, ) -> None: ...
    LogFileFMSTicket: str
    """
            FMS ticket of the import log file, which can be used to download the import log file
            from server to client.
            """
    ErrorFileFMSTicket: str
    """
            FMS ticket of the import error file, which can be used to download the import error
            file from server to client.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data containing the list of created or modified objects and also the partial
            errors in case of failure conditions.
            """

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportFromBriefcase(self, FmsTicket: str, OptionSetTag: Teamcenter.Soa.Client.Model.ModelObject, OptionNamesAndValues: System.Collections.Hashtable, SessionOptionAndValues: System.Collections.Hashtable) -> MfgImportFromBriefcaseResponse:
        """    
             This operation is applicable specifically for Manufacturing Process Planner MPP application.
             
             This operation performs following operation
             
             Teamcenter::Soa::GlobalMultiSite::_2008_06::ImportExport importObjectsFromOfflinePackage
             
             In addition to this, it supports asynchronous import of briefcase.
             

Use Cases:

Use Case 1: Importing objects from briefcase

             This operation can be used in Manufacturing Process Planner (MPP) application to
             import Briefcase file into Teamcenter. Briefcase file is a zipped file containing
             TC XML and data set files. The TC XML file specifies the object to be imported. The
             import dialog presents various option sets to control the objects during import.
             
             First time import will create the objects and upload the datasets. Subsequent import
             of same object will update it. Importer log is generated and presented after the
             import.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param FmsTicket: 
                         The FMS file ticket for the briefcase file, the file should be uploaded to the server
                         before calling this operation.
             
        :param OptionSetTag: 
                         A reference to the <b>TransferOptionSet</b> object, this object holds the list of
                         options and their default values which can influence importing briefcase.
             
        :param OptionNamesAndValues: 
                         For example: For option opt_imp_XXX  in TransferOptionSet, the default value is false.
                         It can be overridden by adding the option with new value as true.
             
        :param SessionOptionAndValues: 
                         For example: A session option modified_objects_only specifies whether to import modified
                         object.
             
        :return: 
        """
        ...

