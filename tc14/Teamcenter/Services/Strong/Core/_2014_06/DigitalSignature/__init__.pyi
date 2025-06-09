import System
import Teamcenter.Soa.Client.Model
import typing

class ApplySignaturesInputData:
    """
    This structure contains input parameters required for applyDigitalSignatures operation.Â Â Â Â 
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Target business object to which Digital Signature is to be applied."""
    EncryptedString: str
    """CMS (Cryptographic Message Syntax ) string."""

class GetSignatureMessagesOutput:
    """
    This structure contains computed signature message.
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """Target object for which signature message is computed."""
    Message: str
    """Signature message computed for the targetObject."""

class GetSignatureMessagesResponse:
    """
    
            This structure contains the output parameters of the getSignatureMessages service
            operation.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetSignatureMessagesOutput]
    """List of getSignatureMessagesOuput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            ServiceData Containing list of partial errors and details of business objects for
            which signature message computation was not successful.
            """

class VoidSignaturesInputData:
    """
    This structure contains input parameters required for voidDigitalSignatures operation.
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """business object on which digital signatures are to be voided."""
    Signatureobject: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of digital signature objects to be voided."""
    Comment: str
    """User comments (optional)."""

class DigitalSignature:
    """
    Interface DigitalSignature
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ApplySignatures(self, Input: list[ApplySignaturesInputData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation applies digital signature to a list of Business objects provided in
             the input. The operation input is a list of DigitalSignatureInput structures. Each
             structure in this list consists of details pertaining to the Business Object and
             its corresponding CMS (Cryptographic Message Syntax). Digital Signature is allowed
             to be applied on business objects for which the business object constant Fnd0AllowDigitalSignature
             is enabled.
             

Use Cases:

             To apply digital signature from RAC, the operation getSignatureMessages should first
             be called to compute the signature messages for the input business objects. This
             should be followed by a call to the SOA framework method com.teamcenter.soa.client.PKCS7.sign
             , which takes signature message as input and provides the encrypted string as output.
             The encrypted string is passed as input to the operation applyDigitalSignatures.
             Successful completion of the operation, is an indication that the digital signature
             has been applied to the input business object.
             

Teamcenter Component:

             Fnd0CoreModelSignature - Digital signature core model signature component.
             
        :param Input: 
                         A list of DigitalSignatureInput structures containing the business object and its
                         corresponding CMS ( Cryptographic Message Syntax ).
             
        :return: 
        """
        ...
    def GetSignatureMessages(self, TargetObject: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetSignatureMessagesResponse:
        """    
             This operation returns signature messages for a list of business objects. These signature
             messages are used by SOA framework method  com.teamcenter.soa.client.PKCS7.sign
             API to generate CMS string (Cryptographic Message Syntax). The operation response
             GetSignatureMessagesResponse contains details of signature messages computed for
             each of the input business objects along with the ServiceData. The attributes that
             are to be used for signature message computation are configured using the business
             object constant Fnd0DigitalSignatureAttributes and Fnd0DigitalSignatureChildObjects.
             

Teamcenter Component:

             Fnd0CoreModelSignature - Digital signature core model signature component.
             
        :param TargetObject: 
                         A list of business objects for which signature messages need to be computed.
             
        :return: 
        """
        ...
    def VoidSignatures(self, Input: list[VoidSignaturesInputData], ElectronicSignature: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation voids the selected digital signatureson a given target object.. The
             details of  the electronic signature may be obtained by calling the requisite SOA
             framework method com.teamcenter.soa.client.PKCS7.sign. ..This is provided as input
             to the voidDigitalSignatures opearation along with the other inputs. Successful completion
             of the operation, is an indication that the selected digital signature objects have
             been voided for the input business object.
             

Use Cases:

             After applying a digital signature,the object is locked for modification and users
             would not be able to modify any of the attribute values. In certain conditions, the
             current values on the object would need to be updated and the digital signature would
             need to be reapplied with the updated set of values. To achieve this, the existing
             digital signatures on the object are voided and  required values are updated . After
             all the updates are complete,  digital signature is reapplied on the object. It is
             to be noted that if all the Digital Signatures on an object are voided, then the
             object state is equivalent to not having any digital signature applied and is open
             for updates
             

Teamcenter Component:

             Fnd0CoreModelSignature - Digital signature core model signature component.
             
        :param Input: 
                         This structure contains input parameters required for voidSignatures operation.
             
        :param ElectronicSignature: 
                         An electronic signature that will be used to validate that the person requesting
                         the void operation is the one who logged in to the tcserver that will process the
                         request.
             
        :return: 
        """
        ...

