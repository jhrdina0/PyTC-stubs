import System
import Teamcenter.Soa.Client.Model
import typing

class MakeUserResponse:
    """
    The return data for the makeUser service operation.
    """
    def __init__(self, ) -> None: ...
    CommandStatus: int
    """
            The make_user command completion status (0 - Success, 1 - Failure). See the make_user
            utility documentation for details.
            """
    StandardOutputFmsTicket: str
    """
            FMS ticket for the make_user standard output. This element is empty if the enableStandardOutput
            parameter for the operation is false.
            """
    StandardErrorFmsTicket: str
    """
            FMS ticket for the make_user standard error. This element is empty if the enableStandardError
            parameter for the operation is false.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any errors that occur transferring files to or from FMS or in launcing the make_user
            utility are included in the list of partial errors.
            """

class UserManagement:
    """
    Interface UserManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def MakeUser(self, Arguments: list[str], BatchFileFmsTicket: str, EnableStandardOutput: bool, EnableStandardError: bool) -> MakeUserResponse:
        """    
             This operation executes the make_user utility on the Teamcenter server with the specified
             command line arguments and optional batch input file. The make_user utility runs
             with the same user and group as the current session user.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :param Arguments: 
                         A list of command line arguments for the make_user utility. These arguments are specified
                         in the same format as in the make_user utility. All make_user command line arguments
                         are supported except "<i>-u=</i>", "<i>-p=</i>", "<i>-g=</i>", "<i>-pf=</i>" and
                         "<i>-file=</i>". If unsupported arguments are specified, they are ignored.
             
        :param BatchFileFmsTicket: 
                         FMS transient file ticket for a make_user batch input file. To run make_user with
                         a batch input file, the client must first upload the file to Teamcenter transient
                         volume using FMS, and pass the resulting FMS transient file ticket as this input
                         parameter. If the ticket is not empty, the file is passed to the make_user utility
                         using the <i>-file=file_path</i> argument.
             
        :param EnableStandardOutput: 
                         If true, the standard output from the make_user utility is returned as an FMS file
                         ticket. If false, the output is discarded.
             
        :param EnableStandardError: 
                         If true, the standard error output from the make_user utility is returned as an FMS
                         file ticket. If false, the error output is discarded.
             
        :return: 
        """
        ...

