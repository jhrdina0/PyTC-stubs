import Esm0.Services.Strong.Esmbase._2011_06.ESMBase
import System
import Teamcenter.Soa.Client

class ESMBaseRestBindingStub(ESMBaseService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GenerateHardwareSoftwareReport(self, GenerateReportInputs: list[Esm0.Services.Strong.Esmbase._2011_06.ESMBase.GenerateReportInput]) -> Esm0.Services.Strong.Esmbase._2011_06.ESMBase.GenerateReportResponse: ...
    def GenerateSoftwareHardwareReport(self, GenerateReportInputs: list[Esm0.Services.Strong.Esmbase._2011_06.ESMBase.GenerateReportInput]) -> Esm0.Services.Strong.Esmbase._2011_06.ESMBase.GenerateReportResponse: ...

class ESMBaseService:
    """
    
            This service is used to create, delete, and query Embedded
            Software Management (ESM) relationships for hardware and software item revisions.
            It also is used to generate formatted reports on the relationship of hardware and
            software item revisions.  The relationships are Embedded, GatewayOf,
            and UsedBy.
            
            The ESMBase service can be used for the following use cases:
            

Create an Embedded relation
            between a hardware and software item revision in Structure Manager.
            
Create a GatewayOf relation
            between hardware item revisions in Structure Manager.
            
Create a UsedBy relation
            between software item revisions in Structure Manager.
            
Find which software item revisions are embedded (is the secondary
            in the Embedded relationship) in a hardware
            item revision.
            
Find which software item revisions use (is the primary in the UsedBy relationship) a software item revision.
            
Find which software item revisions are used by (is the secondary
            in the UsedBy relationship) a software item
            revision.
            


Find which hardware item revisions are embedding (is the primary
            in the Embedded relationship) a software
            item revision.
            
Find which hardware item revisions are accessed by (is the secondary
            in the GatewayOf relationship) a hardware
            item revision.
            
Find which hardware item revisions are gateways of (is the primary
            in the GatewayOf relationship) a hardware
            item revision.
            
Generate an XML report dataset showing which software item revisions
            are embedded (is the secondary in the Embedded
            relationship) in a hardware item revision.
            
Generate an XML report dataset showing which hardware item revisions
            are embedding (is the primary in the Embedded
            relationship) a software item revision.
            


Delete an Embedded relation
            between a hardware and software item revision in Structure Manager.
            
Delete a GatewayOf relation
            between hardware item revisions in Structure Manager.
            
Delete a UsedBy relation
            between software item revisions in Structure Manager.
            




Library Reference:

Esm0SoaESMBaseStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ESMBaseService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GenerateHardwareSoftwareReport(self, GenerateReportInputs: list[Esm0.Services.Strong.Esmbase._2011_06.ESMBase.GenerateReportInput]) -> Esm0.Services.Strong.Esmbase._2011_06.ESMBase.GenerateReportResponse:
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
    def GenerateSoftwareHardwareReport(self, GenerateReportInputs: list[Esm0.Services.Strong.Esmbase._2011_06.ESMBase.GenerateReportInput]) -> Esm0.Services.Strong.Esmbase._2011_06.ESMBase.GenerateReportResponse:
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

