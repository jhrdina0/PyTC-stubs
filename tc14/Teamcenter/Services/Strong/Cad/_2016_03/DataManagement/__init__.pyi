import System
import System.Collections
import Teamcenter.Services.Strong.Cad._2008_06.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateOrUpdateModelViewProxiesResponse:
    """
    
            The response contains a map of input caller specified client ID values and the corresponding
            objects that were created or updated. The service data contains a list of added,
            updated, or deleted objects and it also contains a list of any errors which occurred
            within the call.
            
    """
    def __init__(self, ) -> None: ...
    ClientIDMap: System.Collections.Hashtable
    """
            Map (string, Fnd0ModelViewProxy) of the various input client IDs to corresponding
            objects (Fnd0ModelViewProxy) that were created.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains a list of added, updated, or deleted objects.  Also contains list of any
            errors which occurred within the call.
            """

class CreateOrUpdateMVPaletteResponse:
    """
    
            The response contains a map of input caller specified clientId
            values and the corresponding objects that were created or updated. The service data
            contains a list of added, updated, or deleted objects and it also contains a list
            of any errors which occurred within the call.
            
    """
    def __init__(self, ) -> None: ...
    ClientIDMap: System.Collections.Hashtable
    """
            Map(string, Fnd0ModelViewPalette or Fnd0ModelViewGroup) of the various
            input clientId to corresponding objects (Fnd0ModelViewPalette
            or Fnd0ModelViewGroup) that were created. Any input Info structures for which
            a clientId wasn't provided will not have
            objects populated here but only within the serviceData.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains a list of added, updated, or deleted objects.  Also contains list of any
            errors which occurred within the call.
            """

class GroupInfo:
    """
    
            A Model View Group to create or update and what Model View Proxies should be disclosed
            for that Group. It also allows each Group to be sequenced among the other Groups
            in the Palette.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended.  It is used for mapping server
            errors and for correlating data in the response to the inputs.  The caller should
            populate a clientId for each GroupInfo with a value that is unique within the entire operation
            inputs.   The value is not interpreted or manipulated internally by the server
            """
    BoType: str
    """
            The type of group to create. Optional. If provided, must be a "Fnd0ModelViewGroup"
            or a valid sub-type of Fnd0ModelViewGroup. If not provided, "Fnd0ModelViewGroup"
            will be assumed as the type of the group to create.
            """
    ModelViewGroupForUpdate: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Existing Model View Group (Fnd0ModelViewGroup or sub-type only) to be updated. If
            not given, a new Model View Group will be created and linked to the Model View Palette
            which was given as a Palette to create or update in the parent ModelViewPaletteInfo input.
            """
    AttrListForGroup: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.AttributeInfo]
    """
            A list of name-value pairs (string, list of strings) used to specify additional property
            data for the Model View Group.  All values are specified as strings, the caller is
            responsible for generating the correct string representation of each value passed.
            For business objects use the UID value of the object.
            """
    ProxiesInGroup: list[Teamcenter.Soa.Client.Model.Strong.Fnd0ModelViewProxy]
    """
            An ordered list of Model View Proxies for the Group to contain. This is a complete
            list for this Model View Group.
            """
    NewOrderSequenceNumber: list[int]
    """
            Optional hint for ordering Groups when not all Groups of a Palette are given. A 0
            newOrderSequenceNumber means to leave the
            Group in its current sequence order. Other valid sequence values are 1 through the
            new total number of Group objects (e.g. the number of Groups after all Group creates
            and deletes for this Palette are completed.) If newOrderSequenceNumber
            is 0 and this Group is newly created then it will be placed at the end of the existing
            Groups. No particular order is enforced among such zero-sequenced newly created Groups.
            """

class ModelViewPaletteInfo:
    """
    
