import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ConstraintContainerInfo:
    """
    
            Returns geometric constraint container information for model elements that have constraint
            container behavior.
            
    """
    def __init__(self, ) -> None: ...
    Owner: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """The model element that owns the geometric constraint container behavior."""
    Iteration: int
    """
            An iteration number that identifies the precise, 'as-saved' state of a set of constraints
            as defined in CAD for which members are being returned.
            """
    LatestIteration: int
    """The latest iteration of the constraint container."""
    IsLatestIterationWorking: bool
    """
            Whether the latestIteration is allowed to
            have foreground members added or removed. A working iteration has at least one current
            member working rather than released.
            """
    MemberList: list[Membership]
    """
            The positioned model elements objects upon which constraints in the constraintData Dataset depends or are affecting or the
            configured revisions of such objects.
            """
    ConstraintData: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The Dataset containing details about the CAD constraints among the members
            for the returned iteration of the constraint
            container.
            """
    NameReferenceTicketMap: System.Collections.Hashtable
    """
            Map of named reference by which the CAD constraint file is associated to the existing
            or new Dataset and file object's read ticket (FMS) of the CAD file containing constraint
            data. This is populated based on the input datasetOptions.
            """
    AreConstraintsFullySolved: bool
    """
            Whether or not the CAD constraints (held in constraintData
            ) have been fully solved by the CAD tool.
            """
    SystemManaged: bool
    """
            If true, indicates that some CAD tool has constructed the set of members for this
            constraint container, not a user. If false, then a user has manually collected the
            members and their constraints into this container.
            """

class ContainerInputInfo:
    """
    Specifies the set of inputs required to get the Geometric constraint container information.
    """
    def __init__(self, ) -> None: ...
    Owner: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """The model element that owns the geometric constraint container behavior."""
    Iteration: int
    """
            The iteration number specifying the saved state object, i.e. 'as-saved' state of
            a set of constraints as defined in CAD, which will be used to retrieve the information
            if the NavigationMode is "precise". Otherwise, the iteration value may be zero if
            the navigationMode is set to "configured", as then the configuration and the total
            set of foreground members determines which iteration is best to return. Also, if
            the NavigationMode is "precise" and the iteration is given as "-1", then the content
            of the latest iteration will be returned.
            """

class DataSetInfo:
    """
    
            A structure used to create new Datasets and files when needed (either on initial
            creation or when a new saved state iteration is constructed.)
            
    """
    def __init__(self, ) -> None: ...
    DataSetType: str
    """The name of dataset type to create when a new Dataset is required."""
    NameReferenceFileMap: System.Collections.Hashtable
    """
            Map (string,string) of named reference type name by which the CAD constraint file
            is associated to the existing or new Dataset and name of file excluding path
            that CAD tool will upload containing CAD constraints.
            """

class CreateCollectionInfo:
    """
    
            Specifies the full set of inputs required to set or update the Geometric constraint
            container's member and the initial or updated constraint dataset.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This value is optional, but if supplied it
            will be returned with each created constraint collection and may be used to correlate
            which collection resulted from which input CreateCollectionInfo
            structure. Further, partial errors associated with a particular input structure may
            also be correlated in the absence of a created collection against which to log the
            error.
            """
    BoType: str
    """
            The business object type of the constraint collection to be created. This value is
            required for creating the new collection, and it must be a valid subtype of Mdl0ModelElement.
            A supplied type to use is Mdl0GeomCnstrntCollection.
            """
    ModelObject: Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel
    """
            The application model (Mld0ApplicationModel) that should contain the newly
            created model element that will own the constraint container. This object must be
            provided as a model element must be in an application model.
            """
    AttrInfoMap: System.Collections.Hashtable
    """
            A set of name-value pairs used to specify additional property data for the collection.
            All values are specified as strings, the caller is responsible for generating the
            correct string representation of each value passed. For tag values, the UID of the
            tag is used. These pairs may be optional or mandatory depending on the boType of
            the desired collection.
            """
    ConstraintAttrInfoMap: System.Collections.Hashtable
    """
            A set of name-value pairs used to specify additional property data for the constraint
            container's initial saved state. All values are specified as strings, the caller
            is responsible for generating the correct string representation of each value passed.
            For tag values, the UID of the tag is used. These pairs may be optional or mandatory
            depending on the properties of the container being set.
            """
    MemberList: list[Membership]
    """
            The positioned model elements objects upon which constraints in the constraintData Dataset depends or are affecting. This list
            may be empty.
            """
    ConstraintData: DataSetInfo
    """
            The details needed to create the CAD constraint Dataset. The CAD constraint
            Dataset will contain details about the CAD constraints for which the constraint
            collection is being created. This Dataset is optional, but if members are
            provided and have CAD constraints, then it would be usual to provide the details
            for this Dataset in order to be able to provide an actual constraint file.
            """
    AreConstraintsFullySolved: bool
    """
            Stored during creation for the initial saved state, this value tracks for future
            reference whether or not the CAD constraints have been fully solved by the CAD tool.
            This optional value will default to false if not set.
            """
    SystemManaged: bool
    """
            If true, then a CAD tool has constructed the set of members for this constraint collection,
            not a user. If false, then a user has manually collected the members and their constraints
            into this new collection. If a value is not provided,    the
            value will default to false.
            """

class CreateCollectionResponse:
    """
    
            A list of CreatedConstraintCollection structures, each containing details
            of a newly created constraint collection.
            
    """
    def __init__(self, ) -> None: ...
    CreatedConstraintCollections: list[CreatedConstraintCollection]
    """List of CreatedConstraintCollection objects returning created collections."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains any exceptions that occurred.
            
