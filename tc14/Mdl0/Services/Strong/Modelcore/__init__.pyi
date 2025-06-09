import Mdl0.Services.Strong.Modelcore._2011_06.DataManagement
import Mdl0.Services.Strong.Modelcore._2011_06.IdManagement
import Mdl0.Services.Strong.Modelcore._2011_06.ModelConfiguration
import Mdl0.Services.Strong.Modelcore._2011_06.Search
import Mdl0.Services.Strong.Modelcore._2013_05.Search
import Mdl0.Services.Strong.Modelcore._2014_06.DataManagement
import Mdl0.Services.Strong.Modelcore._2014_10.DataManagement
import Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints
import Mdl0.Services.Strong.Modelcore._2014_10.ModelConfiguration
import Mdl0.Services.Strong.Modelcore._2014_10.Search
import Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity
import Mdl0.Services.Strong.Modelcore._2015_07.GeometricConstraints
import Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity
import Mdl0.Services.Strong.Modelcore._2016_10.GeometricConnectivity
import Mdl0.Services.Strong.Modelcore._2016_10.GeometricConstraints
import Mdl0.Services.Strong.Modelcore._2017_05.Search
import Mdl0.Services.Strong.Modelcore._2018_06.Search
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DataManagementRestBindingStub(DataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def DeleteModelContent(self, ObjectsToDelete: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]) -> Mdl0.Services.Strong.Modelcore._2011_06.DataManagement.DeleteModelContentResponse: ...
    def GetReviseDesc(self, TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2011_06.DataManagement.SaveAsDescResponse: ...
    def ReviseObjects(self, SaveAsIn: list[Mdl0.Services.Strong.Modelcore._2011_06.DataManagement.SaveAsIn]) -> Mdl0.Services.Strong.Modelcore._2011_06.DataManagement.SaveAsObjectsResponse: ...
    def QueryRelatedObjects(self, InputObjects: list[Mdl0.Services.Strong.Modelcore._2014_06.DataManagement.RelatedObjectInput]) -> Mdl0.Services.Strong.Modelcore._2014_06.DataManagement.RelatedObjectsResponse: ...
    def CloneModelContent(self, Info: Mdl0.Services.Strong.Modelcore._2014_10.DataManagement.CloneModelContentInfo) -> Mdl0.Services.Strong.Modelcore._2014_10.DataManagement.CloneModelContentResponse: ...

class DataManagementService:
    """
    
            This service contains utilities which augment the Teamcenter core data management
            services.  Specifically this service provides:
            

            Â Â Â Â Â Â Â Â   application models (Mdl0ApplicationModel)
            

Use case:


            Please see the deleteModelContent operation
            documentation for delete use cases.
            
            Please see the reviseObjects operation documentation
            for revise use cases.
            
            Please see the cloneModelContent operation
            documentation for revise use cases.
            


Library Reference:

Mdl0SoaModelCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DataManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def DeleteModelContent(self, ObjectsToDelete: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement]) -> Mdl0.Services.Strong.Modelcore._2011_06.DataManagement.DeleteModelContentResponse:
        """    
             Deletes Mdl0ModelElement objects from an Mdl0ApplicationModel.This
             operation will attempt to delete as many objects as it can and returns a list of
             any objects that could not be deleted.Order of objects in the input list is not important.This
             operation handles the case when one input object has a non circular reference to
             another input object; deletion of the referenced object will occur after its referencing
             object is deleted.
             

Use Cases:

             This API supports model element authoring use cases, specifically the bulk deletion
             of objects within a model.
             
             the following steps can be used for deleting model elements from a model.
             

Find through query or navigate the model elements to be deleted.
             
Call the delete operation deleteModelContent
             to delete a list of existing model elements from a model.
             


             Note:  deleteObjects operation can also be
             used, but requires proper ordering of input   elements to handle the case when one
             model element in the input list references another model element in the input list.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param ObjectsToDelete: 
                         The input list of model elements to be deleted.
             
        :return: 
        """
        ...
    def GetReviseDesc(self, TargetObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2011_06.DataManagement.SaveAsDescResponse:
        """    
             Gets a save as descriptor for a revise operation.Clients may use the output of this
             call to construct generic UI dialogs to collect user input for the revise operation.This
             operation takes in a list of objects to be revised, and returns save as descriptors
             and deep copy for each object input.
             

Use Cases:

             See the reviseObjects operation documentation
             for applicable use cases.
             

Dependencies:

             getReviseDesc, reviseObjects
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param TargetObjects: 
                         Input list of objects to be revised. It must be a subtype of <b>Mdl0ConditionalElement</b>

        :return: The response contains a map of business object types to their save as descriptor
             (used for revise operations as well), and a map of the deep copy data for each of
             input objects.
        """
        ...
    def ReviseObjects(self, SaveAsIn: list[Mdl0.Services.Strong.Modelcore._2011_06.DataManagement.SaveAsIn]) -> Mdl0.Services.Strong.Modelcore._2011_06.DataManagement.SaveAsObjectsResponse:
        """    
             Revises a set of input objects and performs a deep copy of related objects.New objects
             are saved in the Teamcenter database and returned in the response.
             

Use Cases:

             This API supports the authoring use case where an object or a set of objects requires
             a new revision. Objects which are a subtype of Mdl0ConditionalElement support
             the concept of revise.   The elements are first created by a user, undergo edits,
             and then are approved through a workflow and given status. At this point, a new revision
             of the object must be created to further modify it.
             
             The reviseObjects  operation is used to create
             the new revision.  Deep copy rules, defined in BMIDE and deployed to Teamcenter,
             control the sub object copy process during the revise operation.  The operation getReviseDesc is called prior to calling reviseObjects to construct the deep copy information
             and descriptors for the objects to be revised.
             
             Use Case : Revise a conditional element  

             The following assumes an initial revision has been created and released.
             

Construct list of existing, released objects to be revised (objects
             must be valid subtypes of Mdl0ConditionalElement).
             
Construct deep copy data and get saveAs descriptors for the input
             set of objects by using operation getReviseDesc.
             
Revise the objects in Teamcenter by using the reviseObjects operation.
             
Post process / display new object revisions in client
             



Dependencies:

             getReviseDesc
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SaveAsIn: 
                         List of input data  containing object to be revised and its deep copy data.
             
        :return: A list of objects that were created and saved during the revise operation. Any failure
             will be returned with Business object mapped to error message in the ServiceData
             list of partial errors.
        """
        ...
    def QueryRelatedObjects(self, InputObjects: list[Mdl0.Services.Strong.Modelcore._2014_06.DataManagement.RelatedObjectInput]) -> Mdl0.Services.Strong.Modelcore._2014_06.DataManagement.RelatedObjectsResponse:
        """    
             This operation queries, filters, and configures all primary/secondary objects attached
             to the given input set of objects.  Filter criteria are provided through the RelatedObjectInput
             construct. Filtering can be based on the type of the relation, the type of the related
             object, and relation attribute values.  Configuration conditions are specified by
             a ConfigurationContext object, which provides revision and unit effectivity rule
             information. Returned objects are configured by the given configuration context and
             are access checked before being returned.
             

             Some applications, such as CAD tools, need to navigate relationships and return results
             only if they match certain configuration criteria. An example is the navigation from
             a design component to a design control element.  A design component may be related
             to multiple revisions of a design control element; however within a configured view
             of the system, only one of the design control elements may actually be relevant.
             This service operation helps find the secondary object (e.g. Cpd0DesignElement)
             of a relation (e.g. Cpd0ControlModel) given a primary object (e.g. Cpd0DesignControlElement).
             

             RESTRICTION:  Currently this operations support navigation of Mdl0CopyStableRelation
             and its subtypes only.
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param InputObjects: 
                         This vectors provides inputs of the objects for which related objects have to be
                         queried along with query filters.
             
        :return: A set of objects that are access checked before being returned.
        """
        ...
    def CloneModelContent(self, Info: Mdl0.Services.Strong.Modelcore._2014_10.DataManagement.CloneModelContentInfo) -> Mdl0.Services.Strong.Modelcore._2014_10.DataManagement.CloneModelContentResponse:
        """    
             The operation clones (Deep copy) model elements from an application model ( referred
             as source model ) into another application model or within the same application model
             ( referred as target model ). Elements come from source application model, either
             manually or via search criteria to be copied into a second application model. The
             same source content may be cloned multiple times into the same or different target
             model. No associations are maintained between related objects in the source and target
             models, therefore there is no capacity to update any cloned content in the target
             model.
             

             The newly created objects in the target model are fully populated meaning they are
             persistently created in the context of the target model. The object type and category
             of the newly created objects will remain same in the target model. For example, a
             Design Component (Cpd0DesignElement) of category
             Shape from a source model is cloned into a target model, the category and the object
             type of the newly created object in the target model will still be the same as the
             object in the source model. Model elements when cloned across two different source
             models will be re-identified in the target model. For example, upon cloning new IDs
             will be assigned to the Design Component objects in the target model.
             

             The elements to be included from the source to the target model can be either an
             explicit list of elements or results from a recipe. List of elements from the source
             model to be explicitly included (via multi-select action) can be passed to this operation
             for cloning the content into the target model.
             

             Note: Internally BMIDE deep copy rules will be used to traverse and clone the source
             objects.
             



             Preconditions: 

             1)    The source application model is with some pre-existing
             model content.
             
             2)    Target application model already exists.
             
             3)    Partitions (Member owns the membership) are pre created
             in target model if memberships are expected to be copied over to target model.
             



             Cloning in the context of Partitions:


             Note: Partitions are not cloned as part of this operation.
             

             Application must leverage on Partition clone functionality to clone partition from
             one application model into another application model but the model content that resides
             in the source application model are cloned into the new application model using cloneModelContent Operation.
             

             In order to create Partition breakdowns also in the target model, the applications
             must follow a two-step process.
             
             1)    Perform Partition Template Clone using existing clonePartitions service operation to copy partitions from one
             model to another.
             
             2)    Perform Template Clone with model content using the cloneModelContent service operation.



             If the initial elements would reference partitions (member owned partitions) in the
             source application model, membership objects will be also be cloned if the target
             models have the same partitions else the model elements will be cloned as unassigned
             members. If same Partition memberships exist both in source model and target model
             then they are not recreated instead the existing memberships are retained.
             

             Note:
             
             1)    If the source model contains a reuse design component,
             then all its subordinate design components will be cloned. The system will warn and
             stop if the user is trying to clone only subordinate design component without its
             reuse design component.
             
             2)    Delete on cloned content in the target model deletes the
             selected object alone. If the selected object to delete is a reuse Design Component,
             then all its subordinates will also be deleted.
             
             3)    If the category of the newly created target object has
             to be different from source object types then it is Application's/Customer's responsibility
             to manage any such mappings through extension points provided by the infrastructure.
             


             Note:
             

             1) If the source model contain a reuse design component, then all its subordinate
             design components will be cloned. This is control by a business object contants called
             "cloneReuseAlongWithSubordinates". If the value of this constant is true, then reuse
             and its full chain of subordinates will be cloned togther, else reuse or the selected
             subordinate will be ignore.
             

             2) Delete on cloned content in the target model deletes the selected object alone.
             If the selected object to delete is a reuse Design Component , then all its subordinates
             will also be deleted.
             

             3) Variants and Effectivity conditions will not be carry forwarded onto the target
             objects in the target model by default alternatively this behavior can be controlled
             by a business object constant "cloneObjectsWithVariantExpr" , "cloneObjectsWithEffectivityExpr"
             . If the value of the contant is "true" then Variants or effectivity expressions
             will copied from source object.
             

             Refer to TDOC for more information on prerequisites on Variant and effectivity expression
             carry over from source application model to target application model.
             