ModelViewPaletteInfo is used as input for
            creating, updating or deleting Model View Palette (Fnd0ModelViewPalette) and
            Model View Group (Fnd0ModelViewGroup) objects.  During update, boType is left empty and the Model View Palette to update is given.
            Create or delete of a Model View Palette requires the user to have write access to
            the given disclosure. Update of an existing
            Palette will only check write permission of the Palette itself.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended.  It is used for mapping server
            errors and for correlating data in the response to the inputs.  The caller should
            populate a clientId for each ModelViewPaletteInfo with a value that is unique within the input
            set and all input GroupInfo for any input
            ModelViewPaletteInfo. The value is not interpreted
            or manipulated internally by the server.
            """
    Disclosure: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The disclosure object (ItemRevision or Cpd0Workset) for which a Model
            View Palette is to be created, updated, or deleted. A value is optional. If not provided,
            any new Model View Palettes created will not be linked to any disclosure.
            """
    BoType: str
    """
            The business object type of a Model View Palette to be created. This value is optional
            for creating a new Model View Palette, and if provided must be Fnd0ModelViewPalette
            or a valid subtype of Fnd0ModelViewPalette. If no value is provided and no
            paletteToUpdate is provided, then the boType default value used is, "Fnd0ModelViewPalette."
            To update an existing Model View Palette, this value may be empty.
            """
    PaletteToUpdate: Teamcenter.Soa.Client.Model.Strong.Fnd0ModelViewPalette
    """Required if an existing Palette (Fnd0ModelViewPalette) is being updated."""
    AttrListForPalette: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.AttributeInfo]
    """
            A list of name-value pairs (string, list of strings) used to specify additional property
            data for the Model View Palette.  All values are specified as strings, the caller
            is responsible for generating the correct string representation of each value passed.
            For business object, use the UID value of the object.
            """
    GroupsAndProxies: list[GroupInfo]
    """
            Details for new and existing Model View Groups (Fnd0ModelViewGroup) and their
            ordering and content.
            """
    PaletteIsComplete: bool
    """
            If true, the existing list of Group objects (Fnd0ModelViewGroup) will be entirely
            replaced by the input Groups (within groupsAndProxies)
            and existing Groups in the Palette that are not in the groupsAndProxies
            content will be deleted (but not their Proxies). And if true, groupsToDelete is ignored. If false, groups not in the groupsAndProxies content are ignored, barring side-effects of
            requested re-ordering of Groups (see newOrderSequenceNumber
            in groupsAndProxies).
            """
    GroupsToDelete: list[Teamcenter.Soa.Client.Model.Strong.POM_object]
    """
            A list of Fnd0ModelViewGroup objects to delete and remove from the complete
            Palette (optional). List is ignored if paletteIsComplete
            is true.
            """
    DeletePalette: bool
    """
            If true, specifies that the existing Model View Palette (Fnd0ModelViewPalette)
            in paletteToUpdate should be deleted if possible.
            For update of an existing Model View Palette or creation of a new Palette, this value
            should be left at a default of false. All Model View Groups (Fnd0ModelViewGroup)
            objects in the deleted Palette will also be deleted but Proxies (Fnd0ModelViewProxy)
            referenced by the Model View Groups will be untouched.
            """

class ModelViewProxyInfo:
    """
    
            An input for creating, updating or deleting model view proxy objects.  When creating
            a new model view proxy(Fnd0ModelViewProxy), the caller must specify the business
            object type (boType) of the new model view
            proxy.  During update, boType is left empty
            and a reference to the model view proxy (modelView)
            to be updated is specified.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The use of this value is optional, but recommended.  It is used for mapping server
            errors and for correlating data in the response to the inputs.  The caller should
            populate a clientId for each ModelViewProxyInfo
            with a value that is unique within the input set.   The value is not interpreted
            or manipulated internally by the server.
            """
    ModelView: Teamcenter.Soa.Client.Model.Strong.Fnd0ModelViewProxy
    """
            The Fnd0ModelViewProxy to be updated.  A value is required for update or delete
            action cases, otherwise (create case) this value should be empty.
            """
    BoType: str
    """
            The business object type (its internal string name) of a model view proxy to be created.
            This value is optional for creating a new model view proxy, and must be a Fnd0ModelViewProxy
            or subtype.  If no value is provided but also no modelView is provided, then the
            boType default value will be set to "Fnd0ModelViewProxy".  For update of an existing
            model view proxy, this value may be empty.
            """
    DeleteProxy: bool
    """
            If true, specifies that this existing proxy should be deleted if possible. For update
            of an existing model view proxy or create of a new proxy, this value should be left
            at a default of false.
            """
    OwningModel: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The owning object which manages the actual CAD model view for which the proxy is
            being created. This owning object will also control the lifecycle of the new proxy
            object. Required for creating a new model view proxy.  If an existing model view
            proxy is being updated, then this value may be empty.
            """
    AttrList: list[Teamcenter.Services.Strong.Cad._2008_06.DataManagement.AttributeInfo]
    """
            A list of name-value pairs (string, list of strings) used to specify additional property
            data for model view proxies.  All values are specified as strings, the caller is
            responsible for generating the correct string representation of each value passed.
            For business object values, the UID of the object is used.
            """
    ThumbnailFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    """
            The File to associate with the model view proxy to give a thumbnail of the
            model view. Value can be null.
            """
    HiresImageFile: Teamcenter.Soa.Client.Model.Strong.ImanFile
    """
            The File to associate with the model view proxy to give a higher resolution
            (versus the thumbnail) image of the model view. Value can be null.
            """
    GuardObjLastModifiedDate: bool
    """
            If true, causes the update or delete of a model view proxy to check the proxy's last
            modified date to avoid data overwrite.
            """
    ObjLastModifiedDateGuard: System.DateTime
    """
            Modification date guard is used if guardObjLastModifiedDate
            is set to true. Object update or delete will abort if the last modified date of the
            object is greater than objLastModifiedDateGuard.
            """

class OwningModelAndCadLmd:
    """
    
