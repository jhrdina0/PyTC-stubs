import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateDispatcherRequestArgs:
    """
    
            The CreateDispatcherRequestArgs struct is used to pass in multiple sets of data to
            be used in a single call.  These structs are passed in the collection of input arguments
            to the function createDispatcherRequest.
            
    """
    def __init__(self, ) -> None: ...
    ProviderName: str
    """
            Name of the provider implementing this Service associated with this request. Example
            SIEMENS.
            """
    ServiceName: str
    """
            The service name which is the translator to process when this DispatcherRequest is
            executed.
            """
    PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The input primary objects that need to be translated. This usually refers to a dataset
            to translate but can be any component.
            """
    SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The input secondary objects for the request. This usually refers to the Item Revision
            containing the primary objects.
            """
    Priority: int
    """
            The priority to assign to the request. Supported priorities are 1 for low, 2 for
            medium and 3 for high.
            """
    StartTime: str
    """The start time to start the request. Date format is MM/dd/yyyy HH:mm"""
    EndTime: str
    """
            The end time at which repeating request should stop processing based on interval
            setting. Date format is MM/dd/yyyy HH:mm. If request is still processing, the request
            will be completed and will not be stopped.
            """
    Interval: int
    """
            Repeating request is executed from start time to end time with this interval specified
            in seconds.
            """
    KeyValueArgs: list[KeyValueArguments]
    """
            User specified key/value arguments for the request. These are translator specific
            arguments which are handled as inputs by the translators.
            """
    DataFiles: list[DataFiles]
    """
            User specified key/file pairs that can be attached to the Dispatcher Request. These
            are translator specific files which are used as inputs by the translators.
            """
    Type: str
    """
            The type of this request (USER SPECIFIED). Translators could use this option to support
            additional options for a given translator. Example "OnDemand" if created through
            UI and "OnSave" and translator could choose different options based on this type.
            """

class CreateDispatcherRequestResponse:
    """
    
            The CreateDispatcherRequestResponse struct contains the requests that were created
            as a result of the inputs specified in the CreateDispatcherRequestArgs structure
            above.
            
    """
    def __init__(self, ) -> None: ...
    RequestsCreated: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The Dispatcher Request objects created."""
    SvcData: Teamcenter.Soa.Client.Model.ServiceData
    """The SOA Service Data."""

class DataFiles:
    """
    
            This structure represents the user specified key/file pairs that can be attached
            to the Dispatcher Request. These are translator specific files which are used as
            inputs by the translators.
            
    """
    def __init__(self, ) -> None: ...
    Key: str
    """
            The key of the key/file pair. Example "CONFIG_FILE" could be a key to identify a
            configuration file.
            """
    File: Teamcenter.Soa.Client.Model.Strong.ImanFile
    """
            File which could be the input for translation. Example ImanFile which is the configuration
            file.
            """

class KeyValueArguments:
    """
    
            This structure represents the user specified key/value arguments that can be attached
            to the Dispatcher Request. These are translator specific arguments which are handled
            as inputs by the translators.
            
    """
    def __init__(self, ) -> None: ...
    Key: str
    """
            The key of the key/value pair. Example File ticket can be passed as input to translator.
            In this case, key could be "FILE_TICKET"
            """
    Value: str
    """
            The value of the key/value pair. Example value can be FMS File ticket. This value
            can be used to download a file for translation.
            """

class DispatcherManagement:
    """
    Interface DispatcherManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateDispatcherRequest(self, Inputs: list[CreateDispatcherRequestArgs]) -> CreateDispatcherRequestResponse:
        """    
             Create a DispatcherRequest within Teamcenter for use with Dispatcher Management
             Services.
             

Use Cases:

             The Dispatcher Management application provides the ability to process requests in
             an asynchronous fashion thus removing the processing burden from the clients to provisioned
             machine dedicated to processing these requests.  There are quite a few services,
             within Teamcenter and other applications that use this application.
             

             Here are a few examples:
             

Asynchronous Processing (if configured)
             
NXtoPVDirect (provided with NX)
             
PreviewService
             



Teamcenter Component:

             Dispatcher - A set of component (scheduler; translation modules; and translators)
             that provides distributed execution of translations across multiple machine. It has
             capability to schedule jobs to run at specified times in an asynchronous manner.
             
        :param Inputs: 
                         holds the values needed to create the <b>DispatcherRequest</b>.
             
        :return: (s) back to the client
             or a NULLTAG if the creation was unsuccessful.
        """
        ...

