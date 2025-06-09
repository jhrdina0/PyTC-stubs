import Teamcenter.Soa.Client.Model
import typing

class CreateOrUpdateSubSchInput:
    """
    This data structure contains the data required to create or update schedules.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created, optional"""
    BusinessObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Represents the input businessobject of type Cdm0DataReqItemRevision or  Cdm0ContractRevision
            for which submittal delivery schedule or Contract Event Schedule is to be generated.
            """
    ScheduleTemplate: Teamcenter.Soa.Client.Model.ModelObject
    """
            A Schedule business object which is used as a template schedule to generate the contract
            event schedule. This is optional parameter and valid only if the contractObject input
            is of type Cdm0ContractRevision.
            """
    UpdateImpactedOnly: bool
    """
            The flag to indicate whether rescheduling needs to be done for only impacted DRIs.
            If true, submittal delivery schedule will be generated provided the Cdm0DataReqItemRevision
            is really impacted. If false, Submittal delivery schedule will be generated without
            applying any checks.
            """

class ContractManagement:
    """
    Interface ContractManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateSubDelSchedules2(self, CreateOrUpdateSubSchInput: list[CreateOrUpdateSubSchInput], PerformAsynchronously: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...

