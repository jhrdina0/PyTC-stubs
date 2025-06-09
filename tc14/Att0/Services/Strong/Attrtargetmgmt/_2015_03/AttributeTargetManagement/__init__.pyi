import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DefinitionCriteria:
    """
    Structure represents the criteria to get latest ItemRevision objects.
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier defined by client to track the related object."""
    ItemOrRevType: str
    """Required. Item or item revision type name which must exist in database."""
    ObjectName: str
    """
            Optional.The item revision name which is used to perform the search. Wild card "*"
            is supported.
            """
    EnabledStatus: list[str]
    """
            Optional. A list of allowed release status names. During the search system checks
            the latest ItemRevision release status name, if the status name is contained
            in enabledStatus, then the ItemRevision object will be returned.
            

If enabledStatus is empty , the latest ItemRevision will be
            returned
            
If enabledStatus contains multiple values, any release status on
            latest ItemRevision that is matched will be returned
            
If the latest ItemRevision has multiple release statuses, only check
            against the newest release status.
            

"""
    DisabledStatus: list[str]
    """
            A list of disallowed release status names. During the search system checks the latest
            ItemRevision's release status name, if the status name is contained in disabledStatus,
            the ItemRevision object will be ignored.
            

If disabledStatus is empty, the latest ItemRevision will be
            returned
            
If disabledStatus contains multiple values, any release status on
            latest ItemRevision that is matched will be ignored
            
If the latest ItemRevision has multiple release statuses,
            only check against the newest release status
            

"""

class DefinitionsResponse:
    """
    
            Holds the response for getLatestDefinitions. This output structure contains
            service data with partial errors and a StrDefinitionMap
            which contains latest ItemRevision objects based on give criteria for each
            entry in the DefinitionCriteria input list.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Service Data with partial errors for DefinitionCriteria identified by
            its clientId.
            """
    OutputMap: System.Collections.Hashtable
    """Map of input client IDs to the list of ItemRevision objects."""

class SyncMeasurableAttributeInput:
    """
    
SyncMeasurableAttributeInput structure represents the criteria to synchronize
            measurable attribute objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier defined by client to track the related object."""
    ParentObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The parent object holds list of measurable attributes which need to be synchonized.
            

The parent object type must be defined in "PLE_InputOutputAttrParentObjectTypes"
            preference.
            

"""
    AttrCandidates: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute]
    """
            A list of Att0MeasurableAttribute object which needs to be synzhonized or
            published.
            

If this parameter is provided, system will compare candidates with
            their source Att0MeasurableAttribute object and check if they are are out-of-date;
            if the candidate is out-of-date system only synchonize/publish these candidates.
            

"""

class SyncMeasurableAttributePref:
    """
    
SyncMeasurableAttributePref structure represents the synchronization direction(synchonize
            from source or publish to source), and input relations as well as output relations
            which are used to find out all input or output measurable attributes.
            
    """
    def __init__(self, ) -> None: ...
    Direction: str
    """The SyncDirection which identify the synchornization direction."""
    InputRelations: list[str]
    """
            A list of relation names from where system traverse a list of  input Att0MeasurableAttribute
            objects for synchronize.
            

If SyncDirection is SyncFromSource, this parameter
            is used along with parentObj to find a list of Att0MeasurableAttribute
            which will be updated with latest values from source Att0MeasurableAttribute
            as well as latest Att0MeasurableValue related to each Att0MeasurableAttribute.
            
If SyncDirection is PublishToSource, this parameter
            is used along with parentObj to find a list of input Att0MeasurableAttribute
            objects. If input  Att0MeasurableAttribute objects are out of date, system
            stops publication.
            

"""
    OutputRelations: list[str]
    """
            A list of relation names from where system traverse a list of  outputAtt0MeasurableAttribute
            objects for synchronization.
            

If SyncDirection is SyncFromSource, this parameter
            is used along with parentObj to find a list of output Att0MeasurableAttribute.
            Then system removes Att0Measurement object for each output Att0MeasurableAttribute
            object.
            
If SyncDirection is PublishToSource, this parameter
            is used along with parentObj to find a list of output Att0MeasurableAttribute
            objects. System will insert the latest Att0MeasurableValue to source Att0MeasurableAttribute
            for each output Att0MeasurableAttribute object .
            

"""

class SyncMeasurableAttributeResponse:
    """
    
