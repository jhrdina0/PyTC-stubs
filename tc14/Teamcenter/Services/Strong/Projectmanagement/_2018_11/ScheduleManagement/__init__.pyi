import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SubmitTimesheetEntries(self, TimesheetEntries: list[Teamcenter.Soa.Client.Model.Strong.TimeSheetEntry], RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation submits the list of TimeSheetEntry to workflow. The preference SM_TIMESHEET_APPROVE_WORKFLOW
             will be used to determine the workflow template. If not specified, TimeSheetApproval
             template will be used.
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param TimesheetEntries: 
                         A list of TimeSheetEntry objects to to submit to workflow.
             
        :param RunInBackground: 
                         If true perform the operation in background mode in a separate asynchronous server
                         session. False to perform the operation synchronously
             
        :return: 230141 : The privileged user assigned to the Schedule Task is invalid. Please assign
             either a user or a resource pool of any type.
        """
        ...