"""

class CreatedConstraintCollection:
    """
    
            This structure is used to return newly created geometric constraint collections as
            while as their initial members.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from CreateCollectionInfo.clientId.
            It may be used to correlate which collection resulted from which input CreateCollectionInfo structure. Further, partial errors associated
            with that particular input structure may also be correlated in the absence of a created
            collection against which to log the error.
            """
    Collection: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """The newly created model element that has the geometric constraint container behavior."""
    MemberList: list[Membership]
    """
            The positioned model elements objects upon which constraints in the constraintData Dataset depends or are affecting. They are
            returned here in order to return system generated CSID values associated to each
            new member.
            """
    NameReferenceTicketMap: System.Collections.Hashtable
    """
            Map of named reference by which the CAD constraint file is associated to the existing
            or new Dataset and file object's read or write ticket (FMS) of the CAD file containing
            constraint data. Used by CAD tools to upload the new CAD constraint file that correlates
            to the initial memberships of this collection.
            """
    ConstraintDataSet: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            The Dataset that will contain the correct CAD constraints. If the corresponding
            constraintData was provided then the server
            will return a newly created Dataset that was associated to the initial saved
            state of the new collection
            """

class DatasetOptions:
    """
    Dataset options.
    """
    def __init__(self, ) -> None: ...
    Mode: str
    """
            The valid values are NO_DATA, GET_DATASET_ONLY, GET_FILE_FOR_NAMED_REF or  GET READTICKET_FOR_NAMED_REF.
            Controls what data from the CAD saved Dataset to return when retrieving the
            details of a constraint container. If the mode is NO_DATA then no Dataset
            related information returned. If the mode is GET_DATASET_ONLY then Dataset
            information alone is returned. If the mode is GET_FILE_FOR_NAMED_REF then both the
            Dataset and the ImanFile are returned. If the mode is GET_READTICKET_FOR_NAMED_REF
            then the Dataset, ImanFile, and a read ticket are returned.
            """
    NamedRefName: str
    """
            String name of the named reference desired. A value is required if the DatasetMode
            is set to either GET_FILE_FOR_NAMED_REF or GET_READTICKET_FOR_NAMED_REF
            """

class ElementToCheckInputInfo:
    """
    
            Specifies the set of inputs required to get the up-to-date status of Positioned Model
            Element.
            
    """
    def __init__(self, ) -> None: ...
    InputElement: Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement
    """
            Positioned Model Element (Mdl0PositionedModelElement) that the caller is inquiring
            as to whether they are up-to-date with respect to the navigation.
            """
    PendingChecksum: list[str]
    """
            List of CAD application specific strings representing a checksum of a set of geometric
            objects that were involved in constraining the input element.
            """
    PendingTransform: list[float]
    """
            Pending absolute transform values which positions the source object in the coordinate
            system of the product design.
            """

