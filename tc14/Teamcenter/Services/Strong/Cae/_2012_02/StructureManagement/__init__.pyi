import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ExecuteRuleResponse2:
    """
    
ExecuteRuleResponse2 represents the outputs of the published execute StructureMap
            and execute Data Map operations.
            
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            If the root of the output structure has a BOMView Revision, PSBOMViewRevision
            of the root of the output structure is returned as a part of Created Object in the
            Service Data, else the ItemRevision of the root is returned as a part of the
            Created Object in the Service Data.
            """
    ActivityLog: str
    """
            A log containing the results of the Data Map and StructureMap rules
            applied to the input structure and the output items created. The details include
            the Data Map and StructureMap rules applied, type of the output
            item created, the Item ID of the output item, the relationships created between
            the input and the output ItemRevision. Any failures in creation of the output
            item or relationships are also returned as a part of the activity log.
            

            Following are some possible errors returned in ServiceData:
            

206622 Structure Engine unable to load/read/parse Data Map.
            
206642 XML Libraries for StructureMap Engine not available.
            
206643 CAE_dataMapping_file preference not defined.
            
206647 Item creation failed, operation aborted.
            
206648 Occurrence creation failed, operation aborted.
            
206649 Unknown attribute found.
            
206650 Object not modifiable, set attribute operation failed.
            
206651 Form creation failed.
            
206652 BOMView creation failed.
            
206653 Unable to save the Item in the Newstuff folder.
            
206658 Existing Relationship found, relationship not being created.
            
206662 Error encountered in Variant Condition creation.
            
206664 Error in relationship creation.
            
206665 Item node line definition missing in Data Map.
            
206666 StructureMap domain not found for StructureMapRevision.
            
206672 Rules with different domains found in the same StructureMap/Data
            Map.
            
206673 Rules with no domain defined found in StructureMap/Data
            Map.
            
206677 Multiple variant clauses found in the variant condition. Variant
            Condition creation failed.
            
206678 Invalid or missing variant clause expression. Variant Condition
            creation failed.
            
206679 Mapped BOMView Type does not exist, creating default
            view type.
            

"""

class StructureManagement:
    """
    Interface StructureManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteDatamap(self, RootIR: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SnapshotFolder: Teamcenter.Soa.Client.Model.Strong.Snapshot, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule, Domain: str) -> ExecuteRuleResponse2:
        """    
             This operation creates an output BOM structure given the root ItemRevision
             of the root BOMLine of an input BOM structure along with its RevisionRule
             and the VariantRule. A Snapshot folder of the input BOM structure along
             with the VariantRule can also be provided as an input. The output BOM structure
             is determined by the XSLT-based Data Map rules executed against the
             input BOM structure. Data Map syntax is in compliance with the schema defined
             in tcsim_xslWithNode.xsd, located in TC_DATA.
             

Data Map rules define the mapping between an input item type and its resulting
             output item type. Data Map rules are defined for an entire site and are stored
             in the datamapping.xml file located in TC_DATA. The name of the datampping
             file is defined by the site preference CAE_dataMapping_file.
             

             The Data Map rules can be configured for various domains defined as LOV
             objects under StructureMap Domains in BMIDE. To configure the domains,
             in the Extensions view in BMIDE, open LOV->StructureMap Domains
             and add additional domain values. The domain to be used for applying Data Map
             rules can also be provided as an input.
             

             To use this operation, a well-defined datamapping.xml is required in TC_DATA
             and the user should have either a simulation_author or rtt_author license.
             


