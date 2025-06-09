import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class AdditionalInfo:
    """
    Structure for additional information.
    """
    def __init__(self, ) -> None: ...
    StrToBooleanVectorMap: System.Collections.Hashtable
    """
            A map (string, list of bool) to capture additional information. The key isConsiderSubHierarchy
            to cancel checkout with or without hierarchy. If false, cancels checkout without
            hierarchy.
            """
    StrToDateVectorMap: System.Collections.Hashtable
    """A map (string, list of date) to capture additional information for future use."""
    StrToDoubleVectorMap: System.Collections.Hashtable
    """A map (string, list of double) to capture additional information for future use."""
    StrToIntegerVectorMap: System.Collections.Hashtable
    """A map (string, list of int) to capture additional information for future use."""
    StrToObjVectorMap: System.Collections.Hashtable
    """
            A map (string, list of BusinessObject) to capture additional information for
            future use.
            """
    StrToStringVectorMap: System.Collections.Hashtable
    """A map (string, list of string) to capture additional information for future use."""

class Core:
    """
    Interface Core
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CancelManufacturingCheckout(self, RootObjects: list[Teamcenter.Soa.Client.Model.ModelObject], AdditionalInfo: AdditionalInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...

