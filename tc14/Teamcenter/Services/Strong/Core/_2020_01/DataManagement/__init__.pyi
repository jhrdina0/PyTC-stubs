import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class IDContextOut:
    """
    
            The IDContextOut is list of  IdContext objects. It also contains the input
            object of type Item or ItemRevision.
            
    """
    def __init__(self, ) -> None: ...
    InputObj: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Input object of type WorkspaceObject or null for which the list of IdContext
            objects are fetched.
            """
    IdContexts: list[Teamcenter.Soa.Client.Model.Strong.IdContext]
    """A list of all IdContext objects found in the Teamcenter database."""

class IDContextOutput:
    """
    
            The IDContextOutput is list of IdContextOut objects. It also contains the instance
            of ServiceData for the operation.
            
    """
    def __init__(self, ) -> None: ...
    IdContextOuts: list[IDContextOut]
    """
            A list of IdContextOut structures which holds the list of IdContext objects
            and input object of type WorkspaceObject or null.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any partial errors encountered during this operation are returned in the list of
            partial errors of the ServiceData.
            """

class IDDispRuleCreateIn:
    """
    
            The IDDispRuleCreateIn structure is used to hold the name of the ID Display Rule,
            list of ID Context objects and a flag whether to set the ID Display Rule being created
            as the default ID Display Rule.
            
    """
    def __init__(self, ) -> None: ...
    RuleName: str
    """Name of the ID Display Rule being created."""
    IdContexts: list[Teamcenter.Soa.Client.Model.Strong.IdContext]
    """
            A list of input IdContext objects to be set with the IdDispRule object
            being created.
            """
    UseDefault: bool
    """
            If true, the created IdDispRule object is set as the default ID Display Rule
            for the user; otherwise, the existing default ID Display Rule will remain the default.
            """
    SetCurrent: bool
    """
            If true, the created IdDispRule object is set as the current ID Display Rule
            for the user; otherwise, the existing current ID Display Rule will remain the current.
            """

class IdentifiersOut:
    """
    
            The IdentifiersOut structure is used to hold the list of Identifier types,
            applicable object of type Item and list of ItemRevision objects, applicable
            for defining the Alternate IDs.
            
    """
    def __init__(self, ) -> None: ...
    InputItemOrRev: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Input Item or ItemRevision object for which the Identifier type is
            being fetched.
            """
    IdentifierTypes: list[Teamcenter.Soa.Client.Model.Strong.ImanType]
    """
            A list of valid Identifier types which can be used to define the Alternate
            and Alias IDs of the input object.
            """
    Item: Teamcenter.Soa.Client.Model.Strong.Item
    """
Item object of the given input ItemRevision for which Alternate IDs
            can be defined.
            """
    Revisions: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """
            A list containing all revisions of the input Item for which Alternate IDs
            can be defined.
            """