Use Cases:

             This operation supports the most common Clone Template use case for applications
             to re-use project work as part of their knowledge capture for future projects.
             

             Templates shall be creatable in three different ways:
             
             1)    An extract from an existing model.
             
             2)    Authored from Scratch.
             
             3)    Derived from another template (a.k.a. model). This derivation
             shall keep a relation to the original template.
             
             From 4GD standpoint template is a specialization of an Application model which can
             contain explicit content, parameterized content and place holders.
             

             Applications can clone the source template into target application model.. During
             clone operation, a configurable set of relationships will also be copied over from
             the selected elements to the new initial elements in the second application model.
             Once the cloning is completed the initial elements may be modified to fit better
             with the second application model's requirements.
             

             Note: Re-cloning, revise and update on the source model content has no effect on
             the cloned content in the target model.
             

Dependencies:

             autoAssignValues, getSaveAsDesc
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Info: 
                         Data on <font face="courier" height="10">CloneModelContentInfo</font> used for the
                         cloning of the model content from one application model (source) to another application
                         model (target).
             
        :return: 
        """
        ...

class GeometricConnectivityRestBindingStub(GeometricConnectivityService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def CreateOrUpdateGeomConnGroups(self, GroupInfos: list[Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.CreateOrUpdateGeomConnGroupInfo]) -> Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.CreateOrUpdateGeomConnGroupResponse: ...
    @typing.overload
    def CreateOrUpdateGeomConnGroups(self, GroupInfos: list[Mdl0.Services.Strong.Modelcore._2016_10.GeometricConnectivity.CreateOrUpdateGeomConnGroupInfo]) -> Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.CreateOrUpdateGeomConnGroupResponse: ...
    def GetConnectivityContents(self, QueryInputs: list[Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.QueryInput], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, LoadOption: str) -> Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.GetConnectivityContentResponse: ...
    def GetConnectivityGroupContents(self, GeomGroups: list[Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.GetGroupContentResponse: ...
    def MergeGeomConnGroups(self, MergeGroupInfos: list[Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.MergeGeomConnGroupsInfo]) -> Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.MergeGeomConnGroupsResponse: ...
    def SplitGeomConnGroups(self, SplitGroupInfos: list[Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.SplitGeomConnGroupsInfo], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.SplitGeomConnGroupResponse: ...
    def ValidateGeomConnGroups(self, ValidateGroupInfos: list[Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.ValidateGeomConnGroupInfo], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.ValidateGeomConnGroupResponse: ...

class GeometricConnectivityService:
    """
    
            This service provides operations to support 3D routing in 4GD.
            


