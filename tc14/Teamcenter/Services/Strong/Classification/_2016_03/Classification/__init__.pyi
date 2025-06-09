import System
import Teamcenter.Services.Strong.Classification._2007_01.Classification
import Teamcenter.Soa.Client.Model
import typing

class BaseClassDef:
    """
    This structure contains the basic information about a class.
    """
    def __init__(self, ) -> None: ...
    ClassID: str
    """The ID of the class."""
    ClassBO: Teamcenter.Soa.Client.Model.ModelObject
    """Reference to the business object representing this class."""
    ClassName: str
    """The name of the class."""
    IsAbstract: bool
    """
            If true, this class is abstract. Classification instances cannot be stored in this
            class. False, indicates that Classification instances can be stored in this class.
            """
    ClassUnitBase: int
    """
            The unit system of the class:
            

0 - The class supports the storage of metric objects only
            
1 - The class supports the storage of non-metric only
            
2 - The class supports both metric and non-metric objects
            

"""
    ClassIconLoaded: bool
    """If true, the icon file for this class is loaded. False, it is not loaded."""
    ClassIconDocument: Teamcenter.Services.Strong.Classification._2007_01.Classification.TypedDocument
    """The icon document attached to this class."""

class ConvertValuesResponse:
    """
    
            Structure containing the converted values. Any failures with the conversion will
            be mapped to the error message in the ServiceData list of partial errors.
            
    """
    def __init__(self, ) -> None: ...
    ConvertedValues: list[ValueConversionOutput]
    """The converted values."""
    SvcData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failures with the conversion will be mapped to the error message in the ServiceData
            list of partial errors.
            """

class ExtendedClassDef:
    """
    This structure contains the extended information about a class.
    """
    def __init__(self, ) -> None: ...
    ClassDef: BaseClassDef
    """This basic information about the class."""
    ParentDefs: list[BaseClassDef]
    """
            List of the parent definitions specific to the class and the parent corresponding
            basic properties.
            """
    ClassShortName: str
    """The short name of the class."""
    ClassDescription: str
    """The description of the class."""
    ClassUserData1: str
    """User data 1 added to the class."""
    ClassUserData2: str
    """User data 2 added to the class."""
    ClassChildCount: int
    """The count of child classes of the class. If not retrieved, the count is -1."""
    ClassInstanceCount: int
    """The count of instances in the class. If not retrieved, the count is -1."""
    ClassImagesLoaded: bool
    """
            If true, value indicates that the image documents for this class were loaded. False,
            they were not loaded.
            """
    ClassImageDocuments: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.TypedDocument]
    """A list of class documents attached to the class (like class image)."""

class GetChildrenExtendedOutput:
    """
    
            Structure containing the found classes for the given search criteria. Any failures
            with the search will be mapped to the error message in the ServiceData list of partial
            errors.
            
    """
    def __init__(self, ) -> None: ...
    ClassDescriptions: list[ExtendedClassDef]
    """List of child classes found."""

class GetChildrenExtendedResponse:
    """
    Contains a list of child classes found for the given classes.
    """
    def __init__(self, ) -> None: ...
    ClassDescriptions: list[GetChildrenExtendedOutput]
    """List of child classes found for input class IDs."""
    SvcData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failures with class ID mapped to the error message are returned in the ServiceData
            list of partial errors.
            """

class SearchClassesExtendedOutput:
    """
    
            Structure containing the found classes for the given search criteria. Any failures
            with the search will be mapped to the error message in the ServiceData list of partial
            errors.
            
    """
    def __init__(self, ) -> None: ...
    ClassDescriptions: list[ExtendedClassDef]
    """List of classes found for input search criteria."""

class SearchClassesExtendedResponse:
    """
    
            Structure containing the found classes for the given search criteria. Any failures
            with the search will be mapped to the error message in the ServiceData list of partial
            errors.
            
    """
    def __init__(self, ) -> None: ...
    ClassDescriptions: list[SearchClassesExtendedOutput]
    """List of classes found for input search criteria."""
    SvcData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failures with the search will be mapped to the error message in the ServiceData
            list of partial errors.
            """

class ValueConversionInput:
    """
    
            Structure containing the value(s) and unit systems which should be used to convert
            the input values.
            
    """
    def __init__(self, ) -> None: ...
    InputValues: list[str]
    """
            The input values. For regular attributes it's just one value. In case of VLA (variable
            length array) attributes each value has its own entry.
            
            The calling client is responsible for converting the different property types (int,
            float, date .etc) to a string using the appropriate functions in the SOA client framework's
            Property class.
            """
    InputUnit: str
    """The input unit e.g. the unit definition ID "Length_mm" or also the display name "mm"."""
    OutputUnit: str
    """
            The output unit e.g. the unit definition ID "Length_mm" or also the display name
            "mm".
            """
    OutputFormat: Teamcenter.Services.Strong.Classification._2007_01.Classification.AttributeFormat
    """The output format to which the converted value should be formatted."""
    Options: int
    """The options parameter (This option is for future use)."""

class ValueConversionOutput:
    """
    
            The converted values. For regular attributes it's just one value, in case of VLA
            (variable length array) attributes, each value has its own entry.
            
    """
    def __init__(self, ) -> None: ...
    ConvertedValues: list[str]
    """
            The converted values. For regular attributes it's just one value. In case of VLA
            (variable length array) attributes each value has its own entry.
            

            The calling client is responsible for converting the string value to the different
            property types  (int, float, date .etc) using the appropriate functions in the SOA
            client framework's Property class.
            """

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ConvertValues(self, ValueConversionInputs: list[ValueConversionInput]) -> ConvertValuesResponse:
        """    
             This operation converts the input value using provided input and output unit.
             

             The conversion happens only when the output format represents a numerical format.
             For String and KeyLOV(Stxt) formats, no conversion will occur, and the input
             string will be returned as is.
             

