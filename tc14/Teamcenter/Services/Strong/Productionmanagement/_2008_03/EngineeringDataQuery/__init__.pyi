import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FeatureAttributeData3:
    """
    
The FeatureAttributeData3 structure is used return the feature attribute
information
belonging to the routine
    """
    def __init__(self, ) -> None: ...
    AttributeCode: str
    """ID, code or name of a feature attribute"""
    Abbreviation: str
    """Abbreviation of a attributeCode"""
    CodeDirection: int
    """Direction of an attributeCode"""
    Significance: int
    """Significance of the feature attribute. '0' - Insignificant; '1' - significant"""
    MeasurementApproach: str
    """
            Specifies how the Coordinate Measuring Machine (CMM) probe measures a point for -
            "Surface": takes into account the actual vector of the measured geometry; "Vector":
            Takes the nominal             vector
            
"""
    Need: str
    """
            Attribute need with values such as 'Optional', 'Planned' or 'Required'.This
            information is used by the Extract Transact and Loader (ETL) client application to
            determine if a feature attribute is required or optional for a routine revision
            """
    Nominal: float
    """The ideal nominal value of each attribute. Typically, '0' for deviations"""
    Formula: str
    """Derived feature expression and it is not used for a non-derived feature"""
    SpecSetCodes: list[SpecSetCode3]
    """List of specification sets containing the tolerance limit information for the attribute"""

class FeatureNominals3:
    """
    The FeatureNominals3 structure is used return the nominal values of the feature
    """
    def __init__(self, ) -> None: ...
    X: float
    """X location of the feature"""
    Y: float
    """Y location of the feature"""
    Z: float
    """Z location of the feature"""
    I: float
    """component i of the first feature vector"""
    J: float
    """component j of the first feature vector"""
    K: float
    """component k of the first feature vector"""
    I2: float
    """component i of the second feature vector"""
    J2: float
    """component j of the second feature vector"""
    K2: float
    """component k of the second feature vector"""

class FeatureData3:
    """
    
The FeatureData3 structure is used return the feature information belonging to
the
routine. Each feature has set of feature attributes These set of feature
attributes
are captured in a vector.
    """
    def __init__(self, ) -> None: ...
    FeatureId: str
    """ID of the feature"""
    FeatureLabel: str
    """Feature name"""
    FeatureType: str
    """
            Specifies the type of feature such as 'Point', 'Hole', 'Pin',
            'Slot', 'Tab'
            
"""
    AltLabel: str
    """
            An alternative name for the feature for systems that may have length requirements
            so you can enter another name by which to reference the feature
            
"""
    Description: str
    """Feature description"""
    Need: str
    """
            Feature Need with values such as 'Required', 'Planned' and 'Optional'.
            This information is used by the Extraction Transaction and Load (ETL) client to determine
            if a feature is required or optional for a routine revision.
            """
    ActiveStatus: bool
    """
            Status that shows whether or not Dimensional Planning and Validation (DPV) device
            client and DPV Reporting & Analysis should process data for this feature ('Y'
            - process the data; 'N' - do not process the data)
            
"""
    LoadingSplitId: str
    """
            Loading Split ID of the feature. If a routine is measured with two or more devices,
            the Loading Split ID identifies the portion of a routine (or several features) measured
            by a device. If the routine is measured by only one device, then the Loading Split
            ID is blank
            
"""
    NominalValues: FeatureNominals3
    """
            Nominal values such as x,y,z,i,j,k. x, y
            and z are the anchor point coordinates used
            in interactive reporting i,j and k are the vector normal direction
            
"""
    AttributeData: list[FeatureAttributeData3]
    """A list of attributes defined for the feature"""

class RoutineData3:
    """
    
The RoutineData3 structure is used return the engineering data belonging to the
routine.
Each routine has set of features These set of features are captured in a vector.
    """
    def __init__(self, ) -> None: ...
    Routine: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            The routine revision to which the featureData
            belongs
            """
    FeatureData: list[FeatureData3]
    """A list of feature information, such as active status, name, description, and ID"""

class RoutineIdVer3:
    """
    
The RoutineIdVer3 structure is used give the information (i.e. item id and
revision)
of the routines of interest
    """
    def __init__(self, ) -> None: ...
    RoutineId: str
    """Item id of the routine"""
    RoutineRev: str
    """Routine revision of the routine"""

class RoutineQryResponse3:
    """
    
The RoutineQryResponse3 structure is used return the engineering data of a
routine.
This structure has a RoutineData3 structure and the service data structure in
it.
    """
    def __init__(self, ) -> None: ...
    RoutineData: list[RoutineData3]
    """A list of structures containing engineering data of routine revisions"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class SpecSetCode3:
    """
    The SpecSetCode3 structure is used return the spec set code values of an
attribute
    """
    def __init__(self, ) -> None: ...
    SpecSetCodeName: str
    """
            Name or identifier for the specification limits. A character string to define the
            type of specification
            """
    Target: float
    """Target value of the spec set code"""
    Usl: float
    """Upper specification limit value of the spec set code"""
    Lsl: float
    """Lower specification limit value of the spec set code"""

class EngineeringDataQuery:
    """
    Interface EngineeringDataQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetEngineeringDataFromRoutine3(self, RoutineIdVer: list[RoutineIdVer3]) -> RoutineQryResponse3:
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

