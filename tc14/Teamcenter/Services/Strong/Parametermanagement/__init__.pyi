import System
import Teamcenter.Services.Strong.Parametermanagement._2009_10.Parameter
import Teamcenter.Services.Strong.Parametermanagement._2012_02.ImportExport
import Teamcenter.Services.Strong.Parametermanagement._2012_02.Parameter
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class ImportExportRestBindingStub(ImportExportService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExportParmData(self, InputForExportDataAndOptions: list[Teamcenter.Services.Strong.Parametermanagement._2012_02.ImportExport.ParmDataInputForExport]) -> Teamcenter.Services.Strong.Parametermanagement._2012_02.ImportExport.ExportParmDataResponse: ...
    def ImportParmData(self, InputImportDataAndOptions: list[Teamcenter.Services.Strong.Parametermanagement._2012_02.ImportExport.ParmDataInputForImport]) -> Teamcenter.Services.Strong.Parametermanagement._2012_02.ImportExport.ImportParmDataResponse: ...

class ImportExportService:
    """
    
            The ImportExport service provides operations to communicate the
parameter
            data between Teamcenter and third party sides. The operations in
this service allow
            export of parameter definitions, parameter values and computed
values/addresses from
            Teamcenter to generate Flash files; and allow import of memory
address and formula
            information into Teamcenter to update the existing business objects,
such as ParmGrpDevRevision,
            Ccd0MemoryLayoutRevision and Ccd0OverrideContRevision.

            The ImportExport service can be used for the following use cases:

Generate Flash files from ProductVariantIntent

Generate Flash files from Configured Parameter Project

Import the memory address and formula information into Parameter
            Project/Dictionary

Import the memory address and formula information into Memory
            Layout

Import the memory address and formula information into Override
            Container

Library Reference:

TcSoaParameterManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ImportExportService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExportParmData(self, InputForExportDataAndOptions: list[Teamcenter.Services.Strong.Parametermanagement._2012_02.ImportExport.ParmDataInputForExport]) -> Teamcenter.Services.Strong.Parametermanagement._2012_02.ImportExport.ExportParmDataResponse:
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
    def ImportParmData(self, InputImportDataAndOptions: list[Teamcenter.Services.Strong.Parametermanagement._2012_02.ImportExport.ParmDataInputForImport]) -> Teamcenter.Services.Strong.Parametermanagement._2012_02.ImportExport.ImportParmDataResponse:
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

class ParameterRestBindingStub(ParameterService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetBitDefinitionProperties(self, BitDefinitions: list[Teamcenter.Soa.Client.Model.Strong.BitDef]) -> Teamcenter.Services.Strong.Parametermanagement._2009_10.Parameter.GetBitDefinitionPropertiesResponse: ...
    def GetBitValueProperties(self, BitValues: list[Teamcenter.Soa.Client.Model.Strong.BitValue]) -> Teamcenter.Services.Strong.Parametermanagement._2009_10.Parameter.GetBitValuePropertiesResponse: ...
    def SetBitDefinitionProperties(self, BitDefinitionInfo: list[Teamcenter.Services.Strong.Parametermanagement._2009_10.Parameter.BitDefinitionInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def SetBitValueProperties(self, BitValInfo: list[Teamcenter.Services.Strong.Parametermanagement._2009_10.Parameter.BitValueInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetMemoryLayoutOrBlockInfo(self, ParmGrpDefRev: Teamcenter.Soa.Client.Model.ModelObject, MemLayoutOrBlock: list[Teamcenter.Services.Strong.Parametermanagement._2012_02.Parameter.MemLayoutOrBlockInfo], IncludeChildren: bool, IncludeOverrides: bool) -> Teamcenter.Services.Strong.Parametermanagement._2012_02.Parameter.GetMemoryInfoResponse: ...
    def SetTableSEDProperties(self, TableData: list[Teamcenter.Services.Strong.Parametermanagement._2012_02.Parameter.TableSEDInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class ParameterService:
    """
    
            The Parameter service provides operations to get and set the
BitDefintion
            properties, get and set the BitValue properties, set the SED Table
            properties, refresh and load a parameter dictionary/project, refresh
and load memory
            layouts and blocks.

            The Parameter service can be used for the following use cases:

Get bit definition for a BitDefinition

Create a BitDefinition

Modify a BitDefinition

Get a BitValue

Modify a BitValue

Modify a SED Table

Refresh and load a Parameter Dictionary/Project

Refresh and load Memory Layouts and Blocks

Library Reference:

TcSoaParameterManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ParameterService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetBitDefinitionProperties(self, BitDefinitions: list[Teamcenter.Soa.Client.Model.Strong.BitDef]) -> Teamcenter.Services.Strong.Parametermanagement._2009_10.Parameter.GetBitDefinitionPropertiesResponse:
        """    
             This operation loads the bit definition for each ccdm::BitDef
             supplied. Bit definition contains information for properties such as byte number,
             bit number within the byte, name, meaning of 0 and meaning of 1.
             

Use Cases:

Use case 1: Get bit definition for a BitDef

             You can get the bit definition data using getBitDefinitionProperties operation
             by providing the BitDef tag.
             

Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param BitDefinitions: 
                         BitDef objects
             
        :return: .
        """
        ...
    def GetBitValueProperties(self, BitValues: list[Teamcenter.Soa.Client.Model.Strong.BitValue]) -> Teamcenter.Services.Strong.Parametermanagement._2009_10.Parameter.GetBitValuePropertiesResponse:
        """    
             This operation loads the bit value for each ccdm::BitValue
             supplied. Bit value contains information for properties such as value (true/false),
             bit definition object.
             

Use Cases:

Use case 1: Get bit value for a BitValue object

             You can get the bit value data using getBitValueProperties operation by providing
             the BitValue object.
             

Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param BitValues: 
<b>BitValue</b> objects
             
        :return: .
        """
        ...
    def SetBitDefinitionProperties(self, BitDefinitionInfo: list[Teamcenter.Services.Strong.Parametermanagement._2009_10.Parameter.BitDefinitionInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates or modifies a BitDef business object for each BitDefinitionInfo supplied. The BitDefinitionInfo contains information for properties such as
             byte number, bit number within the byte, name, meaning of 0, and meaning of 1. If
             the BitDef is not null in BitDefinitionInfo
             structure, the operation updates this BitDef with the rest of the property
             values. Otherwise the operation creates a new BitDef with the specific property
             values.
             

Use Cases:

Use case 1: Create a Bit Definition

             You can create a new BitDef using setBitDefinitionProperties operation
             by providing bitDefinitionObject as null
             in BitDefinitionInfo structure.
             

Use case 2: Modify a Bit Definition

             You can modify an existing BitDef using setBitDefinitionProperties
             operation by providing bitDefinitionObject
             as an existing BitDef in BitDefinitionInfo
             structure.
             


Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param BitDefinitionInfo: 
                         Structures containing the details of the bit definition to be created/modified.
             
        :return: in Created/Updated lists.
        """
        ...
    def SetBitValueProperties(self, BitValInfo: list[Teamcenter.Services.Strong.Parametermanagement._2009_10.Parameter.BitValueInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation modifies a BitValue business object for each BitValueInfo supplied. The BitValueInfo
             contains information for properties such as value (true/false), bit definition object.
             The BitValue business object is specified in BitValueInfo
             structure as well.
             

Use Cases:

Use case 1: Modify a Bit Value

             You can modify an existing BitValue using setBitValueProperties operation
             by providing bitValueObject as an existing BitValue in BitValueInfo structure.
             


Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param BitValInfo: 
                         Structures containing the details of the bit value to be modified.
             
        :return: in Updated lists.
        """
        ...
    def GetMemoryLayoutOrBlockInfo(self, ParmGrpDefRev: Teamcenter.Soa.Client.Model.ModelObject, MemLayoutOrBlock: list[Teamcenter.Services.Strong.Parametermanagement._2012_02.Parameter.MemLayoutOrBlockInfo], IncludeChildren: bool, IncludeOverrides: bool) -> Teamcenter.Services.Strong.Parametermanagement._2012_02.Parameter.GetMemoryInfoResponse:
        """    
             This operation refreshes and loads memory layouts and/or blocks information for the
             parameter dictionary/project supplied. If memLayoutOrBlock
             is empty, the operation finds out unassigned parameters in context of the parameter
             dictionary/project. Meanwhile, it loads the associated memory layouts, as well as
             the memory blocks and sub blocks if includeChildren
             is true. However, if memLayoutOrBlock is
             not empty, the operation loads the assigned parameters for each memory layout/block,
             as well as the sub blocks if includeChildren is true. If parmGrpDevRev
             points to a parameter project and includeOverrides
             is true, the operation loads the override records from the associated override container
             as well.
             

Use Cases:

Use Case1: Refresh and load a parameter dictionary/project

             You can refresh and load a parameter dictionary/project using getMemoryLayoutOrBlockInfo
             operation by setting memLayoutOrBlock as
             empty. The operation finds out the unassigned parameters in context of the parameter
             dictionary/project. It loads the associated memory layouts, as well as the memory
             blocks and sub blocks if includeChildren
             is true. If includeOverrides is true and
             parmGrpDev points to a parameter project,
             the operation loads the override records from the associated override container as
             well.
             

Use Case2: Refresh and load memory layouts and blocks

             You can refresh and load memory layouts and blocks using getMemoryLayoutOrBlockInfo
             operation by specifying memory layout/block objects in the memLayoutOrBlock.
             The operation loads the assigned parameters for each selected memory layout/block,
             as well as the sub blocks if includeChildren
             is true. If includeOverrides is true and
             parmGrpDev points to a parameter project,
             the operation loads the override records from the associated override container as
             well.
             

Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param ParmGrpDefRev: 
<b>ParmGrpDefRevision</b> business object. It shall be parameter dictionary or project.
                         If <b>ParmGrpDef</b> represents property equals <b>Parameter Dictionary</b>, <font face="courier" height="10">ParmGrpDefRev</font> points to a parameter dictionary.
                         If equaling to <b>Parameter Breakdown</b>, <font face="courier" height="10">ParmGrpDefRev</font>
                         points to a parameter project.
             
        :param MemLayoutOrBlock: 
                         Structures of memory layout or block information
             
        :param IncludeChildren: 
                         True to load the sub blocks
             
        :param IncludeOverrides: 
                         True to load the override records. Only if <font face="courier" height="10">parmGrpDefRev</font>
                         points to a parameter project, is the parameter useful.
             
        :return: 
        """
        ...
    def SetTableSEDProperties(self, TableData: list[Teamcenter.Services.Strong.Parametermanagement._2012_02.Parameter.TableSEDInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation modifies a SED (State Encoded) Table for each TableSEDInfo supplied. The TableSEDInfo
             contains information for properties such as table definition, and table cells information.
             The Table business object is specified in TableSEDInfo
             structure as well.
             

Use Cases:

Use case 1: Modify a SED Table

             You can modify an existing SED Table using setTableSEDProperties operation
             by providing tableObject as an existing SED Table in TableSEDInfo structure.
             

Teamcenter Component:

             Calibration and Configuration Data Management - Calibration and Configuration Data
             Management
             
        :param TableData: 
                         Structures containing the details of the SED <b>Table</b> to be modfied.
             
        :return: in Updated lists.
        """
        ...

