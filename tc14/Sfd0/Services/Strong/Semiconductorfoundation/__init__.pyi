import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class MarkingServiceRestBindingStub(MarkingServiceService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ValidateAndUpdatePanelContent(self, MarkingPanelRev: Teamcenter.Soa.Client.Model.Strong.Sfd0MrkgPanelRevision, DesignType: str, MarkingPattern: str, MarkingValue: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class MarkingServiceService:
    """
    
            Manufactured IC chip needs to be marked with information such as, the chip ID, the
            maker of the chip, the first pin source, the lot code, the expiration date etc. MarkingService
            is a service used for marking functionality in Teamcenter to mark electronical components
            of semiconductor in order to guarantee accurate identification and traceability.
            

Dependencies:

            MarkingService
            


Library Reference:

Sfd0SoaSemiconductorFoundationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MarkingServiceService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ValidateAndUpdatePanelContent(self, MarkingPanelRev: Teamcenter.Soa.Client.Model.Strong.Sfd0MrkgPanelRevision, DesignType: str, MarkingPattern: str, MarkingValue: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...

