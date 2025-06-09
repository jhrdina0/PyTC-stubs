import Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2021_06.MultiDisciplinaryDataMgt
import Mdo0.Services.Strong.Mdomanagement._2021_12.MultiDisciplinaryDataMgt
import System
import Teamcenter.Soa.Client

class MultiDisciplinaryDataMgtRestBindingStub(MultiDisciplinaryDataMgtService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateMDO(self, MdoInputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.MDOInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.CreateOrUpdateMDOResponse: ...
    def LinkDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.DesignInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.InstancesToLinkResponse: ...
    def SearchForArtifactsUsingInstances(self, SearchInputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForDesignArtifactInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchMDOResponse: ...
    def SearchForLinkedDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesResponse: ...
    def SearchMDO(self, SearchInputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchMDOResponse: ...
    def UnlinkDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.DesignInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.InstancesToUnlinkResponse: ...
    def QryNotificationsByDesignOrProject(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.QryInputByDesignOrProject]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.QryNotificationByDesignResponse: ...
    def QryNotificationsByImpactedDesign(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.NotificationQueryInput]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.QueryNotificationResponse: ...
    def QryNotificationsByOriginDesign(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.NotificationQueryInput]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.QueryNotificationResponse: ...
    def SearchForArtifactsUsingInstances2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.SearchForDesignArtifactInput2]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.SearchMDO2Response: ...
    def SearchMDO2(self, SearchInputs2: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.SearchInput2]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.SearchMDO2Response: ...
    def UpdateMDONotification(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.MDONotificationUpdateInput]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.UpdateMDONotificationResponse: ...
    def CarryForwardMDInstanceAssociation(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.MDInstanceLinkCarryFwdInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesResponse: ...
    def CarryForwardMDThreadAssociation(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.MDThreadLinkCarryFwdInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchMDOResponse: ...
    def LinkDesignInstances2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.DesignInstancesInput2]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.InstancesToLinkResponse2: ...
    def QueryNeedsValidationLink(self, QueryInput: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.NeedsValidationLinkInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.NeedsValidationLinkResponse: ...
    def SearchForArtifactsUsingInstances3(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchForDesignArtifactInput3]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchMDO3Response: ...
    def SearchForLinkedDesignInstances2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchForLinkedInstances2Response: ...
    def SearchMDO3(self, SearchInputs3: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchInput3]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchMDO3Response: ...
    def UpdateDomainRelevancy(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.DomainRelevancyInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.UpdateDomainRelevancyResponse: ...
    def UpdateLinksToValidated(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.UpdateLinkStatusToValidatedInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.UpdateLinksToValidatedResponse: ...
    def UpdateMDInstanceToMDThreadLink(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.MDInstanceToMDThreadInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.UpdateMDInstanceToMDThreadResponse: ...
    def GetDomainRelevancyOfAnObject(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.GetDomainRelevancyInput]) -> Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.GetDomainRelevancyOfAnObjectResp: ...
    def SplitDesignArtifactsOfMDThread(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.SplitDesignArtifactInput]) -> Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.SplitDesignArtifactsResponse: ...
    def SplitDesignInstancesOfMDInstance(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.SplitDesignInstanceInput]) -> Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.SplitDesignInstancesResponse: ...
    def GetLinkedInstancesFor4G(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.GetLinkedInstancesInputFor4G]) -> Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.GetLinked4GAndBVRInstancesResponse: ...
    def GetLinkedInstancesForBVR(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.GetLinkedInstancesInputForBVR]) -> Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.GetLinked4GAndBVRInstancesResponse: ...
    def Link4GAndBVRDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.BVRAnd4GDesignInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.InstancesToLinkResponse2: ...
    def Unlink4GAndBVRDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.BVRAnd4GDesignInstancesUnlinkInput]) -> Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.InstancesToUnlinkResponse2: ...
    def QueryNeedsValidationLink2(self, QueryInputs: list[Mdo0.Services.Strong.Mdomanagement._2021_06.MultiDisciplinaryDataMgt.NeedsValidationLinkInput2]) -> Mdo0.Services.Strong.Mdomanagement._2021_06.MultiDisciplinaryDataMgt.NeedsValidationLinkResponse2: ...
    def UpdateLinksToValidated2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2021_06.MultiDisciplinaryDataMgt.UpdateLinkStatusToValidatedInput2]) -> Mdo0.Services.Strong.Mdomanagement._2021_06.MultiDisciplinaryDataMgt.UpdateLinksToValidatedResponse2: ...
    def GetDomainRelevancyOfAnObject2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2021_12.MultiDisciplinaryDataMgt.GetDomainRelevancyInput2]) -> Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.GetDomainRelevancyOfAnObjectResp: ...
    def UpdateDomainRelevancy2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2021_12.MultiDisciplinaryDataMgt.DomainRelevancyInput2]) -> Mdo0.Services.Strong.Mdomanagement._2021_12.MultiDisciplinaryDataMgt.UpdateDomainRelevancyResponse2: ...

