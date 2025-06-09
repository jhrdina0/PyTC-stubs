import System
import Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery
import Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad
import Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataLoad
import Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataQuery
import Teamcenter.Services.Strong.Productionmanagement._2008_03.EngineeringDataQuery
import Teamcenter.Services.Strong.Productionmanagement._2008_03.MeasurementDataEdit
import Teamcenter.Services.Strong.Productionmanagement._2008_03.MeasurementDataQuery
import Teamcenter.Services.Strong.Productionmanagement._2008_06.EngineeringDataQuery
import Teamcenter.Services.Strong.Productionmanagement._2008_06.MeasurementDataQuery
import Teamcenter.Services.Strong.Productionmanagement._2010_04.MeasurementDataQuery
import Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataLoad
import Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery
import Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class EngineeringDataLoadRestBindingStub(EngineeringDataLoadService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ImportFeatureData(self, Input: list[Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataLoad.RoutineAndFile]) -> Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataLoad.ImportFeatureDataResponse: ...
    def CreateRelBwDsRoutineRev(self, XlsbDs: Teamcenter.Soa.Client.Model.Strong.Dataset, RoutineRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class EngineeringDataLoadService:
    """
    
            The EngineeringDataLoad service exposes operations that import
feature data for a
            routine revision and create relationship between a routine revision
and a Dpv0ruleset
            item.

            This service provides the following use cases:

Import an xml file with Feature data in the Manufacturing Process
            Planner (MPP) application in the Teamcemcenter rich client by
selecting a Routine
            Revision of the type MEInspection_Revision and then using the
Tools|'Import
            Feature Data' menu option.

In the MPP application, a user can associate a Dpv0ruleset
            item to  a routine revision after selecting a routine revision and
choosing the Tools|'Import
            Feature Data' menu option.

In the MPP application, a user can associate a Dpv0ruleset
            item to  a routine revision by right-clicking the routine revision
and then selecting
            "Apply Rule Set" from the ensuing context menu.

Library Reference:

TcSoaProductionManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> EngineeringDataLoadService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ImportFeatureData(self, Input: list[Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataLoad.RoutineAndFile]) -> Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataLoad.ImportFeatureDataResponse:
        """    
             This operation uploads the feature data for a routine revision. A routine revision
             is an ItemRevision of the type MEInspection_Revision. This operation
             takes an FMS file ticket of an XML file containing engineering data of a routine,
             such as feature ID, feature name, feature attributes and specification limits, as
             an input. It creates a DPVExcel dataset under the routine revision with an
             IMAN_specification relation on successful
             execution of the operation. All the features and attributes in the XML file are included
             in the DPVExcel  dataset.
             

Use Cases:

             Import an XML file in Manufacturing Process Planner (MPP) application in the Teamcenter
             rich client by selecting a routine revision of type MEInspection_Revision
             and usinging the Tools|"Import Feature Data" menu option.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param Input: 
                         A list of feature import data. Each element has the routine revision object for which
                         the feature data is to be imported, the FMS file ticket for an XML file with feature
                         data for the routine revision,  the name of the <b>DPVExcel</b> dataset that is to
                         be attached to the routine revision, and a description of the <b>DPVExcel</b> dataset
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def CreateRelBwDsRoutineRev(self, XlsbDs: Teamcenter.Soa.Client.Model.Strong.Dataset, RoutineRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates a Dpv0CustomRoutineRuleset  relationship between a
             Dpv0ruleset  and a routine revision (MEInspection_Revison). The operation
             determines the Dpv0ruleset from the xlsbDs,
             which is associated to any revision of the Dpv0ruleset.
             

Use Cases:

             In the Manufacturing Process Planner (MPP) application in the Teamcenter rich client,
             a user can associate a Dpv0ruleset  with  a routine revision via Tools|"Import
             Feature Data" after a routine revision is selected.
             

             In the MPP application, a user can associate a Dpv0ruleset  with  a routine
             revision by right-clicking the routine revision and selecting "Apply Rule Set" from
             the ensuing context menu.
             


Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param XlsbDs: 
                         The <b>Dpv0RuleSetDataset</b> dataset attached to a<b> Dpv0rulesetRevision</b>

        :param RoutineRev: 
                         A routine revision of type <b>MEInspection_Revison</b>

        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...

class EngineeringDataQueryRestBindingStub(EngineeringDataQueryService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetDatabaseDetailsForPlant(self, Plantids: list[str]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.DatabaseDetailsResponse: ...
    def GetEngineeringDataFromRoutine(self, RoutineIdVer: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.RoutineIdVer]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.RoutineQryResponse: ...
    def GetFeatureAttributeDataOfCluster(self, ClusterIdentifier: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.ClusterIdentifier]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.ClusterQryResponse: ...
    def GetEngineeringDataFromRoutine2(self, RoutineIdVer: list[Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataQuery.RoutineIdVer2]) -> Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataQuery.RoutineQryResponse2: ...
    def GetFeatureAttributeDataOfCluster2(self, ClusterIdentifier: list[Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataQuery.ClusterIdentifier2]) -> Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataQuery.ClusterQryResponse2: ...
    def GetEngineeringDataFromRoutine3(self, RoutineIdVer: list[Teamcenter.Services.Strong.Productionmanagement._2008_03.EngineeringDataQuery.RoutineIdVer3]) -> Teamcenter.Services.Strong.Productionmanagement._2008_03.EngineeringDataQuery.RoutineQryResponse3: ...
    def GetMappedFeatureData(self, Request: list[Teamcenter.Services.Strong.Productionmanagement._2008_06.EngineeringDataQuery.RoutineSetInfo]) -> Teamcenter.Services.Strong.Productionmanagement._2008_06.EngineeringDataQuery.MappedFeatureResponse: ...
    def GetFeatureAttributesForSpec(self, InputToGetFtrAtt: list[Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.InputToGetAttrCode]) -> Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.GetFtrAttResponse: ...
    def GetSpecificationLimits(self, SpecLimitInput: list[Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.GetSpecLimitInput]) -> Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.GetSpecLimitInfoResponse: ...
    def GetSpecSheetNames(self, PlantAndRtnInfo: list[Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.InputToGetSpecSheetNames]) -> Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.SpecInfoResponse: ...

class EngineeringDataQueryService:
    """
    
            The EngineeringDataQuery service exposes operations that are used to
query engineering
            data of plants, routines, and clusters.

            This service provides the following use cases:

Get database details of a plant

Get feature attribute, specification limits, and data load information
            for a routine revision

Get the mapped feature data given two routine revisions

Get feature attributes associated with a DPVCluster_Revision

Library Reference:

TcSoaProductionManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> EngineeringDataQueryService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetDatabaseDetailsForPlant(self, Plantids: list[str]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.DatabaseDetailsResponse:
        """    
             Given a list of plant IDs, for each plant ID, this operation returns the database
             name of the database that contains measurement data for the plant, the server in
             which the database resides, and the type of database. There are two possible types
             of databases: 'Oracle' and 'MSSQL'.
             

Use Cases:

             Dimensional Planning and Validation (DPV) Analysis Services client application queries
             Teamcenter for the plant details.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param Plantids: 
                         List of plant IDs whose database information is required
             
        :return: holds
             model objects and partial errors. No model objects are returned in this operation.
             Also, no specific partial error is returned by this operation and only errors from
             underlying subsystems are returned.
        """
        ...
    def GetEngineeringDataFromRoutine(self, RoutineIdVer: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.RoutineIdVer]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.RoutineQryResponse:
        """    
             Get the Engineering Data for a given Routine.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param RoutineIdVer: 
                         The Item Id and Revision of the Routine
             
        :return: Has the engineering data (Features, Feature Attributes and Forms attached to Feature
             Attributes) of the given routine
        """
        ...
    def GetFeatureAttributeDataOfCluster(self, ClusterIdentifier: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.ClusterIdentifier]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.EngineeringDataQuery.ClusterQryResponse:
        """    
             Get the contents of a given Cluster.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param ClusterIdentifier: 
                         The Item Id, Revision of the Routine and the Cluster ref
             
        :return: Has the Feature Attributes clustered and Forms attached to Feature Attributes along
             with the parent feature occurrence
        """
        ...
    def GetEngineeringDataFromRoutine2(self, RoutineIdVer: list[Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataQuery.RoutineIdVer2]) -> Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataQuery.RoutineQryResponse2:
        """    
             Get the Engineering Data for a given Routine.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param RoutineIdVer: 
                         The Item Id and Revision of the Routine
             
        :return: Has the engineering data (Features, Feature Attributes and Forms attached to Feature
             Attributes) of the given routine
        """
        ...
    def GetFeatureAttributeDataOfCluster2(self, ClusterIdentifier: list[Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataQuery.ClusterIdentifier2]) -> Teamcenter.Services.Strong.Productionmanagement._2007_12.EngineeringDataQuery.ClusterQryResponse2:
        """    
             For a DPVCluster_Revision, this operation provides all the feature attributes
             that belong to it. The feature attribute information includes the feature ID, feature
             name, and attribute code for each feature attribute in the cluster.
             

Use Cases:

             Client applications, such as standalone Teamcenter lifecycle visualization, query
             Teamcenter for cluster information.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param ClusterIdentifier: 

        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def GetEngineeringDataFromRoutine3(self, RoutineIdVer: list[Teamcenter.Services.Strong.Productionmanagement._2008_03.EngineeringDataQuery.RoutineIdVer3]) -> Teamcenter.Services.Strong.Productionmanagement._2008_03.EngineeringDataQuery.RoutineQryResponse3:
        """    
             This operation returns the engineering data of routine revisions. A routine revision
             is an ItemRevision of  type MEInspection_Revision. The engineering
             data includes information, such as features, feature attributes, and specification
             limits associated with feature attributes.
             

Use Cases:

             External client applications, such as standalone Teamcenter  lifecycle visualization
             and Extracttion Transactaction and Load(ETL) query for engineering data from Teamcenter.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param RoutineIdVer: 
                         A list of <b>Item</b> IDs and revisions of routines
             
        :return: holds model objects and partial errors. No model
             objects are returned in this operation. Also, no specific partial error is returned
             by this operation and only errors from underlying subsystems are returned.
        """
        ...
    def GetMappedFeatureData(self, Request: list[Teamcenter.Services.Strong.Productionmanagement._2008_06.EngineeringDataQuery.RoutineSetInfo]) -> Teamcenter.Services.Strong.Productionmanagement._2008_06.EngineeringDataQuery.MappedFeatureResponse:
        """    
             This operation returns a set of mapped features for each pair of routine revisions
             in the request list. For each pair of routine revisions, the mapped feature information
             maps a subset of features in the second routine to features in the first routine
             revision. This map information is for features and not feature attributes. If one
             feature is mapped to another feature, then all the common attribute codes between
             the two features are mapped that is, there is no way to map select attribute codes
             under a feature).
             

Use Cases:

             The DPV Reporting & Analysis client application in standalone Teamcenter lifecycle
             visualization queries Teamcenter for mapped features between two routine revisions.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param Request: 
                         A list of routine set information structures. Each structure contains a <font face="courier" height="10">clientId</font> and a pair of routine revisions for which the mapped
                         feature information is requested. The <font face="courier" height="10">clientId</font>
                         is a unique integer and a key that represents the pair of routine revisions in the
                         structure. It is the responsibility of the user to ensure that the <font face="courier" height="10">clientId</font> is unique
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def GetFeatureAttributesForSpec(self, InputToGetFtrAtt: list[Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.InputToGetAttrCode]) -> Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.GetFtrAttResponse:
        """    
             This operation gets all feature attribute codes (X deviation (X_DEV),Y deviation
             (Y_DEV) Z deviation( Z_DEV)) from a given specification sheet.
             

             The feature attribute codes are further used to query corresponding measurement data
             and engineering data based on search criteria
             


Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param InputToGetFtrAtt: 
                         This data is used as a search criteria to get the corresponding feature attributes
                         from a given specification sheet.
             
        :return: 
        """
        ...
    def GetSpecificationLimits(self, SpecLimitInput: list[Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.GetSpecLimitInput]) -> Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.GetSpecLimitInfoResponse:
        """    
             This operation gets all specification limits for a given feature attributes codes
             based on given search criteria.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param SpecLimitInput: 
                         This data is used as a search criteria to get the corresponding specification limits.
                         It includes date based and last number of processed jobs criteria.
             
        :return: 
        """
        ...
    def GetSpecSheetNames(self, PlantAndRtnInfo: list[Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.InputToGetSpecSheetNames]) -> Teamcenter.Services.Strong.Productionmanagement._2014_12.EngineeringDataQuery.SpecInfoResponse:
        """    
             This operation is using to get all spec sheet names available in an excel dataset
             of type DPVExcel attached to the given Operation Revision.
             

             The spec sheet names are further used to get all the defined data specific to that
             sheet. These sheets consist of Lower Specification Limit (LSL), Upper Specification
             Limit (USL) and Target values of a particular feature.
             


Use Cases:

Use Case 1: To know Available spec sheets for an excel sheet.

             Excel sheet might have 10's of spec sheets and user wants to know what they are so
             that he/she can choose any spec sheet to get further data from it to analyze it.
             


Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param PlantAndRtnInfo: 
                         This data is used as a search criteria to get all available specification sheet names.
             
        :return: 
        """
        ...

class MeasurementDataEditRestBindingStub(MeasurementDataEditService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ActivateOrDeactivateData(self, TargetRows: list[Teamcenter.Services.Strong.Productionmanagement._2008_03.MeasurementDataEdit.TargetEvents]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class MeasurementDataEditService:
    """
    
            The MeasurementDataEdit service exposes operations that are used to
activate or deactivate
            a measurement event.

            This service provides the following use cases:

Change the active status of measurement events using the Dimensional
            Planning and Validation (DPV) Measurement user interface in the rich
client interface.

Library Reference:

TcSoaProductionManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MeasurementDataEditService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ActivateOrDeactivateData(self, TargetRows: list[Teamcenter.Services.Strong.Productionmanagement._2008_03.MeasurementDataEdit.TargetEvents]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates the status of one or more measurement events specified in
             the list of TargetEvents to active or inactive.
             TargetEvents  includes a plant ID, measurement
             event that belongs to the plant ID, and its associated active status
             

Use Cases:

             Change the active status of measurement events using the Dimensional Planning and
             Validation (DPV) Measurement user interface in the Teamcenter rich client.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param TargetRows: 
                         A list of target events that  includes a plant ID, measurement event ID that belongs
                         to a plant ID, and an active status. Different <font face="courier" height="10">TargetEvents</font>
                         can have different active statuses.
             
        :return: holds model objects and partial
             errors. No model objects are returned in this operation. Also, no specific partial
             error is returned by this operation and only errors from underlying subsystems are
             returned.
        """
        ...

class MeasurementDataLoadRestBindingStub(MeasurementDataLoadService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def InsertEventTrace(self, PlantId: str, EventSysId: str, EventTraceval: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.TraceEvent]) -> bool: ...
    def InsertFeatureActuals(self, PlantId: str, EventSysId: str, FeatureActuals: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.FtrActual]) -> bool: ...
    def InsertLimitData(self, TargetTable: str, LimitInput: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.Limit]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.LimitInsertResponse: ...
    def InsertLogData(self, LogInput: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.LogData]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.LogInsertResponse: ...
    def InsertMeasurementData(self, Rawdata: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.MeasmtData]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.MeasmtLoadResponse: ...
    def UpdateEventColumn(self, EventInfo: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.NewEventInfo]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.UpdateEventResponse: ...
    def CreateLinkNames(self, LinkName: str, UserName: str, PassWord: str, DbName: str) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataLoad.CreateLinkNameInfoResponse: ...
    def PopulateLinkTables(self, PlantId: str, DbName: str, UserName: str, LinkName: str, TargetDbType: str, ServerName: str, UpdateTables: str, OldLinkName: str) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataLoad.PopulateLinkTablesResponse: ...

class MeasurementDataLoadService:
    """
    
            The MeasurementDataLoad service exposes operations that are used to
load the measurement
            data into database tables, as well as, populate database link
information.

            This service provides the following use cases:

External client applications, such as Extraction Transfer and Load
            (ETL), load the measurement data including feature actuals, event
trace, specification
            limits data, and event log data.

The Manufacturing Process Planner application in the rich client
            interface is used to store the database links into measurement
databases of the Dimensional
            Planning and Validation (DPV) application.

Library Reference:

TcSoaProductionManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MeasurementDataLoadService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def InsertEventTrace(self, PlantId: str, EventSysId: str, EventTraceval: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.TraceEvent]) -> bool:
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
    def InsertFeatureActuals(self, PlantId: str, EventSysId: str, FeatureActuals: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.FtrActual]) -> bool:
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
    def InsertLimitData(self, TargetTable: str, LimitInput: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.Limit]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.LimitInsertResponse:
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
    def InsertLogData(self, LogInput: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.LogData]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.LogInsertResponse:
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
    def InsertMeasurementData(self, Rawdata: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.MeasmtData]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.MeasmtLoadResponse:
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
    def UpdateEventColumn(self, EventInfo: list[Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.NewEventInfo]) -> Teamcenter.Services.Strong.Productionmanagement._2007_06.MeasurementDataLoad.UpdateEventResponse:
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
    def CreateLinkNames(self, LinkName: str, UserName: str, PassWord: str, DbName: str) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataLoad.CreateLinkNameInfoResponse:
        """    
             This operation will create database links to external databases, in the Teamcenter
             database. The link names will be stored in the USER_DB_LINKS system table of the
             Teamcenter database. The external databases store measurement data for the Dimensional
             Planning and Validation (DPV) application. The link names are used to store the measurement
             data and query measurement data from measurement database by external applications,
             such as Extraction Transaction and Load (ETL) and Teamcenter lifecycle visualization.
             


Use Cases:

             In the Manufacturing Process Planner application in the Teamcenter rich client, the
             send plant ID context menu under a MEPrPlantProcessRevision object is used
             to gather measurement database name, measurement database user name, measurement
             database password, and link name. Then, this operation is used to create the database
             link.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param LinkName: 

        :param UserName: 
                         User name for the external database, <font face="courier" height="10">dbName</font>

        :param PassWord: 
                         Password for the <font face="courier" height="10">userName</font> for the external
                         database, <font face="courier" height="10">dbName</font>

        :param DbName: 
                         The external database name to which a link is created
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def PopulateLinkTables(self, PlantId: str, DbName: str, UserName: str, LinkName: str, TargetDbType: str, ServerName: str, UpdateTables: str, OldLinkName: str) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataLoad.PopulateLinkTablesResponse:
        """    
             This operation will populate the DPV_DB_LOCATOR and DPV_LINK_LOCATOR  tables in the
             Teamcenter database. DPV_DB_LOCATOR table has plant ID(s) and database name(s). One
             plant ID can belong to only one database. DPV_LINK_LOCATOR  table has database names
             and corresponding database links.
             

Use Cases:

             Database links are used by external applications such as Extraction Transfer and
             Load (ETL) and standalone Teamcenter lifecycle visualization to insert data into,
             as well as, query from measurement databases.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param PlantId: 
                         The plant ID
             
        :param DbName: 

        :param UserName: 

        :param LinkName: 

        :param TargetDbType: 

        :param ServerName: 

        :param UpdateTables: 

        :param OldLinkName: 
                         The old link name will be used to update the tables
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...

class MeasurementDataQueryRestBindingStub(MeasurementDataQueryService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def QueryActiveOrDeactiveData(self, SearchCriterion: list[Teamcenter.Services.Strong.Productionmanagement._2008_03.MeasurementDataQuery.SearchCriteria]) -> Teamcenter.Services.Strong.Productionmanagement._2008_03.MeasurementDataQuery.QueryActiveOrDeactiveDataResponse: ...
    def GetMeasurementTicket(self, Request: list[Teamcenter.Services.Strong.Productionmanagement._2008_06.MeasurementDataQuery.SearchCriteriaInfo]) -> Teamcenter.Services.Strong.Productionmanagement._2008_06.MeasurementDataQuery.MeasurementsTicketResponse: ...
    def QueryEngineeringParameters(self, OperationType: str, Request: Teamcenter.Services.Strong.Productionmanagement._2008_06.MeasurementDataQuery.EngineeringData) -> Teamcenter.Services.Strong.Productionmanagement._2008_06.MeasurementDataQuery.EngineeringResponse: ...
    def QueryActiveOrDeactiveData2(self, SearchCriterion: list[Teamcenter.Services.Strong.Productionmanagement._2010_04.MeasurementDataQuery.SearchCriteria2]) -> Teamcenter.Services.Strong.Productionmanagement._2010_04.MeasurementDataQuery.QueryActiveOrDeactiveDataResponse2: ...
    def QueryPlantsInfo(self) -> Teamcenter.Services.Strong.Productionmanagement._2010_04.MeasurementDataQuery.PlantsInfoResponse: ...
    def QueryRoutinesInfo(self, PlantId: str) -> Teamcenter.Services.Strong.Productionmanagement._2010_04.MeasurementDataQuery.RoutinesInfoResponse: ...
    def QueryClusterGroupInfo(self, RoutineRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.ClusterGroupInfoResponse: ...
    def QueryCustomXlsbDs(self, XlsxDs: Teamcenter.Soa.Client.Model.Strong.Dataset) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.CustomXlsbDsResponse: ...
    def QueryLinkNamesInfo(self, DbType: str) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.LinkNamesInfoResponse: ...
    def QueryRuleSetDataSet(self) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.DpvRuleSetDsResponse: ...
    def QuerySsrsUrlInfo(self) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.SsrsUrlInfoResponse: ...

class MeasurementDataQueryService:
    """
    
            The MeasurementDataQuery service exposes operations that are used to
query data of
            plant Items of type MEPrPlantProcess, routine items of type
MEInspection.

            This service provides the following use cases:

Get all plant Item IDs, names, and database links associated with
            a plant.

Get Routine Item Revisions associated with a plant item.

Get the DPVClusterGroup information.

Get the plant, program, part, and so on information from Teamcenter
            so that a user can

            query for the required Routine Revision in standalone Teamcenter
lifecycle visualization.

Get measurement data associated with a MEInspection_Revision.

Get the Dpv0RuleSetDataset associated with a MEInspection_Revision.Get
            all the Dpv0RuleSetDataset(s) associated with the latest released
Dpv0rulesetRevison(s)

Get the URL information of SQL Server Reporting Services server of
            the Dimensional Planning and Validation (DPV) application.

Library Reference:

TcSoaProductionManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MeasurementDataQueryService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def QueryActiveOrDeactiveData(self, SearchCriterion: list[Teamcenter.Services.Strong.Productionmanagement._2008_03.MeasurementDataQuery.SearchCriteria]) -> Teamcenter.Services.Strong.Productionmanagement._2008_03.MeasurementDataQuery.QueryActiveOrDeactiveDataResponse:
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
    def GetMeasurementTicket(self, Request: list[Teamcenter.Services.Strong.Productionmanagement._2008_06.MeasurementDataQuery.SearchCriteriaInfo]) -> Teamcenter.Services.Strong.Productionmanagement._2008_06.MeasurementDataQuery.MeasurementsTicketResponse:
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
    def QueryEngineeringParameters(self, OperationType: str, Request: Teamcenter.Services.Strong.Productionmanagement._2008_06.MeasurementDataQuery.EngineeringData) -> Teamcenter.Services.Strong.Productionmanagement._2008_06.MeasurementDataQuery.EngineeringResponse:
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
    def QueryActiveOrDeactiveData2(self, SearchCriterion: list[Teamcenter.Services.Strong.Productionmanagement._2010_04.MeasurementDataQuery.SearchCriteria2]) -> Teamcenter.Services.Strong.Productionmanagement._2010_04.MeasurementDataQuery.QueryActiveOrDeactiveDataResponse2:
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
    def QueryPlantsInfo(self) -> Teamcenter.Services.Strong.Productionmanagement._2010_04.MeasurementDataQuery.PlantsInfoResponse:
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
    def QueryRoutinesInfo(self, PlantId: str) -> Teamcenter.Services.Strong.Productionmanagement._2010_04.MeasurementDataQuery.RoutinesInfoResponse:
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
    def QueryClusterGroupInfo(self, RoutineRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.ClusterGroupInfoResponse:
        """    
             This operation gives a list of DPVClusterGroup _Revision(s) associated with
             a routine revision. There is no direct relation between a routine revision and cluster
             group revisions. From the routine revision, a list of DPVCluster_Revision(s)
             related to it with Manifestation relation
             is obtained. Then for each DPVCluster, the DPVClusterGroup _Revision
             to which it is related with the DPVClusterGroupContent relation is obtained
             

Use Cases:

             In the Manufacturing Process Planner (MPP) application, a list of cluster groups
             associated with a routine revision is displayed via a context menu in the routine
             revision.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param RoutineRevs: 
                         A list of routine revisions. A routine revision is an item revision of type <b>MEInspection_Revision</b>

        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def QueryCustomXlsbDs(self, XlsxDs: Teamcenter.Soa.Client.Model.Strong.Dataset) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.CustomXlsbDsResponse:
        """    
             The operation gets the Dpv0RuleSetDataset datasets associated with a DPVExcel
             dataset. The Dpv0RuleSetDataset is a dataset attached to a Dpv0rulesetRevision.
             The DPVExcel  dataset is attached to MEInspection_Revision. There is
             a relationship Dpv0CustomRoutineRuleset  between MEInspection_Revision
             and Dpv0ruleset  and based on these relations, the  Dpv0RuleSetDataset
             datasets associated with a DPVExcel dataset are obtained.
             

Use Cases:

             Display the current Dpv0RuleSetDataset datasets associated with a MEInspection_Revision.
             This information is useful prior to associating a new Dpv0RuleSetDataset dataset
             to a MEInspection_Revision.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param XlsxDs: 
                         A DPVExcel dataset
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def QueryLinkNamesInfo(self, DbType: str) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.LinkNamesInfoResponse:
        """    
             This operation will list all the database links to the Dimension Planning and Validation
             (DPV) measurement databases. It is obtained from the USER_DB_LINKS and DPV_LINK_LOCATOR
             tables.
             

Use Cases:

             The "Send Pland ID..." context menu under a plant in the Manufacturing Process
             Planner (MPP) application displays all the available links in a dialog after it is
             selected.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param DbType: 
                         The database type of the DPV measurement database. Its possible values are "<i>ORACLE</i>",
                         "<i>SQLSERVER</i>", and "<i>SQLSEERVERLOCAL</i>"
             
        :return: is a combination of plant ID and link name with
             a comma delimiter. The ServiceData  holds model objects and partial errors. No model
             objects are returned in this operation. Also, no specific partial error is returned
             by this operation and only errors from underlying subsystems are returned.
        """
        ...
    def QueryRuleSetDataSet(self) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.DpvRuleSetDsResponse:
        """    
             List all the datasets of  type Dpv0RuleSetDataset associated with the latest
             released item revisions of all Dpv0ruleset(s).
             

Use Cases:

             List all the Dpv0RuleSetDataset datasets associated with the latest revisions
             of Dpv0ruleset items so they can be associated with a routine revision of
             type MEInspection_Revision.  The Dpv0RuleSetDataset contains validation
             rules that are used to verify the DPVExcel dataset associated with routine
             revisions.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :return: 
        """
        ...
    def QuerySsrsUrlInfo(self) -> Teamcenter.Services.Strong.Productionmanagement._2011_06.MeasurementDataQuery.SsrsUrlInfoResponse:
        """    
             This operation gives all the SQL Server Reporting Service (SSRS) server URLs stored
             in Teamcenter. These values are stored as values of the DPV_ccuaservice_url
             preference.
             

Use Cases:

             In the Manufacturing Process Planner (MPP) application, all the SSRS server URLs
             are listed so a user can choose one of them to upload a .rdl (Report Definition Language)
             to it.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :return: 
        """
        ...