class GetContainerInfoResponse:
    """
    
            This structure details about a list of geometric constraint containers and their
            members. If there is any exception during a container's member retrieval it will
            be added to the ServiceData object and returned as a partial error, correlated
            by the constraint container's owner object.
            
    """
    def __init__(self, ) -> None: ...
    ContainerInfo: list[ConstraintContainerInfo]
    """
            A list of detailed information about a constraint container corresponding with an
            input constraint container owner. The order of objects in this list matches with
            the order of inputs.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains any exceptions that may occur.
            
"""

class GetImpactedContainersResponse:
    """
    
            A list of impacted containers for each input positioned model element including full
            details for each impacted container iteration.
            
    """
    def __init__(self, ) -> None: ...
    ListImpactedContainers: list[ImpactedContainerOwnersData]
    """
            List containing sets of server ID strings for    pairs
            of the owners and the iterations that are impacted by each input element. Each list
            of server ID strings are in the same order as the input elements. Each constraint
            container that is impacted may be looked up in containerInfoMap
            by these server ID strings to retrieve full details.
            """
    ContainerInfoMap: System.Collections.Hashtable
    """
            Contains full details for each constraint container iteration that is impacted by
            one of the input elements. The map key is a generated server ID string provided
            by a list inside listImpactedContainers.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains any exceptions that occur. Also all container owners are added to the plain
            object list.
            """

class GetImpactingContainersResponse:
    """
    
            Used to return constraint container iteration details that are impacting on the input
            elements.
            
    """
    def __init__(self, ) -> None: ...
    InputElementToContainerMap: System.Collections.Hashtable
    """
            A map of the input elements to a server ID String (Mdl0PositionedModelElement/string)
            that is used to identify a constraint container iteration in containerInfo. If the
            navigation mode is "precise", then the container iteration is the one that defined
            the input element's position.
            """
    ContainerInfoMap: System.Collections.Hashtable
    """
            A map of server generated string and full details for each constraint container that
            is    impacting one or more of the input elements (string/ConstraintContainerInfo).
            The map key is a server Id string (a value from inputElementToContainerMap)
            of the constraint container iteration for which the map value contains detailed information.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains any exceptions that occur. Also all container owners are added to the plain
            object list.
            """

class GetUpToDateStatusResponse:
    """
    A map of up-to-date status data and ServiceData.
    """
    def __init__(self, ) -> None: ...
    UpToDate: System.Collections.Hashtable
    """
            A map of the input elements to the UpToDateResult structure representing the
            up-to-date status.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """An object of ServiceData which contains any exceptions if occurred."""

class ImpactedContainerOwnersData:
    """
    
            This structure is used to return a list of containers that are impacted by a given
            positioned model element (Mdl0PositionedModelElement.)
            
    """
    def __init__(self, ) -> None: ...
    ImpactedOwnerIterationIds: list[str]
    """
            A list of server IDs that are a key entry for the
IdToContainerInfoMap structure in GetImpactedGCContainersResponse.
            Each server ID can retreive a constraint container owner where the container has
            members that include the corresponding input element or a configured revision of
            that element as a member.
            """

class Membership:
    """
    
            This structure represents an object upon which a constraint depends.  The object
            may be a foreground member of the constraint container, or another design component
            (positionable) object that is not positioned by the constraint container (a.k.a.
            a background member) but is needed in order to position the foreground members. This
            structure is used both for callers to specify desired members and also for various
            operations to return current members.
            

    """
    def __init__(self, ) -> None: ...
    Member: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            An object that is a current or desired member of a geometric constraint container.
            It must be a type of model element that has the positionable behavior (such as the
            Mdl0PositionedModelElement type.)
            """
    Csid: str
    """
            A copy stable identifier (CSID) assigned to the member. As an operation input, if
            this CSID is not  provided, then it will be system generated for the desired member.
            As an input membership request, if this CSID already exists in the container's current
            saved state, then the member is being requested to replace the old member for this
            CSID.
            """
    IsForeground: bool
    """If true, the member is foreground; otherwise, false."""

