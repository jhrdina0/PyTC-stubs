import Mei0.Services.Strong.Mesinteg._2013_05.Release
import Mei0.Services.Strong.Mesinteg._2014_12.Release
import Mei0.Services.Strong.Mesinteg._2015_10.Release
import Teamcenter.Soa.Client.Model
import typing

class Credentials:
    """
    Credentials for validating MES user authenticity.
    """
    def __init__(self, ) -> None: ...
    MesUserName: str
    """MES user name for validating user authenticity."""
    MesUserPassword: str
    """MES user password for validating user authenticity."""

class CreateReleaseUpdatePackageInput:
    """
    
            A vector of objects that holds all the release candidates objects and ICs for the
            created workflow.
            
    """
    def __init__(self, ) -> None: ...
    DeltaReleaseinfo: Mei0.Services.Strong.Mesinteg._2013_05.Release.ReleaseCandidatesDeltaReleaseInfo
    """Information about Release Candidates."""
    FullReleaseInfo: Mei0.Services.Strong.Mesinteg._2013_05.Release.ReleaseCandidatesFullReleaseInfo
    """
            The structure has the additional information in case that the user exports the entire
            structure and not just a delta export.
            """
    FullReleaseUpdate: bool
    """True in case that a full release update, false in case of a delta release."""
    WorkflowTemplate: Teamcenter.Soa.Client.Model.ModelObject
    """The EPMTaskTemplate to be created."""
    InfoForm: Teamcenter.Soa.Client.Model.ModelObject
    """
            The Mei0ReleaseUpdateToMesInfo form or any other customized form with the export
            additional information to be attached to the workflow.
            """
    MesCredentials: Credentials
    """The MES user credentials for validating authenticity."""

class ExecutionDataExportInputData3:
    """
    The data objects that needs to be exported.
    """
    def __init__(self, ) -> None: ...
    DataInfo: Mei0.Services.Strong.Mesinteg._2015_10.Release.DataInfo2
    """Information related to input data export."""
    ExportInfo: Mei0.Services.Strong.Mesinteg._2014_12.Release.ExportInfo
    """Information related to export of data objects."""
    UserCredentials: Credentials
    """MES user credentials to validate user authentication."""

class Release:
    """
    Interface Release
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateReleaseUpdatePackage2(self, Input: list[CreateReleaseUpdatePackageInput]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.CreateReleaseUpdatePackageResponse:
        """    
             The operation creates the workflow ReleaseUpdateToMes which exports the released
             candidate objects to the MES system. It is a preliminary to call the operation findReleaseCandidates
             before calling the createReleaseUpdatePackage operation.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         Input a vector of objects that holds all the release candidates objects and ICs for
                         the created workflow.
             
        :return: The results of the created workflow.
        """
        ...
    def ExecutionDataExport3(self, Input: list[ExecutionDataExportInputData3]) -> Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportResponse:
        """    
             The operation creates the workflow ReleaseUpdateToExecution which exports the input
             data objects to the execution system.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         A list of objects that holds all the export data objects and IncrementalChange object
                         for the created workflow.
             
        :return: 286524 - The EPMTaskTemplate does not exist.
        """
        ...