OwningModelAndCadLmd is used to identify when the CAD model views have last
            been modified. For each owning model object being passed in a OwningModelAndCadLmd
            input, all the owned model view proxies should be have their CAD last modified date
            synchronized to this date which is being provided.
            
    """
    def __init__(self, ) -> None: ...
    OwningModel: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject
    """
            The owning object which manages the actual CAD  model views which have a new date
            time. Required.
            """
    CadLastModifiedDate: System.DateTime
    """
            The date time at which at least some CAD model views have been most recently updated,
            and hence the date time to which the associated proxy objects should have their CAD
            last modified date set. Required.
            """
    OwningDataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The owning dataset which manages the actual CAD  model views which have a new date
            time. Optional.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateModelViewPalette(self, MvPaletteInfo: list[ModelViewPaletteInfo]) -> CreateOrUpdateMVPaletteResponse:
        """    
             Creates, updates or deletes a model view palette (Fnd0ModelViewPalette) object
             and its groups. The model view palette supports Visualization tools in creating and
             managing model view groups (Fnd0ModelViewGroup) during creation of a Disclosure
             object (an Item or Workset that discloses installation assembly designs). The disclosed
             model view proxy objects may be grouped by this operation.
             
             Using this API, applications can create and update a list of objects in bulk. Providing
             better context and fewer calls from the CAD clients than otherwise would be achieved
             using standard object create and update service operations.
             

Use Cases:

             This API supports the following use cases
             

Use Case 1: Creation of Model View Palette and Model View Groups for a Design
             Disclosure


             The operation can be used for supporting creation of a disclosure object. The disclosure
             object will most commonly be a Workset (Cpd0Workset subtype) but may also
             be a specific type of ItemRevision. The actual disclosure object may be pre-existing
             but would not be acting as a disclosure until this operation creates and attaches
             the desired list of disclosed Model View Proxy references.
             

             The purpose of a design disclosure is to act as a 3D equivalent of a 2D drawing of
             individual installation assemblies (IA.) This disclosure object will collect all
             geometry needed to show both the IA and its assembly PMI. After the various PMI and
             Model Views within the disclosure have been created, they must be "disclosed".
             

             To be considered as disclosed by a disclosure object, a Model View Proxy must be
             referenced by a Model View Group (Fnd0ModelViewGroup)that is referenced by
             a Model View Palette (Fnd0ModelViewPalette) that is associated to the disclosure
             object.
             

             The paletteIsComplete input must be set to
             true for creation of a Model View Palette, as it makes no sense to be false.
             

Use Case 2: Update of Model View Palette and Model View Groups for a Design Disclosure

             If groupsToDelete is set then see Use case
             3 for details, else if paletteIsComplete
             is set to true, then the system will:
             
             1) Process groupsAndProxies, creating or
             updating various Groups.
             
             2) Check the existing Group list on the Palette to determine if any existing Groups
             in the current Palette list are not in the input groupsAndProxies
             input. If so, then set aside such existing Groups for deletion.
             
             3) Set the list of existing and newly created Groups (from step 1 above) onto the
             Palette.
             
             4) Now delete the now unreferenced Groups (from step 2) if any.
             

             If paletteIsComplete is set to false, the system will:
             
             1) process groupsAndProxies, creating or updating various Groups.
             
             2) Again, if groupsToDelete is set then see Use case 3 for details. This must be
             done before re-ordering the Palette's sequence of Groups in order for the input sequence
             order values to be understood correctly by the system.
             
             3) Set the list of existing and newly created Groups (from step 1 above) onto the
             Palette list of Groups (using any specified newOrderSequenceNumber if one was given.
             If any newOrderSequenceNumber is within the range of existing Groups, and that existing
             Group is not in the groupsAndProxies being given a new sequence number, then the
             existing group being replaced in that sequence number will be set aside to be placed
             at the end of the sequence.
             
             4) Now place any set-aside (due to be pushed out of place or being given a sequence
             value of 0) Groups at the end of the Palette's list of Groups.
             


             Use Case 3: Delete of existing Model View Palette and/or specific Groups within the
             Palette
             

             To delete an entire Palette and all its Groups, the caller will simply send both
             the disclosure and the deletePalette flag.
             
             The system will :
             

