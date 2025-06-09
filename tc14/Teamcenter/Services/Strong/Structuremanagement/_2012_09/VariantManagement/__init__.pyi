import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class SaveAsInput:
    """
    
Structure encapsulating all information related to a Workspace Object which may
be
required for "Save As" operation during operations 'createVariantItem'
or 'createAndSubstituteVariantItem'.
    """
    def __init__(self, ) -> None: ...
    BoName: str
    """Type Name Of Business Object"""
    StringProps: System.Collections.Hashtable
    """Map containing string property values . Pairs (string, string)"""
    StringArrayProps: System.Collections.Hashtable
    """Map containing string array property values. Pairs (string, string[])"""
    DoubleProps: System.Collections.Hashtable
    """Map containing double property values. Pairs (string, double)"""
    DoubleArrayProps: System.Collections.Hashtable
    """Map containing double array property values. Pairs (string,  double[])"""
    FloatProps: System.Collections.Hashtable
    """Map containing float property values. Pairs (string, float)"""
    FloatArrayProps: System.Collections.Hashtable
    """Map containing float array property values. Pairs (string, float[])"""
    IntProps: System.Collections.Hashtable
    """Map containing integer property values. Pairs (string, integer)"""
    IntArrayProps: System.Collections.Hashtable
    """Map containing integer array property values. Pairs (string, integer[])"""
    BoolProps: System.Collections.Hashtable
    """Map containing boolean property values. Pairs (string, boolean)"""
    BoolArrayProps: System.Collections.Hashtable
    """Map containing boolean array property values. Pairs (string, boolean[])"""
    DateProps: System.Collections.Hashtable
    """Map containing date property values. Pairs (string, Date)"""
    DateArrayProps: System.Collections.Hashtable
    """Map containing date array property values . Pairs (string, Date[])"""
    TagProps: System.Collections.Hashtable
    """Map containing tag property values. Pairs (string, Tag)"""
    TagArrayProps: System.Collections.Hashtable
    """Map containing tag array property values. Pairs (string, Tag[])"""

class SaveAsIn:
    """
    Input for save as operation
    """
    def __init__(self, ) -> None: ...
    TargetObject: Teamcenter.Soa.Client.Model.ModelObject
    """Target object being saved as"""
    SaveAsInput: SaveAsInput
    """SaveAsInput (user input from SaveAs dialog) for the targetobject being saved as"""
    DeepCopyDatas: list[DeepCopyData]
    """DeepCopyData of the objects attached to the targetobject"""

class CreateOrSaveAsDescriptor:
    """
    
This is helper structure to collect all information of new variant Item required
for either creating New Item or saving existing Item as variant Item.
    """
    def __init__(self, ) -> None: ...
    Properties: list[ItemProperties]
    """Input properties for new variant Item."""
    SaveAsIn: SaveAsIn
    """Input for save as operation"""
    BCreateOrSaveAsFlag: bool
    """
            bool flag to indicate Create new Item as true and "Save as" operation as false
            value.
            """

class CreateAndSubsVIInput:
    """
    
Input structure for operation 'createAndSubstituteVariantItem'.
One structure represents One new variant Item to be created.
    """
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
BOMLine of configured structure from which new variant Item Structure
            should be created. This structure has Variants defined and can be configured for
            some given variant Configuration. For more details please refer section 'Creating
            and updating variant Items' from Teamcenter Documentation.
            """
    CreateOrSaveAsDescriptor: CreateOrSaveAsDescriptor
    """
            Create or SaveAs description required for Item Creation. This will include
            information about new variant Item creation such as Item Id, name,
            description, objects that need to be copied or done 'Save As' along with new Item.
            """
    ViBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
BOMLine of variant Item structure. After creating new variant Item
            from genericBOMLine, the newly created variant ItemRevision will be substituted
            on this viBOMLine.
            """
    LinkVIToGenericItem: bool
    """
            Flag to decide Variant Item should be linked to its generic structure or not.
            Value of this parameter will be overriden by preference 'PSEIsNewVILinkedToModule',
            if exists on SITE level.
            """
    FindVIBeforeCreate: bool
    """
            Find existing Variant Item before creating new Variant Item. If existing
            Variant Item is found, then new Variant Item is not created. This existing
            Variant Item will be replaced on viBOMLine.
            """

