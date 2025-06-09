import System
import Teamcenter.Soa.Client.Model
import typing

class Event2:
    """
    
This structure consists of Measurement Event information and a vector of
corresponding
feature information.
    """
    def __init__(self, ) -> None: ...
    EventSysId: str
    """ID associated with the measurement event"""
    BuildLabel: str
    """Build label for the measurement event"""
    EventType: str
    """The type of event, such as "N"(Normal), "H"(Hold), and "D"(Duplicate)"""
    EventDatetime: str
    """
            The date and time at which the event (eventSysId)
            was measured
            """
    VehicleProgram: str
    """The vehicle program associated with the routine"""
    PhaseName: str
    """Phase  during which the event is measured (for example, production and pre-production)"""
    PlantId: str
    """Plant ID in which the routine is measured"""
    RoutineId: str
    """Item ID of the routine being measured"""
    RoutineRev: str
    """Revision associated with the routineId"""
    DeviceType: str
    """
            Device type of the measurement event, such as "CMM", "Vision" and "Hand
            Held"
            """
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
            The production day that may not be the same as the calendar day (for example,  all
            events measured after 10 pm the previous day may have the shiftDay
            of today)
            """
    HiLow: str
    """A value that specifies if the routine is measured with high or low frequency"""
    Active: int
    """The active status of the event ("1" for active and "0" for inactive)"""
    FtrsData: list[FtrInfo]
    """
            A list of feature information that includes all the features associated with the
            measurement event
            """
    TraceData: list[TraceInfo]
    """
            Certain tracking codes and values associated with the measurement event. For example,
            the code could be "Operator" and the value could be "Mike"
            
"""

class EventResults2:
    """
    
It will show the actual ouput of query; consists of Measurement Event
information
along with corresponding Feature information.
    """
    def __init__(self, ) -> None: ...
    ClientId2: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with the input structure
            
"""
    EventsSet2: list[Event2]
    """Data associated with measurement event such as device type, part name, and so on"""

class FtrInfo:
    """
    
It is a string with feature information including feature name (feature_name),
feature
attribute code (feature_att_code ) and actual measurement value (actual_value)
with
"."(dot) and ","(comma)

delimiters in the format "feature_name.feature_att_code,actual_value"

    """
    def __init__(self, ) -> None: ...
    FtrNameFtrAttCodeAval: str
    """
            It is a string with feature information including feature name (feature_name), feature
            attribute code (feature_att_code ) and actual measurement value (actual_value)  with
            "."(dot) and ","(comma)
            
            delimiters in the format "<feature_name>.<feature_att_code>,<actual_value>"
            
"""

class PlantResults:
    """
    This structure consits of Plant Information( Plant Id and Plant Name).
    """
    def __init__(self, ) -> None: ...
    PlantId: str
    """Item ID of the plant"""
    PlantName: str
    """Name of the plant"""

class PlantsInfoResponse:
    """
    
This structure consists of Vector which consists of a structure with the Plant
Information(Plant
Id and Plant Name). And it has a partial errors object giving error information,
if any
    """
    def __init__(self, ) -> None: ...
    PlantSet: list[PlantResults]
    """
            A  list of structures that consist of plant ID and name
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class QueryActiveOrDeactiveDataResponse2:
    """
    
This structure is used to return the all columns of the DIS_MEASMT_EVENT table
and
corresponding Feature info(Feature Name,Feature Attribute Code,Acutal Value)
from
DIS_MEASMT_FTR_ACTUAL table.
    """
    def __init__(self, ) -> None: ...
    Events2: list[EventResults2]
    """
            A list of event results with data associated with measurement event such as device
            type, part name, and so on
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class RoutineResults:
    """
    
This structure consits of Routine Information( Routine Id,Routine Name and
Routine
Revision).
    """
    def __init__(self, ) -> None: ...
    RoutineId: str
    """Item ID of a routine"""
    RoutineName: str
    """Name associated with the routineId"""
    RoutineRev: str
    """Revision of the routineId"""

class RoutinesInfoResponse:
    """
    
This structure consists of Vector which consists of a structure with the Routine
Information(Routine Id ,Routine Name and Routine Revision). And it has a partial
errors object giving error information, if any
    """
    def __init__(self, ) -> None: ...
    RoutineSet: list[RoutineResults]
    """A list of  structures that consists of routine item ID, name, and revision"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The  Service Data"""

class SearchCriteria2:
    """
    The SearchCriteria structure is used to get active or deactive mesurement data.
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
            build. Such data generally records the measured location of holes, pins, slots, tabs
            and surface planes for each manufactured part or assembly
            """
    ActiveInactive: str
    """
            The string value to specify what data to get ("ACTIVE": active events, "INACTIVE":
            inactive events, "ALL": active and inactive events)
            """

class TraceInfo:
    """
    
This structure contains the event trace information like trace code and event
trace
code value.
    """
    def __init__(self, ) -> None: ...
    TraceCode: str
    """
            Trace codes are information added to a measurement data file to define specific conditions
            that apply to a particular measurement (for example, product variants, such as having
            a sunroof or no sunroof)
            """
    TraceCodeValue: str
    """
            The value associated with the traceCode (usually
            for a measurement event
            """

class MeasurementDataQuery:
    """
    Interface MeasurementDataQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryActiveOrDeactiveData2(self, SearchCriterion: list[SearchCriteria2]) -> QueryActiveOrDeactiveDataResponse2:
        """    
             This operation gives the measurement event information stored in the DIS_MEASMT_EVENT
             table and the corresponding feature attribute measurement information, including
             feature name, feature attribute code, and the actual measurement value from the DIS_MEASMT_FTR_ACTUAL
             table.
             

Use Cases:

             The DPVMeasurements functionality in the Teamcenter rich client can be used to display
             measurement event and corresponding feature attribute measurement values.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param SearchCriterion: 

        :return: holds model objects and partial errors. No model
             objects are returned in this operation. Also, no specific partial error is returned
             by this operation and only errors from underlying subsystems are returned.
        """
        ...
    def QueryPlantsInfo(self) -> PlantsInfoResponse:
        """    
             This operation lists all the plants stored in the Teamcenter database based on the
             dpv_raw_data_location Teamcenter preference value. Plant information includes
             the plant item ID and name. If the dpv_raw_data_location preference value
             is "0" the plant information will be obtained from the Teamcenter database, otherwise;
             it is obtained from the "DPV_DB_LOCATOR" database table.
             

Use Cases:

             External applications, such as Teamcenter lifecycle visualization, and internal applications,
             such as DPVMeasurements, obtain the plant
             information before querying for measurement data.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :return: 
        """
        ...
    def QueryRoutinesInfo(self, PlantId: str) -> RoutinesInfoResponse:
        """    
             This operation will list information for routine revisions of type MEInspection_Revision
             given a plant item ID. The routine information includes routine item ID, routine
             name, and routine revision. If the Teamcenter dpv_raw_data_location preference
             value is "0" the information is obtained from the DPV_MEASMT_EVENT (non-pom table)
             in the Teamcenter database; otherwise, it is obtained from the DPV_MEASMT_EVENT table
             in an external measurement database.
             

Use Cases:

             The standalone Teamcenter lifecycle visualization application queries for routine
             information from Teamcenter.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param PlantId: 

        :return: holds model objects and partial errors.
             No model objects are returned in this operation. Also, no specific partial error
             is returned by this operation and only errors from underlying subsystems are returned.
        """
        ...