class MultiDisciplinaryDataMgtService:
    """
    
            The MultiDisciplinaryDataMgt service exposes operation to create, modify and search
            for the MDThread objects. The operation allows to search for MDThread
            based on attributes or design artifacts (WorkspaceObject) associated to it.
            
            The service provides following use case
            

Create MDThread object
            
Modify MDThread object
            
Search for MDThread object
            

            .
            

Dependencies:

            DataManagement
            


Library Reference:

Mdo0SoaMDOManagementStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MultiDisciplinaryDataMgtService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateMDO(self, MdoInputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.MDOInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.CreateOrUpdateMDOResponse:
        """    
             The operation creates a  new MDThread  object based on the MDThread
             properties and set of design artifacts (WorkspaceObject). The operation can
             optionally update an existing MDThread object by associating additional required
             design artifacts to it, or removing existing design artifacts association.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param MdoInputs: 
                         List of input data which contains information about the <b>MDThread</b> to be created
                         or updated
             
        :return: 
        """
        ...
    def LinkDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.DesignInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.InstancesToLinkResponse:
        """    
             The operation links two or more design instances from multi-discipline designs together
             through a common object Mdo0MDInstance. The operation may also update the
             design instance linkage by adding more design instances to the existing design instance
             linkage. Currently the Mdl0ModelElement is the supported object for design
             instance. If the linking is precise, the given design instance is used to link to
             the Mdo0Instance. If the linking is imprecise, the Mdl0ElementThread
             object of the Mdl0ModelElement is used for linking. If the input design instance
             is not a revisable type and do not have Mdl0ElementThread  then the instance
             will be linked precisely always.  Context information  for the linking of design
             instances is optional. If the context information is provided while linking design
             instances, then the design instance linkage is valid only for that context.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information to be linked together .
             
        :return: 
        """
        ...
    def SearchForArtifactsUsingInstances(self, SearchInputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForDesignArtifactInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchMDOResponse:
        """    
             The operation searches for MDThread and compatible design artifacts for the
             given design instances. Currently the Mdl0ModelElement is the supported object
             for design instance.  The underlying object for the Mdl0ModelElement is used
             for searching for Md0MDThread. If more than 1 design instance is given as
             input, all the designinstance's underlying object will be identified and collected.
             Then all the Mdo0MDThread objects containing this set of design artifacts
             will be returned.
             

Use Cases:

             Compatible design artifacts are associated to MDThread using createOrUpdateMDO services
             operation.
             
             Later the compatible design artifacts can be searched for using design instances.
             


Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param SearchInputs: 
                         Design instance information and for which compatible design artifacts are to be searched
                         for.
             
        :return: objects along with the associated design artifacts.
             Any failure will be returned with client id mapped to error message in the ServiceData
             list of partial errors.
        """
        ...
    def SearchForLinkedDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesResponse:
        """    
             The operation searches for linked  design instances for the given design instances.
             Currently the Mdl0ModelElement is the supported object for design instance.
             If search is for precise design instance,  using the given input design instance,
             the linked other design instances are searched and returned.  If search is for imprecise
             design instance, the Mdl0ElementThread  object of the Mdl0ModelElement
             is used for search. If the input design instance is not a revisable type and do not
             have Mdl0ElementThread  then the search will be based on precise instance
             always.  If the context information is provided along with design instances input
             while searching for design instances, then the Mdo0MDInstance object for the
             given design instance and context is identified and design instance of the MdoMDInstance
             are returned as linked design instances. If only context information is provided
             as input, all the MdoMDInstance for that context are identified and all the
             design instances of the MdoMDInstance are returned as linked design instances.
             If configuration details are provided as part of input, for every  linked design
             instance if any configuration is provided in input, the configuration is applied
             and if it is valid for this configuration, then the design instance is returned as
             linked design instances.  Otherwise, the design instance is not returned as linked
             design instance for this input configuration.
             