Use Cases:

             Use Case 1: Create an output structure given a top BOMLine of the input structure
             along with its configuration

             Given an input root BOMLine of a BOM structure, along with its RevisionRule
             and VariantRule, the user can apply Data Map rule to the BOM structure
             and generate a corresponding output BOM structure. The output BOM structure would
             consist of BOMLine occurrences of ItemRevision objects as defined in
             the datamapping.xml file. The user can review the actions executed with the
             process log returned with the BOMViewRevision. An email notification containing
             the activity log would be sent to the current user if the session option for email
             notification is set to true.
             

             Use Case 2: Create an output structure given a Snapshot folder of the input structure
             along with the variant rule

             Given a Snapshot folder of the input BOM structure and its VariantRule,
             the user can apply Data Map rules to the BOM structure and generate a corresponding
             output BOM structure. The output BOM structure would consist of BOMLine occurrences
             of ItemRevision objects as defined in the datamapping.xml file. The
             user can review the actions executed with the process log returned with the BOMViewRevision.
             An email notification containing the activity log would be sent to the current user
             if the session option for email notification is set to true.
             


Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param RootIR: 
<b>ItemRevision</b> of the root item of the input structure. This can be null if
                         the <i>snapshotFolder</i> is provided as input to the operation. If the <i>rootIR</i>
                         is not null and <i>snapshotFolder</i> is also provided as an input, then <i>rootIR</i>
                         input will be ignored and <i>snapshotFolder</i> will take precedence.
             
        :param SnapshotFolder: 
                         The <b>Snapshot</b> folder of the input structure. The <i>snapshotFolder</i> can
                         be null if the root <i>rootIR</i> is used as an input to the operation. The <i>snapshotFolder</i>
                         takes precedence over the <i>rootIR</i>.
             
        :param RevRule: 
                         The <b>RevisionRule</b> of the input structure. This is an optional parameter and
                         can be provided if the root <b>ItemRevision</b> is used as an input to the operation.
                         This parameter will be ignored if <i>snapshotFolder</i> is used as an input.
             
        :param VariantRule: 
                         The <b>VariantRule</b> for the input structure. This can be provided for both, the
                         <i>rootIR</i> or <i>snapshotFolder</i> as input. This is an optional parameter and
                         can be null.
             
        :param Domain: 
                         The domain for the <i>Data Map rules</i> to be applied. The <i>datamapping.xml</i>
                         file can be configured for various domains defined as <b>LOV</b> objects under <b>StructureMap
                         Domains</b> in <i>BMIDE</i>. This argument is used to specify which domain to be
                         used from the <i>datamapping.xml</i> file. If the value is not provided, the default
                         is assumed to be <b>CAE</b>.
             
        :return: . Any failures in creation of the output item or
             relationships are also returned as a part of the activity log.
        """
        ...
    def ExecuteStructureMap(self, RootIR: Teamcenter.Soa.Client.Model.Strong.ItemRevision, SnapshotFolder: Teamcenter.Soa.Client.Model.Strong.Snapshot, RevRule: Teamcenter.Soa.Client.Model.Strong.RevisionRule, VariantRule: Teamcenter.Soa.Client.Model.Strong.VariantRule, StructureMapIR: Teamcenter.Soa.Client.Model.Strong.StructureMapRevision) -> ExecuteRuleResponse2:
        """    
             This operation creates an output BOM structure given the root ItemRevision
             of the root BOMLine of an input BOM structure along with its RevisionRule
             and the VariantRule. A Snapshot folder of the input BOM structure along
             with the VariantRule can also be provided as an input. The output BOM structure
             is determined by a combination of XSLT-based Data Map and StructureMap
             rules executed against the input BOM structure. Data Map/StructureMap
             syntax is in compliance with the schema defined in tcsim_xslWithNode.xsd,
             located in TC_DATA.
             

Data Map rules define the mapping between an input item type and its resulting
             output item type. Data Map rules are defined for an entire site and are stored
             in the datamapping.xml file located in TC_DATA. The name of the data
             mapping file is defined by the site preference CAE_dataMapping_file.
             

StructureMap rules tailor the output BOM Structure. There are several rule
             types:
             

Filter - Removes input BOM lines (and their children) from Data
             Map evaluation.
             
Include - Inserts item revisions in either the input or output BOM
             structure as required.
             
Reuse - Retrieve existing item revision to be used in the output
             structure.
             
