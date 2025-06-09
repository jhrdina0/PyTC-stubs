import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MACreatedInfo:
    """
    
            The structure for SSF0MaintenanceAction object and information that SSF0MaintenanceAction
            is either newly created or already existed
            
    """
    def __init__(self, ) -> None: ...
    CreatedMA: Teamcenter.Soa.Client.Model.ModelObject
    """
            The SSF0MaintenanceAction objects either newly created or already existing
            for given asset, impacted part and FaultCode combination
            """
    IsCreated: bool
    """
            whether the SSF0MaintenanceAction is created or already existed. true if SSF0MaintenanceAction
            is created and false if already existed.
            """

class MaintenanceActionOutInfo:
    """
    
            The Structure contains output information of SSF0MaintenanceAction created
            for impacted part and FaultCode.
            
    """
    def __init__(self, ) -> None: ...
    AllMAs: list[MACreatedInfo]
    """
            The list of MACreatedInfo structure, specifying  SSF0MaintenanceAction
            objects and information that SSF0MaintenanceAction is either newly created
            or already existed
            """
    ImpactedPart: Teamcenter.Soa.Client.Model.ModelObject
    """The part of the asset for which SSF0MaintenanceAction is returned."""
    FaultCode: Teamcenter.Soa.Client.Model.Strong.FaultCode
    """The FaultCode for which SSF0MaintenanceAction is returned."""

class MaintenanceActionResponse:
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data."""
    MaOutInfo: list[MaintenanceActionOutInfo]
    """A list of created maintenanceActionOutInfo structure"""

class MaintenanceInputInfo:
    """
    
            A MaintenanceInputInfo structure, which hold the required information for creating
            MaintenanceAction.
            
    """
    def __init__(self, ) -> None: ...
    Asset: Teamcenter.Soa.Client.Model.ModelObject
    """
            The top level or sub-assembly asset which contains the impacted part. Valid object
            types are PhysicalPart, PhysicalPartRevision or PhysicalBOMLine
"""
    ImpactedPart: Teamcenter.Soa.Client.Model.ModelObject
    """
            The part of the asset for which anamoly has been dectected. Valid object types are
            PhysicalPart, PhysicalPartRevision or PhysicalBOMLine
"""
    FaultCode: Teamcenter.Soa.Client.Model.Strong.FaultCode
    """The FaultCode of the the anamoly."""
    AdditionalPropsOnMA: System.Collections.Hashtable
    """
            A map(string, string) that speicfies additional properties that need to be set on
            SSF0MaintenanceAction object created
            """

class ServiceForecasting:
    """
    Interface ServiceForecasting
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateMaintenanceActionByFaultCode(self, Info: list[MaintenanceInputInfo]) -> MaintenanceActionResponse: ...

