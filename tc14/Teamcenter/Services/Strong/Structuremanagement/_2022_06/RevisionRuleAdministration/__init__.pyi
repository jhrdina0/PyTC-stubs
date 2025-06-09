import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetAPSValidRevisionRulesResponse:
    """
    Get Valid Revision Rule Response structure.
    """
    def __init__(self, ) -> None: ...
    ValidRevisionRules: list[Teamcenter.Soa.Client.Model.Strong.RevisionRule]
    """A list of RevisionRule instances."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Teamcenter service data."""

class RevisionRuleAdministration:
    """
    Interface RevisionRuleAdministration
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetAPSValidRevisionRules(self, InputObject: Teamcenter.Soa.Client.Model.Strong.WorkspaceObject) -> GetAPSValidRevisionRulesResponse:
        """    
             Retrieves the Advanced PLM Services (APS) non-suppressed revision rules (RevisionRule)
             valid for the input WorkspaceObject.
             
             Common uses for RevisionRule include configuration of product structure, Collaborative
             Design, Product Configurator, Search. Examples of Rule Entries are: Latest Entry,
             Working Entry, Status Entry, and Override Entry.
             

Use Cases:

             Input:
             
                 {
             
                     inputObject = { Cfg0ProductItem }
             
                 }
             
                 
             
             Output:
             
             The output of the operation returns valid RevisionRule objects for the given
             configurator context input which can be used to configure the configurator data objects.
             

Teamcenter Component:

             Structure - Provides basic structure maintenance facilities.
             
        :param InputObject: 
                         The input <b>WorkspaceObject</b>. The valid input types are: <b>Cfg0ConfContext</b>,
                         <b>Cfg0ProductItem</b>, <b>Item</b> and <b>Mdl0ModelElement</b>. The list of <b>RevisionRule</b>
                         objects will be valid and visible for this input object.
             
        :return: 
        """
        ...

