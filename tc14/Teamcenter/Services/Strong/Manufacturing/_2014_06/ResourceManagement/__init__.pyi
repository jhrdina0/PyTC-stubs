import System
import Teamcenter.Soa.Client.Model
import typing

class CheckResult:
    """
    Contains the check results for one tool.
    """
    def __init__(self, ) -> None: ...
    IcoId: str
    """The ID of the tool whose parameters were checked."""
    Status: int
    """
            If the status value is 0, checking succeeded. If it is not 0, some check failed.
            The details why the checking failed are described in the report.
            
"""
    Report: list[str]
    """A list of strings that make up the lines of the report."""

class CheckToolParametersResponse:
    """
    
A CheckToolParametersResponse structure contains the reports and statuses for
all
tools that were checked, as well as a ServiceData object that may contain error
descriptions,
if any errors occurred.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data that can contain error descriptions."""
    CheckResults: list[CheckResult]
    """A list containing a check result for each tool."""

class ResourceManagement:
    """
    Interface ResourceManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CheckToolParameters(self, IcoIds: list[str], CheckLevel: str, CheckTypes: list[str]) -> CheckToolParametersResponse:
        """    
             This operation checks for a list of tools if they define the required attribute values
             to create their 3D graphics or use them as cutters in NX CAM.  The list of tools
             is identified by their internal classification object IDs (ICO IDs).   The caller
             can select the level and type of checking that gets performed. The operation will
             return a check result consisting of a status and report for each tool  being checked.
             

Teamcenter Component:

             Resource Manager - Resource Manager is application used by process planners; and
             tool designers to store; modify; and retrieve information about the resources they
             use in their processes.
             
        :param IcoIds: 
                         A list of  classification object IDs that identify the list of tools to be checked.
             
        :param CheckLevel: 

        :param CheckTypes: 

        :return: 
        """
        ...

