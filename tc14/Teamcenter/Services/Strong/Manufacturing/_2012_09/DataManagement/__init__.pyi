import Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement
import Teamcenter.Soa.Client.Model
import typing

class ApplyConfigInput:
    """
    
            Structure containing the configuration information and the context on which configuration
            needs to be applied.
            
    """
    def __init__(self, ) -> None: ...
    ConfigObj: Teamcenter.Soa.Client.Model.ModelObject
    """Object holding the configuration information that needs to be applied"""
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """The context to which the configuration needs to be applied."""

class CreateConfigInput:
    """
    Object containing input information for createOrUpdateConfigObjects action.
    """
    def __init__(self, ) -> None: ...
    Data: Teamcenter.Services.Strong.Manufacturing._2009_10.DataManagement.CreateInput
    """
            CreateInput structure used to capture the inputs required for creation of a business
            object.
            """
    ModifyObject: Teamcenter.Soa.Client.Model.ModelObject
    """Object to be modified."""
    BasedOn: Teamcenter.Soa.Client.Model.ModelObject
    """
            Top line of the BOMWindow object in case of StructureContext or ConfigurationContext,
            Null in case of CollaborationContext.
            """
    InternalConfigData: list[CreateConfigInput]
    """
            Internal related config objects. For a CC, this would be a vector of SCs. For an
            SC, this would be a Config Context. For ConfigContext, this would be null.
            """

class CreateConfigOutput:
    """
    Object containing information related to createOrUpdateConfigObjects action.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """Configuration object created or modified as per input."""
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """The context based on which configuration object is created."""
    InternalConfigData: list[CreateConfigOutput]
    """Data regarding created and updated internal nested configuration objects."""

class CreateConfigResponse:
    """
    Response for createOrUpdateConfigObjects action.
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateConfigOutput]
    """Object of CreateConfigOutput."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data including partial errors."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ApplyConfigObjects(self, Input: list[ApplyConfigInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Apply configuration objects to applicable business objects.
        :param Input: 
                         Input parameters for applying configuration objects
             
        :return: Service Data
        """
        ...
    def CreateOrUpdateConfigObjects(self, Input: list[CreateConfigInput]) -> CreateConfigResponse:
        """    Creates or updates the configuration objects based on the input data.
        :param Input: 
                         Vector of CreateConfigInput structure which contains the information for creating
                         or updating context objects.
             
        :return: Contains the created or updated object and the service data.
        """
        ...

