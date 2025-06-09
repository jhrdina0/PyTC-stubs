import System
import System.Collections
import Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink
import Teamcenter.Services.Strong.Structuremanagement._2008_03.Composition
import Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure
import Teamcenter.Services.Strong.Structuremanagement._2008_12.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2010_04.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure
import Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure
import Teamcenter.Services.Strong.Structuremanagement._2012_02.IncrementalChange
import Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate
import Teamcenter.Services.Strong.Structuremanagement._2012_09.Structure
import Teamcenter.Services.Strong.Structuremanagement._2012_09.VariantManagement
import Teamcenter.Services.Strong.Structuremanagement._2012_10.Structure
import Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2013_05.IncrementalChange
import Teamcenter.Services.Strong.Structuremanagement._2013_05.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement
import Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureFilterWithExpand
import Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate
import Teamcenter.Services.Strong.Structuremanagement._2014_10.Structure
import Teamcenter.Services.Strong.Structuremanagement._2014_12.Effectivity
import Teamcenter.Services.Strong.Structuremanagement._2014_12.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2015_10.Effectivity
import Teamcenter.Services.Strong.Structuremanagement._2016_05.StructureVerification
import Teamcenter.Services.Strong.Structuremanagement._2016_09.PublishByLink
import Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2018_11.Structure
import Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement
import Teamcenter.Services.Strong.Structuremanagement._2021_06.Effectivity
import Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2021_12.StructureSearch
import Teamcenter.Services.Strong.Structuremanagement._2022_06.RevisionRuleAdministration
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class CompositionRestBindingStub(CompositionService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AssignChildLines(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2008_03.Composition.AssignChildLinesParameter]) -> Teamcenter.Services.Strong.Structuremanagement._2008_03.Composition.AssignChildLinesResponse: ...

class CompositionService:
    """
    
            Contains Composition Services

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> CompositionService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AssignChildLines(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2008_03.Composition.AssignChildLinesParameter]) -> Teamcenter.Services.Strong.Structuremanagement._2008_03.Composition.AssignChildLinesResponse:
        """    Assign lines from one or more parent to a new parent line.
        :param Input: 
                         BomLines to be assigned from one or more parent  to new parent line
             
        :return: including newLines, lines without predecessors and exceptions.
        """
        ...

class EffectivityRestBindingStub(EffectivityService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateOccurrenceEffectivities(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_12.Effectivity.CreateOccEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateReleaseStatusEffectivity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_12.Effectivity.ReleaseStatusEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def EditOccurrenceEffectivity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2015_10.Effectivity.EditOccEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def EditReleaseStatusEffectivity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2015_10.Effectivity.EditRelStatusEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveOccurrenceEffectivities(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2015_10.Effectivity.RemoveOccEffectivitiesInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveReleaseStatusEffectivity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2015_10.Effectivity.RemoveRelStatusEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetEffectivities(self, InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Structuremanagement._2021_06.Effectivity.GetEffectivitiesResponse: ...

class EffectivityService:
    """
    
            This service provides all the operations required to manage
