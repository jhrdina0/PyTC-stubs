import System
import Teamcenter.Services.Strong.Ai._2012_09.Ai
import Teamcenter.Soa.Client.Model
import typing

class FindRequestOnAiWithReferencesResponse:
    """
    
            The latest RequestObjects (by creation date) that are on the AppInterface
            objects (latest by creation date) that reference the input baseRefs .
            
            The following partial errors may be returned:
            

Â Â Â Â Invalid inputs
            
    Permission errors
            


    """
    def __init__(self, ) -> None: ...
    Details: list[Teamcenter.Services.Strong.Ai._2012_09.Ai.RequestDetail]
    """
            Each element in the details (type _2012_09::Ai::RequestDetail) vector maps to the
            corresponding set based input vector and contains the following fields.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The standard soa serviceData that is used for adding partial errors and sending properties
            of the object. The properties that are returned by default ( without getting not
            loaded exception ) are:
            

object_name
            
object_desc
            

"""

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindRequestOnAiWithReferences(self, BaseRef: list[Teamcenter.Soa.Client.Model.ModelObject], RequestType: str) -> FindRequestOnAiWithReferencesResponse:
        """    
             The operation queries for the latest RequestObjects (by creation date and
             type) on the latest ApplicationInterface Object ( by creation date) that references
             the input object in the base_refs member. Additional filtering based on type of RequestObject
             is also possible.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param BaseRef: 
                         The input is set based.
             
        :param RequestType: 
<ul>
<li type="disc">Sync
                         </li>
<li type="disc">Publish
                         </li>
<li type="disc">All (default if value is not one of Sync or Publish including NULL)
                         </li>
</ul>

        :return: 
        """
        ...

