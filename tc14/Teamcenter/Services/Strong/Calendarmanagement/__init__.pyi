import System
import Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement
import Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement
import Teamcenter.Services.Strong.Calendarmanagement._2008_06.CalendarManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CalendarManagementRestBindingStub(CalendarManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateTCCalendars(self, NewTCCalendars: list[Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.NewTCCalendar]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarResponse: ...
    def GetTCCalendars(self, GetTCCalendars: list[Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.GetTCCalendarData]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarResponse: ...
    def ModifyTCCalendars(self, Modifications: list[Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarModification]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarResponse: ...
    def UpdateTCCalendars(self, TccalendarUpdates: list[Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarUpdate]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarResponse: ...
    def DeleteTCCalendars(self, TccalendarsToDelete: list[Teamcenter.Soa.Client.Model.Strong.TCCalendar]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateCalendars(self, NewTCCalendars: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CalendarContainer]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CreateCalendarResponse: ...
    @typing.overload
    def CreateCalendars(self, NewTCCalendars: list[Teamcenter.Services.Strong.Calendarmanagement._2008_06.CalendarManagement.CalendarContainer]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CreateCalendarResponse: ...
    @typing.overload
    def UpdateCalendars(self, TccalendarUpdates: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CalendarUpdate]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def UpdateCalendars(self, TccalendarUpdates: list[Teamcenter.Services.Strong.Calendarmanagement._2008_06.CalendarManagement.CalendarUpdate]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class CalendarManagementService:
    """
    
            The CalendarManagement service provides standard
            operations to satisfy primarily the typical needs of a user dealing with calendar
            management.  It also enables the user to perform various operations to manage specific
            calendars and customize them with specified calendar data and calendar events.
            
            The CalendarManagement service can be used
            for supporting following use-cases:
            

Creating new calendars
            
Updating calendars
            
Getting calendars
            
Deleting calendars
            




Library Reference:

TcSoaCalendarManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> CalendarManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateTCCalendars(self, NewTCCalendars: list[Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.NewTCCalendar]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarResponse:
        """    
             Creates new calendars based on the input parameters.
             

Teamcenter Component:

             Calendar Management - Application in Teamcenter to manage calendars in project schedules
             
        :param NewTCCalendars: 
                         A vector of NewCalendar structures that holds the various attributes for the calendar
                         to be created. This includes any new calendar events.
             
        :return: A structure that contains a CalendarContainer structure for each calendar which in
             turn contains the newly created calendar and all its inherited calendar events. ServiceData
             includes the error stack if partial or all operations fail.
        """
        ...
    def GetTCCalendars(self, GetTCCalendars: list[Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.GetTCCalendarData]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarResponse:
        """    
             This operation gets the list of  calendars based on the user's request to the application
             interface. Multiple calendars can be obtained through this operation.
             
             The information needed to get TCCalendar  objects is specified in the GetTCCalendarData  structure. It returns TCCalendarResponse which contains response data
             from the getcalendar request. Errors will
             be returned in the list of partial errors in the ServiceData.
             


Teamcenter Component:

             Calendar Management - Application in Teamcenter to manage calendars in project schedules
             
        :param GetTCCalendars: 

        :return: 
        """
        ...
    def ModifyTCCalendars(self, Modifications: list[Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarModification]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarResponse:
        """    
             Modifies the specified schedule calendars based on the action string. Reset: Reset
             the schedule calendar to the base calendar Merge: Merge the schedule calendar with
             the base calendar
             

Teamcenter Component:

             Calendar Management - Application in Teamcenter to manage calendars in project schedules
             
        :param Modifications: 
                         Contains a vector of Schedule Calendars to modify
             
        :return: A structure that contains the modified schedule calendars within CalendarContainer
             objects. ServiceData includes the error stack if partial or all operations fail.
        """
        ...
    def UpdateTCCalendars(self, TccalendarUpdates: list[Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarUpdate]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_01.CalendarManagement.TCCalendarResponse:
        """    
             Updates the specified calendars and their events. This includes creating, modifying
             and deleting events associated with specified calendars
             

Teamcenter Component:

             Calendar Management - Application in Teamcenter to manage calendars in project schedules
             
        :param TccalendarUpdates: 
                         Contains a vector of CalendarUpdate structures. The CalendarUpdate contains the calendar
                         to be updated and the CalendarData structure that holds its new attribute values.
                         It also includes vectors that specify the following event modifications for each
                         calendar: 1. Vector of events to be deleted 2. Vector of events to be updated 3.
                         Vector containing CalendarEventData that specifies new attribute values for the event
                         4. Vector of CalendarEventData containing data for creating new events
             
        :return: A structure that contains the updated calendars within CalendarContainer objects.
             The ServiceData object will contain uids of the created, modified and deleted calendar
             events. ServiceData also includes the error stack if partial or all operations fail.
        """
        ...
    def DeleteTCCalendars(self, TccalendarsToDelete: list[Teamcenter.Soa.Client.Model.Strong.TCCalendar]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the specified calendars and their calendar events based on
             the user's request to the application interface. Multiple calendars and its their
             events can be deleted   through this operation. Existing schedule, resource , and
             base calendars can be deleted through this operation..
             
             The information needed to delete a TCCalendar  object is specified in the
             TCCalendar structure. It returns  ServiceData
             , which is  a common data structure used to return sets of Teamcenter data model
             objects from a service request. This structure holds lists of data model objects
             that were 'created', 'deleted', 'updated' or 'plain' in the database with this service
             request. 'Plain' objects are simply objects that the service is returning where no
             changes have been made to the database object, i.e. e.g., GetHomeFolder
             returns a list of objects that are contained in the user's home folder. Errors will
             be returned in the list of partial errors in the ServiceData.
             
             



Teamcenter Component:

             Calendar Management - Application in Teamcenter to manage calendars in project schedules
             
        :param TccalendarsToDelete: 

        :return: 
        """
        ...
    @typing.overload
    def CreateCalendars(self, NewTCCalendars: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CalendarContainer]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CreateCalendarResponse: ...
    @typing.overload
    def CreateCalendars(self, NewTCCalendars: list[Teamcenter.Services.Strong.Calendarmanagement._2008_06.CalendarManagement.CalendarContainer]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CreateCalendarResponse: ...
    @typing.overload
    def UpdateCalendars(self, TccalendarUpdates: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CalendarUpdate]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def UpdateCalendars(self, TccalendarUpdates: list[Teamcenter.Services.Strong.Calendarmanagement._2008_06.CalendarManagement.CalendarUpdate]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

