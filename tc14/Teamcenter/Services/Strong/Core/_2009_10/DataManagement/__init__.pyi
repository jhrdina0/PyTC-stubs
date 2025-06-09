import System
import System.Collections
import Teamcenter.Services.Strong.Core._2007_01.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetItemFromAttributeInfo:
    """
    
            Input parameters for retrieving Item and ItemRevision objects based
            on attribute keys
            
    """
    def __init__(self, ) -> None: ...
    ItemAttributes: System.Collections.Hashtable
    """
            A map of attribute names and values (string/string)
            used to peform the search. Typical keys are "item_id", "object_type", "object_name",
            "owning_organization", and "date_released".  A special key, "rev_id", may also be
            used to specify a single related ItemRevision object to retrieve. This "rev_id"
            key is effective only if the nRev parameter equals zero.
            """
    RevIds: list[str]
    """
            A list of revision ID strings specifying ItemRevison objects to retrieve.
            This parameter only takes effect if the nRev
            parameter equals zero. This list of revision IDs can be used independent of the "rev_id"
            key value in itemAttributes
"""

class GetItemFromAttributeItemOutput:
    """
    
            This data structure contains an Item and a list of related ItemRevision
            objects retrieved by a getItemFromAttribute
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """The retrieved Item object"""
    ItemRevOutput: list[GetItemFromAttributeItemRevOutput]
    """The list of related ItemRevision objects"""

class GetItemFromAttributeItemRevOutput:
    """
    Contains a single ItemRevision retrieved by the getItemFromAttribute operation
    """
    def __init__(self, ) -> None: ...
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The retrieved ItemRevision"""
    Datasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """list of Datasets associated with the ItemRevision"""

class GetItemFromAttributeResponse:
    """
    
            The return structure from from getItemFromAttribute
            operation. Contains a list of GetItemFromAttributeItemOutput
            structures.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetItemFromAttributeItemOutput]
    """A list of found Item and ItemRevision objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard ServerData member with any returned
            error codes and messages
            """

class GetTablePropertiesResponse:
    """
    Structure holds response from getTableProperties.
    """
    def __init__(self, ) -> None: ...
    TableInfo: list[TableInfo]
    """
            This vector contains a list of TableInfo, and each TableInfo contains
            information pertaining to the specific Table it references.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData structure is used to return the updated Table objects in the update
            section and also any errors encountered during this operation call.
            """

class TableCellValueTypeInfo:
    """
    This structure contains table cell value type info.
    """
    def __init__(self, ) -> None: ...
    Type: str
    """
            This specifies the data type that the cell of the table can hold. The type specified
            in this string, should be one of the below supported type:
            

TableCellInt
            
TableCellString
            
TableCellDouble
            
TableCellLogical
            
TableCellHex
            
TableCellSED
            
TableCellBCD
            
TableCellDate
            

