import System
import Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CreateFormAttrSearchCriteriaInputInfo:
    """
    Specifies the full set of inputs required to create the Form Search Criteria
object.
    """
    def __init__(self, ) -> None: ...
    Relationtype: str
    """
            Type name of Relation with which Form is attached to an Item/Item Revision. (For
            example: References). The valid relation types can be fetched from BMIDE: Open BMIDE->Go
            to Business Objects View->Search for ImanRelation->Expand ImanRelation.
            The name of any object listed as child of ImanRelation, can be supplied.
            """
    ParentType: bool
    """
            Boolean value indicating type of parent (true if the parent type is Item and false
            if the parent type is Item Revision)
            """
    FormType: str
    """
            Type name of Form being used for the search. The valid form type can be fetched from
            BMIDE: Open BMIDE->Go to Business Objects View->Search for Form. The name of any
            object listed as child of 'Form' can be supplied.
            """
    LogicalOpr: str
    """Logical operator. The only valid operator currently supported is 'AND'."""
    PropertyName: str
    """Name of the selected property on the form used for the search."""
    MathOpr: str
    """
            Operator used for comparison. List of valid operators:
            

'EQ' - Equal
            
'NE' - Not Equal
            
'GT' - Greater Than
            
'GE' - Greater Than or Equal
            
'LT' - Less Than
            
'LE' - Less Than or Equal
            
'LIKE'
            
'NOT LIKE'
            

"""
    PropertyType: str
    """
            Name of the type of property. The valid string values for this member are:
            

'BooleanType' - For Boolean Property
            
'DateType' - For Date Property
            
'IntegerType' - For Integer Property
            
'StringType' - For String Property
            
'DoubleType' - For Double Property
            
'TagType' - For Tag Property
            

"""
    Values: list[str]
    """
            List of string values used for the search. Each value specified here would be an
            appropriate value for the property specified in 'propertyName' parameter. These     values
            are passed in string format and converted back to their original format based on
            the 'propertyType' parameter specified above.
            """

class CreateFormAttrSearchCriteriaResponse:
    """
    
Contains the list of newly created Fnd0ApprSchCriteriaFormAttr objects and
ServiceData object
    """
    def __init__(self, ) -> None: ...
    FormAttrSchCriteria: list[Teamcenter.Soa.Client.Model.Strong.Fnd0ApprSchCriteriaFormAttr]
    """List of newly created Fnd0ApprSchCriteriaFormAttr objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains any
            exceptions if occurred during creation of Form attribute object.
            """

class CreateSearchCriteriaScopeInfo:
    """
    
This structure is used to store the list of scope BOMLine objects and the
Apprearance Goup objects.
    """
    def __init__(self, ) -> None: ...
    Nodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of all the scope BOMLine objects. If the search is performed on occurrence
            group object then this list will be empty.
            
"""
    Collections: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            It is a vector of BusinessObjects. If search is performed on one or more Occurrence
            group BOMLine objects then this list should have those occurrence group objects.
            
"""

class CreateSearchCriteriaScpResponse:
    """
    
This structure is used to store information about the newly created
Fnd0ApprSchCriteriaScpAttr
objects and ServiceData object after execution
of the operation createSearchCriteriaScope.
    """
    def __init__(self, ) -> None: ...
    SearchCriteriaScpObjects: list[Teamcenter.Soa.Client.Model.Strong.Fnd0ApprSchCriteriaScpAttr]
    """
            The list of objects of Fnd0ApprSchCriteriaScpAttr created by the createSearchCriteriaScope action.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains any
            exceptions if occurred during the creation of Scope Search Criteria object
            """

class CreateSearchSCOInputInfo:
    """
    
This structure is used to store additional information about a SCO object such
as
the availability of results, option to specify if SCO is shared or not.
    """
    def __init__(self, ) -> None: ...
    ScoInputInfo: Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.CreateSCOInputInfo
    """
            It is an object of CreateSCOInputInfo structure
            which contains name, description, search criteria information.
            """
    ResultStored: bool
    """Specifies whether results are stored or not in the SearchSCO."""
    IsShared: bool
    """Specifies whether the SearchSCO object will be shared with other users or not."""
    Nodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """List of all the scope bomlines used to store additional information in the SearchSCO."""

class CreateSearchSCOResponse:
    """
    
The CreateSearchSCOResponse structure represents search structure context object
created and the service data.
    """
    def __init__(self, ) -> None: ...
    SrchSCO: list[Teamcenter.Soa.Client.Model.Strong.SearchStructureContext]
    """
            The vector of objects of SearchStructureContext created by the createSearchSCO action
            
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            An object of ServiceData which contains any
            exceptions if occurred during creation of SearchSCO
            """

