import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class HasActiveMarkupAssociatedOut:
    def __init__(self, ) -> None: ...
    HasActiveMarkup: bool
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class MassUpdateChange:
    def __init__(self, ) -> None: ...
    PropName: str
    PropValue: str

class SaveImpactedAssembliesIn:
    def __init__(self, ) -> None: ...
    ImpactedObject: Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject
    MassUpdateChanges: list[MassUpdateChange]

class MassUpdate:
    def __init__(self , *args: typing.Any) -> None: ...
    def HasActiveMarkupAssociated(self, ChangeObject: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> HasActiveMarkupAssociatedOut: ...
    def SaveImpactedAssemblies(self, ChangeObject: Teamcenter.Soa.Client.Model.Strong.ItemRevision, ImpactedObjectsInfo: list[SaveImpactedAssembliesIn]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

