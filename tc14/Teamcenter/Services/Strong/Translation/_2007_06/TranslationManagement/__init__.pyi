import System
import Teamcenter.Soa.Client.Model
import typing

class CreateTranslationRequestArgs:
    """
    
The CreateTranslationRequestArgs struct is used to pass in multiple sets of data

to be used in a single call.  These structs are passed in the collection of

input arguments to the function createTranslationRequest.
    """
    def __init__(self, ) -> None: ...
    PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The primary objects for the request.  This usually refers to a dataset to translate
            but can be any component.
            """
    SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The secondary objects for the request.  This usually refers to the Item Revision
            containing the primary objects.
            """
    Priority: int
    """The priority to assign to the request."""
    ProviderName: str
    """The provider name to process the request."""
    TranslatorName: str
    """The translator from the above provider to translate the request."""
    Trigger: str
    """The trigger is a string that identifies who/where created this request."""
    TranslatorArgs: list[str]
    """
            The translator arguments to pass to the translator.  These are name value pairs like:
            NAME=FENDER.
            """

class CreateTranslationRequestResponse:
    """
    
The CreateTranslationRequestResponse struct contains the requests that were
created
as a result of the inputs specified in the CreateTranslationRequestArgs struct
above.
    """
    def __init__(self, ) -> None: ...
    RequestsCreated: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The Translation Request objects created."""
    SvcData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class TranslationManagement:
    """
    Interface TranslationManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateTranslationRequest(self, Inputs: list[CreateTranslationRequestArgs]) -> CreateTranslationRequestResponse:
        """    
             Create a translation request within Teamcenter for use with translation services.
             
             This operation creates a ETSTranslationRequest object in the Teamcenter database.    
             


Use Cases:

             The ETS application provides the ability to process requests in an asynchronous fashion
             thus removing the processing burden from the clients to a provisioned machine dedicated
             to processing these requests.
             

Teamcenter Component:

             Translation Services - A set of component (scheduler; translation modules; and translators)
             that provides distributed execution of translations across multiple machine. It has
             capability to schedule jobs to run at specified times in an asynchronous manner.
             
        :param Inputs: 
                         - List of input structures
             
        :return: It returns the successfully created request(s) back to the client or a NULLTAG if
             the creation was unsuccessful.
        """
        ...

