import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AdjacentObjectInfo:
    """
    
            The structure representing an adjacent object (either the predecessor or the successor)
            along with the constraint object
            
    """
    def __init__(self, ) -> None: ...
    ConstraintObject: Teamcenter.Soa.Client.Model.ModelObject
    """The constraint object (Mfg0BvrPrecedenceConstraint)"""
    AdjacentObject: Teamcenter.Soa.Client.Model.ModelObject
    """The preceding or succeeding object (Mfg0BvrProcess / Mfg0BvrOperation)"""

class GetPrecedenceConstraintPathsInputs:
    """
    Input structure for the getPrecedenceConstraintPaths operation.
    """
    def __init__(self, ) -> None: ...
    StartNode: Teamcenter.Soa.Client.Model.ModelObject
    """
            The process/operation line at the start of the precedence chain. This member can
            hold BOs of type Mfg0BvrProcess and Mfg0BvrOperation.
            """
    EndNode: Teamcenter.Soa.Client.Model.ModelObject
    """
            The operation/process line at the end of the precedence chain This member can hold
            BOs of type Mfg0BvrProcess and Mfg0BvrOperation.
            """

class GetPrecedenceConstraintPathsResponse:
    """
    Response structure for the getPrecedenceConstraintPaths operation.
    """
    def __init__(self, ) -> None: ...
    Results: list[GetPrecedenceConstraintPathsResult]
    """
            A list of result structures that contain the paths for each start and end node pair
            specfied in the input structures.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData object for the matching GetPrecedenceConstraintPathsInputs structure."""

class GetPrecedenceConstraintPathsResult:
    """
    The result structure for the getPrecedenceConstraintPaths operation.
    """
    def __init__(self, ) -> None: ...
    Paths: list[PrecedenceConstraintPath]
    """The list of paths that connect the respective start and end node."""

class GetPrecedenceConstraintsIn:
    """
    The input structure for the getPrecedenceConstraints service operation
    """
    def __init__(self, ) -> None: ...
    PredecessorLevel: int
    """
            The integer indicating the number of predecessor levels to be processed in the precedence
            chain
            """
    SuccessorLevel: int
    """
            The integer indicating the number of successor levels to be processed in the precedence
            chain
            """
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """The input object (Mfg0BvrProcess / Mfg0BvrOperation)"""

class GetPrecedenceConstraintsResponse:
    """
    
            The response structure of the getPrecedenceConstraints service operation. Contains
            the predecessor and successor maps.
            
    """
    def __init__(self, ) -> None: ...
    PredecessorMap: System.Collections.Hashtable
    """The map of objects to their predecessors"""
    SuccessorMap: System.Collections.Hashtable
    """The map of objects to their successors"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData structure"""

class PrecedenceConstraintPath:
    """
    Defines a specific path for the GetPrecedenceConstraintPaths API
    """
    def __init__(self, ) -> None: ...
    Components: list[PrecedenceConstraintPathComponent]
    """
            A list of structures that hold the nodes and constraints that make up the path to
            the end node.
            """
    EndNode: Teamcenter.Soa.Client.Model.ModelObject
    """The end node itself. The Business Object  is of type Mfg0BvrProcess or Mfg0BvrOperation."""

class PrecedenceConstraintPathComponent:
    """
    A component of a constraint path for structure PrecedenceConstraintPath
    """
    def __init__(self, ) -> None: ...
    Predecessor: Teamcenter.Soa.Client.Model.ModelObject
    """A node which is part of the path (type Mfg0BvrProcess or Mfg0BvrOperation)."""
    Constraint: Teamcenter.Soa.Client.Model.ModelObject
    """
            The constraint that connects the node of this component structure to the next, or,
            in case this is the last component in the path, to the end node. Note that the predecessor
            of the constraint is different from the predecessor member in case the constraint
            is inherited.The same applies to the successor of the constraint: it does not necessarily
            have to be the successor in the path. This member is of type Mfg0BvrPrecedenceConstraint.
            """
    ConstraintIsInherited: bool
    """
            Indicates whether the constraint is directly connected to the predecessor and successor
            nodes in the path or whether it has been inherited from a parent node:
            """

