import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GenerateReportInput:
    """
    Input structure for ESM Report Generation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Hardware/software ItemRevision for which a report is to be generated."""
    ConfigRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """
            The configuration revision rule that supplies which revision of an Item is
            the parent of the hardware ItemRevision. If null, the default configuration
            rule will be used.
            """
    ReportFormatType: int
    """Desired format of the generated report, 0 for HTML, 1 for Microsoft Excel."""
    CreateDataset: bool
    """If true a Dataset is created with the report attached to it."""
    DatasetName: str
    """
            The name of the Dataset of the generated report. This value is ignored if
            createDataset is false.
            """

class GenerateReportOutput:
    """
    Report Generation Output.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the GenerateReportInput.clientId.
            This can be used by the caller to identify this data structure with the source input
            data.
            """
    DatasetObject: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The Dataset created for the generated report. This will be null if the createDataset flag was set to false.
            """
    FileName: str
    """
            The full local path name of the generated HTML or Excel report in the FMS transient
            volume.
            """

class GenerateReportResponse:
    """
    GenerateReport Response for Report generation.
    """
    def __init__(self, ) -> None: ...
    ReportOutputs: list[GenerateReportOutput]
    """A list of generated reports."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The newly created Datasets are returned in the Created list."""

class ESMBase:
    """
    Interface ESMBase
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateHardwareSoftwareReport(self, GenerateReportInputs: list[GenerateReportInput]) -> GenerateReportResponse:
        """    
             This operation generates an ESM report which shows the software used by the indicated
             hardware.  The report is stored in a file in either HTML or Excel format.  Optionally
             the file can be stored as a Teamcenter Dataset.
             

Use Cases:

             The user inputs a hardware type item revision and selects a report output format
             (HTML or Excel).  A report showing the software items or revisions used by this hardware
             is created in either an HTML or Excel file.  This file can be stored as a Teamcenter
             Dataset.
             

Teamcenter Component:

             Embedded Software Manager Base - Application to manage software binaries in Tc and
             manage their relations to ECUs (electronic control units)
             
        :param GenerateReportInputs: 
                         A list of requested hardware/software reports.
             
        :return: has
             multiple UsedBy relations then the partial error 48161 is returned.
        """
        ...
    def GenerateSoftwareHardwareReport(self, GenerateReportInputs: list[GenerateReportInput]) -> GenerateReportResponse:
        """    
             This operation generates an ESM report which shows the hardware that uses the indicated
             software.  The report is generated in either HTML or Excel format and can optionally
             be stored on a Dataset.
             

Use Cases:

             The user inputs a software type item revision and selects a report output format
             (HTML or Excel).  A report showing the hardware items or revisions that use this
             software is created in either an HTML or Excel dataset.  This file can be stored
             as a Teamcenter Dataset.
             

Teamcenter Component:

             Embedded Software Manager Base - Application to manage software binaries in Tc and
             manage their relations to ECUs (electronic control units)
             
        :param GenerateReportInputs: 
                         A list of requested hardware/software reports.
             
        :return: has
             multiple UsedBy relations then the partial error 48161 is returned.
        """
        ...

