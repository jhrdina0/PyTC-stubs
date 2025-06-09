import System
import Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConnectorTableInfo:
    """
    The structure containing ItemRevision and its connector details.
    """
    def __init__(self, ) -> None: ...
    ItemRev: Teamcenter.Soa.Client.Model.ModelObject
    """ItemRevision for which connector details are to be retrieved."""
    ConnectorProperties: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.GeneralInfo]

class GetConnectorResponse:
    """
    Response for getConnectorInfo operation.
    """
    def __init__(self, ) -> None: ...
    ConnectorInfo: list[ConnectorTableInfo]
    """
            List of structures containing connector information for given ItemRevision
            objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial errors as part of the serviceData."""

class GetPhysicalAttachmentsInput:
    """
    
Input structure containing context and scope information for which the
attachments
need to be retrieved.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A root Mfg0BvrWorkarea object in Bill of Equipment structure. The operation
            processes scope within context.
            """
    Scope: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """A Mfg0BvrWorkarea object under context for which attachment need to be queried"""

class GetPhysicalAttachmentsResponse:
    """
    Response for getPhysicalAttachmentsInScope operation.
    """
    def __init__(self, ) -> None: ...
    AttachmentsInfo: list[PhysicalAttachmentInfo]
    """
            List of structures containing information about the physical attachment relation
            Mfg0MEPhysicalAttachment or Mfg0MEMountToolToRobot between AbsOccurrence
            of BOMLine objects under the given scope Mfg0BvrWorkarea.
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial errors as part of the serviceData."""

class PhysicalAttachmentInfo:
    """
    
The structure containing source and target BOMLine and the
Mfg0MEPhysicalAttachment
relation information.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """A root Mfg0BvrWorkarea object in Bill of Equipment structure."""
    Scope: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """A Mfg0BvrWorkarea object under context"""
    Source: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A BOMLine node of the AbsOccurrence represeting primary  in MfgMEPhysicalAttachment
            or Mfg0MEMountToolToRobot relation.
            """
    Target: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A BOMLine node of the AbsOccurrence represeting secondary  in MfgMEPhysicalAttachment
            or Mfg0MEMountToolToRobot relation.
            """
    RelationName: str
    """
            Name of relation by which  AbsOccurence of source BOMLine and target
            BOMLine are related. Possible values are Mfg0MEPhysicalAttachment or
            its subtype Mfg0MEMountToolToRobot.
"""
    RelationInfo: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.GeneralInfo

class RemovePhysicalAttachmentRelInput:
    """
    Input structure containing context, scope, source, and target information.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A root Mfg0BvrWorkarea object in Bill of Equipement structure. The operation
            deletes relations of type Mfg0MEPhysicalAttachment or Mfg0MEMountToolToRobot
            created in this context.
            """
    Scope: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A Mfg0BvrWorkarea object under context.  The operation travereses the scope,
            finds the source and target BOMLine,gets  AbsOccurrence for source and target
            BOMLine and collects Mfg0MEPhysicalAttachment or Mfg0MEMountToolToRobot
            relation to be deleted.
            """
    Source: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A BOMLine node of the AbsOccurrence represeting primary  in MfgMEPhysicalAttachment
            or Mfg0MEMountToolToRobot relation.
            """
    Target: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A BOMLine node of the AbsOccurrence represeting secondary in MfgMEPhysicalAttachment
            or Mfg0MEMountToolToRobot relation.
            """

class SetConnectorInput:
    """
    Input structure containing ItemRevision and connectorInformation
    """
    def __init__(self, ) -> None: ...
    ItemRev: Teamcenter.Soa.Client.Model.ModelObject
    """ItemRevision for which connector details are to be updated."""
    ConnectorInformation: list[Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.GeneralInfo]

