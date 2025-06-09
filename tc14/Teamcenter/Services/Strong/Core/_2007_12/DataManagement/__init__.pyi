import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class IdentifierData:
    """
    This structure contains information for Identifier data.
    """
    def __init__(self, ) -> None: ...
    IdentifiableObject: Teamcenter.Soa.Client.Model.ModelObject
    """identifiableObject"""
    AlternateId: str
    """alternateId"""
    AdditionalProps: System.Collections.Hashtable
    """additionalProps"""
    MakeDefault: bool
    """makeDefault"""

class AlternateIdentifiersInput:
    """
    Description of Alternate Identifiers to create.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.IdContext
    """The IdContext to associate with the Alternate ID."""
    IdentifierType: Teamcenter.Soa.Client.Model.Strong.ImanType
    """The Type of Alternate Identifier to create."""
    MainObject: IdentifierData
    """The Item to be associated with the Alternate ID."""
    RevObject: IdentifierData
    """An ItemRevision to associate with the Alternate ID, optional."""

class ContextAndIdentifierTypes:
    """
    This structure contains Context and Identifier Types.
    """
    def __init__(self, ) -> None: ...
    Context: Teamcenter.Soa.Client.Model.Strong.IdContext
    """The IdContext"""
    IdentfierTypes: list[Teamcenter.Soa.Client.Model.Strong.ImanType]
    """The list of ImanTypes that are valid for the IdContext"""

class GetContextAndIdentifiersResponse:
    """
    GetContextAndIdentifierTypes response
    """
    def __init__(self, ) -> None: ...
    ContextAndIdentifierTypesMap: System.Collections.Hashtable
    """
            A map of context and identifier types for each requested ImanType (ImanType/ContextAndIdentifierTypes)
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service data associated with the call"""

class ListAlternateIdDisplayRulesInfo:
    """
    
            Input structure for ListAlternateIdDisplayRules
            operation
            

    """
    def __init__(self, ) -> None: ...
    Users: list[Teamcenter.Soa.Client.Model.Strong.User]
    """A list of users to return display rules for."""
    CurrentUser: bool
    """Flag to indicate display rules for current user."""

class ListAlternateIdDisplayRulesResponse:
    """
    Return structure ListAlternateIdDisplayRules
    """
    def __init__(self, ) -> None: ...
    UserDisplayRuleMaps: System.Collections.Hashtable
    """
            A list of maps of Teamcenter::UserImpl to
            IdDisplayRules.
            
"""
    CurrentRuleInDB: Teamcenter.Soa.Client.Model.Strong.IdDispRule
    """The current rule in the database ( valid for current user only )."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData associated with the call."""

class ValidateAlternateIdInput:
    """
    Input structure representing the alternate id to validate.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Input clientId to help the caller match the
            input to the output and identify error conditions.
            """
    AlternateId: str
    """The Item alternateId to be validated."""
    AlternateRevId: str
    """The ItemRevision alternate id to be validated."""
    PatternName: str
    """
            The name of the pattern for the alternate id. This is passed to the user exit USER_validate_alt_id for validation.
            """
    Context: Teamcenter.Soa.Client.Model.Strong.IdContext
    """The IdContext for the alternate id."""
    IdentifierType: Teamcenter.Soa.Client.Model.Strong.ImanType
    """The ImanType for the Identifier."""

class ValidateAlternateIdOutput:
    """
    This structure contains information for ValidateAlternateIdOutput.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Input clientId to help the caller match the
            input to the output.
            """
    ModifiedAltId: str
    """
            Returned alternate id for the Item. This will be a modified id if the input
            id was invalid.
            """
    ModifiedAltRevId: str
    """
            Returned alternate id for the ItemRevision. This will be a modified id if
            the input id was invalid.
            """
    ValidityId: str
    """
            Status of the validation for the alternate id for the Item. The values can
            be found in Teamcenter::Soa::Core::_2007_12::DataManagement::ValidateIdsStatus
"""
    ValidityRevId: str
    """
            Status of the validation for the alternate id for the ItemRevision. The values
            can be found in Teamcenter::Soa::Core::_2007_12::DataManagement::ValidateIdsStatus
"""

