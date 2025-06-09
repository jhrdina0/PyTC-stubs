import System
import Teamcenter.Services.Strong.Ai._2006_03.Ai
import Teamcenter.Services.Strong.Ai._2008_06.Ai
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateAppInterfaceRecordInput:
    """
    
            CreateAppInterfaceRecordInput structure contains a AppInterface object and
            PLMXML labels for which corresponding RecordObjects are to be created and
            associated with the MasterRecord of the input AppInterface object.
            
    """
    def __init__(self, ) -> None: ...
    Ai: Teamcenter.Soa.Client.Model.Strong.AppInterface
    """
            The ApplicationInterface object whose MasterRecord is to be modified
            with the newly created RecordObjects based on the labels.
            """
    Labels: list[str]
    """A list of strings in the label format of PLMXML Application Reference element."""

class CreateAppInterfaceRecordOutput:
    """
    
            CreateAppInterfaceRecordOutput returns the PLMXML style labels for which the RecordObjects
            could not be created and the corresponding reason for failure.
            
    """
    def __init__(self, ) -> None: ...
    FailedLabels: list[str]
    """A list of labels for which  RecordObjects could not be created."""
    Reasons: list[str]
    """A list of strings each indicating the reason for failure."""

class CreateAppInterfaceRecordsResponse:
    """
    
            CreateAppInterfaceRecordsResponse structure contains a vector of CreateAppInterfaceRecordOutput,
            the size of which matches the input vector. It also includes the standard serviceData
            object.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateAppInterfaceRecordOutput]
    """A list of CreateAppInterfaceRecordOutput structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data capturing partial errors using the input array index as client id."""

class GetMappedAppRefsInput:
    """
    
            GetMappedAppRefsInput structure contains a Application Reference representing the
            object for which Application References of different Application name are needed,
            the Configuration to be used if Application Reference is of Teamcenter PSOccurrenceThread
            chain, and a list of Application names.
            
    """
    def __init__(self, ) -> None: ...
    Configuration: Teamcenter.Services.Strong.Ai._2008_06.Ai.Configuration
    """
            A optional element only used if the appRef is of "Teamcenter" application and is
            a PSOccurrenceThread chain. If not used, the useDefaultRevistionRule member
            should be set to false and existingWindow should be set to NULL.
            """
    AppRefs: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]
    """
            A list of 3-tuple each consisting of application name, label string and version string
            to represent the objects for which Application References are needed. For each Application
            Reference in the list, there will be appNames number of Application References.
            """
    AppNames: list[str]
    """
            A list of strings representing the names of Applications for which the "appRef" values
            are needed. Atleast one value must be provided. Valid value for Teamcenter is "Teamcenter".
            """

class GetMappedAppRefsResponse:
    """
    
            GetMappedAppRefsResponseElement returns the Application References for each input
            appref for each input appname. The vector is laid out sequencially - all the apprefs
            for each appName following each other.
            
    """
    def __init__(self, ) -> None: ...
    AppRefs: list[GetMappedAppRefsResponseElement]
    """A list of GetMappedRefsResponseElement structures."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data capturing partial errors using the input array index as client id."""

class GetMappedAppRefsResponseElement:
    """
    
            Element corresponding to each element in the input containing the details of the
            desired Application Reference. The layout of the vector corresponds to appRef values
            for each appName in sequence.
            
    """
    def __init__(self, ) -> None: ...
    AppRefs: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]
    """
            A list of Application Reference elements corresponding to the Application names specified
            in the input element.
            """

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateApplicationInterfaceRecords(self, Input: list[CreateAppInterfaceRecordInput]) -> CreateAppInterfaceRecordsResponse:
        """    
             This operation creates RecordObjects for the specified labels in the MasterRecord
             associated with the input AppInterface object. Input labels are PLMXML style
             label strings of ApplicationRef element related to Application type "Teamcenter".
             

Use Cases:

Use Case 1: Creating RecordObjects for specified PLMXML labels.

             This operation should be used to create RecordObjects for  Teamcenter Application
             References which were not exported via PLMXML. Typical case would be Light Weight
             BOM APIs are used to get the data, but, later there is a need to do a PLMXML import
             using AppInterface object.
             



Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param Input: 
                         The details of <b>AppInterface</b> and set of labels for which <b>RecordObjects</b>
                         are to be created
             
        :return: 
        """
        ...
    def GetMappedApplicationRefs(self, AppRefs: list[GetMappedAppRefsInput]) -> GetMappedAppRefsResponse:
        """    
             This operation searches for objects with specified Application References and returns
             the matching Application References with specified Application names. Application
             Reference is a 3-tuple construct with name, label and version strings. This is used
             in PLMXML exchange between Teamcenter and target applications to uniquely identity
             Teamcenter entities like Item, ItemRevision, Form objects etc.
             

Use Cases:

Use Case 1: Getting Teamcenter Application References for non Teamcenter Application
             References.
             
             This operation can be used to fetch the Application References of Teamcenter given
             non Teamcenter Application References. These are typically used in PLMXML interchange.
             
Use Case 2: Getting non Teamcenter Application References for Teamcenter Application
             References.
             
             This operation can be used to fetch the Application References of non Teamcenter
             Application References given Teamcenter Application References. These are typically
             used in PLMXML interchange.
             


Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AppRefs: 
                         The details of Application References for which correponding Application References
                         with different Application names are required.
             
        :return: 
        """
        ...

