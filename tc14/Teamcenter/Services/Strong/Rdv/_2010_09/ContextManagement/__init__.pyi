import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class StructureCntxtObjectInfo:
    """
    This structure contains the information required to create or update the SCO.
    """
    def __init__(self, ) -> None: ...
    PrdItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Product Item Revision used during performing the search."""
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """Revision Rule used during performing the search. For e.g, 'Latest working'."""
    VarRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """Variant Rule set while performing the search."""
    WorkParts: list[Teamcenter.Soa.Client.Model.Strong.Item]
    """List of work parts selected from DesignContext(DC) UserInterface(UI)."""
    TgtBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of all the Target BOMLine objects selected in DC UI."""
    BgdBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """List of Background BOMLine objects returned by the search."""
    SelTgtBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            List of selected Target BOMLine objects used. This is used for storing     the
            selections.
            """
    SelBgdBomLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """
            List of selected Background BOMLine objects. This is used for storing the
            selections.
            """
    TgtSearchCrtGrp: Teamcenter.Soa.Client.Model.Strong.ApprSearchCriteriaGroup
    """Object of Appearance Search Criteria Group for Target."""
    BgdSearchCrtGrp: Teamcenter.Soa.Client.Model.Strong.ApprSearchCriteriaGroup
    """Object of Appearance Search Criteria Group for Background."""

class CreateSCOInputInfo:
    """
    This structure specifies the type, name and description information of a SCO
object.
    """
    def __init__(self, ) -> None: ...
    ScoType: str
    """Type of the Structure Context Object. For e.g. VisStructureContext."""
    ScoName: str
    """Name by which the StructureContext Object will be created."""
    ScoDesc: str
    """Description provided while creating the StructureContext object in DC UI."""
    ScoInfo: StructureCntxtObjectInfo
    """
StructureCntxtObjectInfo object which contains
            all the details related to the search criteria and search results.
            """

class CreateSCOResponse:
    """
    
This structure contains newly created StructureContext object and ServiceData
object
    """
    def __init__(self, ) -> None: ...
    StrCntxtObject: Teamcenter.Soa.Client.Model.Strong.StructureContext
    """
            Object of StructureContext created newly using the values passed in the     input
            parameter. This object encapsulates complete DesignContext session information.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains any
            exceptions if occurred during creation of SCO.
            """

class UpdateSCOInputInfo:
    """
    
This structure contains the StructureContext object and StructureCntxtObjectInfo
object containing information that needs
to be updated.
    """
    def __init__(self, ) -> None: ...
    StrCntxtObject: Teamcenter.Soa.Client.Model.Strong.StructureContext
    """
            Structure Context Object that needs to be updated. This SCO object will be updated
            with the modified values.
            """
    ScoInfo: StructureCntxtObjectInfo
    """
            Object of StructureCntxtObjectInfo structure.
            It internally holds all the details related to the search criteria and search results.
            """

class UpdateSCOResponse:
    """
    
This structure contains the updated StructureContext object and error, if
any, in serviceData object.
    """
    def __init__(self, ) -> None: ...
    StrCntxtObject: Teamcenter.Soa.Client.Model.Strong.StructureContext
    """
            Object of StructureContext updated with the values supplied through the input
            parameter.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any exceptions if occurred during updation of SCOs."""

class ContextManagement:
    """
    Interface ContextManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateSCO(self, Inputs: list[CreateSCOInputInfo]) -> CreateSCOResponse:
        """    
             Creates the Structure Context Object (SCO) based on the inputs supplied. It creates
             an SCO object and then sets the following properties on SCO object created: Product
             Item Revision, Revision Rule, Variant Rule, Work parts selected, Search Criteria
             Group, Target and Background BOMLine objects from the input structure. This
             SCO will contain the Item, Item revisions, Target BOMLine objects, Background
             BOMLine objects. The operation is designed to support multiple SCOs creations
             in a single call. (Limitation: Though this operation can create multiple SCO objects
             however it can return reference of only one object). The operation will initially
             create the SCO object using the name, type and description. Subsequently it would
             set the additional parameters supplied through the input structure. SCO object would
             still be created and saved even if setting of the additional parameters is not successful.
             

Use Cases:

1. Create an SCO

             YouYou can create a new SCO object of type VisStructureContext using createSCO operation by providing the CreateSCOInputInfo structure.
             


Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param Inputs: 
                         An object of <b>StructureContext</b> is created for each <font face="courier" height="10">CreateSCOInputInfo</font>
                         object  in the inputs list. The data in the <font face="courier" height="10">CreateSCOInputInfo</font>
                         like SCO type, name, and description along with search related criteria is used to
                         create object of <b>StructureContext</b>.
             
        :return: 
        """
        ...
    def UpdateSCO(self, Inputs: list[UpdateSCOInputInfo]) -> UpdateSCOResponse:
        """    
             Updates the Structure Context Object (SCO) based on the inputs attributes. It sets
             the following properties on SCO object which is to be modified: Product Item Revision,
             Revision Rule, Variant Rule, Work parts, Search Criteria Group, Target and Background
             BOMLine objects from the input structure. This SCO will contain the Item,
             Item revisions, Target BOMLine objects, Background BOMLine objects.
             The operation is designed to support multiple SCOs creations in a single call. (Limitation:
             Though this operation can update multiple SCO objects however it can return reference
             of only one object). This operation first checks for the local ownership of the object
             to be updated. This operation will fail if null or incorrect reference to existing
             SCO object is passed in the input.
             

Use Cases:

             1. Update an SCO
             
             You can update an SCO object of type VisStructureContext using updateSCO operation by providing the UpdateSCOInputInfo
             structure.
             

Create an SCO, object of StructureContext, using the createSCO operation.
             
Retrieve the reference to StructureContext returned from above
             step.
             
Modify the required search criteria and populate the UpdateSCOInputInfo structure.
             
Call updateSCO which will
             modify the existing StructureContext object.
             



Dependencies:

             createSCO
             

Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param Inputs: 
                         An object of <b>StructureContext</b> is updated for each <font face="courier" height="10">UpdateSCOInputInfo</font>
                         in the inputs list. The data in the <font face="courier" height="10">UpdateSCOInputInfo</font>
                         object is used for updation.
             
        :return: 
        """
        ...

