import Teamcenter.Soa.Common
import typing

class RegisterIndex:
    """
    Contains the index to be used for unregistering.
    """
    def __init__(self, ) -> None: ...
    RegistryIndex: int
    """Index to be used for unregistering."""

class SetPolicyResponse:
    """
    The policy ID and full definition of the object property policy.
    """
    def __init__(self, ) -> None: ...
    PolicyId: str
    """Unique ID for this object property policy."""
    Policy: Teamcenter.Soa.Common.ObjectPropertyPolicy
    """The full definition of the object property policy."""

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RegisterState(self, Level: str) -> RegisterIndex:
        """    
             Register desired level for server state as used by the Server Manager to control
             server timeout. Note that an attempt to register at LEVEL_STATELESS is ignored since
             this is the default level when no registrations are in effect. To move from a higher
             level to the stateless level the unregister
             operation should be used to delete the earlier registration. Note that it is possible
             to be registered at more than one level and there may be multiple registrations at
             each level.
             

Dependencies:

             unregisterState
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Level: 
                         Desired server state: "<i>Edit</i>" or "<i>Read</i>"
             
        :return: operation to undo
             this registration.  If no registration occurs, zero is returned.
        """
        ...
    def SetObjectPropertyPolicy(self, PolicyName: str, UseRefCounting: bool) -> SetPolicyResponse:
        """    
             Sets the current object property policy. The business logic of a service operation
             determines what business objects are returned, while the object property policy determines
             which properties are returned on each business object instance. This allows the client
             application to determine how much or how little data is returned based on how the
             client application uses those returned business objects. The policy is applied uniformly
             to all service operations.
             
             By default, all applications use the Default object property policy, defined
             on the Teamcenter server $TC_DATA/soa/policies/default.xml.
             It is this policy that is applied to all service operation responses until
             the client application changes the policy. Siemens PLM Software strongly recommends
             that all applications change the policy to one applicable to the client early in
             the session.
             
             The object property policy is set to the policy named in the file $TC_DATA/soa/policies/<policyName>.xml The reserved policy
             name "Empty", will enforce a policy that only returns minimum data required
             for each object (UID and type name).The object property policy will stay in affect
             for this session until changed by another call to setObjectPropertyPolicy.
             The full policy is returned where the client application can modify it throughout
             the session via calls to updatObjectPropertyPolicy.
             

             Like any other service operation, this operation cannot be called before establishing
             a session with the login serivce operation,
             so if you need a policy other than the Default policy for the business objects returned
             by the login operation, use the _2011_06 version of the login/loginSso
             operation to authenticate and establish a session without returning business objects.
             The setObjectPropertyPolicy operation can
             then be called to establish the policy for the session.
             


Dependencies:

             updateObjectPropertyPolicy
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param PolicyName: 
                         The name of the policy file without the .xml extension. The file must exist on the
                         Teamcenter server volume at <font face="courier" height="10">$TC_DATA\soa\policies\&lt;policyName&gt;.xml</font>.
             
        :param UseRefCounting: 
                         When set to true, the policy will not remove a property value until there is a matching
                         number of removes and adds in subsequent calls to <font face="courier" height="10">updateObjectPropertyPolicy</font>

        :return: .
        """
        ...
    def UnregisterState(self, Index: int) -> bool:
        """    
             Remove the specified registration.
             

Dependencies:

             registerState
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Index: 
                         Index returned by previous call to <font face="courier" height="10">registerState</font>.
             
        :return: True
        """
        ...

