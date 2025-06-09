import System
import Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement
import Teamcenter.Soa.Client.Model
import typing

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateNewBaselines(self, CreateBaselineContainer: list[Teamcenter.Services.Strong.Projectmanagement._2007_01.ScheduleManagement.CreateBaselineContainer], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates new schedule baselines. In case of background mode,
             this operation files an asynchronous request to create the baselines and releases
             the client immediately so that the user can perform other operation.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param CreateBaselineContainer: 
                         A list of CreateBaselineContainer structures. This structure contains the information
                         to create new schedule baseline.
             
        :param RunInBackground: 
<b>True</b> to perform the operation in background mode in a separate asynchronous
                         server session. <b>False</b> to perform the operation synchronously.
             
        :return: 
        """
        ...

