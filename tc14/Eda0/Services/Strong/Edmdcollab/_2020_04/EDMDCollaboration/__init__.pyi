import Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateObjectInfo:
    """
    This structure is an input to create or update an Eda0EDMDCollaboration.
    """
    def __init__(self, ) -> None: ...
    CollabObjectUID: str
    """
            Teamcenter UID of Eda0EDMDCollaboration to be updated. Client should pass
            an empty value when a new Eda0EDMDCollaboration is to be created.
            """
    ObjectProps: System.Collections.Hashtable
    """
            A map (string, PropertyValues) of property name and values pairs that need to be
            set on the created or updated object.
            """

class CreateOrUpdateInput:
    """
    
            Structure which enables to create or update an ECAD MCAD Collaboration. The client
            can pass formation to create a Collaboration by passing in collaborationToCreateOrUpdate
            or update a Collaboration by passing the collaborationObject. The client can attach
            any object to the Collaboration using  attachObjectsToCollaboration or detach any
            object from the Collaboration using detachObjectsFromCollaboration.
            
    """
    def __init__(self, ) -> None: ...
    CollaborationToCreateOrUpdate: CreateOrUpdateObjectInfo
    """The input that has information to create or update an Eda0EDMDCollaboration."""
    AttachObjectsToCollaboration: list[ObjectAttachInfo]
    """
            A list of information about the objects that need to be attached to Eda0EDMDCollaboration.
            This would typically include any ECAD or MCAD Design Item Revision
            that would participate in the Collaboration.
            """
    DetachObjectsFromCollaboration: list[str]
    """A list of Teamcenter UID of the objects that need to be detached from the Eda0EDMDCollaboration."""

class CreateOrUpdateResponse:
    """
    Structure representing the created or updated Eda0EDMDCollaboration object.
    """
    def __init__(self, ) -> None: ...
    CollaborationObject: Teamcenter.Soa.Client.Model.ModelObject
    """Eda0EDMDCollaboration object which is created or updated in Teamcenter."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Eda0EDMDCollaboration is added to the Created or Updated object list."""

class FileOutput2:
    """
    
            This structure represents the Eda0IDX object and the File Management System (FMS)
            Read Ticket to fetch the respective IDX file from Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    IdxObject: Teamcenter.Soa.Client.Model.ModelObject
    """Eda0IDX object managed in Teamcenter."""
    IdxReadTicket: str
    """FMS read ticket of the IDX file."""
    PackageObject: Teamcenter.Soa.Client.Model.ModelObject
    """Eda03DModelsPackage object corresponding to idxObject."""
    PackageReadTicket: str
    """FMS read ticket for the components 3D models package file."""

class GetAssembly3DModelsResponse:
    """
    Structure representing the output of the operation.
    """
    def __init__(self, ) -> None: ...
    ReadTicket: str
    """
            File Management System (FMS) Ticket corresponding to the zip file containing the
            3D Model part files and the Assembly file of the PCB parent assembly context. Using
            this read ticket, the caller needs to download the zip file, using FMS APIs.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains partial errors for the operation, if any."""

class GetCollaborationDataOutput2:
    """
    Structure containing the Collaboration data objects.
    """
    def __init__(self, ) -> None: ...
    IdxBaselineInfos: list[IDXBaselineInfo2]
    """
            Collection of IDXBaselineInfo2, each containing an Eda0IDXBaseline object
            and  the associated Eda0IDXIncrement objects.
            """
    IdxIncrementInfos: list[IDXIncrementInfo2]
    """
            Collection of IDXIncrementInfo2, each containing Eda0IDXIncrement object and
            the associated Eda0IDXBaseline object and Eda0IDXResponse object.
            """
    ChangeItems: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Collection of ChangeItem associated with the input design."""

class GetCollaborationDataResponse2:
    """
    Structure containing the Collaboration data requested from Teamcenter.
    """
    def __init__(self, ) -> None: ...
    GetCollaborationDataOutput: GetCollaborationDataOutput2
    """Collaboration data fetched from Teamcenter."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains the partial errors for the operation."""

class GetCollaborationInput2:
    """
    
            This structure contains all the information for fetching data from Teamcenter for
            a design participating in ECAD MCAD Collaboration.
            
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for the ECAD or MCAD design Item."""
    IdxObjectType: str
    DomainIdentifier: str
    """
            Unique Identifier representing a domain, one each chosen by ECAD and MCAD. The value
            could be any non-empty string, the only condition being that the value should be
            consistent across all service calls made by each domain. This is used to establish
            ownership of objects published by respective domains.
            """
    FilterCriteria: str
    Include3DModelPackage: bool
    """
            If true, Components 3D Models Package file corresponding to each Eda0IDXBaseline
            or Eda0IDXIncrement would be included in  GetCollaborationDataResponse2.
            """

