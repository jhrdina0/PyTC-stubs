import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateInput:
    """
    This structure captures the inputs required for creation of a business object.
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Business object type name. Valid type is Cpd0Workset."""
    StringProps: System.Collections.Hashtable
    """
            Initial values of properties of type string. A map (string, string) of string property
            names to values.
            """
    StringArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type string array. A map (string, list of strings)
            of property names to values.
            """
    DoubleProps: System.Collections.Hashtable
    """
            Initial values of properties of type double. A map (string, double) of double property
            names to values.
            """
    DoubleArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type string array. A map (string, list of strings)
            of property names to values.
            """
    FloatProps: System.Collections.Hashtable
    """
            Initial values of properties of type float. A map (string, float) of float property
            names to values.
            """
    FloatArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type float array. A map (string, list of floats)
            of property names to values.
            """
    IntProps: System.Collections.Hashtable
    """
            Initial values of properties of type int. A map (string, int) of int property names
            to values.
            """
    IntArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type int array. A map (string, list of integers)
            of property names to values.
            """
    BoolProps: System.Collections.Hashtable
    """
            Initial values of properties of type boolean. A map (string, bool) of boolean property
            names to values.
            """
    BoolArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type boolean array. A map (string, list of bools)
            of property names to values.
            """
    DateProps: System.Collections.Hashtable
    """
            Initial values of properties of type date. A map (string, date) of date property
            names to values.
            """
    DateArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type date array. A map (string, list of date) of
            property names to values.
            """
    ObjectProps: System.Collections.Hashtable
    """
            Initial values of properties of type BusinessObject. A map (string, BusinessObject)
            of BusinessObject property names to values.
            """
    ObjectArrayProps: System.Collections.Hashtable
    """
            Initial values of properties of type BusinessObject. A map (string, list of BusinessObjects)
            of property names to values.
            """
    CompoundCreateInput: System.Collections.Hashtable
    """
            Initial secondary CreateInput values of reference or relation properties. A map (string,
            list of CreateInputs) of reference or relation property names to values. This struture
            is not used at this time.
            """

class CreateIn:
    """
    CreateIn is used to specify information for Cpd0Workset/Item creation.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            Unique client identifier. If there is an error in create, the client id in the ServiceData
            PartialError list can be used to associate to the clientId in the input to detect
            which object creation failed.
            """
    Data: CreateInput
    """
            Input data for create operation. A map of property name-value pairs representing
            the input data for creation of the desired new worksets (Cpd0Workset) or items
            (Item).
            """

class GenerateDesignContextOption:
    """
    Structure controls how the product data will be generated.
    """
    def __init__(self, ) -> None: ...
    Configuration: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext
    """Configuration applied to design elements (Cpd0DesignElement)."""
    Models: list[Teamcenter.Soa.Client.Model.Strong.Mdl0ApplicationModel]
    """
            List of application models (Mdl0ApplicationModel) to search for design components
            (Cpd0DesignElement) that reuse the input item revision (ItemRevision) objects
            """
    ProximityDistance: float
    """Distance value used by proximity search of design components (Cpd0DesignElement)."""
    IncludeReuseOnly: bool
    """
            Boolean value used to generate the content of the subset. When it is set to true, only reuse design components (Cpd0DesignElements)
            are searched and added to the newly created Cpd0DesignSubsetElement objects.
            """
    IncludeSubordinate: bool
    """
            Boolean value used to specify if subordinate Cpd0DesignElements are included.
            When it is set to true, subordinate Cpd0DesignElements
            are included for the reuse. Otherwise subordinate Cpd0DesignElements are not
            included. It is used only when includeReuse is set to true.
            """

class GenerateDesignContextInfo:
    """
    GenerateDesignContextInfo is used as input for creating design context.
    """
    def __init__(self, ) -> None: ...
    CreateInput: CreateIn
    """Information used to create a Cpd0Workset or Item object."""
    Option: GenerateDesignContextOption
    """Option for creating design context."""
    DesignItems: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]
    """A list of ItemRevision and/or Cpd0DesignElement objects."""