class CreateAndSubsVIOutput:
    """
    
Output structure for CreateAndSubstituteVI
SOA
    """
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Generic BOMLine from which variant Item is created."""
    ViBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
BOMLine of variant Item structure. After creating new variant Item
            from genericBOMLine, the newly created variant
            ItemRevision will be substituted on this viBOMLine.
            """
    NewVariantItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """ItemRevision of newly created Variant Item."""
    IsExistingVIFound: bool
    """
            This flag will be returned populated only when flag 'findVIBeforeCreate'
            in server input 'CreateAndSubsVIInput' is
            passed as 'True'. Flag to indicate that if existing Variant Item was not found
            and new Variant Item is created. If value is true, this means existing Variant
            Item was found, and was used for substitute operation.
            """

class CreateAndSubsVIResponse:
    """
    Response structure to operation 'createAndSubstituteVariantItem'.
    """
    def __init__(self, ) -> None: ...
    CreateAndSubsOutputs: list[CreateAndSubsVIOutput]
    """
            List of CreateAndSubsVIOutput s for each
            CreateAndSubsVIInput.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data to return error back to caller."""

class CreateVIInput:
    """
    Input Structure for operation 'createVariantItem'.
    """
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
BOMLine of configured structure from which new variant Item Structure
            should be created. This structure has Variants defined and can be configured for
            some given variant Configuration. For more details please refer section 'Creating
            and updating variant Items' from Teamcenter Documentation.
            """
    CreateOrSaveAsDescriptor: CreateOrSaveAsDescriptor
    """
            Create or SaveAs description required for Item Creation. This will include
            information about new variant Item creation such as Item Id, name,
            description, objects that need to be copied or done 'Save As' along with new Item.
            """
    LinkVIToGenericItem: bool
    """
            Flag to decide variant Item should be linked to its generic structure or not.
            Value of this parameter will be overridden by preference 'PSEIsNewVILinkedToModule',
            if exists on SITE location.
            """

class CreateVIOutput:
    """
    
Output structure for operation 'createVariantItem'.
There will be one CreateVIOutput for each
CreateVIInput.
    """
    def __init__(self, ) -> None: ...
    GenericBOMLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """
            BOM Line of configured structure from which new Variant Item Structure should be
            created. This structure has Variants defined and can be configured for some given
            Variant Configuration. For more details please refer section 'Creating and updating
            variant items' from Teamcenter Documentation.
            """
    NewVariantItemRevision: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """Item Revision of newly created Variant Item."""

class CreateVIResponse:
    """
    Response structure for operation 'createVariantItem'
    """
    def __init__(self, ) -> None: ...
    CreateVariantItemOutput: list[CreateVIOutput]
    """List of outputs one each for 'CreateVIInput'"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Service Data to return error back to caller."""

class DeepCopyData:
    """
    
Structure to collect information about objects which should be copied or
referenced
in new variant Item.
    """
    def __init__(self, ) -> None: ...
    AttachedObject: Teamcenter.Soa.Client.Model.ModelObject
    """Other side object"""
    PropertyName: str
    """Name of relation type or reference property for which DeepCopy rule is configured"""
    PropertyType: str
    """Name of relation type or reference property for which DeepCopy rule is configured"""
    CopyAction: str
    """DeepCopy action [NoCopy, CopyAsReference, CopyAsObject or Select]"""
    IsTargetPrimary: bool
    """Flag indicating if target object is primary or secondary"""
    IsRequired: bool
    """If this flag is false, the copy action can be dynamically changed by user"""
    CopyRelations: bool
    """
            This is a Boolean representing whether the Properties on the Relation if any in the
            Relation that exists between
            """
    SaveAsInputTypeName: str
    """SaveAsInput type name"""
    SaveAsInput: SaveAsInput
    """
            SaveAsInput field to capture user inputs on the SaveAs dialog. NOTE: This field is
            unused in the getSaveAsDesc operation. It is used in the saveAsObjects operation
            """
    ChildDeepCopyData: list[DeepCopyData]
    """Vector of DeepCopy data for the secondary objects on the other side"""

