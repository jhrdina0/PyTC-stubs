import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SnapshotViewInfo:
    """
    
            The data to create issue scene 3D snapshot view dataset. This interface was defined
            before visualization SOA was available and it exposes snapshot view data model to
            Issue Management service client. It is recommended to create snapshot view dataset
            by calling visualization service and provide the dataset as object to be attached
            under issue report revision with IsM0SnapshotBeforeFix or IsM0SnapshotAfterFix
            relation.
            
    """
    def __init__(self, ) -> None: ...
    RelationToIssue: str
    """Relation name from issue report revision to this snapshot view dataset."""
    ExistingSnapshot: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            Existing snapshot view dataset to be updated. Should be NULL when creating a new
            snapshot dataset.
            """
    SceneName: str
    """Snapshot view dataset name. This serves as issue scene name."""
    ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """Assembly configuration context object."""
    TopNodeBVR: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    """Top assembly node BVR."""
    RefAndFiles: list[NamedReferenceAndFile]
    """
            Snapshot files and named reference names to create 3D snapshot view dataset. Client
            needs to provide thumbnail image, view file (plmxml) and structure file (xml) to
            create a valid snapshot view dataset.
            """

class CreateIssueInfo:
    """
    
            Inputs to create a new issue object. The issue title is the issue item name. The
            issue description is the issue item description.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    Id: str
    """Issue report item ID. Can be auto generated."""
    Type: str
    """Issue report item type. Must be IssueReport or a sub class from IssueReport."""
    Title: str
    """Issue report item name."""
    RevId: str
    """Issue report revision ID. Can be auto generated."""
    Desc: str
    """Issue report item description. This is a short description when an issue is captured."""
    Attributes: list[ExtendedAttribute]
    """Issue report revision attributes. The structure supports multiple values for an attribute."""
    RelationData: list[RelationshipData]
    """
            Attachment object, relation from issue report revision to the attachment object,
            and operation to add or remove the attachment object. Use this structure to update
            issue report attachments.
            """
    ReviewSetting: SnapshotViewInfo
    """
            Issue scene information. This structure contains data to create a product view dataset
            (snapshot view dataset). This interface was defined before the visualization service
            was available and it exposes the product view dataset data model to the client code.
            When possible, it is recommended to leverage the visualization service to create
            the product view dataet and use the relationData to attach the dataset to
            the issue report revision.
            """
    GeneralDatasets: list[DatasetInput]
    """List of information to create or update datasets."""
    CapturedImageFile: str
    """Issue before fix image file name."""
    CapturedImageFileTicket: str
    """Issue before fix image file upload ticket."""

class CreateIssueItemsResponse:
    """
    Create issue response.
    """
    def __init__(self, ) -> None: ...
    Output: list[IssueItemsOutput]
    """Array of issue report revisions created."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data. Teamcenter error stack content will be returned to client when error
            occurs.
            """

class DatasetInfo:
    """
    Create dataset info.
    """
    def __init__(self, ) -> None: ...
    Tool: str
    """Dataset tool."""
    Type: str
    """Dataset type."""
    Name: str
    """Dataset name."""
    Description: str
    """Dataset description."""

class NamedReferenceAndFile:
    """
    File and named reference pair to create a dataset.
    """
    def __init__(self, ) -> None: ...
    FileType: str
    """File type (text or binary). Optional."""
    FileName: str
    """File name."""
    FileTicket: str
    """File upload ticket obtained by calling FMS client utility."""
    RefName: str
    """Named reference name in dataset."""

