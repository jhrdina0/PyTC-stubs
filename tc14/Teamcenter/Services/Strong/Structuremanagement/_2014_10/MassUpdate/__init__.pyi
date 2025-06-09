import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ChildScope:
    """
    
This is a structure containing information about a child node and a boolean flag
indicating whether this child node has to be included recursively in the search
scope
of impacted objects.
    """
    def __init__(self, ) -> None: ...
    Child: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Child node to be included in the impacted object search scope."""
    Recurse: bool
    """
            Indicates whether the child nodes are to be included recursively for the impacted
            object search scope.
            """

class ExecuteMarkupChangeInput:
    """
    
Input structure containing information about Change Item revision and it's
Fnd0MarkupChange
object UIDs to be executed.
    """
    def __init__(self, ) -> None: ...
    ChangeItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
ChangeItemRevision whose associated Fnd0MarkupChange objects are to
            be executed.
            """
    MarkupChangeUIDs: list[str]
    """List of Fnd0MarkupChange object UIDs associated with ChangeItemRevision"""

class ExecuteMarkupChangeOutput:
    """
    
This is a structure containing information about an update status and the list
of
updated Fnd0MarkupChange objects per input ChangeItemRevision.
    """
    def __init__(self, ) -> None: ...
    ChangeItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ChangeItemRevision whose associated Fnd0MarkupChange objects are executed"""
    MarkupChangeObjs: list[Teamcenter.Soa.Client.Model.Strong.Fnd0MarkupChange]
    """A list of Fnd0MarkupChange objects that are executed"""
    IsUpdateSuccessful: bool
    """
            This flag is set to true only if all the input Fnd0MarkupChange objects executes
            succesfully.
            """

class ExecuteMarkupChangeResponse:
    """
    
This is a response structure containing update status information about
Fnd0MarkupChange
objects per input ChangeItemRevision and standard service data for partial
errors.
    """
    def __init__(self, ) -> None: ...
    Output: list[ExecuteMarkupChangeOutput]
    """
            List of structure containing update status and updated Fnd0MarkupChange objects
            per input ChangeItemRevision.
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data for partial errors."""

class ExpandOneLevelSearchScopeInput:
    """
    
This operation expands the given parent product structure node to fetch its
immediate
children. A call to this operation is made when defining a search scope for
impacted
object search.
    """
    def __init__(self, ) -> None: ...
    Operation: int
    """
            Type of mass update operation being performed.
            
            Following are the valid values:
            
            129 - Replace Realization Source
            
"""
    ParentNode: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Node in a product structure to be expanded."""
    Type: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Type of child node"""
    RevRule: str
    """Revision rule using which the expanded structure is to be configured with."""

class ExpandOneLevelSearchScopeOutput:
    """
    
This is an output structure containing information about child nodes for a given
parent node
    """
    def __init__(self, ) -> None: ...
    ParentNode: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Parent node of a product structure for which list of child nodes are requested."""
    ChildNodes: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """List of child nodes for a given input parent node."""

class ExpandOneLevelSearchScopeResponse:
    """
    
This is a structure containing information about child nodes for a given input
parent
node and partial errors occured during an operation.
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandOneLevelSearchScopeOutput]
    """
            List of structure containing information about list of child nodes for a given input
            parent node of a product structure.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data to handle partial errors."""

class GetMarkupChangesForUpdateOutput:
    """
    
Structure containing information about Fnd0MarkupChange objects per input
ChangeItemRevision.
    """
    def __init__(self, ) -> None: ...
    ChangeItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
ChangeItemRevision whose markup changes are to be executed for mass update
            operation.
            """
    MarkupChangeUIDs: list[str]
    """
            List of unprocessed and/or previously failed Fnd0MarkupChange UIDs referenced
            by Fnd0Markup object associated with changeItemRev
            """