class ExtendedAttributes:
    """
    
Structure to collect additional attributes to be assigned apart from default
'Save
As' or 'Cretae New' Item operation.
    """
    def __init__(self, ) -> None: ...
    ObjectType: str
    """Type of Business Object."""
    Attributes: System.Collections.Hashtable
    """Map of attribute name and its value. pairs( String, String )"""

class ItemProperties:
    """
    
Specifies attributes for the new Item or ItemRevision. Mainly used
in 'Create new Item' scenario, describes specific attributes to be assigned.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """Identifier that helps the client to track the object(s) created"""
    ItemId: str
    """Id of the Item to be created"""
    Name: str
    """Name of the Item to be created"""
    Type: str
    """Business Object type of the Item to be created"""
    RevId: str
    """Id of the initial revision of the Item to be created"""
    Uom: str
    """UOM of the Item to be created"""
    Description: str
    """Description of the Item to be created"""
    ExtendedAttributes: list[ExtendedAttributes]
    """
            List of 'extendedAttributes' structures having
            Name/value pairs for additional attributes to set.
            """

class VariantManagement:
    """
    Interface VariantManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateAndSubstituteVariantItem(self, CreateAndSubstituteVIInput: list[CreateAndSubsVIInput]) -> CreateAndSubsVIResponse:
        """    
             This operation will create new variant Item for given BOMLine (also
             called as 'Generic BOMLine') from a BOM structure (also called as 'Generic
             Structure') having variability using variants. Addition to creating new variant Item,
             this is operation will also replace or substitute newly created variant Item Revision
             in given target BOMLine (also called as 'VI BOMLine') in variant Structure
             which corresponding to fully configured structure by fixing variability in Generic
             BOM Structure.
             

             Operation also accepts 2 flags 'findVIBeforeCreate'
             used to control if existing variant Item should be searched and used instead
             of creating new variant Item and 'linkVIToGenericItem'
             to link newly created variant Item to source Item of generic BOMLine.
             

             The new variant Item can be created in 2 ways either creating new separate
             Item or doing "Save-As" operation on generic Item. In case of "Save-As" the
             parameter 'CreateOrSaveAsDescriptor' will
             provide additional information about which all related objects are carried over to
             new Item from source generic Item.
             


Use Cases:

             This operation should be used when user has Generic Structure & corresponding
             created variant Structure and user wants to create Item which is variant for
             each child BOMLine object and replace in variant Structure.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param CreateAndSubstituteVIInput: 
                         Consists of set of output structures, an output structure for each input. An output
                         structure have respective input <font face="courier" height="10">'genericBOMLine</font>'
                         &amp; <font face="courier" height="10">'viBOMLine</font>' and newly created <b>ItemRevision</b>
                         object as <font face="courier" height="10">'newVariantItemRevision</font>'; along
                         with flag '<font face="courier" height="10">isExistingVIFound</font>' indicating
                         if <font face="courier" height="10">'newVariantItemRevision</font>' is created newly
                         or found existing Item which is variant and used.
             
        :return: 
        """
        ...
    def CreateVariantItem(self, CreateVIInputs: list[CreateVIInput]) -> CreateVIResponse:
        """    
             This operation will create new variant Item for given BOMLine (also
             called as 'Generic BOMLine') from a BOM structure (also called as 'Generic
             Structure') having variability using variant Options.
             

             Operation also accepts a flag 'linkVIToGenericItem'
             to link newly created variant Item to source Item of 'generic BOMLine'.
             

             The new variant Item can be created in 2 ways either by creating new separate
             Item or doing "Save-As" operation on generic Item. In case of "Save-As"
             the parameter
             
'CreateOrSaveAsDescriptor' will provide additional
             information about which all related objects are carried over to new Item from
             source generic Item.
             


Use Cases:

             This operation should be used when user wants to create new variant Item using
             generic BOMLine from a generic BOM structure.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param CreateVIInputs: 
                         List of <font face="courier" height="10">createVIInput</font> structures
             
        :return: 
        """
        ...

