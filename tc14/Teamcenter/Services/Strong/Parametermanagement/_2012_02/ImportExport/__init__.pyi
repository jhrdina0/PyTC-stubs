import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class FileInfo:
    """
    
FileInfo structure represents the details
            of a file.
    """
    def __init__(self, ) -> None: ...
    Filename: str
    """File name"""
    FileTicket: str
    """
            File ticket specific to the memory layout. Callers of this Teamcenter Service would
            use this file ticket information to download the files to the path specified by the
            user.
            """

class DatasetOutput:
    """
    
DatasetOutput structure represents the output
            of the dataset.
    """
    def __init__(self, ) -> None: ...
    MemoryLayout: Teamcenter.Soa.Client.Model.ModelObject
    """The selected Memory Layout object."""
    DatasetCreated: Teamcenter.Soa.Client.Model.ModelObject
    """Dataset created for the specific Memory Layout."""
    DatasetFileInfo: FileInfo
    """Dataset file name and file ticket information"""

class ExportParmDataResponse:
    """
    
ExportParmDataResponse structure represents
            the details of the exported parameter data.
    """
    def __init__(self, ) -> None: ...
    SelectedObjectsExpOutput: list[SelectedObjectExportOutput]
    """Output of export for each selected input object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data to hold Teamcenter Services framework objects that were created or updated
            by the service.
            """

class FormInfo:
    """
    
FormInfo structure represents the details
            of form information.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the form to be created."""
    Description: str
    """Description of form"""
    FormType: str
    """Form type"""
    FormObject: Teamcenter.Soa.Client.Model.ModelObject
    """Form object if exists. Null for new form creation."""
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    """Dataset object which form is associated, if it already exists. Null for new form."""
    RelationName: Teamcenter.Soa.Client.Model.ModelObject
    """Relation name with which form will be associated to dataset."""
    AttributesMap: System.Collections.Hashtable
    """Name value pair of option data of form."""

class ImportParmDataResponse:
    """
    
ImportParmDataResponse structure represents
            the details of output of import.
    """
    def __init__(self, ) -> None: ...
    SelectedObjectsImpOutput: list[SelectedObjectImportOutput]
    """Output of import for each selected input object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data to hold Teamcenter Services framework objects that were created or updated
            by the service. Warnings/violations during validation [Validate Only options] or
            import will be added to ServiceData partial erros. Based on severity information,
            we can show warnings, violations infromation to user in client.
            """

class ParmDataInputForExport:
    """
    
ParmDataInputForExport structure represents
            all the details of the selected objects and related information for
export.
    """
    def __init__(self, ) -> None: ...
    SelectedObjectsInfo: list[SelectedObjectsInfo]
    """
            The selected object can be ProductVariantIntent or Configured Parameter
            Project. When multiple objects are passed, they need to be of the same type only.
            """
    MemoryLayouts: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of Memory Layout objects"""
    OverrideContainer: Teamcenter.Soa.Client.Model.ModelObject
    """Override Container object"""
    PurposeString: str
    """Enumerated values to specify the purpose of export."""
    FileType: Teamcenter.Soa.Client.Model.ModelObject
    """It shall be a sub type of Ccd0ParmFile."""
    FileNamePrefix: str
    """Prefix name to be used for dataset and form creation."""
    SaveFlag: bool
    """True indicates to save dataset and form"""
    OverwriteFlag: bool
    """True indicates to overwrite the existing dataset/form if any."""
    ExportOptionsFormData: FormInfo
    """
            Form optional data input for the selected file type if applicable or else it will
            be empty.
            """

class ParmDataInputForImport:
    """
    
ParmDataInputForImport structure represents
            all the details of the selected object and related information for
import.
    """
    def __init__(self, ) -> None: ...
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Either Parameter Project, or Dictionary, or Memory Layout, or
            Override Container, or ProductVariantIntent.
            """
    FileTickets: list[FileInfo]
    """List of files to import."""
    FileType: Teamcenter.Soa.Client.Model.ModelObject
    """It shall be a sub type of Ccd0ParmFile."""
    Purpose: str
    """Enumerated values to specify the purpose of import."""
    SaveFlag: bool
    """True indicates to save dataset and form."""
    Filename: str
    """File name to be used for dataset and form created."""
    ValidateOnly: bool
    """
            True indicates only validation of data and data will not be imported into Teamcenter.
            False indicates data will be imported into Teamcenter
            """
    ProceedOnError: bool
    """
            If true then the validation (if validateOnly is selected) or import (if validateOnly
            is not selected) will proceed with the next data in the input files even if there
            is an error.
            """
    OverwriteFlag: bool
    """True indicates to overwrite the existing dataset/form if any."""
    ImportOptionsFormData: FormInfo
    """
            Form optional data input for the selected file type if applicable or else it will
            be empty.
            """

