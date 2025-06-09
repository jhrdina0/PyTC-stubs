import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class PrinterDefinitionOutput:
    """
    
            Printer definition output, this information will be used for the printSubmitRequest
            operation.
            
    """
    def __init__(self, ) -> None: ...
    PrinterConfigurationName: str
    """The PrintConfiguration object name."""
    PrinterName: str
    """The printer name."""
    PaperSizes: list[str]
    """List of paper sizes."""
    SupportStamp: bool
    """Support stamp or not."""
    PrintableDatasetTypeNames: list[str]
    """The printable dataset type names."""

class PrinterDefinitionResponse:
    """
    The return list of PrinterDefinitionOutput structures.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[PrinterDefinitionOutput]
    """List of PrinterDefinitionOutput."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard return; includes any error information."""

class PrintSubmitRequestInfo:
    """
    The input values needed to submit the print request.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    PrintObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that will get printed."""
    PrinterConfigurationName: str
    """The PrintConfiguration object name."""
    PrinterName: str
    """The printer name."""
    ColorMode: str
    """The print color mode."""
    UserStamp: str
    """
            Specifies text for a user stamp to be applied in addition to any existing system
            stamp configuration.
            """
    PaperSize: str
    """The print paper size."""
    PrintStamp: str
    """
            Specify whether the print stamp applies to the first page, the banner page, or all
            pages.
            """
    PageRange: str
    """Specifies a range of pages to print."""
    NumberCopies: str
    """The number of copies."""
    Collate: bool
    """
            When two or more copies are printed, this specifies whether the printed pages are
            collated.
            """
    PrintToScale: str
    """Specifies the scaling factor."""
    Orientation: str
    """Specifies the paper orientation of best fit, portrait or landscape."""
    BannerPage: str
    """
            Specifies whether to print a page including the defined stamps and listing additional
            data as specified by the VVCP setup.
            """
    ExtraInfo: System.Collections.Hashtable
    """The placeholder for extra name value pair information."""

class RenderSubmitRequestInfo:
    """
    The input values needed to submit the render request.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    RenderObjs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of objects that will get rendered."""
    Preserve: bool
    """If true preserve the previous rendered dataset, otherwise replace the rendered dataset."""
    ExtraInfo: System.Collections.Hashtable
    """The placeholder for extra name value pair information."""

class SubmitRequestOutput:
    """
    The structure contains the created request object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            The unmodified value from the PrintSubmitRequestInfo.clientId. This can be used by
            the caller to identify this data structure with the source input data.
            """
    RequestObject: Teamcenter.Soa.Client.Model.ModelObject
    """The request object created."""

class SubmitRequestResponse:
    """
    The structure contains a list of SubmitRequestOutput.
    """
    def __init__(self, ) -> None: ...
    Outputs: list[SubmitRequestOutput]
    """List of SubmitPrintRequestOutput."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard return; includes any error information."""

class PrintOrRender:
    """
    Interface PrintOrRender
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetPrinterDefinitions(self) -> PrinterDefinitionResponse:
        """    
             This operation returns Print Definition information from the PrintConfiguration
             objects defined in Teamcenter.
             

Use Cases:

             The client wants to get the information required for the Batch Print operation printSubmitRequest.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :return: 
        """
        ...
    def PrintSubmitRequest(self, Input: list[PrintSubmitRequestInfo]) -> SubmitRequestResponse:
        """    
             This operation submits print requests for batch printing.
             

Use Cases:

             The client can call this operation to do batch printing. Batch printing lets you
             select workspace objects, such as Item, ItemRevision, or Dataset
             objects, and print the associated documents with system stamps and watermarks.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Input: 
                         The input need to create batch print request.
             
        :return: 
        """
        ...
    def RenderSubmitRequest(self, Input: list[RenderSubmitRequestInfo]) -> SubmitRequestResponse:
        """    
             This operation submits render requests for rendering.
             

Use Cases:

             The client can call this operation to do the rendering on ItemRevision objects.
             When you render an ItemRevision object containing a dataset, you translate
             the associated file to an alternate format.
             

Teamcenter Component:

             Document Management - Application to manage documents in Teamcenter; including managing
             structured documents; rendition management; and digital rights management integrations.
             
        :param Input: 
                         The input values needed to submit the render request.
             
        :return: 
        """
        ...