class IdentifierTypesIn:
    """
    
            The IdentifierTypesIn structure is used to hold the input Item or ItemRevision
            object and the input IdContext object.
            
    """
    def __init__(self, ) -> None: ...
    InputItemOrRev: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            Input Item or ItemRevision object for which the Identifier type
            is being fetched.
            """
    IdContext: Teamcenter.Soa.Client.Model.Strong.IdContext
    """
            Input IdContext object used to fetch the Identifier type for the input
            Item or ItemRevision from the defined ID Display Rules.
            """

class IdentifierTypesOut:
    """
    
            The IdentifierTypesOut is list of IdentifiersOut objects. It also contains the instance
            of ServiceData for the operation.
            
    """
    def __init__(self, ) -> None: ...
    IdentifiersOutput: list[IdentifiersOut]
    """
            A list of IdentifiersOut structures which holds list of Identifier types,
            object of type Item and list of ItemRevision objects, applicable for
            defining the Alternate IDs.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any partial errors encountered during this operation are returned in the list of
            partial errors of the ServiceData.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateIdDisplayRules(self, IdDispRuleCreIns: list[IDDispRuleCreateIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates the ID Display Rules (IdDispRule) with the input ID
             Context information.
             
             ID Display Rule contains the list of ID Contexts and their order. Based on the order
             of the ID Contexts defined, the system evaluates the display name of the Item
             and ItemRevision from their Alternate IDs.
             

             ID Context (IdContext), represents the context information under which the
             OEM defines the unique IDs of their Item and ItemRevision. This context
             information is used when Teamcenter users define the unique IDs of Item and
             ItemRevision objects.
             

             User can set one of the ID Display Rules as the current ID Display Rule. The current
             ID Display Rule is used to evaluate the display names of the Item and ItemRevision.
             In case the ID Context of the Alternate ID with the Item and ItemRevision
             object does not match with that of the current ID Display Rule then system uses the
             default ID Display Rule to evaluate the display names of Item and ItemRevision
             objects.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param IdDispRuleCreIns: 
                         A list of objects of type IdDispRuleCreateIn. The data on IdDispRuleCreateIn is used
                         to create the <b>IdContextRule</b> objects with input name and ID contexts.
             
        :return: 
        """
        ...
    def GetIdentifierTypes(self, IdentifierTypesIn: list[IdentifierTypesIn]) -> IdentifierTypesOut:
        """    
             This operation fetches the applicable Identifier types for the input objects
             of type Item and/or ItemRevision along with the input IdContext
             object. System queries the ID Context Rules defined in Teamcenter database and retrives
             the Identifier types.
             

             Alternate and Alias IDs are defined in Teamcenter as instances of business object
             of type Identifier. ID Context, of business object type IdContext,
             represents the context information under which the OEM defines the unique IDs of
             their Item and ItemRevision. This context information is used when
             Teamcenter users define the Alternate and Alias IDs of Item and ItemRevision
             objects.
             

             ID Context Rules are defined as instances of business object type IdContextRule
             in Teamcenter database. These rules map the combination of ID Context and the object
             type e.g.  Item or ItemRevision, called Identifiable types, to the
             type of the Identifier applicable in the context.
             

             This operation also returns the other applicable objects for which Alternate IDs
             along with the input objects can be defined. In case of input objects of type Item,
             this operation returns the list of revision objects of the Item, and in case
             of input objects of type ItemRevision, this operation returns the Item
             object as the applicable object for which Alternate IDs can be defined.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param IdentifierTypesIn: 
                         A list of objects of type IdentifierTypesIn. The data on IdentifierTypesIn is used
                         to query <b>Identifer</b> type based on input <b>Item</b> or <b>ItemRevision</b>
                         and <b>IdContext</b>.
             
        :return: 
        """
        ...
    def GetIdContexts(self, InputObjs: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> IDContextOutput:
        """    
             This operation fetches all instances of the ID Context objects (IdContext)
             from the Teamcenter database applicable for the input objects of type Item
             and ItemRevision based on defined ID Context Rules (IdContextRule)
             by the system administrators.
             

             This operation queries ID Context Rule objects and fetches the ID Context objects
             based on the input Item, ItemRevision or null. The input is the identifiable
             type defined on the ID Context Rules. For a null input, it returns the Id Context
             objects where the identifiable type is null.
             
             All ID Context objects from the Teamcenter data base are returned in case input object
             is other than Item, ItemRevision or null. An empty input list would
             also return all ID Context objects from the Teamcenter data base.
             

IdContext objects represents the context information under which the OEM defines
             the unique IDs of their Item and ItemRevision objects. This context
             information is used when Teamcenter users define the unique IDs of Item and
             ItemRevision objects.
             

             Alternate and Alias IDs of Teamcenter are the example of the such unique IDs of Item
             and ItemRevision. Users define Alternate and Alias IDs with the help of the
             ID Context as one of the unique attribute of the ID.
             

Teamcenter Component:

             Core Model General - This component provides a set of generic capabilities that form
             the very core of Teamcenter platform.
             
        :param InputObjs: 
                         A list of objects of type <b>WorkspaceObject</b> or null for which the objects of
                         type <b>IdContext</b> are fetched.
             
        :return: objects found.
        """
        ...

