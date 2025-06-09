import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Common
import typing

class AddPoliciesResponse:
    """
    The policies added to the session.
    """
    def __init__(self, ) -> None: ...
    PolicyIDs: list[str]
    """
            A list of policy IDs. The initial size and order of this list will match the input
            list of clientPolicies, with an unique ID
            generated for each policy defined in the  clientPolicies
            list. Successfully added policies from the namedPolicies
            list are appended to th end of this list.
            """
    PartialErrors: Teamcenter.Soa.Client.Model.PartialErrors
    """Partial errors or warnings."""

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AddObjectPropertyPolicies(self, ClientPolicies: list[Teamcenter.Soa.Common.ObjectPropertyPolicy], NamedPolicies: list[str]) -> AddPoliciesResponse:
        """    
             Adds multiple object property policies to the session. Once these policies are added
             to the session, the client application can quickly switch between policies using
             the appropriate methods on the ObjectPropertyPolicyManager
             class in the SOA client framework.
             
             The business logic of a service operation determines what business objects are returned,
             while the object property policy determines which properties are returned on each
             business object instance. This allows the client application to determine how much
             or how little data is returned based on how the client application uses those returned
             business objects. The policy is applied uniformly to all service operations.
             
             By default, all applications use the Default object property policy, defined
             on the Teamcenter server $TC_DATA/soa/policies/default.xml.
             It is this policy that is applied to all service operation responses until the client
             application changes the policy. Siemens PLM Software strongly recommends that all
             applications change the policy to one applicable to the client early in the session.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param ClientPolicies: 
                         A list of client defined object property policies.
             
        :param NamedPolicies: 
                         A list of policy files defined on the Teamcenter server volume at<font face="courier" height="10"> $TC_Data/soa/policies/*.xml</font>.
             
        :return: 
        """
        ...

