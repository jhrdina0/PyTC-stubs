import System
import Teamcenter.Services.Strong.Bom._2008_06.StructureManagement
import Teamcenter.Services.Strong.Bom._2010_09.StructureManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model.Strong

class StructureManagementRestBindingStub(StructureManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateBaseline(self, Inputs: list[Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.BaselineInput]) -> Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.BaselineResponse: ...
    def AddOrUpdateChildrenToParentLine(self, Inputs: list[Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.AddOrUpdateChildrenToParentLineInfo]) -> Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.AddOrUpdateChildrenToParentLineResponse: ...
    def RemoveChildrenFromParentLine(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.RemoveChildrenFromParentLineResponse: ...
    def GetTraversedObjectsByRule(self, Input: Teamcenter.Services.Strong.Bom._2010_09.StructureManagement.TraversedObjectsInput) -> Teamcenter.Services.Strong.Bom._2010_09.StructureManagement.TraversedObjectsResponse: ...
    def VerifyObjectCoverageByRule(self, Input: Teamcenter.Services.Strong.Bom._2010_09.StructureManagement.ObjectCoverageInput) -> Teamcenter.Services.Strong.Bom._2010_09.StructureManagement.ObjectCoverageResponse: ...

class StructureManagementService:
    """
    
            The BOM StructureManagement service exposes operations that are used to adds item
            or item revision to the parent bomline, creates a new Baseline, removes item or item
            revision to the parent bomline, traverses the structure according to supplied filtering
            rule, verifies whether the received lines fit the supplied filtering rule.
            

            This service provides following use cases:
            


Adds item or item revision (depending on precise or imprecise structure),
            item element  or bomview to the parent bom line in a relative Structure.
            
Creates a new Baseline ItemRevision based on a work in progress ItemRevision.
            
Removes the bom lines from parent bomline in a structure.
            
Traverses the structure according to supplied filtering rule.
            
Verifies whether the received lines fit the supplied filtering rule.
            




Library Reference:

TcSoaBomStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateBaseline(self, Inputs: list[Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.BaselineInput]) -> Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.BaselineResponse:
        """    
             Creates a new Baseline ItemRevision based on a work in progress ItemRevision.
             If the input ItemRevision consists of a PSBOMViewRevision that represents
             a multi level structure, all components of the structure are baselined in a recursive
             fashion. If smart baseline option is enabled at the site, then components of the
             structure will be baselined only if they satisfy the criteria set forth by smart
             baseline feature. Released ItemRevision objects are not baselined, unless
             the specific name of ReleaseStatus object is mentioned in the preference Baseline_allowed_baserev_statuses.
             

Teamcenter Component:

             Baseline - Allows creation of a new baseline ItemRevision based on an input ItemRevision
             
        :param Inputs: 
                         Each of the structures , holds the <b>ItemRevision</b> to be baselined, <b>RevisionRule</b>
                         and valid <b>PSViewType</b> name to be used in case the <b>ItemRevision</b> has <b>BOMViewRevision</b>.
                         Dry run can be performed by providing value as 'true' for the dry run flag. In addition
                         to the above, user  needs to provide the Workflow template name to be used for baselining
                         and job name required to initialize the baseline workflow process.
             
        :return: sets of Teamcenter Data Model object from a service request. This also holds services
             exceptions. To process BaselineResponse:
        """
        ...
    def AddOrUpdateChildrenToParentLine(self, Inputs: list[Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.AddOrUpdateChildrenToParentLineInfo]) -> Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.AddOrUpdateChildrenToParentLineResponse:
        """    
             This operation takes item / item revision (depending on precise or
             imprecise structure) or a GDE. It takes view type to create a BOMView
             for the parent line in a product structure.  When the BOMLine for the item/item
             revision is provided and client id is empty, an update will be performed.
             

Use Cases:


User wants to update properties of two lines. He/She invokes the
             operation with the two lines and property values. The two lines will be updated with
             the specified property values.
             
User wants to create two lines with certain initial property values.
             He/she invokes the operation with the parent line, the two items to add and the initial
             property values. Two new lines will be created with the initial property values.
             
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Inputs: 
                         This is a vector of AddOrUpdateChildrenToParentLineInfo. Each element of this vector
                         contains an input <b>BOMLine</b> which is going to get updated, view type e.g. CAEAnalysis,
                         MEProcess, MESetup, View, an array of ItemLineInfo and ItemElementLineInfo capturing
                         the details of children to be added or updated.
             
        :return: structures containing newly added Item BOMLines, Item Element Lines and ServiceData
             containing any created child bomline and the updated bomline object will be sent
             back in the standard ServiceData member lists of created objects and updated objects
             respectively. Any failures will be returned in the ServiceData list of partial errors.
        """
        ...
    def RemoveChildrenFromParentLine(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Bom._2008_06.StructureManagement.RemoveChildrenFromParentLineResponse:
        """    
             This operation allows developers to remove a BOMLine from an assembly /product
             structure. This operation takes vector of BOMLine business objects as input,
             which allows removal of multiple BOMLines from the structure in a single operation.
             

Use Cases:

             User wants to remove two lines. He/She invokes the operation with the lines, and
             the lines are removed.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Bomlines: 
                         This is a vector of <i>Teamcenter::BOMLine</i> and contains all the <i>BOMLines</i>
                         that need to be deleted from an assembly/product structure
             
        :return: sets of Teamcenter Data Model object from a service request. This also holds services
             exceptions.
        """
        ...
    def GetTraversedObjectsByRule(self, Input: Teamcenter.Services.Strong.Bom._2010_09.StructureManagement.TraversedObjectsInput) -> Teamcenter.Services.Strong.Bom._2010_09.StructureManagement.TraversedObjectsResponse:
        """    
             This SOA traverses the structure according to supplied filtering rule and returns
             the full list of resulting lines.
             

Teamcenter Component:

             BOM Expand - Set of core services that allow to efficiently solve a product structure
             based on revision rules; effectivities etc.
             
        :param Input: 
                         TraversedObjectsInput structure
             
        :return: return the filtered and expanded lines for a structure
        """
        ...
    def VerifyObjectCoverageByRule(self, Input: Teamcenter.Services.Strong.Bom._2010_09.StructureManagement.ObjectCoverageInput) -> Teamcenter.Services.Strong.Bom._2010_09.StructureManagement.ObjectCoverageResponse:
        """    
             This SOA verifies whether the received lines fit the supplied filtering rule.
             

Teamcenter Component:

             BOM Expand - Set of core services that allow to efficiently solve a product structure
             based on revision rules; effectivities etc.
             
        :param Input: 
                         ObjectCoverageInput structure
             
        :return: for each received line returns whether it fits the supplied closure rule
        """
        ...