class GetMarkupChangesForUpdateResponse:
    """
    
Response structure containing information about Fnd0MarkupChange objects per
input ChangeItemRevision and standard service data for partial errors.

    """
    def __init__(self, ) -> None: ...
    Output: list[GetMarkupChangesForUpdateOutput]
    """
            List of structure containing information about Fnd0MarkupChange objects per
            input ChangeItemRevision.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data for partial errors."""

class GetRevisionRulesResponse:
    """
    
This operation returns the list of valid revision rules applicable for specific
mass
update operation type.
    """
    def __init__(self, ) -> None: ...
    RevRuleNames: list[str]
    """List of valid revision rules applicable for mass update operation type."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data for partial errors."""

class ImpactedObjectDetailsInput:
    """
    This is a structure containing information required to get mass update specific
details
    """
    def __init__(self, ) -> None: ...
    Operation: int
    """
            Mass update operation type being performed.
            
            Following are the valid values:
            
            129 - Replace Realization Source
            
"""
    ImpactedObjectUIDs: list[str]
    """
            This is a list of impacted object UIDs for which mass update specific details are
            required.
            """
    ProcessedImpactedUIDs: list[str]
    """
            This is an optional list of impacted object UIDs for which mass update specific details
            were already fetched previously. Objects corresponding to these UIDs will be unloaded
            from the server since they are no longer needed.
            """
    Change: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Change ItemRevision to record mass update results."""

class ImpactedObjectDetailsOutput:
    """
    
This is a structure containing information like whether the impacted object is
selectable
for performing an update, if not selectable then the reason for it being non-
selectable,
whether the impacted object is out of date etc.
    """
    def __init__(self, ) -> None: ...
    ImpactedObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """This is an impacted object in respect of which mass update specific details are fetched."""
    IsSelectable: bool
    """Indicates whether the impacted object is selectable for update."""
    IsOutOfDate: bool
    """Indicates whether the impacted object is out of date"""
    NonSelectableReason: str
    """
            This text informs why the impacted object is not selectable. For selectable impacted
            objects, this text is empty.
            """

class ImpactedObjectDetailsResponse:
    """
    
This is a structure containing mass update specific impacted object information
and
service data to hold partial errors.
    """
    def __init__(self, ) -> None: ...
    Output: list[ImpactedObjectDetailsOutput]
    """List of structure containing mass update specific impacted object information."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data to handle partial errors"""

class SearchScope:
    """
    
This is a structure containing information about search scope for searching
impacted
objects.
    """
    def __init__(self, ) -> None: ...
    ProductScope: list[ProductScope]
    """
            List of structure containing product scope information for searching the impacted
            objects.
            """
    PropNames: list[str]
    """List of impacted object property names based on which the impacted objects are filtered."""
    PropValues: list[str]
    """List of impacted object property values based on which the impacted objects are filtered."""
    DefaultRevRule: str
    """Default Revision rule to be applied on resultant impacted objects."""

class ImpactedObjectsQueryInput:
    """
    
This is a structure containing information about inputs required to query
impacted
objects.
    """
    def __init__(self, ) -> None: ...
    Operation: int
    """
            Mass update operation type being performed. This is used to identify type of filtering
            to use when searching for impacted objects.
            
            Following are the valid values:
            
            129 - Replace Realization Source
            
"""
    Target: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Target ItemRevision whose impacted objects are to be searched."""
    Change: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Change ItemRevision to record mass update results."""
    SearchScope: SearchScope
    """
            Search scope for searching the impacted objects. If no search scope is provided,
            impacted object search is performed in all available product structures.
            """

class ImpactedObjectsQueryOutput:
    """
    
This is an output structure containing information about list of impacted UIDs
per
input target ItemRevision.
    """
    def __init__(self, ) -> None: ...
    Target: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
            Target ItemRevision whose impacted objects are queried for performing mass update
            operation.
            """
    ImpactedObjectUIDs: list[str]
    """List of all impacted object UIDs for a given target ItemRevision."""

class ImpactedObjectsQueryResponse:
    """
    