class NavigationOptions:
    """
    Mode of navigation either through precise references or using configuration context.
    """
    def __init__(self, ) -> None: ...
    Mode: str
    """
            Mode of navigation either through precise references or using configuration context.
            The valid values are "PRECISE" or "CONFIGURED".
            """
    ConfigContextObject: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Configuration context object used to configure member revisions. This must be passed,
            if mode is set to be "configured". If mode is set to "precise", then the configContextObject will be ignored.
            """

class UpdateContainerInfo:
    """
    
            Specifies the full set of inputs required to update the Geometric constraint container's
            members and possibly create a new constraint Dataset (if a new container iteration
            is required.)
            
    """
    def __init__(self, ) -> None: ...
    Owner: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            The model element that owns the geometric constraint container behavior. The container
            owner object must be provided.
            """
    AttrInfoMap: System.Collections.Hashtable
    """
            A set of name-value pairs used to specify additional property data for the owner
            model element.  All values are specified as strings, the caller is responsible for
            generating the correct string representation of each value passed.  For tag values,
            the UID of the tag is used.
            """
    ConstraintAttrInfoMap: System.Collections.Hashtable
    """
            A set of name-value pairs used to specify additional property data for the    
            constraint container's initial saved state. All values are specified as strings,
            the caller is responsible for generating the correct string representation of each
            value passed.  For tag values, the UID of the tag is used. These pairs may be optional
            or mandatory depending on the     properties of the container
            being set.
            """
    UpdateIteration: int
    """
            The precise, 'as-saved' state of a set of constraints as defined in CAD. Unset for
            the first update of the owner object's constraint container.
            
            The precise, 'as-saved' state of a set of constraints as defined in CAD. Unset or
            zero for the first update of the owner object's constraint container. Otherwise it
            is the iteration based on which an update is being requested.
            """
    MemberList: list[Membership]
    """
            The positioned model elements objects upon which constraints in the constraintData Dataset depends or are affecting.
            """
    ConstraintData: DataSetInfo
    """
            The details needed to either update the existing CAD constraint dataset or create
            a new one. The CAD constraint dataset will contain details about the CAD constraints
            for which the constraint container is being updated.
            """
    AreConstraintsFullySolved: bool
    """
            Stored for the existing or new saved state that will be updated, this value tracks
            for future reference whether or not the CAD constraints have been fully solved by
            the CAD tool. This optional value will default to false if not set.
            """
    SystemManaged: bool
    """
            If true, indicates that some CAD tool has constructed the set of members for this
            constraint collection, not a user. If false, then a user has manually collected the
            members and their constraints into this new collection. If a value is not provided,the
            value will default to false.
            """

class UpdateContainerResponse:
    """
    
UpdateContainerResponse object, this object contains list of UpdatedContainer
            showing which owners underwent a state change versus an in-place update and ServiceData.
            If there is any exception during the object creations it will be added to the ServiceData
            object and returned as a partial error.
            
    """
    def __init__(self, ) -> None: ...
    UpdatedContainers: list[UpdatedContainer]
    """
            A list of UpdatedContainer objects, showing
            for each container owner which iteration an update was requested and which iteration
            was actually updated. This information is needed because a new iteration will be
            created if the iteration requested for new members contains only released foreground
            members.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains any exceptions if occurred.
            
"""

