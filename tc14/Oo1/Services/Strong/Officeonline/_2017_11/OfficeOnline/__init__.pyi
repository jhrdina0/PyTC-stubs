import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class LaunchInfoInput:
    """
    
            The structure contains the needed information to retrieve the launch URL for a Teamcenter
            Dataset for access Office Online Server.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure.
            """
    Obj: Teamcenter.Soa.Client.Model.ModelObject
    """
            The Teamcenter BusinessObject. The BusinessObject need to resolve to
            an Office dataset type such as MSWordX.
            """
    Action: str
    """The WOPI action name. The action name is defined by WOPI protocol."""
    ExtraInfo: System.Collections.Hashtable
    """
            A map (string, string) for extra name value pair information. This is intended for
            future use.
            """

class LaunchInfoOutput:
    """
    
            The structure contains the information needed to access the Dataset from the
            Office Online Server.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the LaunchInfoInput.clientId. This can be used by
            the caller to indentify this data structure with the source input data.
            """
    OosUrlString: str
    """The launch URL to access the Dataset from the Office Online Server."""
    AccessToken: str
    """Teamcenter access token."""
    AccessTtl: str
    """Teamcenter access token time to live."""

class LaunchInfoOutputResponse:
    """
    The structure contains a list of LaunchInfoOutput and the Service Data.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[LaunchInfoOutput]
    """A list of LaunchInfoOutput."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class OfficeOnline:
    """
    Interface OfficeOnline
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLaunchInfo(self, Inputs: list[LaunchInfoInput]) -> LaunchInfoOutputResponse:
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