Use Cases:

             When creating classification classes, you can define whether a class contains only
             metric ICOs, only nonmetric ICOs, or both. If the classification administrator specifies
             that a class can contain both, you can search for an object using either of the unit
             systems you define, and the search mechanism finds a match, regardless of the unit
             in which the object is stored. For example, if you search for a bolt with a width
             of 5/8th inches, the classification search mechanism finds a bolt that is stored
             with a width of 1.6 centimeters. This operation supplies this conversion mechanism.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ValueConversionInputs: 
                         The values to be converted.
             
        :return: 
        """
        ...
    def GetChildrenExtended(self, ClassObjects: list[Teamcenter.Soa.Client.Model.ModelObject], FilterForWriteAccess: bool, Options: int) -> GetChildrenExtendedResponse:
        """    
             Gets the detailed information about immediate children in the classification hierarchy
             for given group(s) or class(es). It also contains all detailed information about
             the parent classes within the hierarchy.
             

             In comparison to getChildren it contains
             extended information about the class itself and also extended information about its
             parent classes.
             

Use Cases:

             User wants to get the details of the class "Tools and Components" and all the classes
             under it, to render the entire hierarchy.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param ClassObjects: 
                         The class objects for which the children should be retrieved.
             
        :param FilterForWriteAccess: 
                         If true, the classes which are not available for the classify action (that is, to
                         which the user does not have write access) are not returned.
             
        :param Options: 
<ul>
<li type="disc">1 &lt;&lt; 0 - return parent information as part of the ExtendedClassDef
                         </li>
<li type="disc">1 &lt;&lt; 1 - return the child count as part of the ExtendedClassDef
                         </li>
<li type="disc">1 &lt;&lt; 2 - return the instances count as part of the ExtendedClassDef
                         </li>
<li type="disc">1 &lt;&lt; 3 - return the icon documents as part of the BaseClassDef
                         </li>
<li type="disc">1 &lt;&lt; 4 - return the class image documents as part of the ExtendedClassDef
                         </li>
</ul>

        :return: 
        """
        ...
    def SearchClassesExtended(self, SearchCriterias: list[Teamcenter.Services.Strong.Classification._2007_01.Classification.SearchAttribute], SortAttributes: list[int], FilterForWriteAccess: bool, Options: int) -> SearchClassesExtendedResponse:
        """    
             Finds the classification classes based on provided search criteria and provides detailed
             information about those classes. The user can search using a search expression on
             attributes of the class (class ID, name, used attribute etc.). For example, the user
             shall be able to search all the classes whose name begins with a particular set of
             characters and where the class ID matches certain pattern. The order of search results
             can also be sorted on various criteria.
             

             In comparison to searchForClasses it contains
             extended information about the class itself and also extended information about its
             parent classes.
             

Use Cases:

             The user needs to search for classification classes using a search criterion based
             on various attributes of a class. The search criterion can be based on one or more
             attributes.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param SearchCriterias: 
<ul>
<li type="disc">class ID search "-600 = 123"
                         </li>
<li type="disc">class name search "-607 = abc"
                         </li>
<li type="disc">class short name search "-608 = abc"
                         </li>
<li type="disc">class user data 1 "-612 = abc"
                         </li>
<li type="disc">class user data 2 "-613 = abc"
                         </li>
<li type="disc">for all classes using a specific attribute "8 = attribute ID"
                         </li>
<li type="disc">for all classes using a specific attribute "3 = attribute name"
                         </li>
</ul>

        :param SortAttributes: 
<ul>
<li type="disc">class ID = -600
                         </li>
<li type="disc">class name = -607
                         </li>
<li type="disc">class short name = -608
                         </li>
<li type="disc">class user data 1 = -612
                         </li>
<li type="disc">class user data 2 = -613
                         </li>
</ul>

        :param FilterForWriteAccess: 
                         If true, the classes which are not available for the classify action (that is, to
                         which the user does not have write access) are not returned.
             
        :param Options: 
<ul>
<li type="disc">1 &lt;&lt; 0 - return parent information as part of the <font face="courier" height="10">ExtendedClassDef</font>
</li>
<li type="disc">1 &lt;&lt; 1 - return the child count as part of the <font face="courier" height="10">ExtendedClassDef</font>
</li>
<li type="disc">1 &lt;&lt; 2 - return the instances count as part of the <font face="courier" height="10">ExtendedClassDef</font>
</li>
<li type="disc">1 &lt;&lt; 3 - return the icon documents as part of the <font face="courier" height="10">BaseClassDef</font>
</li>
<li type="disc">1 &lt;&lt; 4 - return the class image documents as part of the <font face="courier" height="10">ExtendedClassDef</font>
</li>
</ul>

        :return: 
        """
        ...

