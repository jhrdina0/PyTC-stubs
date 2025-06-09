import System
import Teamcenter.Soa.Client.Model
import typing

class AttrLimits:
    """
    The AttrLimits structure is used to give the reject or spec limits for a
attribute
    """
    def __init__(self, ) -> None: ...
    FtrUid: str
    """
            UID of the feature to which the attribute or ftrattCode
            belongs
            """
    FtrattCode: str
    """Feature attribute code"""
    Lsl: float
    """Lower specification limit for the attribute or ftrattCode"""
    Usl: float
    """Upper specification limit for the attribute or ftrattCode"""

class FtrActual:
    """
    The FtrActual structure is used to give details of measurement made for an
attribute
    """
    def __init__(self, ) -> None: ...
    FtrUid: str
    """ID of the feature"""
    FtrName: str
    """Name of the feature"""
    FtrattCode: str
    """Feature attribute code"""
    ActualValue: float
    """The measured value for the feature attribute for a given measurement event"""

class Limit:
    """
    The Limit structure is used to give the reject or spec limit information
    """
    def __init__(self, ) -> None: ...
    PlantId: str
    """Item ID of the plant. This is used to identify the measurement database"""
    RoutineId: str
    """Item ID of the routine"""
    RoutineRev: str
    """Revision of the routine"""
    DeviceType: str
    """
            Device type of the measurement event, such as 'CMM', 'Vision' and 'Hand
            Held'
            """
    CreationTime: str
    """Creation time in "dd-mon-yy HH24:MI:SS" format"""
    Success: bool
    """
            Success or failure of limit insertion. Fails even if one of the limit insertions
            fail
            """
    FtrLimits: list[AttrLimits]
    """List of attribute specification limits"""

class LimitInsertResponse:
    """
    The LimitInsertResponse structure is used to return the status of insertions
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The  Service Data"""

class LogData:
    """
    The LogData structure is used to give event data to be inserted
    """
    def __init__(self, ) -> None: ...
    EventTime: str
    """Event date time in "dd-mon-yy HH24:MI:SS" format"""
    UploadTime: str
    """Upload time in "dd-mon-yy HH24:MI:SS" format"""
    PlantId: str
    """Item id of the plant"""
    DeviceId: str
    """Device identifier for the measurement event"""
    Jsn: str
    """Job sequence number or label for the measurement event"""
    ScriptId: str
    """
            Item ID of type "InspectionDevice" for the parsing script that processes the
            measurement event data
            """
    ScriptRev: str
    """Script revision of the scriptId"""
    RoutineId: str
    """Item ID of the routine"""
    RoutineName: str
    """Name of the routine"""
    FileName: str
    """Feature label pertaining to the errorCode"""
    UrlToDevice: str
    """URL of device that measures the routine for the measurement event"""
    FeatureName: str
    """Feature Name"""
    AttributeId: str
    """Attribute code pertaining to the errorCode"""
    ErrorCode: int
    """Error code for the measurement event"""
    ErrorMessage: str
    """Error message for the measurement event"""
    IFail: int
    """Failure code for the measurement event"""

class LogInsertResponse:
    """
    The LogInsertResponse structure is used to return the status of insertions
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data object with the error messages for the failed insertions"""

class MeasmtData:
    """
    The MeasmtData structure is used to give event data to be inserted
    """
    def __init__(self, ) -> None: ...
    BuildLabel: str
    """Build label of the measurement event"""
    EventType: str
    """Event type of the measurement event"""
    EventDateTime: str
    """Event execution date time in "dd-mon-yy HH24:MI:SS" format"""
    VehicleProgram: str
    """Vehicle program name associated with the measurement event"""
    PhaseName: str
    """Phase name associated with the measurement event"""
    PlantId: str
    """Item ID of the plant associated with the measurement event"""
    RoutineId: str
    """Revision of the routine associated with the measurement event"""
    RoutineRev: str
    """Revision of the routine"""
    DeviceType: str
    """
            Device type of the measurement event such as 'CMM', 'Vision' an 'Hand
            Held'
            """
    PartName: str
    """Part name of the measurement event"""
    Device: str
    """Device identifier of the measurement device"""
    ShiftNumber: int
    """
            Shift number ('0', '1', '2', '3' or '4') of the
            measurement event.
            
            "0" means shift information is not given. "1" means morning, "2" means afternoon,
            "3" means evening and "4" means night shifts
            
"""
    UtcTime: str
    """Event execution time in UTC. Date format "dd-mon-yy HH24:MI:SS""""
    ShiftDay: str
    """Shift day time in "dd-mon-yy HH24:MI:SS" format"""
    FtrInput: list[FtrActual]
    """
            List of feature actual information including feature attribute codes and corresponding
            measured values for one measurement event
            """
    TraceInput: list[TraceEvent]
    """List of trace code values for one measurement event"""

class MeasmtLoadResponse:
    """
    The MeasmtLoadResponse structure is used to return the event sys id and error
information
    """
    def __init__(self, ) -> None: ...
    EventSysId: list[str]
    """
            A list of  event system IDs corresponding to each MeasmtData
            provided in the input
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The  Service  Data"""