Library Reference:

Mdl0SoaModelCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> GeometricConnectivityService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def CreateOrUpdateGeomConnGroups(self, GroupInfos: list[Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.CreateOrUpdateGeomConnGroupInfo]) -> Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.CreateOrUpdateGeomConnGroupResponse: ...
    @typing.overload
    def CreateOrUpdateGeomConnGroups(self, GroupInfos: list[Mdl0.Services.Strong.Modelcore._2016_10.GeometricConnectivity.CreateOrUpdateGeomConnGroupInfo]) -> Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.CreateOrUpdateGeomConnGroupResponse: ...
    def GetConnectivityContents(self, QueryInputs: list[Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.QueryInput], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext, LoadOption: str) -> Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.GetConnectivityContentResponse: ...
    def GetConnectivityGroupContents(self, GeomGroups: list[Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.GetGroupContentResponse: ...
    def MergeGeomConnGroups(self, MergeGroupInfos: list[Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.MergeGeomConnGroupsInfo]) -> Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.MergeGeomConnGroupsResponse: ...
    def SplitGeomConnGroups(self, SplitGroupInfos: list[Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.SplitGeomConnGroupsInfo], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.SplitGeomConnGroupResponse: ...
    def ValidateGeomConnGroups(self, ValidateGroupInfos: list[Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.ValidateGeomConnGroupInfo], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> Mdl0.Services.Strong.Modelcore._2016_05.GeometricConnectivity.ValidateGeomConnGroupResponse:
        """    
             This operation verifies the geometric connectivity groups and returns their validation
             statuses. If both start and end geometric links are null, the connectivity is verified
             for the whole geometric group and it returns all incomplete or invalid positioned
             model elements. Otherwise, will traverse the group from both, stop at the first positioned
             model element that is incomplete and return these two incomplete positioned model
             elements.
             

Use Cases:

             Validating geometric connectivity group and fixing any invalid connectivity.
             
             This use case is entirely within the domain of CAD tools. Using this SOA, the CAD
             tools can validate the list of geometric connectivity groups, load invalid connectivity
             in CAD tools and fix them.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param ValidateGroupInfos: 
                         The set of information needed to validate a geometric connectivity group.
             
        :param ConfigContext: 
                         Configuration context to filter routing contents. It is required to validate the
                         geometric connectivity group.
             
        :return: 
        """
        ...

class GeometricConstraintsRestBindingStub(GeometricConstraintsService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateCollection(self, ContainerCollectionInfo: list[Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.CreateCollectionInfo]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.CreateCollectionResponse: ...
    def GetContainerInfo(self, Inputs: list[Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.ContainerInputInfo], NavOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.NavigationOptions, DatasetOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.DatasetOptions) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.GetContainerInfoResponse: ...
    def GetImpactedContainers(self, Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement], NavOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.NavigationOptions, DatasetOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.DatasetOptions) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.GetImpactedContainersResponse: ...
    def GetImpactingContainers(self, InputElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement], NavOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.NavigationOptions, DatasetOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.DatasetOptions) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.GetImpactingContainersResponse: ...
    def GetUpToDateStatus(self, Inputs: list[Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.ElementToCheckInputInfo], NavOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.NavigationOptions, VerifyInContextOfPendingData: bool) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.GetUpToDateStatusResponse: ...
    def UpdateContainer(self, ContainerInfo: list[Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerInfo]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerResponse: ...
    def UpdateContainer2(self, ContainerInfo2: list[Mdl0.Services.Strong.Modelcore._2015_07.GeometricConstraints.UpdateContainerInfo2]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerResponse: ...
    def UpdateContainer3(self, ContainerInfo3: list[Mdl0.Services.Strong.Modelcore._2016_10.GeometricConstraints.UpdateContainerInfo3]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerResponse: ...

class GeometricConstraintsService:
    """
    
            This service provides operations for CAD tools to create and manipulate the members
            of geometric constraint containers.
            


Library Reference:

Mdl0SoaModelCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> GeometricConstraintsService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateCollection(self, ContainerCollectionInfo: list[Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.CreateCollectionInfo]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.CreateCollectionResponse:
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
    def GetContainerInfo(self, Inputs: list[Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.ContainerInputInfo], NavOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.NavigationOptions, DatasetOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.DatasetOptions) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.GetContainerInfoResponse:
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
    def GetImpactedContainers(self, Elements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement], NavOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.NavigationOptions, DatasetOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.DatasetOptions) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.GetImpactedContainersResponse:
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
    def GetImpactingContainers(self, InputElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement], NavOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.NavigationOptions, DatasetOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.DatasetOptions) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.GetImpactingContainersResponse:
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
    def GetUpToDateStatus(self, Inputs: list[Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.ElementToCheckInputInfo], NavOptions: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.NavigationOptions, VerifyInContextOfPendingData: bool) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.GetUpToDateStatusResponse:
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
    def UpdateContainer(self, ContainerInfo: list[Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerInfo]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerResponse:
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
    def UpdateContainer2(self, ContainerInfo2: list[Mdl0.Services.Strong.Modelcore._2015_07.GeometricConstraints.UpdateContainerInfo2]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerResponse:
        """    
             This operation allows updating of model elements that have constraint container behavior.
             The updates may include altering the member content of model elements, i.e. foreground
             members (having their position affected and possibly affecting other foreground members
             in the container) and background members (only affecting positions of foreground
             members). In addition, the CAD dataset specifying the geometric constraints among
             the members is also updated.
             

Use Cases:

1. Adding DE as member of a constraint container (such as a Geometric Constraint
             Collection.)
             
             This use case is entirely within the domain of CAD tools. Using this SOA the CAD
             tool can manage the constraint container membership (foreground references). User
             will require site ownership of the design component to add it as a foreground member
             of a constraint container. It will also require write privilege to the constraint
             container add the design component as a (foreground or background) member of the
             group.
             

2.  Removing DE as member of a constraint container

             This use case is entirely within the domain of CAD tools. Using this operation a
             CAD tool can remove Design Components from the constraint container.
             

Example client to server interaction :

             1)    A CAD tool calls updateContainer3
             passing in the complete set of desired members, but does not provide csid values
             for each entirely new members. ConstraintData
             will usually be populated with the desired dataset type and desired named reference
             file type for the given CAD tool.
             
             2)    The server returns a details about the updated constraint
             container, an existing or newly created dataset of the specified type, and also the
             nameReferenceTicketMap that is bound to the
             existing or new ImanFile that is associated to the dataset. In the returned
             memberList, the newly allocated csid values
             per entirely new member record are also returned.
             
             3)    The CAD tool takes the returned csid values for each new
             member and records them appropriately in its own CAD geometric constraint file. The
             CAD tool may also need to update any record of the container iteration number if
             the outputIteration differs from the inputIteration. Then it uploads that file using
             the returned nameReferenceTicketMap and saves
             the constraintDataSet.
             


Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param ContainerInfo2: 
                         List of objects of <b>UpdateContainerInfo2</b>. Each object contains the set of information
                         needed to update the geometric constraint container's members and an updated constraint
                         dataset.
             
        :return: 
        """
        ...
    def UpdateContainer3(self, ContainerInfo3: list[Mdl0.Services.Strong.Modelcore._2016_10.GeometricConstraints.UpdateContainerInfo3]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerResponse: ...

class IdManagementRestBindingStub(IdManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AutoAssignValues(self, Input: list[Mdl0.Services.Strong.Modelcore._2011_06.IdManagement.AssignInput]) -> Mdl0.Services.Strong.Modelcore._2011_06.IdManagement.AssignResponse: ...

class IdManagementService:
    """
    
            This service contains utilities to assist with assignment of ID values for application
            models (Mdl0ApplicationModel) and their content in support of create, save as, and
            revise actions.
            
            Currently one operation is provided by this service (autoAssignValues).
            

Use case:

            Please see documentation for autoAssignValues
            operation.
            




Library Reference:

Mdl0SoaModelCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> IdManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AutoAssignValues(self, Input: list[Mdl0.Services.Strong.Modelcore._2011_06.IdManagement.AssignInput]) -> Mdl0.Services.Strong.Modelcore._2011_06.IdManagement.AssignResponse:
        """    
             Auto generates the values of the auto assignable  properties in bulk. The input parameters
             expected on the input, include the business object or the business object name.
             For cases where the assignment is based on other properties, those values must be
             supplied on input; this includes any reference objects.  The output includes the
             generated values as well as other properties defined in the input.
             

             Support is currently limited to the following Collaborative Product Development (CPD)
             specific classes:
             
    Mdl0ApplicationModel (mdl0model_id)
             
                 Ptn0Partition (ptn0partition_id)
             
                 Cpd0DesignElement (cpd0design_element_id)
             
                 Cpd0DesignFeature (cpd0design_feature_id)
             
                 Cpd0DesignControlElement (cpd0design_control_element_id)
             



Use Cases:

             This API supports the authoring use case for model content.It is used to fill in
             autoassignable property values. Applications may choose to allow a user to enter
             a value or assign one.
             
             Use Case 1: Assign ID during Create 

             During creation of a new object, the user requests the system to assign a value
             

Application constructs AssignInput
             and specifies the business object type (boType) of the object being created and an
             operationType: CreateOperation.  A client
             ID (unique for the call) is also specified on the AssignInput
             for error reporting.
             
Generate new ID values for the object using the autoAssignValues operation.
             
Post process the new ID value (e.g. display it back to the user).
             


             Use Case 2: Assign ID during Revise 

             During revise of an existing object, the user requests the system to assign an ID
             value to the new revision.
             

Application constructs AssignInput and specifies the business object
             (bo) of the object being revised and an operationType: ReviseOperation.
             A client ID (unique for the call) can be optionally specified on the AssignInput.
             
Generate ID value for new revision using the autoAssignValues operation.
             
Post process the ID value (e.g. display it back to the user).
             


             Use Case 3: Assign ID during SaveAs 

             During saveas (copy) of an existing object, the user requests the system to assign
             an ID value to the new object.
             

Application constructs AssignInput
             and specifies the business object (bo) of the object being revised and an operationType:
             SaveAsOperation.A client ID (unique for the
             call) can be optionally specified on the AssignInput.
             
Generate ID value for new revision using the autoAssignValues operation.
             
Post process the ID value (e.g. display it back to the user).
             



Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Input: 
                         A list of <font face="courier" height="10">AssignInput</font> for which property
                         values should be autoassigned.
             
        :return: The the input data with autoassigned values filled in.The errors if any are returned
             in the service data.
        """
        ...

class ModelConfigurationRestBindingStub(ModelConfigurationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def FindRevisionRulesForModel(self) -> Mdl0.Services.Strong.Modelcore._2011_06.ModelConfiguration.FindRevisionRulesForModelResponse: ...
    def ChangeMinorConfiguration(self, TargetSample: Teamcenter.Soa.Client.Model.ModelObject, SourceObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2014_10.ModelConfiguration.ChangeMinorConfigurationResponse: ...

class ModelConfigurationService:
    """
    
            This service contains utilities to assist with configuring application model (Mdl0ApplicationModel)
            content, specifically subclasses of conditional model elements (Mdl0ConditionalElemet).
            
            
            Currently one operation is provided by this service (findRevisionRulesForModel)which
            returns revision rules which are valid for configuring Mdl0ConditionalElements.
            
            Use Case 1: Perform a Configured Search of an Application Model 


Find/select the application model of interest (e.g. using a saved
            queries)
            
Use operation findRevisionRulesForModel
            to get the list of valid revision rules for configuring application models.  Display
            this list to the user so they can select one.
            
Allow the user to set (additional) effectivity criteria on revision
            rule, if they choose.
            
Create a configuration context (using operations from Search service) which references the selected (and possibly modified
            revision rule)
            
Execute the search (using operations from Search
            service)
            


            Use Case 2: Change Presented Configuration of an Application Model 


When build display for presenting configured application models,
            give the user a button or menu which allows them to change the revision rule used
            to configure the model.
            
Use operation findRevisionRulesForModel
            to get the list of valid revision rules for configuring application models.  Display
            as options in the UI for the user to pick from.
            
When user picks a new revision rule, reload and display content of
            the model based on the new revision rule.
            




Library Reference:

Mdl0SoaModelCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ModelConfigurationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def FindRevisionRulesForModel(self) -> Mdl0.Services.Strong.Modelcore._2011_06.ModelConfiguration.FindRevisionRulesForModelResponse:
        """    
             Finds all revision rules which are valid for configuring content (subtypes of Mdl0ConditionalElement
             and Mdl0ConditionalArtifact) of an application model (Mdl0ApplicationModel).Not
             all revision rules can be used to configure application models; this operation aids
             the application in finding the list of revision rules which can be used for this
             type of configuration. (See Teamcenter technical documentation for further information
             regarding valid  revision rules for model content configuration.)
             

Use Cases:

             Users configure application model content to select proper revisions based on criteria
             like Working or Has Status, and by effectivity.   Revision rules capture these
             criteria and are used within Teamcenter to select revisions which match these criteria.
             Because only a subset of all Teamcenter revision rules can be used to configure
             application model content, the user/application needs a way to get the list of valid
             revision rules for this type of configuration.   The findRevisionRulesForModel
             operation is used to get this list.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :return: 
        """
        ...
    def ChangeMinorConfiguration(self, TargetSample: Teamcenter.Soa.Client.Model.ModelObject, SourceObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2014_10.ModelConfiguration.ChangeMinorConfigurationResponse:
        """    
             Change the minor configuration of each sourceObject
             to match the minor revision configuration of targetSample.
             

Use Cases:

             A user is viewing a historical minor revision of an object and wishes to display
             the latest minor revision. You call the changeMinorConfiguration service, passing
             in a targetSample of null and a sourceObjects array containing the historical minor
             revision.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param TargetSample: 
                         Sample object, configured using the target minor configuration. If the sample object
                         is null, the "POM latest" target minor configuration will be used. See <b>Fnd0Cparam</b>.
             
        :param SourceObjects: 
                         A list of objects to re-configure. Both revisable and non-revisable objects are allowed.
             
        :return: 
        """
        ...

class SearchRestBindingStub(SearchService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOrUpdateConfigurations(self, ConfigData: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ConfigurationData]) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.ConfigResponse: ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpInput: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpInput: Mdl0.Services.Strong.Modelcore._2013_05.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpInput: Mdl0.Services.Strong.Modelcore._2014_10.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpressionInput: Mdl0.Services.Strong.Modelcore._2017_05.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpressionInput: Mdl0.Services.Strong.Modelcore._2018_06.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    def ExecuteSearch(self, Recipe: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchRecipe, Options: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchOptions) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchResponse: ...
    def FetchNextSearchResults(self, SearchCursor: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchCursor) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchResponse: ...
    def GetRecipes(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.RecipeResponse: ...
    def SetRecipes(self, RecipeInputs: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.RecipeData]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchCursor) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.StopSearchResponse: ...
    def AggregateRecipes(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2014_10.Search.RecipeResponse2: ...
    def GetRecipes2(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2014_10.Search.RecipeResponse2: ...
    def SetRecipes2(self, RecipeInputs: list[Mdl0.Services.Strong.Modelcore._2014_10.Search.RecipeData2]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetRecipes3(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2018_06.Search.RecipeResponse3: ...
    def SetRecipes3(self, RecipeInputs: list[Mdl0.Services.Strong.Modelcore._2018_06.Search.RecipeData3]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class SearchService:
    """
    
            This service provides operations that enable searching conditional model elements
            (Mdl0ConditionalElement) in a given application model. An application model
            could be a product design (Cpd0CollaborativeDesign in the case of CPD).
            
            Search  service provides the ability to search for conditional model elements using
            various search recipes (spatial and nonspatial). Search service also provides the
            ability to save a search recipe in the database and retrieve a previously stored
            recipe.
            

Use Cases:

            Search service is used by the CPD application to implement Searching CPD Design Components
            (Cpd0DesignElement) within a product design. Search is a generic search capability
            that could be used to search conditional model elements within a given application
            model(Mdl0ApplicationModel). Please refer to the CPD Server Functional Specifications
            for detailed descriptions on application model and model element data schema.
            
            AppModel  search supports searching of model elements based on different search expressions.
            The search expressions could be
            

            Spatial:
            
            Â Â Â Â Box Zone Expression (Mdl0SearchBoxZone)   defines
            a rectangular (axis aligned) box, defined in a 3d space, which could be used to find
            Conditional Model Elements that are either inside/outside/intersecting the 3 dimensional
            box.
            
            Â Â Â Â Plane Zone Expression (Mdl0SearchPlaneZone)   defines
            a 3d plane and the search expression could define to look for Conditional Model Elements
            above/below/intersecting the plane.
            
            Â Â Â Â Proximity Expression (Mdl0SearchProximity)  used to
            find Conditional Model Elements that are spatially nearby a given set of other Conditional
            Model Elements.
            

            Non Spatial:
            
            Â Â Â Â Saved Query Expression (Mdl0SearchSavedQuery)   used
            to search Conditional Model Elements with specific  property values. Accepts wildcards
            for  property values.
            
            Â Â Â Â Include Expression (Mdl0SearchSlctContent) 
            specific set of Model Elements that are included as part of the search result.
            
            Â Â Â Â Exclude Expression (Mdl0SearchGroup)   specific set
            of Model Elements that are excluded from the search result.
            
            Â Â Â Â Partition Expression (Ptn0SearchPartition) 
            Model Elements that are members of a particular set of Partitions in the given Product
            Design.
            
            Â Â Â Â Closure Query Expression (Mdl0SearchOptionSet)
            Return related objects, selected by the given option set and closure rule, as part
            of the search results.
            

            The above search expressions could be joined using AND/OR operators to form
            complex Search Recipes. Also the results of the execution of a Search Recipe could
            be constrained to return only a given set of object types. For e.g. the results of
            a Search Recipe could be restricted to return only Cpd0DesignElement objects.
            The callers could also use NOT operator to negate any of the non spatial expressions
            above and combine them in a Search Recipe (Note that NOT is a Unary operator and
            it accepts only one expression to negate unlike AND/OR which combines multiple
            expressions).
            

            Search Service is typically used to perform the following operations:
            

Create Configuration Context for a CPD session: A CPD client session could
            call createOrUpdateConfigurations to create
            one or more ConfigurationContext objects that hold the RevisionRule and
            Effectivity Rule and Variant Rule that is required to configure the results of a
            Search execution. These ConfigurationContext objects are runtime objects that
            could be used repeatedly by the client throughout the session (over different search
            operations).
            

Create Search Expressions to perform a Search (or Save a Search Recipe): Before
            executing a search or saving a recipe, this is a prerequired step to create the elemental
            search expressions (both Spatial and non Spatial).
            

Execute a Search Recipe: Executes a complex search recipe formed using the
            various search expression combinations and constrained using the search scope (Application
            Model, Search Types). The results of a executing a search could be sorted using the
            one or more of the attributes properties of the returned object type. Also the number
            of objects that should be returned to the caller can be controlled by setting the
            defaultLoadCount. If the default load count is set to zero then all the results are
            returned in one shot.
            
            If the default load count is set to a non zero value, then the caller will be returned
            a search cursor which could be used to get search results as and when it is required.
            Also an active search cursor could be released by calling the stopSearch operation.
            
            Save/Retrieve a stored Search Recipe: Save and Retrieve a complex search recipe in
            the Teamcenter database. Recipes are not independent objects and they would have
            to be stored in an object that exhibits a RecipeContainer behavior. In CPD, There
            are four objects that exhibit RecipeContainer behavior as of now. They are Mdl0SubsetDefinition
            object to store a search recipe, Ptn0Partition  a dynamic partition that
            finds members based on a search operation and Cpd0DesignSubsetInstance  object
            that selects a subset of a Product Design using a search recipe and instantiates
            into a Workset, and Mdl0BaselineDefinition an object which stores a recipe
            for use with an Mdl0BaselineRevision.
            

            Sample code:
            
            Typically following is the sequence of operations to perform a Search:
            
            1. Call createOrUpdateConfigurations and
            create a ConfigurationContext with a valid RevisionRule (optionally
            with effectivity and variant configuration).
            
            2.Call createSearchExpressions and create
            the elemental search expressions.
            
            3.Create the Search Expression Sets to join the elemental search expressions to a
            complex search recipe.
            
            4.Call executeSearch with the complex Search
            Expression Set. executeSearch will return
            a default set of conditional elements (defined by the defaultLoadCount).
            
            5.Call fetchNextSearchResults repeatedly
            to get further results based on the search and each time this operation could be
            called with its own defaultLoadCount value.
            
            6.Â Â Â Â Optionally stopSearch
            could be called to clean up the results and this call would indicate that the caller
            is no longer interested in getting back the remaining search results.
            
            Apart from execution of a search query, there are two operations that help the callers
            to save a Search Recipe and enquire the contents of a persisted Search Recipe. The
            setRecipes2 call saves a Search Recipe and
            it requires a Search Container object to persist the recipe. Currently in CPD application,
            this could be one of either Cpd0DesignSubsetInstance or Ptn0Partition
            or Mdl0SubsetDefinition or Mdl0BaselineDefinition. The getRecipes2 call returns the search expressions and their combinations
            (as Search Expression Sets) of a stored recipe.
            
            The sample in soa_client.zip, com.teamcenter.cpdsearch.SearchServiceSOASampleTest.java
            shows the use of Search operations for the following 2 use cases:
            
            1.Execute a Search with a complex recipe (Saved Query combined with Box Zone and
            the results restricted to Cpd0DesignElement objects)
            
            2.Save and Retrieve a complex recipe on a Recipe Container object
            





Library Reference:

Mdl0SoaModelCoreStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> SearchService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOrUpdateConfigurations(self, ConfigData: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.ConfigurationData]) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.ConfigResponse:
        """    
             This operation creates a configuration context (ConfigurationContext) object
             (or updates a configuration context object). In CPD, the configuration information
             is kept track using a Configuration Context object. This object is not persisted
             in the Database. It is just created and kept alive until the session is active and
             destroyed when the user logs out.
             
             A configuration context keeps track of the Revision Rule (with any attached Effectivity
             Conditions) (and in the future would keep track of variant rule as well) created/used
             by a client session. In Teamcenter 9.1.0, minor revisioning is not supported in CPD.
             When minor revisioning is introduced in Teamcenter 10.1.0, then the configuration
             context will also serve the purpose of allocating a cparam for the corresponding
             Revision Rule used by the client session.
             
             cparam is an object used by the POM revisioning framework to configure the correct
             minor revision of a reviseable object being used.
             
             A configuration context created could be used by the caller during executeSearch or any other operation that requires the revision
             and effectivity configuration settings.
             


Use Cases:

             This operation supports the use case of creating and maintaining configuration context
             objects with different Revision and Effectivity configurations. Also in the future,
             this will be extended to keep track of cparam objects to pick the correct minor revision
             (historical revision) of the object.  The configuration context objects thus created
             are used during execution of a CPD search operation or other operations such getMembers on a partition.
             

Dependencies:

             createOrUpdateConfigurations
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param ConfigData: 
                         Input data structure to create configuration context objects with associated Revision
                         Rule and other configuration conditions.
             
        :return: Returns ConfigResponse data structure.This operation returns runtime configuration
             context objects.
        """
        ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpInput: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpInput: Mdl0.Services.Strong.Modelcore._2013_05.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpInput: Mdl0.Services.Strong.Modelcore._2014_10.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpressionInput: Mdl0.Services.Strong.Modelcore._2017_05.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    @typing.overload
    def CreateSearchExpressions(self, SearchExpressionInput: Mdl0.Services.Strong.Modelcore._2018_06.Search.SearchExpressionInput) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchExpressionResponse: ...
    def ExecuteSearch(self, Recipe: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchRecipe, Options: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchOptions) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchResponse:
        """    
             Operation that executes a search based on an input Search Recipe and returns the
             list of Model Elements (Mdl0ModelElement) back to the caller. Search Recipe
             could be a complex expression set that combines multiple simpler search terms (both
             spatial and non spatial) in a logical sequence.
             
             Search is always executed within the scope of an Application Model and all the Model
             Elements returned belong to the given Application Model. executeSearch
             operation uses the configuration information given in the recipe to configure the
             results of a search (Both Revision and Effectivity Configurations).
             
             The results of a search are returned one set at a time based on the defaultLoadCount specified in the SearchOptions.
             The SearchResponse also contains a Search
             Cursor object that the caller could use to fetch the next set of results by invoking
             the fetchNextSearchResults call. Search options
             also gives the caller the ability to sort the results of a search using any (one
             or more) of the attributes of the returned objects.
             

Use Cases:

             This API provides the ability for searching Model Content in a given Application
             Model. Application Model is a construct in AppModel template that defines an abstract
             boundary in which content could be populated. The populated model content is called
             Model Element which again is an abstract object which has some basic attributes such
             as an ID, revision Id, name and description.
             
             CPD has specialized the Application Model to be a Product Design and the Model Element
             to be a Design Component. In this context, the executeSearch
             API provides the ability to Search for Design Components in a Product Design using
             various Search terms (combined together as a Search Recipe).
             
             The Search term could be spatial (searching for objects in a 3d space specified by
             a bounding box or a 3d plane or proximity to another Design Component) or an attribute
             term (Saved Query searching for Design Components with specific attribute values/patterns)
             or a partition term (Searching for membership in specific segments of a Product Design).
             
             The results of the execute search operation could be constrained by the search scope
             which is part of the search recipe and organized by the search options.
             


Dependencies:

             getConfigurableProducts, getEffectivityConditions, fetchNextSearchResults, stopSearch
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param Recipe: 
                         Recipe for executing the search
             
        :param Options: 
                         Search Options for a given Search (load count and sorting)
             
        :return: object
        """
        ...
    def FetchNextSearchResults(self, SearchCursor: Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchCursor) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.SearchResponse:
        """    
             This operation gets the next set of Model Elements from a previously executed search
             results. The results returned will be based on the load count specified in the SearchCursor input structure. This API returns
             the same response structure as that of executeSearch.
             

Use Cases:

             This API is used in conjunction with executeSearch
             operation. executeSearch operation is a prerequisite for invoking fetchNextSearchResults. The search cursor returned by the executeSearch is used to call fetchNextSearchResults operation. This operation could be called
             repeatedly by the caller, until all the search results are returned.
             

Dependencies:

             fetchNextSearchResults
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SearchCursor: 
<ul>
<li type="disc"><font face="courier" height="10">cursor</font>  A runtime object
                         identifier that keeps track of the Search results and the corresponding indexes as
                         of where the caller has consumed the results
                         </li>
<li type="disc"><font face="courier" height="10">loadCount</font>  An integer number
                         that specifies the number of objects to be fetched from the Search result set. If
                         the <font face="courier" height="10">loadCount</font> is zero (or more than the number
                         of objects left in the result set) then all the remaining objects in the result set
                         is returned.
                         </li>
</ul>

        :return: structure
        """
        ...
    def GetRecipes(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.RecipeResponse:
        """    
             This operation retrieves the stored recipe against a set of recipe container objects.
             The persistent objects used to store the search recipe in Teamcenter are objects
             that do not have lifecycle by itself, so they are always associated to objects that
             exhibit the RecipeContainer behavior. In the current CPD application there
             are three objects that exhibit RecipeContainer behavior. They are
             

Mdl0SubsetDefinition:  object to store a search recipe (without
             the results)
             
Ptn0Partition:   A dynamic partition that executes the search
             recipe to find its members
             
Cpd0DesignSubsetInstance:  A realization object that takes
             a subset of a Product Design and instantiates into a Workset.
             


             The retrieved recipe from the recipe container is translated to the data structures
             defined in the Search SOA service and then it is presented back to the caller.
             

Use Cases:

             This operation supports the use case of retrieving a stored search recipe from Teamcenter
             DB against a recipe container object. The retrieved recipe could be reexecuted by
             calling executeSearch operation.
             

Dependencies:

             getRecipes
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeContainers: 
                         reference to <b>RecipeContainer</b> Objects. The input vector could contain any Teamcenter
                         object that exhibits a <b>RecipeContainer</b> behavior.
             
        :return: data structure
        """
        ...
    def SetRecipes(self, RecipeInputs: list[Mdl0.Services.Strong.Modelcore._2011_06.Search.RecipeData]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation saves a search recipe as persistent objects in Teamcenter. The stored
             recipe could be retrieved using getRecipes operation. This is a bulk operation, i.e.
             it can store multiple complex search recipes in a single call.
             
             The persistent objects used to store the search recipe in Teamcenter are objects
             that do not have lifecycle by itself, so they are always associated to objects that
             exhibit the RecipeContainer behavior. In the current CPD application there
             are three objects that exhibit RecipeContainer behavior. They are
             

Mdl0SubsetDefinition  object to store a search recipe (without
             the results)
             
Ptn0Partition   A dynamic partition that executes the search
             recipe to find its members
             
Cpd0DesignSubsetInstance   A realization object that takes
             a subset of a Product Design and instantiates into a Workset.
             


             Note that the recipe is deleted when its container object is deleted.
             

Use Cases:

             The setRecipes operation is used to save
             search recipes against a Recipe Container object. Apart from capturing the logical
             combination of search expressions, the setRecipes
             also stores the current configuration conditions against the RecipeContainer
             object (Revision Rule and Effectivity Rule), except in the case of Ptn0Partition
             object. Ptn0Partition object does not provide a persistence mechanism for
             the configuration conditions and it uses the configuration set in the current CPD
             application.
             
             The search recipes are stored as ApprSearchCriteria objects in Teamcenter
             and ApprSearchCriteria object hierarchy has a subclass to store each Search
             expression separately.
             


Dependencies:

             convertEffectivityExpressions, createOrUpdateConfigurations, createSearchExpressions
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeInputs: 
                         Recipe Data that should be set for specific Container Objects
             
        :return: data structure.
        """
        ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.Strong.Mdl0SearchCursor) -> Mdl0.Services.Strong.Modelcore._2011_06.Search.StopSearchResponse:
        """    
             This operation stops further loading of objects from a previously executed search
             and clears all the memory allocated for the search operation. It deletes the search
             cursor and the list of Model Elements that are kept track by the Search cursor from
             the Server Memory.
             
             The stopSearch does not unload any previously
             loaded Model Elements. Also there is no locking or unlocking performed by the stopSearch operation.
             


Use Cases:

             When a search is executed in CPD and the search returns a large set of objects. The
             server process keeps the results of a search using a search cursor object. At each
             fetchNextSearchResults operation, the results
             are further filtered and returned in batches specified by the load count. However
             if the caller is not interested in consuming the search results further, then a stopSearch could be called to release all the resources
             allocated for that search operation. This includes dropping the runtime search cursor
             object and the list of Model Elements kept track by the cursor.
             

Dependencies:

             executeSearch, fetchNextSearchResults
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param SearchCursor: 
                         Search Cursor for stopping the search
             
        :return: data structure.
        """
        ...
    def AggregateRecipes(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2014_10.Search.RecipeResponse2:
        """    
             Return the aggregate recipe for each given recipe container. Recipe containers are
             not modified by this operation; however the aggregate recipes returned are suitable
             for storage using the operation setRecipes2.
             
                 
             
             For an Mdl0BaselineDefinition recipe container, the aggregate recipe is formed
             from the baseline definition recipe and the recipe of each supporting baseline (see
             relation Mdl0SupportingBaseline) in the following way:
             

             1. The aggregate recipe is set to a copy of the baseline definition recipe.
             

             2. Each supporting recipe is assigned a name using the display name of its owning
             Mdl0Baseline.
             

             3. For each supporting recipe group:
             
             If the aggregate group contains one or more recipe groups which match the assigned
             name: the contents of each group is replaced with a copy of the supporting recipe.
             
             Else: the aggregate group is appended to the recipe, using a recipe group with the
             assigned name.
             

             4. New groups are appended using the OR operator.
             

             For all other recipe containers the aggregate recipe is identical to the recipe returned
             by operation getRecipes2.
             


Use Cases:

             A user is constructing an aggregate baseline from a number of supporting baselines.
             Construction has now finished on the supporting baselines, and the user wishes to
             pull the recipes from the supporting baselines into the aggregate baseline. Call
             the aggregateRecipes operation to pull the
             recipes together, confirm any changes with the user, then call the setRecipes2 operation to save the changes.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeContainers: 
                         Reference to <b>RecipeContainer</b> objects. The input vector could contain any Teamcenter
                         object that exhibits a <b>RecipeContainer</b> behavior.
             
        :return: 
        """
        ...
    def GetRecipes2(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2014_10.Search.RecipeResponse2:
        """    
             This operation retrieves the stored recipe against a set of recipe container objects.
             The persistent objects used to store the search recipe in Teamcenter are objects
             that do not have lifecycle by itself, so they are always associated to objects that
             exhibit the RecipeContainer behavior. In the current CPD application there are four
             objects that exhibit RecipeContainer behavior. They are:
             

             Mdl0SubsetDefinition:  object to store a search recipe (without the results).
             
             Ptn0Partition:   A dynamic partition that executes the search recipe to find
             its members.
             
             Cpd0DesignSubsetInstance:  A realization object that takes a subset of a Product
             Design and instantiates into a Workset.
             
Mdl0BaselineDefinition: object to store a search recipe (without the results)
             for use an Mdl0BaselineRevision.
             

             The retrieved recipe from the recipe container is translated to the data structures
             defined in the search operation and then it is presented back to the caller.
             

Use Cases:

             This operation supports the use case of retrieving a stored search recipe from Teamcenter
             DB against a recipe container object. The retrieved recipe could be re-executed by
             calling the executeSearch operation.
             


Dependencies:

             getRecipes2
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeContainers: 
                         reference to RecipeContainer Objects. The input vector could contain any Teamcenter
                         object that exhibits a RecipeContainer behavior.
             
        :return: 
        """
        ...
    def SetRecipes2(self, RecipeInputs: list[Mdl0.Services.Strong.Modelcore._2014_10.Search.RecipeData2]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation saves a search recipe as persistent objects in Teamcenter. The stored
             recipe could be retrieved using getRecipes2
             operation. This is a bulk operation, i.e. it can store multiple complex search recipes
             in a single call.
             
             The persistent objects used to store the search recipe in Teamcenter are objects
             that do not have lifecycle by itself, so they are always associated to objects that
             exhibit the RecipeContainer behavior. In the current CPD application there
             are four objects that exhibit RecipeContainer behavior. They are:
             

Mdl0SubsetDefinition: object to store a search recipe (without the results).
             


             Ptn0Partition: A dynamic partition that executes the search recipe to find its
             members.
             


             Cpd0DesignSubsetInstance: A realization object that takes a subset of a Product
             Design and instantiates into a Workset.
             


             Mdl0BaselineDefinition: object to store a search recipe (without the results)
             for use with historical dataan Mdl0BaselineRevision.
             

             Note that the recipe is deleted when its container object is deleted.
             

Use Cases:

             The setRecipes2 operation is used to save
             search recipes against a Recipe Container object. Apart from capturing the logical
             combination of search expressions, the setRecipes2
             operation also stores the current configuration conditions against the RecipeContainer
             object (including RevisionRule and optional effectivity and variant configuration),
             except in the case of Ptn0Partition object. Ptn0Partition object does
             not provide a persistence mechanism for the configuration conditions and it uses
             the configuration set in the current CPD application.
             
             The search recipes are stored as ApprSearchCriteria objects in Teamcenter
             and ApprSearchCriteria object hierarchy has a subclass to store each Search
             expression separately.
             


Dependencies:

             convertEffectivityExpressions, createOrUpdateConfigurations, createSearchExpressions
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param RecipeInputs: 
                         List of Recipe Data that should be set for specific Container Objects
             
        :return: 
        """
        ...
    def GetRecipes3(self, RecipeContainers: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Mdl0.Services.Strong.Modelcore._2018_06.Search.RecipeResponse3: ...
    def SetRecipes3(self, RecipeInputs: list[Mdl0.Services.Strong.Modelcore._2018_06.Search.RecipeData3]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

