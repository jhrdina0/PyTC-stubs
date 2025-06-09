import System
import Teamcenter.Services.Strong.Core._2011_06.DataManagement
import Teamcenter.Services.Strong.Core._2012_10.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ObjectInfoLegacy:
    """
    
            This structure holds object information of source or target object of trace link
            in Report structure.
            
    """
    def __init__(self, ) -> None: ...
    ContextName: str
    """
            This parameter will hold the name of context for source or target object of
            
            trace link.
            """
    DisplayObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            If the trace link is created on the occurrence then this variable will represent
            the object to show in the trace report.
            

"""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """
            This object represent any Business Object in Teamcenter on which Trace Link is
            
            created.
            
"""
    BomView: Teamcenter.Soa.Client.Model.ModelObject
    """This field represents the PSBOMView of context line for the trace link."""
    ContextLineObj: Teamcenter.Soa.Client.Model.ModelObject
    """
            This field represents the context line for the trace link, this will be PSBOMViewRevision
            object.
            
"""

class ReportLegacy:
    """
    
            This structure holds information about each trace link report with information of
            parent object, and its children associated with trace link relation.
            
    """
    def __init__(self, ) -> None: ...
    Parent: ObjectInfoLegacy
    """Parent object of trace link."""
    Children: list[ObjectInfoLegacy]
    """List of all child objects for the parent with trace link relation."""

class TraceabilityReportOutput2:
    """
    
            TraceabilityReportOutput2 structure holds information of either of following including
            service data:
            
            1.Â Â Â Â Generated trace reports with defining and/or complying
            trace trees with selected objects, and its persistent objects
            
            2.Â Â Â Â Information about the file ticket for exported file generated
            at the server.
            

            The following partial error may be returned:
            
            1.Â Â Â Â  223201: MS Excel's outlining feature is limited to 8 levels,
            and the selected structure exceeds that level. Therefore it will be exported as a
            flat list with the "Level" column added.
            
            2.Â Â Â Â 223209: The Trace View template <template_name> is invalid.
            Please select an appropriate template as per the report type of trace view.
            
            3.Â Â Â Â 223036: Some of the objects were skipped during the export
            operation as no matching rule was found in the <sheet_name> sheet of the Excel
            template <template_name>.
            
            4.Â Â Â Â 214411: No input objects found. Please select the object
            to get traceability report.
            


    """
    def __init__(self, ) -> None: ...
    TraceReports: list[TraceReport2]
    """All of the requested Trace Reports."""
    TransientFileReadTickets: list[str]
    """
            The transient file read tickets for the exported file, this is specific to Export
            to Excel.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data."""

class TraceabilityReportOutputLegacy:
    """
    
            TraceabilityReportOutputLegacy structure holds information about generated trace
            reports with defining and complying trace trees with selected objects and its persistent
            objects, including service data.
            

            The following partial errors may be returned:
            
            214311: No input objects found. Please select the object to get traceability report.
            
            214312: The provided report type value is not correct; allowed values are 1,2 and
            3.
            
            214313: The provided report depth value is not correct; please provide any value
            greater than zero.
            

    """
    def __init__(self, ) -> None: ...
    TraceReports: list[TraceReportLegacy]
    """
            This member holds all the Trace Reports user has asked for. This is list of
            
            TraceReport type of structures.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data."""

class TraceReportTreeNode2:
    """
    
            This structure holds information of each trace link report line with information
            of parent object, and its children associated with trace link relation.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """BusinessObject instance in Teamcenter on which Trace Link is created."""
    DisplayObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            If the trace link is created on the occurrence then this variable will represent
            the object to show in the trace report.
            """
    SrcContextName: str
    """Context name for source object of trace link."""
    TarContextName: str
    """Context name for target object of trace link."""
    BomView: Teamcenter.Soa.Client.Model.ModelObject
    """The PSBOMView of context line for the Trace Link."""
    ContextLineObj: Teamcenter.Soa.Client.Model.ModelObject
    """The context line (PSBOMViewRevision) for the Trace Link"""
    IsDirectLink: bool
    """If true, the object is a direct trace line object."""
    IsTraceLinkObj: bool
    """If true, the current object  is a trace  link."""
    ChildNodes: list[TraceReportTreeNode2]
    """Child nodes with trace link relation with current object."""

class TraceReport2:
    """
    
            This structure holds information about generated trace reports with defining and
            complying trace trees with selected objects, and its persistent objects.
            
    """
    def __init__(self, ) -> None: ...
    DefRootNode: TraceReportTreeNode2
    """The root node of defining tree in the trace report."""
    CompRootNode: TraceReportTreeNode2
    """The root node of complying tree in the trace report."""
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """The selected object for which trace report generated."""
    PersistentObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Persistent objects for the selected object for which Trace Report generated."""