class GetICSClassNamesResponse:
    """
    
This structure contains the ICS class names and error, if any, in ServiceData
object.
    """
    def __init__(self, ) -> None: ...
    IcsClassNames: list[str]
    """
            ICS Class names for the corresponding     ApprSearchCriteriaInClass
            objects provided     in input paramter.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains any exceptions if occurred while getting the class name of InClass Search
            Criteria object.
            """

class UpdateSearchSCOInputInfo:
    """
    
This structure contains the Search Structure Context Object, the
StructureCntxtObjectInfo object containing information to be updated,
a flag to indicate if results should be stored or not and the scope bomlines.
    """
    def __init__(self, ) -> None: ...
    SrchSCO: Teamcenter.Soa.Client.Model.Strong.SearchStructureContext
    """
            Search Structure Context Object that needs to be updated. This SCO object will be
            updated with the modified values.
            
"""
    ScoInfo: Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.StructureCntxtObjectInfo
    """
            Object of StructureCntxtObjectInfo structure.
            It internally holds all the details related to the search criteria and search results.
            """
    ResultStored: bool
    """Describes whether the results are stored or not."""
    Nodes: list[Teamcenter.Soa.Client.Model.ModelObject]
    """It is a vector of all the scope bomlines used."""

class UpdateSearchSCOResponse:
    """
    
This structure contains the list of updated SearchStructureContext object
and error, if any, in ServiceData object.
    """
    def __init__(self, ) -> None: ...
    SrchSCO: list[Teamcenter.Soa.Client.Model.Strong.SearchStructureContext]
    """Vector of object of SearchStructureContext updated with the supplied inputs."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any exception that occurred during updating the SearchSCO."""

class ContextManagement:
    """
    Interface ContextManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateFormAttrSearchCriteria(self, Inputs: list[CreateFormAttrSearchCriteriaInputInfo]) -> CreateFormAttrSearchCriteriaResponse:
        """    
             Creates a list of Form Search Criteria objects based on the input parameters. It
             uses the following inputs from the input structure
             

Form type
             
Parent Type
             
Name of the property
             
Type of the property
             
Relation type
             
Operator and
             
Search value
             


             Form Search Criteria object is created as part of creation of the VisStructureContext
             object to persist form attribute search criteria.
             
             It is mandatory to provide all the input parameters. This operation will fail if
             null is provided for any of the string input parameters. The Form type or Relation
             type input should be valid string representing the name of a type in Teamcenter database.
             Empty string for Form type or Relation type input will cause the operation to fail.
             

Use Cases:

             1. Creating an Structure Context Oject(SCO)
             
             While pesristing the search criterias in Structure Context Oject, createFormAttrSearchCriteria operation is called to persist the
             Form serach criteria related information . You can create this object by providing
             the CreateFormAttrSearchCriteriaInputInfo
             structure. This form search criteria object is wrapped in Appearance Search Criteria
             Group object and stored in StructureContext object.
             

Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param Inputs: 
                         An object of Form Search Criteria is created for each <font face="courier" height="10">CreateFormAttrSearchCriteriaInputInfo</font>
                         in the inputs list. The data on the <font face="courier" height="10">CreateFormAttrSearchCriteriaInputInfo</font>
                         is used to create object of Form Search Criteria.
             
        :return: object and returned as a
             partial error. If the creation of an object fails, then error code 202017 is returned
             as a partial error.
        """
        ...
    def CreateSearchCriteriaScope(self, Inputs: list[CreateSearchCriteriaScopeInfo]) -> CreateSearchCriteriaScpResponse:
        """    
             This operation creates the Fnd0ApprSchCriteriaScpAttr object (ScpSrchCriteria)
             based on the inputs supplied. It creates a Scope Search Criteria object and stores
             the scope of the search. Scope Search Criteria object is created as part of the creation
             of the SearchStructureContext object to persist the scope of the search.
             
             If the input contains APNs or BOMLine objects, then these are saved in either
             appearance path nodes list or occurrence list property depending on the value of
             RDV_CREATE_SCO_WITHOUT_APN preference. If the input contains appearance groups, these
             are stored in occurrence group list property of ScpSrchCriteria object.
             

