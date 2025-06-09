import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CreateChangeObjectInput:
    def __init__(self, ) -> None: ...
    BoName: str
    ChangeRelatedProps: System.Collections.Hashtable
    CompoundCreateChange: System.Collections.Hashtable

class CreateChangeWorkflowInfo:
    def __init__(self, ) -> None: ...
    TemplateName: str
    SubmitToWorkflow: bool
    AdditionalWorkflowData: System.Collections.Hashtable

class CreateAndSubmitChangeInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    CreateData: CreateChangeObjectInput
    RelatedData: System.Collections.Hashtable
    PasteProp: str
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    SetActive: bool
    WorkflowData: CreateChangeWorkflowInfo
    ChangeParticipantData: list[CreateChangeParticipantInfo]

class CreateAndSubmitChangeOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]

class CreateAndSubmitChangeResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    Output: list[CreateAndSubmitChangeOutput]

class CreateChangeParticipantInfo:
    def __init__(self, ) -> None: ...
    InternalName: str
    AllowMultipleAssignee: bool
    AssigneeList: list[Teamcenter.Soa.Client.Model.ModelObject]
    AdditionalParticipantData: System.Collections.Hashtable

class ChangeManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAndSubmitChangeObjects(self, Input: list[CreateAndSubmitChangeInput]) -> CreateAndSubmitChangeResponse: ...

