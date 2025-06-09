import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def WhatIfAnalysis(self, Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule, WhatIfOption: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation allows the user to perform What-If analysis on a Schedule by
             making scheduling changes locally without affecting other users and save or cancel
             the changes made during the What-If analysis.
             

             Only the following operations can be performed by the user who has started the What-If
             analysis:
             
             1. Modify all properties of the Schedule.
             
             2. Modify all properties of the ScheduleTask other than the following execution
             proeprties : status, work complete, complete percent, actual start date, actual finish
             date, work remaining.
             
             3. Create, delete and update ScheduleTask, ResourceAssignment, TaskDependency,
             and Fnd0ProxyTask objects.
             

             The following operations cannot be performed by the user who has started the What-If
             analysis:
             
             1. Modify the following execution properties of the ScheduleTask : status,
             work complete, complete percent, actual start date, actual finish date, work remaining.
             
             2. Insert Schedule and detach Schedule operations.
             

             Only the following operations can be performed by other users when a Schedule is
             in What-If analysis mode:
             
             1. Modify the following execution properties of the ScheduleTask : status,
             work complete, complete percent, actual start date, actual finish date, work remaining.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Schedule: 
                         The Schedule to set the What-If analysis mode.
             
        :param WhatIfOption: 
                         Specifies the What-If analysis option. The valid options are Start, SaveAndContinue,
                         SaveAndExit and CancelAndExit.
             
        :return: 230086 : The Schedule cannot be unlocked, because it is locked by the user.
        """
        ...

