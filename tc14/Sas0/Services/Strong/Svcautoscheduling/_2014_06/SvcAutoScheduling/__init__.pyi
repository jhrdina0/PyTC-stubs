import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class RelatedDiscrepancies:
    """
    List of ServiceDiscrepancy object related to PhysicalPart
    """
    def __init__(self, ) -> None: ...
    Discrepancies: list[Teamcenter.Soa.Client.Model.Strong.ServiceDiscrepancy]
    """
            A list of ServiceDiscrepancy objects related to the AsMaintainedBOMLine
            for PhysicalPart
"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial Errors are returned in the ServiceData"""

class RelatedServicePlan:
    """
    
            Contains information related to each SSP0ServicePlan which are retrived by
            identifyServicePlans operation.
            
    """
    def __init__(self, ) -> None: ...
    ServicePlan: Teamcenter.Soa.Client.Model.Strong.Item
    """The SSP0ServicePlan which is attached to Part"""
    TopPartitionLine: Teamcenter.Soa.Client.Model.Strong.BOMLine
    """Top BOMLine of the BOMWindow created for SSF0ServicePlan"""
    Asset: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """This is the PhysicalPartRevision for which the ServicePlan is returned."""
    UsageName: str
    """This is the usage name of the asset for which the ServicePlan is returned."""

class RelatedServicePlans:
    """
    Contains list of SSP0ServicePlan which are returned by operation identifyServicePlans.
    """
    def __init__(self, ) -> None: ...
    RelatedServicePlan: list[RelatedServicePlan]
    """A list of SSP0ServicePlan objects related to a Part"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial Errors are returned in the ServiceData."""

class RequirementInformation:
    """
    All the information related to ServiceRequirement.
    """
    def __init__(self, ) -> None: ...
    ServReqRev: Teamcenter.Soa.Client.Model.Strong.ItemRevision
    """SSP0ServiceReq used to generate the Schedule"""
    StructureContext: Teamcenter.Soa.Client.Model.Strong.StructureContext
    """StructureContext by which the SSP0ServiceReq is configured"""
    ServicePlan: Teamcenter.Soa.Client.Model.Strong.Item
    """SSP0ServicePlan of the SSP0ServiceReq"""
    Asset: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision
    """This is the PhysicalPartRevision for which the ServicePlan is returned."""
    UsageName: str
    """
            Contains information related to each SSP0ServicePlan which are retrived by
            identifyServicePlans operation.
            """

class SvcAutoScheduling:
    """
    Interface SvcAutoScheduling
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def IdentifyDiscrepancies(self, SelectedAsmBomLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine) -> RelatedDiscrepancies:
        """    
             This operation returns the ServiceDiscrepancy  objects which are related to
             a PhysicalPart by InProgress relation. The PhysicalPart is retrieved
             from the input AsMaintainedBOMLine. The operation also returns ServiceDiscrepancy
             objects which are related to child lines of given AsMaintainedBOMLine.
             

Use Cases:

             Use Case 1
             

             When an As Maintained BOM structure is loaded into the Service Editor view you can
             select a line and right mouse button click to show the options menu.  Select New->Generate
             Automated Service Schedule and the Generate Automated Schedule dialog is opened.
             There are 3 tabs, Service Plan, Service Discrepancy and Maintenance Action.  The
             Service Discrepancy tab has a Show Discrepancies button.  Clicking on the button
             will populate the Service Discrepancies table using the As Maintained BOM line that
             was selected to launch the dialog.
             


Teamcenter Component:

             Service Automated Scheduling - Teamcenter component which provides functionality
             to populate service schedule from service plan automatically.
             
        :param SelectedAsmBomLine: 
                         The <b>AsMaintainedBOMLine</b> for which <b>ServiceDiscrepancy</b> objects needs
                         to be retrived.
             
        :return: 
        """
        ...
    def IdentifyServicePlans(self, SelectedAsmLine: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine) -> RelatedServicePlans:
        """    
             This operation returns all of the SSP0ServicePlan objects which are related
             to a Part by the SSP0PlanForNeturalProduct relation. The operation
             traverses the complete AsMaintained structure from the selected AsMaintainedBOMLine
             and gets the PhysicalPart for each AsMaintainedBOMLine in the structure.
             From the PhyscialPart objects, the operation gets the Part objects
             from which the PhysicalPart objects were generated using the PhysicalRealization
             relation. It then uses the Part objects to get the SSP0ServicePlan objects.
             
             The operation also creates BOMWindows for each resulted SSF0ServicePlan.
             The operation returns the top line for the generated BOMWindow. This BOMLine
             is directly used in Client to display a complete SSF0ServicePlan structure.
             


