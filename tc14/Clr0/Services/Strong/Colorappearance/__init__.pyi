import Clr0.Services.Strong.Colorappearance._2014_12.AppearanceManagement
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong

class AppearanceManagementRestBindingStub(AppearanceManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def GetColorAppearance(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]) -> Clr0.Services.Strong.Colorappearance._2014_12.AppearanceManagement.GetColorAppearanceResponse: ...
    def SetColorAppearance(self, CreateInput: list[Clr0.Services.Strong.Colorappearance._2014_12.AppearanceManagement.BusinessObjectColorAppearance]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class AppearanceManagementService:
    """
    
            This service contains operations for setting and getting color appearance business
            objects.
            


Library Reference:

Clr0SoaColorAppearanceStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AppearanceManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def GetColorAppearance(self, TargetObjects: list[Teamcenter.Soa.Client.Model.Strong.POM_object]) -> Clr0.Services.Strong.Colorappearance._2014_12.AppearanceManagement.GetColorAppearanceResponse:
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
    def SetColorAppearance(self, CreateInput: list[Clr0.Services.Strong.Colorappearance._2014_12.AppearanceManagement.BusinessObjectColorAppearance]) -> Teamcenter.Soa.Client.Model.ServiceData:
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

