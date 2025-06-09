import Teamcenter.Services.Strong.Ai._2006_03.Ai
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GenerateArrangementsResponse:
    """
    GenerateArrangementsResponse struct
    """
    def __init__(self, ) -> None: ...
    FileTicket: str
    """The FMS ticket is used to get the generated PLMXML file."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data is used to report any partial failures."""

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateArrangements(self, ItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision, RevRule: Teamcenter.Services.Strong.Ai._2006_03.Ai.Configuration, BvType: str) -> GenerateArrangementsResponse:
        """    
             The generateArrangements operation will generate a PLMXML file with arrangements
             for an Item Revision. This operation will find out the BOMView Revision with input
             BOMView Type associated to the Item Revision at first and then do generating process.
             An Item Revision and a BOMView Type can specify an unique BOMView Revision. If input
             BOMView Type is NULL, the default BOMView Type will be picked up. A revision rule
             can be applied to the BOMView Revision while generating. The output is struct GenerateArrangementsResponse
             with generated PLMXML file ticket and soa service data.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param ItemRev: 
                         The Item Revision object to generate arrangements from.
             
        :param RevRule: 
                         The revision rule to be applied to BOMView Revision of input Item Revision.
             
        :param BvType: 
                         The BOMView Type name to be used to specify the BOMView Revision of the input Item
                         Revision. There may be more than one BOMView Revision associated to an Item Revision
                         with different BOMView Types. If the input BOMView Type name is NULL, the default
                         BOMView Type will be used to pick up the BOMView Revision.
             
        :return: The FMS ticket to generated PLMXML file and any partial failures.
        """
        ...