class IDXBaselineInfo2:
    """
    
            This structure contains criteria on the basis of which the operation would return
            the matching Eda0IDXBaseline objects.
            
    """
    def __init__(self, ) -> None: ...
    IdxBaseline: FileOutput2
    """FileOutput2 representing an Eda0IDXBaseline object."""
    AssociatedIDXIncrements: list[IDXIncrementInfo2]
    """Collection of IDXIncrementInfo2, each representing an Eda0IDXIncrement object."""

class IDXIncrementInfo2:
    """
    
            This structure contains criteria on the basis of which the operation would return
            the matching IDX Baseline objects.
            
    """
    def __init__(self, ) -> None: ...
    IdxIncrement: FileOutput2
    """FileOutput2 representing an Eda0IDXIncrement object."""
    AssociatedIDXBaseline: FileOutput2
    """FileOutput2 for the Eda0IDXBaseline object, to which the idxIncrement is associated."""
    AssociatedIDXResponse: FileOutput2
    """FileOutput2 for the Eda0IDXResponse object associated with the idxIncrement."""

class ObjectAttachInfo:
    """
    
            This structure is an input to specify the objects which need to be attached to an
            Eda0EDMDCollaboration.
            
    """
    def __init__(self, ) -> None: ...
    ObjectUID: str
    """Teamcenter UID of the object to be attached to Eda0EDMDCollaboration."""
    RelationName: str
    """
            The relation to be used to associate the object with Eda0EDMDCollaboration.
            If this is not provided, then the relation type is determined using the preference
            <Primary>_<Secondary>_default_relation. For example, if relateToObject
            is of type ItemRevision and boName is DirectModel then preference ItemRevision_DirectModel_default_relation
            used. If not found, then ItemRevision_default_relation will be searched for and used.
            """

