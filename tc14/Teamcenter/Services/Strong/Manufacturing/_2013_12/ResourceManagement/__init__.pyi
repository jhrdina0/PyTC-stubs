import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CatalogInfo:
    """
    The structure contains vendor catalog information
    """
    def __init__(self, ) -> None: ...
    VendorName: str
    """Name of the vendor that provided the catalog"""
    VendorAcronym: str
    """Acronym of the vendor that provided the catalog"""
    VendorCatalogVersion: str
    """Version of the catalog"""
    VendorCatalogLanguage: str
    """Language of the catalog"""
    VendorCatalogDescription: str
    """Description of the catalog"""
    VendorCatalogShortDescription: str
    """Short description of the catalog"""
    VendorCatalogID: str
    """Unique ID of the catalog"""
    VendorCatalogRootClassID: str
    """Root class ID of the catalog"""
    VendorCatalogRootDir: str
    """Root directory of the catalog"""

class GetStepP21FileCountsResponse:
    """
    
The counts of available STEP P21 product files for the given classes will be
returned.

The following partial errors may be returned:

- 71513 Invalid class ID

- 300361 Assortment file cannot be found.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""
    CountMap: System.Collections.Hashtable
    """A map of class IDs for which the counts are requested and its corresponding counts."""

class GetVendorCatalogInfoResponse:
    """
    
A list of all vendor catalogs that are available on the Teamcenter server
machine.
Each catalog info object contains detailed information about each catalog like
the
name, acronamy, version, language and description. Additionally a unique catalog
ID is returned that can be used to identify it lateron. The root class ID is the
ID of the Classification main class for this specific vendor catalog, when it is
imported. The root directory that is returned is the actual, full directory
where
the catalog is located. It can be used to start the import of the catalog
hierarchy
using the service operation importVendorCatalogHierarchy.

Only valid catalogs will be returned. If there is a corrupt catalog (e.g., if
one
of the mandatory files or directories is missing), this catalog will not be
returned
in the list of catalogs. If one corrupt catalog is found, the system continues
searching
for other valid catalogs and returns all valid ones.

The following partial errors may be returned:

- 300300 The preference MRMGTCVendorCatalogRootDir is not defined.

- 300301 The specified vendor catalog root directory does not exist.

- 300302 No vendor catalog was found.

    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""
    CatalogInfo: list[CatalogInfo]
    """The vendor catalog information"""

class RMFileTicket:
    """
    The file information of log file
    """
    def __init__(self, ) -> None: ...
    Ticket: str
    """The FMS file ticket"""
    FileName: str
    """The original file name"""

class ImportStepP21FilesResponse:
    """
    
The importStepP21FilesResponse object that contains the logfile with additional
data
of the import. When there is a failure during the import, an error code will be
returned
as the part of the service data.

Possible errors are:

- 71513 Invalid class ID

- 300361 Assortment file cannot be found

- 300362 Mapping file cannot be found

- 300363 STEP P21 file cannot be found

- 300324 Invalid import options

- 300364 Error importing STEP P21 files (details can be found in the import log
file (file ticket))
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""
    LogFileTicket: RMFileTicket
    """Ticket of the import log file"""

class ImportVendorCatalogHierarchyResponse:
    """
    
This importVendorCatalogHierarchyResponse object that contains the logfile with
additional
data for the import. When there is a failure during the import, an error code
will
be returned as the part of the service data.

Possible errors are:

- 300301 Specified vendor catalog root directory does not exist

- 300320 Transfer mode cannot be found

- 300321 Invalid transfer mode tag

- 300322 Transfer mode object does not exist

- 300323 Vendor catalog hierarchy import file does not exist

- 300324 Invalid import options

- 300325 File ticket for PLMXML log file cannot be created

