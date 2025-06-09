import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ApplySignatureInput:
    """
    
Structure represents the parameters required to apply digital signature on
target
objects.
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The target object whose digital signature will be applied."""
    Base64String: str
    """The Base64 string containing signed information."""

class PerformActionInputInfo:
    """
    
Structure represents the parameters required to perform an action on an EPMTask
or Signoff.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Input string to uniquely identify the input, used primarily for error handling and
            output mapping.
            
"""
    ActionableObject: Teamcenter.Soa.Client.Model.ModelObject
    """The EPMTask or Signoff on which the action needs to be performed."""
    Action: str
    """
            Action to be performed on EPMTask or Signoff.
            

            Possible values for action are as follows.
            

                            Action                        Description
            

            "SOA_EPM_assign_action"- Assign task or delegate a signoff
            
            "SOA_EPM_start_action"- Start task
            
            "SOA_EPM_complete_action"- Mark the task as Complete
            
            "SOA_EPM_skip_action"- Skip task
            
            "SOA_EPM_suspend_action"- Suspend task
            
            "SOA_EPM_resume_action"    - Resume task
            
            "SOA_EPM_undo_action"- Undo task
            
            "SOA_EPM_abort_action"- Abort task
            
            "SOA_EPM_perform_action"- Perform task
            
            "SOA_EPM_approve_action"- Approve a Review Task
            
            "SOA_EPM_reject_action"- Reject a Review Task
            
            "SOA_EPM_promote_action"- Promote task
            
            "SOA_EPM_demote_action"- Demote task
            
            "SOA_EPM_assign_approver_action"- This action is not used. Use addSignoffs operations
            to add users to select-signoff-team task
            
            "SOA_EPM_notify_action"- Notify
            
            "SOA_EPM_no_action"- No action, results in the comments being set without triggering
            state change on the task.
            
            "SOA_EPM_fail_action"- Fail the task
            
            "SOA_EPM_claim_action"- Claim the task
            """
    Password: str
    """
            The password for a secure Task. The value of this parameter is ignored for non-secure
            Task.
            
"""
    SupportingValue: str
    """
            This argument can be used to send in decision value or result.  If the task is perform-signoff
            task, possible values for decision are:
            

"SOA_EPM_no_decision"
            
"SOA_EPM_approve"
            
"SOA_EPM_reject"
            



            Following are the result values applicable for different tasks:
            


"SOA_EPM_unset"- Do Task, Review Task, Route Task, Ackowledge Task,
            EPMTask, Condition Task (Auto/Manual), select-signoff-team task, Validate Task
            
"SOA_EPM_completed"- Do Task, EPMTask, select-signoff-team task
            
"SOA_EPM_unable_to_complete"- Do Task, EPMTtask, Condition Task (Manual)
            
"SOA_EPM_true"- Condition Task (Auto/Manual)
            
"SOA_EPM_false"- Condition Task (Auto/Manual)
            
"SOA_EPM_no_error"- Validate Task
            

"""
    SupportingObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            If the action is assign, provide a User or ResourcePool to assign the
            task.
            """
    PropertyNameValues: System.Collections.Hashtable
    """
            Property name and values map that will contain all property names and corresponding
            string values that needs to be saved. e.g. comments can be set on the EPMTask/Signoff
            by adding it to this map.
            """
    Signatures: list[ApplySignatureInput]
    """
            List of ApplySignatureInput objects, each representing target object and its corresponding
            Base64 string.
            """

class SetActiveSurrogateInputInfo:
    """
    
Structure represents the parameters required to set/unset the logged in user as
an
active surrogate on the EPMTask or Signoff objects and transfer the
checkout of the target objects to/from the original user.
    """
    def __init__(self, ) -> None: ...
    TaskOrSignoffTag: Teamcenter.Soa.Client.Model.ModelObject
    """
            The EPMTask or Signoff business object for which the current user needs
            to be set/unset as an active surrogate.
            """
    ReleaseStandIn: bool
    """
            Logged in user is set as an active surrogate on EPMTask or Signoff
            when value of this parameter is false and is released as an active surrogate from
            the EPMTask or Signoff when value of this parameter is true.
            """
    TransferCheckouts: bool
    """
            During Stand-In operation, if the value of this parameter is true, the transfer of
            checkout of the target object(s) from the original user to the current user is performed.
            During Release operation, if the value of this  parameter is true, the transfer of
            checkout of the target object(s) from the current user to the original user is performed.
            If the value of the parameter is false, transfer of checkout of the target object(s)
            is not performed during Stand-In or Release operation.
            """

class SurrogateInput:
    """
    
