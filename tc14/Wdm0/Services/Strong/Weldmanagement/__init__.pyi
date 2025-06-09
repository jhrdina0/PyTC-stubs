import System
import Teamcenter.Soa.Client
import Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement

class WeldManagementRestBindingStub(WeldManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateUpdateWelds(self, Inputs: list[Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.CreateWeldInput]) -> Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.CreateWeldResp: ...
    def DeleteWelds(self, Inputs: list[Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.DeleteWeldInput]) -> Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.DeleteWeldResp: ...
    def FindWelds(self, Inputs: list[Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.FindWeldInput]) -> Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.FindWeldResp: ...

class WeldManagementService:
    """
    
            This service exposes the functionalities of Teamcenter Weld
Management to service
            clients. It contains a set of service operations that can publish
weld feature to
            Teamcenter, including create, update and delete and find operation.

            The defined weld features in nx are children nodes created
underneath weld component
            (in the assembly structure). Those child nodes are weld feature
business object type
            (ArcWeld, DatumPoint, WeldPoint, WdM0SurfaceAdd) in teamcenter,
            which are individual items and item revisions of PSConnection. This
will enable
            lifecycle management and configuration support for individual
welding features and
            datum items which in turn would enable the downstream applications.

            Weld component revision contains NX dataset to defined the weld
features. Weld feature
            revision contains JT dataset as well as weld feature attribute form
for individual
            weld feature. Weld features are linked to connection part via
"TC_CONNECT_TO" relationship.

            The WeldManagement service can be used for supporting following use-
cases:

Create weld feature items/revisions by providing a list of CreateWeldInput
            structure.

Modify the existing weld feature item/revision to set/modify attributes
            in form, JT file,connecto_to part information.

Delete weld component and weld feature by providing a list of DeleteWeldInput
            structure.

Finding/retrieve weld component parts by providing a list of FindWeldInput
            structure.

Library Reference:

WdM0SoaWeldManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> WeldManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateUpdateWelds(self, Inputs: list[Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.CreateWeldInput]) -> Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.CreateWeldResp:
        """    
             This operation creates or modifies weld feature business objects for the CreateWeldInput
             supplied.The CreateWeldInput contains information for properties client Id,
             parent bvr that is used to create bom window contains weld components as well as
             connection parts, WeldCompWithFeatData. WeldCompWithFeatData contains
             weld component information and Weld feature data properties of UG Entity Handle,
             attriubtes, forms, JT file, JT ticket, connected part information, weld feature type,revise
             mark.
             

             Server implementation compares the features list from input with the one retrieved
             from weld component occurrence in Teamcenter. if the weld feature does not exist,
             then the features  will be created in weld component occurrence and added as children.
             If the weld feature exists, then the features  will be updated based on the input
             information.  If the features is missing from input, the features will be removed
             from weld component occurrence children.
             

             Client application should mark the features that are to be revised. by default the
             revise mark is false, if the revise mark set to true, the new weld feature revison
             will be created and attached to the weld component.Rest of the features are assumed
             to be updated.
             

Use Cases:

             when you enable weld publish option and  save the assembly part that including weld
             feature, the SOA createUpdateWeld will be called and weld feature will be created
             in teamcenter.
             

Teamcenter Component:

             Weld Management - Weld Management SOA service.
             
        :param Inputs: 
                         List of create/update weld component inputs.
             
        :return: The created/updated weld feature business objects are returned via CreateWeldResp
             in Created/Updated lists
        """
        ...
    def DeleteWelds(self, Inputs: list[Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.DeleteWeldInput]) -> Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.DeleteWeldResp:
        """    
             This operation deletes weld components and weld feature business objects for the
             DeleteWeldInput supplied.The DeleteWeldInput contains information for
             properties client Id, parent bvr that is used to create bom window contains weld
             components as well as connection parts, List of weld components to be deleted, Type
             of relation from weld feature object to connection parts,and logical destroy mark.
             The destory mark will determine destroy object or just remove from the structure,
             if it is true, weld component and feature objects will be destroyed  from TC; if
             it is false, the weld component will be removed from assembly structure.
             

Use Cases:

             You can delete weld components or weld features(destroy or remove it from structure
             based on the destroy mark argument)  using deleteWelds operation by providing
             a list of DeleteWeldInput.
             

Teamcenter Component:

             Weld Management - Weld Management SOA service.
             
        :param Inputs: 
                         List of delete weld component inputs.
             
        :return: List of message on eached weld component showing whether is deleted or failed to
             be deleted.
        """
        ...
    def FindWelds(self, Inputs: list[Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.FindWeldInput]) -> Wdm0.Services.Strong.Weldmanagement._2012_02.WeldManagement.FindWeldResp:
        """    
             This operation find weld components by the FindWeldInput supplied. The FindWeldInput
             contains information for properties client Id, parent bvr that is used to create
             bom window contains weld components as well as connection parts, Connection part
             PS Occurrences, which must fall in the bom window that created by parent BVR, Connection
             relation type, Weld component types as a filter, for example, weld component and
             features occurrence are related to connection part APN by TC_CONNECT_TO relation.
             

Use Cases:

             You can find weld components using findWelds operation by providing a list
             of  FindWeldInput structure.
             

Teamcenter Component:

             Weld Management - Weld Management SOA service.
             
        :param Inputs: 
                         List of find weld component inputs.
             
        :return: List of weld components.
        """
        ...