- 300326 Error importing vendor catalog hierarchy (details can be found in the
import
log file (file ticket))

    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data that can contain error codes"""
    LogFileTicket: RMFileTicket
    """Ticket of the import log file"""

class ResourceManagement:
    """
    Interface ResourceManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetStepP21FileCounts(self, ClassIDs: list[str]) -> GetStepP21FileCountsResponse:
        """    
             This operation retrieves the count of STEP P21 product files that are available in
             a GTC vendor catalog in and below the specified classes.
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param ClassIDs: 

        :return: - 300361 Assortment file cannot be found.
        """
        ...
    def GetVendorCatalogInfo(self) -> GetVendorCatalogInfoResponse:
        """    
             This operation retrieves information about the GTC vendor catalogs that are available
             on the Teamcenter server machine. The multi-value preference "MRMGTCVendorCatalogRootDir"
             allows you to specify one or multiple root directories where those catalogs can be
             stored. This operation scans the given directories for GTC vendor catalogs and returns
             detailed information for each catalog.
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :return: 
        """
        ...
    def ImportStep3DModels(self, IcoIDs: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation imports STEP 3D model files for Generic Tool Catalog (GTC) vendor
             catalog components. The STEP files are converted to NX part and to JT file format
             and imported into Teamcenter. If needed, items are created for the Classification
             objects (ICO). One UGMaster dataset for the NX part file and one DirectModel dataset
             for the JT file is created below the (new) item.
             

Use Cases:

             There are two different use cases:
             
                 A) The specified ICO is classified in a GTC vendor catalog
             class
             
             (the ICO has an attribute -159003 "3D Model file name")
             
                 B) The specified ICO is classified in an MRL MyComponents
             class
             
             (the ICO does not have an attribute -159003 "3D Model file name")
             

             In use case A, this operation retrieves the file name of the 3D model directly from
             GTC attribute
             
             -159003 "3D Model file name".
             
             (Another attribute ID instead of -159003 can be defined in the "MRMGTC3DModelAttributeID"
             preference.)
             

             In use case B, the SOA operation checks if there is an Manufacturing Resource Libraray
             (MRL) attribute -40930 "Vendor Reference Object ID" in the given ICO. This attribute
             is used to store the reference from the MRL MyComponents ICO to the GTC vendor catalog
             ICO. If this attribute exists in the ICO's class and has a valid ICO ID as value,
             the 3D model file name will be retrieved from the referenced ICO. (see use case A)
             
             (Another attribute ID instead of -40930 can be defined in the "MRMGTCReferenceObjectAttributeID"preference.)
             

             The SOA operation retrieves the information about the server-sided directory, where
             all STEP 3D models of the catalog are stored, based on the class of the GTC vendor
             catalog ICO.
             

             If there is a problem during importing one of the 3D models, the operation will continue
             importing the 3D models of the following ICOs.
             

             Note: The Graphics Builder has to be configured properly for this operation to work.
             


Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param IcoIDs: 
                         The Classification object (ICO) IDs identifying the tool component under which the
                         graphics will be imported.
             
        :return: 
        """
        ...
    def ImportStepP21Files(self, ClassID: str, ImportOptions: int) -> ImportStepP21FilesResponse:
        """    
             This operation imports STEP P21 files containing the attributes values of manufacturing
             components (vendor product data) into the vendor catalog Classification classes.
             
             It creates Classification objects (ICOs) and associated data. Depending on the available
             data in the input directory, the associated items might be created to store drawing
             files and/or images.
             


Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param ClassID: 
                         The class ID of a specific vendor catalog class. All catalog products from this class
                         and all child classes of this class will be imported.
             
        :param ImportOptions: 

        :return: 
        """
        ...
    def ImportVendorCatalogHierarchy(self, VendorCatalogRootDir: str, ImportOptions: int) -> ImportVendorCatalogHierarchyResponse:
        """    
             This operation imports the Classification class hierarchy (including class icons
             and images) of a GTC (Generic Tool Catalog) vendor catalog. The catalog hierarchy
             will be imported below the Manufacturing Resource Library (MRL) "Vendor Catalogs"
             class. The vendor catalog root directory that is needed as input parameter can be
             retrieved using the service operation getVendorCatalogInfo().
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param VendorCatalogRootDir: 
                         The root directory that contains the GTC vendor catalog
             
        :param ImportOptions: 
                         The import options allow you to control whether the catalog hierarchy will overwrite
                         (1) existing classes or ignore (0) those classes and not import them.
             
        :return: - 327102 Current GTC root directory does not exist
        """
        ...
    def UpdateNXToolAssemblies(self, IcoIDs: list[str], IdentifyCutAndNoCut: bool, GenerateSpinning: bool, SetToolJunctions: bool, WritePartAttributes: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation triggers specific actions on the NX side to update one or mutliple
             tool assemblies for use in NX CAM. The tool assemblies are identified by their Classification
             object (ICO) IDs. Initially, the tool assemblies are created in the Resource Manager
             in Teamcenter. Then this operation uses the Graphics Builder and calls some NX user
             functions. UGMaster datasets and an NX part files are created for the tool assemblies.
             The different input parameters trigger more actions.  To ensure that this operation
             works properly, the "NX Tool Type" (MRL attribute -45110) has to be defined in the
             tool assemblies. Turning tool assemblies have to have a "Tracking Point" (MRL attribute
             -45015) specified. This operation works only for tool assemblies that are classified
             using the Manufacturing Resource Library (MRL).
             
             Note: The Graphics Builder has to be configured properly for this operation to work.
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param IcoIDs: 
                         The Classification object (ICO) IDs identifying the tool assemblies
             
        :param IdentifyCutAndNoCut: 
                         If true, the "Cut" and "NoCut" information from the different tool components is
                         taken and stored in the assembly itself.
             
        :param GenerateSpinning: 
                         If true, the "Cut" and "NoCut" information from the tool assembly is taken and the
                         "Cut" and "NoCut" rotation spun.
             
        :param SetToolJunctions: 

        :param WritePartAttributes: 

        :return: 
        """
        ...

