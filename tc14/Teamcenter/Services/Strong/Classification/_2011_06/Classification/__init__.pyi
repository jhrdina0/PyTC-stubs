import System
import Teamcenter.Services.Strong.Classification._2007_01.Classification
import Teamcenter.Soa.Client.Model
import typing

class ClassInfo:
    """
    Structure representing class description in ClassDef structure and business object
    """
    def __init__(self, ) -> None: ...
    ClassDefn: Teamcenter.Services.Strong.Classification._2007_01.Classification.ClassDef
    """
            Reference of the class definition structures holding all the class properties for
            the classes retrieved by this operation
            """
    ClassBO: Teamcenter.Soa.Client.Model.ModelObject
    """Reference to the business object found associated to this class."""

class GetLibraryHierarchyResponse:
    """
    
            Holds classification objects returned by getLibraryHierarchy() method.
            
    """
    def __init__(self, ) -> None: ...
    ClsInfo: list[ClassInfo]
    """List of class references found for this library"""
    SvcData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Any failures with Key-LOV ID mapped to the error message in the ServiceData list of partial errors.
            """

class HierarchyInfoAndOptions:
    """
    Structure representing the ClassId and options
    """
    def __init__(self, ) -> None: ...
    Id: str
    """Class ID to be deleted."""
    TheRecurseOption: bool
    """
            Flag to indicate if the delete operation should be recursively executed on the child
            classes for the given class.
            """
    TheViewsOption: bool
    """
            Flag to indicate if the Views associated with the class being deleted should
            be removed first. If views exist and this flag does not indicate deleting them first,
            then a referential integrity error will be generated for the given class.
            """
    TheIcosOption: bool
    """
            Flag to indicate if the Classification objects (ICO) should be delete first.
            If ICOs exist and this flag does not indicate deleting them first, then a referential
            integrity error will be generated for the given class.
            """
    TheWSOOption: bool
    """Flag to indicate if the classified Workspace Objects should be deleted first."""
    TheChildrenOnlyOption: bool
    """Flag to indicate if only the child classes should be deleted."""
    TheIgnoreOption: bool
    """
            Flag to indicate if the operation to should continue on error.
            

FALSE: stop on first error
            
TRUE: continue on error and report all failed objects back in the
            list of failed objects.
            

"""

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeleteChildrenInHierarchy(self, OptionsInput: list[HierarchyInfoAndOptions]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes classification class hierarchy based on the classification class identifier.
             All the child classes can be recursively deleted along with any classification views
             associated with those classification classes. If needed, the classification objects
             associated with classification classes & any workspace objects associated with
             the classification objects can also be deleted
             

Use Cases:

             User wants to delete a classification class hierarchy, or a part of it. User may
             also need to delete the associated data for these classes such as classification
             views, classification objects or workspace objects
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param OptionsInput: 
                         List of structure <font face="courier" height="10"><b>HierarchyInfoAndOptions</b></font>
                         that specifies the identifiers for classification classes whose class hierarchy needs
                         to be deleted. It also includes information on the objects that needs to be deleted
                         along with the classes &amp; also the options for deleting children
             
        :return: list of partial errors.
        """
        ...
    def GetLibraryHierarchy(self, LibraryValues: list[str]) -> GetLibraryHierarchyResponse:
        """    
             Gets the classification class details such as class ID, parent information, child
             count etc. for the specified library values criteria
             

Use Cases:

             The operation is called when the user queries to get class hierarchy information
             using the given library values.  The operation is typically used for data dictionary
             related functionality in classification area, and the library components are created
             using this feature in Teamcenter. Data dictionary is a central organizational repository
             for reusable components.
             

Teamcenter Component:

             Classification - Application to allow Classification of product data-standard parts.
             
        :param LibraryValues: 
                         The library value is passed as an input to the operation and is used as a search
                         criteria to get library hierarchy information
             
        :return: 
        """
        ...