effectivities.

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> EffectivityService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateOccurrenceEffectivities(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_12.Effectivity.CreateOccEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates a new effectivity object for each BOMLine  in the list.
             If the isShared flag is true the operation applies same effectivity for all BOMLine
             in the list.
             

Use Cases:


User can create and associate the effectivity with one occurrence
             by selecting appropriate line in the structure and choosing Tools->Effectivity->Occurrence
             Effectivity->View,Create and Edit.

User can create and associate the effectivity with several occurrences
             by selecting appropriate lines in the structure and choosing Tools->Effectivity->Occurrence
             Effectivity->Create on Multiple BOM Lines, ensure the Use shared effectivity
             check box is cleared so the effectivity is not shared between BOMLines.
             
User can create and associate the same effectivity with several occurrences
             by selecting appropriate lines in the structure and choosing Tools->Effectivity->Occurrence
             Effectivity->Create on Multiple BOM Lines, ensure the Use shared effectivity
             check box is checked so the effectivity can be shared among all occurrences.
             



Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The information required to create occurrence effectivity for a list of <b>BOMLine</b>

        :return: 37062   Effectivity with unit range cannot have null end item.
        """
        ...
    def CreateReleaseStatusEffectivity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_12.Effectivity.ReleaseStatusEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation sets new effectivity on a release status.
             

Use Cases:

             User can configure a release status by choosing Tools->Effectivity->Revision Effectivity,
             then in the Effectivity dialog, select the corresponding release status and click
             create. Define Unit/Date range to set effectivity on the release status.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         Information required to create effectivity on a release status
             
        :return: 
        """
        ...
    def EditOccurrenceEffectivity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2015_10.Effectivity.EditOccEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates effectivity object for the specified BOMLine.
             

Use Cases:

             User can configure a release status by choosing Tools->Effectivity->Revision Effectivity,
             then in the Effectivity dialog, select the corresponding release status and click
             create. Define Unit/Date range to set effectivity on the release status.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The information required to update occurrence effectivity for the  <b>BOMLine</b>

        :return: 
        """
        ...
    def EditReleaseStatusEffectivity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2015_10.Effectivity.EditRelStatusEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation updates effectivity object for the specified released status.
             

Use Cases:


User can edit a release status by choosing Views->Effectivity->Revision
             Effectivity, then in the Revision Effectivity dialog box, select the corresponding
             release status effectivity and click Edit. Modify Unit/Date range to update effectivity
             on the release status.
             
User can also edit release status effectivity in My Teamcenter. Double-click
             the item status and change the displayed value.
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The information required to update effectivity on a released status
             
        :return: 
        """
        ...
    def RemoveOccurrenceEffectivities(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2015_10.Effectivity.RemoveOccEffectivitiesInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes effectivity objects from the specified BOMLine objects.
             

Use Cases:

             User can remove an occurrence effectivity by choosing Tools->Effectivity->Occurrence
             Effectivity, then in the Occurrence Effectivity dialog box, click Remove to clear
             all boxes. Click OK and Teamcenter removes the effectivity object from the selected
             occurrence. Any other occurrences sharing this effectivity retain their references
             to the effectivity object.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The information required to remove a list of <b>Effectivity</b> objects from specified
                         <b>BOMLine</b>

        :return: 
        """
        ...
    def RemoveReleaseStatusEffectivity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2015_10.Effectivity.RemoveRelStatusEffectivityInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes effectivity object from the specified released status.
             

Use Cases:

             User can remove a release status effectivity by choosing Views->Effectivity->Revision
             Effectivity, then in the Effectivity dialog, select the corresponding release status
             and click Delete.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The information required to remove <b>Effectivity</b> from a released status
             
        :return: 
        """
        ...
    def GetEffectivities(self, InputObjects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Services.Strong.Structuremanagement._2021_06.Effectivity.GetEffectivitiesResponse: ...

class IncrementalChangeRestBindingStub(IncrementalChangeService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CarryOver(self, BomLineInfos: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.IncrementalChange.BomLineInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def RemoveIncrementalChanges(self, ListOfObjects: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.IncrementalChange.ObjectsICEInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class IncrementalChangeService:
    """
    
            The IncrementalChange service exposes operations that are used to
track structure
            changes to a component such as addition or removal of components,
changes to attachments
            (data), changes on the occurrence attribute,  predecessor changes,
carries the IncrementalChangeElement
            (ICE) object or deletes the list of Incremental Change Elements
(ICE).

            This method of change control allows several independent structure
changes to be
            made concurrently, including the addition or removal of unrelated
components. Those
            changes can be implemented in any sequence. This method of change
control is suitable
            for large, flat structures without nested subassemblies or
components.

            To enable incremental changes, the Teamcenter administrator must set
the Incremental_Change_Management
            preference to true.

            This service provides following use cases:

Retrieves changes on datasets, forms etc under IncrementalChange
            (IC) context.

Retrieves changes on the occurrence attribute under IC.

Retrieves predecessor changes under IC.

Fnd0EnableIceCarryOver: Defines item types of the source and destination
            parent BOM line under which ICEs should be copied while copying.

Removes individual incremental changes.

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> IncrementalChangeService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CarryOver(self, BomLineInfos: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.IncrementalChange.BomLineInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation carries the IncrementalChangeElement (ICE) object(s) from the
             source line to the corresponding target line by cloning them.
             
             There are two BMIDE constants that were introduced for this functionality
             

             Type Constant Fnd0EnableIceCarryOver

             Property Constant Fnd0AttrIcesToExclude


             - New IncrementalChangeElement object(s) are attached to the original incremental
             change revision.
             

             - Add changes on the occurrence are ignored - It does not make sense to have two
             occurrences appearing at the same time at different locations.


             - GDELine objects are not supported.
             

             - For attribute changes the context of the absolute occurrence data is the new parent
             BOMView Revision.
             

             - If there is no write access on incremental change revision, the carryover is allowed
             with a programmatic bypass.
             
             - If there is any failure while cloning any IncrementalChangeElement object
             that is being carried over, the entire operation will rollback.
             

             - Carryover is not possible if we have the following two conditions:
             

Both source and target BomView Revision item type are not
             available in the BMIDE Type Constant Fnd0EnableIceCarryOver.
             
BOM-BOP case - If the source line is a BOMLine and the target
             line is a BOP (Bill of Process) line or vice versa
             



Use Cases:

             User wants to carry over IncrementalChangeElement object(s) when doing a Copy-Paste
             or a Cut-Paste of a BOMLine having IncrementalChangeElement object(s),
             from one structure partition to another partition within the Plant BOP.
             
             User wants to carry over IncrementalChangeElement object(s) when doing a Copy-Paste
             or a Cut-Paste of a BOMLine having IncrementalChangeElement object(s),
             from Product BOP and to another partition in the Plant BOP.
             



Teamcenter Component:

             Incremental Change - An incremental change collects a number of structure changes
             to a component such as add or remove of components or changes to attachments (data).
             Incremental change is an alternative to revision-based effectivity configuration.
             
        :param BomLineInfos: 
                         A list of source and their corresponding target <b>BOMLine</b> objects
             
        :return: 
        """
        ...
    def RemoveIncrementalChanges(self, ListOfObjects: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.IncrementalChange.ObjectsICEInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes the list of Incremental Change Elements (ICE) on the given
             BOMLine or the MECfgLine.
             

Teamcenter Component:

             Incremental Change - An incremental change collects a number of structure changes
             to a component such as add or remove of components or changes to attachments (data).
             Incremental change is an alternative to revision-based effectivity configuration.
             
        :param ListOfObjects: 
                         A list of BOMLine or the MECfgLine component and their corresponding ICE.
             
        :return: For successfully deleted ICEs, corresponding business object will be sent back in
             the ServiceData lists of updated object. If an invalid business object is detected,
             72035 is returned as a partial error with the corresponding business object. If an
             ICE does not affect the corresponding BOMLine, 46000 is returned as a partial error.
             Similarly, if an ICE does not affect the corresponding MECfgLine, 200165 is returned
             as a partial error.
        """
        ...

class MassUpdateRestBindingStub(MassUpdateService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def MassGetAffectedParents(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateAffectedInput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateAffectedResponse: ...
    def MassUpdateExecutionECR(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateExecuteECRinput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateExecuteECRresponse: ...
    def MassUpdateExecutionECN(self, ChangeItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateExecuteECNresponse: ...
    def ExecuteMarkupChanges(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ExecuteMarkupChangeInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ExecuteMarkupChangeResponse: ...
    def ExpandOneLevel(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ExpandOneLevelSearchScopeInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ExpandOneLevelSearchScopeResponse: ...
    def GetImpactedObjectDetails(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ImpactedObjectDetailsInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ImpactedObjectDetailsResponse: ...
    def GetImpactedObjects(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ImpactedObjectsQueryInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ImpactedObjectsQueryResponse: ...
    def GetRevisionRules(self, Operation: int) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.GetRevisionRulesResponse: ...
    def ManageImpactedObjectUpdates(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ManageImpactedObjectUpdateInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ManageImpactedObjectUpdatesResponse: ...
    def UpdateImpactedObjects(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectInput], UpdateRequestId: str) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectResponse: ...
    def UpdateImpactedObjectsEnd(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectEndResponse: ...
    def UpdateImpactedObjectsStart(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectStartResponse: ...
    def GetMarkupChangesForUpdate(self, Input: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.GetMarkupChangesForUpdateResponse: ...
    def ValidateChangeObjectForMassUpdate(self, Input: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], MassUpdateType: str) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ValidateChangeObjectForMassUpdateResponse: ...

class MassUpdateService:
    """
    
            Mass Update is a feature that automates the updating of multiple
assemblies
            at one time with a single process or two phase Change Request/Change
Notice
            processes.  Mass Update will track and manage all impacted
structures when performing
            a Mass Replace (Add or Remove).

Mass Update One-Time Processing

Identify common component to use for query impact assemblies using
            operation getImpactedObjects

Query for impacted assemblies

Identify which impacted assemblies to update

Identify which operation type to use (Replace, Add or Remove)

If replace or add need to identify replacing or adding part

Set Execution Mode to "1" one time process

Execute Update using operation massUpdateExecutionECR

Two Phase (ECR/ECN change compliant processes)

Create Change Request object

Identify common component to use for query impact assemblies using
            operation getImpactedObjects

Query for impacted assemblies

Identify Change Request object to be used

Identify which impacted assemblies to update

Identify which operation type to use (Replace, Add or Remove).If
            Replace or Add needed then identify replacing or adding part

Set Execution Mode to "2" add mass update entry to Change Request
            object

Add update information to Change Request Revision using operation
            massUpdatExecutionECR

Derive Change Notice object from Change Request object

Execute Update on ECN object using operation massUpdateExecutionECN

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> MassUpdateService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def MassGetAffectedParents(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateAffectedInput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateAffectedResponse:
        """    
             This operation will call ITK PS__masschange_get_parents to get all the affected impacted
             parent parts and there selectablility for mass update.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         The input is a vector of MassUpdateAffectedInput structures.
             
        :return: The results of the ITK PS__masschange_get_parents are returned by this SOA operation.
        """
        ...
    def MassUpdateExecutionECR(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateExecuteECRinput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateExecuteECRresponse:
        """    
             This operation will call one of three ITKs: execute mode=1 calls PS__PS__masschange_onetime,
             execute mode=2 calls PS__masschange_authorize_add and execute mode=3 calls PS__masschange_authorize_remove.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         This is a vector of MassUpdateExecuteECRinput structures.
             
        :return: The results from the three ITKs PS__PS__masschange_onetime, PS__masschange_authorize_add
             and PS__masschange_authorize_remove is return.
        """
        ...
    def MassUpdateExecutionECN(self, ChangeItemRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.MassUpdate.MassUpdateExecuteECNresponse:
        """    
             This operation will call ITK PS__masschange_execute which will process all the change
             item revision markup changes recorded during the ECR CM process.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param ChangeItemRevs: 
                         A vector of mass update change item revisions to be executed during the ECN CM process.
             
        :return: The results of the ITK PS__masschange_execute will be return.
        """
        ...
    def ExecuteMarkupChanges(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ExecuteMarkupChangeInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ExecuteMarkupChangeResponse:
        """    
             This operation executes the markup change objects corresponding to input Fnd0MarkupChange
             object UID list. Each markup change object holds the information like object to be
             modified, the input required for object modification and type of modification. When
             markup change object is executed, it modifies the required object with the help of
             information available on markup change object.
             

Use Cases:

             Execute markup changes associated with ChangeItemRevision


Invoke MassUpdate service operation getImpactedObjects by providing
             target ItemRevision. This API returns the list of impacted object UIDs.
             
Invoke MassUpdate service operation getImpactedObjectDetails by supplying
             the batch of impacted object UIDs. This API returns the information specifying whether
             each of the input impacted objects is modifiable or not.
             
Invoke MassUpdate service operation manageImpactedObjectUpdates providing
             the list of modifiable impacted objects and a ChangeItemRevision. This service
             operation when invoked with executionMode=murAddImpactedObjectToMarkup, adds the
             input impacted objects on the input ChangeItemRevision.
             
Invoke MassUpdate service operation getMarkupChangesForUpdate by
             providing a ChangeItemRevision as input. It returns the list of Fnd0MarkupChange
             object UIDs referenced by Fnd0Markup object associated with input ChangeItemRevision.
             
Invoke MassUpdate service operation  executeMarkupChanges in loop
             by providing a batch of Fnd0MarkupChange objects UIDs until all the Fnd0MarkupChange
             UIDs are processed for execution. Once all the batches are executed successfully
             then delete the Fnd0Markup object associated with input ChangeItemRevision.
             



Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         List of structure containing information about <b>ChangeItemRevision</b> and <b>Fnd0MarkupChange</b>
                         objects UIDs associated with it
             
        :return: 
        """
        ...
    def ExpandOneLevel(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ExpandOneLevelSearchScopeInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ExpandOneLevelSearchScopeResponse:
        """    
             This operation expands the given parent product structure node to fetch its immediate
             children. A call to this operation is made when defining a search scope for impacted
             object search.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         This is a structure information containing inputs required to expand the product
                         structure node to define the impacted object search scope.
             
        :return: 
        """
        ...
    def GetImpactedObjectDetails(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ImpactedObjectDetailsInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ImpactedObjectDetailsResponse:
        """    
             This operation gathers the impacted object details required to perform mass update.
             Details like whether the impacted object is selectable for performing an update,
             if not selectable then the reason for it being non-selectable, whether the impacted
             object is out of date etc. is returned as an output response.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Structure containing input information required to get impacted object details
             
        :return: 
        """
        ...
    def GetImpactedObjects(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ImpactedObjectsQueryInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ImpactedObjectsQueryResponse:
        """    
             This operation searches for product structure objects where  a given target ItemRevision
             is used.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Structure containing information to query impacted objects.
             
        :return: 
        """
        ...
    def GetRevisionRules(self, Operation: int) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.GetRevisionRulesResponse:
        """    
             This operation returns the list of valid revision rules applicable for specific mass
             update operation type.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Operation: 

        :return: 
        """
        ...
    def ManageImpactedObjectUpdates(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ManageImpactedObjectUpdateInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ManageImpactedObjectUpdatesResponse:
        """    
             This operation performs Add impacted object to or Remove impacted object from Change
             ItemRevision Markup as per the client request.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Structure containing information to manage impacted objects on change <b>ItemRevision</b>

        :return: 
        """
        ...
    def UpdateImpactedObjects(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectInput], UpdateRequestId: str) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectResponse:
        """    
             This operation performs an update on input impacted objects by replacing target ItemRevision
             with replacement ItemRevision.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Structure containing information required to perform mass update of impacted objects.
             
        :param UpdateRequestId: 
                         Unique Identifier per update request initiated from the 'Mass Update Realization'
                         wizard. If the update is being performed in batches then this Identifier is same
                         for all the batches.
             
        :return: 
        """
        ...
    def UpdateImpactedObjectsEnd(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectEndResponse:
        """    
             This operation performs the post update cleanup activity. This operation should be
             called only once after all the update batches are executed using 'updateImpactedObjects'.
             If all the update batches are executed successfully then this operation deletes the
             markup associated with input change ItemRevision.
             

Use Cases:


User wants to update the realizations saved on change ItemRevision.
             Operation 'getMarkupChangesForUpdate' is called by providing change ItemRevision
             as an input. This operation returns the Fnd0MarkupChange objects having information
             about impacted objects to be updated.
             
If the number of markup change objects is more than the update batch
             size then objects are updated in batches. Operation 'executeMarkupChanges' is then
             called per batch to update the batched markup change objects. This operation performs
             update on the impacted objects using information available on Fnd0MarkupChange
             objects.
             
Operation 'updateImpactedObjectsEnd' ends the update process and
             performs the cleanup activity if required. E.g. If the update is performed in context
             of change ItemRevision and if all the batches are executed successfully then
             this operation deletes the Fnd0Markup object associated with change ItemRevision
             in context of which the update has been performed.
             



Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Note: Out of all the member variables present in the input structure variable, only
                         'change' member variable is being used presently.Rest all the member variables are
                         kept for Future use.
             
        :return: 
        """
        ...
    def UpdateImpactedObjectsStart(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.UpdateImpactedObjectStartResponse:
        """    
             This operation builds the prerequisite information required to perform an update
             in batches. E.g. this operation generates an update request identifier that is used
             by all update batch requests. This operation should be called only once before calling
             the 'updateImpactedObjects' operation per batch.
             

Use Cases:


User wants to update the realizations (of a target ItemRevision)
             to a specific replacement ItemRevision. To do the update all impacted objects
             needs to be identified. Operation 'getImpactedObjects' is called by providing an
             input target ItemRevision as an input. This operation returns all the impacted
             objects.
             
Operation 'getImpactedObjectDetails' is then called by providing
             all the impacted objects as an input to check whether the impacted objects are modifiable
             or not.
             
User then selects the modifiable impacted objects to perform update
             upon them. If the number of selected impacted objects is more than the update batch
             size then impacted objects are updated in batches. Operation 'updateImpactedObjectsStart'
             starts the update process with some preprocessing. e.g. operation 'updateImpactedObjectsStart'
             builds the update request identifier that is common for all the subsequent update
             batch requests. Operation 'updateImpactedObjectsStart' should be called only once
             before calling the 'updateImpactedObjects' operation per batch
             
Operation 'updateImpactedObjects' is then called per batch to update
             the batched impacted objects. This operation updates the impacted objects as per
             the input replacement ItemRevision.
             



Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         Note: This input parameter is not being used presently. This parameter has been provided
                         for Future use case.
             
        :return: The update request identifier.
        """
        ...
    def GetMarkupChangesForUpdate(self, Input: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.GetMarkupChangesForUpdateResponse:
        """    
             This operation queries Fnd0MarkupChange objects referenced by Fnd0Markup
             object associated with input ChangeItemRevision and returns UIDs of the Fnd0MarkupChange
             objects to the client.
             

Use Cases:

             Execute markup changes associated with ChangeItemRevision object
             

Invoke MassUpdate service operation getImpactedObjects by providing
             target ItemRevision. This operation returns the list of impacted object UIDs.
             
Invoke MassUpdate service operaion getImpactedObjectDetails by supplying
             the batch of impacted object UIDs. This API returns the information specifying whether
             each of the input impacted objects is modifiable or not.
             
Invoke MassUpdate service operation manageImpactedObjectUpdates providing
             the list of modifiable impacted objects and a ChangeItemRevision. This API
             when invoked with executionMode=murAddImpactedObjectToMarkup, adds the input impacted
             objects on the input ChangeItemRevision.
             
Invoke MassUpdate service operation getMarkupChangesForUpdate by
             providing a ChangeItemRevision as input. It returns the list of Fnd0MarkupChange
             object UIDs referenced by Fnd0Markup object associated with input ChangeItemRevision.
             
Invoke MassUpdate service operation executeMarkupChanges in loop
             by providing a batch of Fnd0MarkupChange object UIDs until all the Fnd0MarkupChange
             UIDs are processed for execution.
             



Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         List of  <b>ChangeItemRevision</b>  objects to be executed for mass update operation
             
        :return: 
        """
        ...
    def ValidateChangeObjectForMassUpdate(self, Input: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision], MassUpdateType: str) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.MassUpdate.ValidateChangeObjectForMassUpdateResponse:
        """    
             This operation validates the input change ChangeItemRevision object for a
             given Mass Update type. When invoked with "massUpdate" as an input, it validates
             whether the input ChangeItemRevision is valid for 'Mass Update' action. When
             invoked with "massUpdateRealization" as an input, it validates whether the input
             ChangeItemRevision is valid for 'Mass Update Realization' action.
             

Use Cases:

             Select ChangeItemRevision and perform 'Mass Update' or 'Mass Update Realization'.
             Operation 'validateChangeObjectForMasUpdate' is invoked to validate whether the selected
             ChangeItemRevision is valid for the respective action 'Mass Update' or 'Mass
             Update Realization' initiated by the user.
             

Teamcenter Component:

             MassUpdate - Provides the ability to perform mass changes on multiple assemblies
             at one time, by using a single (non-workflow related) process or with a Change Management
             two phase CR orCN change process.
             
        :param Input: 
                         List of <b>ChangeItemRevision</b> objects to be validated for specified Mass Update
                         type
             
        :param MassUpdateType: 

        :return: 
        """
        ...

class PublishByLinkRestBindingStub(PublishByLinkService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def AddTargets(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.SourceAndTargets]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishLinksResponse: ...
    def CompletenessCheck(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.CompletenessCheckInputData]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.CompletenessCheckResponse: ...
    def CreateLinks(self, LinkInfos: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishLinkInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishLinksResponse: ...
    def FindLinesWithSameLogicalIdentity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LineAndWindow]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LogicallyEquivalentLinesResponse: ...
    def FindSourceInWindow(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LineAndWindow]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.FindSourceResponse: ...
    def FindTargetsInWindow(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LineAndWindow]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.FindTargetsResponse: ...
    def PublishData(self, PublishDataInfos: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishDataInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishLinksResponse: ...
    def DeleteLinkForSource(self, Sources: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteTargetsFromLink(self, Targets: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetSourceTopLevel(self, Targets: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.GetSourceTopLevelResponse: ...
    def DeleteLinksForSource2(self, SourceBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], DataToUnpublish: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def FindSourcesInWindow(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LineAndWindow]) -> Teamcenter.Services.Strong.Structuremanagement._2016_09.PublishByLink.FindSourcesResponse: ...

class PublishByLinkService:
    """
    
            Teamcenter offers CAD and BOM independence through which customer
can have separation
            of design and part related information so that both part and design
structures can
            evolve at different pace. It is desired to have association between
part and design
            structures through which user can link logically equivalent
occurrences. The PublishByLink
            feature allows user to perform in-context association of
occurrences.

            This service contains various operations to do in-context
association of occurrences
            and other subsequent operations like publishing geometry related
information from
            source (typically design) to target occurrence, find target/source
BOMLine
            objects, CompletenessCheck, delete PublishLink.

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> PublishByLinkService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def AddTargets(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.SourceAndTargets]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishLinksResponse:
        """    
             Adds AbsOccViewQualifier of target BOMLine objects to the existing
             PublishLink of input source BOMLine. The operation also saves updated
             PublishLink.
             

             Following validations are performed during operation and failures are reported in
             ServiceData.
             


PublishLink exists with source as input source and user has
             access to it.
             
Item type of source and target BOMLine as per PUBLISH_AlignableSourceTypes
             and PUBLISH_AlignableTargetTypes preference respectively.
             
No PublishLink exists with target as input target.
             
Logical identity of all target BOMLine is same.
             
Logical identity of source and target BOMLines is same.
             



Use Cases:

             Add in-context occurrence as target to an existing PublishLink for given source.
             

Dependencies:

             createLinks
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
<font face="courier" height="10">SourceAndTargets</font> containing source <b>BOMLine</b>
                         and corresponding target <b>BOMLine</b> objects.
             
        :return: 
        """
        ...
    def CompletenessCheck(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.CompletenessCheckInputData]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.CompletenessCheckResponse:
        """    
             Recursively evaluates completeness for BOMLine objects having underlying component
             as Part.  A BOMLine which requires positioned designed is marked as
             complete if underlying PartRevision has primary representation OR BOMLine
             has source associated via PublishLink object. If a BOMLine does not
             need positioned designed then such BOMLine is marked as complete as well.
             This operation also supports recursively clearing completeness results.
             

             If required the BOM is expanded internally. In case of packed BOMLines, if
             any of the BOMLine is incomplete then that packed line is marked as incomplete.
             


Use Cases:


Recursively perform completeness check for Part structure.
             
Recursively clears completeness check for Part structure.
             



Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
                         String representing action to be performed on corresponding <b>BOMLine</b>.
             
        :return: 
        """
        ...
    def CreateLinks(self, LinkInfos: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishLinkInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishLinksResponse:
        """    
             Creates PublishLink between AbsOccurrenceViewQualifier of source and
             target BOMLines. The dataFlags attribute
             of the PublishLink is set to 0 as no data was published. The operation also
             saves new PublishLink object.
             

             Following validations are performed during operation and failures are reported in
             ServiceData.
             


Item type of source and target BOMLine as per PUBLISH_AlignableSourceTypes
             and PUBLISH_AlignableTargetTypes preference respectively.
             
Type name is a valid TCType name.
             
PSBOMView of the source is local.
             
No PublishLink exists with source as input source.
             
No PublishLink exists with target as input target.
             



Use Cases:

             Perform in-context association between occurrences of two structures.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param LinkInfos: 
                         Contains information to create <b>PublishLink</b>.
             
        :return: 
        """
        ...
    def FindLinesWithSameLogicalIdentity(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LineAndWindow]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LogicallyEquivalentLinesResponse:
        """    
             Finds logically equivalent BOMLines in BOMWindow for list of input
             BOMLines.
             

BOMLines are said to be identical if their AbsoluteOccurrence objects
             have same Usage Address and Positioned Designator.
             

Use Cases:

             Find equivalent BOMLine objects and associate them.
             

Dependencies:

             createLinks
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
<font face="courier" height="10">LineAndWindow</font> containing <b>BOMLine</b> for
                         which equivalent <b>BOMLine</b>s to be searched in corresponding input <b>BOMWindow</b>.
             
        :return: 
        """
        ...
    def FindSourceInWindow(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LineAndWindow]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.FindSourceResponse:
        """    
             Finds source of the PublishLink in source BOMWindow for input target
             BOMLine objects. Source is returned as BOMLine.
             


Use Cases:

             Determine if BOMWindow has source for input target BOMLine objects.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
<font face="courier" height="10">LineAndWindow</font> containing target <b>BOMLine</b>
                         and <b>BOMWindow</b> in which source of <b>PublishLink</b> to search.
             
        :return: 
        """
        ...
    def FindTargetsInWindow(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LineAndWindow]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.FindTargetsResponse:
        """    
             Finds target of the PublishLink in target BOMWindow for input source
             BOMLine objects. Targets are returned as BOMLine objects.
             

Use Cases:


Determine if BOMWindow has targets for input source BOMLine.
             
Find targets for source of PublishLink and subsequently use
             found target BOMLine objects to delete links.
             



Dependencies:

             deleteTargetsFromLink
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
<font face="courier" height="10">LineAndWindow</font> containing source <b>BOMLine</b>
                         and <b>BOMWindow</b> in which target of <b>PublishLink</b> to search.
             
        :return: 43119 No Publish Link exists for the source.
        """
        ...
    def PublishData(self, PublishDataInfos: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishDataInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.PublishLinksResponse:
        """    
             Copies Absolute Transformation Matrix and/or
             JT from source BOMLine to target BOMLine objects. If a PublishLink
             does not exist for source and target then a new PublishLink is created with
             input dataFlags. In case if PublishLink already exists then dataFlags of the
             PublishLink object is updated.
             

             Input dataFlags is used to determine which
             data has to be copied. Unless context was explicitly set - the data on target BOMLines
             is stored in-context of top BOMLine of the target BOMWindow.
             

             The DirectModel Dataset is attached with Rendering relation. If the target
             BOMLine is an assembly then PLMXML file is created based on RevisionRule
             of the source BOMWindow and attached to target BOMLine as Text
Dataset with Rendering relation. In case, in-context Dataset with Rendering
             relation already exists then that is replaced with the new one. The BOMWindow
             is saved after attaching the Dataset.
             

             Below validations are performed during operation and failures are reported in ServiceData.
             


dataFlags contains a valid
             value.
             
Target BOMLine requires positioned design.
             
Item type of source and target BOMLine as per PUBLISH_AlignableSourceTypes
             and PUBLISH_AlignableTargetTypes preference respectively.
             
Type name is a valid TCType name.
             
PSBOMView of the source is local.
             
No PublishLink exists other than source and target as in input.
             



Use Cases:

             Perform in-context association between occurrences of two structures and copy Absolute Transformation Matrix and/or JT from source
             to target BOMLine objects.
             

Dependencies:

             createLinks
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param PublishDataInfos: 
<font face="courier" height="10">PublishDataInfo</font> containing information to
                         create <b>PublishLink</b> and <font face="courier" height="10">dataFlag</font> to
                         determine which attributes should be copied to target <b>BOMLine</b>s.
             
        :return: 
        """
        ...
    def DeleteLinkForSource(self, Sources: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Finds and deletes PublishLink for input source BOMLine objects.
             

Use Cases:

             Delete PublishLink.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Sources: 
                         Set of source <b>BOMLine</b> objects for which <b>PublishLink</b> to be deleted.
             
        :return: 43111 Invalid source as input.
        """
        ...
    def DeleteTargetsFromLink(self, Targets: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Deletes AbsOccViewQualifier of target BOMLines from the existing PublishLink.
             If the target being removed is the last one for PublishLink then PublishLink
             is also deleted. Otherwise operation saves updated PublishLink.
             

             Following validations are performed during operation.
             


             PublishLink exists whose target as input
             


Use Cases:

             Detach target BOMLine from PublishLink.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Targets: 
                         Target <b>BOMLine</b> objects which need to be removed from existing <b>PublishLink</b>.
             
        :return: 
        """
        ...
    def GetSourceTopLevel(self, Targets: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.GetSourceTopLevelResponse:
        """    
             Finds source of PublishLink for given target BOMLine. For the source
             of the PublishLink finds context PSBOMView.
             

Use Cases:

             Find context PSBOMView for the source of PublishLink.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Targets: 
<b>BOMLine</b>s for which source has to be found in order to determine context <b>PSBOMView</b>.
             
        :return: 43112 Invalid target as input.
        """
        ...
    def DeleteLinksForSource2(self, SourceBOMLines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], DataToUnpublish: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Finds and deletes PublishLink for input source BOMLine objects.
             

             The AbsOccXform of the target BOMLine objects will be deleted if dataToUnpublish is TRANSFORM. All in context JTs
             of the target BOMLine objects will be unattached if dataToUnpublish
             is SHAPE. If all data(as of now TRANSFORM and SHAPE only) needs to be removed then
             value of dataToUnpublish should be ALL. None
             of the published data will be impacted when dataToPublish
             is empty string.
             

Use Cases:

             Delete PublishLink and unpublish data from target BOMLine.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param SourceBOMLines: 
                         Source <b>BOMLine</b> objects for which  <b>PublishLink</b> to be deleted. The <b>PublishLink</b>
                         found is used to find target <b>BOMLine</b> objects before <b>PublishLink</b>s are
                         deleted.
             
        :param DataToUnpublish: 
                         Data to unpublish. Valid values are TRANSFORM, SHAPRE, ALL or empty string. The value
                         is case sensitive.
             
        :return: 43111 Invalid source as input.
        """
        ...
    def FindSourcesInWindow(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2007_06.PublishByLink.LineAndWindow]) -> Teamcenter.Services.Strong.Structuremanagement._2016_09.PublishByLink.FindSourcesResponse:
        """    
             Finds all source BOMLines objects of the PublishLink in source BOMWindow
             for input target BOMLine objects. All sources are returned as BOMLine
             objects.
             

Use Cases:

             Determine if BOMWindow has sources for input target BOMLine objects.
             

Teamcenter Component:

             Part BOM independence - Teamcenter offers CAD and BOM independence through which
             customer can have separation of design and part related information so that both
             part and design structures can evolve at different pace.
             
        :param Input: 
                         This containing target <b>BOMLine</b> and <b>BOMWindow</b> in which source of <b>PublishLink</b>
                         to search.
             
        :return: 46002 Invalid tag received by BOM Module.
        """
        ...

class RevisionRuleAdministrationRestBindingStub(RevisionRuleAdministrationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetAPSValidRevisionRules(self, InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject) -> Teamcenter.Services.Strong.Structuremanagement._2022_06.RevisionRuleAdministration.GetAPSValidRevisionRulesResponse: ...

class RevisionRuleAdministrationService:
    """
    
            The RevisionRuleAdministration service exposes operations that are
used to view,
            update, create or delete RevisionRule. Common uses for RevisionRule
include configuration
            of product structure, Collaborative Design, Product Configurator,
Search.

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> RevisionRuleAdministrationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetAPSValidRevisionRules(self, InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject) -> Teamcenter.Services.Strong.Structuremanagement._2022_06.RevisionRuleAdministration.GetAPSValidRevisionRulesResponse:
        """    
             Retrieves the Advanced PLM Services (APS) non-suppressed revision rules (RevisionRule)
             valid for the input WorkspaceObject.
             
             Common uses for RevisionRule include configuration of product structure, Collaborative
             Design, Product Configurator, Search. Examples of Rule Entries are: Latest Entry,
             Working Entry, Status Entry, and Override Entry.
             

Use Cases:

             Input:
             
                 {
             
                     inputObject = { Cfg0ProductItem }
             
                 }
             
                 
             
             Output:
             
             The output of the operation returns valid RevisionRule objects for the given
             configurator context input which can be used to configure the configurator data objects.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param InputObject: 
                         The input <b>WorkspaceObject</b>. The valid input types are: <b>Cfg0ConfContext</b>,
                         <b>Cfg0ProductItem</b>, <b>Item</b> and <b>Mdl0ModelElement</b>. The list of <b>RevisionRule</b>
                         objects will be valid and visible for this input object.
             
        :return: 
        """
        ...

class StructureFilterWithExpandRestBindingStub(StructureFilterWithExpandService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ExpandAndSearch(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], SearchConditions: list[Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureFilterWithExpand.SearchCondition]) -> Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureFilterWithExpand.ExpandAndSearchResponse: ...

class StructureFilterWithExpandService:
    """
    
            This service contains the operations for searching the BOMLines in a
collapsed
            structure. Search criteria is based on runtime properties.

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureFilterWithExpandService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ExpandAndSearch(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], SearchConditions: list[Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureFilterWithExpand.SearchCondition]) -> Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureFilterWithExpand.ExpandAndSearchResponse:
        """    
             This operation does a full expansion of the given lines, then performs the search
             on the expanded structure with the given search conditions. The lines of a structure
             and search criteria as BOMLine property value are required. This operation
             returns the result BOMLines with satisfied condition indexes.
             
             A user can search for BOMLine with multiple search criteria by separating
             those criteria with an "OR" operator. The output line contains the information
             about the search conditions in the form of indexes which are satisfied by a particular
             BOMLine.
             
             Logical operator for the first condition is ignored
             
             This service will support search criterias like "find no = 10 and quantity = 1
             or quantity = 20 and AbsOccId = CFG". In this criteria "AND" has precedence
             over "OR" operator.
             

             Comparison are done on the basis of BOMLine property type only.
             

Valid inputs for Date type property : A user must give input in a specific
             date format that is defined in timelocal.xml If the date format is not defined in
             timelocal.xml then default format will be considered as "dd-mmm-yyyy hh:mm"
             .
             
Example. "01-jan-2010 12:23"
             

             Invalid inputs for Date type property :    "01-jan-201012:23", "01-january-2010
             12:23", "32-jan-2010 12:23", "32-jan-20112 12:23"
             


Valid inputs for String values : A user must give a valid string for search
             it should not contain spaces until u meant to find a string with spaces. Leading
             and trailing spaces will be taken care.
             
Example: "validInput" , "validInput  ", "   validInput", "  validInput   "
             
             Invalid Input : "valid   Input"
             
Note: Since Comparison is done on the basis of BOMLine property type
             only. There are some integer and double type properties which is defined as string
             on BOMLine so you need to pass the exact value in that case that will be a
             string comparison.
             
Example : "010" and "10" will be considered as different values
             

Valid inputs for Boolean type property : only true and false is allowed. For
             those properties which is shown as Y and N in Rich Client you should pass
             the value as Y and N only.
             

Valid inputs for Double and Integer type property : A user must provide a
             valid value which could be parsed successfully to specified type.
             
Example : "12334" , "234.456", "007854", "0088.675"
             
Invalid Input : "345fg", "fr4567", "456.54er"
             

Note: 1) If a condition contains a invalid inputValue than comparison
             for that property will be skipped. Results will be returned for valid values only.
             
             2) Equal operator(=) will be used for wild card search by default. User must
             not pass a wild card character('*' or '?') in a string value. Search
             will be case insensitive for all relational operators except "==" operator.
             
             3) Only "AND" and "OR" logical operators are supported.
             
             4) For integer, double and Date types "=" and "==" operators have same
             behavior.
             


Use Cases:

             Search for BOMLine with their properties - A User can search for BOMLine in a collapsed
             structure by giving criteria as their property values like "bl_item_item_id = 000016"
             where bl_item_item_id is a property and 000016 is input value given by user for search.
             
Example1: A User searches for some BOMLines by giving the criteria "find
             no. =10 OR quantity > 1" and BOMLine1 satisfies the condition "find
             no. =10" and BOMLine2 satisfies the condition "quantity > 1" then
             the first output line will contain the BOMLine1 and search condition index
             as 0 and the second output line will contain the BOMLine2 and search condition
             index as 1.
             

Example2: A User searches for some BOMLines by giving the criteria
             "find no = 10 and quantity > 1 or Find No = 20 and quantity = 1" and BOMLine1
             satisfies the condition "find no = 10 and quantity > 1" and BOMLine2
             satisfies the condition "Find No = 20 and quantity = 1" then the first output
             line will contain the BOMLine1 and search condition index  as 0,1 and the
             second output line will contain the BOMLine2 and search condition index as
             

Teamcenter Component:

             BOM Expand - Set of core services that allow to efficiently solve a product structure
             based on revision rules; effectivities etc.
             
        :param Lines: 
                         The lines of a structure where search is to be performed.
             
        :param SearchConditions: 

        :return: 
        """
        ...

class StructureRestBindingStub(StructureService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def Duplicate(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateInputInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateResponse: ...
    def ExpandOrUpdateDuplicateItems(self, Infos: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsResponse: ...
    def ValidateStructureItemIds(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ValidateStructureItemIdsInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ValidateStructureItemIdsResponse: ...
    def Duplicate2(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure.DuplicateInputInfo2]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateResponse: ...
    def ExpandOrUpdateDuplicateItems2(self, OpInput: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsInfo], SelectionOption: int) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsResponse: ...
    def ValidateStructureItemIds2(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure.ValidateStructureItemIdsInfo2]) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure.ValidateStructureItemIdsResponse2: ...
    def PackOrUnpack(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Flag: int) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def Duplicate3(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.DuplicateInputInfo3]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateResponse: ...
    def ExpandOrUpdateDuplicateItems3(self, OpInput: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsInfo], SelectionOption: int) -> Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.ExpandOrUpdateDuplicateItemsResponse2: ...
    def ValidateStructureItemIds3(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.ValidateStructureItemIdsInfo3]) -> Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.ValidateStructureItemIdsResponse3: ...
    def SetClosureRuleVariablesAndValues(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, ClosureRuleName: str, ClosureRuleVariableInfos: list[Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.ClosureRuleVariableInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def UnloadBelow(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], UnloadType: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def Add(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.Structure.AddParam]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.Structure.AddResponse: ...
    def ValidateParentChildConditions(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.Structure.ParentChildPair]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ValidateOccurrenceConditions(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Flag: int) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CutItems(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_10.Structure.CutItemParam]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CloneStructure(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.Structure.CloneStructureInputInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.Structure.CloneStructureResponse: ...
    def CloneStructureExpandOrUpdate(self, OpInput: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.Structure.CloneStructureExpandOrUpdateItemsInfo], SelectionOption: int) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.Structure.CloneStructureExpandOrUpdateResponse: ...
    def ToggleOccurrenceSuppression(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def TogglePrecision(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def CreateInterchangeableGroups(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2018_11.Structure.CreateGroupInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class StructureSearchRestBindingStub(StructureSearchService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def StartSearch(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchScope, SearchExpression: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchExpressionSet) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse: ...
    @typing.overload
    def StartSearch(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchScope, SearchExpression: Teamcenter.Services.Strong.Structuremanagement._2010_04.StructureSearch.SearchExpressionSet) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse: ...
    @typing.overload
    def StartSearch(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchScope, SearchExpression: Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureSearch.SearchExpressionSet) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse: ...
    def NextSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse: ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse: ...
    def GetAssemblyBoundingBox(self, Items: list[Teamcenter.Soa.Client.Model.Strong.Item]) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureSearch.BoundingBoxInfoResponse: ...
    def IsSpatialDataAvailable(self, TopItem: Teamcenter.Soa.Client.Model.Strong.Item) -> bool: ...
    def GetStructureChanges(self, ChangeTrackerInput: list[Teamcenter.Services.Strong.Structuremanagement._2014_12.StructureSearch.ChangeTrackerInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_12.StructureSearch.StructureChangesResponse: ...
    def NextSearch2(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.StructureSearchResultResponse: ...
    def StartSearch2(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.SearchScope, SearchExpression: Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.SearchExpressionSet, ReturnLiteLines: bool) -> Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.StructureSearchResultResponse: ...
    def StopSearch2(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.StructureSearchResultResponse: ...
    def NextExpandBOMLines(self, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandResponse: ...
    def StartExpandBOMLines(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject], ExpandSettings: System.Collections.Hashtable, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions) -> Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandResponse: ...
    def StopExpandBOMLines(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def NextExpandBOMLines2(self, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2021_12.StructureSearch.ExpandResponse2: ...
    def StartExpandBOMLines2(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject], ExpandSettings: System.Collections.Hashtable, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions) -> Teamcenter.Services.Strong.Structuremanagement._2021_12.StructureSearch.ExpandResponse2: ...

class StructureSearchService:
    """
    
            Contains StructureSearch Services

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureSearchService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def StartSearch(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchScope, SearchExpression: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchExpressionSet) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse: ...
    @typing.overload
    def StartSearch(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchScope, SearchExpression: Teamcenter.Services.Strong.Structuremanagement._2010_04.StructureSearch.SearchExpressionSet) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse: ...
    @typing.overload
    def StartSearch(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.SearchScope, SearchExpression: Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureSearch.SearchExpressionSet) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse: ...
    def NextSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse:
        """    
             This operation gets the next set of search results, which was initialized by the
             startSearch operation. This operation returns
             the results in batches and needs to be called repeatedly until the flag for search
             complete is true in the response. Input to this operation is the search cursor object
             which was returned by the startSearch or
             a previous call to nexSearch operation.
             

Use Cases:

             A user wants to perform structure search within a particular scope. The user needs
             to select search criteria(s), from the supported list to create search expression
             and start search operation. Once the initial set of a search result is returned,
             this operation will be used to get the next set of search result.
             

Dependencies:

             startSearch
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchCursor: 
                         Search cursor identifies a search session which was started by calling <font face="courier" height="10">startSearch</font> operation. This object is returned from the <font face="courier" height="10">startSearch</font> or previous call to <font face="courier" height="10">nextSearch</font> operation. Same should be passed as input to current
                         operation.
             
        :return: 
        """
        ...
    def StopSearch(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureSearch.StructureSearchResultResponse:
        """    
             This operation stops the current search identified by the search cursor object. The
             input to the operation is the search cursor object which was returned by the startSearch or previous call to nextSearch operation.
             

Use Cases:

             A user wants to perform Cacheless search within a particular scope. The user needs
             to select  search criteria(s) from the supported list to create search expression
             and start search operation. Once the initial batch of search result is returned,
             this operation can be used to stop the search.
             

Dependencies:

             nextSearch, startSearch
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchCursor: 
<b>SearchCursor</b> holds the current state of the search session which was created
                         in the <font face="courier" height="10">startSearch</font> or <font face="courier" height="10">nextSearch</font> operation. This is used as a handle to identify this
                         search when executing the next step of the search or stopping the search.
             
        :return: A flag to indicate the search is complete and service data. This operation does not
             return any partial errors.
        """
        ...
    def GetAssemblyBoundingBox(self, Items: list[Teamcenter.Soa.Client.Model.Strong.Item]) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureSearch.BoundingBoxInfoResponse:
        """    
             This operation returns the bounding box for each Item.The bounding box returned
             is for all revisions of the Item. It represents the box for entire assembly.
             

Use Cases:

             A user wants to get the bounding box for the items selected.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Items: 
                         A list of <b>Items</b> whose bounding box information is expected in the response
             
        :return: 
        """
        ...
    def IsSpatialDataAvailable(self, TopItem: Teamcenter.Soa.Client.Model.Strong.Item) -> bool:
        """    
             This operation checks if the spatial data is available for the Item provided
             in input. If yes, it returns "true" otherwise it returns "false".
             

Use Cases:

             A user wants to check if spatial data is created for given Item which is pre-requiste
             for spatial search operation.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param TopItem: 
                         Specifies the top <b>Item</b> of the assembly for which user wants to find out whether
                         the spatial data exists or not.
             
        :return: else returns
             false. This operation does not return any partial error.
        """
        ...
    def GetStructureChanges(self, ChangeTrackerInput: list[Teamcenter.Services.Strong.Structuremanagement._2014_12.StructureSearch.ChangeTrackerInput]) -> Teamcenter.Services.Strong.Structuremanagement._2014_12.StructureSearch.StructureChangesResponse:
        """    
             This operation searches for delta changes in the structure based on different search
             criteria. The BOMLine objects directly or indirectly affected by changes done in
             Incremental Change context or revision effectivity context or occurrence effectivity
             context that are configured in are returned. The caller must supply the BOMLine object(s)
             that determines the scope for the search in addition to search parameters like intent,
             release status names, and one of unit range or date range. The lines returned are
             those that are configured by the current revision rule. All the BOMLines created/found
             will be returned as part of ServiceData along with incremental changes elements (
             in case of IncrementalChange context), or ItemRevisions ( in case of Revision
             effectivity/Occurrence effectivity). All partial errors are grouped by the index
             of the input vector. This operation should be consided when the scope will not yield
             too many expandlines lines below.
             

Use Cases:

             A user wants to find a set of incremental changes of a particular type and with a
             specific unit effectivity.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param ChangeTrackerInput: 
                         The type of change to be tracked ( <b>IncrementalChange</b>,   <b>RevisionEffectivity</b>,
                         or <b>OccurrenceEffectivity</b> or modified time) and the scoping BOMLine objects
                         and the selection criteria for Incremental Change elements ( only relevant when Incremental
                         Change context is specified ).
             
        :return: 
        """
        ...
    def NextSearch2(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.StructureSearchResultResponse:
        """    
             This operation gets the next set of search results, which was initialized by the
             startSearch2 operation. This operation returns the results in batches and needs to
             be called repeatedly until the flag for search complete is true in the response.
             Input to this operation is the search cursor object which was returned by the startSearch2
             or a previous call to nextSearch2 operation.
             

Use Cases:

             A user wants to perform structure search within a particular scope. The user needs
             to select search criteria(s), from the supported list to create search expression
             and start search operation. Once the initial set of a search result is returned,
             this operation will be used to get the next set of search result.
             

Dependencies:

             startSearch2
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchCursor: 
                         SearchCursor identifies a search session which was started by calling startSearch2
                         operation. This object is returned from the startSearch2 or previous call to nextSearch2
                         operation. Same should be passed as input to current operation.
             
        :return: 
        """
        ...
    def StartSearch2(self, Scope: Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.SearchScope, SearchExpression: Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.SearchExpressionSet, ReturnLiteLines: bool) -> Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.StructureSearchResultResponse:
        """    
             This operation initializes the structure search. The input to the operation is a
             search expression set and the scope to perform the search in.
             

Use Cases:

             A user wants to perform structure search within a particular scope. The user needs
             to select search criteria(s) from the supported list to create search expression
             and start search operation.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param Scope: 
                         The scope of the search.
             
        :param SearchExpression: 
                         The full set of search expressions that are used to perform a single structure search.
                         Each of the expressions provided are combined using a logical 'AND' operator.
             
        :param ReturnLiteLines: 
                         If true, <b>Fnd0BOMLineLite</b> are returned in response; otherwise, a normal <b>BOMLine</b>.
                         If scopeLines are of <b>Fnd0BOMLineLite</b> type, this flag should be true.
             
        :return: 
        """
        ...
    def StopSearch2(self, SearchCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2017_05.StructureSearch.StructureSearchResultResponse:
        """    
             This operation stops the current search identified by the search cursor object. The
             input to the operation is the search cursor object which was returned by the startSearch2
             or previous call to nextSearch2 operation.
             

Use Cases:

             A user wants to perform Cacheless search within a particular scope. The user needs
             to select search criteria(s) from the supported list to create search expression
             and start search operation. Once the initial batch of search result is returned,
             this operation can be used to stop the search.
             

Dependencies:

             nextSearch2, startSearch2
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param SearchCursor: 
<b>SearchCursor</b> holds the current state of the search session which was created
                         in the startSearch2 or nextSearch2 operation. This is used as a handle to identify
                         this search when executing the next step of the search or stopping the search.
             
        :return: to indicate the search is
             complete and service data. This operation does not return any partial errors.
        """
        ...
    def NextExpandBOMLines(self, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandResponse:
        """    
             This operation gets the next set of objects from a previously executed expansion
             result. The results returned are based on the pageSize specified in the input. This
             API returns the same response structure as that of startExpandBOMLines.
             

Use Cases:

             This API is used in conjunction with startExpandBOMLines operation. startExpandBOMLines
             operation is a prerequisite for invoking nextExpandBOMLines. The expand cursor returned
             by the startExpandBOMLines is used to call nextExpandBOMLines operation. This operation
             could be called repeatedly by the caller, until all the expansion results are returned.
             

Dependencies:

             startExpandBOMLines
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param PageSize: 
                         The number of objects to be returned by the call. The real number of returned may
                         vary, but it is smaller than pageSize. The value will override loadCount in ExpandCursor.
             
        :param ExpandOptions: 
                         Expand options for the operation.
             
        :param ExpandCursor: 
                         The SearchCursor object that keeps track of the expansion results and the corresponding
                         indexes as of where the caller has consumed the results.
             
        :return: 214556Â Â Â Â Â Â Â Â Invalid relation to get associated
             objects.
        """
        ...
    def StartExpandBOMLines(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject], ExpandSettings: System.Collections.Hashtable, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions) -> Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandResponse:
        """    
             This operation initiates a sequence of operations to expand BOMLine objects based
             on  filter information on BOMWindow and returns a list of BOMLine objects.
             Filter information could be a complex expression set that combines multiple simpler
             Expand terms in a logical sequence.
             
             Expansion is always executed within the scope of a BOMWindow under one or
             more BOMLine objects.
             
             The results of an expansion are returned one set at a time based on the pageSize.
             The ExpandResponse also contains a Cursor object that the caller uses to expand
             the next set of results by invoking the StructureManagement::StructureSearch::nextExpandBOMLines
             call.
             

Use Cases:

             1.    Expand all lines of a structure page by page by setting
             levels to 0 (expand all levels) and pageSize is 100. The operation will return the
             result breadth first.
             
             2.    Expand all lines of a structure by setting levels to 0
             (expand all levels) and pageSize is 0.
             
             3.    Expand all child lines of a list of lines by setting level
             to 1 and pageSize is 100.
             
             4.    Expand all child lines from the structure based on the
             given pageSize.
             
             The returned childlines may or may not contain specific datasets. For example, if
             dataset information is specified - dataset relation is IMAN_reference and
             dataset type is Text then the response will contain the specified datasets (if there
             are any).
             
             5.    Expand the child lines from the structure given the page
             size. The dataset information contains the minimum number of dataset objects to be
             returned. For example, dataset relation is given as IMAN_reference, dataset
             type is Text, expandRelatedObjects is 1 and min datasets to be returned is set to
             10. In this case, the response will contain only 10 specified datasets.
             
             6.     Expand the child lines from the structure given the page
             size. When dataset information specify the dataset relation and dataset type. In
             this case, the response will contain 0 datasets.
             
             7.    Expand the child lines defined by the Expand criteria (Expand
             criteria given in the BOM window) given the page size.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param BomLines: 
                         Input for executing the expansion.
             
        :param ExpandSettings: 
                         Â Â Â Â replay: List of stable IDs( Chain of clone stable ID from
                         TopBomline) on which replay to be performed.
             
        :param PageSize: 
                         Value: 0 means unlimited.
             
        :param ExpandOptions: 
                         Expand Options for the operation.
             
        :return: 214556Â Â Â Â Â Â Â Â Invalid relation to get associated
             objects.
        """
        ...
    def StopExpandBOMLines(self, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation stops further loading of objects from a previously executed expansion
             and clears all the memory allocated for the expansion operation. The expand cursor
             is deleted and the list of objects that are kept track by the expand cursor are removed
             from the server memory.
             
             The stopExpandBomlines does not unload any previously loaded objects. Also there
             is no locking or unlocking performed by the stopExpandBOMLines operation.
             

Use Cases:

             When an expansion is executed in structure and the expansion returns a large set
             of objects. The server process keeps the results of a expansion using a expand cursor
             object. At each nextExpandBOMLines operation, the results are further filtered and
             returned in batches specified by the load count. However, if the caller is not interested
             in consuming the expansion results further, then a stopExpandBOMLines could be called
             to release all the resources allocated for that expansion operation. This includes
             dropping the runtime expand cursor object and the list of lines kept track by the
             cursor. The cursor will be automatically deleted if it is exhausted.
             

Dependencies:

             nextExpandBOMLines, startExpandBOMLines
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param ExpandCursor: 
                         The SearchCursor for stopping the expansion.
             
        :return: 214556        Invalid cursor received.
        """
        ...
    def NextExpandBOMLines2(self, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions, ExpandCursor: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2021_12.StructureSearch.ExpandResponse2: ...
    def StartExpandBOMLines2(self, BomLines: list[Teamcenter.Soa.Client.Model.Strong.RuntimeBusinessObject], ExpandSettings: System.Collections.Hashtable, PageSize: int, ExpandOptions: Teamcenter.Services.Strong.Structuremanagement._2021_06.StructureSearch.ExpandOptions) -> Teamcenter.Services.Strong.Structuremanagement._2021_12.StructureSearch.ExpandResponse2:
        """    
             This operation initiates a sequence of operations to expand BOMLine objects
             based on  filter information on BOMWindow and returns a list of BOMLine
             objects. Filter information could be a complex expression set that combines multiple
             simpler Expand terms in a logical sequence.
             
             Expansion is always executed within the scope of a BOMWindow under one or
             more BOMLine objects.
             
             The results of an expansion are returned one set at a time based on the pageSize.
             The ExpandResponse also contains a Cursor object that the caller uses to expand
             the next set of results by invoking the StructureManagement::StructureSearch::nextExpandBOMLines
             call.
             

Use Cases:

             1.    Expand all lines of a structure page by page by setting
             levels to 0 (expand all levels) and pageSize is 100. The operation will return the
             result breadth first.
             
             2.    Expand all lines of a structure by setting levels to 0
             (expand all levels) and pageSize is 0.
             
             3.    Expand all child lines of a list of lines by setting level
             to 1 and pageSize is 100.
             
             4.    Expand all child lines from the structure based on the
             given pageSize.
             
             The returned childlines may or may not contain specific datasets. For example, if
             dataset information is specified - dataset relation is IMAN_reference and dataset
             type is Text then the response will contain the specified datasets (if there are
             any).
             
             5.    Expand the child lines from the structure given the page
             size. The dataset information contains the minimum number of dataset objects to be
             returned. For example, dataset relation is given as IMAN_reference, dataset type
             is Text, expandRelatedObjects is 1 and min datasets to be returned is set to 10.
             In this case, the response will contain only 10 specified datasets.
             
             6.     Expand the child lines from the structure given the page
             size. When dataset information specify the dataset relation and dataset type. In
             this case, the response will contain 0 datasets.
             
             7.    Expand the child lines defined by the Expand criteria (Expand
             criteria given in the BOM window) given the page size.
             

Teamcenter Component:

             Search - The capabilities to allow searching objects using the business object symantics
             that have been persisted via the persistence management.
             
        :param BomLines: 
                         Input for executing the expansion.
             
        :param ExpandSettings: 
                         childrenThenDepthFirst: TRUE/FALSE, TRUE means expand children and then depth
                         first.
             
        :param PageSize: 
                         Value: 0 means unlimited.
             
        :param ExpandOptions: 
                         Expand Options for the operation.
             
        :return: 214560        Invalid named reference for DataSet objects.
        """
        ...

class StructureService:
    """
    
            Contains basic structure management operations like structure clone
supporting operations,
            BOMLine creation, copying, resequencing, pack/unpack, closure rule
changes,
            structure unloading, etc.

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def Duplicate(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateInputInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateResponse:
        """    
             This operation will create a duplicate (clone) of the input structure from its top
             level down.
             
             Depending on the user action, all or some of the original structure is duplicated
             and the rest is referenced.  The user has the option to de-select a sub assembly
             or leaf Item on the duplicate dialog.  Those Item objects that are
             not selected in the duplicate dialog will not be cloned but referenced from the original
             structure.
             

             The user can define a specific naming pattern for the ItemIds of the duplicated (cloned)
             structure.  The user can define specific ItemIds for individually selected ItemRevision
             objects or a default naming pattern for the duplicated structure.   The default pattern
             can be defined by adding prefixes, suffixes or replacing part of the original name
             with a different pattern.  The user can also choose to allow the system to assign
             default ids.
             

             All of the structure dependent data of the input structure like datasets and attachments
             are copied to the duplicated structure based on the Business Modeler IDE deep copy
             rules for SaveAs.  The duplicate operation
             internally uses SaveAs at every level of
             the structure; therefore it uses the SaveAs
             deep copy rules.
             

             CAD specific attachments and relations are copied based on the transfer mode defined
             for the Business Modeler IDE global constant StructureCloneTransferModes.
             The transfer mode contains dependent closure rules for expansion and cloning.  The
             value for the closure rules is added by the installed CAD system.
             

             For e.g. The closure rule defined for IPEM ProE integration (ipemSCloneClosureRule)
             looks like this:
             

TYPE.ProPrt:CLASS.ItemRevision:RELATIONP2S.IPEM_master_dependency:PROCESS:PartFamilyMaster:R,
             TYPE.ProAsm:CLASS.ItemRevision:RELATIONP2S.IPEM_master_dependency:PROCESS:PartFamilyMaster:R,
             TYPE.ProPrt:CLASS.ItemRevision:RELATIONS2P.IPEM_master_dependency:PROCESS+TRAVERSE:PartFamilyMember,
             


Note: The difference between the three operations duplicate,
             duplicate2 and duplicate3
             are the following:
             

duplicate and duplicate2

             - In duplicate the input top BOMLine
             is the top BOMLine of the original configured structure in Structure Manager.
             In duplicate2 the input top BOMLine
             is the selected BOMLine from the configured structure in Structure Manager
             or Systems Engineering.  i.e. the user can select to clone a sub-assembly of the
             original structure.
             

             - The input for duplicate2 includes project(s).
             The cloned structure is assigned to those project(s).  duplicate
             does not have project(s) as input.
             

duplicate2 and duplicate3

             - duplicate3 was created as a result of the
             Multi Field Key (MFK ) project.   The difference between duplicate2
             and duplicate3 is that in duplicate2 is that the input and output had a DuplicateIdMap2 whereas to align with the MFK project, duplicate3 has a DuplicateIdStructure.
             


Use Cases:

Use case1: Simple Clone

             A user has an assembly which does not have cad dependencies nor does it belong to
             a specific project(s).  The user wants to duplicate the entire structure with a specific
             naming pattern for the ItemIds.  The naming pattern is a prefix "test_".
             

             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned, and the naming pattern for the new structure.  The result
             is a new structure with the following naming pattern for the ItemIds -> test_OriginalItemId.
             

Use case2: CAD Clone

             A user has an assembly structure which has cad dependencies.  The user wants to start
             a new product with a similar structure and cad dependencies.  The expansion and cloning
             rules have been defined in the Business Modeler IDE global constant StructureCloneTransferModes

             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned.
             
             The user picks the cad dependency option "Part Families
             Masters".  The expansion and cloning will be done based on the closure rules
             defined for Part Family Master in the CAD closure rules.
             
             The "Rename Cad Files" will be passed to
             the CAD integration in a callback.  If the "Rename
             Cad Files", is set to true by the user, the cad files need to be renamed by
             the cad integration.
             
             The result will be a duplicated structure with the expected cad dependencies and
             it will open in the CAD tool without any errors.
             


Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A list of <font face="courier" height="10">DuplicateInputInfo</font>, the struct
                         that contains the information needed to duplicate (clone) an assembly structure.
             
        :return: 
        """
        ...
    def ExpandOrUpdateDuplicateItems(self, Infos: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsResponse:
        """    
             This operation is called as part of the duplicate functionality.   It expands the
             structure one level at a time and gets structure dependent data. The dependencies
             have been defined to allow duplication of CAD dependent structure.  The expandOrUpdateDuplicateItems operation uses Business Modeler IDE
             global constant StructureCloneTransferModes to determine which of the cad
             specific attachments and relationships can be expanded. This constant defines the
             transfer modes containing dependent closure rules for expansion and cloning.  The
             value for the closure rules is added by the installed CAD system.
             

             Note: The difference between expandOrUpdateDuplicateItems,
             expandOrUpdateDuplicateItems2 and expandOrUpdateDuplicateItems3 are as follows:
             

             Difference in expandOrUpdateDuplicateItems
             and expandOrUpdateDuplicateItems2

             -    We allow the user to select a sub assembly for duplication.
             There is a performance problem that was uncovered.  Even though a sub assembly is
             sent for duplication, traversal on the server side was happening from the top BOMLine
             of the structure.  To improve the performance we get a BOB object.
             

             -    The smart selection logic was added to decide whether to
             clone or reference an Item in a structure based on the project that the top
             line of the original structure belongs to.  This smart selection logic is bottom
             up, so if a child is selected based on project assignment, the parent will be selected,
             no matter whether the parent belongs to the top item project assignment or not.
             

             Difference in expandOrUpdateDuplicateItems2
             and expandOrUpdateDuplicateItems3

             The mandatory flag is passed back to the client.  When a cad option has been flagged
             with a mandatory flag, a "R" predicate in the closure rules, that option will
             come up in the Duplicate Dialog pre-checked and its selected status will be un-changeable.
             This will prevent the user from un-checking those ItemRevision objects that
             were added in to make the structure cad consistent.  That is if a family table member
             in the assembly structure has been selected for duplication, then automatically include
             all its masters from the referenced ItemRevision all the way to the top master.
             Including the masters automatically will only happen if the CAD closure rules are
             defined with a predicate "R" that says this CAD relation is mandatory for
             duplication.
             


Use Cases:

             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input and the value of the closure
             rules defined.  The input consists of the BOMLine for expansion, the ItemRevision
             objects on which to perform the expansion, and the dependency types.  The ItemRevision
             objects could be null, in which case the ItemRevision object(s) gotten from
             the expansion of the BOMLine are used.  The dependency types are checked against
             the definition in the closure rules to determine what dependent data is expanded.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Infos: 
                         It contains the <b>BOMLine</b> objects, list of <b>ItemRevision</b> objects and list
                         of Dependency types
             
        :return: 
        """
        ...
    def ValidateStructureItemIds(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ValidateStructureItemIdsInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ValidateStructureItemIdsResponse:
        """    
             This operation will validate the un-validated ItemIds that will be used to clone(duplicate)
             an assembly structure.  All portions of the structure that are displayed in the duplicate
             dialog have been validated by the client.
             

             Note: The differences between the three operations validateStructureItemIds,
             validateStructureItemIds2 and validateStructureItemIds3 are the following:
             
             - In validateStructureItemIds the input is
             the top BOMLine of the original configured structure in Structure Manager.
             In validateStructureItemIds2 the input is
             the selected BOMLine of the configured structure in Structure Manager or Systems
             Engineering.  i.e. the user can select to clone a sub-assembly of the original structure
             or the entire assembly.  The input for validateStructureItemIds2
             includes project(s).  The cloned structure is assigned to those project(s).  validateStructureItemIds did not have projects
             as input.
             

             - validateStructureItemIds3 was created as
             a result of the Multi Field Key(MFK) project.  The difference between validateStructureItemIds2 and validateStructureItemIds3
             is that in validateStructureItemIds2 the
             input and output have a DuplicateIdMap2 whereas
             to align with the MFK project, validateStructureItemIds3
             has a DuplicateIdStructure.
             


Use Cases:

             The user sends in a structure for validation of the new ItemIds .  The input to this
             operation is the top BOMLine, a map of old ItemIds to new ones for those Item
             objects that are already validated, and the default naming scheme.  Based on the
             structure traversal, the input map, and the naming scheme this operation validates
             whether the proposed names for the un-validated Item objects are valid.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         List of structure ValidateStructureItemIdsInput that contains the information needed
                         for validation before a duplicate operation  can be performed.
             
        :return: 
        """
        ...
    def Duplicate2(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure.DuplicateInputInfo2]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateResponse:
        """    
             This operation will create a duplicate (clone) of the input structure from its top
             level down or a selected sub assembly.
             
             Depending on the user action, all or some of the original structure is duplicated
             and the rest is referenced.  The user has the option to de-select a sub assembly
             or leaf Item on the duplicate dialog.  Those Item objects that are
             not selected in the duplicate dialog will not be cloned but referenced from the original
             structure.
             
             The user can define a specific naming pattern for the ItemIds of the duplicated (cloned)
             structure.  The user can define specific ItemIds for individually selected ItemRevision
             objects or a default naming pattern for the duplicated structure.   The default pattern
             can be defined by adding prefixes, suffixes or replacing part of the original name
             with a different pattern.  The user can also choose to allow the system to assign
             default ids.
             
             If project(s) have been passed in as input, the cloned structure is assigned to that
             project(s).  By default the projects to which the top BOMLine in the duplicate
             dialog belongs and to which the user has access, is used to populate the project
             list.  The user has the option to modify that list based on which projects are available
             to that user.
             
             All of the structure dependent data of the input structure like datasets and attachments
             are copied to the duplicated structure based on the Business Modeler IDE deep copy
             rules for SaveAs.  The duplicate operation
             internally uses SaveAs at every level of
             the structure; therefore it uses the SaveAs
             deep copy rules.
             
             If the structure being cloned is a Requirements Manager structure, tracelink GRMs
             are handled based on the deep copy rules set for ReqRev for SaveAs.
             
             Target                            
             ReqRev
             
             Relation                        
             FND_TraceLink                
             
             Attached Type                ReqRev
             
             Operation                        SaveAs
             
             Action                            
             CopyAsReference
             
             Condition
             
             Direction                        
             IsTargetPrimary= false
             

             CAD specific attachments and relations are copied based on the transfer mode defined
             for the Business Modeler IDE global constant StructureCloneTransferModes.
             The transfer mode contains dependent closure rules for expansion and cloning.  The
             value for the closure rules is added by the installed CAD system.
             
             For e.g. The closure rule defined for IPEM ProE integration (ipemSCloneClosureRule)
             looks like this:
             
TYPE.ProPrt:CLASS.ItemRevision:RELATIONP2S.IPEM_master_dependency:PROCESS:PartFamilyMaster:R,
             TYPE.ProAsm:CLASS.ItemRevision:RELATIONP2S.IPEM_master_dependency:PROCESS:PartFamilyMaster:R,
             TYPE.ProPrt:CLASS.ItemRevision:RELATIONS2P.IPEM_master_dependency:PROCESS+TRAVERSE:PartFamilyMember,


Note: The difference between the three operations duplicate,
             duplicate2 and duplicate3
             are the following:
             
duplicate and duplicate2

             - In duplicate the input top BOMLine
             is the top BOMLine of the original configured structure in Structure Manager.
             In duplicate2 the input top BOMLine
             is the selected BOMLine from the configured structure in Structure Manager
             or Systems Engineering.  i.e. the user can select to clone a sub-assembly of the
             original structure.
             
             - The input for duplicate2 includes project(s).
             The cloned structure is assigned to those project(s).  duplicate
             does not have project(s) as input.
             

duplicate2 and duplicate3

             - duplicate3 was created as a result of the
             Multi Field Key (MFK ) project.   The difference between duplicate2
             and duplicate3 is that in duplicate2 is that the input and output had a DuplicateIdMap2 whereas to align with the MFK project, duplicate3 has a DuplicateIdStructure



Use Cases:

Use case1: Simple Clone

             A user has an assembly which does not have cad dependencies nor does it belong to
             a specific project(s).  The user wants to duplicate the entire structure with a specific
             naming pattern for the ItemIds.  The naming pattern is a prefix "test_".

             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned, and the naming pattern for the new structure.  The result
             is a new structure with the following naming pattern for the ItemIds -> test_OriginalItemId.
             

Use case2: CAD Clone

             A user has an assembly structure which has cad dependencies.  The user wants to start
             a new product with a similar structure and cad dependencies.  The expansion and cloning
             rules have been defined in the Business Modeler IDE global constant StructureCloneTransferModes.
             
             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned.
             
             The user selects the cad dependency option Part Family Master.  The expansion and
             cloning will be done based on the closure rules defined for Part Family Master in
             the CAD closure rules.
             
             The "Rename Cad Files" will be passed to
             the CAD integration in a callback.  If the "Rename
             Cad Files", is set to true by the user, the cad files need to be renamed by
             the cad integration.
             
             The result will be a duplicated structure with the expected cad dependencies and
             it will open in the CAD tool without any errors.
             

Use case3: Requirements Manager (Systems Engineering) Clone:

             The user has a requirements manager structure with internal and/or external tracelink
             GRMs that need to be copied to the cloned structure.  The user defines a set of projects
             to which the newly cloned structure should belong.  The user does not want to clone
             the entire structure only a sub-assembly.
             
             The precondition to this operation, is that the deep copy rules for SaveAs have been setup correctly
             
             The user invokes the duplicate operation by passing in the selected BOMLine
             of the sub structure to be cloned.  The projects to which the cloned structure should
             belong are passed in as input.  The naming rule for the ItemId is passed in.
             
             The result is a requirement manager structure with the tracelink relations pointing
             to the correct objects in the new structure.  And the newly cloned structure belongs
             to the defined projects for which the user has permissions.
             



Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A list of <font face="courier" height="10">DuplicateInputInfo2</font> - A struct
                         that contains the information needed to duplicate (clone) an assembly structure.
             
        :return: 
        """
        ...
    def ExpandOrUpdateDuplicateItems2(self, OpInput: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsInfo], SelectionOption: int) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsResponse:
        """    
             This operation is designed to expand structures one level at a time and get structure
             dependent data. When it is flagged for smart selection, it will try to solve the
             uncertain smart selection by expansion, in which case only qualified ItemRevision
             objects will be returned. This operation is used by the duplicate (clone) structure
             feature.  The dependencies have been defined to allow duplication of CAD dependent
             structure.  The expandOrUpdateDuplicateItems2
             operation uses Business Modeler IDE global constant StructureCloneTransferModes
             to determine which  of the cad specific attachments and relationships can be expanded.
             This constant defines the transfer modes containing dependent closure rules for expansion
             and cloning.  The value for the closure rules is added by the installed CAD system.
             

Note: The difference between expandOrUpdateDuplicateItems,
             expandOrUpdateDuplicateItems2 and expandOrUpdateDuplicateItems3 is as follows:
             

             Difference in expandOrUpdateDuplicateItems
             and expandOrUpdateDuplicateItems2

             -    We allow the user to select a sub assembly for duplication.
             There is a performance problem that was uncovered.  Even though a sub assembly is
             sent for duplication, traversal on the server side was happening from the top BOMLine
             of the structure.  To improve the performance we get a BOB object.
             

             -    The smart selection logic was added to decide whether to
             clone or reference an Item in a structure based on the project that the top
             line of the original structure belongs to.  This smart selection logic is bottom
             up, so if a child is selected based on project assignment, the parent will be selected,
             no matter whether the parent belongs to the top item project assignment or not.
             

             Difference in expandOrUpdateDuplicateItems2
             and expandOrUpdateDuplicateItems3

             The mandatory flag is passed back to the client.  When a cad option has been flagged
             with a mandatory flag, a "R" predicate in the closure rules, that option will
             come up in the Duplicate Dialog pre-checked and its selected status will be un-changeable.
             This will prevent the user from un-checking those ItemRevision objects that
             were added in to make the structure cad consistent.  That is if a family table member
             in the assembly structure has been selected for duplication, then automatically include
             all its masters from the referenced ItemRevision all the way to the top master.
             Including the masters automatically will only happen if the CAD closure rules are
             defined with a predicate "R" that says this CAD relation is mandatory for
             duplication.
             


Use Cases:

Use case 1: selectionOption is 0 and the original structure has cad data:
             
             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input and the value of the defined
             closure rule.  The input consists of the BOMLine for expansion and ItemRevision
             objects on which to perform the expansion,  the dependency types, and the selectionOption.
             The ItemRevision objects could be null, in which case the ItemRevision
             object(s) gotten from the expansion of the BOMLine are used.  The dependency
             types are checked against the definition in the closure rules to determine  what
             dependent data is expanded.
             

Use case 2: selectionOption is 1 and the original structure has no cad data
             
             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input.  In this case no closure
             rule may be defined, since the structure has no cad data.   The input consists of
             the BOMLine for expansion and ItemRevision objects on which to perform
             the expansion,  the dependency types, and the selectionOption.  The ItemRevision
             objects could be null, in which case the ItemRevision object(s) gotten from
             the expansion of the BOMLine are used.  Since the selectionOption is 1, the
             input lines will be checked based on the top BOMLine object's project assignments.
             


Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param OpInput: 
                         Contains the <b>BOMLine</b> objects, list of <b>ItemRevision</b> objects and list
                         of Dependency types
             
        :param SelectionOption: 
                         When the value is 1, the system will check the input lines based on the top <b>BOMLine</b>
                         item's project assignment. If any child belongs to the project, then the parent <b>BOMLine</b>
                         will be returned otherwise the parent <b>BOMLine</b> will not be returned. When the
                         value is 0, the operation will do expansion only.
             
        :return: 
        """
        ...
    def ValidateStructureItemIds2(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure.ValidateStructureItemIdsInfo2]) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.Structure.ValidateStructureItemIdsResponse2:
        """    
             This operation is called as part of the duplicate/clone operation.  It will validate
             the un-validated ItemIds and user selected projects that will be used to clone(duplicate)
             an assembly structure.   All portions of the structure that are displayed in the
             duplicate dialog have been validated by the client.
             

             Note: The differences between the three operations validateStructureItemIds,
             validateStructureItemIds2 and validateStructureItemIds3 are the following:
             
             - In validateStructureItemIds the input is
             the top BOMLine of the original configured structure in Structure Manager.
             In validateStructureItemIds2 the input is
             the selected BOMLine of the configured structure in Structure Manager or Systems
             Engineering.  i.e. the user can select to clone a sub-assembly of the original structure
             or the entire assembly.  The input for validateStructureItemIds2
             includes project(s).  The cloned structure is assigned to those project(s).  validateStructureItemIds did not have projects
             as input.
             

             - validateStructureItemIds3 was created as
             a result of the Multi Field Key(MFK) project.  The difference between validateStructureItemIds2 and validateStructureItemIds3
             is that in validateStructureItemIds2 the
             input and output have a DuplicateIdMap2 whereas
             to align with the MFK project, validateStructureItemIds3
             has a DuplicateIdStructure.
             


Use Cases:

             The user sends in a structure for validation of the new ItemIds.  The input to this
             operation is the top BOMLine or the selected BOMLine, a map of old
             ItemIds to new ones for those Item objects that are already validated, the
             default naming scheme and a list of user defined projects to which the duplicated
             items will be added.  Based on the structure traversal, the input map, and the naming
             scheme this operation validates whether the proposed names for the un-validated Item
             objects are valid and whether the user can add the new structure to the list of user
             defined projects.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A list of structure <font face="courier" height="10">ValidateStructureItemIdsInput2</font>
                         that contains the information needed for validation before a duplicate operation
                         would be performed.
             
        :return: 
        """
        ...
    def PackOrUnpack(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Flag: int) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Provides set-based pack/unpack functionality. When recursive option is selected,
             all loaded substructures of the selected lines will also be packed or unpacked.
             

Use Cases:


User calls the operation with some lines to pack them, the lines
             will be packed.
             
User calls the operation with root line to unpack the whole structure,
             all loaded packed lines in the structure will be unpacked.
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Lines: 
                         The lines that need to be packed. If pack all option is selected, the children of
                         the lines will be packed.
             
        :param Flag: 
                         0:pack the lines 1:unpack the lines 2:pack all lines 3:unpack all lines
             
        :return: 
        """
        ...
    def Duplicate3(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.DuplicateInputInfo3]) -> Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.DuplicateResponse:
        """    
             This operation will create a duplicate (clone) of the input structure from its top
             level down or a selected sub assembly.
             

             Depending on the user action, all or some of the original structure is duplicated
             and the rest is referenced.  The user has the option to de-select a sub assembly
             or leaf Item on the duplicate dialog.  Those Item objects that are
             not selected in the duplicate dialog will not be cloned but referenced from the original
             structure.
             

             The user can define a specific naming pattern for the ItemIds of the duplicated (cloned)
             structure.  The user can define specific ItemIds for individually selected ItemRevision
             objects or a default naming pattern for the duplicated structure.   The default pattern
             can be defined by adding prefixes, suffixes or replacing part of the original name
             with a different pattern.  The user can also choose to allow the system to assign
             default ids.
             

             If project(s) have been passed in as input, the cloned structure is assigned to that
             project(s).  By default the projects to which the top BOMLine in the duplicate
             dialog belongs and to which the user has access, is used to populate the project
             list.  The user has the option to modify that list based on which projects are available
             to that user.
             

             All of the structure dependent data of the input structure like datasets and attachments
             are copied to the duplicated structure based on the Business Modeler IDE deep copy
             rules for SaveAs.  The duplicate operation
             internally uses SaveAs at every level of
             the structure; therefore it uses the SaveAs
             deep copy rules.
             

             If the structure being cloned is a Requirements Manager structure, tracelink GRMs
             are handled based on the deep copy rules set for ReqRev for SaveAs.
             
             Target                            
             ReqRev
             
             Relation                        
             FND_TraceLink                
             
             Attached Type                ReqRev
             
             Operation                        SaveAs
             
             Action                            
             CopyAsReference
             
             Condition
             
             Direction                        
             IsTargetPrimary= false
             

             CAD specific attachments and relations are copied based on the transfer mode defined
             for the Business Modeler IDE global constant StructureCloneTransferModes.
             The transfer mode contains dependent closure rules for expansion and cloning.  The
             value for the closure rules is added by the installed CAD system.
             
             For e.g. The closure rule defined for IPEM ProE integration (ipemSCloneClosureRule)
             looks like this:
             
TYPE.ProPrt:CLASS.ItemRevision:RELATIONP2S.IPEM_master_dependency:PROCESS:PartFamilyMaster:R,
             TYPE.ProAsm:CLASS.ItemRevision:RELATIONP2S.IPEM_master_dependency:PROCESS:PartFamilyMaster:R,
             TYPE.ProPrt:CLASS.ItemRevision:RELATIONS2P.IPEM_master_dependency:PROCESS+TRAVERSE:PartFamilyMember,
             


Note: The difference between the three operations duplicate,
             duplicate2 and duplicate3
             are the following:
             
duplicate and duplicate2

             - In duplicate the input top BOMLine
             is the top BOMLine of the original configured structure in Structure Manager.
             In duplicate2 the input top BOMLine
             is the selected BOMLine from the configured structure in Structure Manager
             or Systems Engineering.  i.e. the user can select to clone a sub-assembly of the
             original structure.
             
             - The input for duplicate2 includes project(s).
             The cloned structure is assigned to those project(s).  duplicate
             does not have projects as input.
             

duplicate2 and duplicate3

             - duplicate3 was created as a result of the
             Multi Field Key (MFK ) project.   The difference between duplicate2
             and duplicate3 is that in duplicate2 is that the input and output had a DuplicateIdMap2 whereas to align with the MFK project, duplicate3 has a DuplicateIdStructure.
             


Use Cases:

Use case1: Simple Clone

             A user has an assembly which does not have cad dependencies nor does it belong to
             a specific project(s).  The user wants to duplicate the entire structure with a specific
             naming pattern for the ItemIds.  The naming pattern is a prefix "test_".
             
             The user invokes the duplicate operation by passing in the top BOMLine of the structure
             to be cloned, and the naming pattern for the new structure.  The result is a new
             structure with the following naming pattern for the ItemIds -> test_OriginalItemId.
             

Use case2: CAD Clone

             A user has an assembly structure which has cad dependencies.  The user wants to start
             a new product with a similar structure and cad dependencies.  The expansion and cloning
             rules have been defined in the Business Modeler IDE global constant StructureCloneTransferModes.
             
             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned.
             
             The user selects the cad dependency option Part Family Master.  The expansion and
             cloning will be done based on the closure rules defined for Part Family Master in
             the CAD closure rules.
             
             The "Rename Cad Files" will be passed to
             the CAD integration in a callback.  If the "Rename
             Cad Files", is set to true by the user, the cad files need to be renamed by
             the cad integration.
             
             The result will be a duplicated structure with the expected cad dependencies and
             it will open in the CAD tool without any errors.
             

Use case3: Requirements Manager (Systems Engineering) clone:

             The user has a requirements manager structure with internal and/or external tracelink
             GRMs that need to be copied to the cloned structure.  The user defines a set of projects
             to which the newly cloned structure should belong.  The user does not want to clone
             the entire structure only a sub-assembly.
             
             The precondition to this operation, is that the deep copy rules for SaveAs have been setup correctly
             
             The user invokes the duplicate operation by passing in the selected BOMLine
             of the sub structure to be cloned.  The projects to which the cloned structure should
             belong are passed in as input.  The naming rule for the ItemId is passed in.
             
             The result is a requirement manager structure with the tracelink relations pointing
             to the correct objects in the new structure.  And the newly cloned structure belongs
             to the defined projects for which the user has permissions.
             



Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A vector of DuplicateInputInfo3 structs that contains the information needed to duplicate
                         (clone) an assembly structure.
             
        :return: 
        """
        ...
    def ExpandOrUpdateDuplicateItems3(self, OpInput: list[Teamcenter.Services.Strong.Structuremanagement._2008_06.Structure.ExpandOrUpdateDuplicateItemsInfo], SelectionOption: int) -> Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.ExpandOrUpdateDuplicateItemsResponse2:
        """    
             This operation  is designed to expand structures one level at a time and get structure
             dependent data. When it is flagged for smart selection, it will try to solve the
             uncertain smart selection by expansion, in which case only qualified ItemRevision
             objects will be returned. This operation is used by the duplicate (clone) structure
             feature.  The dependencies have been defined to allow duplication of CAD dependent
             structure.  The expandOrUpdateDuplicateItems3
             operation uses Business Modeler IDE global constant StructureCloneTransferModes
             to determine which  of the cad specific attachments and relationships can be expanded.
             This constant defines the transfer modes containing dependent closure rules for expansion
             and cloning.  The value for the closure rules is added by the installed CAD system.
             For this version of the operation a mandatory clause has been added in the closure
             rules that removes the limit on one level of relationship traversal.   This was done
             to enhance the Duplicate functionality to ensure that the duplicated structure is
             CAD consistent.
             

Note: The difference between expandOrUpdateDuplicateItems,
             expandOrUpdateDuplicateItems2 and expandOrUpdateDuplicateItems3 is as follows:
             

             Difference in expandOrUpdateDuplicateItems
             and expandOrUpdateDuplicateItems2

             -    We allow the user to select a sub assembly for duplication.
             There is a performance problem that was uncovered.  Even though a sub assembly is
             sent for duplication, traversal on the server side was happening from the top BOMLine
             of the structure.  To improve the performance we get a BOB object.
             

             -    The smart selection logic was added to decide whether to
             clone or reference an Item in a structure based on the project that the top
             line of the original structure belongs to.  This smart selection logic is bottom
             up, so if a child is selected based on project assignment, the parent will be selected,
             no matter whether the parent belongs to the top item project assignment or not.
             

             Difference in expandOrUpdateDuplicateItems2
             and expandOrUpdateDuplicateItems3

             The mandatory flag is passed back to the client.  When a cad option has been flagged
             with a mandatory flag, a "R" predicate in the closure rules, that option will
             come up in the Duplicate Dialog pre-checked and its selected status will be un-changeable.
             This will prevent the user from un-checking those ItemRevision objects that
             were added in to make the structure cad consistent.  That is if a family table member
             in the assembly structure has been selected for duplication, then automatically include
             all its masters from the referenced ItemRevision all the way to the top master.
             Including the masters automatically will only happen if the CAD closure rules are
             defined with a predicate "R" that says this CAD relation is mandatory for
             duplication.
             


Use Cases:

Use case 1: selectionOption is 0 and the original structure has cad data:
             
             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input and the value of the defined
             closure rule.  The input consists of the BOMLine for expansion and ItemRevision
             objects on which to perform the expansion,  the dependency types, and the selectionOption.
             The ItemRevision objects could be null, in which case the ItemRevision object(s)
             gotten from the expansion of the BOMLine are used.  The dependency types are
             checked against the definition in the closure rules to determine  what dependent
             data is expanded.
             


             Use case 2: selectionOption is 1 and the original structure has no cad data
             
             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input.  In this case no closure
             rule may be defined, since the structure has no cad data.   The input consists of
             the BOMLine for expansion and ItemRevision objects on which to perform
             the expansion,  the dependency types, and the selectionOption.  The ItemRevision
             objects could be null, in which case the ItemRevision object(s) gotten from
             the expansion of the BOMLine are used.  Since the selectionOption is 1, the
             input lines will be checked based on the top Use case 1: selectionOption is 0 and
             the original structure has cad data:
             
             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input and the value of the defined
             closure rule.  The input consists of the BOMLine for expansion and ItemRevision objects
             on which to perform the expansion,  the dependency types, and the selectionOption.
             The ItemRevision objects could be null, in which case the ItemRevision object(s)
             gotten from the expansion of the BOMLine are used.  The dependency types are
             checked against the definition in the closure rules to determine  what dependent
             data is expanded.
             


Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param OpInput: 
                         Contains the <b>BOMLine</b> objects, list of <b>ItemRevision</b> objects and list
                         of Dependency types.
             
        :param SelectionOption: 
                         When the value is 1, the system will check the input lines based on the top <b>BOMLine</b>
                         item's project assignment. If any child belongs to the project, then the parent <b>BOMLine</b>
                         will be returned otherwise the parent <b>BOMLine</b> will not be returned. When the
                         value is 0, the operation will do expansion only.
             
        :return: 
        """
        ...
    def ValidateStructureItemIds3(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.ValidateStructureItemIdsInfo3]) -> Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.ValidateStructureItemIdsResponse3:
        """    
             This operation is called as part of the duplicate/clone operation.  It will validate
             the un-validated ItemIds and user selected projects that will be used to clone(duplicate)
             an assembly structure.   All portions of the structure that are displayed in the
             duplicate dialog have been validated by the client.
             

             Note: The differences between the three operations validateStructureItemIds,
             validateStructureItemIds2 and validateStructureItemIds3 are the following:
             
             - In validateStructureItemIds the input is
             the top BOMLine of the original configured structure in Structure Manager.
             In validateStructureItemIds2 the input is
             the selected BOMLine of the configured structure in Structure Manager or Systems
             Engineering.  i.e. the user can select to clone a sub-assembly of the original structure
             or the entire assembly.  The input for validateStructureItemIds2
             includes project(s).  The cloned structure is assigned to those project(s).  validateStructureItemIds did not have projects
             as input.
             

             - validateStructureItemIds3 was created as
             a result of the Multi Field Key(MFK) project.  The difference between validateStructureItemIds2 and validateStructureItemIds3
             is that in validateStructureItemIds2 the
             input and output have a DuplicateIdMap2 whereas
             to align with the MFK project, validateStructureItemIds3
             has a DuplicateIdStructure.
             

Use Cases:

             The user sends in a structure for validation of the new ItemIds.  The input to this
             operation is the top BOMLine or the selected BOMLine, a structure of
             old item components to new ItemId and new ItemName for those Item objects that are
             already validated, the default naming scheme and a list of user defined projects
             to which the duplicated Item objects will be added.  Based on the structure
             traversal, the input structure, and the naming scheme this operation validates whether
             the proposed names for the un-validated Item objects are valid and whether
             the user can add the new structure to the list of user defined projects.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A list of structure <font face="courier" height="10">ValidateStructureItemIdsInput3</font>
                         that contains the information needed for validation before a duplicate operation
                         would be performed.
             
        :return: 
        """
        ...
    def SetClosureRuleVariablesAndValues(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, ClosureRuleName: str, ClosureRuleVariableInfos: list[Teamcenter.Services.Strong.Structuremanagement._2011_06.Structure.ClosureRuleVariableInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Sets ClosureRule on the BOMWindow. If ClosureRule has variables
             then respective values supplied are used during ClosureRule evaluation. Only
             ClosureRule with scope PIE_TEAMCENTER is considered by this operation.
             

             In case if ClosureRule should be reset on BOMWindow then input ClosureRule
             name should be empty string.
             

Use Cases:

             Perform controlled BOM expansion using ClosureRule.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Window: 
                         The <b>BOMWindow</b> on which <b>ClosureRule</b> is to be set.
             
        :param ClosureRuleName: 
                         Valid <b>ClosureRule</b> name to search <b>ClosureRule</b> object with scope as scope
                         PIE_TEAMCENTER.
             
        :param ClosureRuleVariableInfos: 
                         List of structures holding variable name and corresponding value as string.
             
        :return: 
        """
        ...
    def UnloadBelow(self, Bomlines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], UnloadType: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation unloads and destroy the BOM structure ( i.e. BOMLine objects)
             below supplied BOMLine object or objects. It would unload associated persistence
             objects like Item, ItemRevision, PSBomViewrevision and PSOccurrence
             etc. and free up memory.
             

Use Cases:

             The operation is intended to improve the scalability of BOM structure expansion.
             From a large BOM structure, user can unload the BOM structure that he has finished
             working on. This will free up the memory which would be used for expanding another
             sub-structure that user starts working on.
             

Teamcenter Component:

             BOM Expand - Set of core services that allow to efficiently solve a product structure
             based on revision rules; effectivities etc.
             
        :param Bomlines: 
                         The <b>BOMLine</b> itself is not unloaded.
             
        :param UnloadType: 
                         Currently only <font face="courier" height="10">Unrecoverable</font> unload Type
                         is supported.
             
        :return: objects could
             not be unloaded.
        """
        ...
    def Add(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.Structure.AddParam]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.Structure.AddResponse:
        """    
             The operation adds business objects as child lines or substitutes of the specified
             lines with option to propagate transform matrix. .  The business objects can be item,
             item revision, General Design Elements, ImanItemLines or GDELines . If the business
             object to be added is a pending cut line, then the pending cut line will be processed
             after it is added. . If the business object is a WorkArea object or a line of WorkArea
             object and the object is to be added to WorkArea structure, then it will be added
             with predecessor relation. . If the object to be added is a line that contains Incremental
             Change Elements, the elements will be carried over to the newly created line. . BOMLine
             property values can be specified for the new line. . Occurrence type can be specified
             for the newline as one BOMLine property but will be handled specially.
             

Use Cases:


User  wants to add an item to a line. He/she invokes the operation
             to add it with initial values for find  number, quantity, etc. The line will be created
             with the initial BOMLine properties.
             
User wants to add an item revision as a substitute of a precise line.
             He/she invokes the operation to add it.
             
User invokes the operation to copy and paste a line. The Incremental
             Change Elements are carried over to the new line.
             
User invokes the operation to cut and paste a GDE line.
             
User paste a WorkArea object to a WorkArea structure, the newly added
             line is also added with the predecessor relationship.
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The input for the operation which contains the parent where the objects are to be
                         added, the objects to be added, initial property values, options of the operation.
             
        :return: Created lines and service data that contains partial errors.
        """
        ...
    def ValidateParentChildConditions(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.Structure.ParentChildPair]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation is to validate parent and child objects against occurrence conditions.
             

Use Cases:

             User invokes the operation to validate against occurrence conditions before creating
             two occurrences by using an ItemRevision as parent for the two occurrences
             and a General Design Element object as one child and another ItemRevision
             as another child.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         The parent child pairs to validate occurrence conditions
             
        :return: 
        """
        ...
    def ValidateOccurrenceConditions(self, Lines: list[Teamcenter.Soa.Client.Model.Strong.BOMLine], Flag: int) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation is to validate occurrences of specified lines and their substitutes
             against occurrence conditions with option to validate the whole substructure.
             

Use Cases:

             User imports a structure which has some substitutes and wants to validate the structure
             against occurrence conditions.  Invoke the operation by passing in the root line
             and the flag for recursive validation. Failed BOMLine validations are returned
             in the ServiceData object.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Lines: 
                         The <b>BOMLine</b> that the validation will be performed.
             
        :param Flag: 
                         Note: when doing recursive validation, it will not load unloaded children.
             
        :return: 
        """
        ...
    def CutItems(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_10.Structure.CutItemParam]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             Cut lines of the selected Item Revisions in a window and delete the Item
             Revisions.
             
             If the selected Item Revision is the last revision of the Item , then
             the Item will be deleted.
             

Use Cases:

Use case1: Simple Cut

             A user wants to delete some Item Revisions in a structure which are not referenced
             anywhere else. The user calls the operation with the BOMWindow and the
             Item Revisions. The BOMLine for the selected Item Revisions will
             be removed from the structure and the Item Revisions will be deleted.
             

Use case2: Cut with partial errors

             A user wants to delete some Item Revisions in a structure which are referenced
             in My Teamcenter and lines of some of the Item Revisions are in released
             structure. The user calls the operation with the BOMWindow and the Item
             revisions. The Item Revisions for the lines that are in released structure
             will fail to be deleted but the other Item Revisions will be deleted and the
             entries in My Teamcenter will also be removed.
             

Use case3: Cut the last revision of the item

             A user wants to delete an Item Revision, which is the last revision of the
             Item. The user calls the operation with the BOMWindow and the Item
             Revision. The BOMLine for the selected Item Revision will be removed
             from the structure and the Item will be deleted
             



Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Input: 
                         A structure that contains the input information for cut items.
             
        :return: 
        """
        ...
    def CloneStructure(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.Structure.CloneStructureInputInfo]) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.Structure.CloneStructureResponse:
        """    
             This operation validates and creates a duplicate (clone) of the input structure
             from its top level down or a selected sub assembly.
             

             Depending on the input arguments, all or some of the original structure is duplicated
             and the rest are referenced, revised or replaced.
             

             The caller can define a specific naming pattern for the Item ids of the duplicated
             (cloned) structure. The caller can define specific Item ids for individually selected
             ItemRevision objects or a default naming pattern for the duplicated structure.
             The default pattern can be defined by adding prefixes, suffixes or replacing part
             of the original name with a different pattern. The caller can also choose to allow
             the system to assign default ids.
             

             If project(s) have been passed in as input, the cloned structure is assigned to that
             project(s). By default the projects to which the top BOMLine in the duplicate
             dialog belongs and to which the user has access, is used to populate the project
             list. The user has the option to modify that list based on which projects are available
             to that user.
             

             All of the structure dependent data of the input structure like Datasets and
             attachments are copied to the duplicated structure based on the Business Modeler
             IDE Deep Copy Rules for SaveAs or the Deep Copy Data override rules
             parameter passed in to the input structure. The duplicate operation internally uses
             SaveAs at every level of the structure; therefore it uses the SaveAs Deep
             Copy Rules.
             

             If the structure being cloned is a Requirements Manager structure,Tracelink
             GRMs are handled based on the deep copy rules set for ReqRev for SaveAs.
             
             CAD specific attachments and relations are copied based on the transfer mode defined
             for the Business Modeler IDE global constant StructureCloneTransferModes.
             The transfer mode contains dependent closure rules for expansion and cloning. The
             value for the closure rules is added by the installed CAD system.
             

             The caller can also tell the operation to just validate only and do not perform a
             duplicate of the input structures.
             

Note: The difference between the operations duplicate4 and cloneStructure
             are the following:
             

Duplicate4 and cloneStructure

             - cloneStructure was created as a result of the project to get NX CAD on board.
             The difference is cloneStructure will now process set based inputs, it combines
             the validate and duplicate actions into one API, provides a validate only mode, introduces
             the ability to override DeepCopyData GRM rules to change the core default DeepCopy
             rules behavior (with exception of restricted rules), the ability to choose the folder
             to store new cloned root item revisions into, added two new action types revise and
             replace along with the reference and clone action types for determining what to do
             with the children of the structure being cloned and  the cloneStructure will
             return all cloned mapping information to client if requested by cloneFlags.
             


Use Cases:

Use case1: Simple Clone


             A user has an assembly which does not have cad dependencies nor does it belong to
             a specific project(s). The user wants to duplicate the entire structure with a specific
             naming pattern for the ItemIds. The naming pattern is a prefix "test_".
             
             The user invokes the duplicate operation by passing in the top BOMLine of the structure
             to be cloned, and the naming pattern for the new structure. The result is a new structure
             with the following naming pattern for the ItemIds -> test_OriginalItemId.
             

Use case2: CAD Clone


             A user has an assembly structure which has cad dependencies. The user wants to start
             a new product with a similar structure and cad dependencies. The expansion and cloning
             rules have been defined in the Business Modeler IDE global constant StructureCloneTransferModes.
             
             The user invokes the duplicate operation by passing in the top BOMLine of
             the structure to be cloned.
             
             The user selects the cad dependency option Part Family Master. The expansion and
             cloning will be done based on the closure rules defined for Part Family Master in
             the CAD closure rules.
             
             The "Rename Cad Files" will be passed to the CAD integration in a callback.
             If the "Rename Cad Files", is set to true by the user, the cad files need
             to be renamed by the cad integration.
             
             The result will be a duplicated structure with the expected cad dependencies and
             it will open in the CAD tool without any errors.
             

Use case3: Requirements Manager (Systems Engineering) clone:


             The user has a requirements manager structure with internal and/or external tracelink
             GRMs that need to be copied to the cloned structure. The user defines a set of projects
             to which the newly cloned structure should belong. The user does not want to clone
             the entire structure only a sub-assembly.
             
             The precondition to this operation, is that the deep copy rules for SaveAs
             have been setup correctly
             
             The user invokes the duplicate operation by passing in the selected BOMLine
             of the sub structure to be cloned. The projects to which the cloned structure should
             belong are passed in as input. The naming rule for the ItemId is passed in.
             
             The result is a requirement manager structure with the tracelink relations pointing
             to the correct objects in the new structure. And the newly cloned structure belongs
             to the defined projects for which the user has permissions.
             

Use Case 4: Validate and Duplicate Process with Revise and Replace Child Component
             Options


             A user has an assembly to start a new product with a similar structure but wants
             to replace and revise some components for the new structure. The user will need to
             select the components to revise from the client interface and mark those selected
             as a revise action to be recorded in the data map. Then the user will need to select
             the components to replace from the client interface and enter an existing component
             to be the replacing component for the components selected for replace. The replacing
             action will also be recorded in the data map.
             
             The results will be a cloned structure where the children selected for replace and
             revise will be replaced and revised in the new cloned structure.
             

Use Case 5: Validate Only Mode


             A user has an assembly and wants to validate it before trying to clone it. User selects
             the assembly structure and selects the "Validate Only"  option.
             
             The results is the structure will run through a validation routine and not be cloned
             at all. The information of the validation will be returned to the client where the
             user then can fix any issues or proceed with the cloning.
             

Use Case 6: Run In Background Mode


             A user has a very large assembly and wants to clone it in background mode so they
             can free up there client interface to perform other work. The user selects the assembly
             structure and selects the "Run In Background"  option.
             
             The system will return a message saying the job was dispatched. Then the system will
             validate the structure against the input provided and then duplicate the structure
             in an Asynchronous Teamcenter server thread. The results of the "Run In Background"
             process will be recorded in a text dataset that will be sent to the user via Teamcenter
             Mail Envelope.
             

Use Case 7: Simple Validate and Duplicate Process And Return Cloned Data to Client


             A user has an assembly and wants to the cloned information to be returned to the
             client. The user selects the assembly structure and sets the "return cloned object
             information"  option for the cloneFlags.
             
             The results of the "return cloned object information " option will be returned to
             the client.
             
             Note: The "return cloned object information " option is primarily used for
             CAD Integrations to resolve there internal part to part links that Teamcenter would
             not know about. The RAC Duplicate Dialog does not use this option.
             


Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param Inputs: 
                         A vector of CloneStructureInputInfo structs that contains the information needed
                         to duplicate (clone) an assembly structure. Based on whether the processInBackground
                         flag is true, CloneStructureAsync will be called.
             
        :return: 46232 - The clone structure operation was successful submitting the Asynchronous
             clone job to the dispatcher.
        """
        ...
    def CloneStructureExpandOrUpdate(self, OpInput: list[Teamcenter.Services.Strong.Structuremanagement._2014_10.Structure.CloneStructureExpandOrUpdateItemsInfo], SelectionOption: int) -> Teamcenter.Services.Strong.Structuremanagement._2014_10.Structure.CloneStructureExpandOrUpdateResponse:
        """    
             This operation expand structures one level at a time and gets structure dependent
             data.
             

             When the 'selectionOption" is set to "1" for smart selection, it will try
             to solve the uncertain smart selection by expansion, in which case only qualified
             ItemRevision objects will be returned.
             

             The following are the CAD Dependency options the user can use when expanding or Updating
             a structure to be cloned.
             

Drawings
             
Required
             
PartFamilyMaster
             
PartFamilyMember
             
AllDep
             
Internal
             



             The CAD Dependency options correspond with the CAD Dependency rules defined by the
             Business Modeler IDE global constant "StructureCloneTransferModes". The CAD
             specific rules defined in the "StructureCloneTransferModes" will determine
             which of the CAD specific attachments and relationships can be expanded and included
             as part of the structure to be cloned. The values for the closure rules is added
             by the installed CAD system.
             

Note: The differences between expandOrUpdateDuplicateItems3 and cloneStructureExpandOrUpdate
             are as follows:
             

The CAD options passed into this operation are now strings and no
             longer integers.
             
The cloneStructureExpandOrUpdate API calls a DuplicateExpandOrUpdate
             Business Object operation.The new Business Object operation allows CAD integrations
             to register extension code to identify CAD specific "Internal" relations to a structure
             being duplicated that are not published to Teamcenter.
             



Use Cases:

Use case 1: selectionOption is 0 and the original structure has CAD data:


             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input and the value of the defined
             closure rule. The input consists of the BOMLine for expansion and ItemRevision
             objects on which to perform the expansion, the dependency types, and the selectionOption.
             The ItemRevision objects could be null, in which case the ItemRevision
             object(s) gotten from the expansion of the BOMLine are used. The dependency
             types are checked against the definition in the closure rules to determine what dependent
             data is expanded.
             

Use case 2: selectionOption is 1 and the original structure has no CAD data


             The user sends in a structure for expansion, it will be expanded one level at a time
             and all dependent data will be returned based on the input. In this case no closure
             rule may be defined, since the structure has no CAD data. The input consists of the
             BOMLine for expansion and ItemRevision objects on which to perform
             the expansion, the dependency types, and the selectionOption. The ItemRevision
             objects could be null, in which case the ItemRevision object(s) gotten from
             the expansion of the BOMLine are used. Since the selectionOption is 1, the
             input lines will be checked based on the top.
             

Teamcenter Component:

             Structure Clone - Structure Clone component
             
        :param OpInput: 

        :param SelectionOption: 

        :return: 
        """
        ...
    def ToggleOccurrenceSuppression(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation toggles occurrence suppression of the selected lines.
             

Use Cases:

             User wants to suppress some lines after the structure is constructed, user can call
             this operation to toggle the occurrence suppression of the lines.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Inputs: 
                         A list of <b>BOMLine</b> object to toggle the occurrence suppression.
             
        :return: 
        """
        ...
    def TogglePrecision(self, Inputs: list[Teamcenter.Soa.Client.Model.Strong.BOMLine]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation toggles precision of all lines.
             
Note: 

             -    leaf lines cannot change precision.
             
             -    If multiple lines for same item revision are passed in to
             the operation, the precision for the structure of the lines will be changed only
             once.
             


Use Cases:

             User wants to change precision of some lines after the structure is constructed,
             user can call this operation to toggle the precisions of the lines.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param Inputs: 
                         the lines to toggle precision
             
        :return: 
        """
        ...
    def CreateInterchangeableGroups(self, Inputs: list[Teamcenter.Services.Strong.Structuremanagement._2018_11.Structure.CreateGroupInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class StructureVerificationRestBindingStub(StructureVerificationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CheckAlignment(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureVerification.BOMLinePair]) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureVerification.AlignmentCheckResponse: ...
    @typing.overload
    def AccountabilityCheck(self, Input: Teamcenter.Services.Strong.Structuremanagement._2008_12.StructureVerification.AccCheckInput) -> Teamcenter.Services.Strong.Structuremanagement._2008_12.StructureVerification.AccountabilityCheckResponse: ...
    @typing.overload
    def AccountabilityCheck(self, Input: Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.ACInput) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.AccountabilityCheckResponse: ...
    @typing.overload
    def AccountabilityCheck(self, Input: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.ACInput, BatchDetails: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.BatchDetails) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.AccountabilityCheckResponse: ...
    @typing.overload
    def CompareNetEffectivity(self, Lines: list[Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.EquivalentLines], IgnoreOverlapErrors: bool, UseStructureConfiguration: bool, ReturnOnFirstMismatch: bool) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.CompareNetEffectivityResponse: ...
    @typing.overload
    def CompareNetEffectivity(self, Lines: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], IgnoreOverlapErrors: bool, UseStructureConfiguration: bool, ReturnOnFirstMismatch: bool) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.CompareNetEffectivityResponse: ...
    @typing.overload
    def GetAssignmentComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartRelationTypes: list[str], ToolRelationTypes: list[str], CompareLA: int, CompareManual: bool) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetAssignmentComparisonDetailsResponse: ...
    @typing.overload
    def GetAssignmentComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartialMatchCriteria: list[Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.StringToPartialMatchCriteria]) -> Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.GetAssignmentComparisonDetailsResponse: ...
    def GetDescendentComparisonDetails(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], IgnoreStructureSpecific: bool) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetDescendentComparisonDetailsResponse: ...
    def GetPartitionComparisonDetails(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines]) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetPartitionComparisonDetailsResponse: ...
    def GetPredecessorComparisonDetails(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], IgnoreStructureSpecific: bool) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetPredecessorComparisonDetailsResponse: ...
    def GetPropertyComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentSetElement]) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetPropertyComparisonDetailsResponse: ...
    def PropagateProperties(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.PropagationInput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.PropagationResponse: ...
    def GetComparisonSummaries(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartialMatchCriteria: list[Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.StringToPartialMatchCriteria]) -> Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.GetComparisonSummariesResponse: ...
    def GetAttributeGroupsAndFormsComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], AttributeGroupsNames: list[str]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.StructureVerification.AttributeGroupAndFormComparisonResponse: ...
    def GetConnectedObjectsComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.StructureVerification.ConnectedObjectsComparisonResponse: ...
    def GetACFavorite(self, DatasetUID: str) -> Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureVerification.ACFavoriteInfo: ...
    def ManageACFavorites(self, Input: Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureVerification.ACFavoritesInput) -> Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureVerification.ACFavoritesResponse: ...
    def AccountabilityCheck2(self, Input: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.ACInput, BatchDetails: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.BatchDetails) -> Teamcenter.Services.Strong.Structuremanagement._2016_05.StructureVerification.AccountabilityCheckResponse: ...
    def GetAttrGrpsAndFormsComparisonDetail(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], AttributeGroupsNames: list[str], SourceConfigContext: Teamcenter.Soa.Client.Model.ModelObject, TargetConfigContext: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.StructureVerification.AttributeGroupAndFormComparisonResponse: ...

class StructureVerificationService:
    """
    
            This service provides operations related to structure verification
based on the given
            input.

            Use cases supported by this service include:

Compare the given source and target structures based on the input
            and criteria and generate a check result report.

Get comparison details between given source and target structures
            for various properties like assignment, activities, partition,
predecessors, tool
            requirement, descendents, connected objects, attachments, attribute
groups and forms.

Propagate properties from the source to the target object.

Create, update, delete or retrieve the accountability check favourite
            settings dataset.

Get detail information of changes on the source line and find the
            target lines impacted by these changes.

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> StructureVerificationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CheckAlignment(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureVerification.BOMLinePair]) -> Teamcenter.Services.Strong.Structuremanagement._2008_05.StructureVerification.AlignmentCheckResponse:
        """    
             An alignment connects two occurrences that are to be considered equivalent. They
             are referred to as source and target. An alignment can connect one source to multiple
             targets. Alignment can be used to transfer data from source to target. An alignment
             check is used to determine if the source and target of an alignment have matching
             data.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The source ebom and the target mbom structures.
             
        :return: contains ServiceData along with vector of AlignmentCheckResponse
        """
        ...
    @typing.overload
    def AccountabilityCheck(self, Input: Teamcenter.Services.Strong.Structuremanagement._2008_12.StructureVerification.AccCheckInput) -> Teamcenter.Services.Strong.Structuremanagement._2008_12.StructureVerification.AccountabilityCheckResponse: ...
    @typing.overload
    def AccountabilityCheck(self, Input: Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.ACInput) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.AccountabilityCheckResponse: ...
    @typing.overload
    def AccountabilityCheck(self, Input: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.ACInput, BatchDetails: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.BatchDetails) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.AccountabilityCheckResponse: ...
    @typing.overload
    def CompareNetEffectivity(self, Lines: list[Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.EquivalentLines], IgnoreOverlapErrors: bool, UseStructureConfiguration: bool, ReturnOnFirstMismatch: bool) -> Teamcenter.Services.Strong.Structuremanagement._2010_09.StructureVerification.CompareNetEffectivityResponse: ...
    @typing.overload
    def CompareNetEffectivity(self, Lines: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], IgnoreOverlapErrors: bool, UseStructureConfiguration: bool, ReturnOnFirstMismatch: bool) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.CompareNetEffectivityResponse: ...
    @typing.overload
    def GetAssignmentComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartRelationTypes: list[str], ToolRelationTypes: list[str], CompareLA: int, CompareManual: bool) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetAssignmentComparisonDetailsResponse: ...
    @typing.overload
    def GetAssignmentComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartialMatchCriteria: list[Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.StringToPartialMatchCriteria]) -> Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.GetAssignmentComparisonDetailsResponse: ...
    def GetDescendentComparisonDetails(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], IgnoreStructureSpecific: bool) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetDescendentComparisonDetailsResponse:
        """    
             for each input equivalent set capture the response of getDescendentComparisonDetails
             method. Has the list of details for each input set and serviceData to capture partial
             errors.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         list of equivalent sets of lines.
             
        :param IgnoreStructureSpecific: 
                         flag to indicate if non-allocated lines are to be ignored.
             
        :return: structure to capture the response of getDescendentComparisonDetails method. Has the
             list of details for each input set and serviceData to capture partial errors.
        """
        ...
    def GetPartitionComparisonDetails(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines]) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetPartitionComparisonDetailsResponse:
        """    
             service to get details on a mismatch of parititions.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         equivalent sets of src/targets objects.
             
        :return: details of a mismatch of partitions.
        """
        ...
    def GetPredecessorComparisonDetails(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], IgnoreStructureSpecific: bool) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetPredecessorComparisonDetailsResponse:
        """    
             for a given equivalent set of lines/object, compute and return the list of predecessor
             detail elements and flag if different.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         list of input equivalent objects.
             
        :param IgnoreStructureSpecific: 
                         flag to indicate if non-allocated lines are to be ignored.
             
        :return: return the list of predecessor detail elements and service data for partial errors.
        """
        ...
    def GetPropertyComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentSetElement]) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.GetPropertyComparisonDetailsResponse:
        """    
             method to retrieve details for supplied properties on the provided equivalent sets
             of lines.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         the list of equivalent objects and the property names supplied in the string map
                         of strings.
             
        :return: return the property values for each supplied equivalent set and any partial errors.
        """
        ...
    def PropagateProperties(self, Input: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.PropagationInput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.PropagationResponse:
        """    
             method to propagate properties.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The list of PropagationInput structures - one for each target which needs the changes
                         propagated to.
             
        :return: a map of string to vector of PropagationResultElement structure. The string key will
             match to the input PartialMatchCriteria.
        """
        ...
    def GetComparisonSummaries(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], PartialMatchCriteria: list[Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.StringToPartialMatchCriteria]) -> Teamcenter.Services.Strong.Structuremanagement._2012_10.StructureVerification.GetComparisonSummariesResponse:
        """    
             This operation retrieves comparison summaries for supplied extensions on the provided
             equivalent sets of objects. The source objects in each set can be BOMLines, Cpd0DesignElements
             or Cpd0DesignFeatures. The target objects in each set can be only BOMLines. For each
             received extension on each received equivalent set it performs comparison of objects
             in the equivalent set for this extension according to received criteria. For each
             such comparison only the result is returned - a flag indicating whether the input
             objects were determined different or not. This operation returns comparison results
             for any number of extensions simultaneously.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         The list of source and target objects that were deemed equivalent by some method,
                         for which extensions comparison results are required. The source objects can be BOMLines,
                         Cpd0DesignElements or Cpd0DesignFeatures. The target objects can be only BOMLines.
             
        :param PartialMatchCriteria: 
                         The list of partial match criteria for comparison. For each extension name it holds
                         a PartialMatchCriteria object with comparison criteria of this extension.
             
        :return: The operation returns the extensions comparison results for each supplied equivalent
             set. For each extension on each equivalent set it returns a boolean flag which is
             "true" if there is any difference in comparison of this equivalent set for this extension,
             and "false" otherwise. The following partial errors may be returned:  - 253049 The
             input equivalent set of lines doesn't contain any source lines or any target lines.
             - 253001 This error can only be returned if there is some kind of environment issue
             or a bug in the code, it will never happen during normal execution.
        """
        ...
    def GetAttributeGroupsAndFormsComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], AttributeGroupsNames: list[str]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.StructureVerification.AttributeGroupAndFormComparisonResponse:
        """    
             This operation returns the details of differences between the supplied Attribute
             Groups for the supplied equivalent objects (that can be Cpd0DesignElement, Cpd0DesignFeature,
             or BOMLine objects). For each supplied attribute group the operation returns the
             list of its attributes, the attributes values for each supplied source and target,
             and the result of comparing each attribute on all supplied sources and targets.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         The list ofCpd0DesignElement, Cpd0DesignFeature or BOMLine objects that  were deemed
                         equivalent by some method, for which any differences in attribute groups is required.
             
        :param AttributeGroupsNames: 
                         The list of attribute groups names that need to be compared.
             
        :return: For each supplied attribute group the operation returns the list of its attributes,
             the attributes' values for each supplied source and target, and the result of comparing
             each attribute on all supplied sources and targets. The following partial errors
             may be returned: - 253049 The input equivalent set doesn't contain any sources or
             any targets. - 253001 This error can only be returned if there is some kind of environment
             issue or a bug in the code, it will never happen during normal execution.
        """
        ...
    def GetConnectedObjectsComparisonDetails(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.StructureVerification.ConnectedObjectsComparisonResponse:
        """    
             This operation returns the details of any differences between connected objects (that
             can be either BOMLines or Cpd0DesignElements) for the supplied equivalent objects
             (that can be either BOMLines or Cpd0DesignFeatures). The operation takes the source
             and target and compares their connected objects. The source and target connected
             objects are returned by this operation in the form of a table that is created by
             the output structures.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         The list of BOMLines or Cpd0DesignFeatures that were deemed  equivalent  by some
                         method, for which any differences in connected objects are required.
             
        :return: For each input set of equivalent objects a list of comparison results of their connected
             elements (can be full match, partial match, or multiple match) and for each object
             in the set a detailed connected elements breakdown. The following partial errors
             may be returned:  - 253049 The input equivalent set doesn't contain any sources or
             any targets. -  253001 This error can only be returned if there is some kind of environment
             issue or a bug in    the code, it will never happen during normal execution.
        """
        ...
    def GetACFavorite(self, DatasetUID: str) -> Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureVerification.ACFavoriteInfo:
        """    
             This operation returns accountability check settings for a given dataset UID of accountability
             check favorite. These settings from a favorite are usually required to populate the
             accountability check dialog whenever a favorite is loaded or when accountability
             check is run.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param DatasetUID: 
                         UID of the Dataset that has the accountability check settings for the favorite.
             
        :return: 
        """
        ...
    def ManageACFavorites(self, Input: Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureVerification.ACFavoritesInput) -> Teamcenter.Services.Strong.Structuremanagement._2014_06.StructureVerification.ACFavoritesResponse:
        """    
             This operation creates, updates or deletes an accountability check favorite. Internally
             the dataset representing the accountablity check favorite is created, updated or
             deleted.
             
             To create accountability check favorite, the parameters account settings, name, description
             and action are mandatory.
             
             To update or delete accountability check favorite, the parameters action and datasetUID
             are mandatory.
             


Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         The required parameters for the manageACFavorites method.
             
        :return: Â Â Â Â 204047Â Â Â Â Â Â Â Â Dataset
             is not text type.
        """
        ...
    def AccountabilityCheck2(self, Input: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.ACInput, BatchDetails: Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.BatchDetails) -> Teamcenter.Services.Strong.Structuremanagement._2016_05.StructureVerification.AccountabilityCheckResponse:
        """    
             The operation will call the existing accountability check functions, which will generate
             a check result for report in the colored display.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param Input: 
                         Input values to the operation
             
        :param BatchDetails: 
                         In case the operation has to be performed asynchronously, this parameter can be used
                         to pass that information. Pass NULL for second parameter if unused
             
        :return: Returns the results from the accountability check and the source and target configuration
             context for source and target object.
        """
        ...
    def GetAttrGrpsAndFormsComparisonDetail(self, EquivalentObjects: list[Teamcenter.Services.Strong.Structuremanagement._2012_02.StructureVerification.EquivalentLines], AttributeGroupsNames: list[str], SourceConfigContext: Teamcenter.Soa.Client.Model.ModelObject, TargetConfigContext: Teamcenter.Soa.Client.Model.ModelObject) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.StructureVerification.AttributeGroupAndFormComparisonResponse:
        """    
             This operation returns the details of differences between the supplied Attribute
             Groups for the supplied equivalent objects (that can be Cpd0DesignElement, Cpd0DesignFeature,
             or BOMLine objects) and the supplied configuration contexts for source equivalent
             object and target equivalent object respectively.For 4gd to 4gd compare, attribute
             group names includes attribute groups and managed attribute groups.Source and target
             configuration context is needed if the attribute group names include Managed attribute
             group properties.For each supplied attribute group the operation returns the list
             of its attributes, the attributes values for each supplied source and target, and
             the result of comparing each attribute on all supplied sources and targets.
             

Teamcenter Component:

             Accountability Check - Advanced comparison of two structures
             
        :param EquivalentObjects: 
                         The list of Cpd0DesignElement, Cpd0DesignFeature or BOMLine objects that were deemed
                         equivalent by some method, for which any differences in attribute groups is required.
                         This list also contains correspo0nding configuration context for source equivalent
                         and target equivalent object.
             
        :param AttributeGroupsNames: 
                         The list of attribute groups names that need to be compared.
             
        :param SourceConfigContext: 
                         The source configuration context of source equivalent object.
             
        :param TargetConfigContext: 
                         The target configuration context of target equivalent object
             
        :return: For each supplied attribute group the operation returns the list of its attributes,
             the attributes' values for each supplied source and target, and the result of comparing
             each attribute on all supplied sources and targets. The following partial errors
             may be returned: - 253049 The input equivalent set doesn't contain any sources or
             any targets. - 253001 This error can only be returned if there is some kind of environment
             issue or a bug in the code, it will never happen during normal execution
        """
        ...

class VariantManagementRestBindingStub(VariantManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateAndSubstituteVariantItem(self, CreateAndSubstituteVIInput: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.VariantManagement.CreateAndSubsVIInput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.VariantManagement.CreateAndSubsVIResponse: ...
    def CreateVariantItem(self, CreateVIInputs: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.VariantManagement.CreateVIInput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.VariantManagement.CreateVIResponse: ...
    def GetVariantExpressionsMatchInfo(self, InputBOMLinesSets: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.InputBOMLinesSet]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.GetVariantExpressionsMatchInfoResponse: ...
    def GetBOMVariantRules(self, VariantRuleInput: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.GetBOMVariantRuleInput]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.BOMVariantRulesResponse: ...
    def SetBOMVariantRules(self, SetBOMVariantRuleInput: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.SetBOMVariantRuleData]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.SetBOMVariantRulesResponse: ...
    def ApplyBOMVariantRules(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, Rules: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.BOMVariantRuleContents]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.ApplyBOMVariantRulesResponse: ...
    def GetBOMVariantRules2(self, VariantRuleInput: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.GetBOMVariantRuleInput]) -> Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.BOMVariantRulesResponse2: ...
    def SetBOMVariantRules2(self, SetBOMVariantRuleInput: list[Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.SetBOMVariantRuleData2]) -> Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.SetBOMVariantRulesResponse2: ...
    def ApplyBOMVariantRules2(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, Rules: list[Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.BOMVariantRuleContents2]) -> Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.ApplyBOMVariantRulesResponse2: ...

class VariantManagementService:
    """
    
            This library has operations related to BOM variant functionality.
This service has
            4 operations

getBOMVariantConfigOptions

getModularOptionsForBom

createVariantItem

createAndSubstituteVariantItem

            Operations 'getBOMVariantConfigOptions'
            & 'getModularOptionsForBom'  are internal
            SOAs, and can be used only by Teamcenter Rich Client. Operations 3 &
4 are published
            and can be used by any User additional to Teamcenter Rich Client.

            Operations 'getBOMVariantConfigOptions' and
            'getModularOptionsForBom' can be used for
            getting Modular variant information defined on BOMLine object(s) and
currently
            applied variant configuration (including Legacy and Modular
variants) for BOMLine
            and its BOMWindow, respectively.

            Operation 'createVariantItem' should be used
            to create variant Item for BOMLine after applying a variant
Configuration.
            Operation 'createAndSubstituteVariantItem'
            should be invoked when user wants create new variant Item and then
substitute to
            variant BOMLine.

Dependencies:

            DataManagement

Library Reference:

TcSoaStructureManagementStrong.dll

    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> VariantManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateAndSubstituteVariantItem(self, CreateAndSubstituteVIInput: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.VariantManagement.CreateAndSubsVIInput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.VariantManagement.CreateAndSubsVIResponse:
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
    def CreateVariantItem(self, CreateVIInputs: list[Teamcenter.Services.Strong.Structuremanagement._2012_09.VariantManagement.CreateVIInput]) -> Teamcenter.Services.Strong.Structuremanagement._2012_09.VariantManagement.CreateVIResponse:
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
    def GetVariantExpressionsMatchInfo(self, InputBOMLinesSets: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.InputBOMLinesSet]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.GetVariantExpressionsMatchInfoResponse:
        """    
             This operation calculates and returns the rolledup variant expressions and rolledUp
             clause lists for the input rollUpBomLines. For the nonRolledUpBomLines, BOMLine variant
             conditions and clause lists will be returned. . If doCompare parameter is set as
             true, then this operation compares the equivalent lines based on the variant conditions
             and sets the isDifferent variable accordingly. The lines in input rollUpBomLines,
             will be compared using the rolled up variants and the lines in the nonRollUpBomLines
             list will be compared using variant conditions. All the lines in one InputBOMLinesSet
             will be compared with each other till a difference is found.
             

Teamcenter Component:

             Options & Variants - Modular and Legacy - Capability to specify variabilty (options)
             on a product structure and be able to define multiple variants and solve for a specific
             configuration.
             
        :param InputBOMLinesSets: 
                         The list of roll up BOMLine objects and non-roll up BOMLine objects.
             
        :return: A list VariantExpressionsDetails, one for each request input and serviceData for
             partial errors. The following partial errors may be returned: 1. 214506: An error
             has occurred while retrieving the variant expression match information for the input
             BOM Line set "%1$". 2. 46217: An error has occurred while calculating the Rollup
             Variant Condition for the BOM Line.
        """
        ...
    def GetBOMVariantRules(self, VariantRuleInput: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.GetBOMVariantRuleInput]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.BOMVariantRulesResponse:
        """    
             This operation takes list of window and its identifier and returns variant rules
             and saved variant rules associated with the window. As part of input in this operation
             user can provide saved variant rule along with saved variant rule action mode. This
             action indicates add, remove, update or override actions related to saved variant
             rule. There could be multiple variant rules, associated with window. List of these
             rules will be returned as the output. It also returns list of option and list of
             values associated with each option.  A flag in the value list indicates, if window
             is configured with the particular option value.  There could be multiple values associated
             with a single option and there could be multiple saved variant rules associated with
             a window.
             

Use Cases:

             This operation should be used when user wants to get variant rules associated with
             window. User may also use it to set , unset, override or update saved variant rule
             based on the window mode
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param VariantRuleInput: 
                         List of window for which variant rules are being requested
             
        :return: 
        """
        ...
    def SetBOMVariantRules(self, SetBOMVariantRuleInput: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.SetBOMVariantRuleData]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.SetBOMVariantRulesResponse:
        """    
             This operation set the input variant rule to the window and returns the list of variant
             rule and respective window.
             

Use Cases:

             This operation should be used when user want to set values of the option on variant
             rule.
             

Dependencies:

             getBOMVariantRules
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param SetBOMVariantRuleInput: 
                         List of input object containing variant rule and window on which rule will be set.
             
        :return: This operation returns variant rule and details of option values that is set to window.
        """
        ...
    def ApplyBOMVariantRules(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, Rules: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.BOMVariantRuleContents]) -> Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.ApplyBOMVariantRulesResponse:
        """    
             The applyBOMVariantRules operation applies either given BOM variant rules or Saved
             Variant Rules to the window. BOM Variant rules that contain options having multiple
             values can be applied to the window. Output will be the window and list of BOM variant
             rules and Saved Variant Rules have been applied to the window.
             

Use Cases:

             This operation will be used when BOM variant rules or Saved Variant Rules needs to
             be applied on the window.
             

Teamcenter Component:

             Product Structure Authoring - The application that allows people to create and manage
             product structure using the various components such as configuration management;
             option and variants etc.
             
        :param Window: 
<b>BOMWindow</b> object on which variant rules will be applied.
             
        :param Rules: 
                         This input has a list of BOMVariantRuleContents which contain details of variant
                         rule and list of options and values
             
        :return: This operation returns list of  BomVariantRuleContents object which contains details
             of option values that is applied to window. If multiple saved variant rules set on
             the window or options having multiple values then constraints  (defaults and derived
             defaults and rule check) will not be evaluated.
        """
        ...
    def GetBOMVariantRules2(self, VariantRuleInput: list[Teamcenter.Services.Strong.Structuremanagement._2013_05.VariantManagement.GetBOMVariantRuleInput]) -> Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.BOMVariantRulesResponse2: ...
    def SetBOMVariantRules2(self, SetBOMVariantRuleInput: list[Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.SetBOMVariantRuleData2]) -> Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.SetBOMVariantRulesResponse2: ...
    def ApplyBOMVariantRules2(self, Window: Teamcenter.Soa.Client.Model.Strong.BOMWindow, Rules: list[Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.BOMVariantRuleContents2]) -> Teamcenter.Services.Strong.Structuremanagement._2019_06.VariantManagement.ApplyBOMVariantRulesResponse2: ...

