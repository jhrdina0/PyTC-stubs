import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttrFileData:
    """
    Represents all the data needed to import complex data from Excel.
    """
    def __init__(self, ) -> None: ...
    FileTicket: str
    """The FMS ticket for the Excel file to be imported."""
    SheetNamePropNameMapping: System.Collections.Hashtable
    """
            A map (string, string) where the key is the name of the tab in the Excel and the
            value is the BMIDE property defined in the class Attr0AttributeTable to write complex
            data on.
            """
    SheetNameMeasurementPropNameMapping: System.Collections.Hashtable
    """
            A map (string, string) where the key is the name of the tab in the Excel and and
            the value is the BMIDE property defined in the class Attr0ValueTable to write complex
            data on.
            """

class AttributeComplexData:
    """
    
            Represents the complex data of a property. The complex data includes Table Name,
            Row Headers, Column Headers and actual data of 2D array. The column headers and row
            headers are optional.
            
    """
    def __init__(self, ) -> None: ...
    TableName: str
    """The name of table which represents the complex data."""
    ColumnHeaders: list[AttrTableHeader]
    """
            A list of AttrTableHeader objects which has Information about various column
            headers which includes column name, its id and order.
            """
    RowHeaders: list[AttrTableHeader]
    """
            A list of AttrTableHeader objects which has information about various row
            headers which includes row name, its id and order.
            """
    Rows: list[AttrTableRow]
    """
            A list of AttrTableRow objects which represents the actual complex data in
            form of rows. Each row may have have one or more columns which holds the actual data.
            """

class AttrTableCell:
    """
    Represents a cell in the column.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """The header id of the column. It should match with the Index property of column header."""
    Data: str
    """
            The actual data to be stored. Data will be always be stored in string format, client
            need to convert the data to the data type according to type of Attribute.
            """

class AttrTableData:
    """
    Represent information about complex data and operation to be performend on the data.
    """
    def __init__(self, ) -> None: ...
    Operation: str
    ComplexData: AttributeComplexData
    """The actual complex data to perform operation on."""

class AttrTableHeader:
    """
    
            Represents header information for either row or column. The AttrTableHeader is generic
            data structure. If it is used in AttrTableRow then this represent information about
            row else if it is used in column headers then it represents information about column.
            
    """
    def __init__(self, ) -> None: ...
    Index: int
    """
            The unique id for row or column in the table. It will be used by the client of this
            SOA to show column and row in the correct order and also to make any changes to the
            row or column.
            """
    Name: str
    """Name of the row header or column header. This is an optional field."""

class AttrTableRow:
    """
    Represents a single row of data.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """The header id of the row. It should match with the Index property of row header."""
    Cells: list[AttrTableCell]
    """
            Information about various cells of a row which includes header information, its id
            and actual data.
            """

class SetAttributeComplexDataIn:
    """
    
            Represents all the information needed to create or update the complex data on Attribute
            Definition and Measurable Attribute.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    ObjectToModify: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The object on which complex data needs to be created or updated. The allowed types
            are: Att0AttributeDefRevision and Att0MeasurableAttribute.
            """
    FileData: AttrFileData
    PropNameToTableDataMap: System.Collections.Hashtable
    """
            Name value pair (string,  AttrTableData) of name of property and list of AttrTableData
            to be written to objectToModify. The property name is Teamcenter internal name of
            property on Att0AttributeTable. Supported properties are:  att0GoalTable,
            att0MinTable and att0MaxTable.
            """
    PropNameToMeasurementTableDataMap: System.Collections.Hashtable
    """
            Name value pair (string, AttrTableData) of name of property  list of AttrTableData
            to be written to to be written to objectToModify.  The property name is Teamcenter
            internal name of property on Att0ValueTable.  Supported property is: att0ValueTable.
            """
    IsProceedWithValidationError: bool
    """
            If true, system will proceed with import of data and show warning to user if there
            are any validation errors in the input data. If false, system will show the validation
            error and will not import the data.
            """

class AttributeTargetManagement:
    """
    Interface AttributeTargetManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetAttributeComplexData(self, Inputs: list[SetAttributeComplexDataIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

