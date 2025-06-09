import Teamcenter.Soa.Client.Model
import typing

class CreateLinkNameInfoResponse:
    """
    It has a partial errors object giving error information, if any
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The  Service  Data"""

class PopulateLinkTablesResponse:
    """
    It has a partial errors object giving error information, if any
    """
    def __init__(self, ) -> None: ...
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The  Service  Data"""

class MeasurementDataLoad:
    """
    Interface MeasurementDataLoad
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateLinkNames(self, LinkName: str, UserName: str, PassWord: str, DbName: str) -> CreateLinkNameInfoResponse:
        """    
             This operation will create database links to external databases, in the Teamcenter
             database. The link names will be stored in the USER_DB_LINKS system table of the
             Teamcenter database. The external databases store measurement data for the Dimensional
             Planning and Validation (DPV) application. The link names are used to store the measurement
             data and query measurement data from measurement database by external applications,
             such as Extraction Transaction and Load (ETL) and Teamcenter lifecycle visualization.
             


Use Cases:

             In the Manufacturing Process Planner application in the Teamcenter rich client, the
             send plant ID context menu under a MEPrPlantProcessRevision object is used
             to gather measurement database name, measurement database user name, measurement
             database password, and link name. Then, this operation is used to create the database
             link.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param LinkName: 

        :param UserName: 
                         User name for the external database, <font face="courier" height="10">dbName</font>

        :param PassWord: 
                         Password for the <font face="courier" height="10">userName</font> for the external
                         database, <font face="courier" height="10">dbName</font>

        :param DbName: 
                         The external database name to which a link is created
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...
    def PopulateLinkTables(self, PlantId: str, DbName: str, UserName: str, LinkName: str, TargetDbType: str, ServerName: str, UpdateTables: str, OldLinkName: str) -> PopulateLinkTablesResponse:
        """    
             This operation will populate the DPV_DB_LOCATOR and DPV_LINK_LOCATOR  tables in the
             Teamcenter database. DPV_DB_LOCATOR table has plant ID(s) and database name(s). One
             plant ID can belong to only one database. DPV_LINK_LOCATOR  table has database names
             and corresponding database links.
             

Use Cases:

             Database links are used by external applications such as Extraction Transfer and
             Load (ETL) and standalone Teamcenter lifecycle visualization to insert data into,
             as well as, query from measurement databases.
             

Teamcenter Component:

             Database Configuration for Dimensional Planning And Validation - This is for Dimensional
             Planning and Validation
             
        :param PlantId: 
                         The plant ID
             
        :param DbName: 

        :param UserName: 

        :param LinkName: 

        :param TargetDbType: 

        :param ServerName: 

        :param UpdateTables: 

        :param OldLinkName: 
                         The old link name will be used to update the tables
             
        :return: holds model objects and
             partial errors. No model objects are returned in this operation. Also, no specific
             partial error is returned by this operation and only errors from underlying subsystems
             are returned.
        """
        ...

