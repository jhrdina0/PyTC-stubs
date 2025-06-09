import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CreateTestActivityInfo:
    """
    
This structure holds data to create a Tm0TestActivity.

    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """This unique ID is used to identify partial errors associated with this input structure."""
    TestInstance: Teamcenter.Soa.Client.Model.ModelObject
    """The Tm0TestInstance object."""
    ActivityInfoList: list[TestActivityInfo]
    """A list of activity input data that will be used to create test activities."""

class DeleteTestActivityInfo:
    """
    
This structure holds data to delete Tm0TestActivity objects.

    """
    def __init__(self, ) -> None: ...
    TestInstance: Teamcenter.Soa.Client.Model.ModelObject
    """The Tm0TestInstance object."""
    TestActivities: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of Tm0TestActivity objects to delete."""

class TestActivityInfo:
    """
    This structure holds data to create or modify the Tm0TestActivity information.
    """
    def __init__(self, ) -> None: ...
    ActivityId: str
    """The test activity id."""
    ActivityType: str
    """The test activity type. This comes from Test Execution Status LOV."""
    ActivityComment: str
    """
            The activity comment. If empty, the value from the Tm0TestTemplate of the
            Tm0TestInstance will be used.
            """
    ExecutionResultStatus: str
    """The execution result. This comes from the Test Result Status LOV."""
    ActivityDate: System.DateTime
    """
            The activity date. If empty, current date will be used.
            
"""
    TransientFileTickets: str
    """A list of file tickets for the activity's attachments."""

class EditTestActivityInfo:
    """
    
This structure holds data to modify the Tm0TestActivity object.

    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """This unique ID is used to identify partial errors associated with this input structure."""
    TestActivity: Teamcenter.Soa.Client.Model.ModelObject
    """The Tm0TestActivity to modify."""
    NewActivityInfo: TestActivityInfo
    """New data to update the activity with."""

class TestActivitySearchCriteria:
    """
    
This structure holds search criteria to search for Tm0TestActivity objects.

    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """This unique ID is used to identify partial errors associated with this input structure."""
    TestInstance: Teamcenter.Soa.Client.Model.ModelObject
    """The Tm0TestInstance object."""
    SearchScope: Teamcenter.Soa.Client.Model.ModelObject
    """The BOMLine to limit the search to."""
    CreatedBeforeDate: System.DateTime
    """The last date to filter Tm0TestActivity objects. If empty, this is ignored."""
    ActivityType: str
    """The activity type. If empty, this is ignored."""

class TestActivitySearchResponse:
    """
    
The response structure used by getTestActivities
service operation to return list of Tm0TestActivity objects satisfying the
given input criteria.
    """
    def __init__(self, ) -> None: ...
    SearchResults: list[TestActivitySearchResult]
    """The list of Tm0TestActivity objects that satisfy the input search crieteria."""
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Tm0TestActivity objects that satisfy the input search crieteria are added
            to the Plain objects' list.
            """

class TestActivitySearchResult:
    """
    
This structure stores a list of Tm0TestActivity objects along with the clientId
of the respective input structure. The
getTestActivities service operation uses
this structure to return a list of Tm0TestActivity objects that satisfy the
given input search criteria.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the TestActivitySearchCriteria.clientId.
            This can be used by the caller to identify this data structure with the source input
            data.
            """
    TestActivities: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of Tm0TestActivity objects that satisfy the input search criteria."""

class TestInstanceActivitiesResponse:
    """
    
The return structure used across service operations like create, edit or get
that
return a list of Tm0TestActivity objects that were created, modified or satisfy
the input search criteria.
    """
    def __init__(self, ) -> None: ...
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData structure."""
    TestInst2ActivsMap: System.Collections.Hashtable
    """
            A map (Tm0TestInstance/list of Tm0TestActivity objects) of Tm0TestInstance
            objects to list of Tm0TestActivity objects.
            """

class ActivityManagement:
    """
    Interface ActivityManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateTestActivities(self, Inputs: list[CreateTestActivityInfo]) -> TestInstanceActivitiesResponse:
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
    def DeleteTestActivities(self, Inputs: list[DeleteTestActivityInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
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
    def EditTestActivities(self, Inputs: list[EditTestActivityInfo]) -> TestInstanceActivitiesResponse:
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
    def GetTestActivities(self, Inputs: list[TestActivitySearchCriteria]) -> TestActivitySearchResponse:
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

