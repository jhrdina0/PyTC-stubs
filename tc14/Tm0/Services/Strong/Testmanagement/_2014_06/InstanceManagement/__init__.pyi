import System
import Teamcenter.Soa.Client.Model
import typing

class EditTestInstanceInfo:
    """
    
This structure provides information to modify a Tm0TestInstance object. It
is used by callers in the edit service operation to supply updated data.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """This unique ID is used to identify partial errors associated with this input structure."""
    TestInstance: Teamcenter.Soa.Client.Model.ModelObject
    """The Tm0TestInstance to modify."""
    TestName: str
    """The new name of the test."""
    TestType: str
    """The new test type. This comes from the Test Type LOV."""
    ExecutionSystem: str
    """The execution system. This comes from Execution System LOV."""
    ExecutionScope: str
    """
            The execution scope, typically the value of the BOMLine property bl_clone_stable_occurrence_id.
            """
    TestSteps: list[TestStepInfo]
    """The new list of steps."""
    OwningObject: Teamcenter.Soa.Client.Model.ModelObject
    """The ItemRevision that owns the Tm0TestInstance object."""

class TestInstanceInfo:
    """
    
This structure provides  information to create a new Tm0TestInstance object.
It is used by callers in the create service operation to supply input data.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """This unique ID is used to identify partial errors associated with this input structure"""
    TestName: str
    """The name of the Test"""
    TestType: str
    """The Test type. This comes from the Test Type LOV"""
    ExecutionSystem: str
    """The execution system. This comes from Execution System LOV"""
    ExecutionScope: str
    """
            The execution scope, typically the value of the BOMLine property bl_clone_stable_occurrence_id
"""
    TestSteps: list[TestStepInfo]
    """A list of steps for this test"""
    OwningObject: Teamcenter.Soa.Client.Model.ModelObject
    """The ItemRevision that owns the test instance"""

class TestInstanceSearchCriteria:
    """
    
This structure provides information to search for Tm0TestInstance objects.
It is used by callers in the get service operation to supply input search
criteria.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """This unique ID is used to identify partial errors associated with this input structure."""
    TestName: str
    """The name of the test to search for."""
    TestType: str
    """The test type to search for. If empty, this is ignored."""
    ExecutionSystem: str
    """The execution system that the test was run on. If empty, this is ignored."""
    ExecutionScope: str
    """The execution scope to search for. If empty, this is ignored."""
    TestTemplate: Teamcenter.Soa.Client.Model.ModelObject
    """The Tm0TestTemplate object."""
    SearchScope: Teamcenter.Soa.Client.Model.ModelObject
    """The BOMLine to limit the search to."""
    ReferredObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of BOMLine objects used as placemarks in any of the test's steps.
            
"""

class TestInstanceSearchResponse:
    """
    
The response structure used by getTestInstances
service operation to return list of Tm0TestInstance objects satisfying the
given input criteria.
    """
    def __init__(self, ) -> None: ...
    SearchResults: list[TestInstanceSearchResult]
    """The list of Tm0TestInstance objects that satisfy the input search crieteria."""
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The Tm0TestInstance objects that satisfy the input search crieteria are added
            to the Plain objects' list.
            """

class TestInstanceSearchResult:
    """
    
This structure stores a list of Tm0TestInstance objects along with the clientId
of the respective input structure. The
getTestInstances service operation uses this
structure to return a list of Tm0TestInstance objects that satisfy the given
input search criteria.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the TestInstanceSearchCriteria.clientId. This can be used
            by the caller to identify this data structure with the source input data.
            """
    TestInstances: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of Tm0TestInstance objects that satisfy the input search criteria."""

class TestInstancesResponse:
    """
    
The return structure used across service operations like create, edit or search
that
return a list of Tm0TestInstance objects that were created, modified or satisfy
the input search criteria.

    """
    def __init__(self, ) -> None: ...
    SrvcData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data structure"""
    TestInstances: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The list of Tm0TestInstance objects"""

class TestInstanceTemplateInfo:
    """
    
This structure provides information to create a new Tm0TestInstance object
from a given Tm0TestTemplateRevision object. It is used by callers in the
create service operation to supply input data.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """This unique ID is used to identify partial errors associated with this input structure"""
    TestName: str
    """The name of the test"""
    TestType: str
    """
            The Test type. This comes from the Test Type LOV. If empty, the value from Tm0TestTemplate
            is used
            """
    ExecutionSystem: str
    """
            The execution system. This comes from Execution System LOV. If empty, the value from
            Tm0TestTemplate is used
            """
    ExecutionScope: str
    """
            The execution scope, typically the value of the BOMLine property bl_clone_stable_occurrence_id
"""
    TestPlacemarks: list[str]
    """
            A list of values that will replace the placeholder(s) in the description. Typically,
            this would be a list of bl_clone_stable_occurrence_id
            values of the BOMLine objects
            """
    TestTemplate: Teamcenter.Soa.Client.Model.ModelObject
    """The Tm0TestTemplateRevision to be used as the template"""
    OwningObject: Teamcenter.Soa.Client.Model.ModelObject
    """The ItemRevision that owns the Tm0TestInstance object"""

class TestStepInfo:
    """
    
This structure holds the information of one step of a Tm0TestInstance.

This is used by callers in create and edit service operations to provide new or
updated
step information.
    """
    def __init__(self, ) -> None: ...
    StepDesc: str
    """The step's description containing placeholders"""
    AllowedTypes: str
    """
            The comma-separated BOMLine typenames that are allowed to fill the placeholders.
            For example, string Mfg0BvrPart indicating that Mfg0BvrPart objects
            are allowed.
            
"""
    MultipleObjects: bool
    """TRUE if multiple objects are allowed"""
    TestPlacemarks: list[str]
    """
            A list of values that will replace the placeholder(s) in the description. Typically,
            this would be a list of bl_clone_stable_occurrence_id
            values of the BOMLine objects
            """

class InstanceManagement:
    """
    Interface InstanceManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateTestInstances(self, Inputs: list[TestInstanceInfo]) -> TestInstancesResponse:
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
    def CreateTestInstancesFromTemplate(self, Inputs: list[TestInstanceTemplateInfo]) -> TestInstancesResponse:
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
    def EditTestInstances(self, Inputs: list[EditTestInstanceInfo]) -> TestInstancesResponse:
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
    def GetTestInstances(self, Inputs: list[TestInstanceSearchCriteria]) -> TestInstanceSearchResponse:
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