class SelectedObjectExportOutput:
    """
    
SelectedObjectExportOutput structure represents
            the output of export for each selected input object.
    """
    def __init__(self, ) -> None: ...
    SelectedObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The selected object to export."""
    DatasetOutput: list[DatasetOutput]
    """
            Populated only if saveFlag is true. Contains
            as many members as the number of Memory Layout objects.
            """
    LogFileInfo: FileInfo
    """Log file information generated for export."""

class SelectedObjectImportOutput:
    """
    
SelectedObjectImportOutput structure represents
            the output of import for the selected object.
    """
    def __init__(self, ) -> None: ...
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Selected Object"""
    DatasetCreated: Teamcenter.Soa.Client.Model.ModelObject
    """Populated only if saveFlag is true."""
    Status: bool
    """True indicates import/validation (validation only) is successful."""
    LogFileInfo: FileInfo
    """Log file information generated for import."""

class SelectedObjectsInfo:
    """
    
SelectedObjectsInfo structure represents
            the details of the selected objects.
    """
    def __init__(self, ) -> None: ...
    SelectedObjTag: Teamcenter.Soa.Client.Model.ModelObject
    """
            Either ProductVariantIntent or Configured Parameter Project. If the
            selected object is ProductVariantIntent, varRuleTag
            and revRuleTag will be empty.
            """
    VarRuleTag: Teamcenter.Soa.Client.Model.ModelObject
    """Variant rule object"""
    RevRuleTag: Teamcenter.Soa.Client.Model.ModelObject
    """Revision rule object"""

class ImportExport:
    """
    Interface ImportExport
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportParmData(self, InputForExportDataAndOptions: list[ParmDataInputForExport]) -> ExportParmDataResponse:
        """    
             This operation exports the parameter data (parameter definitions, parameter values,
             computed values and computed address) for each ParmDataInputForExport supplied. The
             ParmDataInputForExport contains the selected business objects and related information
             such as memory layout, override container, export purpose, dataset, and form.  The
             selected object can be ProductVariantIntent or Configured Parameter Project.
             When multiple objects are passed, they need to be of the same type only. The dataset
             shall be a sub type of Ccd0ParmFile. If the save flag is true, the operation
             would create a new dataset containing the exported parameter data and attach the
             dataset to the selected business objects with the relation Ccd0HasOutputFiles.
             If a duplicate dataset (name and type are same) is found in Teamcenter and the override
             flag is true, the operation would overwrite the existing dataset.
             

             Note: Using this operation, customers need to define a sub type of Ccd0ParmFile
             for export and provide the implementation to overwrite the method Ccd0ParmFile::ccd0generateFile().
             

Use Cases:

Use Case1: Generate Flash files from ProductVariantIntent/Configured Parameter
             Project.
             
             You can generate Flash files using exportParmData operations by setting the
             purposeString as FlashFile in the structure
             inputForExportDataAndOptions.
             

Use Case2: Create new datasets containing the exported parameter data.
             
             You can create new datasets containing the exported parameter data. In the structure
             inputForExportDataAndOptions, you need to
             set saveFlag as true and provide the prefix
             name. These new creation datasets will be attached to the selected business objects
             with the relation Ccd0HasOutputFiles. Meanwhile, new form instances including
             the input attribute values will be populated and attached to the datasets with the
             relation Ccd0HasOutputFiles.
             

Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param InputForExportDataAndOptions: 
                         Structures containing the details of the selected objects and the related information
                         for export.
             
        :return: 
        """
        ...
    def ImportParmData(self, InputImportDataAndOptions: list[ParmDataInputForImport]) -> ImportParmDataResponse:
        """    
             This operation imports the memory address and formula information from a user specified
             file into the selected business object. The selection object can be Parameter
             Project or Dictionary or Memory Layout or Override Container
             or ProductVariantIntent. If the save flag is true, the operation would create
             a new dataset containing the input file and attach the dataset to the selected object
             with the relation Ccd0HasInputSource.
             

             Note: Using this operation, customers need to define a sub type of Ccd0ParmFile
             for import and provide the implementation to overwrite the method Ccd0ParmFile::ccd0Parse().
             

Use Cases:

Use case1:  Import the memory address and formula information into Parameter Project/Dictionary

             You can update the existing parameter memory address and the existing parameter formula
             in a Parameter Project/Dictionary using importParmData operation.
             

Use case2:  Import the memory address and formula information into Memory Layout

             You can update the existing parameter memory address and the existing parameter formula
             in a Memory Layout using importParmData operation.
             

Use case3:  Import the memory address and formula information into Override Container

             You can update the existing override memory address and the existing override formula
             in an Override Container using importParmData operation.
             

Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param InputImportDataAndOptions: 
                         Structures containing the details of the selected objects and the related information
                         for import.
             
        :return: 
        """
        ...

