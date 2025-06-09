import Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AttributeComplexData2:
    """
    
            Represents the table data that is consist of a list of column headers, row headers,
            rows, table column title and table row title.
            
    """
    def __init__(self, ) -> None: ...
    ColumnHeaders: list[AttrTableHeader2]
    """A list of column headers to update in the table."""
    RowHeaders: list[AttrTableHeader2]
    """A list of row headers to update in the table."""
    Rows: list[AttrTableRow2]
    """A list of rows to update."""
    TableRowTitile: str
    """The table row title."""
    TableColumnTitle: str
    """The table column title."""
    FreeText: list[str]
    """A list of free texts to update in the table."""

class AttrGoalRangeTableData:
    """
    Represents the goal and range table data of the parameter to be created or updated.
    """
    def __init__(self, ) -> None: ...
    Operation: str
    """
            The operation to be performed on the goal table of the parameter. The supported operations
            are "create" and "update" which would be case-insensitive.
            

"create": The system creates or overwrites the goal table based on
            the input fileTicket or jsonString.
            
"update": The system updates the goal table based on the input table
            data.
            

"""
    FileTicket: str
    """
            A file ticket to be used to create or update the goal table. It is optional. The
            system can create or update the goal table using fileTicket, jsonString
            or tableData.
            """
    JsonString: str
    """
            A JSON string to be used to create or update the goal table. It is optional.The system
            can create or update the goal table using fileTicket, jsonString or tableData.
            """
    TableData: AttributeComplexData2
    """
            A table data to be used to update the goal table. It is optional. The system can
            create or update the goal table using fileTicket, jsonString or tableData.
            """

class AttrTableCell2:
    """
    Represents a cell within the row.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """The column index in the row."""
    CellValues: System.Collections.Hashtable
    """
            The map (string, string) represents the cell data. The valid keys  are: "goal", "min",
            "max", "deviation", and "value". The values can be any string.
            """

class AttrTableHeader2:
    """
    Represents the column or row header in the table.
    """
    def __init__(self, ) -> None: ...
    Indexes: list[int]
    """The indexes of the row or column header."""
    Title: str
    """The title of the row or column header."""
    UnitSymbol: str
    """
            The symbol string of the unit of measure. The system will find the UnitOfMeasure
            based on the symbol. Alternatively, use unit to specify UnitOfMeasure. This is an
            optional field. It is applicable to the column header only.
            """
    Unit: Teamcenter.Soa.Client.Model.Strong.UnitOfMeasure
    """
            A UnitOfMeasure object. This is an optional field. It is applicable to the column
            header only.
            """
    DataType: str
    """The data type of the input column.The valid data type is "string"."""

class AttrTableRow2:
    """
    Represents a row within the table.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """The row index in the table."""
    Cells: list[AttrTableCell2]
    """Information about various cells of a row which includes cell."""

class AttrValueTableData:
    """
    Represent information about complex data and operation to be performed on the data.
    """
    def __init__(self, ) -> None: ...
    Operation: str
    FileTicket: str
    """
            A file ticket to be used to create or update the value table. It is optional. The
            system can create or update the value table using  fileTicket, jsonString
            or rows.
            """
    JsonString: str
    """
            A JSON   string to be used to create or update the value table. It is optional. The
            system can create or update the value table using fileTicket, jsonString or rows.
            """
    Rows: list[AttrTableRow2]
    """
            A list of rows to update in the value table.   It is optional. The system can create
            or update the value table using fileTicket, jsonString or rows.
            """