class SetPhysicalAttachmentsInput:
    """
    
Input structure containing context, scope, source, target, relation name, and
relation
properties information.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A root Mfg0BvrWorkarea object in Bill of Equipment structure. In context of
            this root, AbsOccurrence is created for source BOMLine and target BOMLine.
            """
    Scope: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """A Mfg0BvrWorkarea object under context."""
    Source: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A BOMLine node of the AbsOccurrence representing primary  in MfgMEPhysicalAttachment
            or Mfg0MEMountToolToRobot relation.
            """
    Target: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            A BOMLine node of the AbsOccurrence representing secondary in MfgMEPhysicalAttachment
            or Mfg0MEMountToolToRobot relation.
            """
    RelationName: str
    """
            Name of relation by which AbsOccurence of source BOMLine and target
            BOMLine are related. Possible values are  Mfg0MEPhysicalAttachment
            or Mfg0MEMountToolToRobot.
"""
    RelationInfo: Teamcenter.Services.Strong.Manufacturing._2012_02.DataManagement.GeneralInfo

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetConnectorInfo(self, ItemRevs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetConnectorResponse:
        """    
             Connector is Product and Manufacturing Information (PMI) object created by NX which
             is used to define the connection between two components used on shop floor. This
             operation retrieves the information of connectors represented as a Mfg0MEConnectorTableRow
             in Mfg0MEConnectorTable.
             
Mfg0MEConnectorTableRow has information about connector type, connector name,
             connector ID and transformation.
             
             The Mfg0MEConnectorTableForm holds Mfg0MEConnectorTable and is related
             to ItemRevision through the relation Mfg0MEConnectorTblFormRel.


Use Cases:

             Connector is Product and Manufacturing Information (PMI) object created by NX which
             is used to define the connection between two components used on shop floor. E.g.
             Mfg0Conveyor and Mfg0Conveyor or Mfg0Conveyor and Mfg0MERobot.
             Line Designer user wants to retrieve connector information for ItemRevision.


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param ItemRevs: 
                         List of <b>ItemRevision</b> for which connector information is required.
             
        :return: 251081: Connector information is not defined for the input object.
        """
        ...
    def GetPhysicalAttachmentsInScope(self, Input: list[GetPhysicalAttachmentsInput]) -> GetPhysicalAttachmentsResponse:
        """    
             This operation retrievs all physical attachments (Mfg0MEPhysicalAttachment
             or Mfg0MEMountToolToRobot) relations defined between two BOMLine
             objects that are children of the given scope Mfg0BvrWorkarea and context Mfg0BvrWorkarea
             acting as a root of the structure.
             
             This operation
             

Processes the input scope Mfg0BvrWorkarea under root context
             Mfg0BvrWorkarea in Bill of Equipment structure.
             
Traverses   the scope, finds the AbsOccurrence under the scope
             related with Mfg0MEPhysicalAttachment or Mfg0MEMountToolToRobot relation.
             From primary AbsOccurrence of relation Mfg0MEPhysicalAttachment or
             Mfg0MEMountToolToRobot it collects source BOMLine and from secondary
             AbsOccurrence it collects target BOMLine along with the relation properties
             on Mfg0MEPhysicalAttachment or Mfg0MEMountToolToRobot.
             



Use Cases:

             Line Designer user wants to retrieve mount and attachment information for the BOMLine
             connections with Mfg0MEPhysicalAttachment relation in a given scope of Mfg0BvrWorkarea
             and Mfg0BvrWorkarea acting as a root of the structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         Input structure containing scope and context information for which the attachments
                         need to be retrieved.
             
        :return: 253077: The input scope is invalid. Scope cannot be root line in the structure.
        """
        ...
    def RemovePhysicalAttachementRelation(self, Input: list[RemovePhysicalAttachmentRelInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes Mfg0MEPhysicalAttachment or Mfg0MEMountToolToRobot
             relation between the AbsOccurrence of given source BOMLine and target
             BOMLine objects for given scope Mfg0BvrWorkarea and context Mfg0BvrWorkarea
             acting as a root of the structure.
             

Use Cases:

             Line Designer user wants to disconnect two connected resource object (for e.g.
             Mfg0MEFactoryTool from the Mfg0MERobot ) which are connected with Mfg0MEPhysicalAttachment
             or Mfg0MEMountToolToRobot relation in a given scope Mfg0BvrWorkarea
             and context Mfg0BvrWorkarea acting as a root of the structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         Input structure containing information about the context <b>Mfg0BvrWorkarea</b>,
                         scope <b>Mfg0BvrWorkarea</b> and the source and target <b>BOMLine</b>.
             
        :return: relation between the given source and target object.
        """
        ...
    def SetConnectorInfo(self, Input: list[SetConnectorInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Connector is Product and Manufacturing Information (PMI) object created by NX which
             is used to define the connection between two components used on shop floor. This
             operation sets the connector information stored as Mfg0MEConnectorTableRow
             in Mfg0MEConnectorTable. The Mfg0MEConnectorTableForm is attached to
             the ItemRevision.
             
             If the Mfg0MEConnectorTableForm is not related to the ItemRevision
             the operation first creates Mfg0MEConnectorTableForm and attaches it to the
             given ItemRevision with a relation Mfg0MEConnectorTblFormRel.

             If given input connector id is not present in Mfg0MEConnectorTableRow, then
             a Mfg0MEConnectorTableRow is added in Mfg0MEConnectorTable with information
             connector type, connector name, connector ID and transformation.
             
             If given input connector id is present in Mfg0MEConnectorTableRow,the row
             is updated with latest information.
             
             All the Mfg0MEConnectorTableRow for which information is not given are removed
             from Mfg0MEConnectorTable.


Use Cases:

             Line Designer user wants to add, remove or update the connector information for
             ItemRevision


Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         Input structure containing information about the <b>ItemRevision</b> and the connectors
                         information. i.e. connector type, connector name, connector ID and transformation.
             
        :return: 251083:The value provided for input property  is not valid.
        """
        ...
    def SetPhysicalAttachementsInScope(self, Input: list[SetPhysicalAttachmentsInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates physical attachment Mfg0MEPhysicalAttachment or  Mfg0MEMountToolToRobot
             relation between the AbsOccurrence of given source BOMLine and target
             BOMLine objects for given scope Mfg0BvrWorkarea and context Mfg0BvrWorkarea
             acting as a root of the structure.
             

Use Cases:

             Line Designer user wants to set mount and attach information for BOMLine (e.g.
             Mfg0MEFactoryTool and Mfg0MERobot) using  Mfg0MEPhysicalAttachment
             or Mfg0MEMountToolToRobot relation in a given scope Mfg0BvrWorkarea
             and context Mfg0BvrWorkarea acting as a root of the structure.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         Input structure containing information about the scope <b>(Mfg0BvrWorkarea)</b>,
                         the source<b> (BOMLine) </b>and target <b>(BOMLine)</b> objects and <b>Mfg0MEPhysicalAttachment</b>
                         or <b>Mfg0MEMountToolToRobot</b> relation properties.
             
        :return: 
        """
        ...