Use Cases:

             Use Case 1
             

             When an As Maintained BOM structure is loaded into the Service Editor view you can
             select a line and right mouse button click to show the options menu.  Select New->Generate
             Automated Service Schedule and the Generate Automated Schedule dialog is opened.
             There are 3 tabs, Service Plan, Service Discrepancy and Maintenance Action.  Each
             tab has a Show Service Plan(s) button.  Clicking on the Show Service Plan(s) button
             will populate the Service Plans table using the As Maintained BOM Line that was selected
             to launch the dialog.
             


Teamcenter Component:

             Service Automated Scheduling - Teamcenter component which provides functionality
             to populate service schedule from service plan automatically.
             
        :param SelectedAsmLine: 
                         The AsMaintainedBOMLine for which SSF0ServicePlan needs to be retrived
             
        :return: 
        """
        ...
    def PopulateServiceSchedule(self, RequirementInfo: list[RequirementInformation], DiscrepancyList: list[Teamcenter.Soa.Client.Model.Strong.ServiceDiscrepancy], MaList: list[Teamcenter.Soa.Client.Model.Strong.ServiceActivity], WorkOrder: Teamcenter.Soa.Client.Model.Strong.Item, SelectedPhyPartRev: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision, TopPhyPartRev: Teamcenter.Soa.Client.Model.Strong.PhysicalPartRevision, IsRegenerate: bool, RunInBackground: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates  a physical entity from a neutral entity. The SSP0ServicePlan
             and its SSP0ServiceReq, SSP0WorkCard, and MEActivity objects
             are considered as the neutral entity. SSS0SvcWorkOrder and its Schedule,
             SSS0JobCards, and SSS0JobTask objects are considered as the physical
             entity. The operation reads the neutral entity and creates the equivalent physical
             entity. For example SSP0WorkCard will be mapped to SSS0JobCards, MEActivity
             will be mapped to SSS0JobTask etc.
             

             The starting point for process of creating the physical entity (populate Service
             Schedule) is SSP0ServiceReq. The SSP0ServiceReq objects required to
             populate the Schedule can be passed directly or they can be retrieved from
             ServiceDiscrepancy or SSF0MaintenanceAction objects.
             
             The operation reads the SSP0ServiceReq and populates the Schedule with information
             like SSP0Skill, CharacteristicsDefinition, and Dataset etc.
             

             The operation gets the Schedule from the SSS0SvcWorkOrder passed in
             as input parameter.
             

             Also this operation supports regeneration of Schedule objects. If the isRegenerate
             variable is passed as TRUE the operation reads the SSF0MaintenanceAction,
             gets the SSS0JobCard objects from the Schedule, deletes them and repopulates
             the Schedule with new SSS0JobCard objects.
             

Use Cases:

             Use Case 1 - Generate Service Schedule
             

             When one or more Service Requirements are check box selected from the Service Plans
             table in the Generate Maintenance Schedule dialog and the Generate Schedule button
             is clicked the system will generate a Maintenance Schedule for the selected Service
             Requirements.
             

             Use Case 2 - Regenerate Maintenance Actions
             

             When one or more Maintenance Actions are check box selected from the Maintenance
             Actions table in the Generate Maintenance Schedule dialog and the Regenerate button
             is clicked the system will regenerate the Schedule and Job
             

Teamcenter Component:

             Service Automated Scheduling - Teamcenter component which provides functionality
             to populate service schedule from service plan automatically.
             
        :param RequirementInfo: 
                         A list of <b>SSP0ServiceReq</b> information from which <b>Schedule</b> needs to be
                         created
             
        :param DiscrepancyList: 
                         A list of <b>ServcieDiscrepancy</b> objects from which <b>Schedule</b> needs to be
                         created
             
        :param MaList: 
                         A list of <b>SSF0MaintenanceAction</b> objects from which <b>Schedule</b> needs to
                         be created
             
        :param WorkOrder: 
                         The <b>SSS0SvcWorkOrder</b> from which the <b>Schedule</b> is retrived to populate.
             
        :param SelectedPhyPartRev: 
                         The <b>PhysicalPartRevision</b> that in context of which the <b>Schedule</b> needs
                         to be populated
             
        :param TopPhyPartRev: 
                         The top <b>PhysicalPartRevision</b> for the selected <b>PhysicalPartRevision</b>

        :param IsRegenerate: 
                         This variable is used to identify whether the operation is supposed to be treated
                         as a regenerate or normal populate Schedule action
             
        :param RunInBackground: 
                         Indicates whether populateSchedule needs to be run in background ( asynchronously
                         ) or not.
             
        :return: 
        """
        ...

