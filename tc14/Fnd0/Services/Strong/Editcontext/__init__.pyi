import Fnd0.Services.Strong.Editcontext._2015_07.DataManagement
import Fnd0.Services.Strong.Editcontext._2016_04.DataManagement
import Fnd0.Services.Strong.Editcontext._2016_10.DataManagement
import System
import System.Collections
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class DataManagementRestBindingStub(DataManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def SetEditContext(self, Context: Teamcenter.Soa.Client.Model.Strong.Fnd0EditContext, Objects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetReferencerEditContexts(self, InputObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Fnd0.Services.Strong.Editcontext._2015_07.DataManagement.ReferencerEditContextsResponse: ...
    def SetChangeContext(self, Inputs: System.Collections.Hashtable) -> Fnd0.Services.Strong.Editcontext._2016_04.DataManagement.SetChangeContextResponse: ...
    def SetChangeContext2(self, Inputs: System.Collections.Hashtable) -> Fnd0.Services.Strong.Editcontext._2016_10.DataManagement.SetChangeContextResponse2: ...

class DataManagementService:
    """
    
            Data Management Service for Edit Context.
            


Library Reference:

Fnd0SoaEditContextStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DataManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def SetEditContext(self, Context: Teamcenter.Soa.Client.Model.Strong.Fnd0EditContext, Objects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             If input parameter "context" is not null, the SOA response will contain the input
             Business Objects configured with the configuration parameter belonging to the input
             context. If any of the input Business Objects are not POM Revisable, they will be
             returned without configuration parameter. The Business Objects will be added to the
             Plain Objects array in ServiceData.
             
             If input parameter "context" is null, the input Business Objects will be configured
             for Public edits and returned in the SOA response.
             

Use Cases:

             This operation will enable the user to enter or exit edit mode and subsequently save
             the edits as Private Edits.
             

Teamcenter Component:

             Edit Context - Teamcenter Component for Edit Context.
             
        :param Context: 
                         A context containing a configuration parameter that is used to configure the input
                         Business Objects.
             
        :param Objects: 
                         The array of objects to be configured for edit.
             
        :return: 
        """
        ...
    def GetReferencerEditContexts(self, InputObjects: list[Teamcenter.Soa.Client.Model.Strong.WorkspaceObject]) -> Fnd0.Services.Strong.Editcontext._2015_07.DataManagement.ReferencerEditContextsResponse:
        """    
             This operation will return the list of context (Fnd0EditContext) objects that
             reference the input WorkspaceObjects.
             

Use Cases:

             This operation enables the following use case.
             
             Use Case 1: User wants to provide a list of edit contexts that can be used to configure
             a business object to enable editing in a particular context.
             

User provides the business object as the input to this operation.
             
A list of edit contexts that reference the business object are returned.
             Any of these edit contexts can be used for configuring the business object for editing
             in that particular context.
             



Teamcenter Component:

             Edit Context - Teamcenter Component for Edit Context.
             
        :param InputObjects: 
                         The list of objects whose referencing edit contexts are required.
             
        :return: 
        """
        ...
    def SetChangeContext(self, Inputs: System.Collections.Hashtable) -> Fnd0.Services.Strong.Editcontext._2016_04.DataManagement.SetChangeContextResponse:
        """    
             This operation will configure business objects so that the objects can be edited
             or inspected in a context without changing the public versions of the objects. This
             operation can also be used to remove the configuration of business objects in order
             to edit or inspect the public versions of the objects.
             
             This operation does not have any effect on business objects that are not minor revisable
             and such objects will always be returned without being configured.
             
             The operation can be used to configure multiple sets of objects using different contexts.
             

Use Cases:

             Use Case 1: User wants to edit properties of a set of business objects in a context
             with the intention to  collaborate with other users.
             

User creates a Fnd0EditContext object that abstracts the context
             within which the edit needs to be performed.
             
The Fnd0EditContext object is provided as input to the operation
             along with the business objects that need to be edited.
             
The configured business objects are returned in the response and
             can be used for performing edits in the context.
             



             Use Case 2: User wants to edit properties of a set of business objects in a context
             provided by a ChangeNotice.
             

User creates a ChangeNotice object that abstracts the context within
             which the edit needs to be performed.
             
The ChangeNotice object is provided as input to the operation along
             with the business objects that need to be configured.
             
The configured business objects are returned in the response and
             can be used for performing edits in the context.
             



             Use Case 3: User wants to query a property belonging to the public version of a business
             object that is currently configured for editing in a collaborative space.
             

User passes a null value for the context along with the business
             object that needs to be inspected in public.
             
The unconfigured business objects are returned in the response and
             any queries performed on the objects will return public data.
             



Teamcenter Component:

             Edit Context - Teamcenter Component for Edit Context.
             
        :param Inputs: 
                         The objects to be configured and the contexts to be used for configuring the objects.
             
        :return: 
        """
        ...
    def SetChangeContext2(self, Inputs: System.Collections.Hashtable) -> Fnd0.Services.Strong.Editcontext._2016_10.DataManagement.SetChangeContextResponse2:
        """    
             This operation  configures business objects to allow the objects to be edited, queried
             or deleted in a context without changing the public versions of the objects. This
             operation can also configure business objects with no context in order to edit, query
             or delete the public versions of the objects.
             
             This operation does not have any effect on business objects that are not minor revisable
             and such objects will always be returned without being configured.
             
             The operation can be used to configure multiple sets of objects using different contexts.
             

Use Case:

             Use Case 1: User wants to edit the properties of a set of business objects in an
             isolated context with the intention to share the proposed changes with other users.
             


User creates a Fnd0MarkupSpace object that abstracts the context
             within which the edit needs to be performed.
             
The Fnd0MarkupSpace object is provided as input to the operation
             along with the business objects that need to be edited.
             
The configured business objects are returned in the response and
             can be used for performing edits in the context.
             



             Use Case 2: User wants to query the properties of a set of business objects in an
             isolated context that have been edited in the context of a ChangeNotice.
             


User creates a ChangeNotice object that abstracts the context
             within which the edit needs to be performed.
             
The ChangeNotice object is provided as input to the operation
             along with the business objects that need to be configured.
             
The configured business objects are returned in the response and
             can be used for performing edits in the context.
             




             Use Case 3: User wants to query a property belonging to the public version of a business
             object that is currently configured for editing in a collaborative space.
             


User passes a null value for the context along with the business
             object that needs to be inspected in public.
             
The unconfigured business objects are returned in the response and
             any queries performed on the objects will return public data.
             



Teamcenter Component:

             Edit Context - Teamcenter Component for Edit Context.
             
        :param Inputs: 
                         The operation accepts multiple sets of objects that need to be configured using different
                         contexts. A map (business object, list of ChangeContextStructIn) between a context
                         and a list of objects to be configured using this context. The context object can
                         be null, in which case the corresponding list of objects will be configured for public.
                         The context can also be a runtime business object which holds the context and the
                         change configuration mode.
             
        :return: 
        """
        ...

