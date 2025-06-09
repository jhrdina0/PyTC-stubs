import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Create4GDPreviewFromMappingInfo:
    """
    Input structure for create4GDPreviewFromMapping operation.
    """
    def __init__(self, ) -> None: ...
    MappingDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
Dataset Business Object to represent mapping between source Item assembly
            datatypes to target 4GD datatypes.
            """
    RevisionRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    PreviewInputMap: System.Collections.Hashtable

class FileTicket:
    """
    FileTicket structure to hold filename and the FMS read ticket of the file.
    """
    def __init__(self, ) -> None: ...
    Filename: str
    """The name of the file."""
    Ticket: str
    """FMS Read ticket for the file"""

class Create4GDPreviewFromMappingResponse:
    """
    
Create4GDPreviewFromMappingResponse structure contains Preview Dataset
            business objects which are created during create4GDPreviewFromMapping operation along
            with the service data.
            
    """
    def __init__(self, ) -> None: ...
    PreviewDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """
            Contains list of preview Dataset business objects that represent the mapping
            between the source Item assembly and the target 4GD business objects.
            """
    FileTicket: FileTicket
    """FileTicket structure to hold filename and the FMS read ticket of the file."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contain a list of added, updated or deleted objects and also list of any errors which
            occurred within the call.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def Create4GDPreviewFromMapping(self, Input: Create4GDPreviewFromMappingInfo) -> Create4GDPreviewFromMappingResponse: ...
    def Create4GObjectsFromPreview(self, PreviewDatasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

