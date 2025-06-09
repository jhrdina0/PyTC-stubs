import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateSignoffInfo:
    """
    
CreateSignoffInfo structure contains the
            requisite information to create the Signoff object. If the
originType is "SOA_EPM_SIGNOFF_ORIGIN_PROFILE" and the
            signoff member already exit in

            any signoff member matches the signoff profile.
    """
    def __init__(self, ) -> None: ...
    SignoffMember: Teamcenter.Soa.Client.Model.ModelObject
    """
            Signoff member is the reviewer who needs to perform the signoff action. It can be
            group member, resource pool or an address list.
            """
    Origin: Teamcenter.Soa.Client.Model.ModelObject
    """
            Origin references the source of the signoff. When a profile signoff is added, origin
            references the signoff profile object.When a member of an address list is added as
            signoff, origin represents the address list to which the signoff member belongs.
            
            """
    SignoffAction: str
    """
            Possible values are
            
"SOA_EPM_Review"

            -This values specifies that the signoff needs to be added as a review signoff.
            

"SOA_EPM_Acknowledge"

            -This value specifies that the signoff needs to be addaed as a acknowledge signoff.
            

"SOA_EPM_Notify" 

            -This value specifies that the signoff needs to be addaed as a notify signoff.
            

"SOA_EPM_ACTION_UNDEFINED"

            -This value should not be used in parameter, else an error would be returned.
            
"""
    OriginType: str
    """
            For profile signoff use case , the originType
            is "SOA_EPM_SIGNOFF_ORIGIN_PROFILE" and for subset of addresslist use case
            , the originType is "SOA_EPM_SIGNOFF_ORIGIN_ADDRESSLIST".
            

            Possible string values:
            
"SOA_EPM_ORIGIN_UNDEFINED"

            -This value specifies that the origin value is NULL or not defined.
            

"SOA_EPM_SIGNOFF_ORIGIN_PROFILE"

            -This value is specifies that the origin value is the signoff profile object.
            

"SOA_EPM_SIGNOFF_ORIGIN_ADDRESSLIST"

            -This value is specifies that the origin value is an address list object
            
                    
            """
    SignoffRequired: str
    """
            string which indicates whether the added reviewer decision is required or optional
            while performing signoff.
            


            Possible values are
            
"SOA_EPM_SIGNOFF_OPTIONAL"

            -sets the property to Optional. sign off decision is not required as long as quorum
            is met and can be manualy overridden to "Required Modifiable" before perform signoff
            task starts.
            

"SOA_EPM_SIGNOFF_REQUIRED_MODIFIABLE"

            - sets the property to "Required Modifiable". sign off decision is required even
            if quorum is met and can be manually overriden back to "Optional" before perform
            signoff task starts.
            

"SOA_EPM_SIGNOFF_REQUIRED_UNMODIFIABLE"

            - sets the property to "Required Unmodifiable"  signoff decision is required even
            if quorum is met and cannot be manually overridden to "Optional" before perform signoff
            task starts.
            




"""

class CreateSignoffs:
    """
    
CreateSignoffs structure contains the workflow
            task for which Signoff needs to be added and information to create
the Signoff
            objects like the Signoff Member and references like Signoff Profile
or address list.
    """
    def __init__(self, ) -> None: ...
    Task: Teamcenter.Soa.Client.Model.Strong.EPMTask
    """Workflow task object to which the Signoff need to be added"""
    SignoffInfo: list[CreateSignoffInfo]
    """The required information to create the Signoff object"""

class Workflow:
    """
    Interface Workflow
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddSignoffs(self, Signoffs: list[CreateSignoffs]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation adds signoffs to a workflow task. The signoffs can be added as adhoc-signoffs
             or it can be used to staff profiles. The signoff members can be group members or
             resource pools. When an address list is provided, the members of the address list
             are used to create and add signoffs to the task. The signoffs can be added as review
             signoffs, acknowledge signoffs and notify signoffs. This operation allows to designate
             added reviewers as required or optional.
             

Use Cases:

             Following are four different use cases to add the signoffs -
             
Use case 1: Add adhoc signoff

             To add an adhoc signoff, signoffMember specified as part of CreateSignoffInfo structure can either be a GroupMember, Resource
             Pool or an address list. For this use case, value for origin
             in CreateSignoffInfo should be NULLTAG.
             

Use case 2: Add profile signoff

             In this use case, the signoffMember specified as part of the CreateSignoffInfo structure has to satisfy the signoff profile.
             Value for the origin should be the signoff
             profile object and originType should be "SOA_EPM_SIGNOFF_ORIGIN_PROFILE".
             

Use case 3: Add subset of the  members of the  address list as signoff

             User may want to add subset of the members of an address list as signoffs. In this
             use case, the origin should be the address
             list object and originType should be "SOA_EPM_SIGNOFF_ORIGIN_ADDRESSLIST".
             Note that members of the address list are always added as adhoc signoffs.
             

Use case 4: Add signoff as required or optional

             User may specify the signoff decision is required or optinal for the added reviewer
             . By default the signoff is "Optional" signoff.This can be done by adding
             string member signoffRequired in CreateSignoffInfo.To designate the added reviwer as required signoff
             the string value will be "RequiredUnmodifiable" which cannot be manually overridden
             to "Optional". One Possible value is "RequiredModifiable" It indicates sign
             off decision is required, which can be manually overridden to "Optional".
             

Teamcenter Component:

             Workflow - This feature provides the support for modeling and executing a business
             process. With this feature, WorkspaceObject objects may be submitted to a workflow,
             modified, routed for review,  approved and a release status added.
             
        :param Signoffs: 
                         This is a list of <font face="courier" height="10">CreateSignoffs</font> structures
                         which contain the Task for which theSignoffs need to be added and the list of <font face="courier" height="10">CreateSignoffInfo</font> structure containing the requisite
                         information to create the Signoff object.
             
        :return: 
        """
        ...

