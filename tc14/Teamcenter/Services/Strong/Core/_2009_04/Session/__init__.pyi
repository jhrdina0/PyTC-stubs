import typing

class Session:
    """
    Interface Session
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def StartOperation(self) -> str:
        """    
             Start an operation bracket.  An operation bracket is a period of execution in which
             any object will need to be refreshed in the server from the database only once.
             This allows the client to avoid unnecessary database operations that the server might
             perform redundantly if underlying code accesses the same object multiple times.
             The client will use the return value to call the stopOperation
             operation to indicate the end of the bracket.  Brackets may be nested or overlapped.
             A bracket should start and end within the scope of a single client function and
             should not span a user interaction.  By default, each service operation starts and
             stops its own operation bracket.
             

Dependencies:

             stopOperation
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :return: 
        """
        ...
    def StopOperation(self, OpId: str) -> bool:
        """    
             Stop an operation bracket, in which objects need to be refreshed only once.  See
             startOperation.
             

Dependencies:

             startOperation
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param OpId: 
                         The operation identifier assigned to the operation and returned by the <font face="courier" height="10">startOperation</font> request.
             
        :return: true
        """
        ...

