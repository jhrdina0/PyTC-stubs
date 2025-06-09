import System
import Teamcenter.Services.Strong.Core._2007_06.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetDatasetTypesWithFileExtensionOutput:
    """
    This struct contains pair of file extension and the list of DatasetTypeInfo structures.
    """
    def __init__(self, ) -> None: ...
    FileExtension: str
    """The fileExtension for each dataset type specified in fileExtensions input"""
    DatasetTypesInfo: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.DatasetTypeInfo]
    """The matching list of named reference information"""

class GetDatasetTypesWithFileExtensionResponse:
    """
    
            This struct contains the list dataset type and reference information and Service
            Data.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetDatasetTypesWithFileExtensionOutput]
    """
            List of named reference information for each dataset type specified in fileExtensions
            input
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The DatasetType objects that corresponds to fileExtensions input"""

class TraceabilityFilterInput:
    """
    
            TraceabilityFilterInput structure has parameters for property filtering for trace
            report building. This includes name of property on which filter will get applied,
            operator type, and the value of comparison.
            
    """
    def __init__(self, ) -> None: ...
    LogicalOperatorType: int
    """
            Type of the operator applied to concatenate this property clause with previous property
            clause. Below are valid values
            
            0 - LOGICAL_AND
            
            1 - LOGICAL_OR
            """
    PropertyName: str
    """Name of the property to be filtered."""
    OperatorType: int
    """
            Type of operator to be applied to compare the value of property, below are valid
            values
            
            0 = OP_EQUALS
            
                                    1
            = OP_NOT_EQUALS
            
                                    2
            = OP_LESS_THAN
            
                                    3
            = OP_LESS_OR_EQUAL
            
                                    4
            = OP_GREATER_THAN
            
                                    5
            = OP_GREATER_OR_EQUAL
            
"""
    PropertyValue: str
    """Value of property expected."""

class TraceabilityInfoInput1:
    """
    
            Information required to generate a trace report.  Type of trace report, if indirect
            trace link included, and list of FND_TraceLink relation type name and object
            type names to be included in trace report.  Also, it includes all the details of
            apply property filtering and name of property by which trace report needs to updated.
            Also it has details about whether to export trace report to RAC to show or to export
            to MSExcel application.
            
    """
    def __init__(self, ) -> None: ...
    SelectedObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of objects on which to generate the Trace Report."""
    ReportType: int
    """Type of Report that is defining(0), complying(1), or both(2)."""
    ReportDepth: int
    """
            Level to which Trace Report should be generated. Its value should be greater than
            0.
            """
    IsIndirectTraceReportNeeded: bool
    """If true then only Indirect Trace Report will be included in the final Trace Report."""
    FilteredTraceLinkTypes: list[str]
    """
            This is the list of FND_TraceLink type, for which type only the Trace Report
            needs to be constructed excluding other types.
            """
    FilteredObjectTypes: list[str]
    """
            The list of object type, for which type only the Trace Report needs to be constructed
            excluding other types.
            """
    ScopeLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of all the scope BOM lines from BOM Window under which the searched object
            (which is going to be added in trace report ) BOM lines needs to be searched.
            """
    PropertyFilterInput: list[TraceabilityFilterInput]
    """
            The list of property filtering inputs. This property filter needs to be applied of
            the trace report going to send to client and only filter criteria report will be
            sent to the client.
            """
    SortPropName: str
    """Name of the property name by which the Trace Report needs to be sorted."""
    SortDirection: int
    """1 to sort ascending order, 2 to sort descending order. 0 if no sort applied."""
    ExportTo: str
    """
            Format name to export trace report. It will be either "TraceReportRACExport" - for
            exporting Traceability report to RAC, or " TraceReportMSExcelExport" - for exporting
            Traceability report to MSExcel application.
            
"""
    ExportTemplate: str
    """Name of export template to be used to export the trace report."""
    ExportColumnNames: list[str]
    """This is list of real property names to be exported to Excel."""

class TraceabilityReportOutput1:
    """
    
            This structure holds information of either of following, including service data:
            
            1. Generated trace reports with defining and/or complying trace trees with selected
            objects, and its persistent objects
            
            2. Information about the file ticket for exported file generated at the server.
            
    """
    def __init__(self, ) -> None: ...
    TraceReports: list[TraceReport1]
    """
            This member holds all the Trace Reports user has asked for. This is vector of TraceReport1
            type of structures.
            """
    TransientFileReadTickets: list[str]
    """The transient file read tickets for the exported file."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data."""

