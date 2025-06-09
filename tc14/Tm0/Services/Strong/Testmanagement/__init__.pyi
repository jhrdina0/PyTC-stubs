import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement
import Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement

class ActivityManagementRestBindingStub(ActivityManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateTestActivities(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.CreateTestActivityInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.TestInstanceActivitiesResponse: ...
    def DeleteTestActivities(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.DeleteTestActivityInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def EditTestActivities(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.EditTestActivityInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.TestInstanceActivitiesResponse: ...
    def GetTestActivities(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.TestActivitySearchCriteria]) -> Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.TestActivitySearchResponse: ...

class ActivityManagementService:
    """
    
            This service contains service operations that help manage Test
Activities.

Library Reference:

Tm0SoaTestManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ActivityManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateTestActivities(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.CreateTestActivityInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.TestInstanceActivitiesResponse:
        """    
             This operation creates Tm0TestActivity objects from the given inputs.
             
             For each TestActivityInfo in the CreateTestActivityInfo.activityInfoList parameter, a new Tm0TestActivity
             object is created and the values of parameters activityId,
             activityType, activityComment,
             activityDate, executionResultStatus
             are set in the respective attributes.
             
             A new Tm0TestResults dataset is created and for each file ticket in the transientFileTickets parameter, the file is imported
             under
             

Tm0image named reference
             if the file is a JPEG image
             
Tm0general_attachment named
             reference for all other file types
             


             A new relationship is created between the new Tm0TestActivity object and the
             new Tm0TestResults dataset.
             

Teamcenter Component:

             Test Management - This application model is used to manage the Assembly Tests that
             are done during the Virtual Assessment process in Automotive and Aerospace&Defence.
             
        :param Inputs: 
                         A list of <b>Tm0TestInstance</b> objects and input data to create test activities.
             
        :return: 
        """
        ...
    def DeleteTestActivities(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.DeleteTestActivityInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes Tm0TestActivity objects from the given Tm0TestInstance
             objects.
             
             For each Tm0TestActivity in the DeleteTestActivityInfo.testActivities
             parameter:
             

All named references in the Tm0TestResults dataset connected
             to the Tm0TestActivity are deleted.
             
The relationship between the Tm0TestActivity and Tm0TestResults
             dataset is deleted and then the dataset itself is deleted.
             
The relationship between the Tm0TestInstance object represented
             by the DeleteTestActivityInfo.testInstance
             parameter and the Tm0TestActivity object is deleted.
             
Finally, the Tm0TestActivity object is deleted.
             



Teamcenter Component:

             Test Management - This application model is used to manage the Assembly Tests that
             are done during the Virtual Assessment process in Automotive and Aerospace&Defence.
             
        :param Inputs: 
                         A list of <b>Tm0TestInstance</b> objects and <b>Tm0TestActivity</b> objects to delete.
             
        :return: 
        """
        ...
    def EditTestActivities(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.EditTestActivityInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.TestInstanceActivitiesResponse:
        """    
             This operation modifies Tm0TestActivity objects with the new input values.
             
             The values of parameters activityId, activityType, activityComment,
             activityDate, executionResultStatus
             from the EditTestActivityInfo.newActivityInfo
             input structure are set in the respective attributes of the Tm0TestActivity
             object represented by the EditTestActivityInfo.testActivity
             parameter.
             
             The Tm0TestResults dataset linked to the Tm0TestActivity object is
             updated by deleting all existing named references. For each file ticket in the transientFileTickets parameter, the file is imported
             under
             

Tm0image named reference
             if the file is a JPEG image
             
Tm0general_attachment named
             reference for all other file types.
             



Teamcenter Component:

             Test Management - This application model is used to manage the Assembly Tests that
             are done during the Virtual Assessment process in Automotive and Aerospace&Defence.
             
        :param Inputs: 
                         A list of <b>Tm0TestActivity</b> objects and new data.
             
        :return: 
        """
        ...
    def GetTestActivities(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.TestActivitySearchCriteria]) -> Tm0.Services.Strong.Testmanagement._2014_06.ActivityManagement.TestActivitySearchResponse:
        """    
             This operation searches for Tm0TestActivity objects with the given search
             criteria.
             
             One of the two parameters - testInstance
             or searchScope should be provided failing
             which a partial error will be returned for that input TestActivitySearchCriteria
             structure.
             
             The activityType parameter value (when non-empty)
             is matched exactly against the respective attribute in the Tm0TestActivity
             object.
             
             The createdBeforeDate parameter value (when
             non-empty) should be greater than or equal to the Tm0TestActivity object's
             activityDate attribute value.
             

Teamcenter Component:

             Test Management - This application model is used to manage the Assembly Tests that
             are done during the Virtual Assessment process in Automotive and Aerospace&Defence.
             
        :param Inputs: 
                         A list of input search criteria to search for <b>Tm0TestActivity</b> objects.
             
        :return: 
        """
        ...

class InstanceManagementRestBindingStub(InstanceManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateTestInstances(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstanceInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstancesResponse: ...
    def CreateTestInstancesFromTemplate(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstanceTemplateInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstancesResponse: ...
    def DeleteTestInstances(self, Inputs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def EditTestInstances(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.EditTestInstanceInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstancesResponse: ...
    def GetTestInstances(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstanceSearchCriteria]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstanceSearchResponse: ...

class InstanceManagementService:
    """
    
            The Instance Management service interface provides operations to
create, edit, delete
            and search for Tm0TestInstance objects.

            A Tm0TestInstance represents a validation such as Tool Reachability,
Assembly
            Simulation or Collision Check defined on a station with a list of
steps describing
            the validation process.

Library Reference:

Tm0SoaTestManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> InstanceManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateTestInstances(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstanceInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstancesResponse:
        """    
             This operation creates Tm0TestInstance objects from the given inputs.
             
             For each TestInstanceInfo input structure,
             a new Tm0TestInstance is created and the values of parameters testName, testType, executionSystem and executionScope
             are set on the respective attributes. A new relationship is created between the ItemRevision
             represented by owningObject parameter to
             this new Tm0TestInstance object.
             
             For each TestStepInfo structure represented
             by testSteps parameter, a new Tm0TestInstDescStep
             is created and the values of parameters stepDesc,
             allowedTypes, multipleObjects
             and testPlacemarks are set on the respective
             attributes. A new relationship is created between the new Tm0TestInstance
             object and the new Tm0TestInstDescStep object.
             

Teamcenter Component:

             Test Management - This application model is used to manage the Assembly Tests that
             are done during the Virtual Assessment process in Automotive and Aerospace&Defence.
             
        :param Inputs: 
                         A list of input data to create <b>Tm0TestInstance</b> objects
             
        :return: 
        """
        ...
    def CreateTestInstancesFromTemplate(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstanceTemplateInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstancesResponse:
        """    
             This operation creates Tm0Testinstance objects from the given inputs.
             
             For each TestInstanceTemplateInfo input structure,
             a new Tm0TestInstance is created and the values of parameters testName, testType, executionSystem and executionScope
             are set on the respective attributes. If the parameter testType
             or executionSystem is empty, the corresponding
             attribute value of the Tm0TestTemplateRevision object represented by the testTemplate parameter is used.
             
             A new relationship is created between the ItemRevision represented by owningObject parameter to the new Tm0TestInstance
             object.
             
             The Tm0TestTemplateRevision object represented by the testTemplate parameter contains references to one or more Tm0TestTempDescStep
             objects. For each such reference, a new Tm0TestInstDescStep is created and
             the value of TestInstanceTemplateInfo.testPlacemarks
             parameter is set in the respective attribute. A new relationship is created between
             the new Tm0TestInstance object and the new Tm0TestInstDescStep object.
             

Teamcenter Component:

             Test Management - This application model is used to manage the Assembly Tests that
             are done during the Virtual Assessment process in Automotive and Aerospace&Defence.
             
        :param Inputs: 
                         A list of input data to create <b>Tm0TestInstance</b> objects.
             
        :return: 
        """
        ...
    def DeleteTestInstances(self, Inputs: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the Tm0TestInstance objects.
             
             For each Tm0TestInstance input:-
             

The relationship between the Tm0TestInstance object and the
             Tm0TestTemplate object is deleted, if it exists.
             
The relationship between the ItemRevision object and the Tm0TestInstance
             object is deleted.
             
The Tm0TestInstance object contains references to one or more
             Tm0TestInstDescStep objects. For each such reference, the relationship is
             deleted along with the Tm0TestInstDescStep object itself.
             
Finally, the Tm0TestInstance object is deleted.
             



Teamcenter Component:

             Test Management - This application model is used to manage the Assembly Tests that
             are done during the Virtual Assessment process in Automotive and Aerospace&Defence.
             
        :param Inputs: 
                         A list of <b>Tm0TestInstance</b> objects to delete.
             
        :return: 
        """
        ...
    def EditTestInstances(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.EditTestInstanceInfo]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstancesResponse:
        """    
             This operation modifies the Tm0TestInstance objects with the new input data.
             
             For each EditTestInstanceInfo input structure,
             the values of parameters testName, testType, executionSystem
             and executionScope are set to the respective
             attributes in the Tm0TestInstance object represented by the testInstance parameter.
             
             If the testSteps parameter is not empty:-
             

if the Tm0TestInstance object has a relation to a Tm0TestTemplate
             object, the relationship is deleted.
             
The relationships between the Tm0TestInstance object and Tm0TestInstDescStep
             objects are also deleted along with the Tm0TestInstDescStep objects themselves.
             
For each TestStepInfo structure,
             a new Tm0TestInstDescStep object is created and the values of parameters stepDesc, allowedTypes,
             multipleObjects and testPlacemarks are set on the respective attributes. A new relationship
             is created between the Tm0TestInstance object and the new Tm0TestInstDescStep
             object.
             


             If the owningObject parameter is not empty,
             a new relationship is created between the ItemRevision object represented
             by that parameter and the Tm0TestInstance object. If such a relationship already
             exists, it is deleted before creating the new one.
             

Teamcenter Component:

             Test Management - This application model is used to manage the Assembly Tests that
             are done during the Virtual Assessment process in Automotive and Aerospace&Defence.
             
        :param Inputs: 
                         A list of input data to modify the <b>Tm0TestInstance</b> objects.
             
        :return: 
        """
        ...
    def GetTestInstances(self, Inputs: list[Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstanceSearchCriteria]) -> Tm0.Services.Strong.Testmanagement._2014_06.InstanceManagement.TestInstanceSearchResponse:
        """    
             This operation searches for Tm0TestInstance objects with the given search
             criteria.
             
             One of the three parameters - testName, testTemplate or searchScope
             should be provided failing which a partial error will be returned for that input
             TestInstanceSearchCriteria structure.
             
             If a Tm0TestInstance object's tm0test_name
             attribute contains the value provided in the testName
             parameter, it is considered a valid search result candidate and further checks are
             made. On the other hand, the testType, executionSystem and executionScope
             parameter values (when non-empty) are matched exactly against the respective attributes
             in the Tm0TestInstance object.
             

Teamcenter Component:

             Test Management - This application model is used to manage the Assembly Tests that
             are done during the Virtual Assessment process in Automotive and Aerospace&Defence.
             
        :param Inputs: 
                         A list of input data to search for <b>Tm0TestInstance</b> objects.
             
        :return: 
        """
        ...

