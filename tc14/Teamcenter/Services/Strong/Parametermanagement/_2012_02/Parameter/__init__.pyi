import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetMemoryInfoResponse:
    """
    
GetMemoryInfoResponse structure represents
            all the details of the memory layouts/blocks, unassigned parameters
and override
            records to be loaded.
    """
    def __init__(self, ) -> None: ...
    MemLayoutInfo: list[MemoryLayoutInfo]
    """Memory layout list"""
    MemBlockInfo: list[MemoryBlockInfo]
    """Memory block list"""
    UnassignedParmDefRevs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Unassigned parameter definition list"""
    MemOverrides: list[MemoryOverrideInfo]
    """Override record list"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data to hold SOA framework objects that were created or updated by the service."""

class MemLayoutOrBlockInfo:
    """
    
MemLayoutOrBlockInfo structure represents
            the memory layout/block object to load.
    """
    def __init__(self, ) -> None: ...
    MemLayoutOrBlock: Teamcenter.Soa.Client.Model.ModelObject
    """Memory layout or block business object"""
    IsLayout: bool
    """
            True indicates that memLayoutOrBlock is a
            memory layout.
            """

class MemoryBlockInfo:
    """
    
MemoryBlockInfo structure represents the
            details of the memory block to be loaded.
    """
    def __init__(self, ) -> None: ...
    MemBlock: Teamcenter.Soa.Client.Model.ModelObject
    """Memory block business object"""
    HeaderObject: Teamcenter.Soa.Client.Model.ModelObject
    """Memory block header business object"""
    TrailerObject: Teamcenter.Soa.Client.Model.ModelObject
    """Memory block trailer business object"""
    MemBlocks: list[MemoryBlockInfo]
    """Sub block list"""
    ParmDefRecords: list[ParmDefRecordInfo]
    """Assigned parameter list to this memory block"""

class MemoryContentInfo:
    """
    
MemoryContentInfo structure represents the
            details of the memory content to be loaded.
    """
    def __init__(self, ) -> None: ...
    MemContent: Teamcenter.Soa.Client.Model.ModelObject
    """Memory content business object"""
    MemBlocks: list[MemoryBlockInfo]
    """Memory block list"""
    ParmDefRecords: list[ParmDefRecordInfo]
    """Assigned parameter list"""

class MemoryLayoutInfo:
    """
    
MemoryLayoutInfo structure represents the
            details of the memory layout to be loaded.
    """
    def __init__(self, ) -> None: ...
    LayoutObject: Teamcenter.Soa.Client.Model.ModelObject
    """Memory layout business object"""
    HeaderObject: Teamcenter.Soa.Client.Model.ModelObject
    """Memory layout header business object"""
    TrailerObject: Teamcenter.Soa.Client.Model.ModelObject
    """Memory layout trailer business object"""
    MemoryContent: MemoryContentInfo
    """Memory content information"""

class MemoryOverrideInfo:
    """
    
MemoryOverrideInfo structure represents the
            details of the override records to be loaded.
    """
    def __init__(self, ) -> None: ...
    OverrideContainer: Teamcenter.Soa.Client.Model.ModelObject
    """Override container business object"""
    MemOverrides: list[ParmDefRecordInfo]
    """Memory override record list"""
    ConvRuleOverrides: list[ParmDefRecordInfo]
    """Converion rule override record list"""

class ParmDefRecordInfo:
    """
    
ParmDefRecordInfo structure represents the
            details of the assigned parameter to be loaded.
    """
    def __init__(self, ) -> None: ...
    ParmDefRec: Teamcenter.Soa.Client.Model.ModelObject
    """Parameter record business object"""
    ParmDefRev: Teamcenter.Soa.Client.Model.ModelObject
    """Parameter definition business object"""

class TableCellSEDInfo:
    """
    
TableCellSEDInfo structure represents all
            the details of TableCellSED to be created/updated. If the cell [row,
column]
            is found in the Table in Teamcenter, setTableSEDProperties operation
will
            update this cell with the specified properties. Otherwise,
setTableSEDProperties
            operation will create a new cell.
    """
    def __init__(self, ) -> None: ...
    Row: int
    """Cell row index"""
    Col: int
    """Cell column index"""
    DomainElementName: str
    """Domain element name"""
    Description: str
    """Domain element description"""
    Value: str
    """Domain element value"""

class TableDefInfo:
    """
    
TableDefInfo structure represents all the
            details of Table Definition
    """
    def __init__(self, ) -> None: ...
    Rows: int
    """Number of rows"""
    Cols: int
    """Number of columns"""
    TableDef: Teamcenter.Soa.Client.Model.Strong.TableDefinition
    """TableDefinition business object"""
    RowLabels: list[str]
    """Row labels"""
    ColLabels: list[str]
    """Column labels"""

class TableSEDInfo:
    """
    
TableSEDInfo structure represents all the
            details of SED Table to be updated.
    """
    def __init__(self, ) -> None: ...
    TableObject: Teamcenter.Soa.Client.Model.ModelObject
    """Table business object"""
    TableDefInfo: TableDefInfo
    """Table definition information"""
    TableCells: list[TableCellSEDInfo]
    """Table cell list"""

class Parameter:
    """
    Interface Parameter
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMemoryLayoutOrBlockInfo(self, ParmGrpDefRev: Teamcenter.Soa.Client.Model.ModelObject, MemLayoutOrBlock: list[MemLayoutOrBlockInfo], IncludeChildren: bool, IncludeOverrides: bool) -> GetMemoryInfoResponse:
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
    def SetTableSEDProperties(self, TableData: list[TableSEDInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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

