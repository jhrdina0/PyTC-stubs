import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DemandProfileRequest:
    """
    This represents the input structure for calculating DemandProfile data for each
schedule.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """Input schedule of which DemandProfile data will be calculated."""
    StartPeriod: str
    """Start of schedule Period to calculate data (MM-YYYY)."""
    EndPeriod: str
    """End of schedule Period to calculate data (MM-YYYY)."""
    MonthsInPeriod: int
    """Number of months in the period."""
    Currency: str
    """Currency to calculate the cost (ISO 4217). (Not currently used)"""

class DemandProfileResponse:
    """
    This represents the output structure for calculated DemandProfile data for each
shecule.
    """
    def __init__(self, ) -> None: ...
    Schedule: Teamcenter.Soa.Client.Model.Strong.Schedule
    """Schedule loaded for DemandProfile data."""
    ActiveBaseline: Teamcenter.Soa.Client.Model.Strong.Schedule
    """The active baseline of the schedule."""
    LaborDemand: list[ItemDemand]
    """Labor demand calculated for the schedule."""
    CapitalDemand: list[ItemDemand]
    """Capital Demand calculated for the schedule."""
    ExpenseDemand: list[ItemDemand]
    """Expense Demand calculated for the schedule."""
    Currency: str
    """Currency used in the calculations (not currently used)."""

class DemandProfileResponses:
    """
    This represents the DemandProfileResponses for a schedule.
    """
    def __init__(self, ) -> None: ...
    Response: list[DemandProfileResponse]
    """The Demand Profile Information of one schedule."""
    Data: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData."""

class ItemDemand:
    """
    This represents the output structure to store the labor demand per resource.
    """
    def __init__(self, ) -> None: ...
    ResourceId: str
    """Represents the resource id of an individual labor or resource."""
    Costs: list[PeriodCost]
    """Represents the per period cost of an individual resource."""

class PeriodCost:
    """
    This represents the output structure to store the cost vasule per period.
    """
    def __init__(self, ) -> None: ...
    PeriodNum: int
    """Represents the period number."""
    Cost: str
    """Represents the cost calculated per each period."""

class ScheduleManagement:
    """
    Interface ScheduleManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDemandProfile(self, Requests: list[DemandProfileRequest]) -> DemandProfileResponses:
        """    
             Calculates the demand profile data for a schedule based on the initial input request
             to the Application Interface..
             

Teamcenter Component:

             Schedule Management - Application in Teamcenter to manage project schedules
             
        :param Requests: 

        :return: The demand profile information and errors. The information includes the schedule,
             start period, end period, and months in period.
        """
        ...

