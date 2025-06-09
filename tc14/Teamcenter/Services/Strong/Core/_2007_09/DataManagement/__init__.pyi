import System
import Teamcenter.Services.Strong.Core._2007_06.DataManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExpandGRMRelationsData2:
    """
    
            The data returned from expandGRMRelationsPrimary
            and expandGRMRelationsSecondary operations.
            
    """
    def __init__(self, ) -> None: ...
    RelationshipObjects: list[ExpandGRMRelationship]
    """
            The list of relation objects for the relationships between the input object and side
            objects.
            """
    RelationName: str
    """The input Generic Relationship Manager (GRM) relation type name."""

class ExpandGRMRelationship:
    """
    
            The relation information returned from expandGRMRelationsPrimary
            and expandGRMRelationsSecondary operations.
            
    """
    def __init__(self, ) -> None: ...
    OtherSideObject: Teamcenter.Soa.Client.Model.ModelObject
    """The found side object."""
    Relation: Teamcenter.Soa.Client.Model.Strong.ImanRelation
    """The found relation object for the side object to primary object relationship."""

class ExpandGRMRelationsOutput2:
    """
    
            The output from expandGRMRelationsPrimary
            and expandGRMRelationsSecondary operations.
            
    """
    def __init__(self, ) -> None: ...
    InputObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object that was input to be expanded."""
    RelationshipData: list[ExpandGRMRelationsData2]
    """The list of data for relationships between the input object and found side objects."""

class ExpandGRMRelationsPref2:
    """
    
            Preference structure for expandGRMRelationsPrimary
            and expandGRMRelationsSecondary.
            
    """
    def __init__(self, ) -> None: ...
    ExpItemRev: bool
    """
            Flag that if true signifies that any item revisions that are in the return data should
            be expanded.
            """
    ReturnRelations: bool
    """Flag that if true signifies that the relation objects should be returned."""
    Info: list[Teamcenter.Services.Strong.Core._2007_06.DataManagement.RelationAndTypesFilter]
    """
            The list of relation type and primary or secondary object type filters, depending
            on whether expandGRMRelationsForPrimary or
            expandGRMRelationsForSecondary is called.
            This input must be specified or error 214160 will be returned.  For expandGRMRelationsForPrimary, if all secondary objects should
            be returned, RelationAndTypesFilter input
            parameters should be empty.  For expandGRMRelationsForSecondary,
            if all primary objects should be returned, RelationAndTypesFilter
            input parameters should be empty.
            """

class ExpandGRMRelationsResponse2:
    """
    
            The response from expandGRMRelationsPrimary
            and expandGRMRelationsSecondary operations.
            
    """
    def __init__(self, ) -> None: ...
    Output: list[ExpandGRMRelationsOutput2]
    """The list of input objects and the found related side objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The ServiceData.  This operation will populate
            the ServiceData with the input object, any
            found side object and any found relation object.  All objects are added as plain
            objects.
            """

class NamedReferenceInfo:
    """
    This structure contains information for NamedReference to be removed.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    Type: str
    """
            Remove all NamedReferences of this reference
            name ( required )
            """
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """
            Target object of a specific NamedReference
            to remove ( optional, must match type above ) ) If specified then only this specific
            NamedReference will be removed; other NamedReferences of the same type will not be effected.
            """
    DeleteTarget: bool
    """
            Flag to indicate if targetObject is to be
            deleted
            """

