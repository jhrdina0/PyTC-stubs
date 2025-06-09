import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrSaveAsPSBOMViewRevisionInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    ItemObject: Teamcenter.Soa.Client.Model.Strong.Item
    ItemRevObj: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ViewTypeTag: Teamcenter.Soa.Client.Model.Strong.PSViewType
    SrcBvrTag: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    IsPrecise: bool

class CreateOrSaveAsPSBOMViewRevisionOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    BvrTag: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision

class CreateOrSaveAsPSBOMViewRevisionResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    PsBVROutputs: list[CreateOrSaveAsPSBOMViewRevisionOutput]

class GetAllAvailableViewTypesInput:
    def __init__(self, ) -> None: ...
    ClientId: str
    ItemRevisionObj: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    ItemObject: Teamcenter.Soa.Client.Model.Strong.Item

class GetAvailableViewTypesOutput:
    def __init__(self, ) -> None: ...
    ClientId: str
    ViewTags: list[Teamcenter.Soa.Client.Model.Strong.PSViewType]

class GetAvailableViewTypesResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    ViewTypesOutputs: list[GetAvailableViewTypesOutput]

class Structure:
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrSavePSBOMViewRevision(self, CreateOrSavePSBOMViewRevisionInputs: list[CreateOrSaveAsPSBOMViewRevisionInput]) -> CreateOrSaveAsPSBOMViewRevisionResponse: ...
    def GetAvailableViewTypes(self, GetAvailableViewTypesInputs: list[GetAllAvailableViewTypesInput]) -> GetAvailableViewTypesResponse: ...

