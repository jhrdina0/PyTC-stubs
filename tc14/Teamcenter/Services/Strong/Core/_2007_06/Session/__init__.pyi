import typing

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RefreshPOMCachePerRequest(self, Refresh: bool) -> bool:
        """    
             By Default the service operations will retrieve property value data straight from
             the POM. When refresh is set to true, a refresh
             will be done on business objects before getting any property data. This will update
             the POM with fresh data from the database. The refresh is only applied to business
             objects that are actually being returned by a service operation. This applies only
             to database objects, and is not applied to runtime objects.  This is applied to all
             subsequent service requests from the same client. If multiple clients are sharing
             the same Teamcenter server session the refresh POM state is applied per client. Setting
             this to true will have a performance impact but will grantee all property values
             returned are up-to-date.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Refresh: 
                         If true, the business objects are refreshed before getting property values, if false
                         the properties are retrieved from the POM without checks to the database.
             
        :return: True is always returned.
        """
        ...

