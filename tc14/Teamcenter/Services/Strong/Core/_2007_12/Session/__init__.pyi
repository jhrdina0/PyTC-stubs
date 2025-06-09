import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class StateNameValue:
    """
    This structure is used to hold a single name/value pair.
    """
    def __init__(self, ) -> None: ...
    Name: str
    """The name of the UserSession state property."""
    Value: str
    """The value of the state property."""

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SetUserSessionState(self, Pairs: list[StateNameValue]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set the desired user session state values.  To clear a field's value, pass an empty
             string "" as the value. Failure to set a particular state value will result in a
             Partial Error with the clientId set to the name of the state property. State values
             can be per client session or per server session. Client session state is kept separate
             for each client application sharing the same Teamcenter server session, while server
             session state is shared with all client application sharing the Teamcenter server
             session. Valid keys for the session state pairs are:
             


currentChangeNotice: The UID of the ChangeNotice business
             object for this session (client session). This is deprecated from release Teamcenter
             11.5.
             
refreshPOM: If true the business objects in the POM are refreshed
             before returning property values.  This ensures property data is up-to-date, but
             is a performance hit (client session).
             
objectPropertyPolicy: The name of the current object property
             policy. This can also be controlled through the ObjectPropertyPolicyManager in the
             SOA client framework  (client session).
             
maxOperationBracketTime: Time (seconds) to bracket to limit
             a  POM refresh (client session).
             
maxOperationBracketInactiveTime: Time (seconds) to bracket
             to limit a  POM refresh (client session).
             
usePolicyOnly: If true, only properties defined in the current
             Object Property Policy will be returned. Objects that are added to the updated list
             of the ServiceData without named properties by default are returned with all properties
             currently loaded in the POM.
             
formatProperties: If true, the display value of the property
             will be formatted, if there is an active property formatter is attached to it. If
             false, the display value of the property will not be formatted, even if there is
             an active property formatter attached to it.
             
currentProject: The UID of the Project object (server
             session).
             
workContex: The UID of the WorkContext object (server
             session).
             
volume: The UID of the Volume object (server session).
             
local_volume: The UID of the LocalVolume object (server
             session).
             
groupMember: The UID of the GroupMember object (server
             session).
             
currentDisplayRule: The UID of the DisplayRule object
             (server session).
             
currentOrganization: The UID of the Organization object
             (server session).
             
locationCodePref: The CAGE/Location Code preference. This
             value is set on the Item attribute fnd0OriginalLocationCode
             when Item objects are created (server session).
             
currentChangeItem: The UID of the Change Item Revision business
             object for this session. This functionality is supported from Teamcenter 11.5.
             



Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Pairs: 
                         A list of name/value pairs of state properties to set.
             
        :return: 
        """
        ...
    def SetAndEvaluateIdDisplayRule(self, IdentifiableObjects: list[Teamcenter.Soa.Client.Model.ModelObject], DisplayRule: Teamcenter.Soa.Client.Model.Strong.IdDispRule, SetRuleAsCurrentInDB: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Set the ID display rule for the session and optionally set it in the database.  The
             business objects from the identifiableObjects
             list are expanded using the new ID display rule and returned. The rule is applied
             to all business objects process throughout the rest of the session.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param IdentifiableObjects: 
                         A list of business objects for which the new ID display rule has to be re-evaluated.
             
        :param DisplayRule: 
                         The ID display rule that is to be used for evaluation.
             
        :param SetRuleAsCurrentInDB: 
                         If true then the ID display rule will be set for the current user in the database.
             
        :return: .
        """
        ...

