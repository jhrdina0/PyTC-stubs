import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Tgm0.Services.Strong.Targetmanagement._2016_05.TargetManagement

class TargetManagementRestBindingStub(TargetManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateTargetElements(self, CreateInputs: list[Tgm0.Services.Strong.Targetmanagement._2016_05.TargetManagement.TargetElementCreateInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class TargetManagementService:
    """
    
            This service exposes operations related to Target for Workspace
object in Teamcenter.

Library Reference:

Tgm0SoaTargetManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> TargetManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateTargetElements(self, CreateInputs: list[Tgm0.Services.Strong.Targetmanagement._2016_05.TargetManagement.TargetElementCreateInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates a Tgm0AbsTargetElement object based on the input Target
             Definition( Att0TargetRevision ) object. The Target Element is created in
             the context of the input context object and linked to the input selected Object (
             which can be a Prg0AbsPlan, Cfg0ProductModel or Ptn0Partition
             ). A new Measureable Attribute is created and linked to the newly created Target
             Element. Please refer to documentation for more details on Target Element and Measurable
             Attribute objects.
             

Use Cases:

Use case 1: User wants to create a Volume Target Element  based on an approved
             Target Definition of a Volume Target. The Volume Target Definition defines the required
             target behavior (Target Type, whether the goal value is distributed ) and the Measureable
             Attribute for Volume Target. To create the target element, user passes a Prg0AbsPlan
             object as the context object,; a Prg0AbsPlan , Cfg0ProductModel ,
             or Ptn0Partition object as the source object on which target element will
             be created,; an Att0TargetRevision  object as the target definition object
             and a name for the target element being created as inputs . Using these inputs, the
             system would create a target element, a measurable attribute using the target definition
             and associates them. It also associates the created target element to the input source
             object.
             

Teamcenter Component:

             Attribute Target Management - This component consists of the Client and Enterprise
             Tier code and constructs that support Attribute and Target related functionality
             including such things as Teamcenter Active Workspace application plus SOA, ITK and
             Preferences.
             
        :param CreateInputs: 
                         A list of <font face="courier" height="10">TargetElementCreateInput</font> from which
                         <b>Tgm0AbsTargetElement</b> objects are to be created
             
        :return: .
        """
        ...

