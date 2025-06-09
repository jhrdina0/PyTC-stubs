import System
import Teamcenter.Soa.Client.Model
import typing

class ImportManufaturingFeaturesInput:
    """
    input for import manufaturing features.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """
            A BOMLine in the product structure. The connected parts of the imported manufatruing
            features are searched under this line.
            """
    Content: list[ImportManufaturingFeaturesScope]
    """A list of detailed input."""

class ImportManufaturingFeaturesResponse:
    """
    The output of import manufacturing features.
    """
    def __init__(self, ) -> None: ...
    LogFileName: str
    """The name of the generated log file."""
    LogFileTicket: str
    """The FMS ticket of the log file."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""

class ImportManufaturingFeaturesScope:
    """
    Detailed input for importing manufacturing features
    """
    def __init__(self, ) -> None: ...
    XmlFileTicket: str
    """The FMS file ticket for the input XML file to be imported."""
    Container: Teamcenter.Soa.Client.Model.ModelObject
    """The BOMLine under which the manufaturing features are going to be imported."""
    ImportMode: str
    """
            Indicates whether the existing manufaturing features under the container maybe deleted
            or not. The possible values of the import mode are: keepExistingFeatures -
            The existing discrete manufacturing features under the container should not be deleted.
            refreshWholeContainer - The existing discrete manufacturing features under
            the container may be deleted.
            """
    NameRefFileTickets: list[str]
    """The FMS tickets for dataset named reference files."""

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportManufacturingFeatures(self, Input: ImportManufaturingFeaturesInput) -> ImportManufaturingFeaturesResponse:
        """    
             This operation imports discrete and continuous manufaturing features (MFGs) from
             a given PLMXML file into a target product structure in Teamcenter. The PLMXML contains
             the data about the MFGs. The data contains the name of the MFGs. Their transform,
             their parts' connection, and their form attributes. There are two types of manufacturing
             features. Continuous MFG like arcweld ( Mfg0BVRArcWeld) and discrete MFGs like weld
             point (Mfg0BVRWeldPoint) and datum point (Mfg0BVRDatumPoint). For continuous MFGs,
             the PLMXML also contains the JT information.
             

Use Cases:

             none
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         input for import manufaturing features.
             
        :return: - The preference MEImportMFGsManufacturingFeatureIdAttributeName contains invalid
             value.
        """
        ...