class PublishAssemblyInput:
    """
    
            Structure containing information about the PCB parent assembly BOM context to be
            published to Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for MCAD design ItemRevision."""
    FileInfo: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.FileInfo
    """FileInfo object corresponding to the assy file to be published."""
    BomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of BOMLine objects of the PCB parent assembly BOM that MCAD  tool needs to publish."""

class PublishAssemblyResponse:
    """
    Structure representing the output of the operation.
    """
    def __init__(self, ) -> None: ...
    DatasetUid: str
    """The uid of the dataset to which the Assembly file needs to be uploaded."""
    WriteTicket: str
    """
            File Management System (FMS) Write Ticket corresponding to the Assembly file passed
            in the FileInfo input. Using this Write Ticket, the caller needs to upload the Assembly
            file to the dataset, using FMS APIs.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Eda0AssemblyFile and VisStructureContext are added to the Created object list."""

class PublishIDXResponse2:
    """
    Structure representing the published IDX object.
    """
    def __init__(self, ) -> None: ...
    PublishedIDX: Teamcenter.Soa.Client.Model.ModelObject
    """Eda0IDX object which is created in Teamcenter."""
    PackageFile: Teamcenter.Soa.Client.Model.ModelObject
    """Eda03DModelsPackage object which is created in Teamcenter."""
    IdxWriteTicket: str
    """FMS Write Ticket corresponding to the the IDX file passed in the idxFileInfo input."""
    PackageWriteTicket: str
    """
            FMS Write Ticket corresponding to the the IDX file passed in the packageFileInfo
            input.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Eda0IDX and Eda03DModelsPackage are added to the Created object
            list.
            """

class PublishInput2:
    """
    Structure containing information about the IDX to be published to Teamcenter.
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for the ECAD or MCAD design Item."""
    DomainIdentifier: str
    """
            Unique Identifier representing a domain, one each chosen by ECAD and MCAD. The value
            could be any non-empty string, the only condition being that the value should be
            consistent across all service calls made by each domain. This is used to establish
            ownership of objects published by respective domains.
            """
    IdxObjectType: str
    IdxFileInfo: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.FileInfo
    """FileInfo of the IDX object to be published."""
    PackageFileInfo: Eda0.Services.Strong.Edmdcollab._2020_01.EDMDCollaboration.FileInfo
    """
            FileInfo of the components 3D Models Package file corresponding to the IDX object
            to be published.
            """
    Attributes: System.Collections.Hashtable
    """
            A map of  name/value (string, list of strings) pairs of property or attribute names
            with the desired values for the Eda0IDX object to be created in Teamcenter.
            The calling client is responsible for converting the different property types (int,
            float, date .etc) to a string using the appropriate toXXXString functions in the
            SOA client Property class.
            """

class EDMDCollaboration:
    """
    Interface EDMDCollaboration
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateCollaboration(self, CreateOrUpdateInput: CreateOrUpdateInput) -> CreateOrUpdateResponse: ...
    def GetAssemblyContext3DModels(self, DesignUID: str) -> GetAssembly3DModelsResponse: ...
    def GetCollaborationData2(self, GetCollaborationInput: GetCollaborationInput2) -> GetCollaborationDataResponse2: ...
    def PublishAssemblyContext(self, PublishAssemblyInput: PublishAssemblyInput) -> PublishAssemblyResponse: ...
    def PublishIDX2(self, PublishInput: PublishInput2) -> PublishIDXResponse2:
        """    
             This operation creates a new Eda0IDX business object in Teamcenter for a Design
             participating in an ECAD MCAD Collaboration. Optionally, it also allows creation
             of a package containing 3D Model files corresponding to Printed Circuit Board components
             contained within an Eda0IDXBaseline or Eda0IDXIncrement.
             

             ECAD MCAD Collaboration is a process of exchange of incremental design changes between
             ECAD and MCAD engineers, during the design process for a Printed Circuit Board (PCB).
             The IDX file format is a STEP (STandard for the Exchange of Product
             model data) based neutral format that stores electromechanical data using an XML
             schema.
             

             In Teamcenter, IDX files for an ECAD MCAD Collaboration are managed as Eda0IDXBaseline,
             Eda0IDXIncrement and Eda0IDXResponse objects, which are types of Eda0IDX
             business object.
             

Eda0IDX represents any Teamcenter managed IDX object.
             

Eda0IDXBaseline represents the IDX Baseline object in ECAD MCAD Collaboration.
             The IDX Baseline object represents an IDX file, in which the board outline and the
             complete geometry information of the PCB is captured. The IDX Baseline is the agreed
             state of a PCB design, starting from which the ECAD and MCAD tools would make incremental
             changes and collaborate with each other in the PCB development process.
             

Eda0IDXIncrement represents an IDX (Interdomain Design Exchange) file which
             contains the incremental changes in a PCB layout, during the collaboration between
             ECAD and MCAD, as a part of PCB development process.
             

Eda0IDXResponse represents an IDX (Interdomain Design Exchange) file, which
             is created as a part of ECAD or MCAD tool reviewing and accepting or rejecting the
             proposed incremental changes. The IDX Response file is then imported by the tool
             which initiated the proposal, to bring the design in sync in both ECAD and MCAD tools.
             

Use Cases:

             Use Case 1:
             

ECAD or the MCAD designer while working on the PCB design, use the
             export IDX Baseline functionality within the respective tool, to create Eda0IDXBaseline
             object in Teamcenter. Optionally ECAD designer may also publish the Components 3D
             Model Package file along with Eda0IDXBaseline.
             
The preceding Eda0IDXBaseline and any Eda0IDXIncrement
             business objects published by the calling domain, if existing, are marked as obsoleted
             in Teamcenter.
             



             Use Case 2:
             

ECAD or the MCAD designer while working on the PCB design, use the
             export IDX Increment functionality within the respective tool, to create a Eda0IDXIncrement
             object in Teamcenter. Optionally ECAD designer may also publish the Components 3D
             Model Package file along with Eda0IDXIncrement.
             



             Use Case 3:
             

ECAD or the MCAD designer while working on the PCB design in their
             respective tool, imports an IDX Increment for reviewing the changes.
             
The designer reviews the changes contained within the IDX file, accepts
             or rejects each change and publishes an IDX Response to create an Eda0IDXResponse
             object in Teamcenter.
             



Teamcenter Component:

             EDA Server Support - This feature extends the Teamcenter data model to support Teamcenter
             Electronic Design Automation integrations that allow ECAD designers to log on to
             Teamcenter and open, save, request parts, and check in and check out PCB design data.
             
        :param PublishInput: 
                         This structure represents the input to the operation.
             
        :return: 
        """
        ...

