import System
import Teamcenter.Soa.Client.Model
import typing

class EffectivitiesInfo:
    """
    
Holds effectivity data for each input object. The effectivity data can be either
in the form of list of Teamcenter::Effectivity objects or a list of effectivity
expression
information. If the input object holds the effectivity expression, it will be
broken
into expression data structure which contains unit ranges, date ranges, end item
along with respective formula.

Note:

The operation will either populate effectivityExprData with formula or
effectivityObjects
depending on the underlying effectivity storage model.
    """
    def __init__(self, ) -> None: ...
    InputObjectIndex: int
    """The index of input BusinessObject to which effectivity information is associated."""
    EffectivityExprData: list[EffectivityExpressionData]
    """A list of Effectivity for an inputObject."""
    EffectivityExprFormula: str
    EffectivityObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of Effectivity objects with specified effectivity data."""

class EffectivityExpressionData:
    def __init__(self, ) -> None: ...
    UnitStart: int
    """The unit at which validity range starts."""
    UnitEnd: int
    """The unit at which validity range ends."""
    DateStart: System.DateTime
    """The date at which validity range starts."""
    DateEnd: System.DateTime
    """The date at which validity range ends."""
    EndItemObject: Teamcenter.Soa.Client.Model.ModelObject
    """The effectivity end Item or ItemRevision."""
    ExpressionEffFormula: str
    """Expression Effectivity clause Formula."""
    EffectivityOptions: list[EffectivityOption]

class EffectivityOption:
    def __init__(self, ) -> None: ...
    FamilyNamespace: str
    """
            The namespace by which the effectivity option family is uniquely identified. The
            familyNamespace is the item id of effectivity context associated with product Item
            with relation Fnd0ProductEffConfigCxtRel.
            
            For example, effectivity context with item id EFFCTX001 is associated with product
            Item. It has option families defined with names Maturity Intent and Module Intent.
            Maturity Intent has values Design and Production. Module Intent has values Kit and
            Modkit. The familyNamespace can be EFFCTX001.
            """
    FamilyName: str
    """
            The name of the effectivity option family. Valid option family names are available
            on the effectivity context associated with product Item with relation Fnd0ProductEffConfigCxtRel.
            
            For example, effectivity context with item id EFFCTX001 is associated with product
            Item. It has option families defined with names Maturity Intent and Module Intent.
            Maturity Intent has values Design and Production. Module Intent has values Kit and
            Modkit. The familyNamespace is set as EFFCTX001. The familyName can be either Maturity
            Intent or Module Intent.
            """
    OpCode: int
    OptionValue: str
    """
            The value for the effectivity option. Valid option values for given familyNamespace
            and familyName are available on the effectivity context associated with product
            Item with relation Fnd0ProductEffConfigCxtRel.
            
            For example, effectivity context with item id EFFCTX001 is associated with product
            Item. It has option families defined with names Maturity Intent and Module Intent.
            Maturity Intent has values Design and Production. Module Intent has values Kit and
            Modkit. The familyNamespace is set as EFFCTX001. The familyName is set Maturity Intent.
            The optionValue can be either Design or Production.
            """

class GetEffectivitiesResponse:
    """
    Holds the Effectivity data associated with the input objects.
    """
    def __init__(self, ) -> None: ...
    EffectivitiesInfo: list[EffectivitiesInfo]
    """A list of effectivities info structures per input object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The service data contains partial errors, if there are any errors during the operation."""

class Effectivity:
    """
    Interface Effectivity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetEffectivities(self, InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> GetEffectivitiesResponse: ...

