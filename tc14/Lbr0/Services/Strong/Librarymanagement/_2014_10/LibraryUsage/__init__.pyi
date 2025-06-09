import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindInstantiationsResponse:
    """
    
            The response structure containing information about the Instantiations of the input
            Library Elements.
            
    """
    def __init__(self, ) -> None: ...
    Instantiations: System.Collections.Hashtable
    """A map containing information about each Library Element instantiation."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData response."""

class LibraryElementInfo:
    """
    
            A structure containing a Library Element and its corresponding Library Object and
            Classification Object.
            
    """
    def __init__(self, ) -> None: ...
    LibraryElement: Teamcenter.Soa.Client.Model.Strong.Lbr0LibraryElement
    """The Library Element (Lbr0LibraryElement) ."""
    LibraryObject: Teamcenter.Soa.Client.Model.ModelObject
    """The Library Object that is referenced by the Library Element."""
    ClassificationObject: Teamcenter.Soa.Client.Model.Strong.Cls0ClassBase
    """
            The Classification object (Cls0ClassBase) that is referenced by the Library
            Element.
            """

class ObjectToPublishInfo:
    """
    
            Structure containing information about an object that is to be published to a Library
            Node. It includes Classification properties / values that should be used during the
            Publish.
            
    """
    def __init__(self, ) -> None: ...
    Object: Teamcenter.Soa.Client.Model.ModelObject
    """The object to Publish to the Library Node."""
    Properties: System.Collections.Hashtable
    """
            The classification property names and values to use for the Classification object
            that should be created during the Publish.
            """
    ElementProperties: System.Collections.Hashtable
    """
            The LibraryElement property names and values to use for the LibraryElement object
            that should be created during the Publish.
            """

class PublishObjectsIn:
    """
    
            This structure contains the input details for the objects to be published to a Library
            Node.
            
    """
    def __init__(self, ) -> None: ...
    LibraryNode: Teamcenter.Soa.Client.Model.Strong.Lbr0HierarchyNode
    """The Library Node where the objects are published"""
    ObjectsToPublish: list[ObjectToPublishInfo]
    """
            The objects to Publish along with relevant information for creation of the Library
            Element
            """
    DoBulkPublish: bool
    """
            Indicates whether the Publish should use a 'Bulk' approach that skips all custom
            logic and workflows
            """

class PublishObjectsResponse:
    """
    
            The response structure containing information about the objects Published to the
            Library Node.
            
    """
    def __init__(self, ) -> None: ...
    ObjectsPublished: System.Collections.Hashtable
    """The map of Library Nodes and the objects published."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data response that can contain the partial errors."""

class RetractObjectsIn:
    """
    
            This structure contains the input details for the objects to be retracted from a
            Library Node.
            
    """
    def __init__(self, ) -> None: ...
    LibraryNode: Teamcenter.Soa.Client.Model.Strong.Lbr0HierarchyNode
    """The Library Node from where the objects are Retracted."""
    ObjectsToRetract: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            The Library Element ( Lbr0LibraryElement
            ) or Library Object to Retract from the Library Node.
            """
    DeleteClsObject: bool
    """
            Indicates whether Classification object should also be deleted if the object being
            retracted has global Classification information. Local Classification objects are
            always deleted.
            """
    DoBulkRetract: bool
    """
            Indicates whether the Retract should use a 'Bulk' approach that skips all custom
            logic and workflows.
            """

class RetractObjectsResponse:
    """
    
            The response structure containing information about the objects Retracted from the
            Library Node.
            
    """
    def __init__(self, ) -> None: ...
    ObjectsRetracted: System.Collections.Hashtable
    """The map of Library Nodes and the objects retracted."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data response that can contain the partial errors."""

class ValidateInstantiationIn:
    """
    A structure containing information about the Library Element to validate for Instantiation.
    """
    def __init__(self, ) -> None: ...
    LibraryElement: Teamcenter.Soa.Client.Model.Strong.Lbr0LibraryElement
    """The Library Element to validate for Instantiation."""
    Properties: System.Collections.Hashtable
    """
            Custom properties set by the Design that will be used in validation. Interpretation
            of these properties is up to the custom code written for the validate Instantiation
            operation.
            """

class LibraryUsage:
    """
    Interface LibraryUsage
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindInstantiations(self, LibraryElements: list[Teamcenter.Soa.Client.Model.Strong.Lbr0LibraryElement]) -> FindInstantiationsResponse:
        """    
             Find all the Design Components that  are registered as Instantiations of the given
             Library Elements.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param LibraryElements: 
                         The Library Elements whose Instantiations need to be found.
             
        :return: output
             structure.
        """
        ...
    def PublishObjectsToLibrary(self, ObjectsInput: list[PublishObjectsIn]) -> PublishObjectsResponse:
        """    
             Publish (add) the given objects  to the specified Library (Node). This creates a
             new Library Element in the specified Library Node that  references the object. An
             object can be published to either a Classifying Library Node or a General Library
             Node. In case the Node specified here is a Classifying Library Node, classification
             properties &  values can be passed in for the creation of the Classification
             object. Passing in false for the doBulkPublish
             parameter ensures that all  custom logic and workflows configured for Publish are
             skipped during the operation.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ObjectsInput: 
                         The objects to Publish to the Library Node alongwith relevant information for each
                         object.
             
        :return: 
        """
        ...
    def RetractObjectsFromLibrary(self, ObjectsInput: list[RetractObjectsIn]) -> RetractObjectsResponse:
        """    
             Retract (remove) the given  objects from the specified Library (Node). This operation
             deletes the Library Element, which effectively  removes the Library Object from the
             Node. The Library Object is not deleted. The operation can also optionally  delete
             the Classification object that is referenced by this Library Element. Passing in
             false for the  doBulkRetract parameter ensures
             that all custom logic and workflows configured for Retract are skipped during the
             operation.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param ObjectsInput: 
                         The objects to Retract from the Library Node.
             
        :return: 143504 - if the element being retracted is instantiated in one or more Designs.
        """
        ...
    def ValidateInstantiations(self, InstantiateIn: list[ValidateInstantiationIn]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used to validate whether an Instantiate can be done for the required
             Library Element(s).
             

Use Cases:

             Using a Library Element in a Design is known as Instantiation. Instantiation is a
             multi-step operation wherein the Library and the Design need to exchange information
             in order to validate the Instantiation and perform this operation.
             
             The first step in an Instantiation is typically to validate whether the Library Elements
             can be instantiated. The user calls this operation when such validation is to be
             done.
             

Teamcenter Component:

             Library Management module - Provides a set of features for Library & Specification
             management and usage.
             
        :param InstantiateIn: 
                         Contains the Library Elements to instanatiate and any custom data that needs to be
                         passed in from the Design application.
             
        :return: 
        """
        ...

