import Ssf0.Services.Strong.Serviceforecasting._2014_06.ServiceForecasting
import Ssf0.Services.Strong.Serviceforecasting._2020_04.ServiceForecasting
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class ServiceForecastingRestBindingStub(ServiceForecastingService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def CreateMaintenanceAction(self, MaintenanceActionInput: list[Ssf0.Services.Strong.Serviceforecasting._2014_06.ServiceForecasting.MaintenanceActionInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DisposeMaintenanceAction(self, MaintenanceAction: list[Teamcenter.Soa.Client.Model.Strong.ServiceActivity], IsComplete: bool) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def ExtendMaintenanceActon(self, MantenanceActonsToBeExtended: list[Teamcenter.Soa.Client.Model.Strong.ServiceActivity], RequestedDate: System.DateTime, Note: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def LoadMaintenanceAction(self, PhysicalPart: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine, RelationName: list[str]) -> Ssf0.Services.Strong.Serviceforecasting._2014_06.ServiceForecasting.LoadMaintenanceActionsResponse: ...
    def CreateMaintenanceActionByFaultCode(self, Info: list[Ssf0.Services.Strong.Serviceforecasting._2020_04.ServiceForecasting.MaintenanceInputInfo]) -> Ssf0.Services.Strong.Serviceforecasting._2020_04.ServiceForecasting.MaintenanceActionResponse: ...

class ServiceForecastingService:
    """
    
            SOA Service for Service Forecasting
            


Library Reference:

SSF0SoaServiceForecastingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> ServiceForecastingService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def CreateMaintenanceAction(self, MaintenanceActionInput: list[Ssf0.Services.Strong.Serviceforecasting._2014_06.ServiceForecasting.MaintenanceActionInputInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates an object of type SSF0MaintenanceAction. The SSF0MaintenanceAction
             stores information like SSP0ServiceReq, StructureContext, PhyscialPart,
             ssf0Asset, due_date etc.
             

             This operation also supports the creation of related SSF0MaintenanceAction
             objects using the SSP0Requires and SSP0Satifies relations. The SSP0Requires
             relation dictates that related required SSF0MaintenanceAction must be completed
             in order for the related SSF0MaintenanceAction to be considered complete.
             The SSP0Satifies relation dictates that the related satisfies SSF0MaintenanceAction
             is considered complete when the related SSF0MaintenanceAction is completed.
             


Use Cases:

             Use Case 1 - Automatically
             

             When one or more Service Requirements are check box selected from the Service Plans
             table in the Generate Maintenance Schedule dialog and the Generate Schedule button
             is clicked the system will automatically create Maintenance Actions for all selected
             Service Requirements as well as any related requires or satisfies Service Requirements
             as part of the schedule generation process.
             

             Use Case 2 - Manually
             

             When one or more Service Requirements are check box selected from the Service Plans
             table in the Generate Maintenance Schedule dialog and the New Maintenance Action
             button is clicked the system creates a Maintenance Action for each selected Service
             Requirement as well as any related requires or satisfies Service Requirements.
             

Teamcenter Component:

             Service Forecasting - Component for identification of Service Forecasting Services
             and Operations
             
        :param MaintenanceActionInput: 
                         A list of <b>SSF0MaintenanceAction</b> Input information structures that are used
                         to create <b>SSF0MaintenanceAction</b> objects
             
        :return: 
        """
        ...
    def DisposeMaintenanceAction(self, MaintenanceAction: list[Teamcenter.Soa.Client.Model.Strong.ServiceActivity], IsComplete: bool) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation changes the status of SSF0MaintenanceAction to complete or
             canceled.
             

Use Cases:

             Use Case 1 - Automatically
             

             When an SSS0JobCard related to an SSF0MaintenanceAction is completed
             the system checks to see if all SSS0JobCard objects related to the SSF0MaintenanceAction
             are completed.  If all are completed then the system automatically calls the operation
             passing a TRUE isComplete value and the SSF0MaintenanceAction to be
             completed
             

             Use Case 2 - Manually
             

             When an SSF0MaintenanceAction is selected in the Maintenance Acton Table in
             the Generate Maintenance Schedule dialog (row in table is highlighted) and the right
             mouse button is clicked a selection menu is displayed. You can then choose to either
             Complete MA or Cancel MA. For Complete MA the isComplete value is passed as
             TRUE. For Cancel MA the isComplete value is passed as FALSE.
             

Teamcenter Component:

             Service Forecasting - Component for identification of Service Forecasting Services
             and Operations
             
        :param MaintenanceAction: 
                         A list of <b>SSF0MaintenanceAction</b> objects that are to be completed or canceled
             
        :param IsComplete: 
                         If FALSE the SSF0MaintenanceAction is canceled.
             
        :return: 
        """
        ...
    def ExtendMaintenanceActon(self, MantenanceActonsToBeExtended: list[Teamcenter.Soa.Client.Model.Strong.ServiceActivity], RequestedDate: System.DateTime, Note: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used to change the due date of an SSF0MaintenanceAction
             .The operation creates an object of type SSF0MaintenanceExtension and puts
             the new object in a workflow process for approval. An SSF0ActionExtension
             relation is created between SSF0MaintenanceExtension object and the SSF0MaintenanceAction
             object. The template name for the work flow process is retrieved from the preference
             SF_DEFAULT_WF_TEMPLATE.  When this process is completed the SSF0MaintenanceAction
             will be marked as completed.
             

Use Cases:

             Use Case 1
             

             When one or more Maintenance Actions are check box selected from the Maintenance
             Actions table in the Generate Maintenance Schedule dialog and the Extend Maintenance
             Action button is clicked the system displays the Extend Due Date dialog. Here you
             can enter in a required Due Date and an optional Note.  When the OK button is clicked
             the selected Maintenance Actions are submitted to the Extend Maintenance Action process.
             


Teamcenter Component:

             Service Forecasting - Component for identification of Service Forecasting Services
             and Operations
             
        :param MantenanceActonsToBeExtended: 
                         A list of <b>SSF0MaintenanceAction</b> objects for which due date needs to be changed.
             
        :param RequestedDate: 
                         The new due date
             
        :param Note: 
                         Additional information to pass along in the workflow process
             
        :return: 
        """
        ...
    def LoadMaintenanceAction(self, PhysicalPart: Teamcenter.Soa.Client.Model.Strong.AsMaintainedBOMLine, RelationName: list[str]) -> Ssf0.Services.Strong.Serviceforecasting._2014_06.ServiceForecasting.LoadMaintenanceActionsResponse:
        """    
             This operation returns all of the SSF0MaintenanceAction objects which are
             related to a PhysicalPart by the InProgress, Completed or STP0Voided
             relation. If only open SSF0MaintenanceAction objects are needed, the relationName
             input can be passed as InProgress. The operation will only look for the InProgress
             relation between SSF0MaintenanceAction and PhysicalPart. Similarly
             to get closed SSF0MaintenanceAction objects, Completed needs to be passed
             and to get canceled SSF0MaintenanceAction objects, Voided needs to be passed.
             
             The PhysicalPart is retrieved from the input AsMaintainedBOMLine. The
             operation also returns SSF0MaintenanceAction objects which are related to
             child lines of given AsMaintainedBOMLine.
             

Use Cases:

             Use Case 1 - Populate Maintenance Action Table in Generate Service Schedule dialog
             

             On the Maintenance Acton tab of the Generate Service Schedule dialog you can show
             the Maintenance Actions that are currently open for the selected physical part that
             was in context when the dialog was launched.  When the Show Maintenance Action button
             is clicked the system retrieves all of the open Maintenance Actions for the selected
             physical part.
             

             Use Case 2 - Populated Maintenance Action History Dialog
             

             With an As Maintained BOM Structure loaded into the Service Editor view you can right
             mouse click on any BOM Line to display the action menu.  Selecting Show Maintenance
             Action History will retrieve all complete and canceled Maintenance actions for the
             in context BOM Line.
             


Teamcenter Component:

             Service Forecasting - Component for identification of Service Forecasting Services
             and Operations
             
        :param PhysicalPart: 
                         The AsMaintainedBOMLine for which SSF0MaintenanceAction objects need to be retrived.
             
        :param RelationName: 

        :return: 302008Â Â Â Â Maintenance Actions cannot be retrieved. The provided
             As maintained bom line is not valid.
        """
        ...
    def CreateMaintenanceActionByFaultCode(self, Info: list[Ssf0.Services.Strong.Serviceforecasting._2020_04.ServiceForecasting.MaintenanceInputInfo]) -> Ssf0.Services.Strong.Serviceforecasting._2020_04.ServiceForecasting.MaintenanceActionResponse: ...