Verify write permission on the disclosure object in order to proceed.
             
Remove the relation between the disclosure object and the Model View
             Palette.
             
Delete the Model View Palette
             
Delete all the Model View Groups that were previously referenced
             by the Model View Palette
             



             To delete only specified Groups out of all those currently existing on a Palette,
             the caller will send the Groups to delete in the groupsToDelete list.
             
             The system will:
             

Note: write permission on the Model View Palette is required.
             
Remove all the specified Model View Groups from the reference list
             on the Model View Palette, preserving the order among the remaining Model View Groups
             referenced by the Palette.
             
Delete the now unreferenced Model View Groups.
             



Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param MvPaletteInfo: 
                         The model view palette information describing the details of the palette (<b>Fnd0ModelViewPalette</b>)
                         and model view groups (<b>Fnd0ModelViewGroup</b>) to be created or updated or deleted.
             
        :return: 
        """
        ...
    def CreateOrUpdateModelViewProxies(self, MvProxyInfos: list[ModelViewProxyInfo], UpdatedOwningModels: list[OwningModelAndCadLmd]) -> CreateOrUpdateModelViewProxiesResponse:
        """    
             Creates, updates or deletes a set of model view proxy (Fnd0ModelViewProxy)
             objects. Supports CAD tools in creating and managing model view proxy objects during
             Part save. The model view proxy objects are each a proxy for a master model view
             in the Part's CAD file.
             
             Using this API, applications can create and update proxy objects in bulk, with better
             context and less calls from CAD clients than may otherwise be achieved using standard
             object create and update SOAs.
             

Use Cases:

             This API supports the following use cases:
             
             Use Case 1: Creation of new model view proxy

             The following operation can be used for creating model view proxies for specified
             owning objects (usually ItemRevisions.)
             

Model view proxies have a model view CAD Id (fnd0ModelViewIdCAD)
             which Id is unique within the set of model view proxies associated to the same owning
             object.
             
During the model view proxies initial creation (but not during a
             subsequent save-as or revise), a clone stable ID is generated which can help in identifying
             equivalent proxy objects for cases where the fnd0ModelViewIdCAD wasn't tracked
             but rather the proxy object itself.
             
An optional thumbnail file may be identified that a CAD tool has
             generated for the actual CAD model view.
             
During the operation, the server creates and saves the new model
             view proxies in context of an already existing owning object. The operation returns
             the new objects to the caller.
             



             Use Case 2: Update of existing model view proxy

             The following operation can be used for updating existing model view proxies.
             

Model View Proxies are found by applications via the fnd0OwnedModelViews
             property of workspaceObject objects.
             
The existing model view proxies can be updated using operation createOrUpdateModelViewProxies.
             The application specifies which model view proxies are to be updated.  Note: the
             business object type (boType) and owning
             object (owningModel) do not need to be set
             on the input because they are already known to the model view proxy and cannot be
             changed.  The application sets changed property values.
             



             Use Case 3: Delete of existing model view proxy

             The operation can be used for deleting existing model view proxies due to either
             the CAD designer removing the actual model view or due to a decision that there is
             no need for that model view to have a proxy any longer.
             

Model View Proxies are found by applications via the fnd0OwnedModelViews
             property of certain types of WorkspaceObject objects (currently this property
             is only available at  ItemRevision ).
             
The existing model view proxies can be deleted using operation createOrUpdateModelViewProxies.
             The application specifies which model view proxies are to be modified (modelView) and that they are to be deleted (deleteProxy set to true.)  The server will attempt to delete the
             model view proxy and if successful, the deleted object list will be updated on the
             ServiceData of the response.
             



Teamcenter Component:

             Disclosure - Component that is used to represent the 3D equivalent of the 2D drawing.
             
        :param MvProxyInfos: 
                         The input list of model view proxy information describing the details of the proxies
                         to be created or updated.
             
        :param UpdatedOwningModels: 
                         The input list of model view owners which have had their CAD model views updated.
                         After <font face="courier" height="10">mvProxyInfos</font> has been processed, all
                         proxies associated to these specified owning models will have their CAD last modified
                         date updated to be in sync with a provided date time. This is optional, if no <b>OwningModelAndCADLMD</b>
                         is provided, then no automatic setting of CAD last modified date will be done.
             
        :return: object.
        """
        ...

