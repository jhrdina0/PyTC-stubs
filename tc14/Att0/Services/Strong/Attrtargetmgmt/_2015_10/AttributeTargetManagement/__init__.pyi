import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DeleteMeasurableAttributeInput:
    """
    
DeleteMeasurableAttributeInput structure represents list of measurable attributes
            to be deleted from parent object.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """Identifier defined by client to track the related object."""
    ParentObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """The parent object for measurable attributes."""
    MeasurableAttributes: list[Teamcenter.Soa.Client.Model.Strong.Att0MeasurableAttribute]
    """
            A list of Att0MeasurableAttribute object which will be deleted from parent
            object.
            """

class DeleteMeasurableAttributesResponse:
    """
    
            Holds the response of deleteMeasuableAttributes. This response structure contains
            un-deleted objects and service data with partial errors.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData with partial errors for DeletesMeasurableAttributeInput identified
            by its clientID.
            """
    FailedToDeleteAttrTagMap: System.Collections.Hashtable
    """Represents list of un-deleted objects, identified by its clientID."""

class AttributeTargetManagement:
    """
    Interface AttributeTargetManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteMeasurableAttributes(self, Inputs: list[DeleteMeasurableAttributeInput]) -> DeleteMeasurableAttributesResponse:
        """    
             This operation deletes measurable attribute (Att0MeasurableAttribute) objects
             from given parent object.
             

If the given measurable attribute(Att0MeasurableAttribute)
             is a source attribute,  it is is deleted directly.
             
If the given measurable attribute(Att0MeasurableAttribute)
             is an overridden attribute, the overridden attribute itself is deleted as well as
             its related source attribute.
             
If the given measurable attribute(Att0MeasurableAttribute)
             is a source attribute and it is assigned as Input/Output attribute to an Analysis
             Request(Crt0VldnContractRevision), then the delete actions is discarded  and
             a warning message is returned.
             



Use Cases:


A system architect creates a product structure of logical blocks
             (Fnd0LogicalBlock), and defines for each block its measurable attributes (Att0MeasurableAttribute).
             A system designer may override measurable attribute in context of product. As the
             design of the product architecture evolves or need to re-design, the system designer
             may need to delete the already created measurable attributes from product architecture
             and will re-create measurable attribute.
             
A system architect may revise the logical block (Fnd0LogicalBlock),
             it copies measurable attributes from previous logical block revision (Fnd0LogicalBlockRevision)
             to new revision block. A system designer may want to delete attributes from previous
             logical block revision, and re-create attributes (Att0MeasurableAttribute)
             in the new logical block revision.
             



Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param Inputs: 
                         The list of measurable attributes and their parent objects.
             
        :return: 
        """
        ...

