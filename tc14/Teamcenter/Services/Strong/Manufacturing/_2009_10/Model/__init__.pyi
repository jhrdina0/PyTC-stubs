import System
import Teamcenter.Soa.Client.Model
import typing

class CalculateCriticalPathResponse:
    """
    The response structure for the calculateCriticalPath operation.
    """
    def __init__(self, ) -> None: ...
    Results: list[CalculateCriticalPathResult]
    """A list of CalculateCriticalPathResult structures for each path returned."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data strucuture used to return sets of Teamcenter Data Model object
            from a service request. This also holds services exceptions.
            """

class CalculateCriticalPathResult:
    """
    A structure that represents a path returned by the computeCriticalPath operation
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The root object for which this path was computed"""
    Components: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of components that make up the path. This includes the connecting flows."""
    Duration: float
    """The total duration of the path."""

class FlowInput:
    """
    FlowInput
    """
    def __init__(self, ) -> None: ...
    Successor: Teamcenter.Soa.Client.Model.ModelObject
    """The successor object of the flow object"""
    Predecessor: Teamcenter.Soa.Client.Model.ModelObject
    """The predecessor object of the flow."""
    Delay: float
    """The delay time for the successor."""

class FlowResponse:
    """
    FlowResponse
    """
    def __init__(self, ) -> None: ...
    FlowsResult: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vector of the new succesfully created flow objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class GetResolvedNodesFromLAResponse:
    """
    Response for getResolvedNodesFromLA SOA
    """
    def __init__(self, ) -> None: ...
    OutResolvedNodes: list[ResolvedNodesOutput]
    """All the resolved nodes of all objects"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data object"""

class LogicalAssignmentAttribute:
    """
    Attribute representation
    """
    def __init__(self, ) -> None: ...
    Name: str
    """Attribute name"""
    Value: str
    """Attribute value"""

class LogicalAssignmentData:
    """
    Parameters for editing Logical Assignment object
    """
    def __init__(self, ) -> None: ...
    LaObj: Teamcenter.Soa.Client.Model.ModelObject
    """Logical Assignment object to edit"""
    LaAttributes: list[LogicalAssignmentAttribute]
    """Attributes to set to the object"""

class LogicalAssignmentResolvedNodes:
    """
    Holds resolved nodes of each LA
    """
    def __init__(self, ) -> None: ...
    LaObj: Teamcenter.Soa.Client.Model.ModelObject
    """LA object"""
    ResolvedNodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Resolved nodes of LA object"""

class ResolveData:
    """
    Data for object to resolve
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """object to resolve"""
    LaResolveType: str
    """what type of LAs to resolve (class name)"""
    Recursive: bool
    """
            if this flag is true, resolve all LAs of the above type of this object, all operations
            and processes under this object, all operations and processes under child processes
            and so on
            """

class ResolvedNodesInput:
    """
    Input for getResolvedNodesFromLA SOA
    """
    def __init__(self, ) -> None: ...
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    """parent operation/process"""
    LaObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """vector of LA objects of this op/proc, for which we want resolved nodes"""

class ResolvedNodesOutput:
    """
    Holds resolved nodes of the whole parent object
    """
    def __init__(self, ) -> None: ...
    ParentObject: Teamcenter.Soa.Client.Model.ModelObject
    """Parent object"""
    LaResolvedNodes: list[LogicalAssignmentResolvedNodes]
    """Resolved nodes of all LA objects"""

class Model:
    """
    Interface Model
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CalculateCriticalPath(self, Roots: list[Teamcenter.Soa.Client.Model.ModelObject]) -> CalculateCriticalPathResponse:
        """    
             Calculate the critical paths for MFGBVRProcess, MFGBVROperation or MFGBVRActivity
             and their corresponding APS objects. A critical path is the sequence of processes,
             operations or activities that determine the minimum duration of the root object.
             Thereby only those MFG objects will be considered that are either direct sub elements
             or implementers of the root object.
             
        :param Roots: 
                         The list of MFG BVR or APS root objects the critical path is to be calculated for.
             
        :return: For each object in the roots vector the list of critical paths. There maybe more
             than one per object if multiple paths of the same length exist.
        """
        ...
    def CreateFlow(self, Input: list[FlowInput]) -> FlowResponse:
        """    Create a new mfgFlow object between two mfg objects i.e process or operation
        :param Input: 
                         a vector of  FlowInput structures.
             
        :return: Flow Response a vector of all the new created flow objects
        """
        ...
    def EditLogicalAssignments(self, LaEditVec: list[LogicalAssignmentData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    This service enables editing the values of Logical Assignment objects.
        :param LaEditVec: 
                         Vector of objects to edit.
             
        :return: Service Data object that contains errors
        """
        ...
    def GetResolvedNodesFromLA(self, InputObjects: list[ResolvedNodesInput]) -> GetResolvedNodesFromLAResponse:
        """    
             This service returns the resolved nodes for each of the received Logical Assignment
             objects.
             
        :param InputObjects: 
                         Input objects for which to return resolved nodes.
             
        :return: Response object
        """
        ...
    def RemoveFlow(self, Input: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Removing existing Flow objects.
        :param Input: 
                         a vector of  Flows to remove.
             
        :return: Service Data object
        """
        ...
    def ResolveLogicalAssignments(self, LaVec: list[Teamcenter.Soa.Client.Model.ModelObject], ResolveObjects: list[ResolveData], ExternalSources: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This service will resolve and re-resolve logical assignments to concrete assignments
             against the product structure.
             
        :param LaVec: 
                         Vector of Logical Assignment objects to resolve
             
        :param ResolveObjects: 
                         Vector of objects to resolve for each object the service will resolve all its Logical
                         Assignments
             
        :param ExternalSources: 
                         Vector of loaded product structures on which to run the resolve mechanism
             
        :return: Service Data object that contains errors and a list of Logical Assignment objects
             that were actually updated.
        """
        ...