class ValidateAlternateIdResponse:
    """
    
            Return structure containing a list of output corresponding to the input and the ServiceData.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ValidateAlternateIdOutput]
    """List of ValidateAlternateIdOutput."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData will contain the objects
            that are returned by the service call. Any partial errors will be mapped with input
            client id and error message in the ServiceData.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAlternateIdentifiers(self, Input: list[AlternateIdentifiersInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Create new alternate identifiers. Given an IdContext,
             an IdentifierType and an Item ( and
             optionally an ItemRevision ), create an Identifier object to display
             an option part number when the IdContext
             is valid.
             

Use Cases:

             User has a part number for an Item that is used to track the Item.
             The manufacturer of the Item has a different part number. The sales department
             has another part number. The user needs to keep all 3 part numbers with the Item
             and display them at different times. The user can get a list of IdContext and IdentifierTypes
             from the getContextsAndIdentifierTypes operation.
             Using the IdContext and IdentifierType, the client can create an Identifer for
             the Item and ItemRevision to be displayed when the IdContext is valid.
             

Dependencies:

             getContextsAndIdentifierTypes, listAlternateIdDisplayRules
             

Teamcenter Component:

             Identifier - Component to define Identifier and associate it with an Item or Item
             Revision. An identifier can be an Alternate identifier for an object as well as an
             Alias identifier for other objects at the same time.
             
        :param Input: 
                         This data describes the alternate identifiers to create.
             
        :return: ( if requested ) will be in the updatedObjects
             section.. Error messages are returned in the ServiceData as partial errors, this
             service does not have any specific errors, just errors from the sub-system.
        """
        ...
    def ListAlternateIdDisplayRules(self, Input: ListAlternateIdDisplayRulesInfo) -> ListAlternateIdDisplayRulesResponse:
        """    
             Return the current display rule. If the current user flag is set then also return
             the display rules for the current user. If a list of users is supplied, then return
             the display rules for the list of users; otherwise return the display rules for all
             users.
             

Use Cases:

             Return the current display rule in effect and optionally return all the display rules
             for the current user. Also return the display rules for all users or for a list of
             users only.
             

Teamcenter Component:

             Identifier - Component to define Identifier and associate it with an Item or Item
             Revision. An identifier can be an Alternate identifier for an object as well as an
             Alias identifier for other objects at the same time.
             
        :param Input: 
                         A <font face="courier" height="10">ListAlternateIdDisplayRulesInfo</font> data structure.
             
        :return: partial errors. This service throws no specific errors but the subsystem may.
        """
        ...
    def ValidateAlternateIds(self, Inputs: list[ValidateAlternateIdInput]) -> ValidateAlternateIdResponse:
        """    
             Determines if the supplied alternateIds are valid. The USER exit USER_validate_alt_id
             is used for validation. A "modified" alternate id is returned. If the alternate id
             supplied is valid then the modified one returned is the same as the one supplied.
             If the alternate id supplied is not valid, then the one returned is a valid one.
             

Use Cases:

             The user has an alternate id that they wish to use for an object. The alternate id
             is sent to this function to determine if the new alternate id conforms to the rules
             defined by the user.
             

Dependencies:

             getContextsAndIdentifierTypes
             

Teamcenter Component:

             Identifier - Component to define Identifier and associate it with an Item or Item
             Revision. An identifier can be an Alternate identifier for an object as well as an
             Alias identifier for other objects at the same time.
             
        :param Inputs: 
                         A list of <font face="courier" height="10">ValidateAlternateIdInput</font> data structures.
             
        :return: partial errors.
        """
        ...
    def GetContextsAndIdentifierTypes(self, TypeTags: list[Teamcenter.Soa.Client.Model.Strong.ImanType]) -> GetContextAndIdentifiersResponse:
        """    
             Returns the context and identifier types for the supplied identifiable types.
             

Use Cases:

             A user has defined several IdContexts and Idenitfiers in preparation
             for creating AlternateIds. This service returns the current IdContext
             and Identifiers allowing the user to select the appropriate data for AlternateId
             creation.
             

Teamcenter Component:

             Identifier - Component to define Identifier and associate it with an Item or Item
             Revision. An identifier can be an Alternate identifier for an object as well as an
             Alias identifier for other objects at the same time.
             
        :param TypeTags: 
                         A list of <b>ImanType</b> objects.
             
        :return: is invalid. Other error messages are for problems in the subsystem.
        """
        ...

