import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetTCCalendarData:
    """
    The query information for calendars
    """
    def __init__(self, ) -> None: ...
    Type: int
    """
            The type of TCCalendar (1-System Calendar, 2-Schedule Calendar, 3-User Calendar,
            4-ScheduleMember Calendar)
            """
    Schedule: Teamcenter.Soa.Client.Model.ModelObject
    """The related schedule"""
    Resource: Teamcenter.Soa.Client.Model.ModelObject
    """The related resource"""

class TCCalendarData:
    """
    Data for a calendar
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Name of the tccalendar"""
    Description: str
    """Description of the tccalendar"""
    Schedule: Teamcenter.Soa.Client.Model.ModelObject
    """Null indicates no schedule"""
    Source: Teamcenter.Soa.Client.Model.ModelObject
    """TCCalendar source(schedule/resource)"""
    Type: int
    """Type of tccalendar"""
    MinsSun: int
    """Default minutes for Sunday"""
    MinsMon: int
    """Default minutes for Monday"""
    MinsTue: int
    """Default minutes for Tuesday"""
    MinsWed: int
    """Default minutes for Wednesday"""
    MinsThu: int
    """Default minutes for Thursday"""
    MinsFri: int
    """Default minutes for Friday"""
    MinsSat: int
    """Default minutes for Saturday"""

class NewTCCalendar:
    """
    Holder for new tccalendar and its events
    """
    def __init__(self, ) -> None: ...
    TccalendarAttributes: TCCalendarData
    """The calendar data"""
    NewEvents: list[TCCalendarEventData]
    """The calendar events."""

class TCCalendarContainer:
    """
    Holder for TCCalendar and its events
    """
    def __init__(self, ) -> None: ...
    Tccalendar: Teamcenter.Soa.Client.Model.Strong.TCCalendar
    """The TCCalendar"""
    Events: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    """The TCCalendarEvents for the TCCalendar."""

class TCCalendarEventData:
    """
    Data for a calendar event.
    """
    def __init__(self, ) -> None: ...
    EventDate: System.DateTime
    """The date on which event occurs"""
    EventMin: int
    """The duration of the event in minutes"""

class TCCalendarModification:
    """
    Modification structure
    """
    def __init__(self, ) -> None: ...
    ScheduleTCCalendar: Teamcenter.Soa.Client.Model.Strong.TCCalendar
    """TCCalendar to modify"""
    Action: str
    """enumerated action"""

class TCCalendarResponse:
    """
    Standard response for most tccalendar calls
    """
    def __init__(self, ) -> None: ...
    Tccalendars: list[TCCalendarContainer]
    """The calendar containers"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""

class TCCalendarUpdate:
    """
    A calendar update
    """
    def __init__(self, ) -> None: ...
    Tccalendar: Teamcenter.Soa.Client.Model.Strong.TCCalendar
    """The calendar being updated"""
    UpdatedAttributes: TCCalendarData
    """The updated attributes"""
    EventsToDelete: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    """Events to delete"""
    EventsToUpdate: list[Teamcenter.Soa.Client.Model.Strong.TCCalendarEvent]
    """Events to update"""
    EventAttributes: list[TCCalendarEventData]
    """Corresponding updates for the EventsToUpdate"""
    NewEvents: list[TCCalendarEventData]
    """Events to create"""

class CalendarManagement:
    """
    Interface CalendarManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateTCCalendars(self, NewTCCalendars: list[NewTCCalendar]) -> TCCalendarResponse:
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
    def GetTCCalendars(self, GetTCCalendars: list[GetTCCalendarData]) -> TCCalendarResponse:
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
    def ModifyTCCalendars(self, Modifications: list[TCCalendarModification]) -> TCCalendarResponse:
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
    def UpdateTCCalendars(self, TccalendarUpdates: list[TCCalendarUpdate]) -> TCCalendarResponse:
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