Create Collector - Reorganization rule that creates "container" item
             revisions to move BOMLine objects and sub-assemblies around.
             
Move to Collector - Reorganizational rule that moves BOMLine
             objects and sub-assemblies to collector components.
             
Collapse Single Component Assembly - Identifying sub-assemblies with
             single child component, elevating the child component to the parent sub-assembly
             and removing the parent sub-assembly.
             
Remove Empty Assembly - Identifying sub-assemblies with no child
             components and removing the empty sub-assembly.
             
Skip - Skips the BOMLine but still process its children.
             



StructureMap rules are stored an XML named reference in CAEStructureMap
             dataset attached to a StructureMapRevision. StructureMap rules are
             created with Simulation Process Management CAE Structure Designer.
             

             To use this operation, a well-defined datamapping.xml is required in TC_DATA
             and a StructureMapRevision with an attached CAEStructureMap dataset
             must exist and the user should have either a simulation_author or rtt_author
license.
             

Use Cases:

             Use Case 1:
             
             Given an input root BOMLine of a BOM structure, along with its RevisionRule
             and VariantRule, the user can apply a StructureMap rule to the BOM
             structure and generate a corresponding output BOM structure. The output BOM structure
             would consist of BOMLine occurrences of ItemRevision objects as defined
             in the datamapping.xml file and would be organized by the StructureMap
             rules defined in the CAEStructureMap dataset attached to the StructureMapRevision.
             The user can review the actions executed with the process log returned with the BOMViewRevision.
             An email notification containing the activity log would be sent to the current user
             if the session option for email notification is set to true.
             

             Use Case 2:
             
             Given a Snapshot folder of the input BOM structure and its VariantRule,
             the user can apply a StructureMap rule to the BOM structure and generate a
             corresponding output BOM structure. The output BOM structure would consist of BOMLine
             occurrences of ItemRevision objects as defined in the datamapping.xml
             file and would be organized by the StructureMap rules defined in the CAEStructureMap
             dataset attached to the StructureMapRevision. The user can review the actions
             executed with the process log returned with the BOMViewRevision. An email
             notification containing the activity log would be sent to the current user if the
             session option for email notification is set to true.
             


Teamcenter Component:

             CAE Integrations - Provides custom extensions to the Tc data model to capture the
             CAE data model; the services that provide behaviors that are specific to CAE clients
             and the client side code that accesses the data model and services.
             
        :param RootIR: 
                         The <b>ItemRevision</b> of the root item of the input structure. This can be null
                         if the <i>snapshotFolder</i> is provided as input to the operation. If the <i>rootIR</i>
                         is not null and <i>snapshotFolder</i> is also provided as an input, then <i>rootIR</i>
                         input will be ignored and <i>snapshotFolder</i> will take precedence.
             
        :param SnapshotFolder: 
                         The <b>Snapshot</b> folder of the input structure. The <i>snapshotFolder</i> can
                         be null if the root <i>rootIR</i> is used as an input to the operation. The <i>snapshotFolder</i>
                         takes precedence over the <i>rootIR</i>.
             
        :param RevRule: 
                         The <b>RevisionRule</b> of the input structure. This is an optional parameter and
                         can be provided if the root <b>ItemRevision</b> is used as an input to the operation.
                         This parameter will be ignored if <i>snapshotFolder</i> is used as an input.
             
        :param VariantRule: 
                         The <b>VariantRule</b> for the input structure. This can be provided for both, the
                         <i>rootIR</i> or <i>snapshotFolder</i> as input. This is an optional parameter and
                         can be null.
             
        :param StructureMapIR: 
                         The <b>StructureMapRevision</b> containing a <b>CAEStructureMap</b> <i>Dataset</i>
                         with an XML <i>named reference</i> containing valid <i>StructureMap rules</i>.
             
        :return: . Any failures in creation of the output item or
             relationships are also returned as a part of the activity log.
        """
        ...

