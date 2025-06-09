import System
import Teamcenter.Soa.Client.Model
import typing

class TopicTypesOutput:
    def __init__(self, ) -> None: ...
    TopicTypes: list[Teamcenter.Soa.Client.Model.ModelObject]
    TopicRevisions: list[Teamcenter.Soa.Client.Model.ModelObject]
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData

class ContentManagement:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTopicTypesAndRelatedTopics(self, TopicType: Teamcenter.Soa.Client.Model.ModelObject, TopicTypeNameFilter: str, IncludeReferencedTopics: bool) -> TopicTypesOutput: ...

