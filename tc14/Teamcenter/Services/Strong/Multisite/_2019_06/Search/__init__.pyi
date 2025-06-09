import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class SearchFailure:
    """
    This structure returns failure during publish/unpublish operation
    """
    def __init__(self, ) -> None: ...
    FailureObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object that failed to publish."""
    FailedSite: str
    """The name of the site the object failed to publish to."""
    FailureCodes: list[int]
    """A list of failure codes for the failureObject."""
    FailureStrings: list[str]
    """A list of error strings corresponding to each error in failureCodes."""

class SearchResponse:
    """
    Return structure for publish/unpublish operation
    """
    def __init__(self, ) -> None: ...
    FailureInfo: list[SearchFailure]
    """
            A list of SearchFailure structures. Each structure contains failure information for
            a specific business object that was supplied.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The standard ServiceData return."""

class Search:
    """
    Interface Search
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def Publish(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], TargetSites: list[str], Options: System.Collections.Hashtable) -> SearchResponse: ...
    def Unpublish(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], TargetSites: list[str], Options: System.Collections.Hashtable) -> SearchResponse: ...

