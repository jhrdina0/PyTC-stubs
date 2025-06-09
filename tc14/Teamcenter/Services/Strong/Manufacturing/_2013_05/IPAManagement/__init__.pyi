import System
import Teamcenter.Soa.Client.Model
import typing

class AppPathRootWindowDetails:
    """
    The apperance path root window and its type.
    """
    def __init__(self, ) -> None: ...
    ProductWindowAppPathRoot: Teamcenter.Soa.Client.Model.ModelObject
    """The appearance path root window."""
    AppPathRootType: Teamcenter.Soa.Client.Model.ModelObject
    """The type of appearance path root window."""

class FileTicketDetails:
    """
    The details of the file ticket.
    """
    def __init__(self, ) -> None: ...
    FileName: str
    """The name of the log file."""
    FileTicket: str
    """The file management server ticket of the file."""

class CleanIPATreeResponse:
    """
    
ServiceData element, appearance path root window along with its type which was
deleted
during the operation and the log file details and its ticket. The deleted
occurrence
groups from the process structure and deleted appearance path root of the
product
structure is added to the Deleted object list of ServiceData. Partial errors
occurred
in the operation are added to ServiceData.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""
    AppPathRootWindows: list[AppPathRootWindowDetails]
    """
            List of appearance windows deleted by the operation. These windows corressponds to
            product structures consumed in the process strcuture to be cleaned.
            """
    LogFileTicket: FileTicketDetails
    """The details of the log file ticket."""

class EffectivityDetails:
    """
    
The effectivity details for the IPA generation like end item, its revision,
range
and/or unit of effectivity.
    """
    def __init__(self, ) -> None: ...
    EffectivityEndItem: Teamcenter.Soa.Client.Model.ModelObject
    """The end item of generated assembly tree to which the effectivity is associated."""
    EffectivityEndItemRev: Teamcenter.Soa.Client.Model.ModelObject
    """The end item revision of generated assembly tree to which the effectivity is associated."""
    EffectivityUnitRange: str
    """The unit range of effectivity associated with IPA generated occurrence."""
    EffectivityDateRange: str
    """The date range of effectivity associated with IPA generated occurrence."""

class ConfigDetails:
    """
    
The configuration details about the IPA generation which includes details of
process
structure, consumption types, occurrence group types and effectivity details.
    """
    def __init__(self, ) -> None: ...
    ProcessWindow: Teamcenter.Soa.Client.Model.ModelObject
    """The window of the process structure in which items are consumed from a product structure."""
    IpaName: str
    """The name of the IPA to be processed."""
    OccGrpType: str
    """The type of occurrence group to be generated for the assembly tree."""
    ProcessTypes: list[str]
    """List of process types for which an assembly tree is generated."""
    ConsumptionOccTypes: list[str]
    """List of consumed occurrence types considered for generation of the assembly tree."""
    EffectivityDetails: EffectivityDetails
    """
            The effectivity details for the IPA generation like end item, its revision, range
            and/or unit of effectivity.
            """

class EmailNotificationDetails:
    """
    
The e-mail notification details like recipients of the e-mail, subject and
content
of the message.
    """
    def __init__(self, ) -> None: ...
    LogFileName: str
    """
            This is name of the report on errors and problems during the operation. This report
            contains all the problems or conflicts that occurred during generate/update that
            need to be addressed, for example, missing targets, locked nodes, or checked out
            nodes.
            
            This file is saved as an attachment on the top-level process element on which the
            assembly tree was generated/updated.
            
"""
    IsLogFileNeeded: bool
    """This flag is used to create a run-time statistic log for IPA generation."""
    MailToReceivers: list[str]
    """List of recipients to be added in 'To' list of the e-mail notification."""
    MailCcReceivers: list[str]
    """List of recipients to be added in 'Cc' list of the e-mail notification."""
    MailSubject: str
    """The subject of the e-mail notification."""
    MailMessage: str
    """The message content of the e-mail notification."""

class GenerateIPATreeResponse:
    """
    
ServiceData element, appearance path root window along with its type which was
generated
during the operation and the log file details and its ticket. The newly created
occurrence
groups from the process strcture and appearance path root of the product
strcuture
is added to the Created object list of ServiceData. Partial errors occurred in
the
operation are added to ServiceData.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""
    ProductWindowAppPathRoot: Teamcenter.Soa.Client.Model.ModelObject
    """The appearance window which was created."""
    AppPathRootType: Teamcenter.Soa.Client.Model.ModelObject
    """The type of appearance window which was created."""
    LogFileTicket: FileTicketDetails
    """The details of the log file ticket."""

