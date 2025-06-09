import Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model.Strong

class AspectManagementRestBindingStub(AspectManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExpandAspects(self, AspectExpandInfo: list[Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement.ExpandAspectsInfo]) -> Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement.ExpandAspectsResponse: ...
    def GetAspectSchemesInModel(self, InputModels: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel]) -> Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement.GetAspectSchemesResponse: ...

class AspectManagementService:
    """
    
            Service for managing aspect operations.
            


Library Reference:

Asp0SoaAsp0AspectStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AspectManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExpandAspects(self, AspectExpandInfo: list[Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement.ExpandAspectsInfo]) -> Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement.ExpandAspectsResponse:
        """    
             This operation allows various types of desired expand and navigation operations on
             aspect and aspect-related model elements (these aspected model elements are also
             called engineering objects.)
             
             If the same input starting node is requested more than once for a given expansion
             semantic, a warning is given and the redundant input is skipped.
             
             If the same input starting node is requested more than once but with different expansion
             semantics, then multiple ExpandResult structures
             will be returned, one for each requested expansion semantic.
             


Use Cases:

             For each input ExpandAspectsInfo:
             
             1. Expand from one aspect to child aspects.
             
             2. Expand from one aspect to other aspects in different aspect schemes in which
             the resulting aspects are related to the same model element as the input aspect.
             
             3. While expanding, include the set of aspect parents at all levels for the resulting
             aspects.
             
             This use case is needed because the parent aspects and the associated engineering
             objects provide context for a given aspect in a particular scheme.
             
IncludeParentChain set to True enables this use case.
             
             4. Expand from one engineering object or model element to its aspects in various
             specified aspect schemes.
             


Dependencies:

             getAspectSchemesInModel
             

Teamcenter Component:

             Aspect Infrastructure Support - Teamcenter component for asp0aspect template
             
        :param AspectExpandInfo: 
                         A set of inputs, each containing the information needed to execute an expansion of
                         a set of aspects to child aspects and possibly related aspects in different aspect
                         schemes within the same application model.
             
        :return: 
        """
        ...
    def GetAspectSchemesInModel(self, InputModels: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel]) -> Asp0.Services.Strong.Asp0aspect._2015_07.AspectManagement.GetAspectSchemesResponse: ...

