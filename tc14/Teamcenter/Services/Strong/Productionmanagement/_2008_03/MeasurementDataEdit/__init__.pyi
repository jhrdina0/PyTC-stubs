import Teamcenter.Soa.Client.Model
import typing

class TargetEvents:
    """
    
The TargetEvents structure is used to set as active or deactive based on the int
value
    """
    def __init__(self, ) -> None: ...
    PlantId: str
    """
MEPrPlantProcess to which a measurement event or eventSysId
            belongs
            """
    ActiveInactive: bool
    """Use '1' to activate and '0' to deactive measurement events"""
    EventSysId: str
    """
            Event system ID stored in measurement database for the measurement event for which
            the activeInactive status is to be applied
            """

class MeasurementDataEdit:
    """
    Interface MeasurementDataEdit
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ActivateOrDeactivateData(self, TargetRows: list[TargetEvents]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates the status of one or more measurement events specified in
             the list of TargetEvents to active or inactive.
             TargetEvents  includes a plant ID, measurement
             event that belongs to the plant ID, and its associated active status
             

Use Cases:

             Change the active status of measurement events using the Dimensional Planning and
             Validation (DPV) Measurement user interface in the Teamcenter rich client.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param TargetRows: 
                         A list of target events that  includes a plant ID, measurement event ID that belongs
                         to a plant ID, and an active status. Different <font face="courier" height="10">TargetEvents</font>
                         can have different active statuses.
             
        :return: holds model objects and partial
             errors. No model objects are returned in this operation. Also, no specific partial
             error is returned by this operation and only errors from underlying subsystems are
             returned.
        """
        ...

