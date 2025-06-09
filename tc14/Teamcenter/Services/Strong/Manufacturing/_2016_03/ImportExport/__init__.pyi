import System
import System.Collections
import Teamcenter.Services.Strong.Manufacturing._2015_10.ImportExport
import Teamcenter.Soa.Client.Model
import typing

class ImportManufaturingFeaturesInput:
    """
    input for import manufaturing features
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """
            A BOMLine in the product structure. The connected parts of the imported manufatruing
            features are searched under this line
            """
    Content: list[ImportManufaturingFeaturesScope]
    """A list of detailed input"""

class ImportManufaturingFeaturesScope:
    """
    Detailed input for importing manufacturing features
    """
    def __init__(self, ) -> None: ...
    XmlFileTicket: str
    """The FMS file ticket for the input XML file to be imported"""
    Scope: Teamcenter.Soa.Client.Model.ModelObject
    """
            The BOMLine under which the manufaturing features are being searched. Based
            on the result of the search, the import decides whether to create a new manufacturing
            feature or to update an existing one
            """
    Container: Teamcenter.Soa.Client.Model.ModelObject
    """The BOMLine under which the manufaturing features are going to be imported"""
    ImportMode: str
    """
            Indicates whether the existing manufacturing features under the container shall be
            deleted or not. The possible values of the import mode are:  keepExistingFeatures
            The existing discrete manufacturing features under the container should not be deleted.
            refreshWholeContainer   The existing discrete manufacturing features under the container
            may be deleted.
            """
    NameRefFileTickets: list[str]
    """A list of FMS tickets for the dataset named reference files"""

class MfgExportToBriefcaseResponse:
    """
    This operation returns export log and datasets associated with exported objects.
    """
    def __init__(self, ) -> None: ...
    BriefcaseFileFMSTicket: str
    """
            FMS ticket of the briefcase file, which can be used to download the briefcase file
            from server to client.
            """
    FileTickets: list[str]
    """To represent a file ticket and its original file name."""
    MessageIds: list[str]
    """List of message IDs."""
    BriefcaseDataSet: Teamcenter.Soa.Client.Model.ModelObject
    """
            A business object of Dataset which includes the out briefcase file in its namedReference.
            
            After export, a new Dataset will be created. The exported briefcase file will be
            added to the new Dataset.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data contains the list of created or modified objects and also the partial
            errors in case of failure conditions.
            """

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportToBriefcase(self, Reason: str, Sites: list[Teamcenter.Soa.Client.Model.ModelObject], Objects: list[Teamcenter.Soa.Client.Model.ModelObject], TransferOptionSet: Teamcenter.Soa.Client.Model.ModelObject, OptionNameAndValues: System.Collections.Hashtable, SessionOptionNamesAndValues: System.Collections.Hashtable) -> MfgExportToBriefcaseResponse:
        """    
             This operation is applicable specifically for Manufacturing Process Planner MPP
             application.
             
             This operation combines following two operations.
             
             Teamcenter::Soa::GlobalMultiSite::_2008_06::ImportExport exportObjectsToOfflinePackage
             
             Teamcenter::Soa::GlobalMultiSite::_2008_06::ImportExport requestExportToRemoteSites
             
             In addition, it creates internal objects which are helpful in supplier collaboration
             use cases for manufacturing objects. Details in the use case section.
             

Use Cases:

Use Case 1:  Exporting objects to the briefcase by transferring the ownership
             to the supplier.

             User wants to export Collaboration Context (CC) object in MPP to the
             briefcase to be used by the supplier at remote site.
             
             The CC may contain product structure(s), bill of processes (BOP) such
             as plant BOP, plant structure etc.
             
             While exporting, the user wants to transfer ownership of few objects in the CC
             to the supplier so that the supplier can make changes to those objects on the other
             site.
             
             The user selects the CC and uses the menu option Tools, Export To, Briefcase...
             
             he menu option opens a dialog that allows user to set a destination site, a transfer
             option set, a list of traverse options and a list of session options.
             
             In this case, all the objects which can be traversed by the transfer option set and
             session options will be exported into an output TC XML file.
             
             The files and datasets related to exported objects will be downloaded and packed
             into the briefcase file along with the TC XML file.
             

             In addition, the internal object, Appearance Path Node (APN) will be created
             for the identified BOMLine objects in the CC. The BOMLine objects
             are identified based on the preference MERuleForBriefcaseExport.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Reason: 
                         The reason for the export, the size is limited to 240 characters. This can be blank.
             
        :param Sites: 
                         The destination sites, only one site is supported as of now. The site should be marked
                         as offline in the <b>Organization</b> application in Teamcenter to perform a briefcase
                         export.
             
        :param Objects: 
                         List of objects  to be exported such as <b>CC</b>, <b>BOMLine</b>.
             
        :param TransferOptionSet: 
                         The <b>TransferOptionSet</b> can be created/modified/customized by the end user.
             
        :param OptionNameAndValues: 
                         Please refer the documentation of the PLM XML Export Import administration tool for
                         more details.
             
        :param SessionOptionNamesAndValues: 
                         processUnconfiguredByOccEff
             
        :return: 
        """
        ...
    def ImportManufacturingFeatures(self, Input: ImportManufaturingFeaturesInput) -> Teamcenter.Services.Strong.Manufacturing._2015_10.ImportExport.ImportManufaturingFeaturesResponse:
        """    
             The PLMXML contains the data about the MFGs. The data contains the name of the MFGs.
             Their transform, their parts' connection, and their form attributes. There are two
             types of manufacturing features. Continuous MFG like arcweld ( Mfg0BVRArcWeld)
             and discrete MFGs like weld point (Mfg0BVRWeldPoint) and datum point (Mfg0BVRDatumPoint).
             
             For continuous MFGs, the PLMXML also contains the JT information.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         input for import manufaturing features.
             
        :return: - The preference MEImportMFGsManufacturingFeatureIdAttributeName contains invalid
             value.
        """
        ...

