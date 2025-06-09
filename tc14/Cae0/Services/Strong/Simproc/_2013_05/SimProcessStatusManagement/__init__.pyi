import System
import Teamcenter.Soa.Client.Model
import typing

class SimProcessStatusManagement:
    """
    Interface SimProcessStatusManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSimProcessStatus(self, Attributes: list[str], Values: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The simulation tool launch feature in CAE Manager application supports a progress
             monitor dialog with persistent status management objects. These objects are maintained
             in the database for each simulation tool launch job initiated by a user.
             

             This operation supports creation of the CAE0SimProcessStatus object from the
             client side with necessary parameters and conditions. The cae0JobId
             attribute will be populated on the newly created object with a unique string with
             current time stamp appended to it. This operation will be used by the client whenever
             the user launches the simulation tool and selects to view the progress monitor for
             the launched tool.
             


Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param Attributes: 

        :param Values: 

        :return: 
        """
        ...
    def DeleteSimProcessStatus(self, JobIds: list[str]) -> bool:
        """    
             The simulation tool launch feature in CAE Manager application supports a progress
             monitor dialog with a persistent status management object which will be maintained
             in the database.
             

             This operation removes the corresponding CAE0SimProcessStatus objects from
             datatbase for the given job IDs.
             



Use Cases:

             The progress monitor will display status for all the jobs initiated by a user. However,
             once the job is finished, user may not need its status  tracked on progress monitor.
             Such jobs can be deleted from database using this operation Deleted job attributes
             will no longer apprear on the progress monitor after this operation is completed.
             



Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param JobIds: 

        :return: 
        """
        ...
    def GetSimProcessStatus(self, Attribute: str, Value: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The simulation tool launch feature in CAE Manager application supports a progress
             monitor dialog with a persistent status management object which is maintained in
             the database for each simulation tool launched by the user.
             

             This operation fetches  CAE0SimProcessStatus objects from database that match
             the attribute-value provided as input argument.
             

Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param Attribute: 

        :param Value: 

        :return: 
        """
        ...
    def UpdateSimProcessStatus(self, JobID: str, Attributes: list[str], Values: list[str]) -> bool:
        """    
             The simulation tool launch feature in CAE Manager application supports a progress
             monitor dialog with persistent status management object which are maintained in the
             database for every simulation tool launch job initiated by a user.
             

             The status object CAE0SimProcessStatus, which will be created during the launch
             of the simulation tool launch will need to be updated at different stages of tool
             launch. This operation updates the attributes such as status, last upload date, finish
             time and the last working directory of the CAE0SimProcessStatus object for
             a given simulation tool launch job.
             


Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param JobID: 
                         The unique job ID of the <b>CAE0SimProcessStatus</b> object to be updated.
             
        :param Attributes: 

        :param Values: 

        :return: False - if the attributes updated fails for the status object.
        """
        ...

