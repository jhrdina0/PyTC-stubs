import Oo1.Services.Strong.Officeonline._2017_11.OfficeOnline
import System
import Teamcenter.Soa.Client

class OfficeOnlineRestBindingStub(OfficeOnlineService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetLaunchInfo(self, Inputs: list[Oo1.Services.Strong.Officeonline._2017_11.OfficeOnline.LaunchInfoInput]) -> Oo1.Services.Strong.Officeonline._2017_11.OfficeOnline.LaunchInfoOutputResponse: ...

class OfficeOnlineService:
    """
    
            The OfficeOnline service allows clients to get or save Office Online related data.
            Specifically, there are operations to save Office Online server discovery XML information
            to Teamcenter and to get the launch url information for a microsoft document in order
            to access the Office Online server.
            

            This service supports the following use cases:
            

            Save the Office Online discovery XML information to Teamcenter
            
            Get the launch url information for a microsoft document in order to access the Office
            Online server
            


Library Reference:

Oo1SoaOfficeOnlineStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> OfficeOnlineService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetLaunchInfo(self, Inputs: list[Oo1.Services.Strong.Officeonline._2017_11.OfficeOnline.LaunchInfoInput]) -> Oo1.Services.Strong.Officeonline._2017_11.OfficeOnline.LaunchInfoOutputResponse:
        """    
             This operation retrieves the launch information for a Teamcenter Dataset that
             a client can use to access Office Online to view or edit a Microsoft document. The
             launch URL is the address to use to connect to the Office Online Server (OOS) to
             open a Microsoft Office file in Office Online.
             

             Integration with Office Online requires implementation of the Web Application Open
             Platform Interface (WOPI) protocol.  For this protocol, the OOS is called the WOPI
             client and the Teamcenter component that OOS communications with is called the WOPI
             host.  The Teamcenter WOPI host implements REST based APIs specific to the WOPI protocol
             for the Office Online WOPI client to use to work with files stored in Teamcenter.
             

Use Cases:

             A Teamcenter client finds and selects a Dataset for a Microsoft Office document
             and chooses to view or edit the document.  The client calls this operation to retrieve
             the launch URL to access Office Online to view or edit the Microsoft Office document.
             

Teamcenter Component:

             Teamcenter Office Online - Teamcenter Office Online is an integration with Microsoft
             Office Online Server.  This allows client side viewing and editing of Microsoft documents
             stored in Teamcenter without a client side installation of Microsoft Office.
             
        :param Inputs: 
                         A list of<b> LaunchInfoInput</b> structure.
             
        :return: 
        """
        ...

