import System
import Teamcenter.Soa.Client.Model
import typing

class SrchConnectedLinesOutput:
    """
    Object containing input connection and connected BOMLines.
    """
    def __init__(self, ) -> None: ...
    ConnectionLine: Teamcenter.Soa.Client.Model.ModelObject
    """Input connection BOMLine."""
    ConnectedLines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Connected BOMLine objects."""

class SrchConnectedLinesResponse:
    """
    Return object for searchConnectedLines operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[SrchConnectedLinesOutput]
    """List of objects containing input connection and connected BOMLines."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data."""

class StructureSearch:
    """
    Interface StructureSearch
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SearchConnectedLines(self, InputConnLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> SrchConnectedLinesResponse:
        """    
             This operation searches and returns the connected BOMLine objects for the
             input connection BOMLine objects.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param InputConnLines: 
                         Input <b>BOMLine</b> objects whose connected to information needs to be found.
             
        :return: 
        """
        ...