class ReplaceParameterOut:
    """
    Response for a ReplaceParametersOutput. Returns the list of replaced/ignored parameters.
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """The parent object that owns the parameter."""
    OldParams: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute]
    """A list of old parameters which were replaced with new ones."""
    NewParams: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute]
    """A list of new parameters which were used to replace old ones."""
    IgnoredParams: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute]
    """A list of parameters which cannot be replaced."""

class ReplaceParametersOutput:
    """
    A list of replaced parameters output.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifying string from the source ReplaceParamsInput."""
    ReplaceParamsOut: list[ReplaceParameterOut]
    """A list of replaced parameters for each parent."""

class ReplaceParametersResp:
    """
    Response for a list of ReplaceParametersOutput.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[ReplaceParametersOutput]
    """A list of replaced parameters for each parent."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class ReplaceParamInput:
    """
    Input structure for replaceParameters operation.
    """
    def __init__(self, ) -> None: ...
    SelectedParam: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """The selected parameter to replace."""
    TargetParam: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """
            The target parameter used to replace the selected one. If NULL, the operation revises
            the selected parameter and then replaces it with the newly revised parameter.
            """
    RevisePropInput: System.Collections.Hashtable
    """
            A map (string, list of strings) of attributes names and initial values pairs. If
            this is not empty, the system revises the selected parameter with the given properties
            values.
            """
    ReviseAndReplace: bool
    """
            If true, revise and replace the selected parameter; otherwise, revise the parameter
            only if targetParams is empty.
            
            Input structure for replaceParameters operation.
            """

class ReplaceParamsInput:
    """
    Input structure for replaceParameters operation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned ReplaceParametersOutput
            elements and Partial Errors associated with this input ReplaceParamsInput.
            """
    Parents: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The parent   objects  for the selected parameters  . Supported object types are:
            WorkspaceObject (except Att0ParameterPrjRevision and Att0ParameterSetRevision).
            """
    ReplaceParams: list[ReplaceParamInput]
    """A list of selected parameters to replace."""

class UpdateMeasureValueProperties2:
    """
    Represents the input measure value to update or create.
    """
    def __init__(self, ) -> None: ...
    ToCreate: bool
    """
            If true, a new measure value is created on the input parameter; otherwise, update
            the given measure value.
            """
    Method: str
    """
            The method of the measure value to be created. It is used to distinguish how the
            measure value gets populated, e.g. actual value of the measurement, evaluated value
            of the measurement, calculated value of the measurement, asserted value of the measurement,
            or external value from the external tool. The valid method string is "Actual", "Evaluated",
            "Calculated", "Asserted" or "External". It is ignored when toCreate is false.
            """
    MeasureValue: Teamcenter.Soa.Client.Model.ModelObject
    """The input measure value to be updated."""
    ValueProps: System.Collections.Hashtable
    ValueFileInputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.FileProperties]
    """
            A list of value files to be created or replaced. When the given Dataset is
            null, the system creates a new Dataset for the value file. Otherwise, the
            system replaces the existing value file.
            """
    ValueTableInput: AttrValueTableData
    """The value table of the measure value to be created or updated."""

class UpdateParamProperties2:
    """
    
            ParameterProperties2 structure represents all the information needed to create a
            parameter.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Parameter: Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute
    """The input parameter to be updated."""
    ParamDirection: str
    """
            The parameter direction to be updated on the parent. A parameter with input direction
            is used to capture the input (e.g., the goal of fuel economy on the engine system)
            of the simulation.  A parameter with output direction is used to capture the output
            (e.g., the evaluated value of fuel economy on the engine system) of the simulation.
            A parameter with unused direction is used to define a characteristic of the model
            object   (e.g., engine system). The valid direction strings are: "input", "output",
            or "unused".
            """
    ParamProps: System.Collections.Hashtable
    GoalFileInputs: list[Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.FileProperties]
    ValueInputs: list[UpdateMeasureValueProperties2]
    """A list of measure values to be created or updated."""
    GoalTableInput: AttrGoalRangeTableData
    """The goal table of the parameter to be created or updated."""

class UpdateParamsInput2:
    """
    
            UpdateParamsInput2 structure represents a list of parameters to be updated on the
            input parent object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Parameters: list[UpdateParamProperties2]
    """A list of parameters to be updated."""
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """
            The parent object that contains the parameters to be updated. The valid parent types
            are: WorkspaceObject, BOMLine.
            """

class AttributeTargetManagement:
    """
    Interface AttributeTargetManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ReplaceParameters(self, Inputs: list[ReplaceParamsInput]) -> ReplaceParametersResp: ...
    def UpdateParameters2(self, Inputs: list[UpdateParamsInput2]) -> Att0.Services.Strong.Attrtargetmgmt._2020_12.AttributeTargetManagement.UpdateParamsResponse: ...

