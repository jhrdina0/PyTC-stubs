import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class AddInformation:
    """
    
Contains information of the object to be added as a new line. When used by Add
operation,
only one of the item/itemRev, element and line will be used.
    """
    def __init__(self, ) -> None: ...
    Item: Teamcenter.Soa.Client.Model.ModelObject
    """The item to be added. It can be null."""
    ItemRev: Teamcenter.Soa.Client.Model.ModelObject
    """The item revision to be added. It can be null."""
    BomView: Teamcenter.Soa.Client.Model.ModelObject
    """The BOMView object to be added. It can be null."""
    Element: Teamcenter.Soa.Client.Model.ModelObject
    """The General Design Element object to be added. It can be null."""
    Line: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            The BOMLine object to be pasted as new line. It can be ImanItemLine or GDELine. It
            can be null.
            """
    InitialValues: System.Collections.Hashtable
    """
            A map to hold initial values of BOMLine properties. Occurrence type can be specified
            here but will be handled specially if used by Add operation.
            """

class AddParam:
    """
    The input for adding lines.
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """The parent where the objects are added."""
    ToBeAdded: list[AddInformation]
    """The information about the objects to be added."""
    Flags: int
    """
            A  bit map of the flags. The lowest bit is reserved for as substitute. If the bit
            is 1, it means the operation will add the object as substitute, otherwise it as normal
            line. The second lowest bit is for propagating transform matrix, when specified as
            1, transform matrix will be propagated from source line to the new line. The third
            lowest bit is used for pending cut lines. If set, the line will be removed after
            being copied.  Other bits are not used.
            """

class AddResponse:
    """
    The response for add operation
    """
    def __init__(self, ) -> None: ...
    AddedLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]
    """The added lines."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The serviceData object that contains partial errors."""

class ParentChildPair:
    """
    Structure of a pair of parent and child objects for occurrence condition
validation.
    """
    def __init__(self, ) -> None: ...
    Parent: Teamcenter.Soa.Client.Model.ModelObject
    """The parent ItemRevision object where to add the child"""
    Child: Teamcenter.Soa.Client.Model.ModelObject
    """The child ItemRevision or GeneralDesignElement object to be added"""

class Structure:
    """
    Interface Structure
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def Add(self, Input: list[AddParam]) -> AddResponse:
        """    
             The operation adds business objects as child lines or substitutes of the specified
             lines with option to propagate transform matrix. .  The business objects can be item,
             item revision, General Design Elements, ImanItemLines or GDELines . If the business
             object to be added is a pending cut line, then the pending cut line will be processed
             after it is added. . If the business object is a WorkArea object or a line of WorkArea
             object and the object is to be added to WorkArea structure, then it will be added
             with predecessor relation. . If the object to be added is a line that contains Incremental
             Change Elements, the elements will be carried over to the newly created line. . BOMLine
             property values can be specified for the new line. . Occurrence type can be specified
             for the newline as one BOMLine property but will be handled specially.
             

Use Cases:


User  wants to add an item to a line. He/she invokes the operation
             to add it with initial values for find  number, quantity, etc. The line will be created
             with the initial BOMLine properties.
             
User wants to add an item revision as a substitute of a precise line.
             He/she invokes the operation to add it.
             
User invokes the operation to copy and paste a line. The Incremental
             Change Elements are carried over to the new line.
             
User invokes the operation to cut and paste a GDE line.
             
User paste a WorkArea object to a WorkArea structure, the newly added
             line is also added with the predecessor relationship.
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The input for the operation which contains the parent where the objects are to be
                         added, the objects to be added, initial property values, options of the operation.
             
        :return: Created lines and service data that contains partial errors.
        """
        ...
    def ValidateParentChildConditions(self, Input: list[ParentChildPair]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation is to validate parent and child objects against occurrence conditions.
             

Use Cases:

             User invokes the operation to validate against occurrence conditions before creating
             two occurrences by using an ItemRevision as parent for the two occurrences
             and a General Design Element object as one child and another ItemRevision
             as another child.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The parent child pairs to validate occurrence conditions
             
        :return: 
        """
        ...
    def ValidateOccurrenceConditions(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Flag: int) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation is to validate occurrences of specified lines and their substitutes
             against occurrence conditions with option to validate the whole substructure.
             

Use Cases:

             User imports a structure which has some substitutes and wants to validate the structure
             against occurrence conditions.  Invoke the operation by passing in the root line
             and the flag for recursive validation. Failed BOMLine validations are returned
             in the ServiceData object.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Lines: 
                         The <b>BOMLine</b> that the validation will be performed.
             
        :param Flag: 
                         Note: when doing recursive validation, it will not load unloaded children.
             
        :return: 
        """
        ...

