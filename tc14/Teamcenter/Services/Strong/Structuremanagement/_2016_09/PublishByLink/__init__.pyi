import System
import Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindSourcesOutput:
    """
    
Contains multiple source BOMLine and integer based index to point output to
corresponding input.
    """
    def __init__(self, ) -> None: ...
    InputIndex: int
    """Index to input list. Useful to map output list to input list."""
    SourceLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            The source BOMLines objects for input target BOMLine and source
            BOMWindow. Source BOMLine and Target BOMLine are associated
            via PublishLink.
            """

class FindSourcesResponse:
    """
    
Contains FindSourcesOutput containing multiple
source BOMLine and index to map to source BOMLine to corresponding
input target BOMLine.
    """
    def __init__(self, ) -> None: ...
    Output: list[FindSourcesOutput]
    """
FindSourcesOutput containing multiple source
            BOMLine and integer index to map source BOMLine to input target BOMLine.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
ServiceData with plain objects containing
            multiple source BOMLine and partial errors.
            """

class PublishByLink:
    """
    Interface PublishByLink
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindSourcesInWindow(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LineAndWindow]) -> FindSourcesResponse:
        """    
             Finds all source BOMLines objects of the PublishLink in source BOMWindow
             for input target BOMLine objects. All sources are returned as BOMLine
             objects.
             

Use Cases:

             Determine if BOMWindow has sources for input target BOMLine objects.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
                         This containing target <b>BOMLine</b> and <b>BOMWindow</b> in which source of <b>PublishLink</b>
                         to search.
             
        :return: 46002 Invalid tag received by BOM Module.
        """
        ...

