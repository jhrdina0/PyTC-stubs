import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class FindRevisionRulesForModelResponse:
    """
    
FindRevisionRulesForModelResponse  describes
            information regarding related objects to be copied or referenced during a revise
            operation.This structure is the same as that used for save as operations.
            
    """
    def __init__(self, ) -> None: ...
    RevisonRules: list[Teamcenter.Soa.Client.Model.Strong.RevisionRule]
    """
            List of revision rules that can be used to configure content of application models
            (Mdl0ApplicationModel).
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains any errors encountered during the operation."""

class ModelConfiguration:
    """
    Interface ModelConfiguration
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def FindRevisionRulesForModel(self) -> FindRevisionRulesForModelResponse:
        """    
             Finds all revision rules which are valid for configuring content (subtypes of Mdl0ConditionalElement
             and Mdl0ConditionalArtifact) of an application model (Mdl0ApplicationModel).Not
             all revision rules can be used to configure application models; this operation aids
             the application in finding the list of revision rules which can be used for this
             type of configuration. (See Teamcenter technical documentation for further information
             regarding valid  revision rules for model content configuration.)
             

Use Cases:

             Users configure application model content to select proper revisions based on criteria
             like Working or Has Status, and by effectivity.   Revision rules capture these
             criteria and are used within Teamcenter to select revisions which match these criteria.
             Because only a subset of all Teamcenter revision rules can be used to configure
             application model content, the user/application needs a way to get the list of valid
             revision rules for this type of configuration.   The findRevisionRulesForModel
             operation is used to get this list.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :return: 
        """
        ...

