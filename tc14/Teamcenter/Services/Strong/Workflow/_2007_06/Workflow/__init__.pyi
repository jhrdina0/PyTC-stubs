import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ReleaseStatusInput:
    """
    ReleaseStatus input
    """
    def __init__(self, ) -> None: ...
    Operations: list[ReleaseStatusOption]
    """Operations to perform ( Currently only Append is supported )"""
    Objects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """Objects to modify"""

class ReleaseStatusOption:
    """
    ReleaseStatus option
    """
    def __init__(self, ) -> None: ...
    NewReleaseStatusTypeName: str
    """Name of release type to instantiate and assign"""
    Operation: str
    """Operation to perform"""
    ExistingreleaseStatusTypeName: str
    """Name of old release type to delete or replace"""

class SetReleaseStatusResponse:
    """
    service data
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetReleaseStatus(self, Input: list[ReleaseStatusInput]) -> SetReleaseStatusResponse:
        """    
             Manages the release status status of an object  The permitted operations are Append,
             Delete, Rename and Replace Currently Append and Delete are supported With the delete
             operation if an empty string is passed in instead of the status name all statuses
             will be cleared for that set of workspace objects.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Input: 
                         A vector of ReleaseStatusInput structures that control operations performed on the
                         objects
             
        :return: Failure will be with error messages in the ServiceData.
        """
        ...

