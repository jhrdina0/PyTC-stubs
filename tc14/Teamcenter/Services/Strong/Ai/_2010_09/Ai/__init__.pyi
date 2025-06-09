import System
import System.Collections
import Teamcenter.Services.Strong.Ai._2008_06.Ai
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GenerateAndEvaluateStructureResponse:
    """
    Response structure for generateAndEvaluateStructure method.
    """
    def __init__(self, ) -> None: ...
    XpathToValuesMap: System.Collections.Hashtable
    """
            The map of xpath to the values obtained by evaluating this xpath against the generated
            plmxml.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            partial failures are returned - along with object ids for each plmxml data could
            not be generated.
            """
    TransientFileTicket: str
    """
            If an xml is generated on server - input does not specify an existing plmxml or invalid
            filename - a fileticket is returned for that file.
            """

class Ai:
    """
    Interface Ai
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GenerateAndEvaluateStructure(self, AiObject: Teamcenter.Soa.Client.Model.Strong.AppInterface, ObjectsToProcess: list[Teamcenter.Services.Strong.Ai._2008_06.Ai.ObjectsWithConfig], ExportTransferMode: str, AbsoluteXmlFileName: str, Xpaths: list[str]) -> GenerateAndEvaluateStructureResponse:
        """    
             Service to generate a plmxml based on the input objects, configuration, transfermode
             provided and  evaluate the specified xpaths 1.0 expressions against that plmxml.
             Optionally - a pre-existing xml file can be specified (via a full path accessible
             in tc server environment). In that case, only the xpaths argument is used along with
             the absoluteXmlFile argument.
             

Teamcenter Component:

             Application Interface - Contains the Application Interface (AI) functionality, allowing
             import and export transactions between Teamcenter and external applications. This
             component contains the model, services & user interface required for working
             with AI.
             
        :param AiObject: 
                         This parameter is optional (specify NULL if not used). If specified, will be used
                         to get the export transfermode name to be used for plmxml generation.
             
        :param ObjectsToProcess: 
                         A mandatory parameter. If not specified an exception will be thrown. The list of
                         objects for which a single plmxml will be generated. The configuration for each of
                         the object is also specified here.
             
        :param ExportTransferMode: 
                         The transfermode to use for generating the plmxml file. If not specified, the aiObject's
                         transfermode is used. If neither is specified - an exception will be thrown.
             
        :param AbsoluteXmlFileName: 
                         In case there is already a plmxml file generated and available on the tcserver environment,
                         then instead of passing objectsToProcess - this argument can be passed with the absolute
                         path name of such a file. If this is specified -  only the xpaths argument is used,
                         unless the file does not exist - in which case it will be created using the other
                         arguments.
             
        :param Xpaths: 
                         The list of xpath 1.0 expressions to be used for evaluation on top of the generated
                         plmxml.
             
        :return: return the map of xpath expression to it's evaluations and any errors in serviceData.
             If an xml file is generated - the transient ticket for that file is also returned.
        """
        ...

