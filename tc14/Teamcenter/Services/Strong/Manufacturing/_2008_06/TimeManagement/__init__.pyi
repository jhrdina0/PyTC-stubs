import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AllocatedTime:
    """
    Allocated Time structure for allocatedTimeRollUp operation
    """
    def __init__(self, ) -> None: ...
    Roots: list[Teamcenter.Soa.Client.Model.ModelObject]
    """vector of Tags of the item element"""
    CalculatedBy: str
    """The type of calculation for the allocated time algorythm.possible values: duration_time,simulated_time,estimated_time,best_available_time."""

class AllocatedTimeResponse:
    """
    Return structure for allocatedTimeRollUp operation
    """
    def __init__(self, ) -> None: ...
    Results: System.Collections.Hashtable
    """MAp of each root and its allocated time result."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data strucuture used to return sets of Teamcenter Data Model object
            from a service request. This also holds services exceptions.
            """

class TimeAnalysisInputs:
    """
    Time Analysis Inputs structure for timeAnalysisRollup operation
    """
    def __init__(self, ) -> None: ...
    Roots: list[Teamcenter.Soa.Client.Model.ModelObject]
    """vector of Tags of the item element"""
    RunTimePropertiesToRecalc: list[str]
    """
            The additional run time  properties need to be calculated for the time analysis such
            as total time and duration time
            """

class TimeAnalysisResult:
    """
    Time Analysis Results structure for timeAnalysisRollup operation
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """the item element for the rollup."""
    CategoryResults: System.Collections.Hashtable
    """a map results of the activity total time for each category."""
    MapRunTimeResult: System.Collections.Hashtable
    """a map results of the requested run time properties."""

class TimeAnalysisRollupResponse:
    """
    Return structure for timeAnalysisRollup operation
    """
    def __init__(self, ) -> None: ...
    Results: list[TimeAnalysisResult]
    """vector of the TimeAnalysisResult."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data strucuture used to return sets of Teamcenter Data Model object
            from a service request. This also holds services exceptions.
            """

class TimeManagement:
    """
    Interface TimeManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AllocatedTimeRollUp(self, Object: AllocatedTime) -> AllocatedTimeResponse:
        """    Calculates the allocated time for each requested bop line.
        :param Object: 
                         TODO
             
        :return: structure containing the results of the allocated time calculation.
        """
        ...
    def TimeAnalysisRollup(self, Inputs: TimeAnalysisInputs) -> TimeAnalysisRollupResponse:
        """    
             Calculates the total time for each activity category under a requested bop line.
             An additional calculation is all the run time propertie related to the bop line time
             calculations such as total time and duration time.
             
        :param Inputs: 
                         a Time Analysis Input structure, required
             
        :return: structure containing the results of the time analysis calculation.
        """
        ...

