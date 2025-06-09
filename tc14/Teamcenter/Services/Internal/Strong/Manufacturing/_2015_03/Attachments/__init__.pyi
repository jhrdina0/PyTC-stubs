import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AattachmentsCreated:
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.ModelObject
    CreatedObject: Teamcenter.Soa.Client.Model.ModelObject
    AttachmentLine: Teamcenter.Soa.Client.Model.ModelObject
    WriteFileTicket: str

class AttachmentLines:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    AttachmentsInfo: System.Collections.Hashtable

class AttachmentResponse:
    def __init__(self, ) -> None: ...
    Attchments: list[AattachmentsCreated]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class AttachmentsInput:
    def __init__(self, ) -> None: ...
    Line: Teamcenter.Soa.Client.Model.ModelObject
    AttachmentWindowsList: list[Teamcenter.Soa.Client.Model.ModelObject]

class AttachmentWindowInfo:
    def __init__(self, ) -> None: ...
    AttachmentWindow: Teamcenter.Soa.Client.Model.ModelObject
    AttachmentLines: list[Teamcenter.Soa.Client.Model.ModelObject]

class CreateAttachmentsInput:
    def __init__(self, ) -> None: ...
    SourceLine: Teamcenter.Soa.Client.Model.ModelObject
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    ObjectType: str
    Name: str
    Description: str
    Type: str
    DatasetID: str
    DatasetRev: str
    ToolUsed: str
    ImportFilePath: str
    ImportFileType: str
    NamedRefType: str
    NamedRefSubType: str
    Relation: str
    SaveForm: bool
    DsContainer: Teamcenter.Soa.Client.Model.ModelObject

class Attachments:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAttachmentLines(self, AttachmentsInputList: list[CreateAttachmentsInput]) -> AttachmentResponse: ...
    def GetAttachmentLines(self, InputList: list[AttachmentsInput]) -> AttachmentLines: ...