class UpdatedContainer:
    """
    
            UpdatedContainer showing which owners underwent a state change versus an in-place
            update.
            
    """
    def __init__(self, ) -> None: ...
    Owner: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """The model element that owns the geometric constraint container behavior."""
    InputIteration: int
    """
            The iteration number of a precise, 'as-saved' state of a set of constraints as defined
            in a CAD tool. Unset (zero) for the first update of the owner object's constraint
            container.
            """
    OutputIteration: int
    """
            The iteration number of the resulting 'as-saved' state of a set of constraints as
            defined in a CAD tool. When the server has created a new state due to the requested
            member changes, it is returned here so that callers can request content or update
            that particular state iteration.
            """
    LatestIteration: int
    """Integer value representing the latest iteration of the constraint container."""
    IsLatestIterationWorking: bool
    """
            If true, the latest iteration has at least one current member working rather than
            released.
            """
    Members: list[Membership]
    """
            A complete list of members post update and their csIds for the caller to be able
            to track the new members by their csId.
            """
    NameReferenceTicketMap: System.Collections.Hashtable
    """
            Map of named reference by which the CAD constraint file is associated to the existing
            or new Dataset and file object's read or write ticket (FMS) of the CAD file containing
            constraint data. Used by CAD tools to upload a new or updated CAD constraint file
            that correlates to the updated memberships just completed.
            """
    ConstraintDataSet: Teamcenter.Soa.Client.Model.Strong.Dataset
    """
            If the corresponding constraintData was provided, then this will be the dataset that
            will contain the CAD constraints. If the corresponding constraintData
            was not provided, then no dataset will be returned. If the outputIteration is different
            than the inputIteration, or if there was no prior dataset for thie inputIteration,
            then the server has just created this dataset.
            """

class UpToDateResult:
    """
    Structure representing up-to-date status of input Positioned Model elements.
    """
    def __init__(self, ) -> None: ...
    ElementStatus: bool
    """
            Boolean data representing the up-to-date status. If true, then the positioned model
            element is up-to-date with respect to the input navigation option.
            """
    OutOfDateGeometricConstraintContainers: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]
    """
            ModelElements which are constraint containers that are not fully solved given the
            requested validation request and are the cause of the elementStatus being false.
            """

class GeometricConstraints:
    """
    Interface GeometricConstraints
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateCollection(self, ContainerCollectionInfo: list[CreateCollectionInfo]) -> CreateCollectionResponse:
        """    
             This operation creates a geometric constraint collection containing model elements,
             i.e. foreground members (having their positions affected and possibly affecting other
             foreground members in the container) and background members (only affecting positions
             of foreground members). In addition, the CAD dataset specifying the geometric constraints
             among the members is also set.
             

Use Cases:

             1.    Saving geometric constraint group data to Teamcenter
             by CAD.
             
             This use case is entirely within the domain of CAD tools. Using this service operation
             a CAD tool will save the constraint collection data in Teamcenter. It will provide
             the model elements, i.e. foreground and background members and the CAD dataset specifying
             the geometric constraints among the members.
             

Example client to server interaction :
             
             1)    A CAD tool calls createCollection passing in the
             initial set of desired  members and provides their own generated csid values for
             each new member. ConstraintData will be populated
             with the desired Dataset type and desired named reference file type for the
             given CAD tool.
             
             2)    The server returns a newly created collection, a newly
             created Dataset of the specified type, and also the ticketForNamedRef
             that was also created and associated to the new dataset. In the returned memberList for the new collection, the recorded csid values per member record are also returned.
             
             3)    The CAD tool then uploads its constraint file using the
             returned ticketForNamedRef and saves the
             constraintDataSet.
             

Alternatively the server may be allowed to generate csids:

             1)    A CAD tool calls createCollection passing in the
             initial set of desired  members, but does not provide csid values for each new member.
             ConstraintData will be populated with the
             desired Dataset type and desired named reference file type for the given CAD
             tool.
             
             2)    The server returns a newly created collection, a newly
             created dataset of the specified type, and also the ticketForNamedRef
             that was also created and associated to the new Dataset. In the returned memberList for the new collection, the newly allocated
             csid values per member record are also returned.
             
             3)    The CAD tool takes the returned csid
             values for each new member and records them appropriately in its own CAD geometric
             constraint file. Then it uploads that file using the returned ticketForNamedRef and saves the constraintDataSet.
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param ContainerCollectionInfo: 
                         List of objects of <font face="courier" height="10">CreateCollectionInfo</font>.
                         Each object contains the set of information needed to create the geometric constraint
                         collection, its initial members and the initial constraint dataset.
             
        :return: 
        """
        ...
    def GetContainerInfo(self, Inputs: list[ContainerInputInfo], NavOptions: NavigationOptions, DatasetOptions: DatasetOptions) -> GetContainerInfoResponse:
        """    
             This operation retrieves of member content of model elements that have constraint
             container behavior. If the navigation mode is given as "precise", then the member
             content returned for a given container's saved-state will be only those member revisions
             (for members that support Revise operation ) that are precisely assigned membership.
             If the mode is given as "configured", then the member content returned for a given
             container's saved-state will be modified (versus the precise member revisions) to
             consider an input configuration context  to determine the revision (for members that
             support Revise operation ) that is returned as a member.
             

