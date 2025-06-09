import System
import Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CalendarData:
    """
    The information necessary to create a single TCCalendar including daily default ranges.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the calendar"""
    Description: str
    """The description of the calendar"""
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The schedule this calendar relates to (or null)"""
    Source: Teamcenter.Soa.Client.Model.ModelObject
    """The resource this calendar relates to (or null)"""
    BaseCalendar: Teamcenter.Soa.Client.Model.Strong.TCCalendar
    """The parent BASE calendar (or null)"""
    Type: int
    """
            The type of calendar (1-System Calendar, 2-Schedule Calendar, 3-User Calendar, 4-ScheduleMember
            Calendar)
            """
    SunRanges: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.RangeData]
    """The ranges for Sunday"""
    MonRanges: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.RangeData]
    """The ranges for Monday"""
    TueRanges: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.RangeData]
    """The ranges for Tuesday"""
    WedRanges: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.RangeData]
    """The ranges for Wednesday"""
    ThuRanges: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.RangeData]
    """The ranges for Thursday"""
    FriRanges: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.RangeData]
    """The ranges for Friday"""
    SatRanges: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.RangeData]
    """The ranges for Saturday"""
    TimeZone: str
    """
            The timezone id (as specified in the Olson database eg, 'America/New_York' for US
            Eastern time)
            """

class CalendarContainer:
    """
    A container to hold the Calendar Events related to CalendarData
    """
    def __init__(self, ) -> None: ...
    TccalendarAttributes: CalendarData
    """The Calendar information"""
    NewEvents: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CalendarEventData]
    """The event information"""

class CalendarUpdate:
    """
    The information necessary to modify a calendar.
    """
    def __init__(self, ) -> None: ...
    Calendar: Teamcenter.Soa.Client.Model.Strong.TCCalendar
    """The calendar to modify"""
    CalendarAttributes: CalendarData
    """The basic calendar data to modify"""
    EventsToAdd: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CalendarEventData]
    """New calendar events to add"""
    EventsToDelete: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    """Existing calendar events to delete"""
    EventsToUpdate: list[Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.ModifyCalendarEvent]
    """Calendar events to update."""

class CalendarManagement:
    """
    Interface CalendarManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateCalendars(self, NewTCCalendars: list[CalendarContainer]) -> Teamcenter.Services.Strong.Calendarmanagement._2007_06.CalendarManagement.CreateCalendarResponse:
        """    
             This operation creates a list of calendars based on the users request to the application
             interface.
             
 User, Resource, Schedule, Base Calendars can be created .
             
             The information needed to create Calendar are specified in the CalendarContainer structure. It returns CreateCalendarResponses
             which contains the response data from the create request .Errors will be returned
             in the list of partial errors in the ServiceData.
             



Teamcenter Component:

             Calendar Management - Application in Teamcenter to manage calendars in project schedules
             
        :param NewTCCalendars: 

        :return: 
        """
        ...
    def UpdateCalendars(self, TccalendarUpdates: list[CalendarUpdate]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates the list of specified calendars and their events based on
             the users request to the application interface. This includes creating, modifying
             and deleting events associated with list of specified calendars. The information
             needed to update calendars is specified in the CalendarUpdate
             structure. It returns service data which contains the response data from the update
             request. Errors will be returned in the list of partial errors in the ServiceData.
             


Teamcenter Component:

             Calendar Management - Application in Teamcenter to manage calendars in project schedules
             
        :param TccalendarUpdates: 

        :return: 
        """
        ...

