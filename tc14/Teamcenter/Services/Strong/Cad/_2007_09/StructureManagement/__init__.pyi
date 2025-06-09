import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateVariantCondInput:
    """
    
            Contains the input for create/update variant condition associated with a BOMLine
            object.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created."""
    Operation: str
    """
            Refers to Operation which refers to the operation
            type. Legal values are: Create and Update.
            """
    BomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Refers to BOMLine object on which variant condition has been defined."""
    VariantCondInfo: list[VariantCondInfo]
    """
            Refers to a list of VariantCondInfo struct,
            and contains the information needed to create/update a variant condition.
            """

class VariantCondInfo:
    """
    Contains the information related to classic variant condition.
    """
    def __init__(self, ) -> None: ...
    OptionName: str
    """Refers to the classic variant option name."""
    ItemId: str
    """Refers to item id where classic variant option is defined."""
    JoinOperator: str
    """
            Refers to VariantOperator.  Legal values
            are: AND, OR,
            OPEN_BRACKET and CLOSE_BRACKET.
            """
    CompOperator: str
    """
            Refers to ComparisonOperator.  Legal values
            are: EQ, NEQ,
            LT, GT,
            GTEQ and LTEQ.
            """
    Value: str
    """Refers to classic variant option value."""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateVariantConditions2(self, InputObjects: list[CreateOrUpdateVariantCondInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is to create or update (depending on the Operation) a variantCondition ( which
             is variant expression of type load if) for a BOMLine object.
             

Use Cases:

             This operation will be used when user wants to create a new or update an existing
             classic variant condition for a given BOMLine objects.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param InputObjects: 
                         This has the list of <font face="courier" height="10">CreateOrUpdateVariantCondInput</font>
                         struct, which are used to create a new variant condition or update an existing variant
                         condition.
             
        :return: 
        """
        ...

