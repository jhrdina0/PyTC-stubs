import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ActLineInput:
    def __init__(self, ) -> None: ...
    ActLine: Teamcenter.Soa.Client.Model.Strong.ACTLine
    ClientID: str

class AlignedCadInfo:
    def __init__(self, ) -> None: ...
    CadContext: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    MeAppPathNode: Teamcenter.Soa.Client.Model.Strong.MEAppearancePathNode

class FindAlignedCadOutput:
    def __init__(self, ) -> None: ...
    OutputCad: list[AlignedCadInfo]
    ClientID: str

class FindAlignedCadResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    OutputCadData: list[FindAlignedCadOutput]

class AlignmentManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def FindAlignedCadForACT(self, InputData: list[ActLineInput]) -> FindAlignedCadResponse: ...

