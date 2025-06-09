import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class DataInfo:
    """
    Structure which has information related to the input data.
    """
    def __init__(self, ) -> None: ...
    ExecutionPlan: Teamcenter.Soa.Client.Model.ModelObject
    """
            Object of type Mei0ExecutionPlan to be exported.
            


"""
    ExportObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of BOMLine objects that needs to be exported."""
    ExportObjectsWithIC: System.Collections.Hashtable
    """
            Key would be the IncrementalChange object and the value is the list of BOMLine
            objects affected by which needs to be exported.
            
"""
    ExportScope: Teamcenter.Soa.Client.Model.ModelObject
    """
            Any miscellaneous object that needs to be sent for export.
            
            This object can have ChangeObject(in case of delta export), top line(in case
            of full export), Form for any additional information to be attached to the
            workflow.
            """

class ExportInfo:
    """
    Structure contains input information related to export of the Objects.
    """
    def __init__(self, ) -> None: ...
    WorkflowTemplate: Teamcenter.Soa.Client.Model.ModelObject
    """The EPMTaskTemplate to be created."""
    Ai: Teamcenter.Soa.Client.Model.ModelObject
    """
ApplicationInterface(AI) object created from earlier export.
            
            If AI is provided, then the RequestObject should be created in this given
            AI, if not passed create a new AI.
            """
    TargetSites: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of sites to export the data."""
    ExportType: bool
    """
            If true, a full export is performed else delta export. In full export, all the child
            lines below the input line present in ChangeObject are exported and in delta
            export only the lines which are present in the ChangeObject are exported.
            


"""

class ExecutionDataExportInputData:
    """
    The data objects that needs to be exported.
    """
    def __init__(self, ) -> None: ...
    DataInfo: DataInfo
    """Information related to input data export."""
    ExportInfo: ExportInfo
    """Information related to export of data objects."""

class ExecutionDataExportResponse:
    """
    Contains created Workflow.
    """
    def __init__(self, ) -> None: ...
    Workflows: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of created EPMJob."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Including partial errors."""

class Release:
    """
    Interface Release
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecutionDataExport(self, Input: list[ExecutionDataExportInputData]) -> ExecutionDataExportResponse:
        """    
             The operation creates the workflow ReleaseUpdateToExecution which exports the input
             data objects to the execution system.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         A list of objects that holds all the export data objects and <b>IncrementalChange</b>
                         object for the created workflow.
             
        :return: 286524 - The EPMTaskTemplate does not exist.
        """
        ...

