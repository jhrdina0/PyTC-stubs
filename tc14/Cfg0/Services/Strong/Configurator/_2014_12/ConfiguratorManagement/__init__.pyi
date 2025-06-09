import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AdmissibilityData:
    """
    
            The output structure containing the admissibility data corresponding to the context
            object.
            
    """
    def __init__(self, ) -> None: ...
    AdmissibilityList: list[Teamcenter.Soa.Client.Model.Strong.Cfg0AbsAdmissibility]
    """List of the admissibility objects associated with the context POM_Objects."""
    ContextObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """The context object for which the admissibility information is being returned."""

class AdmissibilityOutput:
    """
    
            The output structure containing the admissibility data corresponding to one input
            entry.
            
    """
    def __init__(self, ) -> None: ...
    AdmissibilityDataList: list[AdmissibilityData]
    """The list of admissibility data associated with the context Business Object."""
    Index: int
    """The index for corresponding input structure."""

class GetAdmissibilityInputStruct:
    """
    
            The input structure for the getAdmissibility operation containing the contexts and
            perspective instance with RevisionRule.
            
    """
    def __init__(self, ) -> None: ...
    ConfigPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective
    """
            The Cfg0ConfiguratorPerspective instance to specify the context and revision rule.
            This parameter can be NULL if the operation parameter for the perspective is not
            NULL.
            """
    ContextObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """The list of context business objects having configurator context as defined by configPrespective."""

class GetAdmissibilityResponse:
    """
    Response structure for getAdmissibility operation.
    """
    def __init__(self, ) -> None: ...
    AdmissibilityOutputList: list[AdmissibilityOutput]
    """The list of admissibility information output structures for each input."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data to return partial errors."""

class ConfiguratorManagement:
    """
    Interface ConfiguratorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAdmissibility(self, OperationConfigPerspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, AdmissibilityInputs: list[GetAdmissibilityInputStruct]) -> GetAdmissibilityResponse:
        """    
             This operation returns the admissibility statements for the variability data associated
             with a given set of context objects. The instance of Cfg0AbsAdmissibility object
             represents the relation and state between a configurator specific object and a non-configurator
             specific object. For example, the pair of a partition and an family is associated
             with state "Available". The admissibility states are defined by the LOV Cfg0AdmissibilityState.
             The allowed values for this property are "Available" and "Not Available".
             

Use Cases:

             Consider that following set of the data-
             

             Groups-
             
             Engine-Box (A Family Group) - It has families "Engine" and "Transmission".
             
             1. Engine- Petrol, Diesel
             
             2. Transmission - Manual, Auto
             
             Wheel (A Family Group) - It has families "Wheel-drive" and "Suspension".
             
             1. Wheel-drive - 2-Wheels, 4-Wheels
             
             2. Suspension - Full-Thrust, Full-Boom
             
             For the Engine partition object, the families, Engine & Transmission are "Available"
             and the families Wheel-drive & Suspension are "Not Available".
             
             The response of the operation for  the Engine partition object will have  the list
             of  Cfg0AbsAdmissibility objects for families Engine and Transmission, 1 for each
             and those will have admissibility state as "Available" and also the Cfg0AbsAdmissibility
             objects for the families Wheel-drive and Suspension, 1 for each and those will have
             admissibility state as "Not Available".
             

Teamcenter Component:

             Teamcenter Configurator - Teamcenter component for cfg0configurator template
             
        :param OperationConfigPerspective: 
                         The Cfg0ConfiguratorPerspective instance to specify the context and revision rule.
                         If configurator perspective is provided by each input structure in list admissibilityInputs,
                         then this operationConfigPerspective parameter can be NULL.
             
        :param AdmissibilityInputs: 
                         The list of target objects for which admissibility data should be returned.
             
        :return: 79010 - The operation expects one product item in the configuration perspective.
        """
        ...