This operation sets or unsets the surrogate resource for a given User effective
for
a given date range.
    """
    def __init__(self, ) -> None: ...
    Unset: bool
    """If true, remove surrogate; if false, set surrogate."""
    FromResource: Teamcenter.Soa.Client.Model.Strong.User
    """The user for whom the surrogate will be set/unset."""
    ToResource: Teamcenter.Soa.Client.Model.Strong.User
    """The surrogate user."""
    StartDate: System.DateTime
    """The date at which the surrogate setting is to take effect."""
    EndDate: System.DateTime
    """The date at which the surrogate setting ceases to be in effect."""

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def PerformAction3(self, Input: list[PerformActionInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation performs an action on an EPMTask or Signoff. This operation
             also allows user to digitally sign the target objects in a workflow.
             


             Note:

             The Teamcenter session should be configured with HTTPS as the password in the input
             structure is not encrypted.
             

             Following actions are supported on EPMTask.
             


Assign
             
Start
             
Complete
             
Skip
             
Suspend
             
Resume
             
Undo
             
Perform
             
Approve
             
Reject
             
Promote
             
Demote
             
Claim
             



             Following action is supported on Signoff.
             


Assign
             


             This action will delegate a Signoff to a different GroupMember or ResourcePool
             and records the comments supplied while performing delegate operation in the audit
             log. User may use workflowService.getResourcePool method To get the ResourcePool
             business object from only group or only role or both.
             

Use Cases:

Use Case 1: User can perform a workflow task.

Description: User can perform an EPMTask from worklist folder in rich
             or thin client. Similarly EPMTask can be performed or signed-off using office
             client as well. This operation can be used to perform or signoff the workflow tasks.
             

Use Case 2: User can assign or delegate a Signoff to a different GroupMember or
             ResourcePool and provide optional comments while performing delegate operation.

Description: When a user delegates a Signoff to a different GroupMember
             or ResourcePool,  the comments provided while performing delegate operation
             gets recorded in the audit log.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Input: 
                         A list of PerformActionInputInfo structure which contains clientId, the <b>EPMTask</b>
                         or <b>Signoff</b> business object, action to be performed on an <b>EPMTask</b> or
                         <b>Signoff</b>, the password for a secure Task, supportingValue which can be used
                         to send in decision value or result, supporting object which can be a <b>User</b>
                         or a <b>ResourcePool</b> business object and the NameValuePair which is a map of
                         property name and values that will contain all property names and corresponding string
                         values that needs to be saved  on an input business object.
             
        :return: 330001(error)Â Â Â Â : Internal error occurred during this operation.
        """
        ...
    def SetActiveSurrogate(self, Input: list[SetActiveSurrogateInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets/unsets the logged in user as an active surrogate on a given EPMTask
             or Signoff. It transfers checkout of the target object(s) to/from the logged
             in user from/to the original user.
             

Use Cases:

Use Case 1: User can Stand In for an EPMTask or Signoff with
             Transfer Check-Out(s).
             
Description: When a user is set as a surrogate and wants to perform received
             task in the original user's inbox while allowing the original user to retain control,
             user can Stand-In for the EPMTask or Signoff. The transfer of checkout
             of the target object(s) from the original user is done when the boolean input parameter
             transferCheckouts is set to true.
             

Use Case 2: User is released from EPMTask or Signoff with Transfer
             Check-Out(s).
             
Description: Releases current user as an active surrogate for a EPMTask
             or Signoff. The transfer of checkout of the target object(s) from the current
             user to the original user is done when the boolean input parameter transferCheckouts
             is set to true.
             

Use Case 3: User can Stand-In for an EPMTask or Signoff without
             Transfer Check-Out(s).
             
Description: When a user is set as a surrogate and wants to perform the task
             in the original user's inbox while allowing the original user to retain control,
             user can Stand-In for the EPMTask or Signoff. The target object(s)
             will remain checked out to the original user if they were checked out before the
             Stand-In operation was performed.
             

Use Case 4: User is released for EPMTask or Signoff without
             Transfer Check-Out(s).
             
Description: Releases current user as an active surrogate for an EPMTask
             or Signoff. The target object(s) will remain checked out to the current user
             if the transfer of checkout(s) was done while Stand-In operation was performed.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Input: 
                         A list of SetActiveSurrogateInputInfo structure which contains the <b>EPMTask</b>
                         or <b>Signoff</b> business object, boolean to indicate the Stand-In or Release operation
                         and the boolean to indicate if the checkout of the target objects(s) should be transferred
                         or not.
             
        :return: 
        """
        ...
    def SetSurrogate(self, Requests: list[SurrogateInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets or unsets the surrogate resource for a given User effective for
             a given date range.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Requests: 
                         A list of SurrogateInput structures which contain the original User, the surrogate
                         User, effective start date, and the end date.
             
        :return: 219021: Start date cannot be later than end date. Please set start date again.
        """
        ...
    def PerformActionWithSignature(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Action: str, Comments: str, Password: str, SupportingValue: str, SupportingObject: Teamcenter.Soa.Client.Model.ModelObject, Signatures: list[ApplySignatureInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation performs an action on workflow task. The following actions are supported.
             


Assign
             
Start
             
Complete
             
Skip
             
Suspend
             
Resume
             
Undo
             
Perform
             
Approve
             
Reject
             
Promote
             
Demote
             
Claim
             



Use Cases:

             User can perform a workflow task from worklist folder in rich or thin client. Similarly,
             workflow tasks
             
             can be performed or signed-off using office client as well.This operation can be
             used to perfrom or sign-off the workflow tasks.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Task: 
                         Workflow task on which the action needs to be performed
             
        :param Action: 
                         Â Â Â Â 
             
        :param Comments: 
                         A comment assigned to this task action. This may be an empty string.
             
        :param Password: 
                         The password for secure task. The value of this parameter is ignored for non-secured
                         tasks.
             
        :param SupportingValue: 
                         Â Â Â Â 
             
        :param SupportingObject: 
                         If the action is assign, provide a user or resource pool to assign the task. If the
                         task is perform-signoff task, provide the Signoff object to set the decision. If
                         the task is a perform-signoff task and the action is claim, provide the signoff object
                         to be claimed.
             
        :param Signatures: 
                         List of ApplySignatureInput objects, each representing target object and its corresponding
                         Base64 string.
             
        :return: 
        """
        ...
    def SetOutOfOffice(self, FromResource: Teamcenter.Soa.Client.Model.Strong.User, ToResource: Teamcenter.Soa.Client.Model.ModelObject, StartDate: System.DateTime, EndDate: System.DateTime) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets/unsets Out of Office resource for a given user. The Out of Office
             resource can be a User or a ResourcePool. The Out of Office setting
             is effective for the specified date range.
             

Use Cases:

Use Case 1: User sets Out of Office
             
Description: When a user is going to be out of the office and wants to have
             someone receive the tasks during his/her absence then user sets Out of Office. If
             the end date is not provided then all the future tasks will be delegated indefinitely.
             

Use Case 2: System Administrator sets Out of Office for another user
             
Description: When a user is out of the office but does not have Out of Office
             setting then System Administrator can set Out of Office for the user. Also, group
             administrators will only be able to set the Out of Office for users within their
             group.
             

Use Case 3:  User modifies Out of Office settings
             
Description: When a user has set Out of Office and during this period if the
             Out of Office resource is also going to be out of the office then System Administrator
             can modify the Out of Office settings of the user
             

Use Case 4:  User unsets Out of Office settings
             
Description: When a user who has set Out of Office is back before the specified
             end date then he/she can unset the current Out of Office setting. The startDate and
             endDate parameters will be set to null and the toResource paramenter will be set
             to an empty object.
             


Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param FromResource: 
                         The <b>User</b> for whom the Out of Office will be set/unset.
             
        :param ToResource: 

        :param StartDate: 
                         The effective start date of the Out of Office setting.
             
        :param EndDate: 
                         The effective end date of the Out of Office setting.  Set to null (for C++ use DateTime::getNullDate())
                         to set the Out of Office to be indefinite (no end).
             
        :return: 219027: The user is out of the office starting from date. Please select another user
             for these dates.
        """
        ...

