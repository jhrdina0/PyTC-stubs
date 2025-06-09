import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2008_06.StructureManagement
import typing

class ExpandPSOneLevelPref:
    """
    
            Contains a list of filtering criteria (RelationAndTypesFilter) used in a product
            structure expand operation.
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """
            Flag if true, returns related object(s); otherwise returns all the child BOMLine
            objects.
            """
    Info: list[Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.RelationAndTypesFilter]
    """
            List of the relation name and the related object types to return along with the children.
            If no RelationAndTypesFilter is supplied (info is empty), and expItemRev is true,
            then all related object types are to be accepted.
            """
    IncludeOccurrenceTypes: list[str]
    """
            A list of Occurrence Types that needs to be included when the expansion of the BOM
            takes place. Either specify includeOccurrenceTypes or excludeOccurrenceTypes cannot
            have both. If both arguments are specified, only includeOccurrenceTypes is honoured.
            """
    ExcludeOccurrenceTypes: list[str]
    """
            List of Occurrence Types that needs to be excluded when the expansion of the BOM
            takes place.
            """
    ExpandSettings: System.Collections.Hashtable
    """A map (string ,list of strings)options to apply to the expansion."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExpandPSOneLevel2(self, Info: Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelInfo, Prefs: ExpandPSOneLevelPref) -> Teamcenter.Services.Strong.Cad._2008_06.StructureManagement.ExpandPSOneLevelResponse2: ...

