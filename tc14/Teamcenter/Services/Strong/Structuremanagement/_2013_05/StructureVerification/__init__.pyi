import System
import Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification
import Teamcenter.Soa.Client.Model
import typing

class AttributeDetailElement:
    """
    Comparison result of an attribute in an Attribute Group.
    """
    def __init__(self, ) -> None: ...
    AttributeNames: list[str]
    """
            Corresponding attribute names for each member  of the equivalentObjects vector. The
            size of this vector matches the size of equivalentObjects vector and it has corresponding
            indices.
            """
    IsDifferent: bool
    """False if the property value is equal in the source and target, otherwise true."""

class AttributeGroupAndFormComparisonResponse:
    """
    
For each supplied attribute group the operation returns the list of its
attributes,
the attributes' values for each supplied source and target, and the result of
comparing
each attribute on all supplied sources and targets.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the property values for each property in each attribute group for each supplied
            equivalent set and any partial errors.
            """
    AttributeGroupAndFormDetails: list[AttributeGroupAndFormDetail]
    """List of attribute groups information elements - one for each input equivalent set."""

class AttributeGroupAndFormDetail:
    """
    Attribute groups details of an equivalent set of objects.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """Index of equivalent set in the input vector for which these details were calculated."""
    EquivalentObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The list of all equivalent business objects in the input equivalent set (all equivalent
            sources in sequence and then all targets in sequence).
            """
    AttributeGroupDetailElements: list[AttributeGroupsDetailElement]
    """
            Attribute groups details of this equivalent set. Each element in the list represents
            one attribute group.
            """

class AttributeGroupsDetailElement:
    """
    Comparison results of an Attribute Group.
    """
    def __init__(self, ) -> None: ...
    AttributeGroupName: str
    """The name of this attribute group."""
    IsDifferent: bool
    """True if any of the properties in this attribute group are different, otherwise false."""
    AttrGroupsAndForms: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            Corresponding attribute groups and forms objects for each member of the equivalentObjects
            vector.   The size of this vector matches the size of equivalentObjects vector and
            it has corresponding indices.
            """
    AttributeDetails: list[AttributeDetailElement]
    """The list of details for each mapped property in the attribute group."""

class BusinessObjectVec:
    """
    Vector of business objects.
    """
    def __init__(self, ) -> None: ...
    BusinessObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """Vector of business objects."""

class ConnectedObjectsComparisonResponse:
    """
    
For each input set of equivalent objects a vector of comparison results of their
connected elements (can be full match, partial match, or multiple match) and for
each object in the set a detailed connected elements breakdown.
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Object that captures any partial errors."""
    ConnectedObjectsDetails: list[ConnectedObjectsDetail]
    """List of connected objects information elements - one for each input equivalent set."""

class ConnectedObjectsDetail:
    """
    
Comparison results of connected elements of an equivalent set of objects (can be
full match, partial match, or multiple match) and for each object in the set a
detailed
connected elements breakdown.
    """
    def __init__(self, ) -> None: ...
    Index: int
    """The index of equivalent set in the input list for which these details were calculated."""
    MatchResults: list[int]
    """
            A list of the comparison results (0 means full match, 1 means partial match, 2 means
            multiple match) of all rows of the output table. Each vector element is the result
            of comparing one equivalent group of connected objects (one row in the table).
            """
    ConnectedObjectsDetails: list[ConnectedObjectsDetailElement]
    """
            A list of input equivalent object and its detailed set of connected elements. This
            vector contains the whole ouput results table, where each vector element represents
            a column in the table.
            """

class ConnectedObjectsDetailElement:
    """
    Contains connected objects of the equivalentObject.
    """
    def __init__(self, ) -> None: ...
    EquivalentObject: Teamcenter.Soa.Client.Model.ModelObject
    """The input equivalent object for which these details are defined."""
    ConnectedObjects: list[BusinessObjectVec]
    """
            The set of connected objects for this input object. The outer vector is  insync with
            the index of the matchResults, each element representing one cell in the output table,
            and the inner vector will be the group of connected elements that are equivalent
            to each other (if there are no equivalent elements in this group at all the inner
            vector will be empty). Each inner list will have only one element, and all equivalent
            elements will be put in separate inner list.
            """

class StructureVerification:
    """
    Interface StructureVerification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAttributeGroupsAndFormsComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], AttributeGroupsNames: list[str]) -> AttributeGroupAndFormComparisonResponse:
        """    
             This operation returns the details of differences between the supplied Attribute
             Groups for the supplied equivalent objects (that can be Cpd0DesignElement, Cpd0DesignFeature,
             or BOMLine objects). For each supplied attribute group the operation returns the
             list of its attributes, the attributes values for each supplied source and target,
             and the result of comparing each attribute on all supplied sources and targets.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         The list ofCpd0DesignElement, Cpd0DesignFeature or BOMLine objects that  were deemed
                         equivalent by some method, for which any differences in attribute groups is required.
             
        :param AttributeGroupsNames: 
                         The list of attribute groups names that need to be compared.
             
        :return: For each supplied attribute group the operation returns the list of its attributes,
             the attributes' values for each supplied source and target, and the result of comparing
             each attribute on all supplied sources and targets. The following partial errors
             may be returned: - 253049 The input equivalent set doesn't contain any sources or
             any targets. - 253001 This error can only be returned if there is some kind of environment
             issue or a bug in the code, it will never happen during normal execution.
        """
        ...
    def GetConnectedObjectsComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines]) -> ConnectedObjectsComparisonResponse:
        """    
             This operation returns the details of any differences between connected objects (that
             can be either BOMLines or Cpd0DesignElements) for the supplied equivalent objects
             (that can be either BOMLines or Cpd0DesignFeatures). The operation takes the source
             and target and compares their connected objects. The source and target connected
             objects are returned by this operation in the form of a table that is created by
             the output structures.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         The list of BOMLines or Cpd0DesignFeatures that were deemed  equivalent  by some
                         method, for which any differences in connected objects are required.
             
        :return: For each input set of equivalent objects a list of comparison results of their connected
             elements (can be full match, partial match, or multiple match) and for each object
             in the set a detailed connected elements breakdown. The following partial errors
             may be returned:  - 253049 The input equivalent set doesn't contain any sources or
             any targets. -  253001 This error can only be returned if there is some kind of environment
             issue or a bug in    the code, it will never happen during normal execution.
        """
        ...

