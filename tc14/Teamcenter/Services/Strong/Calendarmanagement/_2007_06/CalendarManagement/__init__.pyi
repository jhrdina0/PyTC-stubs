import System
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
    """The type of calendar"""
    SunRanges: list[RangeData]
    """The ranges for Sunday"""
    MonRanges: list[RangeData]
    """The ranges for Monday"""
    TueRanges: list[RangeData]
    """The ranges for Tuesday"""
    WedRanges: list[RangeData]
    """The ranges for Wednesday"""
    ThuRanges: list[RangeData]
    """The ranges for Thursday"""
    FriRanges: list[RangeData]
    """The ranges for Friday"""
    SatRanges: list[RangeData]
    """The ranges for Saturday"""

class CalendarContainer:
    """
    A container to hold the Calendar Events related to CalendarData
    """
    def __init__(self, ) -> None: ...
    TccalendarAttributes: CalendarData
    """The Calendar information"""
    NewEvents: list[CalendarEventData]
    """The event information"""

class CalendarEventData:
    """
    The information for a single CalendarEvent.
    """
    def __init__(self, ) -> None: ...
    FirstRecurStart: System.DateTime
    """The date of the event"""
    FirstRecurEnd: System.DateTime
    """Placeholder for recurring end date. (not currently used)"""
    EventExpiryDate: System.DateTime
    """Placeholder for recurring event expiration. (not currently used)"""
    EventRanges: list[RangeData]
    """The time ranges for the event"""
    EventType: int
    """Placeholder for event type. (not currently used)"""
    NumRecurrences: int
    """Placeholder number of recurrences. (not currently used)"""
    RecurInterval: int
    """Placeholder for the recurring interval. (not currently used)"""
    RecurDaysOfWeek: int
    """Placeholder for mask of days. (not currently used)"""
    RecurWeeksOfMonth: int
    """Placeholder for mask of weeks. (not currently used)"""
    RecurMonth: int
    """Placeholder for mask of months. (not currently used)"""

class CalendarResponse:
    """
    The response containing a created calendars and the events.
    """
    def __init__(self, ) -> None: ...
    Calendar: Teamcenter.Soa.Client.Model.Strong.TCCalendar
    """The calendar"""
    CalendarEvent: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    """The events related to that calendar."""

class CalendarUpdate:
    """
    The information necessary to modify a calendar.
    """
    def __init__(self, ) -> None: ...
    Calendar: Teamcenter.Soa.Client.Model.Strong.TCCalendar
    """The calendar to modify"""
    CalendarAttributes: CalendarData
    """The basic calendar data to modify"""
    EventsToAdd: list[CalendarEventData]
    """New calendar events to add"""
    EventsToDelete: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    """Existing calendar events to delete"""
    EventsToUpdate: list[ModifyCalendarEvent]
    """Calendar events to update."""

class CreateCalendarResponse:
    """
    The container with ALL the CalendarResponse and the service data.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""
    CalendarResponse: list[CalendarResponse]
    """The calendars and events"""

class ModifyCalendarEvent:
    """
    The information necessary to modify a calendar event.
    """
    def __init__(self, ) -> None: ...
    Event: Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent
    """The event to modify"""
    EventAttributes: CalendarEventData
    """The new event data"""

class RangeData:
    """
    
            A single time range.  The startRange and endRange represent minutes since midnight.
            There is a special range (startRange=480 and endRange=480) which represents a non-working
            range.
            
    """
    def __init__(self, ) -> None: ...
    StartRange: int
    """The starting offset."""
    EndRange: int
    """The ending offset."""

class CalendarManagement:
    """
    Interface CalendarManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateCalendars(self, NewTCCalendars: list[CalendarContainer]) -> CreateCalendarResponse:
        """    
             Creates new calendars based on the provided input parameters.
             

Teamcenter Component:

             Calendar Management - Application in Teamcenter to manage calendars in project schedules
             
        :param NewTCCalendars: 
                         A vector of CalendarContainer structures that holds the various attributes for the
                         calendar to be created. This includes any new calendar events.
             
        :return: Contains the calendar and calendar event objects. It also contains serviceData that
             has the error stack if partial or all operations fail.
        """
        ...
    def UpdateCalendars(self, TccalendarUpdates: list[CalendarUpdate]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Updates the specified calendars and their events. This includes creating, modifying
             and deleting events associated with specified calendars
             

Teamcenter Component:

             Calendar Management - Application in Teamcenter to manage calendars in project schedules
             
        :param TccalendarUpdates: 
                         Contains a vector of CalendarUpdate structures. The CalendarUpdate contains the calendar
                         to be updated and the CalendarData structure that holds its new attribute values.
                         It also includes vectors that specify the following event modifications for each
                         calendar: 1. UID of the calendar to modify 2. CalendarData containing calendar attributes
                         to be updated 3. Vector of CalendarEventData containing data for creating new events
                         4. Vector of events to be deleted 5. Vector of events to be updated
             
        :return: Contains the calendar and calendar event objects ServiceData also includes the error
             stack if partial or all operations fail.
        """
        ...

