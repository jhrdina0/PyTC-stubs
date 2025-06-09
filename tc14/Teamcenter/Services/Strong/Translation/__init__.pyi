import System
import Teamcenter.Services.Strong.Translation._2007_06.TranslationManagement
import Teamcenter.Soa.Client

class TranslationManagementRestBindingStub(TranslationManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateTranslationRequest(self, Inputs: list[Teamcenter.Services.Strong.Translation._2007_06.TranslationManagement.CreateTranslationRequestArgs]) -> Teamcenter.Services.Strong.Translation._2007_06.TranslationManagement.CreateTranslationRequestResponse: ...

class TranslationManagementService:
    """
    
            This service provides the method for creating ETSTranslationRequest
objects
            within Teamcenter.  These request objects are used with the ETS
application for performing
            translations in a distributed processing environment.

Library Reference:

TcSoaTranslationStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> TranslationManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateTranslationRequest(self, Inputs: list[Teamcenter.Services.Strong.Translation._2007_06.TranslationManagement.CreateTranslationRequestArgs]) -> Teamcenter.Services.Strong.Translation._2007_06.TranslationManagement.CreateTranslationRequestResponse:
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