This is a structure containing information about impacted object UIDs per target
ItemRevision and service data for partial errors.
    """
    def __init__(self, ) -> None: ...
    Output: list[ImpactedObjectsQueryOutput]
    """List of structure containing impacted object UIDs information."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data to handle partial errors."""

class ImpactedObjectStatusOutput:
    """
    
This is a structure containing information about impacted object Save/Remove
operation
status and the text information describing the reason for the failure if any.
    """
    def __init__(self, ) -> None: ...
    ImpactedObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """This is an impacted object added to or removed from change ItemRevision"""
    Status: bool
    """Success/failure status for Save/Remove operation"""
    StatusComment: str
    """
            This text informs why the operation on impacted object has failed. If the operation
            is successful then this text is empty.
            """

class ManageImpactedObjectUpdateInput:
    """
    
This is a structure containing information data required to manage impacted
objects
using markup
    """
    def __init__(self, ) -> None: ...
    Operation: int
    """
            Mass update operation type being executed
            
            Following are the valid values:
            
            129 - Replace Realization Source
            
"""
    ExecutionMode: str
    """
            This defines the change ItemRevision specific mass update operation being performed.
            Following are the valid values
            
            murAddImpactedObjectToMarkup
            
            murRemoveImpactedObjectFromMarkup
            """
    Target: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Target ItemRevision whose impacted objects are to be searched for mass update"""
    Replacement: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The new replacement ItemRevision"""
    Change: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The change ItemRevision object to record mass update results in"""
    AddToProblem: bool
    """Whether to add the target ItemRevision to the problem folder"""
    AddToSolution: bool
    """
            Whether to add the target ItemRevision to solution folder
            
"""
    MarkupChange: Teamcenter.Soa.Client.Model.Strong.Fnd0MarkupChange
    """
            The markup change correponding to an impacted object to be removed from the markup
            object and the impacted folder of change ItemRevision object
            """
    ImpactedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """A list of impacted objects that needs to be managed on change ItemRevision"""

class ManageImpactedObjectUpdatesResponse:
    """
    
This is a structure containing status information about impacted object manage
update
operations.
    """
    def __init__(self, ) -> None: ...
    Output: list[ImpactedObjectStatusOutput]
    """
            List of structure containing information about impacted object Save/Remove operation
            status
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data for partial errors"""

class ProductScope:
    """
    This is a structure containing information about product level search scope.
    """
    def __init__(self, ) -> None: ...
    Product: Teamcenter.Soa.Client.Model.Strong.POM_object
    """Top level product node to be included in the impacted object search scope."""
    ChildScope: list[ChildScope]
    """List of structure containing child scope information for searching the impacted objects."""
    RevRule: str
    """Revision rule to configure the impacted object search result."""

class UpdateImpactedObjectEndResponse:
    """
    
Contains information about whether the cleanup activity is performed
successfully
or not.
    """
    def __init__(self, ) -> None: ...
    IsCleanupSuccessful: list[bool]
    """
            A list of flags indicating whether the cleanup activity is performed succesfully
            for each input.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data for partial errors."""

class UpdateImpactedObjectInput:
    """
    
This is a structure containing information required to update impacted object
for
mass update operation.
    """
    def __init__(self, ) -> None: ...
    Operation: int
    """
            Mass update operation type being executed.
            
            Following are the valid values:
            
            129 - Replace Realization Source
            
"""
    Target: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Target ItemRevision whose impacted objects are to be searched for mass update"""
    Replacement: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The new replacement ItemRevision"""
    Change: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """The change ItemRevision object to record mass update results in"""
    AddToProblem: bool
    """Add the target ItemRevision to the problem folder"""
    AddToSolution: bool
    """Add the replacement ItemRevision to solution folder"""
    ImpactedObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """A list of impacted objects to be updated"""
    IsSelected: list[bool]
    """
            A list of boolean values that indicates whether the impacted objects are selected
            for mass update operation
            """

class UpdateImpactedObjectResponse:
    """
    