Use Cases:

             The related design instances from Multi-discipline designs are linked together.
             
             Later the impacted design instance can be queried before making any change to the
             design instance.
             


Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information and optional context and configuration details for which
                         linked instances are to be searched for.
             
        :return: 
        """
        ...
    def SearchMDO(self, SearchInputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchMDOResponse:
        """    
             This operation searches the MDThread object based on attributes like name,
             description for MDThread and the search criteria for attributes like name,
             id, type for design artifacts associated to MDThread. Design artifacts will
             be of type WorkspaceObject.  All objects satisfying both MDThread attributes
             criteria and the design artifacts criteria will be returned as search results.
             
             If input has only design artifact objects in input, all MDThread having these
             design artifact associated with it will be returned.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param SearchInputs: 
                         Input search criteria for <b>MDThread</b> object based on <b>MDThread</b> attributes
                         and design artifact objects or attribute input for design artifacts.
             
        :return: search.
        """
        ...
    def UnlinkDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.DesignInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.InstancesToUnlinkResponse:
        """    
             The operation unlinks one or more design instances which are linked together through
             a common Mdo0MDInstance object. Currently the Mdl0ModelElement is the
             supported object for design instance. If the unlinking is precise, the given design
             instance is used to unlink from the Mdo0Instance. If the unlinking is imprecise,
             the Mdl0ElementThread  object of the Mdl0ModelElement is used for unlinking.
             If the input design instance is not a revisable type and do not have Mdl0ElementThread
             then the instance will be unlinked precisely always. Context information  for the
             unlinking of design instances is optional. If the context information is provided
             while unlinking design instances, then the Mdo0MDInstance object for the given
             context is indentified and design instance is unlinked from the MdoMDInstance.
             If the last design instance from the MdoMDInstance is unlinked, the MdoMDInstance
             will also be deleted.
             

Use Cases:

             The related design instances from Multi-discipline designs are linked together.
             
             Later the instance linkage can be modified, by unlinking some of the deisgn instance
             .
             


Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         The design instance information to be unlinked.
             
        :return: 
        """
        ...
    def QryNotificationsByDesignOrProject(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.QryInputByDesignOrProject]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.QryNotificationByDesignResponse:
        """    
             This operation queries for all create and modify MDO notifications for a design or
             for all designs in a project and ordered by date and grouped by design. This helps
             the users to know the sequence of action happened in a design or project. Date criteria
             can be provided as input to know the sequence of operation happened in a design between
             specific times.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Search criteria for <b>Mdo0Notification</b> object for create and modify notifications
                         for a design or project along with date criteria.
             
        :return: 
        """
        ...
    def QryNotificationsByImpactedDesign(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.NotificationQueryInput]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.QueryNotificationResponse: ...
    def QryNotificationsByOriginDesign(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.NotificationQueryInput]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.QueryNotificationResponse: ...
    def SearchForArtifactsUsingInstances2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.SearchForDesignArtifactInput2]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.SearchMDO2Response: ...
    def SearchMDO2(self, SearchInputs2: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.SearchInput2]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.SearchMDO2Response: ...
    def UpdateMDONotification(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.MDONotificationUpdateInput]) -> Mdo0.Services.Strong.Mdomanagement._2015_07.MultiDisciplinaryDataMgt.UpdateMDONotificationResponse:
        """    
             This operation groups the create MDO notifications or modify MDO notifications based
             on the response from user. This operation is expected to be called by the designer
             to update the notification system, after the users reacts to a trigger notification
             either by ignoring the notification or performing a change to his design.
             