class ValidateConstraintConsistencyError:
    """
    Describes a problem detected by the validateConstraintConsistency operation.
    """
    def __init__(self, ) -> None: ...
    ConstraintType: Teamcenter.Soa.Client.Model.ModelObject
    """
            The type of the constraint that is violated. This is the ImanType of the runtime
            constraint object, for example Mfg0BvrPrecedenceConstraint for precedence constraints.
            """
    Message: str
    """A localized message explaining the detected inconsistency."""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of operations/processes that participate in the constraints that are inconsistent.
            The list contains business objects of type Mfg0BvrOperation and Mfg0BvrProcess.
            """
    Constraints: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The constraint objects which are inconsistent.These objects are of type Mfg0BvrConstraint."""

class ValidateConstraintConsistencyInputs:
    """
    Input structure for the validateConstraintConsistency operation.
    """
    def __init__(self, ) -> None: ...
    ConstraintTypes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The constraint types to check. Each entry in this vector is of type ImanType; it
            corresponds to the type of the runtime object for the constraint (e.g. Mfg0BvrPrecedenceConstraint
            for precedence constraints or Mfg0BvrPrecedenceConstraint for group constraints;
            customer defined derived types are accepted as well). If the vector is empty, all
            constraints are checked.
            """
    RootNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of BOMLines from the BOP window that define the root nodes of the sub structures
            to check.  The objects must be of type Mfg0BvrProcess or Mfg0BvrOperation. All lines
            must be associated with the same window.
            """

class ValidateConstraintConsistencyResponse:
    """
    Response structure of the validateConstraintConsistencyResponse operation.
    """
    def __init__(self, ) -> None: ...
    Results: list[ValidateConstraintConsistencyResult]
    """The list of result structures that holds one entry for each input structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData object for this request."""

class ValidateConstraintConsistencyResult:
    """
    Result structure for the validateConstraintConsistency operation.
    """
    def __init__(self, ) -> None: ...
    Errors: list[ValidateConstraintConsistencyError]
    """The  list of validation errors, if any."""

class ValidateProcessAreaAssignmentsError:
    """
    
            A structure that contains information about an problem detected in the ValidateProcessAreaAssignments
            operation. In the case of a precedence constraint violation, the objectsOfContextOfConstraint
            vector will contain the predecessor and the sucessor operation or process whose order
            is conflicting with the order of the process areas they are assigned to, if a Product
            BOP is given. The objectsOfContextToValidate member will contain their respective
            counterparts in the Plant BOP, and processAreas will contain the associated process
            areas. In case of a precedence constraint violations the constraints vector will
            be empty, since the constraints themselves are meaningless without the intermittent
            operations/processes. In order to obtain the paths of processes/operations and constraints
            that define the precedence of the start and end node, the GetPrecedenceConstraintPathsAPI
            may be used. Currently one possible type of error may arise when precedence constraints
            are violated. The format of the error message is similar to the following: <Node
            A> is assigned to <Process Area X> while its successor <Node B> is assigned
            to <Process Area Y>  which is a predecessor of  <Process Area X>.
            
    """
    def __init__(self, ) -> None: ...
    ConstraintType: Teamcenter.Soa.Client.Model.ModelObject
    """
            The type of the constraint that is violated. Corresponds to the ImanType of the constraint
            object. See also the constraintTypes member of struct ValidateProcessAreaAssignmentsInputs.
            """
    Message: str
    """A localized message explaining the validation error."""
    ObjectsOfContextOfConstraint: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of operations and/or processes that violate the constraints. These objects
            belong to the contexts passed via the contextOfConstraints parameter i.e. the Product
            BOPs. The vector will be empty if the contextOfConstraints vector is empty. The list
            contains business objects of type Mfg0BvrOperation and Mfg0BvrProcess.
            """
    ObjectsOfContextToValidate: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of assigned nodes from the contextToValidate parameter. In case only a single
            Product BOP exists, the vector will hold the same number of objects as the objectsOfContextOfConstraint
            member. The business objects are of type Mfg0BvrOperation and Mfg0BvrProcess.
            """
    ProcessAreas: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of process areas associated with the Product BOP objects. The objects are
            of type Mfg0BvrProcessArea and belong to the context passed in contextToValidate.
            """
    Constraints: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The constraint objects which are violated. These objects are of type Mfg0BvrConstraint.
            Note that depending on the type of violation the constraints list may be empty. This
            is the case for example for precedence constraints.
            """

