import Teamcenter.Soa.Client.Model
import typing

class PublishColumnConfigInfo:
    """
    
PublishColumnConfigInfo structure represents
            the parameters required to publish the column configuration.
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify return data elements
            and partial errors associated with this input structure.
            """
    ColumnConfiguration: Teamcenter.Soa.Client.Model.ModelObject
    """
            The Fnd0ColumnConfiguration object, that stores all preferences that needs
            to be created as site preferences.
            """

class RequirementsManagement:
    """
    Interface RequirementsManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def PublishColumnConfiguration(self, Input: list[PublishColumnConfigInfo]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation publishes the Column Configuration that is Mark as Publishable
             by the user. This operation will get the column configuration values from the specified
             Fnd0ColumnConfiguration object and create the site preferences. After creating
             the site preference it will set the "IsPublished" property to true present on the
             specified Fnd0ColumnConfiguration object.  So by creating the site preference
             these column configuration will be visible to all present users in the system. This
             operation converts the user preferences to the site level preferences in Teamcenter
             Context so that all users can use it. When user save the column configuration, applied
             on the BOM structure then it will store all applied column configuration values as
             user protection scope preferences. After that user can mark the same column configuration
             as Mark as Publishable that means user want that column configuration to be
             available to other users in the system. So Administrator privileged user can
             publish the column configuration so it will be available to all other users in the
             system. The user which originally saved the column configuration will see two preferences
             with same name, one with protection scope user and other one with site protection
             scope.
             

Use Cases:

             You can publish the column configuration that is Mark as Publishable by the
             user so that it will be visible to all other users and others users can apply the
             publish column configuration on BOM structure.
             

Teamcenter Component:

             Requirement Management - Application to manage requirements in Teamcenter.
             
        :param Input: 
                         A list of <font face="courier" height="10">PublishColumnConfigInfo</font> structures
                         which hold the required information to publish the column configuration.
             
        :return: object
             is returned in the updated object list of ServiceData. Any failure will be returned
             with client id mapped to error message in the ServiceData list of partial errors.
        """
        ...