Use Cases:

             Compatible design artifacts are associated to MDThread using createOrUpdateMDO SOA
             operation.
             
             Design artifacts of MDThread are consumed in design.
             
             Impacted design instances of design are linked together using linkDesignInstances
             SOA operation.
             
             Design instances are modified [replace/revise/remove etc] in the design.
             
             MDO notification for design instance creation can be searched with filter criteria.
             
             MDO notification for modification can be search using design instance with filter
             criteria.
             
             User working on multi- discipline will make respective change in their design based
             on queried MDO notification
             
             User after reacting to a notification will update the MDO notification system with
             details about what relevant changes are made in impacted design. If a designer reacts
             to a MDO notification, the user will update the system by providing information about
             how the user has reacted and the original notification object for which the user
             reacted. The system will identify the MDO notification and process that and creates
             an accepted response for it and set it on original trigger MDO notification.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Input criteria for updating a <b>Mdo0Notification</b> object for create and modify
                         notifications for responses.
             
        :return: 
        """
        ...
    def CarryForwardMDInstanceAssociation(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.MDInstanceLinkCarryFwdInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesResponse:
        """    
             The operation searches for the Mdo0MDInstance associated with input original design
             instance and associates the target design instance with the identified Mdo0MDInstance
             objects precisely. The newly created Mdo0MDInstance association will capture the
             needs validation status on the association as yes.
             

Use Cases:

             Impacted design instances are associated to Mdo0MDInstance using linkDesignInstances
             services operation.
             
             Later the design instance of Mdo0MDInstance is revised.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information from which the Mdo0MDInstance association needs to be
                         carried forward to a new design instance.
             
        :return: 
        """
        ...
    def CarryForwardMDThreadAssociation(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.MDThreadLinkCarryFwdInput]) -> Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchMDOResponse:
        """    
             The operation searches for the Mdo0MDThread associated with input original design
             artifact and associates the target design artifact with the identified Mdo0MDThread
             objects. The newly created Mdo0MDThread association will capture the needs validation
             status on the association as yes.
             

Use Cases:

             Compatible design artifacts are associated to Mdo0MDThread using createOrUpdateMDO
             services operation.
             
             Later the design artifact of Mdo0MDThread is revised.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design artifact information  based on which the Mdo0MDThread  association needs to
                         be carried forward to the new design artifact.
             
        :return: 
        """
        ...
    def LinkDesignInstances2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.DesignInstancesInput2]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.InstancesToLinkResponse2:
        """    
             The operation links two or more design instances from multi-discipline designs together
             through a common object Mdo0MDInstance. The operation may also update the
             design instance linkage by adding more design instances to the existing design instance
             linkage. Currently the Mdl0ModelElement is the only supported object for design
             instance. If the linking is precise, the given design instance is used to link to
             the Mdo0Instance. If the linking is imprecise, the Mdl0ElementThread
             object of the Mdl0ModelElement is used for linking. If the input design instance
             is not a revisable type and do not have Mdl0ElementThread  then the instance
             will be linked precisely always. Context information  for the linking of design instances
             is optional. If the context information is provided while linking design instances,
             then the design instance linkage is valid only for that context.  Mdo0MDThread
             information to be set on Mdo0MDIntance can be part of input.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information to be linked together .
             
        :return: 
        """
        ...
    def QueryNeedsValidationLink(self, QueryInput: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.NeedsValidationLinkInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.NeedsValidationLinkResponse:
        """    
             This operation searches for Mdo0MDThread association and Mdo0MDInstance
             association which has needs validation status captured on the association. If queryAllMDOLinks
             input is passed in, all the Mdo0MDThread association with the needs validation
             will be searched and returned. If inputMDO is passed in, only Mdo0MDThread
             association with passed in input as primary and association which has needs validation
             will be identified and returned. If input inputDesignArtifact is passed in, all Mdo0MDThread
             association having this design artifact as secondary and needs validation captured
             on association will be returned. If queryAllMDILinks input is passed in, all the
             Mdo0MDInstance association with the needs validation will be searched and
             returned. If input inputDesignInstance is passed in, all Mdo0MDInstance association
             having this design instance as secondary and needs validation captured on association
             will be returned.
             

