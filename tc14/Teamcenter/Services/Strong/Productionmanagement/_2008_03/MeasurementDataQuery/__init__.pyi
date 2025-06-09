import System
import Teamcenter.Soa.Client.Model
import typing

class Event:
    """
    The Event structure is used to show the output result.
    """
    def __init__(self, ) -> None: ...
    EventSysId: str
    """ID associated with the measurement event"""
    BuildLabel: str
    """Build label for the measurement event"""
    EventType: str
    """The type of event such as "N"(Normal), "H"(Hold) and "D"(Duplicate)"""
    EventDatetime: str
    """
            The date and time at which the event (eventSysId)
            was measured
            """
    VehicleProgram: str
    """The vehicle program associated with the routine"""
    PhaseName: str
    """Phase for e.g. production and pre-production, during which the event is measured"""
    PlantId: str
    """Plant ID in which the routine is measured"""
    RoutineId: str
    """Item ID of the routine which is measured"""
    RoutineRev: str
    """Revision associated with the routineId"""
    DeviceType: str
    """Device type of the measurement event such as "CMM", "Vision" an "Hand Held""""
    PartName: str
    """Name of the measured part"""
    Device: str
    """Device used to measure the event of the routine"""
    ShiftNumber: int
    """Shift with possible values of "0","1","2","3", or "4""""
    UtcTime: str
    """The UTC time in "dd-mon-yy HH24:MI:SS" format"""
    ShiftDay: str
    """
            Is the production day which may not be the same as calendar day for e.g. all events
            measured after 10 pm the previous day may have the shiftDay
            of today
            """
    HiLow: str
    """A value which specifies if the routine is measured with high or low frequency"""
    Active: int
    """
            Specifies the active status of the event ("1" for active and "0" for
            inactive)
            """

class EventResults:
    """
    The EventResults structure is used to show the output
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with the input structure
            
"""
    EventsSet: list[Event]
    """Data associated with measurement event such as device type, part name, etc"""

class QueryActiveOrDeactiveDataResponse:
    """
    
The QueryActiveOrDeactiveDataResponse structure is used to return the all column
of the DIS_MEASMT_EVENT table and servicedata
    """
    def __init__(self, ) -> None: ...
    Events: list[EventResults]
    """
            A list of event results with data associated with measurement event such as device
            type, part name, etc
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class SearchCriteria:
    """
    The SearchCriteria structure is used to get active or deactive measurement data
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with the input structure
            """
    PlantId: str
    """ID of the plant for the search criteria"""
    RoutineId: str
    """ID of the routine for the search criteria"""
    FromDate: System.DateTime
    """The start date and time associated with the search criteria"""
    ToDate: System.DateTime
    """The end date and time associated with the search criteria"""
    Jsn: str
    """
            Job Serial Number (JSN): An alphabetic and/or numeric combination that identifies
            a collection of measurement data resulting from a specific analysis job or assembly
            build. Such data generally  records the measured location of holes, pins, slots,
            tabs  and surface planes for each manufactured part or assembly
            """
    ActiveInactive: str
    """
            This is string value to specify what data to get ("ACTIVE": active events,
            "INACTIVE": inactive events, "ALL": active and inactive events)
            """

class MeasurementDataQuery:
    """
    Interface MeasurementDataQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryActiveOrDeactiveData(self, SearchCriterion: list[SearchCriteria]) -> QueryActiveOrDeactiveDataResponse:
        """    
             This operation gives the measurement event information stored in the DIS_MEASMT_EVENT
             table.
             

Use Cases:

             DPVMeasurements functionality in Teamcenter rich client can be used to display measurement
             event values.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param SearchCriterion: 

        :return: holds model objects and partial errors. No model
             objects are returned in this operation. Also, no specific partial error is returned
             by this operation and only errors from underlying subsystems are returned.
        """
        ...

