import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CancelProcessInput:
    """
    
            This structure contains the information needed to cancel the processing of an IDX
            Increment.
            
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for the ECAD or MCAD design Item."""
    DomainIdentifier: str
    """
            Unique Identifier representing a domain, one each chosen by ECAD and MCAD. The value
            could be any non-empty string less than 128 characters, the only condition being
            that the value should be consistent across all service calls made by each domain.
            This is used to establish ownership of objects published by respective domains.
            """

class CancelPublishInput:
    """
    This structure represents the input for the operation.
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for the ECAD or MCAD design ItemRevision."""
    DomainIdentifier: str
    """
            Unique Identifier representing a domain, one each chosen by ECAD and MCAD. The value
            could be any non-empty string less than 128 characters, the only condition being
            that the value should be consistent across all service calls made by each domain.
            This is used to establish ownership of objects published by respective domains.
            """

class CheckIDXInput:
    """
    This structure represents the input for the operation.
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for the ECAD or MCAD design ItemRevision."""
    DomainIdentifier: str
    """
            Unique Identifier representing a domain, one each chosen by ECAD and MCAD. The value
            could be any non-empty string less than 128 characters, the only condition being
            that the value should be consistent across all service calls made by each domain.
            This is used to establish ownership of objects published by respective domains.
            """

class CheckIDXOutput:
    """
    
            Structure containing the logical values to indicate whether there is an Eda0IDXBaseline
            or an Eda0IDXIncrement or an Eda0IDXResponse available to be processed
            by the caller.
            
    """
    def __init__(self, ) -> None: ...
    IsIDXBaselineAvailableToProcess: bool
    """
            If true, Teamcenter contains an Eda0IDXBaseline to be downloaded by the caller,
            for the input design ItemRevision.
            """
    IsIDXIncrementAvailableToProcess: bool
    """
            If true, Teamcenter contains an Eda0IDXIncrement to be reviewed by the caller,
            for the input design ItemRevision.
            """
    IsIDXResponseAvailableToProcess: bool
    """
            If true, Teamcenter contains an Eda0IDXResponse to be processed by the caller,
            for the input design ItemRevision.
            """

class CheckIDXToProcessResponse:
    """
    Response containing the structure for the results returned by the SOA.
    """
    def __init__(self, ) -> None: ...
    CheckIDXOutput: CheckIDXOutput
    """Contains status for IDX availability."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains the partial errors for the operation."""

class DeleteInput:
    """
    This structure represents the input for the operation.
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for the ECAD or MCAD design ItemRevision."""
    DomainIdentifier: str
    """
            Unique Identifier representing a domain, one each chosen by ECAD and MCAD. The value
            could be any non-empty string less than 128 characters, the only condition being
            that the value should be consistent across all service calls made by each domain.
            This is used to establish ownership of objects published by respective domains.
            """

class FileInfo:
    """
    
            This structure contains the file system information of an Interdomain Design Exchange
            (IDX) file.
            
    """
    def __init__(self, ) -> None: ...
    FileName: str
    """Name of the Interdomain Design Exchange (IDX) file."""
    FileExtension: str
    """File Extension of the Interdomain Design Exchange (IDX) file."""
    FolderPath: str
    """
            File system path for the folder containing the Interdomain Design Exchange (IDX)
            file.
            """

class FileOutput:
    """
    
            This structure represents the Eda0IDX object and the File Management System
            (FMS) Read Ticket to fetch the respective IDX file from Teamcenter.
            
    """
    def __init__(self, ) -> None: ...
    IdxObject: Teamcenter.Soa.Client.Model.ModelObject
    """Eda0IDX object managed in Teamcenter."""
    ReadTicket: str
    """
            File Management System (FMS) Read Ticket which needs to be used by the calller to
            fetch the IDX file, using FMS operations.
            """

class GetCollaborationDataOutput:
    """
    Structure containing the Collaboration data objects.
    """
    def __init__(self, ) -> None: ...
    IdxBaselineInfos: list[IDXBaselineInfo]
    """
            Collection of IDXBaselineInfo, each containing a Eda0IDXBaseline object and
            the associated Eda0IDXIncrement objects.
            """
    IdxIncrementInfos: list[IDXIncrementInfo]
    """
            Collection of IDXIncrementInfo, each containing Eda0IDXIncrement object and
            the associated Eda0IDXBaseline object and Eda0IDXResponse object.
            """
    ChangeItems: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Collection of ChangeItems associated with the input design."""

class GetCollaborationDataResponse:
    """
    Structure containing the Collaboration data requested from Teamcenter.
    """
    def __init__(self, ) -> None: ...
    GetCollaborationDataOutput: GetCollaborationDataOutput
    """Collaboration data fetched from Teamcenter."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains the partial errors for the operation."""

