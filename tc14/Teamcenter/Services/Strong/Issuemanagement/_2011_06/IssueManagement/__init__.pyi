import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CastDecisionInput:
    """
    Issue review input such as review decision and comment.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    TargetIssue: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision
    """The issue report revision object to be reviewed."""
    TheDecision: str
    """
            Review decision name. Get supported review decision names from the LOV IsM0Issue
            Review Decisions and use the internal value (not localized value) as input.
            """
    TheComment: str
    """A short comment."""

class CastReviewDecisionOutput:
    """
    
            The output from casting a review decision and comment on an issue report revision
            object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Client Id."""
    TheIssueObject: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision
    """The issue report revision object just reviewed."""

class CastReviewDecisionResp:
    """
    Response from casting review decision on the issue.
    """
    def __init__(self, ) -> None: ...
    Resp: list[CastReviewDecisionOutput]
    """Output from casting review decision on the issue."""
    TheServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Service data. Teamcenter error stack content will be returned to client when error
            occurs.
            """

class IssueManagement:
    """
    Interface IssueManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CastReviewDecisionOnIssues(self, Inputs: list[CastDecisionInput]) -> CastReviewDecisionResp:
        """    
             The client calls this operation to log an issue review decision and comment to the
             target issue report, and to complete the issue management workflow process perform-signoff
             task.
             
             You may have multiple business processes to manage the issue life cycle (or design
             review process). Issue management business process can be defined as a workflow template
             that is configured with multiple tasks to model business tasks and handlers to update
             issue report statuses at the completion of a task. Teamcenter users that participate
             in issue life cycle management are issue report revision participants and can be
             auto-assigned as workflow task assignees when the issue management workflow process
             starts. Another option is to assign reviewers from the Teamcenter create new workflow
             process dialog. Workflow review tasks are commonly used to dispatch an issue management
             business task to selected users. Signing off on a workflow review task means that
             the assigned user has successfully accomplished business task and wants to complete
             the workflow review task. A business task may update issue report metadata or context
             data which is completed with various tools outside of the workflow process. This
             operation allows an assigned user to log the review decision and to comment on an
             issue and complete the workflow review task.
             
             When one review task is assigned to multiple users, the review task is called a board-review
             task and each assigned user is a member of the review board. A review decision from
             the review board is the decision from majority of board members. Each board member
             calls this operation to cast a review decision and comment. When all board members
             have signed off their respective review tasks, the workflow action handler ISSUEMGT-update-issue-status
             updates issue the report status based on the review board decision. The way to configure
             this handler is described in Issue Management User's Guide.
             


Use Cases:

             Please refer to the OOTB issue lifecycle workflow template. Users who are assignees
             to the Review Issue and Final Review tasks will call this operation
             to log the review decision and to comment on the target issue report. The rich client
             or the thin client Review Issue dialog calls this operation.
             

Teamcenter Component:

             Issue Management - Teamcenter Issue Management is an application that allows users
             to capture issue, share issue data and collaborate on the business process to resolve
             issue in product life management.
             
        :param Inputs: 
                         Inputs to cast review decisions and comments on issues.
             
        :return: Cast review decision response.
        """
        ...