This is a structure containing information about impacted object update status
for
every object selected for mass update operation. It also contains partial error
information
in ServiceData.
    """
    def __init__(self, ) -> None: ...
    Output: list[ImpactedObjectStatusOutput]
    """List of structure containing information about impacted object update operation status."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data for partial errors."""
    UpdateRequestId: str
    """
            Unique Identifier per update request initiated from the 'Mass Update Realization'
            wizard. If the update is being performed in batches then this Identifier is same
            for all the batches.
            """

class UpdateImpactedObjectStartResponse:
    """
    
Response structure containing update request identifier and standard service
data
for partial errors.

    """
    def __init__(self, ) -> None: ...
    UpdateRequestId: str
    """
            Unique Update Request Identifier per update request initiated by user while performing
            'Mass Update Realization'. If the update is being performed in batches then this
            Identifier is same for all the batches.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard service data for partial errors.
            

            Note: Member 'serviceData' available as part of this structure is not being used
            presently. This member has been added to this structure for Future use case.
            """

class ValidateChangeObjectForMassUpdateOutput:
    """
    
This is a structure containing information whether the input ChangeItemRevision
is valid for Mass Update type.
    """
    def __init__(self, ) -> None: ...
    ChangeItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Input ChangeItemRevision."""
    IsValid: bool
    """
            This flag is set to true if the corresponding input Change Item revision is valid
            for Mass Update type.
            
            -If API is called with input massUpdateType="massUpdate", this flag is set to false
            if Fnd0MarkupChange object associated with input ChangeItemRevision
            is found with mass update operation value = 129
            
            -If API is called with input massUpdateType="massUpdateRealization", this flag is
            set to false if Fnd0MarkupChange object associated with input ChangeItemRevision
            is found with mass update operation value != 129
            
"""

class ValidateChangeObjectForMassUpdateResponse:
    """
    
