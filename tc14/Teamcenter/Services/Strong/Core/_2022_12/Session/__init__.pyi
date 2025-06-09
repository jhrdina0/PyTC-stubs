import typing

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def TcServerSleep(self, Seconds: int) -> str:
        """    
             A no-op serivce operation that puts the TcServer in a wait/sleep for the requested
             amount of time before returning.
             
             This can be used to simulate long running service requests.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Seconds: 
                         The number of seconds to sleep.
             
        :return: A message that the operation has completed.
        """
        ...

