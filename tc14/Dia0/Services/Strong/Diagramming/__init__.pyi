import Dia0.Services.Strong.Diagramming._2015_07.Diagramming
import Dia0.Services.Strong.Diagramming._2017_05.Diagramming
import System
import Teamcenter.Soa.Client

class DiagrammingRestBindingStub(DiagrammingService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    def FindDiagrams(self, Input: list[Dia0.Services.Strong.Diagramming._2015_07.Diagramming.FindDiagramInputInfo]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.FindDiagramResponse: ...
    def QueryDiagramElementsAssociatedWith(self, Input: list[Dia0.Services.Strong.Diagramming._2015_07.Diagramming.DiagramQueryAssociatedInputInfo]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.ElementsResponse: ...
    def QueryDiagramElementsNotAssociated(self, Input: list[Dia0.Services.Strong.Diagramming._2015_07.Diagramming.DiagramQueryInputInfo]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.ElementsResponse: ...
    def QueryElementsNotInDiagram(self, Input: list[Dia0.Services.Strong.Diagramming._2015_07.Diagramming.DiagramQueryNotAssociatedInputInfo]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.ElementsResponse: ...
    def FindDiagrams2(self, Input: list[Dia0.Services.Strong.Diagramming._2017_05.Diagramming.FindDiagramInputInfo2]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.FindDiagramResponse: ...

class DiagrammingService:
    """
    
            Diagramming Services
            


Library Reference:

Dia0SoaDiagrammingStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> DiagrammingService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    def FindDiagrams(self, Input: list[Dia0.Services.Strong.Diagramming._2015_07.Diagramming.FindDiagramInputInfo]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.FindDiagramResponse: ...
    def QueryDiagramElementsAssociatedWith(self, Input: list[Dia0.Services.Strong.Diagramming._2015_07.Diagramming.DiagramQueryAssociatedInputInfo]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.ElementsResponse: ...
    def QueryDiagramElementsNotAssociated(self, Input: list[Dia0.Services.Strong.Diagramming._2015_07.Diagramming.DiagramQueryInputInfo]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.ElementsResponse: ...
    def QueryElementsNotInDiagram(self, Input: list[Dia0.Services.Strong.Diagramming._2015_07.Diagramming.DiagramQueryNotAssociatedInputInfo]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.ElementsResponse: ...
    def FindDiagrams2(self, Input: list[Dia0.Services.Strong.Diagramming._2017_05.Diagramming.FindDiagramInputInfo2]) -> Dia0.Services.Strong.Diagramming._2015_07.Diagramming.FindDiagramResponse: ...