Use Cases:

             Case1:
             
             Compatible design artifacts are associated to Mdo0MDThread using createOrUpdateMDO
             services operation.
             
             The design artifact of Mdo0MDThread is revised.
             
             Query for MDO association with needs validation link.
             
             Case2:
             
             Impacted design instances are associated to Mdo0MDInstance using linkDesignInstances
             services operation.
             
             The design instance of Mdo0MDInstance is revised.
             
             Query for MDI association with needs validation link.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param QueryInput: 
                         Input search criteria for <b>Mdo0MDThread</b> association and <b>Mdo0MDInstance</b>
                         association which has needs validation status on association.
             
        :return: 
        """
        ...
    def SearchForArtifactsUsingInstances3(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchForDesignArtifactInput3]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchMDO3Response: ...
    def SearchForLinkedDesignInstances2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2014_10.MultiDisciplinaryDataMgt.SearchForLinkedInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchForLinkedInstances2Response:
        """    
             The operation is used to search for linked  design instances for the given input
             design instances. Currently the Mdl0ModelElement is the supported object for
             design instance. If search is for precise design instance,  using the given input
             design instance, the linked other design instances are searched and returned.  If
             search is for imprecise design instance, the Mdl0ElementThread  object of
             the Mdl0ModelElement is used for search. If the context information is provided
             along with design instances input while searching for design instances, then the
             Mdo0MDInstance object for the given design instance and context is identified
             and design instance of the Mdo0MDInstance are returned as linked design instances.
             If only context information is provided as input, all the Mdo0MDInstance for
             that context is identified and all the design instances of the MdoMDInstance is retrurned
             as linked design instances. If configuration destail are provided as part of input,
             for every  linked design instance if any configuration is provided in input, the
             configuration is applied and if it is valid for this configuration, then the design
             instance is returned as linked design instances.  Otherwise, the design instance
             is not returned as linked design instance for this input configuration.
             

Use Cases:

             The related design instances from Multi-discipline designs are linked together.
             
             Later the impacted design instance can be queried before making any change to the
             design instance.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         List of input data which contains design instance information and optional context
                         and configuration details for which linked instances are to be searched for.
             
        :return: 
        """
        ...
    def SearchMDO3(self, SearchInputs3: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchInput3]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.SearchMDO3Response: ...
    def UpdateDomainRelevancy(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.DomainRelevancyInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.UpdateDomainRelevancyResponse: ...
    def UpdateLinksToValidated(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.UpdateLinkStatusToValidatedInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.UpdateLinksToValidatedResponse:
        """    
             The operation updates  association between the given Mdo0MDInstance and its
             design instance,  the given Mdo0MDThread and its design artifact association
             to validated status.
             

Use Cases:

             Case1:
             
             Compatible design artifacts are associated to Mdo0MDThread using createOrUpdateMDO
             services operation.
             
             The design artifact of Mdo0MDThread is revised.
             
             Query for MDO association with needs validation link.
             
             Update the MDO association status to validated.
             
             Case2:
             
             Impacted design instances are associated to Mdo0MDInstance using linkDesignInstances
             services operation.
             
             The design instance of Mdo0MDInstance is revised.
             
             Query for MDI association with needs validation link.
             
             Update the MDI association status to validated.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         The input for <b>Mdo0MDThread</b> and <b>Mdo0MDInstance</b> associations to be updated.
             
        :return: 
        """
        ...
    def UpdateMDInstanceToMDThreadLink(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.MDInstanceToMDThreadInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.UpdateMDInstanceToMDThreadResponse:
        """    
             The operation sets or removes association between the given Mdo0MDInstance
             and Mdo0MDThread business object.
             

Use Cases:

             Compatible design artifacts are associated to Mdo0MDThread using createOrUpdateMDO
             services operation.
             
             The related design instances from Multi-discipline designs are linked together.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         The <b>Mdo0MDThread</b> information to be set on <b>Mdo0MDIntance</b> or removed
                         from <b>Mdo0MDInstance</b>.
             
        :return: 
        """
        ...
    def GetDomainRelevancyOfAnObject(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.GetDomainRelevancyInput]) -> Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.GetDomainRelevancyOfAnObjectResp:
        """    
             The operation returns domain relevancy of a design artifact or design instance for
             a input domain. If input is a design artifact, then the domain relevancy on the design
             artifact is used. If the input is a design instance, then the domain relevancy information
             of it is used. If there is no domain relevancy information on the design instance
             object for a domain, then domain relevancy information based on the underlying design
             artifact of the design instance will be used.
             
             If the input domain is specified then a relevancy value will be returned. If the
             input domain is not given then all domain relevancy information for the input object
             will be returned.
             

