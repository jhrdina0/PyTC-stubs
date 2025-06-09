import System
import Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport
import Teamcenter.Soa.Client.Model
import typing

class ImportFromApplicationInputData3:
    """
    Structure represents the parameters required to import a requirement specification.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    TransientFileWriteTicket: str
    """Transient File write ticket for the file to be imported."""
    ApplicationFormat: str
    """Application format associated with the file to be imported into system."""
    CreateSpecElementType: str
    """Subtype of specification element to be imported."""
    SpecificationType: str
    """Type of the specification to be imported. RequirementSpec is default."""
    IsLive: bool
    """Flag to determine live or non live import."""
    SelectedBomLine: Teamcenter.Soa.Client.Model.ModelObject
    """BOMLine under which new structure will get imported."""
    FileMetaDatalist: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.FileMetaData]
    """
            List of FileMetaData that has the imported file information. One for each imported
            specification.
            """
    ImportOptions: list[Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportExportOptions]
    """List of options for import such as keywords. One for each imported specification."""
    SpecDesc: str
    """Description to be set for an Item."""

class FileImportExport:
    """
    Interface FileImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ImportFromApplication(self, Inputs: list[ImportFromApplicationInputData3]) -> Teamcenter.Services.Strong.Importexport._2011_06.FileImportExport.ImportFromApplicationResponse1:
        """    
             This operation imports a Requirement Specification document containing Requirement
             and Paragraph objects. It creates Requirement / Paragraph objects and associated
             data (FullText for each created Item to store the content from the document and IMAN_Specification
             relation between FullText and each created Item). The input structure for this operation
             contains file meta data information, type of specification elements (SpecElement)
             to be created, application format of the MS Word document being imported, keyword
             parsing options to be used during import, live or static import mode to be used for
             import, option to import as new specification or under the selected BOMLine object
             and description to be set on the Item once imported.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Inputs: 
                         The structure which holds the file meta data, format of the document, type of specification
                         elements to be created.
             
        :return: A list of created objects, one for each successfully imported Requirement Specification.
             The following partial error may be returned: 46147   Cannot add the child to the
             selected parent since this child type is not valid for parent type. 46180   The child
             cannot be added to the selected parent since the parent type is not valid for the
             child type.
        """
        ...

