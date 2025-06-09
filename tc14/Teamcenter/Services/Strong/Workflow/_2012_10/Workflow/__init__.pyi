import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def PerformAction2(self, Task: Teamcenter.Soa.Client.Model.Strong.EPMTask, Action: str, Comments: str, Password: str, SupportingValue: str, SupportingObject: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation performs an action on a workflow task. The following actions are supported:
             

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
             workflow tasks can be performed or signed-off using office client as well. This operation
             can be used to perform or sign-off the workflow tasks.
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Task: 
                         Workflow task on which the action needs to be performed
             
        :param Action: 
                         "SOA_EPM_claim_action"                            Claim the task
             
        :param Comments: 
                         A comment assigned to this task action. This may be an empty string.
             
        :param Password: 
                         The password for a secure task. The value of this parameter is ignored for non-secure
                         tasks.
             
        :param SupportingValue: 
                         Following are the result values applicable for different tasks: "SOA_EPM_unset" -
                         Do Task, Review Task, Route Task, Ackowledge Task, EPMTask, Condition Task (Auto/Manual),
                         select-signoff-team task, Validate Task "SOA_EPM_completed" - Do Task, EPMTask, select-signoff-team
                         task "SOA_EPM_unable_to_complete" - Do Task, EPMTtask, Condition Task (Manual) "SOA_EPM_true"
                         - Condition Task (Auto/Manual)  "SOA_EPM_false" - Condition Task (Auto/Manual)  "SOA_EPM_no_error"
                         - Validate Task
             
        :param SupportingObject: 
                         If the action is <i>assign</i>, provide a user or resource pool to assign the task.
                         If the task is perform-signoff task, provide the Signoff object to set the decision.
                         If the task is a perform-signoff task and the action is <i>claim</i>, provide the
                         signoff object to be claimed.
             
        :return: 
        """
        ...

