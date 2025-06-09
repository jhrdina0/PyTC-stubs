import System
import System.Collections
import Teamcenter.Services.Strong.Core._2008_06.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BulkCreIn:
    """
    Input for bulk create operation including unique client identifier.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """client id Unique client identifier."""
    Quantity: int
    """
            Number of instances of each type for creation.For Asp0Aspect objects,CreateInput needs to be populated with the number
            of Asp0Aspect objects to be created hence quantity should be passed as 1.
            """
    Folder: Teamcenter.Soa.Client.Model.Strong.Folder
    """Containing folder for the newly created items."""
    Data: Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateInput
    """Input data for create operation."""

class ValidationResponse:
    """
    Return structure for createConnections operation
    """
    def __init__(self, ) -> None: ...
    ValidationResult: System.Collections.Hashtable
    """
            A map of type <std::string ,bool> indicating
            if the ID is valid. The key is clientId from CreateIn.
            The value is true if the id is valid, otherwise id is invalid.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data"""

class WhereUsedConfigParameters:
    """
    
            Additional Configuration Parameters required for whereUsed
            search. For example tagMap to specify the
            RevisionRule with revision_rule as a key, boolMap
            to specify whereUsedPreciseFlag with whereUsedPreciseFlag
            as a key, and intMap to specify number of
            levels with numLevels as a key.
            
    """
    def __init__(self, ) -> None: ...
    StringMap: System.Collections.Hashtable
    """String Input parameters ( std::string, std::string )"""
    DoubleMap: System.Collections.Hashtable
    """Double Input parameters ( std::string, double )"""
    IntMap: System.Collections.Hashtable
    """int Input parameters ( std::string, int )"""
    BoolMap: System.Collections.Hashtable
    """bool Input parameters ( std::string, bool )"""
    DateMap: System.Collections.Hashtable
    """Date Input parameters ( std::string, Teamcenter::DateTime )"""
    TagMap: System.Collections.Hashtable
    """
            Object Input parameters   ( std::string, BusinessObjectRef ( Teamcenter::BusinessObject
            ) )
            """
    FloatMap: System.Collections.Hashtable
    """Float Input Parameters ( std::string, float )"""

class WhereUsedInputData:
    """
    
            Input data for whereUsed search contains
            the target object to perform search along with the configuration parameters.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Target object to do whereUsed search"""
    UseLocalParams: bool
    """Flag to decide which config paramerters to be used, local or common"""
    InputParams: WhereUsedConfigParameters
    """
            Additional Configuration Parameters required for whereUsed
            search
            """
    ClientId: str
    """Client ID to uniquely idnetify this input data"""

class WhereUsedOutputData:
    """
    This structure contains output information of Where Used Call.
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Input object"""
    Info: list[WhereUsedParentInfo]
    """List of where used result objects"""
    ClientId: str
    """Client ID of input object which this output object is for"""

class WhereUsedParentInfo:
    """
    Generic Parent Info Structure
    """
    def __init__(self, ) -> None: ...
    ParentObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """Parent Workspace Object"""
    Level: int
    """levet at which parent is found"""

class WhereUsedResponse:
    """
    
