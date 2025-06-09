import Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints
import Mdl0.Services.Strong.Modelcore._2015_07.GeometricConstraints
import System
import System.Collections
import Teamcenter.Soa.Client.Model.Strong
import typing

class DataSetInfo2:
    """
    
            A structure used to create new Datasets and files when needed (either on initial
            creation or when a new saved state iteration is constructed.)
            
    """
    def __init__(self, ) -> None: ...
    DataSetType: str
    """The name of dataset type to create when a new Dataset is required."""
    NameReferenceFileMap: System.Collections.Hashtable
    """
            A map (string,string) of named reference type name by which the CAD constraint file
            is associated to the existing or new Dataset and name of file excluding path
            that CAD tool will upload containing CAD constraints.
            """
    DatasetLastModifiedDateGuard: System.DateTime
    """
            Modification date guard is used if datasetLastModifiedDateGuard is not null.
            Dataset update will abort with error if the last modified date of the Dataset
            in the database is not same as datasetLastModifiedDateGuard.
            """

class UpdateContainerInfo3:
    """
    
            Specifies the full set of inputs required to update the geometric constraint container's
            members and possibly create a new constraint Dataset (if a new container iteration
            is required)
            
    """
    def __init__(self, ) -> None: ...
    AreConstraintsFullySolved: bool
    """
            If true, CAD constraints have been fully solved by the CAD tool. If false, CAD constraints
            could not be fully solved by the CAD tool or if the CAD tool has not yet attempted
            to solve the constraints.
            """
    AttrInfoMap: System.Collections.Hashtable
    """
            A map (string, list of strings) used to specify additional property data for owner
            model element. All values are specified as strings, the caller is responsible for
            generating the correct string representation of each value passed.
            """
    ConstraintAttrInfoMap: System.Collections.Hashtable
    ConstraintData: DataSetInfo2
    """
            The details needed to either update the existing CAD constraint dataset or create
            a new one.
            
            The CAD constraint dataset will contain details about the CAD constraints for which
            the constraint container is being updated.
            """
    ConstraintOptionsMap: System.Collections.Hashtable
    """A map (string, bool) used to decide whether to overwrite iteration or not."""
    MemberList: list[Mdl0.Services.Strong.Modelcore._2015_07.GeometricConstraints.UpdateMembership]
    """
            The positioned model elements objects upon which constraints in the constraintData
            Dataset depends or are affecting.
            """
    Owner: Teamcenter.Soa.Client.Model.Strong.Mdl0ModelElement
    """
            The model element that owns the geometric constraint container behaviour.The container
            owner object must be provided.
            """
    SystemManaged: bool
    """
            If true, a CAD tool has constructed the set of members for this constraint collection;
            otherwise, a user has manually collected the members and their constraints into this
            new collection.
            """
    UpdateIteration: int
    """
            The precise, 'as-saved' state of a set of constraints as defined in CAD. Unset for
            the first update of the owner object's constraint container.The precise, 'as-saved'
            state of a set of constraints as defined in CAD. Unset or zero for the first update
            of the owner object's constraint container.
            
            Otherwise it is the iteration based on which an update is being requested.
            """

class GeometricConstraints:
    """
    Interface GeometricConstraints
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def UpdateContainer3(self, ContainerInfo3: list[UpdateContainerInfo3]) -> Mdl0.Services.Strong.Modelcore._2014_10.GeometricConstraints.UpdateContainerResponse: ...