class ValidateProcessAreaAssignmentsInputs:
    """
    Input structure for the validateProcessAreaAssignments operation.
    """
    def __init__(self, ) -> None: ...
    ConstraintTypes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The constraint types to check. Each entry in this vector is of type ImanType; it
            corresponds to the type of the runtime object for the constraint (e.g. Mfg0BvrPrecedenceConstraint
            for precedence constraints or Mfg0BvrGroupConstraint for group constraints). The
            types vector may also contain customized types derived from the base constraint types.
            If the vector is empty, all constraints are checked.
            """
    ContextToValidate: Teamcenter.Soa.Client.Model.ModelObject
    """
            The context of the process area structure. This is the top line of the window that
            holds the Plant BOP structure (the object is of type Mfg0BvrPlantBOP).
            """
    ContextOfConstraints: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of contexts that describes the processes and operations whose assignments
            are to be validated. If empty it is assumed that the context of the process area
            structure is to be used. Currently only one single is accepted that represents the
            topline of the Product BOP structure (this object must be of type Mfg0BvrProductBOP).
            """
    RootProcessAreas: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of BOMLines from the Plant BOP window that define the substructure whose
            allocations are examined If the list is empty, the whole Plant BOP loaded into the
            Plant BOP window will be checked. The Business Objects are of type Mfg0BvrProcessArea.
            """
    MaxErrors: int
    """
            The maximum number of errors to return. Can be set to 0 in order not to impose any
            limit. Otherwise the value must be greater than 0.
            """

class ValidateProcessAreaAssignmentsResponse:
    """
    Response structure for the validateProcessAreaAssignments operation.
    """
    def __init__(self, ) -> None: ...
    Results: list[ValidateProcessAreaAssignmentsResult]
    """The list of result structures that holds one entry for each input structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData object for this request."""

class ValidateProcessAreaAssignmentsResult:
    """
    Result structure for the validateProcessAreaAssignments operation.
    """
    def __init__(self, ) -> None: ...
    Errors: list[ValidateProcessAreaAssignmentsError]
    """The  list of validation errors, if any."""

class Constraints:
    """
    Interface Constraints
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPrecedenceConstraintPaths(self, InputData: list[GetPrecedenceConstraintPathsInputs]) -> GetPrecedenceConstraintPathsResponse:
        """    
             Returns all operations/processes in the precedence chain starting from the given
             start operation/process up to the end operation/process, i.e., all operations/processes
             succeeding the start operation/process and preceding the end operation/process.
             
        :param InputData: 
                         The input data contains the list of start and end operation or process lines.
             
        :return: A structure holding a vector of constraint paths for each input structure.
        """
        ...
    def GetPrecedenceConstraints(self, InputData: list[GetPrecedenceConstraintsIn]) -> GetPrecedenceConstraintsResponse:
        """    
             Fetches all precedence constraints defined on the given input objects - traverses
             'm' levels in the predecessor chain and 'n' levels in the successor chain.
             
        :param InputData: 
                         The list of input objects (Mfg0BvrProcess / Mfg0BvrOperation) whose precedence constraints
                         are to be fetched along with the number of levels to be traversed in the predecessor
                         and successor chains.
             
        :return: Returns a map of predecessors and successors for each object
        """
        ...
    def ValidateConstraintConsistency(self, InputData: list[ValidateConstraintConsistencyInputs]) -> ValidateConstraintConsistencyResponse:
        """    
             This SOA invokes the consistency check service. It checks whether the constraints
             defined in the product BOP or a sub structure thereof are consistent.
             
        :param InputData: 
                         A vector of ValidateConstraintConsistencyInputs structures that defines one or multiple
                         substructures to check.
             
        :return: A set of error descriptions for each input structure.
        """
        ...
    def ValidateProcessAreaAssignments(self, InputData: list[ValidateProcessAreaAssignmentsInputs]) -> ValidateProcessAreaAssignmentsResponse:
        """    
             This SOA invokes the constraint validation service. It checks whether the assignments
             of operations or processes of a Product BOP to process areas in a Plant BOP are consistent
             with the constraint definitions.
             
        :param InputData: 
                         A vector of ValidateProcessAreaAssignmentsInputs structures that define the the Plant
                         and Product BOPs and the set of nodes to validate in the Plant BOP.
             
        :return: A structure that contains a list of errors for each input structure.
        """
        ...

