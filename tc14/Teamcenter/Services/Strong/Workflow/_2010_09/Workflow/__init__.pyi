import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ApplyTemplateInput:
    """
    
New versions of the workflow templates that needs to be applied including the
corresponding
client ids.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """client id"""
    ProcessTemplate: Teamcenter.Soa.Client.Model.Strong.EPMTaskTemplate
    """Process template to be applied"""

class ApplyTemplateOutput:
    """
    Results from applying a template to its corresponding active processes.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """client id"""
    UpdatedProcesses: list[Teamcenter.Soa.Client.Model.Strong.EPMJob]
    """Active processes that were updated successfully"""
    FailedProcesses: list[Teamcenter.Soa.Client.Model.Strong.EPMJob]
    """Active processes that could not be updated"""

class ApplyTemplateResponse:
    """
    Information about active processes that were updated with template changes
    """
    def __init__(self, ) -> None: ...
    ApplyTemplateOutput: list[ApplyTemplateOutput]
    """List of processes that were updated and list of processes that failed."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data"""

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ApplyTemplateToProcesses(self, ApplyTemplateInput: list[ApplyTemplateInput], ProcessingMode: int) -> ApplyTemplateResponse:
        """    
             Apply the specified templates to all active workflow processes that are based on
             earlier versions of the templates.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param ApplyTemplateInput: 
                         Templates to be applied to active processes
             
        :param ProcessingMode: 
                         Indicates if request needs to be processed asynchronously.  0 - Indicates synchronous
                         processing. 1 - Indicates asynchronous processing.
             
        :return: List of active processes that were updated successfully and list of failures
        """
        ...

