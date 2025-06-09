import System
import Teamcenter.Soa.Client.Model
import typing

class ConstructReportURLResponse:
    """
    The response object from constructReportURL operation.
    """
    def __init__(self, ) -> None: ...
    Url: str
    """The URL string for the TcRA servlet."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData which contains the error stack."""

class TcRAReportsCriteria:
    """
    Criteria needed to retrieve the URL for the specified TcRA operation.
    """
    def __init__(self, ) -> None: ...
    MessageName: str
    """
            It designates desired TcRA report definition operation, e.g. retrieve, view, edit,
            delete or set permission.
            """
    ReportDefinition: Teamcenter.Soa.Client.Model.ModelObject
    """The report definition ID."""
    ContextObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of ID's representing context object(s) (required for item reports)."""

class CubeReports:
    """
    Interface CubeReports
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ConstructReportURL(self, InputCriteria: TcRAReportsCriteria) -> ConstructReportURLResponse:
        """    
             Constructs the servlet URL required by clients to process the TcRA report definition
             operation (retrieve, view, edit, delete or set permission) specified. The report
             definition ID, context objects, message name is required to get this URL.
             

Use Cases:

             User retrieves/views/edits/deletes/sets permission for one TcRA report, this operation
             will generate the corresponding URL for the TcRA operation.
             

Teamcenter Component:

             Business Intelligence - Capability to create and manage report definitions and generate
             reports
             
        :param InputCriteria: 
                         A TcRAReportsCriteria structure which includes the report definition ID info, the
                         context objects, the number of the context objects, the message name.
             
        :return: Contains the URL string for the eQube servlet. Failure will be returned in the ServiceData.
        """
        ...

