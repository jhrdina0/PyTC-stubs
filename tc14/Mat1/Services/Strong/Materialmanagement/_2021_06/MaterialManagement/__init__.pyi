import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExportMaterialsDataIn:
    """
    Group of list of Material objects and list export options.
    """
    def __init__(self, ) -> None: ...
    MaterialData: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """
            List of Mat1MaterialRevision objects belonging to same material catalog (Mat1MatCatalogRevision)
            or single Mat1MatCatalogRevision or single Mat1MaterialClassification
"""
    Options: System.Collections.Hashtable
    """Contains map of valid options for exportMaterialsData operation."""

class ImportExportMaterialsDataResponse:
    """
    
            Structure contains list of fileTickets of the files containing
            
            * exported Materials in case of exportMaterialsData operation
            
            * summary of importMaterialsData operation.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service Data including partial errors that are mapped to the client id from the input.
            Service Data could contain errors and in case of importMaterialsData operation it
            could contain any created/updated objects as well.
            """
    TransientFileReadTickets: list[str]
    """List of transient file read tickets for the exported Materials."""

class ImportMaterialsDataIn:
    """
    
            Groups list of files of same format containing materials or material classes belonging
            to same Material Catalog.
            
    """
    def __init__(self, ) -> None: ...
    Files: list[str]
    """
            List of Input File FMS tickets containing Materials or Material classes in file.
            For Materials, File format needs to be specified in import option.
            """
    MaterialCatalog: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Object of type Mat1MatCatalog to be used to create the Mat1Material
            or Mat1MaterialClassification objects from the input file. If this field is
            empty and catalogName option is not specified in ImportExportOptions, then default
            catalog referred by preference IMM_DEFAULT_MATERIAL_CATALOG would be used for Mat1Material
            creation. Global classes would be created if empty Mat1MatCatalog is passed
            during import of material classification data.
            """
    Options: System.Collections.Hashtable
    """Contains map of valid options for importMaterialsData operation."""

class MaterialManagement:
    """
    Interface MaterialManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportMaterialsData(self, Input: list[ExportMaterialsDataIn]) -> ImportExportMaterialsDataResponse:
        """    
             Exports one of the following
             
             1. Instances of input Mat1MaterialRevision & its' decendent classes and
             its parameters in the provided format which belongs to same belonging Mat1MatCatalogRevision.
             One or more instances Mat1MaterialRevision or its' decendent classes is expected.
             
             2. Instances of Mat1MaterialRevision & its' decendent classes and its
             parameters in the provided format belonging to input Mat1MatCatalogRevision.
             Only one instance of Mat1MatCatalogRevision is expected in input.
             
             3. Instances of input Mat1MaterialClassification & all Mat1MaterialClassification
             objects pointing to input object. One or more instances of Mat1MaterialClassification
             class is expected.
             

             ImportExportOptions play an important role in the way Mat1MaterialRevision
             objects are exported.
             

Use Cases:

             X
             

Teamcenter Component:

             Material Management SOA Component - Component for Mat1SoaMaterialMgmt.
             
        :param Input: 
                         List of ExportMaterialsDataIn objects. Each structure contains list of <b>Mat1MaterialRevision</b>
                         objects &amp; corresponding export options. If mutiple objects are to be exported
                         in different export formats, each export format should have one ExportMaterialsDataIn
                         object.
             
        :return: is expected as input.
        """
        ...
    def ImportMaterialsData(self, Input: list[ImportMaterialsDataIn]) -> ImportExportMaterialsDataResponse:
        """    
             Import one of the following
             
             1. Materials and its parameters from given list of files in specified file format.
             
             2. Material classes and its heirarchy.
             

             ImportExportOptions also play an important role in determining the way Materials
             are imported.
             

Use Cases:

             x
             

Teamcenter Component:

             Material Management SOA Component - Component for Mat1SoaMaterialMgmt.
             
        :param Input: 
                         List of ImportMaterialsDataIn objects.
             
        :return: and its' decendent classes are allowed.
        """
        ...

