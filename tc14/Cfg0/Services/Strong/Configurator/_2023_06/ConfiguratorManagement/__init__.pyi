import Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement
import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BuildableCombinationsResponse:
    """
    
            The response contains a limiting expression's validation status and a list of valid
            buildable combinations. ServiceData contains information about partial error details
            for any failures while generating build combinations.
            
    """
    def __init__(self, ) -> None: ...
    IsValid: bool
    """If true, the limiting expression is valid."""
    BuildableCombinationsJson: str
    """
            A JSON string representing a list of buildable combinations. A buildable combination
            is represented as teamcenter expression formula if you specify the output format
            as a "TcFormula" in the requestInfo input. It is the default output format when you
            do not specify the output format. If you specify the output format as a "Features",
            it will contain a list of features of the buildable combination. This string adheres
            to a JSON schema for buildable combinations defined in getBuildableCombinationsResponse_Schema.json;
            please refer to the schema and sample defined at %TC_DATA%/json/variabilityadaptor/schema
            for details. The list of buildable combination will be empty if the limiting expression's
            validation status is invalid.
            """
    NumBuildableCombinations: int
    """
            Number of buildable combinations generated. The value will be less than or equal
            to maxSize.
            """
    DoMoreBuildCombinationsExist: bool
    """If true, more buildable combinations exist than maxSize"""
    ResponseInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]
    """A list of response key and value pairs. This is reserved for future use."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData containing partial exceptions, if any."""

class VariantExpressionsResponse:
    """
    
            The structure represents the response for convertVariantExpressions operation consisting
            of list of formulae for the corresponding input variant expressions.
            
    """
    def __init__(self, ) -> None: ...
    OutputVariantExpressions: list[str]
    DisplayFormulae: list[str]
    """
            A list of display formulae that is corresponding to the list of input Variant expressions.
            The display formula honors the Global constant for primary business relevant attribute
            (Cfg0PrimaryBusinessRelevantAttribute). It also honors operator localization as well
            as user exit extension to customize display formula. This formula is strictly for
            display purposes and cannot be used as input formula.
            """
    ResponseInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]
    """A list of response names and value pairs. This is reserved for future use."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data for errors and returned objects."""

class ConfiguratorManagement:
    """
    Interface ConfiguratorManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ConvertVariantExpressions(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, VariantExpressions: list[str], ExpressionFormat: str, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> VariantExpressionsResponse: ...
    def GenerateBuildableCombinations(self, Perspective: Teamcenter.Soa.Client.Model.Strong.Cfg0ConfiguratorPerspective, SolveProfile: str, LimitingExpression: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.ExpressionInfo, Families: Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.FamilyList, RequestInfo: list[Cfg0.Services.Strong.Configurator._2022_06.ConfiguratorManagement.KeyValuePair]) -> BuildableCombinationsResponse: ...