SyncMeasurableAttributeResponse holds the response of synchronize Measuable
            Attributes. This output structure contains service data with partial errors and an
            outputMap which contains list of Att0MeasurableAttribute objects which
            have been synchronized.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data with partial errors identified by its clientId."""
    OutputMap: System.Collections.Hashtable
    """Map input client ID to list of Att0MeasurableAttribute objects"""

class AttributeTargetManagement:
    """
    Interface AttributeTargetManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetLatestDefinitions(self, Inputs: list[DefinitionCriteria]) -> DefinitionsResponse:
        """    
             This operation gets the list of ItemRevision objects based on given criteria.
             The DefinitionCriteria holds criteria such as item revision name, item or
             item revision type name, enabled release status as well as disabled release status;
             if and only if the latest ItemRevision or sub type objects will be returned
             when it matches these criteria.
             

Use Cases:

             Creates an Attribute Definition Revision into Teamcenter like below and following
             story:
             
             {ItemID=000001, Name=AttributeDef_1, Revision=B, Release Status="Released"}
             
             {ItemID=000001, Name=AttributeDef_1, Revision=C, Release Status="Obsolete"}
             
             {ItemID=000001, Name=AttributeDef_1, Revision=D, Release Status=""}
             

             When DefinitionCriteria is set as objectName=AttributeDef_1, itemOrRevType=Att0AttributeDefRevision
             enabledStatus=Released, disabledStatus=Obsolete
             

             At first case, revision B will be returned since it is released and status matches
             "Released"
             
             At second case, none revision is returned since latest revision C is "Obsolete"
             
             At third case, none revision is returned since latest revision D is in progress,
             while revision C is obsoleted
             


Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param Inputs: 
                         The criteria for filtering the list of latest <b>ItemRevision</b> objects.
             
        :return: 
        """
        ...
    def SynchronizeMeasuableAttributes(self, Inputs: list[SyncMeasurableAttributeInput], Pref: SyncMeasurableAttributePref) -> SyncMeasurableAttributeResponse:
        """    
             This operation is used to synchronize Att0MeasurableAttribute objects between
             source Att0MeasurableAttribute instances and target Att0MeasurableAttribute
             instances.  This synchronization operation has two process flows: synchronize from
             source Att0MeasurableAttribute instances to input Att0MeasurableAttribute
             instances; and publish from output Att0MeasurableAttribute instances to source
             Att0MeasurableAttribute instances.
             

When synchronize from source to input Att0MeasurableAttribute,
             an update operation is done against input Att0MeasurableAttribute with latest
             property values from source Att0MeasurableAttribute. Meanwhile copies the latest
             Att0MeasurableValue of source Att0MeasurableAttribute and inserts it into
             the input Att0MeasurableAttribute.
             
When publish from output to source Att0MeasurableAttribute,
             the latest Att0MeasurableValue is retrieved from output Att0MeasurableAttribute
             and inserts it into the latest Att0MeasurableValue list on the source Att0MeasurableAttribute.
             The source Att0MeasurableAttribute properties will not be updated.
             
If there is an issue during publication, the process stops and all
             modified objects are be restored.
             



Use Cases:

             1.    A system architect creates a product structure of logical
             blocks (Fnd0LogicalBlock), and defines for each block its measurable attributes
             (Att0MeasurableAttribute). As the design of the product architecture evolves,
             the system architect requests a partial or complete validation of the system. As
             part of the request system architect defines the logical blocks to be validated,
             their attributes that will inputs for the validation and the ones that need to be
             measured. As the system architect sets a logical block attribute (Att0MeasurableAttribute)
             as an input of the validation, the system builds a copy of the attribute for the
             validation context. The goal is to isolate the validation context from any updates
             that can be done on the product context.
             
             However when processing the validation request, the validation engineer should know
             if the input attributes are up to date with the product logical blocks attributes.
             If they are not the validation engineer can run synchronize input attributes command.
             
             2.    A system architect creates a product structure of logical
             blocks (Fnd0LogicalBlock), and defines for each block its measurable attributes
             (Att0MeasurableAttribute). As the design of the product architecture evolves,
             the system architect requests a partial or complete validation of the system. As
             part of the request system architect defines the logical blocks to be validated,
             their attributes that will inputs for the validation and the ones that need to be
             measured. As the system architect sets a logical block attribute (Att0MeasurableAttribute)
             as an input of the validation, the system builds a copy of the attribute for the
             validation context. The goal is to isolate the validation context from any updates
             that can be done on the product context.
             
             However when processing the validation request, the validation engineer should know
             if the output attributes are measured which comes out a new measurement value (Att0MeasureValue).
             If new measurement value is generated, the validation engineer can run publish command
             to publish output attribute measurement value to logical block attribute.
             

Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param Inputs: 
                         The synchronization measurable attribute inputs.
             
        :param Pref: 
                         The synchronization measurable attribute preference.
             
        :return: 
        """
        ...