class RemoveNamedReferenceFromDatasetInfo:
    """
    
            Input structure for the removeNamedReferenceFromDataset
            operation
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller.  This ID is used to identify return data
            elements and partial errors associated with this input structure.  If clientId is not provided then it can be difficult to align the
            input with any returned errors.
            """
    Dataset: Teamcenter.Soa.Client.Model.Strong.Dataset
    """The dataset object from which to remove the specified named references."""
    NrInfo: list[NamedReferenceInfo]
    """A list of named reference information."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def RemoveNamedReferenceFromDataset(self, Inputs: list[RemoveNamedReferenceFromDatasetInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes the specified named references from a dataset.
             

             If the NamedReferenceInfo.targetObject input
             is not specified then all named references of the type specified are removed from
             the dataset.  If the NamedReferenceInfo.targetObject
             input is specified then only that named reference is removed from the dataset.  If
             the NamedReferenceInfo.deleteTarget input
             is true then the NamedReferenceInfo.targetObject
             will be deleted if it is no longer referenced.
             


Use Cases:

             User deletes a single named reference from a dataset that has multiple named references
             of the same type.
             

             For this operation, the dataset is passed in along with the named reference type
             and object reference for the specific named reference to be removed from the dataset.
             The specific named reference is removed from the dataset and the dataset is added
             to the ServiceData list of updated objects.
             

Teamcenter Component:

             Core Model Dataset - A set of capabilities/functionality (data model and behaviours)
             that form the very core of Teamcenter PLM platform.  This component defines class
             'Dataset' behavior.
             
        :param Inputs: 
                         A list of datasets and the named references to be removed from the datasets.
             
        :return: 
        """
        ...
    def ExpandGRMRelationsForPrimary(self, PrimaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: ExpandGRMRelationsPref2) -> ExpandGRMRelationsResponse2:
        """    
             This operation returns the secondary objects that are related to the input primary
             objects.  Relation type names and secondary object types can be input as a filter
             to reduce the set of returned secondary objects.  In the context of expanding primary
             objects, secondary objects may be referred to as side objects. If no relation type
             names or secondary object types are input, then all related objects will be returned.
             

             For improved performance, if an item is the output of the expansion, then its associated
             item revisions and the datasets for those item revisions will be returned.  Similarly,
             if an item revision is the output of the expansion, then its associated datasets
             will be returned.
             


Use Cases:

             User wants to see all the secondary objects related to the input primary item object.
             

             For this operation, the item object is input in primaryObjects
             and the filter preference info relationTypeName and otherSideObjectTypes
             parameters are set to be empty.  All secondary objects that have a relation to the
             item are returned in ExpandGRMRelationsOutput2
relationshipData.  The primary object, secondary
             objects and relation objects are returned as plain objects in the ServiceData.
             


Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param PrimaryObjects: 
                         The list of Teamcenter primary objects.
             
        :param Pref: 
                         The structure for setting specific preference input used by this operation.
             
        :return: 
        """
        ...
    def ExpandGRMRelationsForSecondary(self, SecondaryObjects: list[Teamcenter.Soa.Client.Model.ModelObject], Pref: ExpandGRMRelationsPref2) -> ExpandGRMRelationsResponse2:
        """    
             This operation returns the primary objects that are related to the input secondary
             objects.  Relation type names and secondary object types can be input as a filter
             to reduce the set of returned primary objects.  In the context of expanding secondary
             objects, primary objects may be referred to as side objects.  If no relation type
             names or secondary object types are input, then all related objects will be returned.
             

             For improved performance, if an item is the output of the expansion, then its associated
             item revisions and the datasets for those item revisions will be returned.  Similarly,
             if an item revision is the output of the expansion, then its associated datasets
             will be returned.
             


Use Cases:

             User wants to see all the primary objects related to the input secondary dataset
             object.
             

             For this operation, the dataset object is input in secondaryObjects
             and the filter preference info relationTypeName
             and otherSideObjectTypes parameters are set
             to be empty.  All primary objects that have a relation to the dataset are returned
             in ExpandGRMRelationsOutput2 relationshipData.  The secondary object, primary objects and relation
             objects are returned as plain objects in the ServiceData.
             


Teamcenter Component:

             GRM - The Generic Relationship Manager (GRM) module supports the concept of explicit
             relationships. One can define and enforce specific rules pertaining to relationships,
             as well as separate the maintenance of relationships from the data itself.
             
        :param SecondaryObjects: 
                         The list of Teamcenter secondary objects.
             
        :param Pref: 
                         The structure for setting specific preference input used by this operation.
             
        :return: 
        """
        ...
    def LoadObjects(self, Uids: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Load business objects into the client data model for each of the UIDs supplied. The
             business objects are loaded from the Teamcenter server's in memory cache of business
             objects or from the database. UIDs of runtime business objects (BOMLines)
             that are not currently loaded in the Teamcenter server's memory will result in a
             partial error being returned.
             

Teamcenter Component:

             SOA Framework - The framework to expose the Teamcenter services to the clients.
             The framework provices the means to define service interfaces (through BMIDE) and
             exposes those in Java, C++, C# client bindings. The Session service is part of the
             framework.
             
        :param Uids: 
                         An array of UIDs. These UID may come from an outside source or from other service
                         operations such as executeSavedQuery.
             
        :return: 
        """
        ...

