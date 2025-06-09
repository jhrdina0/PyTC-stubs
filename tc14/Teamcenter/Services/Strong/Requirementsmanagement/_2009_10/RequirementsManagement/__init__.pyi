import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GetStdNoteParamAndValues:
    """
    
GetStdNoteParamAndValues structure defines
            the name and value pair of each parameter for
Fnd0ParamReqmentRevision. Each
            Parameter has list of values. And assignedValue
            has the value of parameter for Fnd0ParamReqmentRevision when it is
in context.
    """
    def __init__(self, ) -> None: ...
    Parameter: str
    """Parameter name. Example-Temperature"""
    Values: list[str]
    """
            List of values for given parameter. Example. For above parameter Temperature list
            of values can be : 0, 10, 20, 30, 40
            """
    AssignedValue: str
    """
            Current value of Parameter. Example. From the list of values as mentioned for values
            elements, the assignedValue for any specific context with relation Fnd0ListsParamReqments can be say "10" or "20" for selected parameter
            type.
            """

class StdNoteInput:
    """
    
StdNoteInput structure represents the input
            parameters of setting Standard note values. It includes Standard
Note/Parametric
            Requirement Revision object and the object of Fnd0ListsParamReqments
            relation by which it is attached to any Item/ ItemRevision.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    StandardNote: Teamcenter.Soa.Client.Model.Strong.Fnd0ParamReqmentRevision
    """Tag of Fnd0ParamReqmentRevision object."""
    StdNoteRelation: Teamcenter.Soa.Client.Model.Strong.Fnd0ListsParamReqments
    """
            Relation object of type Fnd0ListParamRequirements by which Fnd0ParamReqmentRevision
            is attached to selected object revision.
            """

class OpenStdNoteContents:
    """
    
OpenStdNoteContents structure contains input structure provided to this
operation
StdNoteInput, note text of Fnd0ParamReqmentRevision object which user want
to see/edit, body_text of Fnd0ParamReqmentRevision object, and map of the
parameter and values for the Fnd0ParamReqmentRevision object.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    InputDetails: StdNoteInput
    """
StdNoteInput structure given as input this
            operation.
            """
    ParametersOnRelation: list[GetStdNoteParamAndValues]
    """
            A list of GetStdNoteParamAndValues which
            gives the list of parameters and their values for Fnd0ParamReqmentRevision
            object.
            """
    NoteText: str
    """
            Note Text of Fnd0ParamReqmentRevision object. In this note text user can type
            any text, and parameter, and its value pair in below format
            
            [<param1 name>: value1, value2,..]
            
            Example [Temperature:0,10,20,30]
            """
    TemplateText: str
    """body_text property of Fnd0ParamReqmentRevision object."""

class OpenStdNoteResponse:
    """
    
OpenStdNoteResponse structure represents
            list of OpenStdNoteContents structure along
            with the ServiceData.
    """
    def __init__(self, ) -> None: ...
    OpenNoteObjectsDetails: list[OpenStdNoteContents]
    """
            A list of GetStdNoteParamAndValues structure
            that hold the information of Fnd0ParamReqmentRevision objects parameter values
            set in the context, note text, body_text property of Fnd0ParamReqmentRevision,
            and input structure as StdNoteInput.
            """
    SreviceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class SetStdNoteDetails:
    """
    
SetStdNoteDetails structure represents Standard
            Note/Parametric Requirement details with note relation object, and
values
            to set on Standard note relation.
    """
    def __init__(self, ) -> None: ...
    InputNoteDetails: StdNoteInput
    """
            A StdNoteInput structure that hold the information
            of Standard note object and Standard note relation.
            """
    Values: list[SetStdNoteParameters]
    """List of Values to be set on Standard note."""

class SetStdNoteParameters:
    """
    
SetStdNoteParameters structure represents
            Parameter and its value to be set on Standard Note Relation object.
    """
    def __init__(self, ) -> None: ...
    Parameter: str
    """Name of parameter."""
    Value: str
    """Value to be set on parameter from the list of values."""

class SetStdNoteResponse:
    """
    
SetStdNoteResponse structure represents list
            of SetStdNoteResult structure containing
            Standard Note details along with the ServiceData.
    """
    def __init__(self, ) -> None: ...
    ResultObjects: list[SetStdNoteResult]
    """
            A list of SetStdNoteResult structure that
            hold the information of Standard Note objects.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data."""

class SetStdNoteResult:
    """
    
SetStdNoteResult structure defines the output
            for each note when set Note SOA operation is invoked. It returns the
new note text
            value set on parametreized Requirement.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    StandardNote: Teamcenter.Soa.Client.Model.Strong.Fnd0ParamReqmentRevision
    """Standard Note/Parametric Requirement Revision object."""
    NoteText: str
    """
            Value of new Note Text on Standard Note/Parametric Requirement Revision
            object
            """

class RequirementsManagement:
    """
    Interface RequirementsManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def OpenStdNote(self, Input: list[StdNoteInput]) -> OpenStdNoteResponse:
        """    
             This operation helps to open Fnd0ParamReqment object, or its Revision Fnd0ParamReqmentRevision
             contents in Teamcenter MS Word view. User will get the note text associated with
             the selected Fnd0ParamReqmentRevision allowing editing in that view. Opening
             Fnd0ParamReqment/ Fnd0ParamReqmentRevision happens in two different
             ways:
             
             1.    In context with Fnd0ListsParamReqments
             relation: In this case, operation gives the Parameter/ value pairs selected in context
             for the parent object of Fnd0ListsParamReqments,
             allowing editing the values.
             
             2.    Without context: In this case, it gives note text associated
             for the Fnd0ParamReqmentRevision for view/edit purpose.
             


Use Cases:

             1.    Suppose user created Fnd0ParamReqment object, and
             now wants to see/edit note text of it, then opening Teamcenter MS Word view, user
             will see it, and can edit it.
             
             2.    Suppose user has attached any Fnd0ParamReqment/Fnd0ParamReqmentRevision
             object to any other Item/ItemRevision object with Fnd0ListsParamReqments relation, and now wants to edit/view parameter
             values which are set while attaching this Fnd0ParamReqment/Fnd0ParamReqmentRevision,
             then opening Teamcenter MS Word view will show it.
             


Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         A list of structures containing <b>Fnd0ParamReqmentRevision</b> object with <font face="courier" height="10">Fnd0ListsParamReqments</font> relation object by which
                         <b>Fnd0ParamReqmentRevision</b> is attached to any other object.
             
        :return: 
        """
        ...
    def SetStdNote(self, Input: list[SetStdNoteDetails]) -> SetStdNoteResponse:
        """    
             Sets the parameters and their values on Standard Note/Parametric Requirement.
             This SOA operation can set values on one or more Standard Note/Parametric
             Requirement in one operation call. When any Standard Note/Parametric
             Requirement attached to any ItemRevision it will get attached with relation
             Fnd0ListsParamRequirements (Parametric Requirements Lists). In that context
             if that Standard Note/Parametric Requirement object is selected, and
             edited in MS Word view, then saving of editing values from this view will
             be set on this Standard Note/Parametric Requirement using this SOA.
             This SOA will set those parameters and their values on given relation object.
             

Use Cases:

             You can edit, and set Standard Note/Parametric Requirement Parameter
             values using MS Word view in Teamcenter. This view can be launched using Window->Show
             view->Other->Teamcenter->MS Word
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         List of standard note input details with their values on parameters to be set.
             
        :return: values will be returned with client id
             mapped to error message in the ServiceData list of partial errors.
        """
        ...