class TraceReportTreeNode:
    """
    
            This structure holds information of each trace link report line with information
            of parent object, and its children associated with trace link relation
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            This object represents any BusinessObject in Teamcenter on which Trace Link
            is created.
            """
    DisplayObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            If the Trace Link is created on the occurrence then this variable will represent
            the object to show in the Trace Report.
            """
    SrcContextName: str
    """This parameter will hold the name of context for source object of Trace Link."""
    TarContextName: str
    """This parameter will hold the name of context for target object of Trace Link."""
    BomView: Teamcenter.Soa.Client.Model.Strong.PSBOMView
    """This field represents the BOMView of context line for the TraceLink."""
    IsDirectLink: bool
    """This flag tells if current object is direct trace link object or not."""
    IsTraceLinkObj: bool
    """This flag tells if current object is trace link object or not."""
    ChildNodes: list[TraceReportTreeNode]
    """This represents child nodes with trace link relation with current object."""

class TraceReport1:
    """
    
            This structure holds information about generated trace reports with defining and
            complying trace trees with selected objects, and its persistent objects.
            
    """
    def __init__(self, ) -> None: ...
    DefRootNode: TraceReportTreeNode
    """Represents the root node of Defining Tree in the Trace Report."""
    CompRootNode: TraceReportTreeNode
    """Represents the root node of Complying Tree in the Trace Report."""
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Represents selected object for which Trace Report generated."""
    PersistentObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Represents persistent object for the selected object for which Trace Report generated."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDatasetTypesWithFileExtension(self, FileExtensions: list[str]) -> GetDatasetTypesWithFileExtensionResponse:
        """    
             This operation returns the dataset type and reference information for a set of file
             extensions. Named references are Teamcenter objects that relate to a specific data
             file. For each file extension, it is possible that it belongs to multiple dataset
             types. For such cases, all matching dataset types will be returned using the file
             extension as the key in the GetDatasetTypesWithFileExtensionOutput structure. The
             order of file extension in the GetDatasetTypesWithFileExtensionOutput structure may
             be different than the order of file extension input. This operation will insert file
             extensions that match the default dataset type defined in AE_default_dataset_type
             preference at the beginning of the list. This operation uses TC_Dataset_Import_Exclude_Wildcard
             preference to determine if wildcard may be used in file extension input. If the preference
             is set and file extension is set to asterisk, this operation will return all data
             set types that allow wildcards in its name reference in Teamcenter. Details about
             these two preferences can be found in Preferences and Environment (Variables Reference
             Configuration preferences, under Data management preferences).
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param FileExtensions: 
                         List of file extensions used to get the named reference information
             
        :return: Dataset type and reference information for each fileExtensions input. Possible errors
             returned in ServiceData are: 214135 The input file extension does not exist
        """
        ...
    def GetTraceReport(self, Input: list[TraceabilityInfoInput1]) -> TraceabilityReportOutput1:
        """    
             This operation will generate a Trace Report on the objects selected by user. The
             report will contain information about complying as well as defining objects which
             are connected to selected object using FND_TraceLink, or its subtype. This
             operation will check if there is any TraceLink relation starting or ending
             from selected object(s). If TraceLink relation exists for selected object(s),
             then it gets the other end of TraceLink relation and generates a trace report.
             
             

             Trace links can be between following objects:
             

             * Between occurrences of an ItemRevision

             * Between any two WorkspaceObject.
             

             Following will be added, in addition to existing getTraceReport operation:
             

             * If scope of search structure is defined for the getting Trace Report in input of
             this operation by sending top lines of BOMWindow instances, then matching
             TraceLink instances within the scope windows will be returned.
             
             * If input of this operation is having list of object type names, then object type
             filter will be applied to target objects of TraceLink.
             
             * If input of this operation is having list of TraceLink type names, then
             those types of TraceLink will be returned in Trace Report.
             
             * If propertyFilterInput is given in the input of this operation, then the additional
             filter of property will be applied on the output before sending to client.
             
             * Trace report tree will be sorted for given property, sort direction can also be
             defined, if not defined then it will get default sorted in ascending direction.
             
             * The output of this operation can be either sent to rich client to build the report
             or to MSExcel application.
             
             * User can export this trace report to MSExcel application by sending appropriate
             exportTo mode in input. If the mode of export is "TraceReportMSExcelExport",
             then trace report will be exported to .xlsm file and this file ticket will be sent
             to rich client. Then rich client will download the file and open MSExcel application.
             


Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 

        :return: format.
        """
        ...
    def RefreshObjects2(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], LockObjects: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used to reload the in-memory representation of the objects from
             the database.
             
             Any references to the object will still be valid. Any in-memory changes to the original
             object will be lost. If the object has been changed in the database since it was
             last loaded, then those changes will not be present in memory.
             
             The operation updates the in memory representation to reflect database changes.
             

             If the lockObjects flag is true then it will aquire write lock on objects otherwise
             operation will release the write lock on the business objects.
             
             This is useful when client needs to do an in-process lock and unlock for shorter
             duration that does not require checkout or checkin mechanism. Client caling this
             operation to lock the objects must unlock those objects by callng this operation.
             
             This operation must be used in pairs to lock and unlock the objects.
             

Use Cases:

             Use this operation to do bulk lock & bulk unlock of Input Objects.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Objects: 
                         A list of business objects for which lock or unlock operation is required .
             
        :param LockObjects: 
                         If true then business objects will be locked , false will unlock the given business
                         objects.
             
        :return: 515109:  The instance is in use.
        """
        ...

