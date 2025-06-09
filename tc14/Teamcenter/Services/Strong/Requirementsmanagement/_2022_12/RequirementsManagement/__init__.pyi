import Teamcenter.Soa.Client.Model
import typing

class SetContentInput2:
    """
    
The SetContentInput2 structure represents the input required to set the contents
on the FullText object.
    """
    def __init__(self, ) -> None: ...
    ObjectToProcess: Teamcenter.Soa.Client.Model.ModelObject
    """
FullText object or any BusinessObject with a FullText, attached via
            an IMAN_Specification relation, where FullText is a secondary object.
            """
    TransientFileWriteTicket: str
    """An FMS ticket of a Microsoft Word file to be uploaded to Teamcenter."""
    ContentType: str
    """
            Type of content to be set on the FullText. Supported values are: REQ_HTML,
            REQ_PLAINTEXT or REQ_RICHTEXT
            """
    Contents: str
    """The actual content to be set on the FullText object."""

class RequirementsManagement:
    """
    Interface RequirementsManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetRichContent2(self, Inputs: list[SetContentInput2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

