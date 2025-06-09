import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SrmServiceInput:
    """
    Input structure for exportToSRM.
    """
    def __init__(self, ) -> None: ...
    Reason: str
    """
            Reason for the export of the selected Teamcenter parts to SRM. This reason for the
            export is used to populate the description of the event in RFx.
            """
    SponsorUserID: str
    """
            Username of the current logged in Teamcenter user who is sponsor user of RFx application
            in a specific partition. This user of Teamcenter will be assigned as sponsor to the
            event being created as part of the SRM export.
            """
    SponsorEmailID: str
    """
            Email ID of the sponsor or any person who is required to be notified for the success
            or failure of the export to SRM.
            """
    Parts: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The reference of the Teamcenter parts to be exported to SRM."""
    TransferOption: Teamcenter.Soa.Client.Model.Strong.TransferOptionSet
    """
            The name of the transfer option set to be used for exporting the selected Teamcenter
            parts as Tc XML which will be further exported to the SRMConnect middleware application.
            This middleware application calls RFx Web services to create an event, items, etc.
            in RFx.
            """

class SRMIntegration:
    """
    Interface SRMIntegration
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExportToSRM(self, SrmInput: SrmServiceInput) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Through this option Teamcenter initiates asynchronous exchange of assemblies, attributes,
             and attachments with the suppliers through RFx. Data is exported directly from Teamcenter
             to RFx through SRMConnect middleware application with no intermediate objects created.
             Once the export finishes, an event is created in RFx with the item data exported
             from Teamcenter. The supplier can provide a change in assembly with the item attribute
             information and attachments through the created RFx event. Sponsors and suppliers
             users of RFx can access Teamcenter datasets directly from the Teamcenter FMS. Responses
             from the supplier to the event can be published back to Teamcenter from RFx. No supplier
             comparison or award process is supported by this exchange.
             

Teamcenter Component:

             SrmIntegration SOA Component - Component for TcSoaSrmIntegration
             
        :param SrmInput: 
                         The data is exported to RFx based on the information on the <font face="courier" height="10">SrmServiceInput</font> type input. It contains information of the Teamcenter
                         parts, transfer option set, sponsor username, sponsor email, and the reason for export.
             
        :return: element with no object is returned
             as part of create, update, delete, or plain lists. If the SRMConnect middleware application,
             which acts as a bridge between Teamcenter and RFx, is not reachable then error code
             33123 is returned as a partial error.
        """
        ...

