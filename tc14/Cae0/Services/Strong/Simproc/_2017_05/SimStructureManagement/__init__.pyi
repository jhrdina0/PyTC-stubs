import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class StructureMapExecutionResponse:
    """
    
            StructureMapExecutionResponse represents the outputs of the internal execute StructureMap
            and execute Datamap operations.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The root ItemRevision of the output structure is returned as a part of the
            Created Object in the Service Data.
            """
    ActivityLog: str
    """
            A summary log having a fixed format containing the results of the DataMap
            and StructureMap rules applied to the input structure and the output
            items created. The details include what DataMap and StructureMap rules
            were applied, type of the output item created, the Item ID of the output item, the
            relationships created between the input and the output ItemRevision. Any failures
            in creation of the output item or relationships are also returned as a part of the
            activity log. The log does not exceed 20 lines of text.
            """

class StructureMapInputsInfo:
    """
    A structure for input parameters of executeStructureMap service operation.
    """
    def __init__(self, ) -> None: ...
    RootIR: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """
ItemRevision of the root item of the input structure. This can be null if
            the snapshotFolder is provided as input to the operation. If the rootIR
            is not null and snapshotFolder is also provided as an input, then rootIR
            input will be ignored and snapshotFolder will take precedence.
            """
    SnapshotFolder: Teamcenter.Soa.Client.Model.Strong.Snapshot
    """
            The Snapshot folder of the input structure. The snapshotFolder can
            be null if the root rootIR is used as an input to the operation. The snapshotFolder
            takes precedence over the rootIR.
            """
    RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule
    """
            The RevisionRule of the input structure. This is an optional parameter and
            can be provided if the root ItemRevision is used as an input to the operation.
            This parameter will be ignored if snapshotFolder is used as an input.
            """
    VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule
    """
            The VariantRule for the input structure. This can be provided for both, the
            rootIR or snapshotFolder as input. This is an optional parameter and
            can be null.
            """
    Domain: str
    """
            The domain for the Data Map rules to be applied. The datamapping.xml
            file can be configured for various domains defined as LOV objects under StructureMap
            Domains in BMIDE. This argument is used to specify which domain to be used
            from the datamapping.xml file. If the value is not provided, the default is
            assumed to be CAE. If StructureMapRevision is null, then domain value will
            be considered and Datamapping will be executed.
            """
    StructureMapIR: Teamcenter.Soa.Client.Model.Strong.StructureMapRevision
    """
            The StructureMapRevision containing a CAEStructureMap Dataset
            with an XML named reference containing valid StructureMap rules. If
            StructureMapRevision is not null, then domain value will be ignored.
            """
    InputOptions: System.Collections.Hashtable

class SimStructureManagement:
    """
    Interface SimStructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteStructureMap(self, StructureMapInputs: StructureMapInputsInfo) -> StructureMapExecutionResponse:
        """    
             This operation creates an output BOM structure given the root ItemRevision
             of the root BOMLine of an input BOM structure along with its RevisionRule
             and the VariantRule. A Snapshot folder of the input BOM structure along
             with the VariantRule can also be provided as an input. The output BOM structure
             is determined by the XSLT-based Data Map rules executed against the input
             BOM structure. Data Map syntax is in compliance with the schema defined in
             tcsim_xslWithNode.xsd, located in TC_DATA.
             

Data Map rules define the mapping between an input item type and its resulting
             output item type. Data Map rules are defined for an entire site and are stored
             in the datamapping.xml file located in TC_DATA. The name of the datamapping
             file is defined by the site preference CAE_dataMapping_file.
             

             The Data Map rules can be configured for various domains defined as LOV objects
             under StructureMap Domains in BMIDE. To configure the domains, in the Extensions
             view in BMIDE, open LOV->StructureMap Domains and add additional domain
             values. The domain to be used for applying Data Map rules can also be provided
             as an input.
             

             To use this operation, a well-defined datamapping.xml is required in TC_DATA
             and the user should have either a simulation_author or rtt_author license.
             

             This service operation calls asynchronous service operation internlly to execute
             Datamap with the given parameters.
             

Use Cases:

             A user can asynchronously execute StructureMap function in ActiveWorkspace Client
             using an existing opened Product structure. Subsequently CAEModel structure
             and a relation are created between newly created CAEModel structure and the
             selected  Product Structure.
             
             Use Case 1: Open a Product structure, select root ItemRevision and internally
             call operation to execute StructureMap asynchronously.
             

             Use Case 2: Open a Product structure, apply revision and variant configurations on
             that structure and internally call operation to execute StructureMap asynchronously.
             

Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param StructureMapInputs: 
                         A structure holding inputs for executeStructureMap operation.
             
        :return: 206679 - Mapped BOMView Type does not exist, creating default view type.
        """
        ...

