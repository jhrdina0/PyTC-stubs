import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClusterData:
    """
    
The ClusterData structure is used return the engineering data belonging to the
cluster.
Each cluster has set of feature attributes These set of feature attributes are
captured
in a vector.
    """
    def __init__(self, ) -> None: ...
    Cluster: Teamcenter.Soa.Client.Model.Strong.AppearanceGroup
    """The Routine object to which the features belong"""
    FeatureAttributeInfo: list[FeatureAttributeInfo]
    """A vector of FeatureAttributeInfo structures"""

class RoutineIdVer:
    """
    
The RoutineIdVer structure is used give the information (i.e. item id and
revision)
of the routines of interest
    """
    def __init__(self, ) -> None: ...
    RoutineId: str
    """Item id of the routine"""
    RoutineRev: str
    """Routine revision of the routine"""

class ClusterIdentifier:
    """
    
The ClusterIdentifier structure is used give the information (i.e. routine id
and
revision and cluster ref) of the clusters of interest
    """
    def __init__(self, ) -> None: ...
    Cluster: Teamcenter.Soa.Client.Model.Strong.AppearanceGroup
    """Ref to the cluster"""
    RoutineIdRev: RoutineIdVer
    """RoutineIdVer structure with the routine information"""

class ClusterQryResponse:
    """
    
The ClusterQryResponse structure is used return the engineering data of a
cluster.
This structure has a ClusterData structure and the service data structure in it.
    """
    def __init__(self, ) -> None: ...
    ClusterData: list[ClusterData]
    """A vector of ClusterData structures with engineering data of a cluster"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data object"""

class DatabaseDetails:
    """
    The DatabaseDetails structure captures the database details for a plant
    """
    def __init__(self, ) -> None: ...
    PlantId: str
    """Plant ID whose database information is required"""
    DatabaseName: str
    """
            The name of the database that contains the measurement data for the plantId
"""
    DatabaseType: str
    """The type of database, which is 'Oracle' or 'MSSQL'"""
    HostName: str
    """The name of the hosting server of the database"""

class DatabaseDetailsResponse:
    """
    
The DatabaseDetailsResponse has the details of the dbs corresponding to the
given
input plant ids
    """
    def __init__(self, ) -> None: ...
    DatabaseDetails: list[DatabaseDetails]
    """
            Structures containing details of database such as database name, database type ('Oracle'
            or 'MSSQL'), as well as  a plant ID key for which the database information
            is sought
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data"""

class FeatureAttributeData:
    """
    
The FeatureAttributeData structure is used return the feature attribute
information
belonging to the routine
    """
    def __init__(self, ) -> None: ...
    FeatureAttribute: Teamcenter.Soa.Client.Model.ModelObject
    """Tag of the feature attribute"""
    FeatureAttributeForm: list[Teamcenter.Soa.Client.Model.Strong.Form]
    """Vector of POMRef of the form attached to the feature attribute"""

class FeatureAttributeInfo:
    """
    
The FeatureAttributeInfo structure is used return the feature attribute
information
belonging to the cluster
    """
    def __init__(self, ) -> None: ...
    ParentFeatureOccurrence: Teamcenter.Soa.Client.Model.ModelObject
    """
            Ref of the parent feature. Note that even though the variable name says occurrence,
            Tc2007.1 doesnt support occurrences. It is objects uid.
            """
    FeatureAttribute: Teamcenter.Soa.Client.Model.ModelObject
    """Tag of the feature attribute"""
    FeatureAttInfoForm: list[Teamcenter.Soa.Client.Model.Strong.Form]
    """Vector of POMRef of the form attached to the feature attribute"""

class FeatureData:
    """
    
The FeatureData structure is used return the feature information belonging to
the
routine. Each feature has set of feature attributes These set of feature
attributes
are captured in a vector.
    """
    def __init__(self, ) -> None: ...
    FeatureOccurrence: Teamcenter.Soa.Client.Model.ModelObject
    """
            The feature.  Note that even though the variable name says occurrence, Tc2007.1 doesnt
            support occurrences. It is objects uid.
            """
    FeatureAttributeData: list[FeatureAttributeData]
    """A vector of FeatureAttributeData structures"""

class RoutineData:
    """
    
The RoutineData structure is used return the engineering data belonging to the
routine.
Each routine has set of features These set of features are captured in a vector.
    """
    def __init__(self, ) -> None: ...
    Routine: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The Routine object to which the features belong"""
    FeatureData: list[FeatureData]
    """A vector of FeatureData structures"""

class RoutineQryResponse:
    """
    
The RoutineQryResponse structure is used return the engineering data of a
routine.
This structure has a RoutineData structure and the service data structure in it.
    """
    def __init__(self, ) -> None: ...
    RoutineData: list[RoutineData]
    """A vector of RoutineData structures with engineering data of a routine"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data object"""

class EngineeringDataQuery:
    """
    Interface EngineeringDataQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDatabaseDetailsForPlant(self, Plantids: list[str]) -> DatabaseDetailsResponse:
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
    def GetEngineeringDataFromRoutine(self, RoutineIdVer: list[RoutineIdVer]) -> RoutineQryResponse:
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
    def GetFeatureAttributeDataOfCluster(self, ClusterIdentifier: list[ClusterIdentifier]) -> ClusterQryResponse:
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

