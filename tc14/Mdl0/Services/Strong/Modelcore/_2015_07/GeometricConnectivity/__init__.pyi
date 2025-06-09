import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GeomConnGroupInfo:
    """
    Specifies the full set of inputs required to create or update the geometric connectivity.
    """
    def __init__(self, ) -> None: ...
    GeomGroup: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup
    """
            Business object reference to geometric connectivity group. If it is null, a geometric
            connectivity group will be created. Otherwise, it will be updated.
            """
    BoType: str
    """
            The business object type of a geometric connectivity group to be created. This value
            is required to create a new geometric connectivity group, and must be a valid subtype
            of Mdl0GeomConnGroup. For update of an existing geometric connectivity group, this
            values should be empty.
            """
    EndObject1: Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement
    """First end positioned model element of the geometric connectivity group."""
    EndObject2: Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement
    """Second end positioend model element of the geometric connectivity group."""
    LogicalId: str
    """ID of the logical connectivity."""
    ConnectionId: str
    """ID of the logical connection."""
    AttrInfo: System.Collections.Hashtable
    """
            A map of (string/list(string)) of name value pairs used to specify additional property
            data for geometric connectivity group. All values are specified as strings, the caller
            is responsible for generating the correct string representation of each value passed.
            For tag values, the UID of the business object is used.
            """

class GeomConnGroupContentInfo:
    """
    
            Specifies the full set of inputs required to add the geometric links to geometric
            connectivity group or remove links from the group.
            
    """
    def __init__(self, ) -> None: ...
    LinksToRemove: list[Teamcenter.Soa.Client.Model.Strong.Mdl0GeomLink]
    """The list of geometric links to be deleted."""
    CreateOrUpdateLinkInfos: list[GeomLinkInfo]
    """The list of geometric links to be created or updated."""

class CreateOrUpdateGeomConnGroupInfo:
    """
    
            Specifies the full set of inputs required to create or update the geometric connectivity
            group and manage its content positioned model elements.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned geometric
            connectivity groups and partial errors associated with this input.
            """
    GeomConnGroupInfo: GeomConnGroupInfo
    """
            A set of information need to create or udpate to geometric connectivity group. If
            it is null, geometric connectivity group will be created. Otherwise, it will be updated.
            """
    GeomConnGroupContentInfo: GeomConnGroupContentInfo
    """
            A set of information used to add and remove contents of geometric connectivity group.
            Also used to mange the connectivity of the contents of the geometric connectivity
            group.
            """

class CreateOrUpdateGeomConnGroupResponse:
    """
    
            This structure is used to return the geometric connectivity group created or updated
            as well as the links created or updated.
            
    """
    def __init__(self, ) -> None: ...
    ClientIdToGroupMap: System.Collections.Hashtable
    """
            A map (string/Mdl0GeomConnGroup) of client id to corresponding geometric connectivity
            group.
            """
    ClientIdToLinkMap: System.Collections.Hashtable
    """A map (string/Mdl0GeomLink) of client id to corresponding geometric link."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains list of added geometric connectivity groups, geometric links and geometric
            group links, updated geometric connectivity groups and geometric links, or deleted
            geoemtric links and geoemtric group links. Also contains list of any errors which
            occurred within the call.
            """

class GeomLinkInfo:
    """
    Specifies the full set of inputs required to create or update the geometric links.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned geometric
            links and partial errors associated with this input.
            """
    Link: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomLink
    """
            Business object reference to geometric link. If it is null, a geometric link will
            be created. Otherwise, it will be updated.
            """
    OwningPME: Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement
    """
            Business object reference to  positioned model element for which the geometric link
            will be created.
            
"""
    AttrInfo: System.Collections.Hashtable
    """
            A map of (string,list(string)) of name value pairs used to specify additional property
            data for geometric links. All values are specified as strings, the caller is responsible
            for generating the correct string representation of each value passed. For tag values,
            the UID of the business object is used.
            """
    ConnectedPME: Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement
    """
            Business object reference to  positioned model element which the owning positioned
            model element will be connected to. This value is ignored when link is not null.
            """

