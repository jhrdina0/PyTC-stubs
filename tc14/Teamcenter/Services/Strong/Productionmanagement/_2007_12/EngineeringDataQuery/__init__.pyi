import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClusterData2:
    """
    
The ClusterData2 structure is used return the engineering data belonging to the
cluster.
Each cluster has set of feature attributes These set of feature attributes are
captured
in a vector.
    """
    def __init__(self, ) -> None: ...
    Cluster: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """A DPVCluster_Revision"""
    FeatureAttributeInfo: list[FeatureAttributeInfo2]
    """A list of  feature attribute information associated with the cluster"""

class ClusterIdentifier2:
    """
    
The ClusterIdentifier2 structure is used give the information of the clusters of
interest
    """
    def __init__(self, ) -> None: ...
    ClusterRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """A DPVCluster_Revision"""

class ClusterQryResponse2:
    """
    
The ClusterQryResponse2 structure is used return the engineering data of a
cluster.
This structure has a ClusterData2 structure and the service data structure in
it.
    """
    def __init__(self, ) -> None: ...
    ClusterData: list[ClusterData2]
    """
            The feature attribute information associated with the cluster and a reference to
            the cluster
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The  Service  Data"""

class FeatureAttributeData2:
    """
    
The FeatureAttributeData2 structure is used return the feature attribute
information
belonging to the routine
    """
    def __init__(self, ) -> None: ...
    AttributeCode: str
    """Attribute Code"""
    Abbreviation: str
    """Attribute Code Abbreviation"""
    CodeDirection: int
    """Attribute Code Direction"""
    Significance: int
    """Attribute Significance"""
    MeasurementApproach: str
    """Attribute measurement approach"""
    Need: str
    """Attribute Need"""
    Nominal: float
    """Attribute Nominal"""
    SpecSetCodes: list[SpecSetCode2]
    """vector of spec sets defined on the Attribute"""

class FeatureAttributeInfo2:
    """
    
The FeatureAttributeInfo2 structure is used return the feature attribute
information
belonging to the cluster
    """
    def __init__(self, ) -> None: ...
    ParentFeatureId: str
    """ID of the feature"""
    ParentFeatureName: str
    """Name of the feature"""
    AttributeCode: str
    """An attribute code/name associated with the parentFeatureId"""

class FeatureNominals2:
    """
    The FeatureNominals2 structure is used return the nominal values of the feature
    """
    def __init__(self, ) -> None: ...
    X: float
    """X Nominal"""
    Y: float
    """Y Nominal"""
    Z: float
    """Z Nominal"""
    I: float
    """I Nominal"""
    J: float
    """J Nominal"""
    K: float
    """K Nominal"""
    I2: float
    """I2 Nominal"""
    J2: float
    """J2 Nominal"""
    K2: float
    """K2 Nominal"""

class FeatureData2:
    """
    
The FeatureData2 structure is used return the feature information belonging to
the
routine. Each feature has set of feature attributes These set of feature
attributes
are captured in a vector.
    """
    def __init__(self, ) -> None: ...
    FeatureId: str
    """Id of the Feature"""
    FeatureLabel: str
    """Feature Name"""
    AltLabel: str
    """Alternate name of the Feature"""
    Description: str
    """Feature Description"""
    Need: str
    """Feature Need"""
    ActiveStatus: bool
    """Active Status of the feature"""
    LoadingSplitId: str
    """Loading Split Id of the feature"""
    NominalValues: FeatureNominals2
    """Nominal values given in a structure"""
    AttributeData: list[FeatureAttributeData2]
    """Vector of attributes defined for this feature"""

class RoutineData2:
    """
    
The RoutineData2 structure is used return the engineering data belonging to the
routine.
Each routine has set of features These set of features are captured in a vector.
    """
    def __init__(self, ) -> None: ...
    Routine: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The Routine object to which the features belong"""
    FeatureData: list[FeatureData2]
    """A vector of FeatureData2 structures"""

class RoutineIdVer2:
    """
    
The RoutineIdVer2 structure is used give the information (i.e. item id and
revision)
of the routines of interest
    """
    def __init__(self, ) -> None: ...
    RoutineId: str
    """Item id of the routine"""
    RoutineRev: str
    """Routine revision of the routine"""

class RoutineQryResponse2:
    """
    
The RoutineQryResponse2 structure is used return the engineering data of a
routine.
This structure has a RoutineData2 structure and the service data structure in
it.
    """
    def __init__(self, ) -> None: ...
    RoutineData: list[RoutineData2]
    """A vector of RoutineData2 structures with engineering data of a routine"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data object"""

class SpecSetCode2:
    """
    The SpecSetCode2 structure is used return the spec set code values of an
attribute
    """
    def __init__(self, ) -> None: ...
    SpecSetCodeName: str
    """Item id of the routine"""
    Target: float
    """target value of the spec set code"""
    Usl: float
    """usl value of the spec set code"""
    Lsl: float
    """lsl value of the spec set code"""

class EngineeringDataQuery:
    """
    Interface EngineeringDataQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetEngineeringDataFromRoutine2(self, RoutineIdVer: list[RoutineIdVer2]) -> RoutineQryResponse2:
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
    def GetFeatureAttributeDataOfCluster2(self, ClusterIdentifier: list[ClusterIdentifier2]) -> ClusterQryResponse2:
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

