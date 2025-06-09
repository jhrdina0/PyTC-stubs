import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class ExecutionStatusPropInfo:
    """
    The structure represents Work Order status properties from the MES system
    """
    def __init__(self, ) -> None: ...
    PropMap: System.Collections.Hashtable
    """
            A map (string, string) of work order execution status properties and their corresponding
            values from the MES system.
            
            The properties would be running, scheduled and completed workorders.
            """

class WorkOrderStatusResponse:
    """
    
            The response contains map where the key is the Mei0ExecutionPlan(Work Order) UID
            and the value is map of execution status properties and their corresponding values
            from MES system.
            
            The following partial error may be returned:
            
            286564 : If the Execution Plan is not a Work Order
            
            325009 : MES system service error
            
            325008 : MES system connection error
            
    """
    def __init__(self, ) -> None: ...
    StatusMap: System.Collections.Hashtable
    """
            A map (string, ExecutionStatusPropInfo) of Mei0ExecutionPlan(Work Order) UID and
            corresponding status properties from the MES system.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data containing partial errors."""

class Release:
    """
    Interface Release
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindWorkOrderStatusProps(self, OrderCCs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> WorkOrderStatusResponse: ...