Use Cases:

             1. Creating a Search Search Criteria
             
             While persisting the search criteria in Search Structure Context object, createSearchCriteriaScope operation is called to persist the scope
             of the search. User can create this object by providing the CreateSearchCriteriaScopeInfo structure. This scope search criteria
             object is wrapped in Appearance Search Criteria Group object and stored in SearchStructureContext
             object.
             


Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param Inputs: 
                         An object of <b>Fnd0ApprSchCriteriaScpAttr</b> is created for each <font face="courier" height="10">CreateSearchCriteriaScopeInfo</font> in the inputs list. The data in
                         the <font face="courier" height="10">CreateSearchCriteriaScopeInfo</font> like <b>BOMLine</b>
                         objects and appGrps is used to create object of <b>Fnd0ApprSchCriteriaScpAttr</b>.
             
        :return: 
        """
        ...
    def CreateSearchSCO(self, Inputs: list[CreateSearchSCOInputInfo]) -> CreateSearchSCOResponse:
        """    
             Creates the SearchStructureContext object (SearchSCO) based on the inputs
             supplied. It creates a SearchSCO object and then sets the following properties on
             SearchSCO object created: Product Item Revision, Revision Rule, Variant Rule, Work
             parts selected, Search Criteria Group, Target and Background BOMLine objects
             from the input structure, result stored status, object shared status. This SearchSCO
             will contain the Item, Item revisions, Target BOMLine objects, Background
             BOMLine objects. The operation is designed to support multiple SearchSCOs
             creation in a single call. The operation will initially create the SearchSCO object
             using the name, type and description. Subsequently it would set the additional parameters
             supplied through the input structure. SearchSCO object would still be created and
             saved even if setting of the additional parameters is not successful.
             

Use Cases:

             1. Create a Search SCO
             
             You can create a new SCO object of type SearchStructureContext using createSearchSCO operation, by providing the CreateSearchSCOInputInfo structure.
             


Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param Inputs: 
                         An object of <b>SearchStructureContext</b> is created for each <font face="courier" height="10">CreateSearchSCOInputInfo</font> in the inputs list. The data in the <font face="courier" height="10">CreateSearchSCOInputInfo</font> like name and description
                         along with search related information is used to create object of <b>SearchStructureContext</b>.
             
        :return: 
        """
        ...
    def UpdateSearchSCO(self, Inputs: list[UpdateSearchSCOInputInfo]) -> UpdateSearchSCOResponse:
        """    
             Updates the Search Structure Context Object (SearchSCO) based on the inputs attributes.
             It sets the following properties on SearchSCO object which is to be modified: Product
             Item Revision, Revision Rule, Variant Rule, Work parts selected, Search Criteria
             Group, Target and Background BOMLine objects, and result status from the input
             structure. This SearchSCO will contain the Item, Item revisions, Target BOMLine
             objects, Background BOMLine objects. The operation is designed to support
             multiple SearchSCOs creation in a single call. This operation first checks for the
             local ownership of the object to be updated. This operation will fail if null or
             incorrect reference to existing SearchSCO object is passed in the input.
             

Use Cases:

             You can update an SCO object of type SearchStructureContext using updateSearchSCO operation by providing the UpdateSearchSCOInputInfo structure.
             

Create an SCO, object of SearchStructureContext, using the
             createSearchSCO operation.
             
Retrieve the reference to SearchStructureContext returned
             from above step.
             
Modify the required search criteria and populate the UpdateSearchSCOInputInfo structure.
             
Call updateSearchSCO which
             will modify the existing SearchStructureContext object.
             



Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param Inputs: 
                         An object of <b>SearchStructureContext</b> is updated for each <font face="courier" height="10">UpdateSearchSCOInputInfo</font> in the inputs list. The data in the <font face="courier" height="10">UpdateSearchSCOInputInfo</font> object is used for updating.
             
        :return: 
        """
        ...
    def GetICSClassNames(self, SearchCriteriaInClass: list[Teamcenter.Soa.Client.Model.Strong.ApprSearchCriteriaInClass]) -> GetICSClassNamesResponse:
        """    
             Creates a list of ICS class names for the ApprSearchCriteriaInClass objects
             passed in the input. Object of ICS class is stored inside ApprSearchCriteriaInClass
             object and this is persisted along with other search criteria in Structure Context
             object (SCO). During replay of SCO, in order to reconstruct the Classification object
             this operation is called to get the class name. Using this class name ICS object
             is recreated at client side. This method is required because the classification object
             cannot be retrieved in its original format from the SCO object.
             

Use Cases:

1. Replaying an SCO

             You can reconstruct the classification object stored in SCO using the class name
             returned from the getICSClassNames operation
             by providing the reference to the ApprSearchCriteriaInClass object.
             

Create an SCO, object of StructureContext, using the createSCO operation.
             
Retrieve the reference to StructureContext returned from above
             step.
             
Fetch the reference of ApprSearchCriteriaInClass stored in
             the Appearance Grouping object.
             
Provide the object retrieved above to getICSClassNames
             operation.
             



Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param SearchCriteriaInClass: 
                         List of Appearance InClass Search Criteria, i.e. <b>ApprSearchCriteriaInClass</b>,
                         object for which ICS class names are to be fetched.
             
        :return: object and returned as partial
             error.
        """
        ...