class TraceReportLegacy:
    """
    
            This structure holds information about generated trace reports with defining and
            complying trace trees with selected objects, and its persistent objects.
            
    """
    def __init__(self, ) -> None: ...
    DefiningTree: list[ReportLegacy]
    """
            List of objects in the Defining Tree in the Trace Report giving all defining trace
            link details.
            
"""
    IndirectDefiningTree: list[ReportLegacy]
    """List of objects in Indirect Defining Tree in the Trace  Report."""
    ComplyingTree: list[ReportLegacy]
    """
            List of objects in the Complying Tree in the Trace Report giving all complying trace
            link details.
            
"""
    IndirectComplyingTree: list[ReportLegacy]
    """List of objects in Indirect Complying Tree in the Trace  Report."""
    SelectedObject: Teamcenter.Soa.Client.Model.ModelObject
    """This structure member represents the object on which Trace Report is generated."""
    PersistentObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of persistent object for the selected object."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTraceReport2(self, Input: list[Teamcenter.Services.Strong.Core._2012_10.DataManagement.TraceabilityInfoInput1]) -> TraceabilityReportOutput2:
        """    
             This operation generates a Trace Report for the input objects.  The report will contain
             information about complying as well as defining objects which are connected to input
             object using FND_TraceLink, or its subtype. This operation checks if there is any
             FND_TraceLink relation starting or ending from input object(s). If FND_TraceLink
             relation exists for input object(s), then it gets the other end of FND_TraceLink
             relation and generates a trace report.
             

             Trace links can be between following objects:
             
             1  Between occurrences of an ItemRevision
             
             2  Between any two WorkspaceObject.
             

             If scope of search structure is defined for the getting trace report in input of
             this operation by sending top lines of BOMWindow instances, then matching trace link
             instances within the scope windows will be returned.
             

             If input of this operation is having list of object type names, then object type
             filter will be applied to target objects of trace link.
             

             If input of this operation is having list of trace link type names, then those types
             of trace link will be returned in trace report.
             

             If property filter is given in the input of this operation, then the additional filter
             of property will be applied on the output before sending to client.
             

             Trace report tree will be sorted for given property, sort direction can also be defined,
             if not defined then it will get default sorted in ascending direction.
             

             The output of this operation can be either sent to rich client to build the report
             or to MSExcel application.
             

             User can export this trace report to MSExcel application by sending appropriate exportTo
             mode in input. If the mode of export is "TraceReportMSExcelExport", then trace report
             will be exported to .xlsm file and this file ticket will be sent to rich client.
             Then rich client will download the file and open MSExcel application.
             


Use Cases:

             Suppose user created trace link between Requirement R1 as start point and R2 as end
             point and creates trace link from Requirement R3 as start and R1 as end point.
             
             When user runs traceability report on R1 requirement he will get R2 object as complying
             object and R3 will come as defining object.
             

             If filter will be added to show only Paragraph type objects, then nothing will be
             returned in Trace Report as the type is not matching with filter.
             

             If filter will be applied to a subtype of FND_TraceLink and above trace link is of
             type FND_TraceLink, then also empty trace report will be returned, as trace link
             type does not match with filter trace link type vector from operation input.
             

             If user invokes command to export the trace report to Excel, then trace report for
             Requirement R1 will be generated and exported in .xlsm file and opened in MSExcel
             application.
             

             Trace link on occurences:
             
             Suppose user created trace link between Requirement R1 as start point and Trace Link
             on occurrence on part P1 as end point by setting the P1's parent line as context
             line then this SOA will also return the PSBomViewRevision which was set as context
             line while creating the Trace Link.
             


Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         Information required to generate a trace report. The object(s) (for which trace report
                         needs to be generated), trace report type, if indirect report required, list of FND_TraceLink
                         types (which are expected in output of this operation), scoped line of BOM Windows
                         (within which trace link needs to searched in), the vector of object types (which
                         need to be added in output of this operation), property search input list, property
                         name by which trace report needs to be sorted, and sorting direction, format of export
                         , and if export to MSExcel application then template name to be applied on trace
                         report.
             
        :return: 
        """
        ...
    def GetTraceReportLegacy(self, Input: Teamcenter.Services.Strong.Core._2011_06.DataManagement.TraceabilityInfoInput) -> TraceabilityReportOutputLegacy:
        """    
             This operation generates a Trace Report for the input objects.  This operation returns
             information about complying as well as defining objects which are connected to selected
             object using FND_TraceLink or its subtype of GRM relation.
             

             Trace links can be between following objects:
             
             1.    Between occurrences of an ItemRevision
             
             2.    Between any two WorkspaceObject.
             

             If indirect trace report flag is set to true during this operation, then user will
             get trace report for ItemRevision if selected object is occurrence, and trace report
             for Items if selected objects is ItemRevision in addition to direct trace report
             for the selected object.
             

             If trace link is on occurrence then This SOA version will return PSBOMViewRevision
             context line information also.
             


Use Cases:

             Suppose user created trace link between Requirement R1 as start point and R2 as end
             point and creates trace link from Requirement R3 as start and R1 as end point.
             
             When user runs traceability report on R1 requirement he will get R2 object as complying
             object and R3 will come as defining object.
             

             TraceLink on occurrences:
             
             Suppose user created trace link between Requirement R1 as start point and trace link
             on occurrence on part P1 as end point by setting the P1's parent line as context
             line then this SOA will also return the PSBomViewRevision which was set as context
             line while creating the trace link.
             



Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         A TraceabilityInfoInput structure to generate a Trace Report.This input structure
                         holds selected objects for which trace report needs to be generated, trace report
                         type, if indirect report required, and base relation type.
             
        :return: 
        """
        ...