class GetConnectivityContentResponse:
    """
    This structure contains the response for the getConnectivityContents call.
    """
    def __init__(self, ) -> None: ...
    ClientIdToContentMap: System.Collections.Hashtable
    """
            A map (string, list of GroupContentOutput) of clientId to returned list of  returned
            GroupContentOutput.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Added, updated, or deleted objects are not expected. Positioned model elements are
            returned as plain objects. Also contains list of any errors which occurred within
            the call along with the position of the group in input vector.
            """

class GetGroupContentResponse:
    """
    This structure is used to return the geometric connectivity group content.
    """
    def __init__(self, ) -> None: ...
    GroupContentMap: System.Collections.Hashtable
    """
            A map (Mdl0GeomConnGroup/ list of Mdl0PositionedModelElement) of connection group
            to corresponding positioned model elements in it.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Added, updated, or deleted objects are not expected. Positioned Model Elements are
            returned as plain objects. Also contains list of any errors which occurred within
            the call along with the position of the group in input list.
            """

class GroupContentOutput:
    """
    This structure is used to return the geometric connectivity group and its content.
    """
    def __init__(self, ) -> None: ...
    GeomGroup: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup
    """Business object reference to geometric connectivity group."""
    GroupContents: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement]
    """
            Contents of geometric connectivity group. It contains a list of positioned model
            elements.
            """

class QueryInput:
    """
    
            The information about each Saved Query to be processed is provided by ways of this
            data structure.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify GroupContentOutput
            and partial errors associated with this input.
            """
    Query: Teamcenter.Soa.Client.Model.Strong.ImanQuery
    """The saved query object to be executed."""
    Entries: list[str]
    """
            List of names for the criteria. They are User Entry Name of the query seen
            in Query Builder, not User Entry L10N Key. To get User Entry Name in
            different local, use com.teamcenter.rac.kernel.TcTextService.getTextValue() for Teamcenter
            rich client customization, use com.teamcenter.services.strong.core._2008_06.Session.getDisplayStrings()
            for Teamcenter service customization.
            """
    Values: list[str]
    """List of values for the criteria."""
    MaxNumToReturn: int
    """A specified maximum number of matches to return, 0 means no limit."""

class GeometricConnectivity:
    """
    Interface GeometricConnectivity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateGeomConnGroups(self, GroupInfos: list[CreateOrUpdateGeomConnGroupInfo]) -> CreateOrUpdateGeomConnGroupResponse:
        """    
             This operation creates or updates geometric connectivity groups. It also adds and
             removes  positioned model elements to and from the geometric connectivity group.
             
             The geometric connectivity group and positioned model elements need to be locked
             before geometric group links and geometric links are created or updated.
             

Use Cases:

             The use cases are entirely within the domain of CAD tools.
             

Creating and updating geometric connectivity group by CAD.
             
Adding positioned model elements to geometric connectivity group
             by CAD
             
Removing content positioned model elements from geometric connectivity
             group by CAD
             



             Sample client to server interaction:
             

A CAD tool creates a geometric connectivity group, adds a few positioned
             model elements to it and connects them. The CAD tool then calls the operation to
             save the data into Teamcenter.
             
The server returns a newly created geometric connectivity group,
             all the positioned model elements in the group, the geometric links that connect
             the positioned model elements and the member links that connect the positioned model
             elements to the group.
             



Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param GroupInfos: 
                         The set of information needed to create or update the geometric connectivity group.
             
        :return: 
        """
        ...
    def GetConnectivityContents(self, QueryInputs: list[QueryInput], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, LoadOption: str) -> GetConnectivityContentResponse: ...
    def GetConnectivityGroupContents(self, GeomGroups: list[Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> GetGroupContentResponse: ...

