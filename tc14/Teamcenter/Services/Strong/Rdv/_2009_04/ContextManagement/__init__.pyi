import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetGOPartSolutionsResponse:
    """
    
The GetGOPartSolutionsResponse structure represents output of vector of APN of
line
of usages (part solution), instantiating architecture  bom window and the
service
data.
    """
    def __init__(self, ) -> None: ...
    LouBomLine: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """vector of BOMLine of LOU"""
    ArchBomWindow: Teamcenter.Soa.Client.Model.Strong.BOMWindow
    """Instantiating Architecture Bom window"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """serviceData returned as response for retrieving information on LOU APN"""

class GetPastePrimeInfo:
    """
    
This structure contains the list of the source and target BOMLine objects
and a flag to indicate which attributes needs to be copied from the source
BOMLine
to target BOMLine.
    """
    def __init__(self, ) -> None: ...
    ParentBomLine: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            List of the target Architecture Breakdown or Architecture Breakdown Element BOMLine
            objects.
            
"""
    ComponentBomLine: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            List of the source Architecture Breakdown Element BOMLine objects.
            
"""
    Flag: int
    """
            Flag to decide which attributes need to be copied from the source to the target BOMLine.
            
            If flag value is 1 then only variability will be copied from the source to target
            BOMLine.
            
            If flag value is 2 then variability and NVEs will be copied from the source to target
            BOMLine.
            
            If flag value is 3 then variability, NVEs and part solutions will be copied from
            the source to target BOMLine.
            
"""

class ContextManagement:
    """
    Interface ContextManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPastePrimeAttributes(self, Input: GetPastePrimeInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation pastes source Architecture Breakdown Element (ABE) BOMLine
             to the target Architecture Breakdown (AB) BOMLine. It pastes all the
             parents (up to top level AB) of the source ABE under target AB. This operation also
             copies the variability, Named Variant Expressions (NVEs) and part solutions from
             the source BOMLine to target BOMLine.
             

Use Cases:

             This operation can be used to paste the source Architecture Breakdown Element BOMLine
             to target Architecture Breakdown BOMLine.
             

             Use case 1: Copy variability
             
             User needs to set flag value as 1 in GetPastePrimeInfo structure to copy only the
             variability from the source BOMLine to target BOMLine.
             

             Use case 2: Copy variability and NamedVariantExpressions
             
             User needs to set flag value as 2 in GetPastePrimeInfo structure to copy the variability
             and Named Variant Expressions from the source BOMLine to target BOMLine.
             

             Use case 3: Copy variability, NamedVariantExpressions and part solutions
             
             User needs to set flag value as 3 in GetPastePrimeInfo structure to copy the variability,
             Named Variant Expressions and part solutions from the source BOMLine to target
             BOMLine.
             


Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param Input: 
                         Reference to <font face="courier" height="10">GetPastePrimeInfo</font> object which
                         contains the list of source and target <b>BOMLine</b> and a flag to indicate which
                         attributes needs to be copied from the source <b>BOMLine</b> to target <b>BOMLine</b>.
             
        :return: 
        """
        ...
    def GetAllGOPartSolutions(self, GoBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> GetGOPartSolutionsResponse:
        """    
             Get the required information for display of part solutions of selected GBE and its
             instantiating ABE.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param GoBomLine: 
                         contains selected GBE bomline
             
        :return: Contains vector of APN of line of usages (part solution) and            instantiating
             architecture bom window
        """
        ...

