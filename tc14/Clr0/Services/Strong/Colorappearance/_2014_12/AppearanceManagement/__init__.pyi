import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class BusinessObjectColorAppearance:
    """
    
            This structure comprises the color appearance usage(s) associated with the input
            context business objects.
            
    """
    def __init__(self, ) -> None: ...
    ClientID: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure. This is optional parameter.
            """
    GroupName: str
    """Name of the group given on the targetObject."""
    TargetObject: Teamcenter.Soa.Client.Model.Strong.POM_object
    """
            Any object of POM_object type that is to be associated with the Clr0AppearanceUsage
            objects.
            """
    AppearanceUsages: list[ColorAppearanceUsage]
    """List of color appearance usages associated with the target object."""

class ColorAppearanceUsage:
    """
    
            The structure containing the appearance usage data corresponding to each color appearance
            block.
            
    """
    def __init__(self, ) -> None: ...
    SurfaceDesignator: str
    """The name of the surface designator."""
    ColorAppearance: Teamcenter.Soa.Client.Model.Strong.Clr0Appearance
    """Color appearance associated with the corresponding surface designator."""

class GetColorAppearanceResponse:
    """
    This is the response structure for getColorAppearance operation.
    """
    def __init__(self, ) -> None: ...
    BusinessObjectColorAppearances: list[BusinessObjectColorAppearance]
    """The list of color appearance data for input context business objects."""
    Servicedata: Teamcenter.Soa.Client.Model.ServiceData
    """Service data to return partial errors."""

class AppearanceManagement:
    """
    Interface AppearanceManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetColorAppearance(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]) -> GetColorAppearanceResponse:
        """    
             This operation returns the color appearance data associated with a given set of input
             business objects. The targetObjects represents the lists of context business objects
             attached to the color appearances e.g. the color rules attached to the color appearances.
             The getColorAppearance operation returns the color appearances for the given set
             of context business objects.
             

Teamcenter Component:

             TCBOM - 0
             
        :param TargetObjects: 
                         The list of targetObjects (context business objects).
             
        :return: 910004Â Â Â Â     You do not have sufficient privilege to get the
             color appearance(s) for the given set of business objects.
        """
        ...
    def SetColorAppearance(self, CreateInput: list[BusinessObjectColorAppearance]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation attaches business object to Color Appearance(s).  Input contains list
             of color appearances associated with the input context business objects. This operation
             first deletes all the existing color appearance data attached to input context business
             objects and then attaches color appearance data specified in input BusinessObjectColorAppearance
             list.
             

Teamcenter Component:

             TCBOM - 0
             
        :param CreateInput: 
                         The list of color appearance along with the target business objects.
             
        :return: 
        """
        ...

