import Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints
import System.Collections
import Teamcenter.Soa.Client.Model.Strong
import typing

class UpdateContainerInfo2:
    """
    
            Specifies the full set of inputs required to update the geometric constraint container's
            members and possibly create a new constraint Dataset (if a new container iteration
            is required)
            
    """
    def __init__(self, ) -> None: ...
    Owner: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            The model element that owns the geometric constraint container behaviour.The container
            owner object must be provided.
            """
    AttrInfoMap: System.Collections.Hashtable
    """
            A set of name-value pairs used to specify additional property data for the owner
            model element. All values are specified as strings, the caller is responsible for
            generating the correct string representation of each value passed. For tag values,
            the UID of the tag is used.
            """
    ConstraintAttrInfoMap: System.Collections.Hashtable
    """
            A set of name-value pairs used to specify additional property data for the constraint
            container's initial saved state. All values are specified as strings, the caller
            is responsible for generating the correct string representation of each value passed.
            For tag values, the UID of the tag is used.
            
            These pairs may be optional or mandatory depending on the properties of the container
            being set.
            """
    UpdateIteration: int
    """
            The precise, 'as-saved' state of a set of constraints as defined in CAD. Unset for
            the first update of the owner object's constraint container.The precise, 'as-saved'
            state of a set of constraints as defined in CAD. Unset or zero for the first update
            of the owner object's constraint container.
            
            Otherwise it is the iteration based on which an update is being requested.
            """
    MemberList: list[UpdateMembership]
    """
            The positioned model elements objects upon which constraints in the constraintData Dataset depends or are affecting.
            """
    ConstraintData: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.DataSetInfo
    """
            The details needed to either update the existing CAD constraint dataset or create
            a new one.
            
            The CAD constraint dataset will contain details about the CAD constraints for which
            the constraint container is being updated.
            """
    AreConstraintsFullySolved: bool
    """
            if CAD constraints have been fully solved by the CAD tool,the value is true otherwise
            false.
            """
    SystemManaged: bool
    """
            If true, indicates that some CAD tool has constructed the set of members for this
            constraint collection, not a user. If false, then a user has manually collected the
            members and their constraints into this new collection.
            """
    ConstraintOptionsMap: System.Collections.Hashtable
    """
            Map of constraint option like shouldOverwriteIteration
            as key and value is either true or false.If user dont want to overwriteIteration,
            false will be passed as input.By default the true will be passed as input.
            """

class UpdateMembership:
    """
    Specifies inputs required to update  member of the geometric constraint container.
    """
    def __init__(self, ) -> None: ...
    Membership: Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.Membership
    """
            The positioned model element object upon which constraints in the constraint Dataset
            depends or are affecting.
            """
    MemberToRemove: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Reference to positioned model element. When a member of membership is also
            specified, it will replace memberToRemove. Otherwise memberToRemove
            will be simply removed from the constraint.
            """

class GeometricConstraints:
    """
    Interface GeometricConstraints
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateContainer2(self, ContainerInfo2: list[UpdateContainerInfo2]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerResponse:
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

