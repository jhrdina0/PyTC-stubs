import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class MoveLineInfo:
    """
    
MoveLineInfo structure represents the parameters
            required to re-sequence the selected Fnd0BuildingBlockBOMLine object
in the
            BOM structure.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    Operation: int
    """
            The operation integer value to decide the operation performed. Following operation
            can be supported by MoveLineInfo.
            

Move Up
            
Move Down
            
Promote
            
Demote
            
Edit Number
            

"""
    SelectedLine: Teamcenter.Soa.Client.Model.Strong.Fnd0BuildingBlockBOMLine
    """The Fnd0BuildingBlockBOMLine object, on which operation will be performed."""
    NewNumber: str
    """
            The new Number property value, will be used when Edit Number operation will be performed.
            Based on new property value selected BOM line will be moved in the BOM structure.
            """

class MoveLineResponse:
    """
    MoveLineResponse structure contains the ServiceData object.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class RequirementsManagement:
    """
    Interface RequirementsManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def MoveLine(self, Input: list[MoveLineInfo]) -> MoveLineResponse:
        """    
             This operation manipulates the BOMLine Structure (Requirement/ Function/
             SEBlock structure) by moving the selected BOMLine object either Upwards,
             Downwards or to a specific position. A Number property will be updated for
             selected Fnd0BuildingBlockBOMLine object along with its children.
             
             Following operation are supported by this service operation.
             

Move Up - To move up the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. For instance, if a requirement structure
             "Req_01", we have two children "SubReq_01" and "SubReq_02". In move up structure
             modification can be done with respect to the parent. Requirements "SubReq_01" and
             "SubReq_02" can be move up in context of parent "Req_01".
             
Move Down - To move down the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. For instance, if a requirement structure
             "Req_01", we have two children "SubReq_01" and "SubReq_02". In move down structure
             modification can be done with respect to the parent. Requirements "SubReq_01" and
             "SubReq_02" can be move down in context of parent "Req_01".
             
Promote - To indent the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. For instance, promote a requirement
             previously occupying level 2, with number "1.1", moves to the level 1, with number
             "2.0". Children previously occupying level 3 with number "1.1.1", moves to the level
             2, with number "2.1".
             
Demote - To out-dent the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. For instance, demote a requirement
             previously occupying level 2, with number "1.0", moves to the level 3, with number
             "1.1.1". Children previously occupying level 3, with number "1.1.1", moves to the
             level 4, with number "1.1.1.1".
             
Edit Number - To move the selected BOM line (Fnd0BuildingBlockBOMLine)
             up in the structure with respect to its sibling. You can able to move selected BOM
             line object from one level to other and from one parent to other parent.  For instance,
             if a requirement has number "1.1.1" which means it is under parent "1.1". If the
             number changed to "1.1.3", the requirement is repositioned under the parent. If the
             number is changed to "2.1", then requirement will be removed from the parent and
             put under the sibling of the parent.
             



Use Cases:

             You can manipulate the hierarchy for a selected Requirement /Function/
             SEBlockBOMLine object by using the moveLine operation. The given Fnd0BuildingBlockBOMLine
             object will be moved as per the choice along with its children and the Number property
             will be updated with new values.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         A list of <font face="courier" height="10">MoveLineInfo</font> structures which hold
                         the required information to move selected <b>Fnd0BuildingBlockBOMLine</b> object
                         along with its sibling.
             
        :return: 
        """
        ...

