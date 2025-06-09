import Sss0.Services.Strong.Svcscheduling._2012_02.SvcScheduling
import Sss0.Services.Strong.Svcscheduling._2014_10.SvcScheduling
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import typing

class SvcSchedulingRestBindingStub(SvcSchedulingService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def RecordUtilization(self, Inputs: list[Sss0.Services.Strong.Svcscheduling._2012_02.SvcScheduling.RecordUtilizationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def RecordUtilization(self, Inputs: list[Sss0.Services.Strong.Svcscheduling._2014_10.SvcScheduling.RecordUtilizationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def UpdateConfiguration(self, Inputs: list[Sss0.Services.Strong.Svcscheduling._2012_02.SvcScheduling.UpdateConfigurationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def UpdateConfiguration(self, Inputs: list[Sss0.Services.Strong.Svcscheduling._2014_10.SvcScheduling.UpdateConfigurationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class SvcSchedulingService:
    """
    
            Contains SvcScheduling services
            


Library Reference:

SSS0SoaSvcSchedulingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SvcSchedulingService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def RecordUtilization(self, Inputs: list[Sss0.Services.Strong.Svcscheduling._2012_02.SvcScheduling.RecordUtilizationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def RecordUtilization(self, Inputs: list[Sss0.Services.Strong.Svcscheduling._2014_10.SvcScheduling.RecordUtilizationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def UpdateConfiguration(self, Inputs: list[Sss0.Services.Strong.Svcscheduling._2012_02.SvcScheduling.UpdateConfigurationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def UpdateConfiguration(self, Inputs: list[Sss0.Services.Strong.Svcscheduling._2014_10.SvcScheduling.UpdateConfigurationInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

