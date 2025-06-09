import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class HigherLevelPkgSKUOutput:
    """
    
            The information about each Higher Level Package SKU object and its Occurrence details
            is provided by way of the HigherLevelPkgSKUOutput data structure.
            
    """
    def __init__(self, ) -> None: ...
    PkgDINumber: str
    """
            Global Trade Identification Number (referred to as Package Device Identifier Number
            on Imd0PackageDI).
            """
    QuantityPerPackage: str
    """Quantity i.e  NNumber of child Packages  of Pmg0HighLevelSKURevision."""
    ContainsDIPackage: str
    """
            Child Pmg0HighLevelSKURevision object's GTIN Number (referred to as Package
            Device Identifier Number on Imd0PackageDI).
            """
    PackageType: str
    """
Pmg0HighLevelSKU object's Package Type (Palette, Shipping Unit, Display Unit
            or a Multi-unit).
            """
    PackageStatus: str
    """
            Current status (In Commercial Distribution or Not In Commercial Distribution) of
            Pmg0HighLevelSKURevision.
            """
    PackageDiscontinueDate: System.DateTime
    """Discontinue Date of Pmg0HighLevelSKURevision."""

class HigherLevelPkgSKUResponse:
    """
    
            The HigherLevelPkgSKUResponse structure represents the list of HigherLevelPkgSKUOutput
            and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[HigherLevelPkgSKUOutput]
    """
            A list of HigherLevelPkgSKUOutput structures. Each entry contains information of
            Higher Level Package SKU.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData structure containing error codes and messages."""

class DIManagement:
    """
    Interface DIManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetHigherLevelPkgSKUInfo(self, Input: Teamcenter.Soa.Client.Model.Strong.Pmg0ItemSKURevision) -> HigherLevelPkgSKUResponse:
        """    
             This service operation returns packaging information of parent Pmg0HighLevelSKURevision
             associated to Pmg0ItemSKURevision.
             

             Use Case:
             

Pmg0ItemSKURevision will be associated to multiple Pmg0HighLevelSKURevision.
             The packaging information of the parent needs to be shown on the child in the format
             as required by various regulatory agencies.
             

Teamcenter Component:

             Medical Device Submissions Template - Solution template that provides capability
             to create and manage UDI data for FDA-US, IMDRF and NMPA-China
             
        :param Input: 
                         The <b>Pmg0ItemSKURevision</b> object used for searching the associated parent <b>Pmg0HighLevelSKURevision</b>.
             
        :return: 
        """
        ...

