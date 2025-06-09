import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class CreateInput:
    """
    
            CreateInput structure used to capture the inputs required for creation of a business
            object. This is a recursive structure containing the CreateInput(s) for any secondary
            (compounded) objects that might be created (e.g Item also creates ItemRevision and
            ItemMasterForm, etc.)
            
    """
    def __init__(self, ) -> None: ...
    Type: str
    """Business Object type name"""
    StringProps: System.Collections.Hashtable
    """Map containing string property values"""
    StringArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    DoubleProps: System.Collections.Hashtable
    """Map containing string property values"""
    DoubleArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    FloatProps: System.Collections.Hashtable
    """Map containing string property values"""
    FloatArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    IntProps: System.Collections.Hashtable
    """Map containing string property values"""
    IntArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    BoolProps: System.Collections.Hashtable
    """Map containing string property values"""
    BoolArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    DateProps: System.Collections.Hashtable
    """Map containing DateTime property values"""
    DateArrayProps: System.Collections.Hashtable
    """Map containing DateTime array property values"""
    TagProps: System.Collections.Hashtable
    """Map containing string property values"""
    TagArrayProps: System.Collections.Hashtable
    """Map containing string array property values"""
    CompoundCreateInput: System.Collections.Hashtable
    """CreateInput for compounded objects"""

class CreateIn:
    """
    Input for create operation including unique client identifier
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    Context: Teamcenter.Soa.Client.Model.ModelObject
    """The context for the new created object"""
    Target: Teamcenter.Soa.Client.Model.ModelObject
    """The target  to connect to"""
    RelationName: str
    """
            The name of the relation to use to connect to the target. If the string is empty
            then the relation defined as default will be used.
            """
    Data: CreateInput
    """Input data for create operation"""

class CreateOut:
    """
    Output for create operation including unique client identifier
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Vector of tags representing objects that were created"""

class CreateResponse:
    """
    Response object for create operation
    """
    def __init__(self, ) -> None: ...
    Output: list[CreateOut]
    """Vector of output objects representing objects that were created"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data including partial errors that are mapped to the client id"""

class DisconnectInput:
    """
    Input for disconnect operation
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Unique client identifier"""
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The object to disconnect"""
    DisconnectFrom: Teamcenter.Soa.Client.Model.ModelObject
    """The object to disconnect from"""
    RelationName: str
    """The relation to disconnect in case 2 objects are connected by more than one relation"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateObjects(self, Input: list[CreateIn]) -> CreateResponse:
        """    
             Generic operation for creation of manufacturing objects. This will also create any
             secondary(compounded) objects that need to be created, assuming the CreateInput for
             the secondary object is represented in the recursive CreateInput object e.g. Item
             is Primary Object that also creates ItemMasterForm, ItemRevision and ItemRevision
             in turn creates ItemRevisionMasterForm. The input for all these levels is passed
             in through the recursive CreateInput object. This operation creates the persistent
             objects and the runtime objects accordingly. This operation also connects the created
             objects to the specified target. The connection will be done by the relation defined
             as default.
             
        :param Input: 
                         a list of CreateIn objects representing the Create Input for Business Objects to
                         be created
             
        :return: Contains a list of tags representing the objects that were created. Any failure will
             be returned with client id mapped to error message in the ServiceData list of partial
             errors.
        """
        ...
    def DisconnectObjects(self, Input: list[DisconnectInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Generic operation to disconnect objects.
        :param Input: 
                         A list of disconnectInput objects for the objects to disconnect
             
        :return: Any failure will be returned with client id mapped to error message in the ServiceData
             list of partial errors.
        """
        ...

