import Teamcenter.Soa.Client.Model
import typing

class AssemblyConfigurationResponse:
    """
    
            This structure is used by SOA Teamcenter::Soa::Cad::_2018_06:: StructureManagement::writeAssemblyConfigurationDetails
            for returning XML output file name in readFileTicketForStructureData and status of
            operation is written to serviceData.
            
    """
    def __init__(self, ) -> None: ...
    ReadFileTicketForStructureData: str
    """
            This is the FMS read file ticket for the TC XML data file written to the transient
            volume. The TC XML file can be downloaded using this ticket.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This service data contains any partial errors which may have been encountered during
            processing. The partial error client Ids match the client Id for the input which
            failed.
            """

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def WriteAssemblyConfigurationDetails(self, BomWindow: Teamcenter.Soa.Client.Model.ModelObject, OptionSetName: str) -> AssemblyConfigurationResponse: ...

