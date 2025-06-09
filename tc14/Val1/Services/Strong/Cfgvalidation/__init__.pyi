import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import Val1.Services.Strong.Cfgvalidation._2018_12.ConfigurableValidation

class ConfigurableValidationRestBindingStub(ConfigurableValidationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateValidationResults(self, CreateOrUpdateInputs: list[Val1.Services.Strong.Cfgvalidation._2018_12.ConfigurableValidation.CreateInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetValidationResults(self, ValAgentRevObjects: list[Teamcenter.Soa.Client.Model.Strong.ValidationAgentRevision], ValDataObjects: list[Teamcenter.Soa.Client.Model.Strong.ValDataRevision], ResultOwningObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class ConfigurableValidationService:
    """
    
            The Configurable Validation framework provides a frameowkr to let
users create a
            custom configurable validation application. The custom configurable
validaiton application
            will ensure a target meets compliance before it is released. Once
validation processes
            are configured, users can select a target in Teamcenter and confirm
its compliance
            with the business rules defined at a site.

            The Validation Manager administrator or the system administrator
must configure one
            or more validation agents and validation checkers. The Validation
Manager administrator
            or the system administrator may also need to modify the preferences
settings for
            Validation Manager.

            Configurable Validation services provides the following
functionalities for users
            to manipulate validation data.

            Create new validation agents.

            Create new validation checkers.

            Create new validation results.

            Create new result override requests for existing validation results.

            Update existing validation agents.

            Update existing validation checkers.

            Update existing validation results.

            Update existing result override requests for validation results.

            Delete validation results.

            Delete result override requests for validation results.

            Search for validation results with given search criteria.

            Execute validation business logic to check compliance of validation
targets and create
            or update validation results for the compliance checking activities.

Dependencies:

            DataManagement

Library Reference:

Val1SoacfgvalidationStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ConfigurableValidationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateValidationResults(self, CreateOrUpdateInputs: list[Val1.Services.Strong.Cfgvalidation._2018_12.ConfigurableValidation.CreateInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates and/or updates validation result objects with the given list
             of CreateInput data structures, and retrieves validation result objects after
             the create/update operations are completed. The values of the required properties
             (val0AgentRevName, val0CheckerClassName, Val0ValidationId,
             and val0TargetContext) in a CreateInput
             structure are used to identify a unique validation result object in the database.
             The values of the above properties are populated in each CreateInput structure
             of a validation result object and used by queries to find an existing validation
             result object. The value of val0TargetContext
             property is stored in the BOMap of a CreateInput structure. The property
             values for properties val0CheckerClassName, val0AgentRevName,
             and val0ValidationId  are stored in the StringMap
             of a  CreateInput structure. If no existing validation result object matches
             the given property values of val0TargetContext,
             val0CheckerClassName, val0AgentRevName, and val0ValidationId
             in the CreateInput structure, a new validation result object is created. If
             an existing validation result object is found, the existing validation result object
             is updated.
             

Teamcenter Component:

             Configurable Validation - Component for the template - val1cfgvalidation
             
        :param CreateOrUpdateInputs: 
                         A list of data structures that contain validation data for creating and/or updating
                         validation result objects.
             
        :return: 
        """
        ...
    def GetValidationResults(self, ValAgentRevObjects: list[Teamcenter.Soa.Client.Model.Strong.ValidationAgentRevision], ValDataObjects: list[Teamcenter.Soa.Client.Model.Strong.ValDataRevision], ResultOwningObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation retrieves configurable validation result objects that are found with
             the given input data. This operation will take the given configurable validation
             agents, validation data objects, and ItemRevision and/or Component business objects
             that logically owns validation results to build the search criteria to find the associated
             validation result objects. Configurable validation agents represent applications
             that were used to generate the configurable validation result objects. Validation
             data objects represent the specialized validation checks that are referenced by the
             configurable validation result objects.
             

Use Cases:

             A configurable validaiton result object is generated for a business object by a configurable
             validation agent using the specialized validation logic that is defined by a validation
             data object. This operation will be used to search for the configurable validation
             result objects that a user will be interested in by reducing the search scope using
             the given input objects.
             

Teamcenter Component:

             Configurable Validation - Component for the template - val1cfgvalidation
             
        :param ValAgentRevObjects: 
                         A list of ValidationAgentRevision objects.
             
        :param ValDataObjects: 
                         A list of ValDataRevision objects.
             
        :param ResultOwningObjects: 
                         A list of ItemRevision and/or Design Element business objects.
             
        :return: This operation returns the found ValidationResult business objects in the plain object
             list of the ServiceData structure.
        """
        ...

