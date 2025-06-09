import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class PublishByLink:
    """
    Interface PublishByLink
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteLinksForSource2(self, SourceBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], DataToUnpublish: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Finds and deletes PublishLink for input source BOMLine objects.
             

             The AbsOccXform of the target BOMLine objects will be deleted if dataToUnpublish is TRANSFORM. All in context JTs
             of the target BOMLine objects will be unattached if dataToUnpublish
             is SHAPE. If all data(as of now TRANSFORM and SHAPE only) needs to be removed then
             value of dataToUnpublish should be ALL. None
             of the published data will be impacted when dataToPublish
             is empty string.
             

Use Cases:

             Delete PublishLink and unpublish data from target BOMLine.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param SourceBOMLines: 
                         Source <b>BOMLine</b> objects for which  <b>PublishLink</b> to be deleted. The <b>PublishLink</b>
                         found is used to find target <b>BOMLine</b> objects before <b>PublishLink</b>s are
                         deleted.
             
        :param DataToUnpublish: 
                         Data to unpublish. Valid values are TRANSFORM, SHAPRE, ALL or empty string. The value
                         is case sensitive.
             
        :return: 43111 Invalid source as input.
        """
        ...

