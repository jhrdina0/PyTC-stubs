import Ads0.Services.Strong.Adsfoundation._2016_10.AdsFoundation
import System
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model

class AdsFoundationRestBindingStub(AdsFoundationService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def ChangeOwningProgramOfItems(self, ChangeOwningProgInput: list[Ads0.Services.Strong.Adsfoundation._2016_10.AdsFoundation.ChangeOwningProgInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class AdsFoundationService:
    """
    
            The AdsFoundation service provides operations that are specific to Aerospace &
            Defense Foundation extension.
            

            This service provides following Aerospace & Defense Foundation use cases:
            


Get list of objects matching the source document information provided
            while creating A&D objects, namely ADSPart, ADSDesign or ADSDrawing.
            




Library Reference:

Ads0SoaAdsFoundationStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> AdsFoundationService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def ChangeOwningProgramOfItems(self, ChangeOwningProgInput: list[Ads0.Services.Strong.Adsfoundation._2016_10.AdsFoundation.ChangeOwningProgInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             The operation changes the owning program of  the Item objects. Owning Program
             (owning_project attribute of item) is changed to the new value passed in.
             

Teamcenter Component:

             Aerospace and Defense Foundation - A set of capabilities/functionality (data model
             and behaviours)required for Aerospace and Defense Foundation extension.  This component
             defines Aerospace and Defense Foundation extension behavior.
             
        :param ChangeOwningProgInput: 
                         A list of <b>Item</b> objects and <b>TC_Project</b> to be the new owning program
                         of the Items
             
        :return: 900041 Only the selected Item and the latest Item Revision are updated with the new
             Owning Program, because no propagation rule is defined for Owning Programs.
        """
        ...

