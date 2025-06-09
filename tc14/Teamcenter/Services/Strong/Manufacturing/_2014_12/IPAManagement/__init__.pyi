import System
import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class ConsumedPartsInfo:
    """
    Structure containing information related to consumed parts.
    """
    def __init__(self, ) -> None: ...
    ConsumedPart: Teamcenter.Soa.Client.Model.ModelObject
    """A BOPLine of type Mfg0BvrPart present in the process structure."""
    ReferencedPart: Teamcenter.Soa.Client.Model.ModelObject
    """
            A BOMLine of type Mfg0BvrPart present in the product window related
            to consumedPart.
            """
    OccInformation: System.Collections.Hashtable
    """A map ( string, string ) of property information related to the occurrence of consumedPart."""

class DynamicIPAData:
    """
    A structure that contains data about a single dynamic IPA.
    """
    def __init__(self, ) -> None: ...
    DynamicIPA: Teamcenter.Soa.Client.Model.ModelObject
    """A business object from type Mfg0BvrDynamicIPA."""
    ConsumedParts: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of of BOMLine of type Mfg0BvrPart. The parts are the content (the direct children)
            of the dynamic IPA.
            """

class DynamicIPAInfo:
    """
    Structure containing information related to dynamic IPA node.
    """
    def __init__(self, ) -> None: ...
    DynamicIPA: Teamcenter.Soa.Client.Model.ModelObject
    """Dynamic IPA node (Mfg0BvrDynamicIPA)."""
    ConsumedParts: list[ConsumedPartsInfo]
    """A list of child parts of dynamic IPA node and its related information."""
    OccInformation: System.Collections.Hashtable
    """A map ( string, string ) of property information related to the of dynamic IPA node."""

class DynamicIPAsOfLine:
    """
    This structure contains data about all the dynamic IPAs of a single bop line
object.
    """
    def __init__(self, ) -> None: ...
    BopLine: Teamcenter.Soa.Client.Model.ModelObject
    """A business object from type Mfg0BvrProcess or Mfg0BvrShdStudy."""
    DynamicIPAsData: list[DynamicIPAData]
    """
            A list of DynamicIPAData structures. Each element contains data about a single dynamic
            IPA.
            """

class DynamicIPAsProcLineInfo:
    """
    This structure contains data about all the dynamic IPAs of a single bop line
object.
    """
    def __init__(self, ) -> None: ...
    BopLine: Teamcenter.Soa.Client.Model.ModelObject
    """A business object of type Mfg0BvrProcess or Mfg0BvrShdStudy."""
    DynamicIPAsInfo: list[DynamicIPAInfo]
    """A list of Dynamic IPA nodes (Mfg0BvrDynamicIPA) and its related information."""

class FindAndRepopulateDynamicIPAsResponse:
    """
    
The response of findAndRepopulateDynamicIPAs operation.

It includes:

1. The response includes data about the dynamic IPAs of all the given bop line
objects.
For each dynamic IPA, the response includes its content (i.e. parts underneath).
There can be several dynamic IPAs for every process.<br />This data is returned
for every given bop line, no matter whether its dynamic IPAs were originally
empty
or not.

2. The following partial errors are returned as part of the serviceData in case
invalid
parameters are passed to the operation:-

Â Â Â Â 25439 :- The type of the given object is not supported

Â Â Â Â 25440 :- The given object doesn't have any dynamic IPA.
    """
    def __init__(self, ) -> None: ...
    DynamicIPAsData: list[DynamicIPAsOfLine]
    """
            A list of DynamicIPAsOfLine. Each element in the list contains data about all the
            dynamic IPAs of a single line.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            The service data.
            

            The following partial errors are returned in case invalid parameters are passed to
            the operation:-
            

            25439 :- The type of the given object is not supported.
            

            25440 :- The given object doesn't have any dynamic IPA.
            """

class RepopulateDynamicIPAsData:
    """
    Input structure for the input for repopulateDynamicIPAs service.
    """
    def __init__(self, ) -> None: ...
    TopLine: Teamcenter.Soa.Client.Model.ModelObject
    """The top BOPLine of the window."""
    Ids: list[str]
    """
            A list of absolute occurrence IDs of processes (Mfg0BvrProcess) or studies
            (Mfg0BvrShdStudy) in context of topLine.
            """

class RepopulateDynamicIPAsResponse:
    """
    Response structure for repopulateDynamicIPAs service.
    """
    def __init__(self, ) -> None: ...
    DynamicIPAsData: list[DynamicIPAsProcLineInfo]
    """
            List of data containing information about process lines (Mfg0BvrProcess) and
            their respective Dynamic IPA nodes (Mfg0BvrDynamicIPA).
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Standard service data."""

class IPAManagement:
    """
    Interface IPAManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindAndRepopulateDynamicIPAs(self, InputBOPLines: list[Teamcenter.Soa.Client.Model.ModelObject]) -> FindAndRepopulateDynamicIPAsResponse:
        """    
             This operation recieves a list of ImanItemBOPLine as an input.
             
             (The type of of the bop line objects can be either Mfg0BvrProcess or Mfg0BvrShdStudy).
             

             For every given object:
             
             1. If the object does not have any dynamic IPAs, the operation issues an error.
             

             2. If the dynamic IPAs (that belong to the given object) are empty, the operation
             re-calculates them.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param InputBOPLines: 
                         (The type of of the bop line objects can be either Mfg0BvrProcess or Mfg0BvrShdStudy).
             
        :return: 2. 25440: The given object doesn't have any dynamic IPA.
        """
        ...
    def RepopulateDynamicIPAs(self, Input: RepopulateDynamicIPAsData) -> RepopulateDynamicIPAsResponse:
        """    
             The operation converts the given input list of absolute occurrence IDs to a list
             of objects (ImanItemBOPLine) and calculates/regenerates & returns dynamic
             in-process assembly nodes and its related information. The input object contains
             the top BOPLine and a list of absolute occurrence IDs of processes(Mfg0BvrProcess)
             or shared studies(Mfg0BvrShdStudy).
             

             For every given absolute occurrence IDs
             

If the object doesn't have any dynamic in-process-assembly (IPA)
             as children, the operation issues an error.
             
If the dynamic IPA nodes (that belong to the given object) are empty,
             the operation re-calculates them.
             
The response of the operation includes the dynamic IPA nodes that
             belongs to the object. For each dynamic IPA, the response includes its content (i.e.
             parts underneath) and occurrence information. Both the consumed part object (BOPLine)
             and referenced part object (BOMLine) are returned along with their related
             occurrence information.
             



             This data is returned for every given object, no matter whether its dynamic IPA nodes
             were originally empty or not.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         The top <b>BOPLine</b> and a list of absolute occurrence IDs of processes (<b>Mfg0BvrProcess</b>)
                         or shared studies (<b>Mfg0BvrShdStudy</b>).
             
        :return: 
        """
        ...

