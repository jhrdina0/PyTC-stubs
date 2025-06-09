import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateInput:
    """
    
CreateOrUpdateInput structure represents
            all the information needed to create the target element and
measurable attribute.
    """
    def __init__(self, ) -> None: ...
    BoType: str
    """
            This is the business object type  of the Target Eelement or Measurable Attribute
            being created. For a Target Element, the supported business object types are: Prg1VolumeTargetElement
            and Prg1ReuseTargetElement. For a Measurable Attribute, the supported business
            object types are: Att0MeasurableAttributeBool, Att0MeasurableAttributeDbl,
            Att0MeasurableAttributeInt and Att0MeasurableAttributeStr.
            """
    PropertyValueMap: System.Collections.Hashtable
    """
            All the information needed to create the Target Element or a Measurable Attribute
            object.  For creating a Target Element, this map provides the key-value pair  for
            object_name property. For a Measurable Attribute, it provides the key-value pair
            for the object_name, att0AttrDefRev, att0Min, att0Max, att0Goal and att0Overridable
            properties.
            """

class TargetElementCreateInput:
    """
    
TargetElementCreateInput structure represents
            all the information needed to create target element and associated
measurable attributes.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Unique ID is used by client to identify return data elements and partial errors associated
            with this input structure.
            """
    ContextObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            This is an optional input parameter and is the Plan Object in whose context the target
            element is getting authored. The Plan Object can be a Prg0ProgramPlan, Prg0ProjectPlan
            or Prg0SubProjectPlan. The context object will be a Prg0AbsPlan object
            in Program Planning. Otherwise set to NULL.
            """
    SelectedObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The object object  selected by the user to create and associate the target element.
            It can be a Prg0AbsPlan, Cfg0ProductModel or Ptn0Partition.
            """
    TargetDefinitionRevision: Teamcenter.Soa.Client.Model.Strong.Att0TargetRevision
    """
            The released target definition object selected by the user while creating the target
            element.
            """
    ApplicationModel: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """The application model for the target element."""
    ParentTargetElement: Teamcenter.Soa.Client.Model.Strong.Tgm0AbsTargetElement
    """
            The parent target element object for the target element being created. Set to NULL
            if there is no parent object.
            """
    CreateOrUpdateInputs: list[CreateOrUpdateInput]
    """
            A list containing details required to create Target Element and Measureable Attribute
            objects.
            """

class TargetManagement:
    """
    Interface TargetManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateTargetElements(self, CreateInputs: list[TargetElementCreateInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates a Tgm0AbsTargetElement object based on the input Target
             Definition( Att0TargetRevision ) object. The Target Element is created in
             the context of the input context object and linked to the input selected Object (
             which can be a Prg0AbsPlan, Cfg0ProductModel or Ptn0Partition
             ). A new Measureable Attribute is created and linked to the newly created Target
             Element. Please refer to documentation for more details on Target Element and Measurable
             Attribute objects.
             

Use Cases:

Use case 1: User wants to create a Volume Target Element  based on an approved
             Target Definition of a Volume Target. The Volume Target Definition defines the required
             target behavior (Target Type, whether the goal value is distributed ) and the Measureable
             Attribute for Volume Target. To create the target element, user passes a Prg0AbsPlan
             object as the context object,; a Prg0AbsPlan , Cfg0ProductModel ,
             or Ptn0Partition object as the source object on which target element will
             be created,; an Att0TargetRevision  object as the target definition object
             and a name for the target element being created as inputs . Using these inputs, the
             system would create a target element, a measurable attribute using the target definition
             and associates them. It also associates the created target element to the input source
             object.
             

Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param CreateInputs: 
                         A list of <font face="courier" height="10">TargetElementCreateInput</font> from which
                         <b>Tgm0AbsTargetElement</b> objects are to be created
             
        :return: .
        """
        ...

