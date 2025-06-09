import System
import Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement
import Teamcenter.Services.Strong.Rdv._2009_04.ContextManagement
import Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement
import Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement
import Teamcenter.Services.Strong.Rdv._2013_05.ContextManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class ContextManagementRestBindingStub(ContextManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AddPartToProduct(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.AddPartSolutionInputInfo]) -> Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.AddPartSolutionResponse: ...
    def GetProductItemInfo(self) -> Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.GetProductItemResponse: ...
    def RemovePartsRelatedToABE(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.RemoveABEPartsInputInfo]) -> Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.GetRemoveABEPartsResponse: ...
    def ReplacePartInProduct(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.ReplacePartSolutionInputInfo]) -> Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.ReplacePartSolutionResponse: ...
    def GetPastePrimeAttributes(self, Input: Teamcenter.Services.Strong.Rdv._2009_04.ContextManagement.GetPastePrimeInfo) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetAllGOPartSolutions(self, GoBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> Teamcenter.Services.Strong.Rdv._2009_04.ContextManagement.GetGOPartSolutionsResponse: ...
    def CreateSCO(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.CreateSCOInputInfo]) -> Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.CreateSCOResponse: ...
    def UpdateSCO(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.UpdateSCOInputInfo]) -> Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.UpdateSCOResponse: ...
    def CreateFormAttrSearchCriteria(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateFormAttrSearchCriteriaInputInfo]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateFormAttrSearchCriteriaResponse: ...
    def CreateSearchCriteriaScope(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateSearchCriteriaScopeInfo]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateSearchCriteriaScpResponse: ...
    def CreateSearchSCO(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateSearchSCOInputInfo]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateSearchSCOResponse: ...
    def UpdateSearchSCO(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.UpdateSearchSCOInputInfo]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.UpdateSearchSCOResponse: ...
    def GetICSClassNames(self, SearchCriteriaInClass: list[Teamcenter.Soa.Client.Model.Strong.ApprSearchCriteriaInClass]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.GetICSClassNamesResponse: ...
    def GetRelatedObjectsInContext(self, ObjectList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Rdv._2013_05.ContextManagement.ContextObjectResponse: ...

class ContextManagementService:
    """
    
ContextManagement service allows a designer
            to accurately model specific product assembly configurations and use
the results
            with analytical and visualization tools to facilitate learning and
decision making.

            The Design Context application allows the user to quickly focus on a
particular
            work part in the Context Management environment and any other parts
affected
            within the context of a change to that part.

            When you have identified your parts, you can view them in the
embedded viewer in
            Structure Manager or a CAD tool or send them to Lifecycle
Visualization.
            You can also perform clearance analysis in Structure Manager or
Lifecycle
            Visualization. Design Context also interoperates with Platform
Designer
            to manage changes to the design solutions in the product.

            The ContextManagement service provides operations
            to carry out the following context management related use-cases.

            1)Â Â Â Â Retrieve product context information

            2)Â Â Â Â Manage the objects that are used to store the search
            criteria information

Retrieve the Product Context Information:  The ContextManagement
            service provides the getProductItemInfo operation,
            which can be used to retrieve all the Product Context objects that
are available
            in the database.  The Product Context is an item of type Item or
subtype whose
            properties satisfy the values specified through preference settings
of the PortalDesignContextProductItemProperties
            preference. Please refer to the operation documentation for more
detailed information.

Manage the search criteria persistence objects: The context management service
            provides a set of operations, which can be used to maintain a
structure context
            object. A structure context object is a top level container that
houses all
            the information related to search criterion specified for multiple
search criteria.

            This service also provides an operation to create
SearchStructureContext object
            which is a subtype of the structure context object and provides
support for saving
            additional information such as scope of the search etc.,

            In addition to the search criteria objects the service provides an
operation
            to create the search criteria for the Form attribute based search
criteria
            and the scope criteria used in the search.  Currently SOA operations
are not available
            for storing any other types of search criteria objects. All other
search criteria
            could currently be managed through operations in the legacy ICT
layer.

            The ContextManagement service also provides
            an operation to get the ICS Class Names as required in the
classification search.
            However, this operation would need to be used in conjunction with
current ICT layer
            calls that are available to create the Classification Attribute
Based search criteria
            persistence objects.

            The steps in creating the search criteria object are mentioned below

            1)Â Â Â Â Perform a Form Attribute Based Search.

            2)Â Â Â Â Capture the search criteria from the UI using existing
            data structure in the UI code.

            3)Â Â Â Â Convert the search criteria into the data structure
accepted
            by the createFormAttrSearchCriteria.

            4)Â Â Â Â Invoke the createFormAttrSearchCriteria
            to create the search criteria object.

            5)Â Â Â Â Group the search criteria object into a search criteria
            grouping object. SOA is unavailable for performing this step
currently. We need
            to use an ICT call for this function.

            6)Â Â Â Â Use the grouping object tag along with other criteria
information
            that forms the overall context of the search and create a structure
context object.

Dependencies:

            StructureManagement

Library Reference:

TcSoaRdvStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ContextManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AddPartToProduct(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.AddPartSolutionInputInfo]) -> Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.AddPartSolutionResponse:
        """    
             get the required Information for add part to product.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param Inputs: 
                         Vector of structure containing the required info to call add part to product
             
        :return: contains required info regarding the success of add part to product for the inputs
             provided.
        """
        ...
    def GetProductItemInfo(self) -> Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.GetProductItemResponse:
        """    
             Returns a list of all Product Items found in the database. The following preferences
             can be used to define an object as a Product Item.
             
             The preference PortalDesignContextProductItemProperties is used to specify one or
             more of the following properties to be used to define the object as Product Item.
             Multiple properties could be specified at the same time and the algorithm will check
             all the specified property values to be satisfied in order to deem an object as a
             Product Item.
             

    object_type
             
    object_desc
             
    owning_group
             


             For Example: PortalDesignContextProductItemProperties = object_type,object_desc
             
             The preference PortalDesignContextProductItemProperties.<property_name>  is used
             to specify the value to be checked in order to determine whether the object is a
             Product Item. For example: PortalDesignContextProductItemProperties.object_type =
             CORP_Vehicle
             
             Only an object of type Item or its sub type could be defined as a Product
             Item. The operation will return empty if any other objects are specified.
             
             The default values are
             
             PortalDesignContextProductItemProperties = object_type, object_desc
             
             PortalDesignContextProductItemProperties.object_type=Item
             
             PortalDesignContextProductItemProperties.object_desc=Product
             

Use Cases:

             The getProductItemInfo operation is called
             when user wants to fetch all Product Items present in the database which are defined
             by setting the PortalDesignContextProductItemProperties preference.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :return: 
        """
        ...
    def RemovePartsRelatedToABE(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.RemoveABEPartsInputInfo]) -> Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.GetRemoveABEPartsResponse:
        """    
             Deletes all the related Part Solutions of an Architecture Breakdown Element (ABE).
             The links through which the Part solutions are related to the Architecture Breakdown
             Element are also removed.
             

Use Cases:

             The removePartsRelatedToABE operation is
             called when user wants to remove all part solutions related to Architecture Breakdown
             Element and their corresponding links. The user can specify the input Architecture
             Breakdown Element and top line to which the Architecture Breakdown Element is linked
             using RemoveABEPartsInputInfo object.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param Inputs: 
                         The list of <font face="courier" height="10">RemoveABEPartsInputInfo</font> objects.
                         Each object contains all the required information to remove Part Solutions related
                         to the Architecture Breakdown Element along with configured Part Data information.
             
        :return: object and a partial error will be returned.
        """
        ...
    def ReplacePartInProduct(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.ReplacePartSolutionInputInfo]) -> Teamcenter.Services.Strong.Rdv._2008_05.ContextManagement.ReplacePartSolutionResponse:
        """    
             get the required Information for replace part in product.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param Inputs: 
                         Vector of structure containing the required info to call replace part in product
             
        :return: contains required info regarding the success of replace part in product for the inputs
             provided.
        """
        ...
    def GetPastePrimeAttributes(self, Input: Teamcenter.Services.Strong.Rdv._2009_04.ContextManagement.GetPastePrimeInfo) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation pastes source Architecture Breakdown Element (ABE) BOMLine
             to the target Architecture Breakdown (AB) BOMLine. It pastes all the
             parents (up to top level AB) of the source ABE under target AB. This operation also
             copies the variability, Named Variant Expressions (NVEs) and part solutions from
             the source BOMLine to target BOMLine.
             

Use Cases:

             This operation can be used to paste the source Architecture Breakdown Element BOMLine
             to target Architecture Breakdown BOMLine.
             

             Use case 1: Copy variability
             
             User needs to set flag value as 1 in GetPastePrimeInfo structure to copy only the
             variability from the source BOMLine to target BOMLine.
             

             Use case 2: Copy variability and NamedVariantExpressions
             
             User needs to set flag value as 2 in GetPastePrimeInfo structure to copy the variability
             and Named Variant Expressions from the source BOMLine to target BOMLine.
             

             Use case 3: Copy variability, NamedVariantExpressions and part solutions
             
             User needs to set flag value as 3 in GetPastePrimeInfo structure to copy the variability,
             Named Variant Expressions and part solutions from the source BOMLine to target
             BOMLine.
             


Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param Input: 
                         Reference to <font face="courier" height="10">GetPastePrimeInfo</font> object which
                         contains the list of source and target <b>BOMLine</b> and a flag to indicate which
                         attributes needs to be copied from the source <b>BOMLine</b> to target <b>BOMLine</b>.
             
        :return: 
        """
        ...
    def GetAllGOPartSolutions(self, GoBomLine: Teamcenter.Soa.Client.Model.Strong.BOMLine) -> Teamcenter.Services.Strong.Rdv._2009_04.ContextManagement.GetGOPartSolutionsResponse:
        """    
             Get the required information for display of part solutions of selected GBE and its
             instantiating ABE.
             

Teamcenter Component:

             Platform Designer - Application to create and manage architecture breakdowns and
             product variability.
             
        :param GoBomLine: 
                         contains selected GBE bomline
             
        :return: Contains vector of APN of line of usages (part solution) and            instantiating
             architecture bom window
        """
        ...
    def CreateSCO(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.CreateSCOInputInfo]) -> Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.CreateSCOResponse:
        """    
             Creates the Structure Context Object (SCO) based on the inputs supplied. It creates
             an SCO object and then sets the following properties on SCO object created: Product
             Item Revision, Revision Rule, Variant Rule, Work parts selected, Search Criteria
             Group, Target and Background BOMLine objects from the input structure. This
             SCO will contain the Item, Item revisions, Target BOMLine objects, Background
             BOMLine objects. The operation is designed to support multiple SCOs creations
             in a single call. (Limitation: Though this operation can create multiple SCO objects
             however it can return reference of only one object). The operation will initially
             create the SCO object using the name, type and description. Subsequently it would
             set the additional parameters supplied through the input structure. SCO object would
             still be created and saved even if setting of the additional parameters is not successful.
             

Use Cases:

1. Create an SCO

             YouYou can create a new SCO object of type VisStructureContext using createSCO operation by providing the CreateSCOInputInfo structure.
             


Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param Inputs: 
                         An object of <b>StructureContext</b> is created for each <font face="courier" height="10">CreateSCOInputInfo</font>
                         object  in the inputs list. The data in the <font face="courier" height="10">CreateSCOInputInfo</font>
                         like SCO type, name, and description along with search related criteria is used to
                         create object of <b>StructureContext</b>.
             
        :return: 
        """
        ...
    def UpdateSCO(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.UpdateSCOInputInfo]) -> Teamcenter.Services.Strong.Rdv._2010_09.ContextManagement.UpdateSCOResponse:
        """    
             Updates the Structure Context Object (SCO) based on the inputs attributes. It sets
             the following properties on SCO object which is to be modified: Product Item Revision,
             Revision Rule, Variant Rule, Work parts, Search Criteria Group, Target and Background
             BOMLine objects from the input structure. This SCO will contain the Item,
             Item revisions, Target BOMLine objects, Background BOMLine objects.
             The operation is designed to support multiple SCOs creations in a single call. (Limitation:
             Though this operation can update multiple SCO objects however it can return reference
             of only one object). This operation first checks for the local ownership of the object
             to be updated. This operation will fail if null or incorrect reference to existing
             SCO object is passed in the input.
             

Use Cases:

             1. Update an SCO
             
             You can update an SCO object of type VisStructureContext using updateSCO operation by providing the UpdateSCOInputInfo
             structure.
             

Create an SCO, object of StructureContext, using the createSCO operation.
             
Retrieve the reference to StructureContext returned from above
             step.
             
Modify the required search criteria and populate the UpdateSCOInputInfo structure.
             
Call updateSCO which will
             modify the existing StructureContext object.
             



Dependencies:

             createSCO
             

Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param Inputs: 
                         An object of <b>StructureContext</b> is updated for each <font face="courier" height="10">UpdateSCOInputInfo</font>
                         in the inputs list. The data in the <font face="courier" height="10">UpdateSCOInputInfo</font>
                         object is used for updation.
             
        :return: 
        """
        ...
    def CreateFormAttrSearchCriteria(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateFormAttrSearchCriteriaInputInfo]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateFormAttrSearchCriteriaResponse:
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
    def CreateSearchCriteriaScope(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateSearchCriteriaScopeInfo]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateSearchCriteriaScpResponse:
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
    def CreateSearchSCO(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateSearchSCOInputInfo]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.CreateSearchSCOResponse:
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
    def UpdateSearchSCO(self, Inputs: list[Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.UpdateSearchSCOInputInfo]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.UpdateSearchSCOResponse:
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
    def GetICSClassNames(self, SearchCriteriaInClass: list[Teamcenter.Soa.Client.Model.Strong.ApprSearchCriteriaInClass]) -> Teamcenter.Services.Strong.Rdv._2012_09.ContextManagement.GetICSClassNamesResponse:
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
    def GetRelatedObjectsInContext(self, ObjectList: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Rdv._2013_05.ContextManagement.ContextObjectResponse:
        """    
             This operation finds all the business objects that are within the current active
             context of the list of objects sent as input. The objects within context are objects
             of the types specified below that are related to the input object either through
             reference or relation.
             

Items

Processes

ChangeRequestRevision

StructureContext

AppearanceGroup





             The RDV module maintains a state that defines the currently active context. A combination
             of one or more of the following objects defines the current active context.
             

WorkpartItem

Process

ChangeRequestRevision

ConfigurationContext

StructureContext

AppearanceGroup





             Every time this operation is invoked, the objects in the current context are refreshed.
             
             This operation is mainly used for adding work parts, EngChange revisions and processes
             to the Design Context application.
             
             The following criteria is used to determine the objects related to the inputs:
             

             1) Item objects that are attached with the ChangeRequestRevision, Process objects
             through the relation type mentioned in the preferences listed below.
             

PortalDesignContextProcess.WorkPartOrChangeAttachmentTypes

PortalDesignContextECObject.WorkPartRelationships



             2) Item objects that are associated with the EPM job where the input object is also
             a part of the EPM job.
             

             3) Item objects that are part of the same ConfigurationContext object, StructureContext
             object or an AppearanceGroup object as that of the input objects.
             

Use Cases:

             Use Case 1: If user enters an item ID in the WorkParts text field in DesignContext
             application. The Design Context application uses this operation to display the item
             revision in the WorkParts list, and any changes or processes that reference the item
             revision in the EngChange Revision and Processes lists.
             

             Use Case 2: If user enters a change ID in the EngChange Revision text field DesignContext
             application. The DesignContext application uses this operation to add the change
             object to the EngChange Revision list, and any item revisions or processes referenced
             by the change object are displayed in the WorkParts and Processes lists. If the change
             references revisions of Product Items, Teamcenter automatically adds them to the
             Selected Product Context list.
             

             Use Case 3: If user enters a process name in Processes test field DesignContext application.
             The DesignContext application uses this operation to add the process object to the
             Processes list, and any objects targeted by the process are displayed in the WorkParts
             and EngChange lists.
             

             The items in the WorkPart lists can then be selected by the user for carrying out
             the design validation analysis.
             

Teamcenter Component:

             Context Management - Application to perform Digital Product Validations. This also
             lists other ITK Main programs maintained by RDV Team.
             
        :param ObjectList: 
<ul>
<li type="disc"><b>Items</b>
</li>
<li type="disc"><b>Processes</b>
</li>
<li type="disc"><b>ChangeRequestRevision</b>
</li>
<li type="disc"><b>StructureContext</b>
</li>
<li type="disc"><b>AppearanceGroup</b>
</li>
</ul>

        :return: 
        """
        ...

