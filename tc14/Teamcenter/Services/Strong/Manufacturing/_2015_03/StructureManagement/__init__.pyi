import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MoveAndResequenceParameter:
    """
    
The structure specifies the nodes to be moved, their target, whether dropped on
the
target, context based on which find number to be decided and whether to clone or
move the nodes to the new target.
    """
    def __init__(self, ) -> None: ...
    SourceNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of BOMLine objects to be re-sequenced within parent or moved to another
            target BOMLine.
            """
    TargetNode: Teamcenter.Soa.Client.Model.ModelObject
    """The BOMLine to which the source BOMLine objects are to be moved."""
    Predecessor: Teamcenter.Soa.Client.Model.ModelObject
    """
            The BOMLine below which source BOMLine objects are dropped. The find
            number of dropped lines is altered to position them after the predecessor. The find
            number of siblings following the pasted BOMLine objects may also change. Ignored
            if the parameter isDroppedOnTarget is true which signifies that source BOMLine
            objects are directly dropped on the target BOMLine, as a result find numbers
            are generated for dropped BOMLine objects and the BOMLine objects are
            position as the last children in the BOM structure.
            """
    IsDroppedOnTarget: bool
    """
            Specifies whether source BOMLine objects are directly dropped on the target
            node. If true, the find numbers are generated for dropped BOMLine objects
            and the BOMLine objects are position as the last children in the BOM structure.
            If false, find numbers are generated so as to position them after the predecessor.
            However, in case predecessor is NULL then the find numbers are generated for dropped
            BOMLine objects and BOMLine objects are position as the first children
            in the BOM structure.
            """
    FindNumberContext: Teamcenter.Soa.Client.Model.ModelObject
    """
            Context based on which find numbers of dropped BOMLine objects are generated.
            Relevant only if the target BOMLine is process resource of type Mfg0BvrProcessResource.
            """
    IsPasteDuplicate: bool
    """
            Specifies whether the source BOMLine objects are to be cloned to the new target
            BOMLine instead of move. If true, source BOMLine objects are cloned
            to the target BOMLine objects. If false, the source BOMLine objects
            are moved to the target BOMLine.
            """

class MoveAndResequenceResponse:
    """
    response structure for the service method moveAndResequenceNodes.
    """
    def __init__(self, ) -> None: ...
    CreatedICRevs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """List of newly created Incremental Change (IC) revisions."""
    CreatedFutureICRevs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """List of newly created future IC revisions."""
    NewChildLines: System.Collections.Hashtable
    """
            The map (BOMLine, List of BOMLine) of target BOMline and the
            newly created or moved BOMLine objects under it.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data containing partial errors."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def MoveAndResequenceNodes(self, InputList: list[MoveAndResequenceParameter]) -> MoveAndResequenceResponse:
        """    
             This operation moves and/or re-sequences the nodes in the structure.
             

Use Cases:

             Use Case 1: Re-sequencin g nodes within parent in a structure.
             
             This operation can be used in M anufacturing Process Planning (MPP) application to
             resequence a node in a struct ure. For example, in a product structure an Item
             or  BOMLine can be reseqenced within the parent by dragging and dropping t
             he Item in between the siblings. Same could be done in proces s structure
             by dragging and dropping a process or operation BOMLine. As a result of drop,
             the find number of the node and its subsequent sibling are modified.
             
             Use Case 2: Re-parent and re-sequence of nodes.
             
             This operation can be used in MPP application to move the nodes from one parent to
             another and sequenced them among the siblings of new parent. For example, in a process
             structure a process or operation BOMLine objects can be dragged and dropped
             in between the child nodes of another process BOMLine. The dragged processes
             or operations are moved as children of the new process BOMLine and sequenced
             among the sibling as per dropped location. While drag and drop, UI presents an option
             whether to clone the nodes. If selected then the nodes are cloned instead of re-parent.
             
             Use Case 3: Moving the processes or operations to process resource in Plant Bill
             of Processes (BOP).
             
             This operation can be used to allocate the process or operation BOMLine of
             type Mfg0BvrProcess or Mfg0BvrOperation to a process resource of type
             Mfg0BvrProcessResource in a Plant BOP structure. The find number of dropped
             BOMLine objects could be calculated either in the context of the process station
             of type Mfg0BvrProcessStation to which process resource is a child object,
             or process resource is itself. If the context is process station of type Mfg0BvrProcessStation
             then the find numbers of the dropped BOMLine objects are calculated based
             on the existing processes or operations that are a child object of process station.
             If the context is process resource then the calculation is based on the processes
             or operations allocated to that process resource. In Teamcenter MPP application,
             the context is always a process station BOMLine.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param InputList: 
                         The list of moveAndResequenceParameter structure. Each structure specifies the nodes
                         to be moved, their target, whether dropped on the target, context based on which
                         find number to be decided and whether to clone or move the nodes to the new target.
             
        :return: 
        """
        ...

