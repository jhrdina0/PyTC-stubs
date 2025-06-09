import System
import Teamcenter.Soa.Client.Model
import typing

class DataManagement:
    """
    Interface DataManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def UnloadObjects(self, ObjsToUnload: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation unloads Business Objects. If input contains one or more Business Objects
             then it will call AOM_unload for each object otherwise it will call unloadAll  to
             unload all the objects.
             

             Note that unloadAll will unload both C++ along with POM objects.
             

        :param ObjsToUnload: 
                         A list of model objects to unload.
             
        :return: It will return partial error if any.
        """
        ...

