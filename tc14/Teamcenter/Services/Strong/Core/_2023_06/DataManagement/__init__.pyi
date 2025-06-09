import System
import Teamcenter.Services.Strong.Core._2008_06.DataManagement
import typing

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateObjects(self, CreateInputs: list[Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateIn], RunInBackground: bool) -> Teamcenter.Services.Strong.Core._2008_06.DataManagement.CreateResponse:
        """    
             Generic operation for creation of Business Objects. This will also create any secondary(compounded)
             objects that need to be created, assuming the CreateInput for the secondary object
             is represented in the recursive CreateInput object e.g. Item is Primary Object
             that also creates Item Master and ItemRevision. ItemRevision
             in turn creates ItemRevision Master. The input for all these levels
             is passed in through the recursive CreateInput object.
             

             This creation of Business Objects is performed in Foreground or Background mode as
             specified in the input to this operation.
             

Use Cases:

             CreateObjects in Synchronous mode:
             
             This operation to create an object is invoked after obtaining user input on the fields
             of the create dialog with the runInBackground attribute value as false. This call
             is typically preceded by a call to Teamcenter::Soa::Core::_2008_06::PropDescriptor::getCreateDesc
             or to the SOA Client Metamodel layer to retrieve Create Descriptor for a Business
             Object.
             

             For example, to create an Item, client will get the Create Descriptor associated
             with the Item from the client metamodel (The associated descriptor type can
             be found by looking at the constant value for the CreateInput constant that is attached
             to Item). Alternatively, for clients that do not use the SOA client metamodel,
             the Descriptor for Item can be obtained by invoking getCreateDesc operation. The
             descriptor information can then be used to populate the Create dialog for the Business
             Object. Once the Create dialog is populated the createObjects operation can be called
             to create the object.
             

             CreateObjects in Asynchronous mode:
             
             This operation to create an object is invoked after obtaining user input on the fields
             of the create dialog with the runInBackground attribute value as true.
             

Dependencies:

             getCreateDesc
             

Teamcenter Component:

             Metamodel - Framework to define data model, operations, extensions and for autogeneration
             of the underlying code for appropriate dispatching. It provides the framework for
             codeless configuration and codeful customization.
             
        :param CreateInputs: 
                         A list of CreateIn objects each one of which represents the CreateInput information
                         used to create an object. Each CreateIn object has a client id and a CreateInput
                         object which contains the information to create the object. The client id can be
                         used to map to any partial errors in the ServiceData information returned in the
                         output.
             
        :param RunInBackground: 
                         If true, the operation is performed in background mode in a separate asynchronous
                         server session; otherwise, perform the operation synchronously.
             
        :return: Teamcenter::Soa::Server::ServiceException:
        """
        ...

