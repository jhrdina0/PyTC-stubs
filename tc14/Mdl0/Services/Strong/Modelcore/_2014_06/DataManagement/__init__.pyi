import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class RelatedObjectFilter:
    """
    
            This filter can specify a combination of the type of the relation to traverse, the
            possible attributes on the relation, and the type of Business Object at the other
            end of that relation. An empty string denotes no filter (acts as a wildcard returning
            all objects without filtering the particular aspect that is not specified).
            
            The combination of filters specified by relatedTypeName, all filters and otherSideObjectTypeName
            are combined together with a logical AND operation, meaning all criteria must be
            met for the related object to be returned to the caller.
            
            WARNING:  Any attribute filter other than mdl0cs_id, if passed in, will cause a not
            implemented error and a service exception.  This service may be extended in the future
            to support filtering on any relation attribute.
            
    """
    def __init__(self, ) -> None: ...
    RelationTypeName: str
    """
            Relation name for the relationship between input source objects and output related
            objects. If not specified, then all relations will be considered.
            """
    OtherSideObjectTypeName: str
    """
            The type of related objects to be queried for the given relation. If not specified,
            all related objects for the given relation name are queried.
            """
    Filters: list[RelationAttributeFilter]
    """
            Filters based on a list of relation attribute values.  If the list is empty, then
            no relationship attribute filtering is applied.  NOTE: Currently only one attribute,
            mdl0cd_id, is supported
            """

class RelatedObjectInput:
    """
    
            RelatedObjectInput specifies the input for the query. It provides:
            

Source Objects that form the starting point of the relation navigation
            
Configuration Context that should be satisfied by the related objects
            
Filters (relations and other criteria) for fetching related objects.
            
Direction of navigation; i.e. whether to fetch primary or secondary
            with source objects being as reference
            
Flag to specify whether or not the relation objects are to be returned
            



            A vector of such RelatedObjectsInput structures are passed as input to the queryRelatedObjects
            operation.
            
    """
    def __init__(self, ) -> None: ...
    SourceObjects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The input (source) objects for which related objects are to be found."""
    ConfigurationContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """
            Configuration criteria to apply to the filtered set of related primary or secondary
            objects. Only those related objects that satisfy to the configuration criteria would
            be returned.
            """
    Filters: list[RelatedObjectFilter]
    """
            A set of filters to apply to the objects related to the sourceObject.  An empty filter
            list denotes no filter ( acts as a wildcard returning all objects without filtering).
            """
    QueryPrimaries: bool
    """
            A boolean flag to set the direction of navigation across the relation while fetching
            the related objects.
            

If set to true, it will return those objects that are primary for
            the relations as specified in RelatedObjectFilter; i.e. the sourceObjects
            are secondary in these relationships.
            
If set to false, it returns those objects that are secondary for
            the relations specified in RelatedObjectFilter; i.e. the sourceObjects are
            primary in these relationships.
            

"""
    ReturnRelations: bool
    """
            Flag to specify if the relation objects should be returned in response.
            

If set to false, relation objects are not returned.
            
If set to true, relation objects are returned.
            



            Setting this to false is particularly useful when only the related objects are of
            interest. The response is lighter in this case. So, false is recommended in cases
            where the input source objects are high in number (order of thousands).
            """

class RelatedObjectOutput:
    """
    
            RelatedObjectOutput contains the result corresponding to one RelatedObjectInput structure.
            This structure maps to the input structures by an index that points to the position
            of RelatedObjectInput structure in the input vector to the operation.
            
    """
    def __init__(self, ) -> None: ...
    IndexToInput: int
    """Index to the position of RelaedObjectInput structure in input vector to operation."""
    OtherSideObjects: list[RelatedObjectsContainer]
    """
            Each of the RelatedObjectsContainer in otherSideObjects vector contains related objects
            for a specific input object. The structure contains an index to position of source
            object within the RelatedObjectInput structure.
            """

class RelatedObjectsContainer:
    """
    
            RelatedObjectsContainer contains related objects for a specific input source object
            with in RelatedObjectInput structure given as input.
            
    """
    def __init__(self, ) -> None: ...
    IndexToSource: int
    """This index maps to the position of the source object within RelatedObjectInput structure."""
    RelationInfos: list[RelationInfo]
    """The related objects for a specific source object in input."""

class RelatedObjectsResponse:
    """
    
            RelatedObjectsResponse is used to return the results of a call to queryRelatedObjects.
            It contains a set of all objects that satisfy any one or more of the input filter
            criteria and that satisfy the input configuration criteria.
            
    """
    def __init__(self, ) -> None: ...
    RelatedObjects: list[RelatedObjectOutput]
    """
            Contains related objects for the input source objects organized in sets corresponding
            to RelatedObjectInput structures passed as input to operation.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard servicedata object."""

class RelationAttributeValues:
    """
    
            This structure contains the values to filter a relation attribute by.  Only one of
            the fields in RelationAttributeValues should be populated, the field populated must
            correspond to the value of RelationAttributeDataType in the RelationAttributeFilter.
            Multiple values, if passed in, are logically grouped with OR, meaning if any of
            the values match, the relation will pass through the filter.
            
    """
    def __init__(self, ) -> None: ...
    BooleanValues: list[bool]
    """A list of boolean values"""
    IntegerValues: list[int]
    """A list of integer values"""
    StringValues: list[str]
    """A list of string values; string value comparisons are case sensitive"""
    DoubleValues: list[float]
    """A list of double values"""
    DateValues: list[System.DateTime]
    """A list of date values"""
    TagValues: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of tag values"""

class RelationAttributeFilter:
    """
    
            This structure specifies a filter on one attribute of a relation.  A mismatch between
            the attributeType and the attributeValues data type results in an invalid input error
            and an SOA exception.  Any attribute other than mdl0cs_id, if passed in, will cause
            a not implemented error and an SOA exception.
            
    """
    def __init__(self, ) -> None: ...
    AttributeName: str
    """A list of values to filter by.  At least one value of the proper type must be specified."""
    AttributeType: str
    """
            The data type of the attribute to be filtered.  Legal values are:
            

BooleanType
            
IntegerType
            
StringType
            
DoubleType
            
DateType
            
TagType
            

"""
    AttributeValues: RelationAttributeValues
    """A list of values to filter by.  At least one value of the proper type must be specified."""

class RelationInfo:
    """
    
            RelationInfo contains the result data for one related object in the output, for a
            given relation.
            
    """
    def __init__(self, ) -> None: ...
    OtherSideObject: Teamcenter.Soa.Client.Model.ModelObject
    """The object found on the other side of the relation."""
    RelationObject: Teamcenter.Soa.Client.Model.Strong.Mdl0CopyStableRelation
    """
            The relation object which relates otherSideObject to the sourceObject. This is returned
            only if the input parameter returnRelations is set to true.
            """

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryRelatedObjects(self, InputObjects: list[RelatedObjectInput]) -> RelatedObjectsResponse:
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

