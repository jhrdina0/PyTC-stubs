import Mei0.Services.Strong.Mesinteg._2014_12.Release
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class DataInfo2:
    """
    Structure which has information related to the input data
    """
    def __init__(self, ) -> None: ...
    ExecutionPlan: Teamcenter.Soa.Client.Model.ModelObject
    """The Mei0ExecutionPlan (derived from CCObject) to be exported."""
    ExportObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of BOM line objects that needs to be exported"""
    ExportObjectsWithIC: System.Collections.Hashtable
    """
            Key would be the IncrementalChange object and the value is the list of BOM
            line objects affected by which needs to be exported.
            """
    InfoForm: Teamcenter.Soa.Client.Model.ModelObject
    """
            The Mei0ReleaseUpdateToMesInfo form or any other customized form with the
            export additional information to be attached to the workflow.
            """
    ExportScope: Teamcenter.Soa.Client.Model.ModelObject
    """
            Any miscellaneous object that needs to be sent for export.This object can have ChangeObject(in
            case of delta export), top line(in case of full export), Form for any additional
            information to be attached to the workflow.
            """

class ExecutionDataExportInputData2:
    """
    The data objects that needs to be exported
    """
    def __init__(self, ) -> None: ...
    DataInfo: DataInfo2
    """Information related to input data export."""
    ExportInfo: Mei0.Services.Strong.Mesinteg._2014_12.Release.ExportInfo
    """Information related to export of data objects."""

class Release:
    """
    Interface Release
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecutionDataExport2(self, Input: list[ExecutionDataExportInputData2]) -> Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportResponse:
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