Use Cases:

             Associate a design artifact or design instance with domain relevancy information
             using the Mdo0::Soa::MDOManagement::_2017_05::MultiDisciplinaryDataMgt::updateDomainRelevancy
             service operation of MultiDisciplinaryDataMgt Service.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Input object and domain information for which domain relevancy is to be fetched.
             
        :return: 
        """
        ...
    def SplitDesignArtifactsOfMDThread(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.SplitDesignArtifactInput]) -> Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.SplitDesignArtifactsResponse:
        """    
             The operation removes the latest revision  ofdesign artifacts from their common Mdo0MDThread
             and links them to a newly created Mdo0MDThread object.
             
             The input design artifacts must be the latest revisions and must be associated with
             the same Mdo0MDThread.
             
             The new Mdo0MDThread will be returned. The updated Mdo0MDThread objects
             from which the input design artifacts are split are also returned.
             

Use Cases:

             Originally a set of design artifacts are linked to an Mdo0MDThread.
             
             Later a revise of one of the design artifacts will automatically link the new revision
             to the same Mdo0MDThread as the original design artifact.
             
             When a subset of the design artifacts need to be grouped differently, splitDesignArtifactsOfMDThread
             will remove them from one Mdo0MDThread and link them to a new Mdo0MDThread.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design artifact information.
             
        :return: 
        """
        ...
    def SplitDesignInstancesOfMDInstance(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.SplitDesignInstanceInput]) -> Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.SplitDesignInstancesResponse:
        """    
             The operation removes the input design instances from their common Mdo0MDInstance
             and links them to a newly created Mdo0MDInstance object.  Currently the Mdl0ModelElement
             is the only supported object for design instance.
             
             The input design instances must be the latest revisions and must be associated with
             the same Mdo0MDInstance.
             
             The new Mdo0MDInstance will be returned. The updated Mdo0MDInstance
             objects from  which the input design instances are split are also returned.
             

Use Cases:

             Originally a set of design instances are linked to an Mdo0MDInstance.
             
             Later a revise of one of the design instances will automatically link the new revision
             to the same Mdo0MDInstance as the original design instances.
             
             When a subset of the design instances need to be grouped differently, splitDesignInstancesOfMDInstance
             will remove the design instances from one Mdo0MDInstance and link them to
             a new Mdo0MDInstance.
             

Teamcenter Component:

             Mechatronics - Core objects and relationships used by Mechatronics applications such
             as ESM; Wire harness and Manufacturing applications.
             
        :param Inputs: 
                         Design instance information.
             
        :return: 
        """
        ...
    def GetLinkedInstancesFor4G(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.GetLinkedInstancesInputFor4G]) -> Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.GetLinked4GAndBVRInstancesResponse: ...
    def GetLinkedInstancesForBVR(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.GetLinkedInstancesInputForBVR]) -> Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.GetLinked4GAndBVRInstancesResponse: ...
    def Link4GAndBVRDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.BVRAnd4GDesignInstancesInput]) -> Mdo0.Services.Strong.Mdomanagement._2017_05.MultiDisciplinaryDataMgt.InstancesToLinkResponse2: ...
    def Unlink4GAndBVRDesignInstances(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.BVRAnd4GDesignInstancesUnlinkInput]) -> Mdo0.Services.Strong.Mdomanagement._2020_12.MultiDisciplinaryDataMgt.InstancesToUnlinkResponse2: ...
    def QueryNeedsValidationLink2(self, QueryInputs: list[Mdo0.Services.Strong.Mdomanagement._2021_06.MultiDisciplinaryDataMgt.NeedsValidationLinkInput2]) -> Mdo0.Services.Strong.Mdomanagement._2021_06.MultiDisciplinaryDataMgt.NeedsValidationLinkResponse2: ...
    def UpdateLinksToValidated2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2021_06.MultiDisciplinaryDataMgt.UpdateLinkStatusToValidatedInput2]) -> Mdo0.Services.Strong.Mdomanagement._2021_06.MultiDisciplinaryDataMgt.UpdateLinksToValidatedResponse2: ...
    def GetDomainRelevancyOfAnObject2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2021_12.MultiDisciplinaryDataMgt.GetDomainRelevancyInput2]) -> Mdo0.Services.Strong.Mdomanagement._2018_06.MultiDisciplinaryDataMgt.GetDomainRelevancyOfAnObjectResp: ...
    def UpdateDomainRelevancy2(self, Inputs: list[Mdo0.Services.Strong.Mdomanagement._2021_12.MultiDisciplinaryDataMgt.DomainRelevancyInput2]) -> Mdo0.Services.Strong.Mdomanagement._2021_12.MultiDisciplinaryDataMgt.UpdateDomainRelevancyResponse2: ...