Use Cases:

             1.    Load members of a constraint container from CAD tool

             This operation will be used by CAD tools to load the members of the constraint network.
             If navigation mode is given as "precise", then the member content returned for a
             given container's saved-state will be only those member revisions (for members that
             support Revise operation ) that are precisely assigned membership. If the mode is
             given as "configured", then the member content returned for a given container's saved-state
             will be modified (versus the precise member revisions) to consider an input configuration
             context  to determine the revision (for members that support Revise operation ) that
             is returned as a member.
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Inputs: 
                         A list of geometric constraint containers to retrieve content from.
             
        :param NavOptions: 
                         Specifies the mode of navigation, i.e., whether to follow precise member references
                         or using an input configuration context.
             
        :param DatasetOptions: 
                         Specifies whether or not to return the constraint dataset, associated file or fileticket.
             
        :return: object and returned as a partial error.
        """
        ...
    def GetImpactedContainers(self, Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement], NavOptions: NavigationOptions, DatasetOptions: DatasetOptions) -> GetImpactedContainersResponse:
        """    
             This operation retrieves of geometric constraint containers and hence their positioned
             model elements (Mdl0PositionedModelElements) that could be impacted if the
             position of the input elements is altered. This operation returns the containers
             impacted only on next level in the hierarchy of impacted containers. This operation
             could be used prior to modifying a CAD constraint in a CAD tool where that CAD constraints
             dependency has been tracked in Teamcenter using the Geometric Constraint Container
             behaviors.
             

Use Cases:

1.    Modifying a CAD constraint in a CAD tool.

             This use case is entirely within the domain of CAD tools. Using this SOA the CAD
             tool can get the list of containers and elements which could be impacted prior to
             making a change in position of one of the input elements
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Elements: 
                         A list of positioned model elements for which impacted containers are returned.
             
        :param NavOptions: 
                         Specifies the mode of navigation, i.e., whether to follow precise member references
                         or using an input configuration context.
             
        :param DatasetOptions: 
                         Specifies whether or not to return the constraint <b>Dataset</b>, associated file
                         or file ticket.
             
        :return: For each input element, a list of impacted owners and a particular saved-state iteration
             are returned, including container iteration details for each such saved-state. If
             there is any exception during the retrieval it will be added to the ServiceData object
             and returned as a partial error.
        """
        ...
    def GetImpactingContainers(self, InputElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement], NavOptions: NavigationOptions, DatasetOptions: DatasetOptions) -> GetImpactingContainersResponse:
        """    
             This operation retrieves member content of particular geometric constraint containers
             (which are owned by model elements that have constraint container behavior.) The
             containers retrieved are those for which the input positionable objects are foreground
             members. The constraint containers which are impacting the input members are retrieved
             according to the navigation mode requested. If the navigation mode is given as "precise",
             then the member content returned for a given container's saved-state will be only
             those member revisions (for members that support Revise operation ) that are precisely
             assigned membership. If the mode is given as "configured", then the member content
             returned for a given container's saved-state will be modified (versus the precise
             member revisions) to consider an input configuration context  to determine the revision
             (for members that support Revise operation ) that is returned as a member.
             

Use Cases:

1.    Load members of a constraint container from CAD tool
             based on a set of input design components.

             This operation will be used by CAD tools to load the members of the constraint containers
             that have impacted the position of the input design components. If navigation mode
             is given as "precise", then the member content returned for a given container's saved-state
             will be only those member that are precisely assigned membership. If the mode is
             given as "configured", then the member content returned for a given container's saved-state
             will be modified (versus the precise members ) to consider an input configuration
             context  to determine the revision (for members that support Revise operation ) that
             is returned as a member.
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param InputElements: 
                         The input positionable model elements that are to be checked for which constraint
                         container defined their position via constraints.
             
        :param NavOptions: 
                         Specifies the mode of navigation, i.e., whether to follow preciseÂ Â Â Â member
                         references or using an input configuration context.
             
        :param DatasetOptions: 
                         Specifies whether or not to return the constraint <b>Dataset</b>, associated file
                         or file ticket.
             
        :return: For each input element, a list of impacting constraint container owners and their
             particular saved-state iteration are returned, including container iteration details
             for each such saved-state. If there is any exception during the retrieval it will
             be added to the ServiceData object and returned as a partial error.
        """
        ...
    def GetUpToDateStatus(self, Inputs: list[ElementToCheckInputInfo], NavOptions: NavigationOptions, VerifyInContextOfPendingData: bool) -> GetUpToDateStatusResponse:
        """    
             This operation queries the constraint status of the input positioned model elements
             with respect to the navigation option to determine whether the elements are up-to-date
             (i.e., their data satisfy the corresponding constraints without further solving).
             The application can use this information to determine if it is necessary or desirable
             to load the associated geometric constraint containers into the CAD workspace.
             

Use Cases:

             1.    Determining if it is necessary to load the associated 4GD
             constraint containers
             
             In CAD, after loading a subset with positioned model elements, the application may
             be interested in knowing whether it is necessary to further load the associated 4GD
             constraint containers to ensure that the position data associated with the positioned
             model elements are up-to-date.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Inputs: 
                         List of objects of <b>ElementToCheckInputInfo</b>. Each object contains Positioned
                         Model Element (<b>Mdl0PositionedModelElement</b>) that the caller is inquiring as
                         to whether they are up-to-date with respect to the navigation option along with pending
                         checksum and transform details.
             
        :param NavOptions: 
                         Specifies the mode of navigation, i.e., whether to follow precise member references
                         or using an input configuration context.
             
        :param VerifyInContextOfPendingData: 
                         If true, the up-to-date check will treat the input elements as having their pending
                         checksums and transforms saved.
             
        :return: 
        """
        ...
    def UpdateContainer(self, ContainerInfo: list[UpdateContainerInfo]) -> UpdateContainerResponse:
        """    
             This operation allows updating of model elements that have constraint container behavior.
             The updates may include altering the member content of model elements, i.e. foreground
             members (having their position affected and possibly affecting other foreground members
             in the container) and background members (only affecting positions of foreground
             members). In addition, the CAD dataset specifying the geometric constraints among
             the members is also updated.
             

Use Cases:

             1.    Adding DE as member of a constraint container (such
             as a Geometric Constraint Collection.)
             
             This use case is entirely within the domain of CAD tools. Using this SOA the CAD
             tool can manage the constraint container membership (foreground references). User
             will require site ownership of the design component to add it as a foreground member
             of a constraint container. It will also require write privilege to the constraint
             container add the design component as a (foreground or background) member of the
             group.
             

             2.    Removing DE as member of a constraint container

             This use case is entirely within the domain of CAD tools. Using this operation a
             CAD tool can remove Design Components from the constraint container.
             

Example client to server interaction :

             1)    A CAD tool calls updateGeomConstraintCollection
             passing in the complete set of desired  members, and also provides csid values for each entirely new member. ConstraintData will usually be populated with the desired Dataset
             type and desired named reference file type for the given CAD tool.
             
             2)    The server returns a details about the updated constraint
             container, an existing or  newly created dataset of the specified type, and also
             the ticketForNamedRef that is bound to the
             existing or new ImanFile that is associated to the dataset. In the returned
             memberList, the newly allocated csid values per entirely new member record are also returned.
             
             3)    The CAD tool takes the returned csid
             values for each new member and records them appropriately in its own CAD geometric
             constraint file. The CAD tool may also need to update any record of the container
             iteration number if the outputIteration differs
             from the inputIteration. Then it uploads
             that file using the returned ticketForNamedRef
             and saves the constraintDataSet.
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param ContainerInfo: 
                         List of objects of <b>UpdateContainerInfo</b>. Each object contains the set of information
                         needed to update the geometric constraint container's members and an updated constraint
                         dataset.
             
        :return: object and returned as a partial
             error.
        """
        ...