WhereUsedResponse object contains list of
            WhereUsedOutputData structure. This structure
            contains list of ItemRevision objects which are result of whereUsed search.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[WhereUsedOutputData]
    """List of WhereUsedOutputData structures"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard ServiceData Member"""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ValidateIdValue(self, Input: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateIn]) -> ValidationResponse:
        """    
             This operation determines if the given MultiFieldKey
             properties are unique based on the MultiFieldKey
             definition.
             

Use Cases:

             Use this operation before creating a new object to validate if the MultiFieldKey property combination is already used.  This is an
             existence check rather than a true validation. It does not validate the property
             values against Naming Rules.
             

Teamcenter Component:

             Core Model Item - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform. This component defines the Item
             Class and behavior.
             
        :param Input: 
                         A list of MultiFieldKey attribute/value pairs for the object to be created
             
        :return: attribute/value pairs
             for the object to be created.
        """
        ...
    def BulkCreateObjects(self, Input: list[BulkCreIn]) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse:
        """    
             This is a generic operation for bulk creation of Business Objects. This will create
             instances of the given quantity of the specified type in their specified containing
             folders. This will also create any secondary(compounded) objects that need to be
             created, assuming the CreateInput for the secondary object is represented in the
             recursive CreateInput object e.g. Item is Primary Object that also creates
             Item Master, ItemRevision and ItemRevision in turn creates ItemRevision
Master. The input for all these levels is passed in through the recursive
             CreateInput object. This operation is applicable for bulk creation of Item,
             Form ,Dataset and Asp0Aspect Types only.
             

Use Cases:

             1. To create large number of objects of specified types namely Item, Dataset
             and Form each of specified quantities and save them through a single transaction
             to significantly reduce the number of sql queries incurred during object creation,
             thus improving object creation performance and making object creation scalable.
             
             2. To create large number of Asp0Aspect objects of specified types and save
             them through a single transaction to significantly reduce the number of sql queries
             incurred during object creation, thus improving object creation performance and making
             object creation scalable.
             

Dependencies:

             createFolders
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param Input: 
                         A vector of <font face="courier" height="10">BulkCreIn</font> structures representing
                         the <font face="courier" height="10">CreateInput</font> for the bulk creation of
                         business objects of the specified quantity for each type.
             
        :return: business objects respectively.
        """
        ...
    def WhereUsed(self, Input: list[WhereUsedInputData], ConfigParams: WhereUsedConfigParameters) -> WhereUsedResponse:
        """    
             The whereUsed service identifies all the
             parent Item and ItemRevision objects in the structure where the input
             Item or ItemRevision is used. User can provide RevisionRule
             to search for specific ItemRevision . By default all ItemRevision objects
             are returned. The number of levels of whereUsed
             search indicates, whether to return one or top or all levels of assemblies. It supports
             whereUsed search on any WorkspaceObject
             which implements the "whereUsed" interface.
             

Use Cases:

             A user performs whereUsed search to find
             all the assemblies that contain a particular Item or ItemRevision.
             User inputs Item or ItemRevision and the search can be made with following
             options:
             

RevisionRule  This can be set to All, displaying all ItemRevision
             objects  that have an occurrence of target ItemRevision. If a specific RevisionRule
             is selected only the ItemRevision objects  configured by the rule are returned
             in the search.
             
Depth up to which numbers of levels are to be returned.
             
Boolean representing whether to only send back precise parents (used
             by ItemRevision specifically and not Item)
             



             Additional Configuration Parameters can be used to do customized whereUsed search.
             WhereUsedConfigParameters has below maps:
             

             stringMap ( std::string, std::string )
             
             doubleMap ( std::string, double )
             
             intMap ( std::string, int )
             
             boolMap ( std::string, bool )
             
             dateMap ( std::string, Teamcenter::DateTime )
             
             tagMap ( std::string, BusinessObjectRef ( Teamcenter::BusinessObject ) )
             
             floatMap ( std::string, float )
             

             COTS whereUsed search uses tagMap to specify
             the RevisionRule with revision_rule as a key, boolMap
             to specify whereUsedPreciseFlag with whereUsedPreciseFlag as a key, and intMap to specify number of levels with numLevels as a key. Similarly
             other maps can be used to pass additional parameters for customized whereUsed search.
             Teamcenter currently don't have any extension where additional Configuration
             Parameters can be considered for whereUsed
             search if passed by user. User can implement "whereUsed" interface on any custom
             WorkspaceObject to consider additional Configuration Parameters for whereUsed search.
             

             The output contains list of  each parent level search result in the structure.
             

Teamcenter Component:

             WhereUsed - Provides where used search capability for Item, ItemRevision, DataSet
             and apperanceGroup objects in the database. User can apply the Rev Rule criteria
             to filter the results for configured results.
             
        :param Input: 
<font face="courier" height="10">WhereUsedInputData</font> object list
             
        :param ConfigParams: 
                         Additional Configuration Parameters if required. For example <font face="courier" height="10">tagMap</font> to specify the <b>RevisionRule</b> with revision_rule as
                         a key, <font face="courier" height="10">boolMap</font> to specify whereUsedPreciseFlag
                         with whereUsedPreciseFlag as a key, and <font face="courier" height="10">intMap</font>
                         tp specify number of levels with numLevels as a key.
             
        :return: 
        """
        ...