This is a structure that contains the information whether the input
ChangeItemRevision
is valid for Mass Update type. It also holds the standard service data for
partial
errors.
    """
    def __init__(self, ) -> None: ...
    Output: list[ValidateChangeObjectForMassUpdateOutput]
    """
            List of structure containing information whether the input ChangeItemRevision
            is valid for Mass Update operation.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data for partial errors."""

class MassUpdate:
    """
    Interface MassUpdate
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteMarkupChanges(self, Input: list[ExecuteMarkupChangeInput]) -> ExecuteMarkupChangeResponse:
        """    
             This operation executes the markup change objects corresponding to input Fnd0MarkupChange
             object UID list. Each markup change object holds the information like object to be
             modified, the input required for object modification and type of modification. When
             markup change object is executed, it modifies the required object with the help of
             information available on markup change object.
             

Use Cases:

             Execute markup changes associated with ChangeItemRevision


Invoke MassUpdate service operation getImpactedObjects by providing
             target ItemRevision. This API returns the list of impacted object UIDs.
             
Invoke MassUpdate service operation getImpactedObjectDetails by supplying
             the batch of impacted object UIDs. This API returns the information specifying whether
             each of the input impacted objects is modifiable or not.
             
Invoke MassUpdate service operation manageImpactedObjectUpdates providing
             the list of modifiable impacted objects and a ChangeItemRevision. This service
             operation when invoked with executionMode=murAddImpactedObjectToMarkup, adds the
             input impacted objects on the input ChangeItemRevision.
             
Invoke MassUpdate service operation getMarkupChangesForUpdate by
             providing a ChangeItemRevision as input. It returns the list of Fnd0MarkupChange
             object UIDs referenced by Fnd0Markup object associated with input ChangeItemRevision.
             
Invoke MassUpdate service operation  executeMarkupChanges in loop
             by providing a batch of Fnd0MarkupChange objects UIDs until all the Fnd0MarkupChange
             UIDs are processed for execution. Once all the batches are executed successfully
             then delete the Fnd0Markup object associated with input ChangeItemRevision.
             



Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         List of structure containing information about <b>ChangeItemRevision</b> and <b>Fnd0MarkupChange</b>
                         objects UIDs associated with it
             
        :return: 
        """
        ...
    def ExpandOneLevel(self, Input: list[ExpandOneLevelSearchScopeInput]) -> ExpandOneLevelSearchScopeResponse:
        """    
             This operation expands the given parent product structure node to fetch its immediate
             children. A call to this operation is made when defining a search scope for impacted
             object search.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         This is a structure information containing inputs required to expand the product
                         structure node to define the impacted object search scope.
             
        :return: 
        """
        ...
    def GetImpactedObjectDetails(self, Input: list[ImpactedObjectDetailsInput]) -> ImpactedObjectDetailsResponse:
        """    
             This operation gathers the impacted object details required to perform mass update.
             Details like whether the impacted object is selectable for performing an update,
             if not selectable then the reason for it being non-selectable, whether the impacted
             object is out of date etc. is returned as an output response.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Structure containing input information required to get impacted object details
             
        :return: 
        """
        ...
    def GetImpactedObjects(self, Input: list[ImpactedObjectsQueryInput]) -> ImpactedObjectsQueryResponse:
        """    
             This operation searches for product structure objects where  a given target ItemRevision
             is used.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Structure containing information to query impacted objects.
             
        :return: 
        """
        ...
    def GetRevisionRules(self, Operation: int) -> GetRevisionRulesResponse:
        """    
             This operation returns the list of valid revision rules applicable for specific mass
             update operation type.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Operation: 

        :return: 
        """
        ...
    def ManageImpactedObjectUpdates(self, Input: list[ManageImpactedObjectUpdateInput]) -> ManageImpactedObjectUpdatesResponse:
        """    
             This operation performs Add impacted object to or Remove impacted object from Change
             ItemRevision Markup as per the client request.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Structure containing information to manage impacted objects on change <b>ItemRevision</b>

        :return: 
        """
        ...
    def UpdateImpactedObjects(self, Input: list[UpdateImpactedObjectInput], UpdateRequestId: str) -> UpdateImpactedObjectResponse:
        """    
             This operation performs an update on input impacted objects by replacing target ItemRevision
             with replacement ItemRevision.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Structure containing information required to perform mass update of impacted objects.
             
        :param UpdateRequestId: 
                         Unique Identifier per update request initiated from the 'Mass Update Realization'
                         wizard. If the update is being performed in batches then this Identifier is same
                         for all the batches.
             
        :return: 
        """
        ...
    def UpdateImpactedObjectsEnd(self, Input: list[UpdateImpactedObjectInput]) -> UpdateImpactedObjectEndResponse:
        """    
             This operation performs the post update cleanup activity. This operation should be
             called only once after all the update batches are executed using 'updateImpactedObjects'.
             If all the update batches are executed successfully then this operation deletes the
             markup associated with input change ItemRevision.
             

Use Cases:


User wants to update the realizations saved on change ItemRevision.
             Operation 'getMarkupChangesForUpdate' is called by providing change ItemRevision
             as an input. This operation returns the Fnd0MarkupChange objects having information
             about impacted objects to be updated.
             
If the number of markup change objects is more than the update batch
             size then objects are updated in batches. Operation 'executeMarkupChanges' is then
             called per batch to update the batched markup change objects. This operation performs
             update on the impacted objects using information available on Fnd0MarkupChange
             objects.
             
Operation 'updateImpactedObjectsEnd' ends the update process and
             performs the cleanup activity if required. E.g. If the update is performed in context
             of change ItemRevision and if all the batches are executed successfully then
             this operation deletes the Fnd0Markup object associated with change ItemRevision
             in context of which the update has been performed.
             



Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Note: Out of all the member variables present in the input structure variable, only
                         'change' member variable is being used presently.Rest all the member variables are
                         kept for Future use.
             
        :return: 
        """
        ...
    def UpdateImpactedObjectsStart(self, Input: list[UpdateImpactedObjectInput]) -> UpdateImpactedObjectStartResponse:
        """    
             This operation builds the prerequisite information required to perform an update
             in batches. E.g. this operation generates an update request identifier that is used
             by all update batch requests. This operation should be called only once before calling
             the 'updateImpactedObjects' operation per batch.
             

Use Cases:


User wants to update the realizations (of a target ItemRevision)
             to a specific replacement ItemRevision. To do the update all impacted objects
             needs to be identified. Operation 'getImpactedObjects' is called by providing an
             input target ItemRevision as an input. This operation returns all the impacted
             objects.
             
Operation 'getImpactedObjectDetails' is then called by providing
             all the impacted objects as an input to check whether the impacted objects are modifiable
             or not.
             
User then selects the modifiable impacted objects to perform update
             upon them. If the number of selected impacted objects is more than the update batch
             size then impacted objects are updated in batches. Operation 'updateImpactedObjectsStart'
             starts the update process with some preprocessing. e.g. operation 'updateImpactedObjectsStart'
             builds the update request identifier that is common for all the subsequent update
             batch requests. Operation 'updateImpactedObjectsStart' should be called only once
             before calling the 'updateImpactedObjects' operation per batch
             
Operation 'updateImpactedObjects' is then called per batch to update
             the batched impacted objects. This operation updates the impacted objects as per
             the input replacement ItemRevision.
             



Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Note: This input parameter is not being used presently. This parameter has been provided
                         for Future use case.
             
        :return: The update request identifier.
        """
        ...
    def GetMarkupChangesForUpdate(self, Input: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> GetMarkupChangesForUpdateResponse:
        """    
             This operation queries Fnd0MarkupChange objects referenced by Fnd0Markup
             object associated with input ChangeItemRevision and returns UIDs of the Fnd0MarkupChange
             objects to the client.
             

Use Cases:

             Execute markup changes associated with ChangeItemRevision object
             

Invoke MassUpdate service operation getImpactedObjects by providing
             target ItemRevision. This operation returns the list of impacted object UIDs.
             
Invoke MassUpdate service operaion getImpactedObjectDetails by supplying
             the batch of impacted object UIDs. This API returns the information specifying whether
             each of the input impacted objects is modifiable or not.
             
Invoke MassUpdate service operation manageImpactedObjectUpdates providing
             the list of modifiable impacted objects and a ChangeItemRevision. This API
             when invoked with executionMode=murAddImpactedObjectToMarkup, adds the input impacted
             objects on the input ChangeItemRevision.
             
Invoke MassUpdate service operation getMarkupChangesForUpdate by
             providing a ChangeItemRevision as input. It returns the list of Fnd0MarkupChange
             object UIDs referenced by Fnd0Markup object associated with input ChangeItemRevision.
             
Invoke MassUpdate service operation executeMarkupChanges in loop
             by providing a batch of Fnd0MarkupChange object UIDs until all the Fnd0MarkupChange
             UIDs are processed for execution.
             



Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         List of  <b>ChangeItemRevision</b>  objects to be executed for mass update operation
             
        :return: 
        """
        ...
    def ValidateChangeObjectForMassUpdate(self, Input: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], MassUpdateType: str) -> ValidateChangeObjectForMassUpdateResponse:
        """    
             This operation validates the input change ChangeItemRevision object for a
             given Mass Update type. When invoked with "massUpdate" as an input, it validates
             whether the input ChangeItemRevision is valid for 'Mass Update' action. When
             invoked with "massUpdateRealization" as an input, it validates whether the input
             ChangeItemRevision is valid for 'Mass Update Realization' action.
             

Use Cases:

             Select ChangeItemRevision and perform 'Mass Update' or 'Mass Update Realization'.
             Operation 'validateChangeObjectForMasUpdate' is invoked to validate whether the selected
             ChangeItemRevision is valid for the respective action 'Mass Update' or 'Mass
             Update Realization' initiated by the user.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         List of <b>ChangeItemRevision</b> objects to be validated for specified Mass Update
                         type
             
        :param MassUpdateType: 

        :return: 
        """
        ...

