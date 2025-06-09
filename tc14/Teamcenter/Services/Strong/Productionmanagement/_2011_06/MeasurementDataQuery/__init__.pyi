import System
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class ClusterGroupInfoResponse:
    """
    
The return structure consists of vector of business objects(cluster group rev).
And
it has a partial errors object giving error information, if any
    """
    def __init__(self, ) -> None: ...
    ClusterGroupInfoSet: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]
    """A list of DPVClusterGroup _Revision(s)"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class CustomXlsbDsResponse:
    """
    
This structure consists of xlsb dataset  which is with the DPVExcel dataset  and
a partial errors object giving error information, if any.
    """
    def __init__(self, ) -> None: ...
    CustomXlsbDs: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """A list of Dpv0RuleSetDataset datasets"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class DpvRuleSetDsResponse:
    """
    
This structure consists of Vector of Ruleset Datasets  and a partial errors
object
giving error information, if any.
    """
    def __init__(self, ) -> None: ...
    DpvRuleSetDsSet: list[Teamcenter.Soa.Client.Model.Strong.Dataset]
    """
            A list of objects that includes all the Dpv0RuleSetDataset datasets associated
            with the latest revision of all the Dpv0ruleset(s) for which the user logged
            in has read privileges
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The  Service  Data"""

class LinkNameResults:
    """
    This structure conists of link name , user name and host name in it.
    """
    def __init__(self, ) -> None: ...
    LinkName: str
    """
            The measurement database link name. This information is obtained from the  USER_DB_LINKS
            and DPV_LINK_LOCATOR tables.
            """
    UserName: str
    """
            A user name for the measurement database. This information is obtained from the USER_DB_LINKS
            and DPV_LINK_LOCATOR tables.
            """
    HostName: str
    """
            Host name of the measurement database's server. This information is obtained from
            the USER_DB_LINKS and DPV_LINK_LOCATOR tables.
            """

class LinkNamesInfoResponse:
    """
    
This structure constis of one vector of structure and one vector of strigs. In
vector
of structures; the structure consists of user name,link name and host name(db
name).
In vector of strings; the string is combination of plant id and link name with
,(comma)
delimiter.And it has a partial errors object giving error information, if any
    """
    def __init__(self, ) -> None: ...
    LinkNameSet: list[LinkNameResults]
    """
            A list consisting of measurement database links,  the hosting servers, and a user
            name for each measurement database
            
"""
    PlantLinkNameSet: list[str]
    """
            A list of plant and link name combinations with "," (comma) delimiter in the format
            of
            
            "plant_id,link_name,current_db" For e.g. "GMO00001,link1,ORACLE"
            




"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The Service Data"""

class SsrsUrlInfoResponse:
    """
    
This structure consists of Vector which consists strings of Sql Server Reporing
Service(SSRS)
urls and it has a partial errors object giving error information, if any
    """
    def __init__(self, ) -> None: ...
    SsrsrUrlSet: list[str]
    """A list of strings consisting of SSRS server URLs"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The  Service  Data"""

class MeasurementDataQuery:
    """
    Interface MeasurementDataQuery
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def QueryClusterGroupInfo(self, RoutineRevs: list[Teamcenter.Soa.Client.Model.Strong.ItemRevision]) -> ClusterGroupInfoResponse:
        """    
             This operation gives a list of DPVClusterGroup _Revision(s) associated with
             a routine revision. There is no direct relation between a routine revision and cluster
             group revisions. From the routine revision, a list of DPVCluster_Revision(s)
             related to it with Manifestation relation
             is obtained. Then for each DPVCluster, the DPVClusterGroup _Revision
             to which it is related with the DPVClusterGroupContent relation is obtained
             

Use Cases:

             In the Manufacturing Process Planner (MPP) application, a list of cluster groups
             associated with a routine revision is displayed via a context menu in the routine
             revision.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param RoutineRevs: 
                         A list of routine revisions. A routine revision is an item revision of type <b>MEInspection_Revision</b>

        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def QueryCustomXlsbDs(self, XlsxDs: Teamcenter.Soa.Client.Model.Strong.Dataset) -> CustomXlsbDsResponse:
        """    
             The operation gets the Dpv0RuleSetDataset datasets associated with a DPVExcel
             dataset. The Dpv0RuleSetDataset is a dataset attached to a Dpv0rulesetRevision.
             The DPVExcel  dataset is attached to MEInspection_Revision. There is
             a relationship Dpv0CustomRoutineRuleset  between MEInspection_Revision
             and Dpv0ruleset  and based on these relations, the  Dpv0RuleSetDataset
             datasets associated with a DPVExcel dataset are obtained.
             

Use Cases:

             Display the current Dpv0RuleSetDataset datasets associated with a MEInspection_Revision.
             This information is useful prior to associating a new Dpv0RuleSetDataset dataset
             to a MEInspection_Revision.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param XlsxDs: 
                         A DPVExcel dataset
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def QueryLinkNamesInfo(self, DbType: str) -> LinkNamesInfoResponse:
        """    
             This operation will list all the database links to the Dimension Planning and Validation
             (DPV) measurement databases. It is obtained from the USER_DB_LINKS and DPV_LINK_LOCATOR
             tables.
             

Use Cases:

             The "Send Pland ID..." context menu under a plant in the Manufacturing Process
             Planner (MPP) application displays all the available links in a dialog after it is
             selected.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param DbType: 
                         The database type of the DPV measurement database. Its possible values are "<i>ORACLE</i>",
                         "<i>SQLSERVER</i>", and "<i>SQLSEERVERLOCAL</i>"
             
        :return: is a combination of plant ID and link name with
             a comma delimiter. The ServiceData  holds model objects and partial errors. No model
             objects are returned in this operation. Also, no specific partial error is returned
             by this operation and only errors from underlying subsystems are returned.
        """
        ...
    def QueryRuleSetDataSet(self) -> DpvRuleSetDsResponse:
        """    
             List all the datasets of  type Dpv0RuleSetDataset associated with the latest
             released item revisions of all Dpv0ruleset(s).
             

Use Cases:

             List all the Dpv0RuleSetDataset datasets associated with the latest revisions
             of Dpv0ruleset items so they can be associated with a routine revision of
             type MEInspection_Revision.  The Dpv0RuleSetDataset contains validation
             rules that are used to verify the DPVExcel dataset associated with routine
             revisions.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :return: 
        """
        ...
    def QuerySsrsUrlInfo(self) -> SsrsUrlInfoResponse:
        """    
             This operation gives all the SQL Server Reporting Service (SSRS) server URLs stored
             in Teamcenter. These values are stored as values of the DPV_ccuaservice_url
             preference.
             

Use Cases:

             In the Manufacturing Process Planner (MPP) application, all the SSRS server URLs
             are listed so a user can choose one of them to upload a .rdl (Report Definition Language)
             to it.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :return: 
        """
        ...

