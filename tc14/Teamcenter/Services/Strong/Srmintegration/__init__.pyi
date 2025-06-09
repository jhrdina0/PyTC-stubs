import Teamcenter.Services.Strong.Srmintegration._2009_10.SRMIntegration
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class SRMIntegrationRestBindingStub(SRMIntegrationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExportToSRM(self, SrmInput: Teamcenter.Services.Strong.Srmintegration._2009_10.SRMIntegration.SrmServiceInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class SRMIntegrationService:
    """
    
            The SRM Integration service exposes operations that are used to
export assemblies,
            attributes, and attachments to the RFx application. The RFx
application is one of
            a suite of SRM products that deals with exchanging information with
the supplier
            and is primarily used for qualifying, negotiating, and collecting
supplier capability
            information.

            This service provides the following SRM Integration use case

Exchange of Teamcenter assemblies, attributes and attachments with
            the suppliers.

Library Reference:

TcSoaSrmIntegrationStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SRMIntegrationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExportToSRM(self, SrmInput: Teamcenter.Services.Strong.Srmintegration._2009_10.SRMIntegration.SrmServiceInput) -> Teamcenter.Soa.Client.Model.ServiceData:
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