class GetCollaborationInput:
    """
    This structure represents the input for the operation.
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for the ECAD or MCAD design ItemRevision."""
    IdxObjectType: str
    DomainIdentifier: str
    """
            Unique Identifier representing a domain, one each chosen by ECAD and MCAD. The value
            could be any non-empty string less than 128 characters, the only condition being
            that the value should be consistent across all service calls made by each domain.
            This is used to establish ownership of objects published by respective domains.
            """
    FilterCriteria: str

class IDXBaselineInfo:
    """
    
            This structure contains criteria on the basis of which the operation would return
            the matching Eda0IDXBaseline objects.
            
    """
    def __init__(self, ) -> None: ...
    IdxBaseline: FileOutput
    """FileOutput representing an Eda0IDXBaseline object."""
    AssociatedIDXIncrements: list[IDXIncrementInfo]
    """Collection of IDXIncrementInfo, each representing an Eda0IDXIncrement object."""

class IDXIncrementInfo:
    """
    
            This structure contains criteria on the basis of which the operation would return
            the matching IDX Baseline objects.
            
    """
    def __init__(self, ) -> None: ...
    IdxIncrement: FileOutput
    """FileOutput representing an Eda0IDXIncrement object."""
    AssociatedIDXBaseline: FileOutput
    """FileOutput for the Eda0IDXBaseline object, to which the idxIncrement is associated."""
    AssociatedIDXResponse: FileOutput
    """FileOutput for the Eda0IDXResponse object associated with the idxIncrement"""

class PublishIDXResponse:
    """
    Structure representing the published IDX object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the PublishIDXInput.clientId. This can be used by the caller
            to identify this data structure with the source input data.
            """
    PublishedIDX: Teamcenter.Soa.Client.Model.ModelObject
    """Eda0IDX object which is created in Teamcenter."""
    WriteTicket: str
    """
            File Management System (FMS) Write Ticket corresponding to the the IDX file passed
            in the FileInfo input. Using this Write Ticket, the caller needs to upload the IDX
            file into the publishedIDX, using FMS APIs.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Eda0IDX is added to the Created object list."""

class PublishInput:
    """
    Structure containing information about the IDX to be published to Teamcenter.
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for the ECAD or MCAD design ItemRevision."""
    DomainIdentifier: str
    """
            Unique Identifier representing a domain, one each chosen by ECAD and MCAD. The value
            could be any non-empty string less than 128 characters, the only condition being
            that the value should be consistent across all service calls made by each domain.
            This is used to establish ownership of objects published by respective domains.
            """
    IdxObjectType: str
    FileInfo: FileInfo
    """FileInfo object corresponding to the IDX object to be published."""
    Attributes: System.Collections.Hashtable
    """
            A map of  name/value (string, list of strings) pairs of property or attribute names
            with the desired values for the Eda0IDX object to be created in Teamcenter.
            The calling client is responsible for converting the different property types (int,
            float, date .etc) to a string using the appropriate toXXXString functions in the
            SOA client Property class.
            """

class RegisterIntentInput:
    """
    Structure containing information about the publish intent of the caller.
    """
    def __init__(self, ) -> None: ...
    DesignUID: str
    """Teamcenter UID for the ECAD or MCAD design ItemRevision."""
    DomainIdentifier: str
    """
            Unique Identifier representing a domain, one each chosen by ECAD and MCAD. The value
            could be any non-empty string less than 128 characters, the only condition being
            that the value should be consistent across all service calls made by each domain.
            This is used to establish ownership of objects published by respective domains.
            """
    PublishIntent: str

class EDMDCollaboration:
    """
    Interface EDMDCollaboration
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CancelProcessChange(self, CancelProcessInput: CancelProcessInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CancelPublishIntent(self, CancelPublishInput: CancelPublishInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CheckIDXToProcess(self, CheckIDXInput: CheckIDXInput) -> CheckIDXToProcessResponse: ...
    def DeleteIDX(self, DeleteInput: DeleteInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetCollaborationData(self, GetCollaborationData: GetCollaborationInput) -> GetCollaborationDataResponse: ...
    def PublishIDX(self, PublishInput: PublishInput) -> PublishIDXResponse: ...
    def RegisterPublishIntent(self, RegisterIntentInput: RegisterIntentInput) -> Teamcenter.Soa.Client.Model.ServiceData: ...