"""
    StrValues: list[str]
    """A list of values"""

class TableCellInfo:
    """
    This structure contains Table Cell Info.
    """
    def __init__(self, ) -> None: ...
    Row: int
    """This specifies the row number of the cell in the Table."""
    Column: int
    """This specifies the column number of the cell in the Table."""
    Desc: str
    """This is a string which can be used to capture a description for the cell."""
    Value: TableCellValueTypeInfo
    """This is a structure which contains information pertaining to a value on the cell."""

class TableDefInfo:
    """
    This structure contains Table Definition Info.
    """
    def __init__(self, ) -> None: ...
    Rows: int
    """This specifies the number of rows in the Table."""
    Columns: int
    """This specifies the number of columns in the Table."""
    RowLabels: list[str]
    """
            This is a vector of strings, each string representing the labels corresponding to
            a row in the Table.
            """
    ColLabels: list[str]
    """
            This is a vector of strings, each string representing the labels corresponding to
            a column in the Table.
            """
    TableDef: Teamcenter.Soa.Client.Model.Strong.TableDefinition
    """tableDef is of type TableDefinition"""

class TableInfo:
    """
    Table Info
    """
    def __init__(self, ) -> None: ...
    TableObject: Teamcenter.Soa.Client.Model.ModelObject
    """The Business Object corresponding to the Table"""
    TableDefInfo: TableDefInfo
    """
            Meta information about the Table such as the row labels, columns labels, and its
            size are contained in this structure.
            """
    TableCells: list[TableCellInfo]
    """
            This is a vector of the structures that contain information pertaining to each of
            the cells in the Table.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetTableProperties(self, TableData: list[TableInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation allows client applications to set the properties pertaining to one
             or more Table business objects. Client developers will need to set information
             pertaining to the number of rows, columns, descriptions of each row and column, and
             cell information for each cell of the Table. The cell information must contain
             the type of cell, value to be placed in the cell, and optionally, a description of
             those values. The current operation only works on cells of specific types and it
             is mandatory that the type of the cells being set on the input structure corresponds
             to one of the cell types defined in the database schema viewable through the BMIDE.
             Supported valid types are:
             

TableCellInt

TableCellString

TableCellDouble

TableCellLogical

TableCellHex

TableCellSED

TableCellBCD

TableCellDate




Use Cases:

             This operation can be used by a client developer, when he/she deals with setting
             Table Business Object specific properties. Typically, Table Business
             Objects are not themselves visible in the Teamcenter workspace and appear as properties
             of other owning objects that are visible in the workspace. Modification to the owning
             objects, may involve changes to one or more of the Table properties that they reference
             through the Table.  In such cases, the setTableProperties is to be called,
             passing in the input structure which is setup to specify the modified values.
             
             One such example of existing usage of this operation, is the existing Teamcenter
             Rich Client functionality for modification of an Integer type of Parameter Definition
             [ ParmDefIntRevision Business Object ]. This Business Object and the functionality
             for its modification are provided by the add on Calibration and Configuration Data
             Management module.  During modification, of the integer parameter definition object,
             client code renders table like UI for each table property of the Parameter Definition,
             gathers the input values from the UI and populates a vector of the input structure
             of type TableInfo, sets the type of thecells to TableCellInt and makes
             the operation call. Client code will then parse the Service Data returned from the
             operation to obtain a handle to the updated Table Business Object. Errors,
             if any were encountered during the operation execution, are handled via the Service
             Data.
             


Teamcenter Component:

             CCDM - Calibration and Configuration Data Management
             
        :param TableData: 
                         This vector contains a list of <i>TableInfo</i>, and each <i>TableInfo</i> contains
                         information pertaining to the specific <b>Table</b> it references. The data present
                         in the <i>TableInfo</i> structures are used to modify specific cell values and/or
                         descriptions of the rows, columns or values.
             
        :return: This operation returns a Service Data structure. The updated Table business objects
             are included in the updated service data member list, which contains any modifications
             to row and column descriptions and the size of the table. Any errors encountered
             at the time of modification are included as part of the Service Data errors.
        """
        ...
    def GetItemFromAttribute(self, Infos: list[GetItemFromAttributeInfo], NRev: int, Pref: Teamcenter.Services.Strong.Core._2007_01.DataManagement.GetItemFromIdPref) -> GetItemFromAttributeResponse:
        """    
             This service retrieves Item and its related ItemRevision objects based
             on the supplied attribute key-value pairs supplied in the infos
             list. All the key-value pairs except for the rev_id
             key are used to create a query for Item objects.
             

             Once a set of Item objects have been retrieved, their ItemRevision
             objects are retrieved based on the following rules:
             

If  nRev is a negative value
             then all the ItemRevision objects are returned
             
If nRev is a positive value
             then the nRev most recent ItemRevision
             objects are returned. If nRev is greater
             than the number of revisions then all of them are returned.
             
If nRev is zero and a rev_id attribute key was supplied in the attribute
             key-value pairs, then that ItemRevision object is returned.
             
If nRev is zero and rev ids
             values were supplied in the GetItemFromAttributeInfo
             object then all of the specified rev ids will be returned.
             



Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Infos: 
                         The list of attribute value keys for the retrieval. The attributes must be the unique
                         key attributes of the class. Currently, only item_id attribute should be used
             
        :param NRev: 
<ul>
<li type="disc">nRev &lt; 0        retrieve all available ItemRevision objects
                         </li>
<li type="disc">nRev = 0        retrieve no ItemRevision objects
                         </li>
<li type="disc">nRev &gt; 0        retrieve the most recent nRev number of ItemRevision
                         objects
                         </li>
</ul>

        :param Pref: 
<font face="courier" height="10">GetItemFromIdPref</font> object used to filter the
                         returned <b>ItemRevision</b> objects. If a <b>Dataset</b> is found related to the
                         <b>ItemRevision</b> with this relation type name and is one of the types specified
                         in the list of object type names, return the <b>ItemRevision</b> object
             
        :return: 
        """
        ...
    def GetTableProperties(self, Table: list[Teamcenter.Soa.Client.Model.Strong.Table]) -> GetTablePropertiesResponse:
        """    
             This operation allows client applications to obtain the properties pertaining to
             one or more Table Business Objects. Client developers will need to pass in
             references to each Table that they need to query information on.  Note that
             the input vector needs to contain only references to the Teamcenter Table business
             object, this operation cannot be used to fetch properties of any other Business Objects.
             

Use Cases:

             This operation can be used by a client developer, when he/she deals with obtaining
             specific Table Business Object specific properties. Typically, Table
             Business Objects are not themselves visible in the Teamcenter workspace and appear
             as properties of other owning objects that are visible in the workspace.  The typical
             scenario in such cases is that a user attempts to obtain/view all properties of the
             the owning object, which may have one or more reference properties pointing to a
             Table.  A custom UI would need to display the Table related properties on the parent
             object in such cases and rendering these properties would require the client applications
             to obtain such information using the getTableProperties operation.
             
             One such example of existing usage of this operation, is the existing Teamcenter
             Rich Client functionality for viewing properties an Integer type of Parameter
             Definition [ ParmDefIntRevision Business Object ]. This Business Object
             and the functionality for viewing its properties are provided by the add on Calibration
             and Configuration Data Management module, through custom stylesheets which render
             a Table like UI for each referenced Table property.  At the time of rendering the
             UI, the client operations call the getTableProperties operation to obtain
             properties such as the number of rows, number of columns, labels for each row and
             column, the type of the cells and cell values and descriptions for each cell in the
             table.
             


Dependencies:

             getProperties
             

Teamcenter Component:

             CCDM - Calibration and Configuration Data Management
             
        :param Table: 
                         This is a vector of the Table Business Objects for which the properties need to be
                         obtained.
             
        :return: Returns GetTablePropertiesResponse
        """
        ...

