import Pfp0.Services.Strong.Featureplanning._2020_12.FeaturePlanningManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model.Strong

class FeaturePlanningManagementRestBindingStub(FeaturePlanningManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetTargetPlanDetails(self, ConfPerspecitve: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, TargetPlans: list[Teamcenter.Soa.Client.Model.Strong.Cfp0AbsVolumePlan]) -> Pfp0.Services.Strong.Featureplanning._2020_12.FeaturePlanningManagement.GetTargetPlanDetailsResponse: ...
    def GetTargetPlans(self, ConfPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, PlanType: str, PlanValidity: list[Pfp0.Services.Strong.Featureplanning._2020_12.FeaturePlanningManagement.PlanValidity], Models: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsModel]) -> Pfp0.Services.Strong.Featureplanning._2020_12.FeaturePlanningManagement.GetTargetPlansResponse: ...

class FeaturePlanningManagementService:
    """
    
            This service contains operations related to Product Configurator Feature Planning.
            

Dependencies:

            DataManagement
            


Library Reference:

Pfp0SoaFeatureplanningStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> FeaturePlanningManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetTargetPlanDetails(self, ConfPerspecitve: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, TargetPlans: list[Teamcenter.Soa.Client.Model.Strong.Cfp0AbsVolumePlan]) -> Pfp0.Services.Strong.Featureplanning._2020_12.FeaturePlanningManagement.GetTargetPlanDetailsResponse: ...
    def GetTargetPlans(self, ConfPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, PlanType: str, PlanValidity: list[Pfp0.Services.Strong.Featureplanning._2020_12.FeaturePlanningManagement.PlanValidity], Models: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsModel]) -> Pfp0.Services.Strong.Featureplanning._2020_12.FeaturePlanningManagement.GetTargetPlansResponse: ...

