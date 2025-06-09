import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MetaDataStampInputInfo:
    """
    
This structure holds information about the objects to stamp along with the
stamping
context within which the stamped objects reside.
    """
    def __init__(self, ) -> None: ...
    MetaStampInfoId: str
    """
            Client supplied unique identifier string that helps the client map the input to the
            MetaDataStampOutput.
            """
    StampingContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            A stamping context BusinessObject within which the stamped objects reside.  The root
            line occurrence object of a structure, or an ItemRevision object that owns
            a DirectModel dataset are two examples of expected inputs for this argument,
            but intended to be general (could be any business object).
            """
    StampedObjects: list[StampedObjectInfo]
    """
            A list of any POM_objects on which the metadatastamp file is to be generated. POM_objects
            like Fnd0ModelViewProxy and Datasets like SnapshotViewData are two
            examples of expected input for this argument, but intended to be general ( could
            be any POM_object ).
            """

class MetaDataStampOutput:
    """
    This structure contains the list of StampedObjectTicketInfo structures.
    """
    def __init__(self, ) -> None: ...
    StampObjectTickets: list[StampedObjectTicketInfo]
    """A list of StampedObjectTicketInfo structures."""

class MetaDataStampOutputResponse:
    """
    
This structure is used to return information from the
getMetaDataStampWithContext
operation. This structure holds information about serviceData and
MetaDataStampOutputMap.
The serviceData may contain information relevant to error messages, which are
then
associated to metaStampInfoId identifier and added to the error stack. The map,
MetaDataStampOutputMap,
contains information mapping the metaStampInfoId identifier to the
MetaDataStampOutput
struct, containing information about the tickets of the stamped object.
    """
    def __init__(self, ) -> None: ...
    MetaDataStampOutputInfo: System.Collections.Hashtable
    """
            A map (string/MetaDataStampOutput) associating the unique metaStampInfoId identifier
            with the correct MetaDataStampOutput structure, containing tickets for the stamped
            objects for the given context object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failure will be returned with error messages in the serviceData list of partial
            errors.
            """

class StampedObjectInfo:
    """
    This structure holds information of the stamped object along with its unique
identifier.
    """
    def __init__(self, ) -> None: ...
    UniqueStampObjectId: str
    """
            Client supplied unique identifier string that helps the client map the returned ticket
            to the stamped object.
            """
    StampedObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Any POM_object on which the metadatastamp file is to be generated. POM_objects like
            Fnd0ModelViewProxy and Datasets like SnapshotViewData are two examples
            of expected input for this argument, but intended to be general ( could be any POM_object
            ).
            """

class StampedObjectTicketInfo:
    """
    
This structure holds information of the ticket generated for the stamped object.
Failures to get ticket for the stamped object maybe recorded as partial errors
in
the error stack and associated to uniqueStampObjectId identifier.
    """
    def __init__(self, ) -> None: ...
    UniqueStampObjectId: str
    """
            Client supplied unique identifier string that helps the client map the ticket to
            the stamped object.
            """
    MdsFileTicket: str
    """
            The FMS transient read ticket generated for the stamped object. The file will be
            placed in the transient file volume and the caller will need to download it from
            there with the ticket sent by the service.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMetaDataStampWithContext(self, MetaDataStampInfos: list[MetaDataStampInputInfo]) -> MetaDataStampOutputResponse:
        """    
             This operation retrieves metadata stamp files for Teamcenter objects based on the
             context within which these objects are being displayed.  For example, when a user
             prints a model view, the stamp will vary based on the context within which this model
             view is printed.  Printing the model view in owning model context provides one stamp,
             while printing the same view from within a disclosure context produces another stamp.
             

             The metadata stamp is generated based on the list of objects and the context of those
             objects using the metaDataStampInfos list. The transient ticket for the generated
             *.mds file is returned. The ticket can then be used to retrieve the file using a
             FMS method like FccProxy::downloadFiles.
             

             The Teamcenter default implementation uses a Metadatastamp template containing an
             MDS file with Teamcenter property names and default values. The Teamcenter site preference
             MetaDataStamp_template is used to find the item where the template files is stored.
             This file is processed and each Attribute specified will be replaced with the matching
             object property values if found. The output mds file will be written to the transient
             volume and the transient ticket of the file is sent to client in the response data.
             The customization hook provided with this interface may wish to use the same template
             mds file as a starting point.
             

             This operation requires the Teamcenter File Management System (FMS) to be installed
             (including FCC and transient volumes).
             

Use Cases:

             This method is called by visualization when integrating with Teamcenter for printing
             objects like Fnd0ModelViewProxy and SnaphotViewData datasets that are loaded into
             some higher level product context. The user loads a configured product structure,
             or some high level object that sets context in Teamcenter. Within this structure
             or context, the user finds objects they wish to print, and invokes a print action,
             The stamping context is the higher level context within which the stamping metadata
             is retrieved from (e.g. the root node of the product structure), and the stamped
             objects are the individual objects that are to be printed (e.g. model views or product
             Views). Stamp files (tickets) are returned to the caller, and these files are used
             by visualization to place metadata markings on views printed. The stamp file represents
             a metadata stamp overlay on top of the printed image and often contains control information
             for printed detailed design data.
             

             The MDS file created by this service can also be used by the VisView Convert and
             Print utilities.
             

             This service may also be useful for customizations that leverage Siemens Embedded
             visualization toolkits, and thus it is a public service.
             

Teamcenter Component:

             Teamcenter Visualization - Application to allow view and markup of multicad product
             structure that has a jt representation.
             
        :param MetaDataStampInfos: 
                         A list of MetaStampInputInfo structures. Each of the structure elements is identified
                         by a unique identifier enabling the caller to map the input to the output. The input
                         structure holds information including the list of objects to stamps and the stamping
                         context object.
             
        :return: 
        """
        ...

