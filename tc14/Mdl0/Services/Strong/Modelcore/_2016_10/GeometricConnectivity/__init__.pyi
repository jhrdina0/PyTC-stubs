import Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity
import System
import System.Collections
import Teamcenter.Soa.Client.Model.Strong
import typing

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
    GeomConnGroupInfo: Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.GeomConnGroupInfo
    """
            A set of information need to create or udpate to geometric connecvitiy group . If
            null, geometric connecvitiy group will be created. Otherwise, it will be updated.
            """
    GeomConnGroupContentInfo: GeomConnGroupContentInfo
    """
            A set of information used to add and remove contents of geometric connecvitiy group.
            Also used to mange the connectivity of the contents of the geometric connectivity
            group.
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
            A map of (string/list(string)) of name value pairs used to specify additional property
            data for geometric connectivity group. All values are specified as strings, the caller
            is responsible for generating the correct string representation of each value passed.
            For tag values, the UID of the business object is used.
            """
    ConnectedPME: Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement
    """
            Business object reference to  positioned model element which the owning positioned
            model element will be connected to. This value is ignored when link is not null.
            """
    OtherHalfLinkClientId: str
    """
            This string specifies the matching geom-link-info in GeomConnGroupContentInfo:: createOrUpdateLinkInfos
            vector. This is used when same pair of Positioned Model Elements are being connected
            multiple times. For instance, 2 different pairs of ports on the Positioned Model
            Elements are being connected. Optional if the Positioned Model Element is being added
            to the Group without a connected Positioned Model Element.
            """

class GeometricConnectivity:
    """
    Interface GeometricConnectivity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateGeomConnGroups(self, GroupInfos: list[CreateOrUpdateGeomConnGroupInfo]) -> Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.CreateOrUpdateGeomConnGroupResponse:
        """    
             This operation creates or updates geometric connectivity groups. It also adds and
             removes positioned model elements to and from the geometric connectivity group.
             
             NOTE: This operation deprecates _2015_07 version of createOrUpdateGeomConnGroups
             operation.
             
             With 2015_07 version, only one pair of geometric links can be created between a given
             pair of positioned model elements. However, it is possible that there can be multiple
             links between the same pair of positioned model elements - particularly in electrical
             circuits. 2016_10 version of this operation, createOrUpdateGeomConnGroups2, supports
             creating multiple links between the same pair of positioned model elements.
             

Use Cases:

             The use cases are entirely within the domain of CAD tools.
             

Creating and updating geometric connectivity group by CAD.
             
Adding positioned model elements to geometric connectivity group
             by CAD.
             
Removing content positioned model elements from geometric connectivity
             group by CAD.
             



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

