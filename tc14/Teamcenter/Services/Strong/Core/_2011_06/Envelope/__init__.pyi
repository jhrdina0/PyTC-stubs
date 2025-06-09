import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Envelope:
    """
    Interface Envelope
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SendAndDeleteEnvelopes(self, Envelopes: list[Teamcenter.Soa.Client.Model.Strong.Envelope]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sends mails to the recipients of each Envelope business object
             in envelopes. All the envelopes passed to this operation are deleted after they are
             processed, even if the processing is not successful. Each Envelope business
             object contains mail information such as subject, body, recipients, and attachments.
             Recipients can be Teamcenter users, groups and address lists, or, external email
             addresses. Teamcenter users receive envelopes in their Teamcenter Mailbox and also
             as emails if Mail_OSMail_activated site preference is set to true.To send the emails, the site preference Mail_server_name
             should be properly configured. Any errors that occur while sending envelopes are
             returned as partial errors in ServiceData.
             

Use Cases:

             Use case 1: Send envelopes to Teamcenter users

             You can send envelopes to the Mailbox of Teamcenter users by specifying the users
             as recipients on Envelope business objects.  Also, email messages can be sent to
             Teamcenter users if Mail_OSMail_activated site preference is set to true.
             

             User case 2: Send emails to external email addresses

             Email messages can be sent to external users by specifying their email addresses
             as recipients on Envelope business objects.
             


Teamcenter Component:

             Mail - Sends SMTP (Simple Mail Transfer Protocol) e-mail to Teamcenter users.Uses
             platform-independent utility to send e-mail on both UNIX and Windows platforms.
             
        :param Envelopes: 
                         The list of <b>Envelope</b> business objects to be sent.
             
        :return: 
        """
        ...

