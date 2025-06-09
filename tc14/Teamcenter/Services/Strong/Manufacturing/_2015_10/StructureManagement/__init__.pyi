import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CloningStructsInfo:
    """
    
Contains BOMLine objects which are to be cloned in CPC along with additional
cloning
information.
    """
    def __init__(self, ) -> None: ...
    NewName: str
    """The name of new structure to be created as a cloned structure in CPC."""
    NewDescription: str
    """The description of new structure to be created as a cloned structure in CPC."""
    NewId: str
    """ID of new structure to be created as a cloned structure in CPC."""
    NewRevId: str
    """The revision ID of new structure to be created as a cloned structure in CPC."""
    Scopes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of  BOMLine objects to be cloned in CPC. It can be either root BOMLine or
            multiple BOMLine objects within the same structure.
            """
    CloningRule: str
    """
            The rule used for cloning. The value varies based on the structure type which is
            getting cloned. For example, the acceptable value for Mfg0MEPlantBOP is  "ProjectPlantBOPTemplate".
            """
    CloningParams: System.Collections.Hashtable
    """
            A map (string, string) containing cloning parameter as key and its flag as the value,
            such as  ("CPC_carryOverICs","true") for carry over Increamental Changes. Other cloning
            parameters are "CPC_cloneSupressLine" and "CPC_createDIPA" for clone suppressed lines
            and create Dynamic In-Process Assembly (DIPA) respectively.
            """

class EffectivityInfoInput:
    """
    The information required to set effectivity for a list of cloned BOMLine
objects.
    """
    def __init__(self, ) -> None: ...
    EndItem: Teamcenter.Soa.Client.Model.Strong.Item
    """Effectivity end Item."""
    EndItemRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Effectivity end ItemRevision."""
    UnitRangeText: str
    """
            Effectivity unit range, for example "5-10". Multiple range can also be provided,
            for example "3,5-10,20-50". This range belongs to the end Item which is part of the
            structrue on which the unit effectivity is applied.
            
            Valid unit ranges are:
            
            -StartUnit
            
            -StartUnit - EndUnit
            
            -StartUnit - SO
            
            -StartUnit - UP
            
            where, StartUnit <= EndUnit
            
            -StartUnit1 - EndUnit1, StartUnit2 - EndUnit2(Ex: 10 - 12, 15, 16 - UP)
            
            where StartUnit2 > EndUnit1.
            
            - All units are positive integers
            

            For example, the effectivity can be 3 - 5 where 3 is start unit and 5 is end unit.
            
            It can also be 3 - UP where 3 is start unit and "UP" means anything above the start
            unit. "UP" and "SO" indicates open ended effectivity.  "SO" is stock out means effectivity
            will be applicable till the stock out condition.
            """
    DateRange: list[System.DateTime]
    """
            The list of effectivity date range. For instance, opened date range could be specified
            as "05 Jan - UP" and closed date range as "01 Jan - 03 Apr". The list may have any
            number of opened and closed date range. For example, If you select multiple dates
            such as start date 19th May 2015 and End date 22nd May 2015 , start date 19th June
            2015 and end date 22nd June 2015, the dataRange list have 4 values as below : 2015-02-19,
            2015-05-22, 2015-06-19,2015-06-22.
            """
    OpenEndedStatus: int
    """
            Effectivity open ended status.
            
            - 0 : for closed unit range effectivity or date effectivity.
            
            - 1 : for opened unit range effectivity or date effectivity (UP).
            
            - 2 : for opened unit range effectivity or date effectivity stock out (SO).
            
            For example, if you select open ended effectivity such as start date 19th May 2015
            and end date "UP", the dateRange list has 2015-05-19 with "openEndedStatus" value
            as "1".
            """

class CreateCPCInputInfo:
    """
    
A list of BOMLine objects  that are to be cloned and\or referred, cloning
information,
name and description of new CPC.
    """
    def __init__(self, ) -> None: ...
    CloningStructsInfo: list[CloningStructsInfo]
    """
            A list of CloningStructureInfo which contains BOMLine objects which are to be cloned
            in CPC. The structure contains additional cloning information as well.
            """
    ReleaseStatus: str
    """
            The release status which gets associated with line(s) in the cloned structure. If
            the line(s) doesn't have any release status in the original structure. It is configurable
            but in this version only acceptable value is "Alternate Planning Initial".
            """
    EffectivityInfo: EffectivityInfoInput
    """The information required to set effectivity for a list of cloned BOMLine objects."""
    OriginalCCUid: Teamcenter.Soa.Client.Model.ModelObject
    """The UID of the MECollaborationContext from which CPC is to be created."""
    CpcName: str
    """Name of the CPC to be created."""
    CpcDesc: str
    """Description of the CPC to be created."""
    RefStructures: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of  BOMLine objects from the original CC that are going to be referred in the
            CPC.
            """

class CreateCPCResponse:
    """
    Contains newly created CPC data.
    """
    def __init__(self, ) -> None: ...
    CpcObject: Teamcenter.Soa.Client.Model.ModelObject
    """The created CPC object."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateCollabPlanningContext(self, CpcInput: CreateCPCInputInfo) -> CreateCPCResponse:
        """    
             This service operation creates a Collaboration Planning Context (CPC) with the given
             input  structures that are to be cloned and/or referred to, and establishes a relation
             between input MECollaborationContext (CC) object and newly created CPC.
             
             CPC is a CC object itself, it is a term used for mix production.
             

Use Cases:

             A user creates a CPC object in Manufacturing Process Planner (MPP) application using
             an existing opened CC structure. Subsequently a relation Mfg0MEAlternatePlanningRel
             is created between newly created CPC and the orginal CC.
             

             Use Case 1: The user opens a CC structure, select some structures available in the
             CC and creates a CPC.
             

             Use Case 2: A user opens a CC structure, select some of the scopes in that structure
             and create a CPC.
             

             Use Case 3: A user opens a CC structure, select some structures/scopes, provide whether
             they need to be referred or cloned and provide cloning parameters such as Clone Suppressed
             Lines, Carry Over ICs etc. to create a CPC.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param CpcInput: 
                         The input to the service is a structure which contains a list of BOMLine objects
                         that are to be cloned and\or referred, cloning information, name and description
                         of new CPC.
             
        :return: 
        """
        ...

