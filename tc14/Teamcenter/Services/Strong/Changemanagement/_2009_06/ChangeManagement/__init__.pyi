import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetNoteVariantOutput:
    """
    
GetNoteVariantOutput structure contains object
            references to 1) the BOMEdit, 2) the associated change revision, 3) the solution
            bvr, and 4) the impacted bvr.  It also contains a list of details count and a list
            of strings representing some textual details of the note or variant change.
            
    """
    def __init__(self, ) -> None: ...
    BomChange: Teamcenter.Soa.Client.Model.Strong.BOMEdit
    """An object reference to a BOMEdit"""
    ChangeRev: Teamcenter.Soa.Client.Model.Strong.ChangeItemRevision
    """An object reference to a change revision."""
    SolutionBVR: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    """An object reference to the Solution bvr."""
    ImpactedBVR: Teamcenter.Soa.Client.Model.Strong.PSBOMViewRevision
    """An object reference to the Impacted bvr."""
    VCount: list[int]
    """Count of note or variant change details"""
    VBomChangeDetails: list[str]
    """Note or variant change details."""

class GetNoteVariantResponse:
    """
    
GetNoteVariantResponse structure contains
            a list of GetNoteVariantOutput structures
            and a standard service data.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[GetNoteVariantOutput]
    """A reference to the list of GetNoteVariantOutput"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard Service data."""

class GetNoteVariantsInput:
    """
    
            GetNoteVariantsInput structure contains an object reference to a BOMEdit whose integer
            type is EITHER 6 (=Note Change) OR 7(=Variant Change) and a matching context string.
            
    """
    def __init__(self, ) -> None: ...
    BomChangeNode: Teamcenter.Soa.Client.Model.ModelObject
    """An object reference to a BOMEdit"""
    ContextRelName: str
    """A context string of two possible values: CM_note_change_details or CM_variant_change_details."""

class ChangeManagement:
    """
    Interface ChangeManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetNoteVariantChanges(self, GetNoteVariantRequest: list[GetNoteVariantsInput]) -> GetNoteVariantResponse:
        """    
             This operation is specifically designed to handle the retrieval of information for
             Note or Variant changes to be consumed by the Teamcenter Structure Manager Rich Client
             UI.  There are helper functions in the Rich Client to facilitate the consumption
             and interpretation of the retrieved information.  In other words, this operation
             may pose challenges to users of this operation who are unfamiliar with the intended
             usage of the returned details.  For Rich Client developers, it is better to use the
             helper functions instead.
             
             The operation accepts as input a list of GetNoteVariantsInput
             structures, each containing an object reference to a BOMEdit
             whose integer type is EITHER 6 (=Note Change) OR 7(=Variant Change) and a matching
             context string of one of the following two possible values:
             

CM_note_change_details
             
CM_variant_change_details
             


             Based on the input structures, the operation will assemble the retrieved information
             in a list of GetNoteVariantOutput structures,
             and package them together with a standard service data in the returned GetNoteVariantResponse structure.
             

Use Cases:

Use Case 1: Getting the details for a note change

             This operation can be invoked via an instance of the ChangeManagementService.
             The caller program will need to supply an object reference to a BOMEdit whose integer type is 6 and a matching context string
             of CM_note_change_details in the input structure GetNoteVariantsInput.
             The corresponding output structure GetNoteVariantOutput
             contains object references to 1) the BOMEdit, 2) the associated change revision,
             3) the solution bvr, and 4) the impacted bvr.  It also contains a list of details
             count and a list of strings representing some textual details of the note change.
             The caller program will use the count to read the strings for details.
             
Use Case 2: Getting the details for a variant change

             This operation can be invoked via an instance of the ChangeManagementService.
             The caller program will need to supply an object reference to a BOMEdit whose integer type is 7 and a matching context string
             of CM_variant_change_details in the input structure GetNoteVariantsInput.
             The corresponding output structure GetNoteVariantOutput
             contains object references to 1) the BOMEdit, 2) the associated change revision,
             3) the solution bvr, and 4) the impacted bvr.  It also contains a list of details
             count and a list of strings representing some textual details of the variant change.
             The caller program will use the count to read the strings for details.
             



Teamcenter Component:

             Change Management - This feature provides support for proposing changes to a product
             and managing the entire lifecycle of the changes. With this feature ItemRevision
             objects may be related to ChangeItemRevision objects as Problem, Impacted, or Solution
             items.
             
        :param GetNoteVariantRequest: 

        :return: 
        """
        ...

