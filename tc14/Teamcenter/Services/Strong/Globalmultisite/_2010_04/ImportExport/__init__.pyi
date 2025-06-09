import System
import Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FileTicket:
    """
    To represent a  file ticket and its original file name.
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """The FMS file Ticket."""
    FileName: str
    """The original file name."""

class ExportObjectsToPLMXMLResponse:
    """
    
            The response for exportObjectsToPLMXML operation.
            It holds the file ticket for the exported XML file, file ticket for the export log
            file, file tickets  for the dataset named reference files, and any partial failures.
            
    """
    def __init__(self, ) -> None: ...
    XmlFileTicket: FileTicket
    """The FMS ticket is used to get the generated PLMXML file."""
    LogFileTicket: FileTicket
    """The FMS ticket is used to get the generated export log file."""
    NamedRefFileTickets: list[FileTicket]
    """
            The FMS tickets are used to get the dataset named  reference files. On Teamcenter
            Services client, the files must be loaded into the directory along with the PLMXML
            file. And the directory must have the same name as the PLMXML file without the file
            extension name.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors is used to report any partial failures.
            """

class ImportObjectsFromPLMXMLResponse:
    """
    
            The response for importObjectsFromPLMXML
            operation. It holds the file ticket for the import log file, and any partial failures.
            
    """
    def __init__(self, ) -> None: ...
    LogFileTicket: FileTicket
    """The FMS ticket is used to get the generated import log file."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors.
            """

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportObjectsToPLMXML(self, ExportObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, Languages: list[str], XmlFileName: str, SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> ExportObjectsToPLMXMLResponse:
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
    def ImportObjectsFromPLMXML(self, XmlFileTicket: str, NamedRefFileTickets: list[str], Transfermode: Teamcenter.Soa.Client.Model.Strong.TransferMode, IcRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SessionOptions: list[Teamcenter.Services.Strong.Globalmultisite._2007_12.ImportExport.NamesAndValues]) -> ImportObjectsFromPLMXMLResponse:
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

