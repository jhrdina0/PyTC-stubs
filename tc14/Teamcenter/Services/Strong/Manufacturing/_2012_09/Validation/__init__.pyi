import Teamcenter.Soa.Client.Model
import typing

class ValidationCheckCallbackParam:
    """
    Validation Check Callback Param
    """
    def __init__(self, ) -> None: ...
    Type: str
    """The type of the validation always MFG_ValidationChecksCallback"""
    Library: str
    """Customized DLL Name"""
    Name: str
    """Customized Name - The name of the validation test"""
    Func: str
    """Customized Function name"""
    FailAllOnError: bool
    """Continue to the next test if the previous test failed."""

class ValidationCheckExecutionErrors:
    """
    Validation Check Execution Errors
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """the non valid object line"""
    ValidationErrors: list[ValidationCheckExecutionErrorsDetails]
    """validationErrors"""
    ValidationTest: ValidationCheckCallbackParam
    """The validation check that failed."""

class ValidationCheckExecutionErrorsDetails:
    """
    Validation Check Execution Errors Details
    """
    def __init__(self, ) -> None: ...
    MsgId: int
    """could be ifail or lov (msgId from ValidationNotice struct)"""
    Msg: str
    """description of the localized error"""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The object on which the validation check failed"""
    ValidationNoticeType: str
    """The type of the returned notice from the callback functions"""

class ValidationCheckExecutionParam:
    """
    Validation Check Execution Param
    """
    def __init__(self, ) -> None: ...
    Root: Teamcenter.Soa.Client.Model.ModelObject
    """
            The root object to be validated, could be any line type of Mfg0BvrProcess or Mfg0BvrOperation
            or its derived.
            """
    ValidationChecks: list[ValidationCheckCallbackParam]
    """all the validation checks to perform on the object"""

class ValidationsChecksExecutionResponse:
    """
    Validations Checks Execution Response
    """
    def __init__(self, ) -> None: ...
    Errors: list[ValidationCheckExecutionErrors]
    """errors"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData member"""

class ValidationsChecksObjectsResponse:
    """
    Validations Checks Objects Response
    """
    def __init__(self, ) -> None: ...
    Params: list[ValidationCheckCallbackParam]
    """params"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData"""

class Validation:
    """
    Interface Validation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteValidations(self, Input: list[ValidationCheckExecutionParam], FailAllOnError: bool) -> ValidationsChecksExecutionResponse:
        """    
             This SOA function is to execute the validation checks by the user choice from the
             UI.
             
        :param Input: 
                         Validation Check Execution Param
             
        :param FailAllOnError: 
                         whether or not to fail all tests when error occurs on a specific validation check
                         for a specific line or to continue.
             
        :return: Validations Checks Execution Response
        """
        ...
    def GetAllValidations(self) -> ValidationsChecksObjectsResponse:
        """    
             This SOA function is to get all the customized registered callback to show the user
             in the UI.
             
        :return: 
        """
        ...

