import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class DateTimeRange:
    """
    The DateTimeRange structure represents the time at the beginning and end of the
range.
    """
    def __init__(self, ) -> None: ...
    FromDateTime: str
    """
            The time at the beginning of the date time range in the format "MM-DD-YYYY HH24:MI:SS"
            
"""
    ToDateTime: str
    """
            The time at the end of the date time range in the format "MM-DD-YYYY HH24:MI:SS"
            
"""

class EngineeringData:
    """
    
The EngineeringData structure represents all of the information about
Engineering
data Parameters.
    """
    def __init__(self, ) -> None: ...
    Additionalinfo: System.Collections.Hashtable
    """Reserved for future use"""
    Plantid: str
    """Plant item ID pertaing to a routineid"""
    Vehicleprogram: str
    """Vehicle program name associated with the routineid"""
    Devicetype: str
    """
            The device type used to measure a routine (routineid),
            such as "CMM", "Vision", and "Hand Held"
            """
    Partnames: str
    """Part name of the measurement routine (routineid)"""
    Routineid: str
    """Item ID of type MEInspection"""
    Routinerev: str
    """Revision of the routineid"""
    Device: str
    """Device ID used to measure the routinerev"""
    Phasename: str
    """The production phase of the routinerev"""
    Eventtypes: str
    """The measurement event type, such as "N" (Normal) and "D" (Duplicate)"""

class EngineeringResponse:
    """
    
The EngineeringResponse structure represents the vector of responses depending
on
the operationType.
    """
    def __init__(self, ) -> None: ...
    Response: list[Response]
    """The list of responses"""
    PartialErrors: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data object with any partial errors"""

class JobRange:
    """
    The JobRange structure represents the beginning and end of job range.
    """
    def __init__(self, ) -> None: ...
    FromJob: str
    """The build label of the beginning job of the job range"""
    ToJob: str
    """The build label of the ending job of the job range"""
    DateTimeRange: DateTimeRange
    """
            The data range within which the from and to builds need to be queried. Builds outside
            the date range will be ignored
            

"""

class MeasurementsTicketResponse:
    """
    
The MeasurementsTicketResponse structure represents the mapping of client id to
measurement
ticket
    """
    def __init__(self, ) -> None: ...
    MeasurementTicketsInfo: System.Collections.Hashtable
    """
            A map of input parameter clientId, which
            is the key, and the file ticket to measurement file containing engineering and measurement
            data pertaining to the clientId

"""
    PartialErrors: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class SingleJob:
    """
    The SingleJob structure represents the single job
    """
    def __init__(self, ) -> None: ...
    Job: str
    """A build label"""
    DateTimeRange: DateTimeRange
    """
            The data range within which the job need to be queried. Builds outside the date range
            will be ignored
            
"""

class QueryRange:
    """
    The QueryRange structure represents the user query information.
    """
    def __init__(self, ) -> None: ...
    QueryLastXjobs: int
    """Last number of builds"""
    QueryLastXhrs: int
    """Last number of hours"""
    QueryLastXmin: int
    """Last number of minutes"""
    QueryDateTimeRange: DateTimeRange
    """
            A date time range with from and to values in the format "MM-DD-YYYY HH24:MI:SS"
            
"""
    QueryJobRange: JobRange
    """A range of build labels"""
    QuerySingleJob: SingleJob
    """One build label"""
    Additionalinfo: System.Collections.Hashtable
    """This is for future use and not currently used"""

class Response:
    """
    
The Response structure represents the id and displayname of each attribute that
defined
in EngineeringData struct.
    """
    def __init__(self, ) -> None: ...
    Additionalresponses: System.Collections.Hashtable
    """Reserved for future use"""
    Id: str
    """Identifier of the object/information requested"""
    Displayname: str
    """Display name of the object/information requested"""

class SearchCriteriaInfo:
    """
    
