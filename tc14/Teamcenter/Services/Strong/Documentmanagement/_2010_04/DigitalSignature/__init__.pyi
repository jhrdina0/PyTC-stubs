import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DigitalSignSaveInput:
    """
    The digitalSigningSave input structure.
    """
    def __init__(self, ) -> None: ...
    BaseObj: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The Dataset object that contains the named reference file to be signed.  This
            is required.
            """
    SignedFileTicket: str
    """The FMS file ticket for uploading the signed file.  This is required."""
    CreateToolName: str
    """The tool name that is used to sign the file.  This is required."""
    ValidSignature: bool
    """
            If this is set to true, then the signature is valid; otherwise, it is not.  If the
            signing tool does not declare the signature is valid, then the base dataset will
            not be checkin.
            """
    UserNameWhoSign: str
    """The Teamcenter user name that completed the digitally sign operation."""
    SignTime: str
    """The timestamp of the digital signature in the signing tool."""

class DigtalSigningSaveResponse:
    """
    Digital signing save operation response
    """
    def __init__(self, ) -> None: ...
    BasedDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """If the Dataset is updated successfully, then the Dataset is returned."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The partial error list if there is any system errors."""

class DigitalSignature:
    """
    Interface DigitalSignature
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DigitalSigningSave(self, SaveInput: DigitalSignSaveInput) -> DigtalSigningSaveResponse:
        """    
             The digitalSigningSave function will update an existing dataset that has the name
             referenced uploaded signed file.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param SaveInput: 
                         Digital signing input
             
        :return: Return based dataset if successful.
        """
        ...