class DatasetInput:
    """
    
            Info to create or update a dataset and relation to attach the dataset to issue report
            revision.
            
    """
    def __init__(self, ) -> None: ...
    DsInfo: DatasetInfo
    """Dataset info. Ignored when updating existing dataset."""
    FileInfo: NamedReferenceAndFile
    """Data file info."""
    ExistingDS: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Existing dataset to be updated. NULL to create a new dataset."""
    RelationToContainer: str
    """Relation name from issue revision to dataset."""

class ExtendedAttribute:
    """
    
            This structure contains issue report revision attribute name versus attribute values
            pairs to update an issue report revision.
            
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Issue report revision attribute name."""
    Values: list[str]
    """
            Issue report revision attribute values. The structure supports multiple values for
            an issue report revision attribute. Attribute value is in char string (C++) or String
            (Java/C#). Teamcenter object can be passed as UID string (obtained from POM_tag_to_string()).
            Numbers (integer or long or double) can be passed in as string as well. Logical value
            is passed in as TRUE or FALSE string.
            """

class IssueItemsOutput:
    """
    
            It contains the newly created issue report item and revision, snapshot dataset or
            general datasets.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    ChangeItem: Teamcenter.Soa.Client.Model.Strong.ChangeItem
    """Issue report item created."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision
    """Issue report revision created."""
    ViewDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Snapshot view dataset created."""
    GeneralDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """General attachment datasets created."""

class RelationshipData:
    """
    
            It contains the attachments (existing Teamcenter objects), relation that the attachments
            are to be attached to (or de attached from) issue report revision. This is the way
            that client updates issue context data.
            
    """
    def __init__(self, ) -> None: ...
    Tags: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Attachment objects. Can be any Teamcenter Workspace Objects."""
    RelationName: str
    """Relation name (from issue revision to attachment)."""
    Operation: str
    """Add or REMOVE."""

class ReviewIssueInput:
    """
    Deprecated.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    TheIssue: Teamcenter.Soa.Client.Model.ModelObject
    """The target issue object."""
    ReviewIssueDecision: str
    """Review issue decision."""
    PerformSignoffDecision: str
    """Workflow perform signoff decision."""
    AssignedUser: Teamcenter.Soa.Client.Model.Strong.User
    """The Teamcenter user who is responsible to fix the issue."""
    Comment: str
    """Comments."""

class ReviewIssueOutput:
    """
    Deprecated.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    TheIssue: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision
    """Updated issue object."""

class ReviewIssueResp:
    """
    Deprecated.
    """
    def __init__(self, ) -> None: ...
    Resp: list[ReviewIssueOutput]
    """List of review issue outputs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """SOA service data."""

class UpdateIssueInfo:
    """
    Data and files to update an issue.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    ExistingIssueRev: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision
    """Existing issue report revision to be updated."""
    Attributes: list[ExtendedAttribute]
    """Attributes and values."""
    RelationData: list[RelationshipData]
    """Attachments to be updated."""
    ReviewSetting: SnapshotViewInfo
    """Issue scene snapshot."""
    GeneralDatasets: list[DatasetInput]
    """General dataset attachments."""
    FixedImageFile: str
    """Image file name when issue is fixed."""
    FixedImageFileTicket: str
    """Image file ticket when issue is fixed."""

class UpdateIssueRevsResponse:
    """
    Update issue report revision response.
    """
    def __init__(self, ) -> None: ...
    Output: list[UpdateRevisionOutput]
    """Array of update issue report revisions."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data. Teamcenter error stack content will be returned when error occurs."""

class UpdateRevisionOutput:
    """
    Update issue report revision output.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    ItemRev: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision
    """Issue report revision updated."""
    ViewDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """Snapshot view dataset updated."""
    GeneralDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """General datasets updated."""

class IssueManagement:
    """
    Interface IssueManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateIssueItems(self, Inputs: list[CreateIssueInfo]) -> CreateIssueItemsResponse:
        """    
             A client calls this operation to create issue reports. An issue report contains two
             categories of data to describe a problem: issue metadata which can be issue report
             ID, title, description, severity level, disposition and so on; issue context data
             which can be problem parts, issue scene setting (product view), view stat data, check
             / analysis logs, images, screenshots and documentation. Issue report metadata is
             managed as issue report item and revision attributes (mostly issue report revision
             attributes) while issue report context data is managed as attachments to issue report
             revisions under different pseudo-folders (relations). Customers can customize issue
             report data model to manage issue metadata and context data to better fit different
             issue management business process models. In the OOTB configuration, problem parts
             are attached under the CMHasProblemItem relation, and issue images are attached
             under the ImageBeforeFix or ImageAfterFix relation. Product view datasets
             (snapshots) are attached under the IsM0SnapshotBeforeFix or IsM0SnapshotAfterFix
             relation. General datasets can be attached under the CMReferences relation.
             
             Issue report type, title, and description are required inputs to create new issue
             report. When the issue report ID is not provided, the system generates a unique ID
             according to the naming convention. When an issue report ID is provided and there
             is an existing issue report with the same ID from Teamcenter, a new revision will
             be created and populated with the provided issue metadata and issue context data.
             This operation does not copy or reference any attributes or attached objects from
             the existing issue report revision to the newly created issue report revision.
             
             The client must call the Teamcenter FMS utility to upload the file and provide the
             upload ticket along with the file name, dataset type, and named reference name to
             create a new dataset or update an existing dataset. It is recommended that the client
             application calls Visualization service to create and save a product view (snapshot
             view) dataset and provide the product view dataset under the relationData
             when creating or updating the issue report.
             


Use Cases:

             The NX Check-Mate application integrates with Teamcenter Issue Management to log
             an issue report when the part fails a Check-Mate check. The client provides an issue
             title (that is related to the Check-Mate checker name), a description (that is related
             to the Check-Mate checker description), a log file as a general dataset to be attached
             under the CMReferences relation, and a part that is to be attached under the
             CMHasProblemItem relation. The client can also capture the current assembly
             / part scene as a product view dataset and attachs the dataset under the IsM0SnapshotBeforeFix
             relation. In this use case, a log file is provided as generalDatasets, and
             an issue scene dataset is provided as a relationData object.
             

Teamcenter Component:

             Issue Management - Teamcenter Issue Management is an application that allows users
             to capture issue, share issue data and collaborate on the business process to resolve
             issue in product life management.
             
        :param Inputs: 
                         Inputs to create issues.
             
        :return: Array of created issue report revisions.
        """
        ...
    def ReviewIssues(self, Inputs: list[ReviewIssueInput]) -> ReviewIssueResp:
        """    
             This operation/function provides a mechanism for issue review board members to cast
             a vote on issue review and optionally perform workflow signoff task. The timing to
             call this SOA is when issue management workflow process perform signoff task is started.
             Each board member can cast one vote whether to defer or reject or approve an issue
             (so the issue must be assigned and fixed) or approve issue fix or re-open issue or
             close issue. Issue review board members are selected perform signoff users from issue
             management workflow process review task. Only the votes from review board members
             are counted by workflow action handler EPM-update-issue-status. Votes from non-members
             are not counted. Final decision is rendered by simple majority of votes or a percentage
             of votes as configured in issue management workflow template. Issue status is changed
             based on final decision when review task completes. Calling this SOA function alone
             will not change issue status directly (except that a reviewer can assign an issue
             to a user). A reviewer can not change vote after his or her perform signoff task
             is completed.
             

Teamcenter Component:

             Issue Management - Teamcenter Issue Management is an application that allows users
             to capture issue, share issue data and collaborate on the business process to resolve
             issue in product life management.
             
        :param Inputs: 
                         Review issue inputs.
             
        :return: Review issue response that contains a list of updated issue objects.
        """
        ...
    def UpdateIssueItems(self, Inputs: list[UpdateIssueInfo]) -> UpdateIssueRevsResponse:
        """    
             Client calls this operation to update existing issue reports. An issue report may
             be populated or updated by multiple applications during its life cycle. For example,
             issue report metadata may be updated due to issue status changes, reviews and comments,
             and so on. Issue report context data may be updated with new product view datasets,
             documents, or markups. Out-of-date documents may be updated with new files. Irrelevant
             attachments may be detached. The way to pack up data to update an issue report is
             the same as to create an issue report.
             

Use Cases:

             The NX application may call this operation to update the issue report with a new
             Check-Mate log file, and issue scene dataset. The client provides the existing log
             file dataset, the new log file (and its upload ticket) as generalDatasets data, the
             new issue scene dataset as a relationData object to update the issue report for a
             particular Check-Mate check failure.
             

Teamcenter Component:

             Issue Management - Teamcenter Issue Management is an application that allows users
             to capture issue, share issue data and collaborate on the business process to resolve
             issue in product life management.
             
        :param Inputs: 
                         Inputs to update issues.
             
        :return: Array of updated issue revisions.
        """
        ...