The SearchCriteriaInfo structure represents the whole information about the
search
criteria.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            associated with this input structure
            """
    EnggData: EngineeringData
    """
            This is primarily the ItemRevision of a routine. It has associated data such
            as plant ID, vehicle program, and device ID
            """
    ShiftNumber: int
    """
            The shift filter to be applied to the search criteria. The allowed values are between
            '0' and '4', inclusive. Any other values will be ignored and a default
            of '0' will be used instead. If the value is '0', it indicates measurement
            data for all shifts
            """
    Filter: str
    """
            The type of queryRange with possible values
            of 'LAST_N_JOBS', 'LAST_N_HRS','LAST_N_MIN','DATETIME_RANGE','JSN_RANGE','JSN'
            """
    QueryRange: QueryRange
    """
            A specification of a range to be applied as a filter
            for the measurement data. The type of the queryRange is determined by the filter parameter. This has the details of all possible query ranges
            but only the details pertaining to filter parameter will be used to filter the measurement
            data
            """

class MeasurementDataQuery:
    """
    Interface MeasurementDataQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetMeasurementTicket(self, Request: list[SearchCriteriaInfo]) -> MeasurementsTicketResponse:
        """    
             Given a search criteria with primarily the routine revision and filter data, such
             as last number of builds and date range, this operation gives a text file with engineering
             data and measurement data for the routine revision.
             

Use Cases:

             The DPV Reporting & Analysisi client application in standalone Teamcenter lifecycle
             visualization queries Teamcenter for engineering and measurement data of a routine
             revision
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param Request: 
                         A list of <font face="courier" height="10">SearchCriteriaInfo</font> structures.
                         This has a <font face="courier" height="10">clientId</font> key provided as an input.
                         Also, it includes the engineering data for which a query is to be performed.  In
                         addition,  it includes the shift and query criteria to filter the measurement data.
                         The clientId is a key for the remaining data in the <font face="courier" height="10">SearchCriteriaInfo</font>
                         and is used in the output parameter to represent the complete <font face="courier" height="10">SearchCriteriaInfo</font>

        :return: key and a measurement ticket for the file that contains the requested engineering
             and measurement data.
        """
        ...
    def QueryEngineeringParameters(self, OperationType: str, Request: EngineeringData) -> EngineeringResponse:
        """    
             This operation gets data pertaining to a MEInspection (routine) depending
             on what is specified in the operationType
             parameter. For example, if the desired data is program then the operation type should
             be set to 'Program'. The values are obtained by querying the measurement databases
             for the routines.
             

Use Cases:

             This operation is used by the DPV Reporting & Analysis application in standalone
             Teamcenter lifecycle visualization to query routine data.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param OperationType: 
                         Determines what operation will be performed.  Possible values for this are   <i>"Program</i>",<i>"DeviceType</i>",<i>"Part</i>",<i>"Routine</i>",<i>"DeviceID</i>",
                         <i>"Phase</i>", and <i>"EventType</i>". The order of the possible values mentioned
                         here and in the EngineeringData structure from the top upto  the <font face="courier" height="10">routineid</font> is important.The <font face="courier" height="10">additionalinfo</font>
                         parameter is not used. For any structure element that is queried for, all the information
                         above it should be provided. However, no input information for structure elements
                         below the routineid parameter is required. For example, if the "<i>DeviceType</i>"
                         information is required, the <font face="courier" height="10">plantid</font> and
                         <font face="courier" height="10">vehicleprogram</font> information should be filled
                         in the <font face="courier" height="10">EngineeringData</font> structure. Similarly
                         for routineid, the plantid, vehicleprogram, devicetype, and partnames should be sent
                         in the input. Also, as no input information for structure elements below the routineid
                         parameter is required, for example, if the "<i>EventType</i>" is required, there
                         is no need to specify routinerev, device or phasename
             
        :param Request: 
                         Has the different input parameters. The output parameter will be filled in based
                         on the <font face="courier" height="10">operationType</font>. What data needs to
                         be sent in as part of the input parameter is described under <font face="courier" height="10">operationType</font>

        :return: holds model objects and partial errors. No model
             objects are returned in this operation. Also, no specific partial error is returned
             by this operation and only errors from underlying subsystems are returned.
        """
        ...