class NewEventInfo:
    """
    The NewEventInfo structure is used to give the reject or spec limits for a
attribute
    """
    def __init__(self, ) -> None: ...
    PlantId: str
    """
            Item  ID of the plant of type MEPrPlantProcess. The plant information is used
            to determine in which measurement database the eventSysId
            is stored
            """
    EventSysId: str
    """The event system ID of the measurement event"""
    ColumnName: str
    """
            Column of the value to be modified in the DIS_MEASMT_EVENT
            table
            """
    NewValue: str
    """
            The value to be set in the column identied by the columnName
            for the eventSysId
"""

class TraceEvent:
    """
    The TraceEvent structure is used to give details of event trace information
    """
    def __init__(self, ) -> None: ...
    TraceCode: str
    """Trace code for a measurement event,  fo rexample, 'Operator'"""
    EventTraceCodeValue: str
    """
            The value of the traceCode for the measurement event, for example, 'Mike'
            for a traceCode of 'Operator'
            
"""

class UpdateEventResponse:
    """
    The UpdateEventResponse structure is used to return the status of insertions
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The  Service  Data"""

class MeasurementDataLoad:
    """
    Interface MeasurementDataLoad
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def InsertEventTrace(self, PlantId: str, EventSysId: str, EventTraceval: list[TraceEvent]) -> bool:
        """    
             This operation inserts trace codes and the corresponding values into the measurement
             database, given the measurement event sys ID and plant item ID.
             

Use Cases:

             The external Extraction Transfer and Load (ETL) application adds the trace codes
             and corresponding values to the measurement database after adding measurement event
             and feature attribute values.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param PlantId: 
                         The plant item ID to which the measurement event or <font face="courier" height="10">eventSysId</font>
                         belongs. The plant ID information is used to identify the measurement database to
                         which the trace code information is to be added
             
        :param EventSysId: 
                         The measurement event for which the <font face="courier" height="10">eventTraceval</font>
                         is to be added
             
        :param EventTraceval: 
                         A structure that includes trace codes and corresponding event trace code values for
                         the measurement event or <font face="courier" height="10">eventSysId</font>

        :return: ' for failure.
        """
        ...
    def InsertFeatureActuals(self, PlantId: str, EventSysId: str, FeatureActuals: list[FtrActual]) -> bool:
        """    
             Inserts the given set of feature actual values into the measurement database for
             a measurement event. This operation is used to add measurement data for a single
             measurement event.
             

Use Cases:

             External applications, such as Extraction Transfer and Load (ETL), use this operation
             to store feature actual data into the measurement database for a measurement event.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param PlantId: 

        :param EventSysId: 
                         ID for the measurement event
             
        :param FeatureActuals: 

        :return: ' for failure.
        """
        ...
    def InsertLimitData(self, TargetTable: str, LimitInput: list[Limit]) -> LimitInsertResponse:
        """    
             Inserts the given set of specification limit data for a feature attribute.
             

Use Cases:

             An external application, such as Extraction Transfer and Load (ETL), uses this operation
             to insert the given set of specification limit data for a feature attribute.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param TargetTable: 

        :param LimitInput: 
                         A list used to give the reject or specification  limit information
             
        :return: The ServiceData  holds model objects and partial errors. No model objects are returned
             in this operation. Also, no specific partial error is returned by this operation
             and only errors from underlying subsystems are returned.
        """
        ...
    def InsertLogData(self, LogInput: list[LogData]) -> LogInsertResponse:
        """    
             This operation inserts the log data into the measurement database. The log data has
             error and warning messages pertaining to a measurement event.
             

Use Cases:

             External application, such as Extraction Transfer and Load (ETL), insert measurement
             data into measurement database using other operations in the MeasurementDataLoad service. The log information is entered into
             the DPV_LOG_INFO table of measurement database
             for every event whether the data insertion was successful or not
             

Dependencies:

             insertMeasurementData
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param LogInput: 
                         A list of log values for a measurement event
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def InsertMeasurementData(self, Rawdata: list[MeasmtData]) -> MeasmtLoadResponse:
        """    
             This operation inserts the given measurement data including event parameters, measured
             feature attribute values and trace code information. It returns event system IDs
             on successful completion of the insertions. This inserts all the feature attribute
             measurement values pertaining to several measurement events in bulk.
             

Use Cases:

             This operation is used by external application such as Extraction Transaction and
             Load (ETL) to insert measurement data into measurement database.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param Rawdata: 
                         The measurement data including event parameters, measured feature attribute values
                         and trace code information
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def UpdateEventColumn(self, EventInfo: list[NewEventInfo]) -> UpdateEventResponse:
        """    
             This operation updates the Active column value of the DIS_MEASMT_EVENT
             table  to '1' (active) or '0' (inactive) for  the given event information.
             The event information contains the plantId
             and eventSysId.  The plantId is used to identify the external measurement database
             that contains the events for the plant.
             

Use Cases:

             This operation is used by external application, such as Extraction Transfer and Load
             (ETL) to update a column value in DIS_MEASMT_EVENT
             table with the given input event information.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param EventInfo: 

        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...