class GenerateDesignContextResponse:
    """
    Structure contains response of the operation.
    """
    def __init__(self, ) -> None: ...
    ClientIdMap: System.Collections.Hashtable
    """Map (string, business object) of client ID to newly created workset and item."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Added, updated, deleted object data plus any error information."""

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateDesignContext(self, DesignContextInfos: list[GenerateDesignContextInfo]) -> GenerateDesignContextResponse:
        """    
             This operation creates a Cpd0Workset or Item with a list of Cpd0DesignSubsetElements
             for each GenerateDesignContextInfo and returns
             the Cpd0Workset or Item objects.
             

Use Cases:

Generate Design Context:

             Generates design contexts for a list of ItemRevision objects and Cpd0DesignElement
             objects.
             

Application finds the source ItemRevision objects of the input
             Cpd0DesignElement objects.
             
Application finds the corresponding Item object for each of the input
             ItemRevision objects and the above source ItemRevision objects.
             
Application finds all the ItemRevision objects of the above
             Item objects.
             
Application finds the realized Cpd0DesignElement objects of
             above ItemRevision objects.
             
Application performs a proximity search on the input subordinate
             Cpd0DesignElement objects.
             
All Cpd0DesignElement objects are grouped based on unique
             configuration per collaborative design.
             
For each group of Cpd0DesignElement objects, a subset is created.
             A recipe is also created and set on the subset. The recipe adds all Cpd0DesignElement
             objects in the group to the subset.
             
Application creates a Cpd0Workset or Item object and
             puts all newly created Cpd0DesignSubsetElement objects in it.
             
Application returns the Cpd0Workset or Item.
             




Generate Design Context for Change Item Revision:

             Generates design context for a list of ChangeItemRevisions:
             

Application finds the ItemRevision objects and Cpd0DesignElement
             objects attached to ChangeItemRevision objects through a relation defined
             by the preference ChangeItemRevision_Design_Item_default_relation.
             
Application finds source ItemRevision objects of above Cpd0DesignElement
             objects.
             
Application finds the Item objects of above ItemRevision objects
             and source ItemRevision objects.
             
Application finds all ItemRevision objects of the above Item
             objects.
             
Application finds the realized Cpd0DesignElement objects of
             above ItemRevision objects.
             
Application performs a proximity search on the input subordinate
             Cpd0DesignElement objects.
             
All Cpd0DesignElement objects are grouped based on unique
             configuration per collaborative design.
             
For each group of Cpd0DesignElement objects, a subset is created.
             A recipe is also created and set on the subset. The recipe adds all Cpd0DesignElement
             objects in the group to the subset.
             
Application creates a Cpd0Workset or Item object and puts
             all newly created Cpd0DesignSubsetElement objects in it.
             
Application returns the Cpd0Workset or Item object.
             



Generate Design Context with Reuse Cpd0DesignElements:

             Generates design context for a list of ItemRevision and Cpd0DesignElement
             objects.
             

Application finds the realized Cpd0DesignElement objects of
             the ItemRevision objects.
             
Application finds the reuse Cpd0DesignElement objects of the
             above Cpd0DesignElement objects and the input Cpd0DesignElement objects.
             
Application finds the source ItemRevision objects of the reuse
             Cpd0DesignElement objects.
             
Application finds the Item objects of the above ItemRevision
             objects.
             
Application finds all ItemRevision objects of the above Item
             objects.
             
Application finds reuse Cpd0DesignElement objects of the above
             ItemRevision objects and subordinate Cpd0DesignElement objects for
             the reuse.
             
All Cpd0DesignElement objects are grouped based on unique
             configuration per collaborative design.
             
For each group of Cpd0DesignElement objects, a subset is created.
             A recipe is also created and set on the subset. The recipe adds all Cpd0DesignElement
             objects in the group to the subset.
             
Application creates a Cpd0Workset or Item object and puts
             all newly created Cpd0DesignSubsetElement objects in it.
             
Application returns the Cpd0Workset or Item object.
             



Teamcenter Component:

             Collaborative Product Development - Defines data management of 4GD application objects
             (Design Components,Design Features,Design Control Elements),defines operations to
             create and manage Subsets from Product Design and navigation operations for Workset
             and Subset content.
             
        :param DesignContextInfos: 
                         The operation takes in a list of GenerateDesignContextInfo, creates a workset or
                         item with a list of subsets in it each GenerateDesignContextInfo and returns the
                         worksets and items.
             
        :return: 
        """
        ...

