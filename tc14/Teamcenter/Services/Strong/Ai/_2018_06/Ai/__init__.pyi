import System
import System.Collections
import Teamcenter.Services.Strong.Ai._2006_03.Ai
import Teamcenter.Services.Strong.Ai._2008_06.Ai
import Teamcenter.Soa.Client.Model
import typing

class AdditionalInfo2:
    """
    A generic structure to capture additional information.
    """
    def __init__(self, ) -> None: ...
    IntMap: System.Collections.Hashtable
    """A map containing a set of (string/vector<int>) elements."""
    DblMap: System.Collections.Hashtable
    """A map containing a set of (string/vector<double>) elements."""
    StrMap: System.Collections.Hashtable
    """A map containing a set of (string/vector<string>) elements."""
    ObjMap: System.Collections.Hashtable
    """A map containing a set of (string/vector<businessObject>) elements."""
    DateMap: System.Collections.Hashtable
    """A map containing a set of (string/vector<dateTime>) elements."""

class ConfigurationInfo:
    """
    Configuration and Application Ref info used to find associated BOM Lines.
    """
    def __init__(self, ) -> None: ...
    ConfigInfo: Teamcenter.Services.Strong.Ai._2008_06.Ai.Configuration
    """Configuration information including BOMWindow or configuringObject."""
    AppRefs: list[Teamcenter.Services.Strong.Ai._2006_03.Ai.ApplicationRef]
    """
            List of ApplicationRef objects for which associated business objects are found.
            Using the PLMXML format.
            """
    AdditionalInfo: AdditionalInfo2
    """A generic structure to be used for additional information."""

class GetObjectsByApplicationRefsRespElem:
    """
    The objects found for the input ApplicationRefs.
    """
    def __init__(self, ) -> None: ...
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            A list of BusinessObject representing persistent or runtime business objects
            associated with the input ApplicationRef objects.
            """
    CreatedWindows: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of BOMWindow objects the client should close."""
    AdditionalInfo: AdditionalInfo2
    """Reserved for future use."""

class GetObjectsByApplicationRefsResponse:
    """
    The objects found for the input ApplicationRefs.
    """
    def __init__(self, ) -> None: ...
    ResponseElements: list[GetObjectsByApplicationRefsRespElem]
    """
            A list of GetObjectsForApplicationRefsElement objects specifying the business
            objects associated with the input list of ConfigurationInformation objects.
            """
    AdditionalInfo: AdditionalInfo2
    """Reserved for future use."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Partial errors"""

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetObjectsByApplicationRefs(self, Input: list[ConfigurationInfo]) -> GetObjectsByApplicationRefsResponse:
        """    
             This operation finds business objects associated with the list of input ApplicationRef
             objects. The ApplicationRef can be associated with either persisent or runtime
             business objects. One business object is returned for each ApplicationRef.
             If no associated business object can be found for an ApplicationRef then a
             NULL  is returned for that entry.
             

Teamcenter Component:

             MPP - Core objects and relationships used by the Manufacturing Process Planner application.
             
        :param Input: 
                         A list of <i>ConfigurationInformation</i> objects specifying the configuration and
                         <b>ApplicationRef</b> objects for which the associated business objects are needed.
             
        :return: 
        """
        ...