class IPAExistResponse:
    """
    
ServiceData element, flag indicating whether IPA tree exists for the process
structure
and ticket of configuration file if the IPA tree exists for the structure.
Partial
errors occurred in Teamcenter internal APIs during the operation are returned in
ServiceData.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""
    IsIPAExist: bool
    """The flag indicating whether IPA tree exists for the process structure."""
    ConfigFileTicket: FileTicketDetails
    """
            The ticket of configuration file. This file is saved as an attachment on the top-level
            process element on which the assembly tree was generated/updated. This file contains
            information about all the configured product structures consumed in the process structure.
            """

class IPATreeInput:
    """
    
All the details for IPA generation that includes the name of the IPA, process
types,
consumption types, occurrence group type, effectivity, email notification
details
etc.
    """
    def __init__(self, ) -> None: ...
    ConfigDetails: ConfigDetails
    """
            The configuration details about the IPA generation which includes details of process
            structure, consumption types, occurrence group types and effectivity details.
            """
    EmailDetails: EmailNotificationDetails
    """
            The e-mail notification details like recipients of the e-mail, subject and content
            of the message.
            """

class LocalUpdateIPATreeResponse:
    """
    
ServiceData element, the log file name and its ticket. The updated occurrence
groups
from the process structure and appearance path root of the product structure is
added
to the Updated object list of ServiceData. Partial errors occurred in the
operation
are added to ServiceData.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""
    LogFileticket: FileTicketDetails
    """The details about the log file ticket."""

class IPAManagement:
    """
    Interface IPAManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CleanIPATree(self, ProcessWindow: Teamcenter.Soa.Client.Model.ModelObject, ForceCleanAll: bool) -> CleanIPATreeResponse:
        """    
             This operation removes the In-Process Assembly (IPA) occurrences from the process
             structure and deletes the IPA occurrence group from product structure. This operation
             cleans only the IPA which has been configured by current configuration rule and configuring
             structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param ProcessWindow: 
                         Window of the process structure containing the IPA that is to be deleted.
             
        :param ForceCleanAll: 
                         This flag is used to forcefully delete all IPAs. This functionality is not supported
                         currently.
             
        :return: 515182:Â Â Â Â Â Â Â Â Could not find the log file.
        """
        ...
    def DoesIPAExist(self, ProcessWindow: Teamcenter.Soa.Client.Model.ModelObject) -> IPAExistResponse:
        """    
             This operation checks if an In-Process Assembly tree exists for a process structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param ProcessWindow: 
                         Window of the process structure.
             
        :return: 
        """
        ...
    def GenerateIPATree(self, IpaInput: IPATreeInput) -> GenerateIPATreeResponse:
        """    
             An In-Process Assembly (IPA) is an aggregation of incoming parts into stations. IPA
             is generated based on consumed item(s) from a product structure in a process structure.
             Teamcenter creates a tree structure representing the IPA by traversing the process
             structure and collecting IPAs from previous process elements and adding the selected
             line's consumed objects.
             

             The IPA is stored as an occurrence group and is displayed in a separate tab beside
             the base view of the root product.
             

             When the assembly tree is created by the operation, it places a configuration file
             as an attachment on the process for which the IPA is generated.
             

             Teamcenter sends an e-mail notification to the recipients specified in the input
             after completion of the operation. This e-mail contains information about the IPA
             creation, as well as log files that are created during generation of the IPA.
             


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param IpaInput: 
                         All the details for IPA generation that includes the name of the IPA, process types,
                         consumption types, occurrence group type, effectivity, email notification details
                         etc.
             
        :return: 
        """
        ...
    def LocalUpdateIPATree(self, ProcessLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> LocalUpdateIPATreeResponse:
        """    
             This operation is used to perform a local update on an In-Process Assembly (IPA)
             tree. Local update changes the IPA on which the operation is invoked. If necessary,
             it also updates the occurrence pointing to this in-process assembly in the process
             structure.
             

             If the IPA has not been created and attached to the matching process, Teamcenter
             also changes the matching process and adds the incoming IPA as MEWorkpiece. This
             happens only if a process whose type is in the process types list of the configuration
             details during the initial IPA generation.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param ProcessLines: 
                         List of processes in the process structure on which local update requested.
             
        :return: 515182:Â Â Â Â Â Â Â Â Could not find the log file.
        """
        ...
    def UpdateIPATree(self, IpaInput: IPATreeInput) -> GenerateIPATreeResponse:
        """    
             This operation is used to update an In-Process Assembly (IPA) tree that already exists,
             when a process structure is changed. The options set at creation of the assembly
             tree may be changed for example process types, consumed occurrence types, name of
             the report on errors and problems, e-mail notification configuration.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param IpaInput: 
                         All the details for updating IPA that includes the name of the IPA, process types,
                         consumption types, occurrence group type, effectivity, email notification details
                         etc.
             
        :return: 
        """
        ...

