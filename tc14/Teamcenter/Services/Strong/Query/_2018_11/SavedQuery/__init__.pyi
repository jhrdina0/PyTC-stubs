import System
import System.Collections
import Teamcenter.Services.Strong.Query._2007_09.SavedQuery
import Teamcenter.Services.Strong.Query._2010_09.SavedQuery
import typing

class BusinessObjectQueryInput2:
    """
    Business Object Query Input. Supports Configuration Context input.
    """
    def __init__(self, ) -> None: ...
    BoTypeName: str
    """Name of business object type. Supports BusinessObject and all subtypes."""
    Clauses: list[Teamcenter.Services.Strong.Query._2010_09.SavedQuery.BusinessObjectQueryClause]
    """
            Query  clauses in search criteria. Each clause consists of property name on typeName,
            property value, logic and math operators.
            """
    MaxNumToReturn: int
    """Specified maximum number of objects to return."""
    RequestId: str
    """
            Unique ID used to register the query execution task. This can be used by the caller
            to cancel the time consuming query, the value can be generated by any unique string
            generator. The query can be cancelled by calling TcSoaFrameworkCore.Session.cancelOperations(
            requestId ).
            """
    ClientId: str
    """
            This unique ID is used to identify return data elements and partial errors associated
            with this input structure. This is currently not yet used by the return data elements,
            the caller can leave it empty.
            """
    ConfigurationContextMap: System.Collections.Hashtable
    """
            A map (string, string) of an included logical object ID and the selected Configuration
            Context UID. An Included Logical Object ( Fnd0IncludedLODef ) is a logical
            object definition that has been added to another logical object defintion.
            """

class SavedQuery:
    """
    Interface SavedQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def ExecuteBOQueriesWithContext(self, Inputs: list[BusinessObjectQueryInput2]) -> Teamcenter.Services.Strong.Query._2007_09.SavedQuery.SavedQueriesResponse: ...

