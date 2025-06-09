import Mei0.Services.Strong.Mesinteg._2013_05.Release
import Mei0.Services.Strong.Mesinteg._2014_06.Release
import Mei0.Services.Strong.Mesinteg._2014_12.Release
import Mei0.Services.Strong.Mesinteg._2015_03.Release
import Mei0.Services.Strong.Mesinteg._2015_10.Release
import Mei0.Services.Strong.Mesinteg._2016_09.Release
import Mei0.Services.Strong.Mesinteg._2017_11.Release
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import typing

class ReleaseRestBindingStub(ReleaseService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def ApplyReleaseStatusToLines(self, Input: list[Mei0.Services.Strong.Mesinteg._2013_05.Release.ApplyReleaseStatusToLinesInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ApplyReleaseStatusToLines(self, Input: list[Mei0.Services.Strong.Mesinteg._2014_06.Release.ApplyReleaseStatusToLinesInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateReleaseUpdatePackage(self, Input: list[Mei0.Services.Strong.Mesinteg._2013_05.Release.CreateReleaseUpdatePackageInputData]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.CreateReleaseUpdatePackageResponse: ...
    def FindReleaseCandidates(self, Input: list[Mei0.Services.Strong.Mesinteg._2013_05.Release.FindReleaseCandidatesInputData]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.FindReleaseCandidatesResponse: ...
    def IsUpdateAllowed(self, ExecutionPlans: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.IsUpdateAllowedResponse: ...
    def OpenPreviousReleasedVersion(self, ExecutionPlans: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.OpenPreviousReleasedVersionResponse: ...
    def ExecutionDataExport(self, Input: list[Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportInputData]) -> Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportResponse: ...
    def SetExecutionIdAndRevisionRule(self, Input: Mei0.Services.Strong.Mesinteg._2015_03.Release.SetExecutionIdAndRevRuleInput) -> Mei0.Services.Strong.Mesinteg._2015_03.Release.SetExecutionIdAndRevRuleResponse: ...
    def ExecutionDataExport2(self, Input: list[Mei0.Services.Strong.Mesinteg._2015_10.Release.ExecutionDataExportInputData2]) -> Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportResponse: ...
    def CreateReleaseUpdatePackage2(self, Input: list[Mei0.Services.Strong.Mesinteg._2016_09.Release.CreateReleaseUpdatePackageInput]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.CreateReleaseUpdatePackageResponse: ...
    def ExecutionDataExport3(self, Input: list[Mei0.Services.Strong.Mesinteg._2016_09.Release.ExecutionDataExportInputData3]) -> Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportResponse: ...
    def FindWorkOrderStatusProps(self, OrderCCs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mei0.Services.Strong.Mesinteg._2017_11.Release.WorkOrderStatusResponse: ...

class ReleaseService:
    """
    
            Release
            


Library Reference:

Mei0SoaMESIntegStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ReleaseService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def ApplyReleaseStatusToLines(self, Input: list[Mei0.Services.Strong.Mesinteg._2013_05.Release.ApplyReleaseStatusToLinesInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def ApplyReleaseStatusToLines(self, Input: list[Mei0.Services.Strong.Mesinteg._2014_06.Release.ApplyReleaseStatusToLinesInputData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateReleaseUpdatePackage(self, Input: list[Mei0.Services.Strong.Mesinteg._2013_05.Release.CreateReleaseUpdatePackageInputData]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.CreateReleaseUpdatePackageResponse:
        """    
             The operation creates the workflow ReleaseUpdateToMes which exports the released
             candidate objects to the MES system.  It is a preliminary to call the operation findReleaseCandidates
             before calling the createReleaseUpdatePackage operation.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         A vector of objects that holds all the release candidates objects and ICs for the
                         created workflow.
             
        :return: The results of the created workflow
        """
        ...
    def FindReleaseCandidates(self, Input: list[Mei0.Services.Strong.Mesinteg._2013_05.Release.FindReleaseCandidatesInputData]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.FindReleaseCandidatesResponse:
        """    
             The operation returns all the Mfg0BvrProcess and Mfg0BvrOperation candidates to be
             exported to the MES system. The candidate objects will be captured in one out of
             the two ways: 1. By a new release status Mei0PendingRelease or the status defined
             within the preference Mei0PendingReleaseStatus added to the revision.  2. Any change
             that was done within the incremental change which is configured in the structure.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         The input structure contains the data we need in order to find the release candidates
                         Lines or ICs for release and Release to the MES system
             
        :return: The results of the calculation for finding the release candidates lines from Item
             Revisions and from ICs.
        """
        ...
    def IsUpdateAllowed(self, ExecutionPlans: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.IsUpdateAllowedResponse:
        """    
             The operation checks if a delta update is allowed for the Mei0ExecutionPlan.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param ExecutionPlans: 
                         This object derives from an MECollaborationContext object.
             
        :return: These errors will be returned in the serviceData as partial errors. 286523: Cannot
             have more than a single BOPWindow configured in the structure.
        """
        ...
    def OpenPreviousReleasedVersion(self, ExecutionPlans: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.OpenPreviousReleasedVersionResponse:
        """    
             This operation returns the correlative structure which had been released and exported
             for the existing Mei0ExecutionPlan.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param ExecutionPlans: 
                         The Mei0ExecutionPlan which had been exported.
             
        :return: Response
        """
        ...
    def ExecutionDataExport(self, Input: list[Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportInputData]) -> Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportResponse:
        """    
             The operation creates the workflow ReleaseUpdateToExecution which exports the input
             data objects to the execution system.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         A list of objects that holds all the export data objects and <b>IncrementalChange</b>
                         object for the created workflow.
             
        :return: 286524 - The EPMTaskTemplate does not exist.
        """
        ...
    def SetExecutionIdAndRevisionRule(self, Input: Mei0.Services.Strong.Mesinteg._2015_03.Release.SetExecutionIdAndRevRuleInput) -> Mei0.Services.Strong.Mesinteg._2015_03.Release.SetExecutionIdAndRevRuleResponse:
        """    
             The service operation sets order ID to Mei0ExecutionPlan. Along with that
             it sets unit effectivity, date effectivity and end item to RevisionRule of
             ConfigurationContext


Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         SetExecutionIDAndRevisionRule structure which contains the information for creating
                         or updating <b>RevisionRule</b> of <b>ConfigurationContext</b> and setting order
                         id value on <b>Mei0ExecutionPlan</b>

        :return: and the following partial error may be returned:300069:If
             an object of wrong type is passed to the operation210006:Specified value is not an
             integer
        """
        ...
    def ExecutionDataExport2(self, Input: list[Mei0.Services.Strong.Mesinteg._2015_10.Release.ExecutionDataExportInputData2]) -> Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportResponse:
        """    
             The operation creates the workflow ReleaseUpdateToExecution which exports the input
             data objects to the execution system.
             

Teamcenter Component:

             MES Integration Services Component - Manufacturing execution system (MES) Integration
             Services Component supports the integration with the SIMATIC IT (SIT) and general
             MES systems.
             
        :param Input: 
                         A list of objects that holds all the export data objects and <b>IncrementalChange</b>
                         object for the created workflow.
             
        :return: 286524 - The EPMTaskTemplate does not exist.
        """
        ...
    def CreateReleaseUpdatePackage2(self, Input: list[Mei0.Services.Strong.Mesinteg._2016_09.Release.CreateReleaseUpdatePackageInput]) -> Mei0.Services.Strong.Mesinteg._2013_05.Release.CreateReleaseUpdatePackageResponse:
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
    def ExecutionDataExport3(self, Input: list[Mei0.Services.Strong.Mesinteg._2016_09.Release.ExecutionDataExportInputData3]) -> Mei0.Services.Strong.Mesinteg._2014_12.Release.ExecutionDataExportResponse:
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
    def FindWorkOrderStatusProps(self, OrderCCs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mei0.Services.Strong.Mesinteg._2017_11.Release.WorkOrderStatusResponse: ...

