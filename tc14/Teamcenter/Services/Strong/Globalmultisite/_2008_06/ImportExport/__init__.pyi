import System
import Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExportObjectsToOfflinePackageResponse:
    """
    
            ExportObjectsToOfflinePackageResponse structure defines the response from ExportObjectsToOfflinePackage
            operation. It contains briefcase file FMS ticket, export log file FMS ticekts, briefcase
            dataset, and partial errors.
            
    """
    def __init__(self, ) -> None: ...
    BriefcaseFileFMSTicket: str
    """
            FMS ticket of the briefcase file, which can be used to download the briefcase file
            from server to client.
            """
    ExportLogFileFMSTickets: list[str]
    """
            FMS ticket of the briefcase file, which can be used to download the briefcase file
            from server to client.
            """
    BriefcaseDataSet: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            A Dataset which includes the out briefcase file in its namedReference.
            
            After export, a new Dataset will be created. The exported briefcase file will be
            added to the new Dataset. And a new mail which contains the Dataset will be added
            to mailbox folder of the user.  The mail will also be send to mail box of the user
            if the user has set the Email Address.
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors listed above in case of failure conditions.
            """

class ImportObjectsFromOfflinePackageResponse:
    """
    
            ImportObjectsFromOfflinePackageResponse structure defines the response from ImportObjectsFromOfflinePackageResponse
            operation. It contains FMS ticket of the log file, error file, and partial errors
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
            Service data contains the list of created or modified objects and also the partial
            errors listed above in case of failure conditions.
            """

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportObjectsToOfflinePackage(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], OptionSetTag: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue], SessionOptionAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> ExportObjectsToOfflinePackageResponse:
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
    def ImportObjectsFromOfflinePackage(self, FmsTicket: str, OptionSetTag: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet, OptionNamesAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue], SessionOptionAndValues: list[Teamcenter.Services.Strong.Globalmultisite._2007_06.ImportExport.NamesAndValue]) -> ImportObjectsFromOfflinePackageResponse:
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

