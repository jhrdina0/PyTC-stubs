import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetTargetPlanDetailsResponse:
    """
    
            The response structure containing the Target Plan and associated Targets information
            along with the objects on which Targets have been defined.
            
    """
    def __init__(self, ) -> None: ...
    TargetPlanDetails: list[TargetPlanDetails]
    """
            A list of  TargetPlanDetails structure containing
            the input Target Plan, associated root Target, associated root Product Line or Product
            Model and map of owning object to list of associated target objects under target
            plan.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """An object of ServiceData for any error information."""

class GetTargetPlansResponse:
    """
    
            Structure containing the Target Plan along with Product Line or Product Model for
            the given Configurator Perspective, plan type and plan date range.
            
    """
    def __init__(self, ) -> None: ...
    TargetPlansInfo: list[TargetPlanInfo]
    """
            A list of  TargetPlanInfo structure containing
            the Target Plan information along with root Product Line or Product Model for the
            given Configurator Perspective and plan type.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """An object of ServiceData for any error information."""

class PlanValidity:
    """
    Structure containing target plan validity date range.
    """
    def __init__(self, ) -> None: ...
    ValidFrom: System.DateTime
    """Start date of target plan. This is considered as start of the day."""
    ValidTo: System.DateTime
    """End date of target plan. This is considered as end of the day."""

class TargetPlanDetails:
    """
    
            The output structure containing the Target Plan with root target, root Product Line
            or Product Model and map of owning objects to the list of associated targets for
            the given Configurator Perspective and Target Plans.
            
    """
    def __init__(self, ) -> None: ...
    TargetPlan: Teamcenter.Soa.Client.Model.Strong.Cfp0AbsVolumePlan
    """
            The source Target Plan (Cfp0AbsVolumePlan) object for which Target details
            has been retrieved.
            """
    RootTarget: Teamcenter.Soa.Client.Model.Strong.Cfp0AbsVolume
    """
            The root Target (Cfp0AbsVolume) object created under targetPlan.
            """
    RootModel: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsModel
    """
            The Product Line or Product Model (Cfg0AbsModel) object against which the
            rootTarget is created.
            """
    TargetInfo: System.Collections.Hashtable
    """
            A map (Cfg0AbsConfiguratorWSO,list of Cfp0AbsVolume) of owning objects
            and list of Targets created under targetPlan.
            """

class TargetPlanInfo:
    """
    
            Structure containing the Target Plan information along with root Product Line or
            Product Model for the given Configurator Perspective and plan type.
            
    """
    def __init__(self, ) -> None: ...
    Model: Teamcenter.Soa.Client.Model.Strong.Cfg0AbsModel
    """
            A Cfg0AbsModel object is a Product Line or Product Model for which Target
            Plan is retrieved. If Product Line or Product Model was not provided in input then
            this object would contain Product Line or Model for which associated Target Plan
            has root level Target defined. This would be Null, if targetPlans
            retrieved are not subtype of Cfp0AbsProductMixPlan and Cfp0AbsProductPlan.
            """
    TargetPlans: list[Teamcenter.Soa.Client.Model.Strong.Cfp0AbsVolumePlan]
    """A Cfp0AbsVolumePlan object contains the list of Target Plans for the model."""

class FeaturePlanningManagement:
    """
    Interface FeaturePlanningManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetTargetPlanDetails(self, ConfPerspecitve: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, TargetPlans: list[Teamcenter.Soa.Client.Model.Strong.Cfp0AbsVolumePlan]) -> GetTargetPlanDetailsResponse: ...
    def GetTargetPlans(self, ConfPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, PlanType: str, PlanValidity: list[PlanValidity], Models: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsModel]) -> GetTargetPlansResponse: ...

