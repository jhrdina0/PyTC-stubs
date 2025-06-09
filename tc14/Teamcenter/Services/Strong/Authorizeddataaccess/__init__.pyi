import System
import Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement
import Teamcenter.Services.Strong.Authorizeddataaccess._2009_10.LicenseManagement
import Teamcenter.Services.Strong.Authorizeddataaccess._2012_09.LicenseManagement
import Teamcenter.Services.Strong.Authorizeddataaccess._2013_05.LicenseManagement
import Teamcenter.Services.Strong.Authorizeddataaccess._2017_05.LicenseManagement
import Teamcenter.Services.Strong.Authorizeddataaccess._2018_06.LicenseManagement
import Teamcenter.Soa.Client
import Teamcenter.Soa.Client.Model
import typing

class LicenseManagementRestBindingStub(LicenseManagementService):
    def __init__(self, connection: Teamcenter.Soa.Client.Connection) -> None: ...
    @typing.overload
    def AttachLicenses(self, AttachLicense: list[Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def AttachLicenses(self, AttachLicense: list[Teamcenter.Services.Strong.Authorizeddataaccess._2009_10.LicenseManagement.LicenseInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteLicense(self, LicenseIds: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetLicenseDetails(self, LicenseIds: list[str]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.GetLicenseDetailsResponse: ...
    def GetLicenseIdsAndTypes(self, LicenseFilterInput: list[Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseTypeAndStatusFilter]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseIdsAndTypesResponse: ...
    def RemoveLicenses(self, RemoveLicense: list[Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetLicenseDetails(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetLicenseDetails(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2009_10.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetLicenseDetails(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2012_09.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetLicenseDetails2(self, LicenseIds: list[str]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2009_10.LicenseManagement.GetLicenseDetailsResponse: ...
    def GetLicenseDetails3(self, LicenseIds: list[str]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2012_09.LicenseManagement.GetLicenseDetailsResponse: ...
    @typing.overload
    def CreateOrUpdateLicense(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2013_05.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateOrUpdateLicense(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2018_06.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetLicenseDetails4(self, LicenseIds: list[str]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2013_05.LicenseManagement.GetLicenseDetailsResponse: ...
    def AttachOrDetachLicensesFromObjects(self, LicenseAttachOrDetachInput: list[Teamcenter.Services.Strong.Authorizeddataaccess._2017_05.LicenseManagement.LicenseAttachOrDetachInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...

class LicenseManagementService:
    """
    
            The LicenseManagement service provides operations
            to manage the Authorized Data Access (ADA) licenses. ADA licenses provide a mechanism
            to grant time bound access for specified users and groups to classified data. The
            data can be any WorkspaceObject such as an Item,  ItemRevision,
            Dataset, etc. Teamcenter provides three types of licenses based on the type
            of control needed: ITAR (International Traffic in Arms Regulation),  license for
            export controlled data,  IP (Intellectual Property) license for proprietary data
            and Exclude license for revoking access to named users and groups.
            
            The operations in this service allow creation, modification and deletion of all three
            types of ADA licenses. This service also provides operations to query for all ADA
            licenses, to get details of a specific license, to attach licenses to a WorkspaceObject
            and to detach them.
            

            The LicenseManagement service can be used for supporting following usecases:
            


Create an ADA_License business object of type ITAR/IP/Exclude
            
Modify an ADA_License business object to set/modify lock date, license
            expiry, users, groups, reason, and in accordance with information
            
Search for all ADA_License business objects the user has READ access
            to
            
Get details of a specific ADA_License business object
            
Attach ADA_License Business Objects to classified WorkspaceObject
            business objects to grant access for users and/or groups listed on the licenses
            
Detach ADA_License business objects from WorkspaceObject business
            objects
            
Delete ADA_License business objects the user has access to
            




Library Reference:

TcSoaAuthorizedDataAccessStrong.dll
            


    """
    @staticmethod
    def getService(connection: Teamcenter.Soa.Client.Connection) -> LicenseManagementService:
        """    Get service from the connection object
        :param connection: Connection class object
        :return: Returns the service object to call the correct service operation
        """
        ...
    @typing.overload
    def AttachLicenses(self, AttachLicense: list[Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def AttachLicenses(self, AttachLicense: list[Teamcenter.Services.Strong.Authorizeddataaccess._2009_10.LicenseManagement.LicenseInput]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def DeleteLicense(self, LicenseIds: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes all ADA_License business objects specified in
             licenseIds parameter. Users performing this
             operation will need privilege specified in ADA_license_administration_privilege
             site preference to delete the licenses. If the user does not have necessary privilege
             to delete the licenses, or if any license is attached to workspace objects, or, if
             there is any other error while deleting the licenses, the errors are returned as
             partial errors in ServiceData.
             

Use Cases:

             You can delete ADA_License business objects of type ITAR/IP/Exclude
             by providing license IDs for the licenses.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseIds: 
                         License IDs of the ADA licenses to delete.
             
        :return: 
        """
        ...
    def GetLicenseDetails(self, LicenseIds: list[str]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.GetLicenseDetailsResponse:
        """    
             This operation gets the properties for each ADA_License business object specified
             in licenseIds and returns them in LicenseDetails structures as part of GetLicenseDetailsResponse.
             The LicenseDetails contains information for
             properties such as license type, license ID,  expiry date, reason, and associated
             users and groups, for a given license. If there is no matching license for a given
             license ID, LicenseDetails structure for
             that license will contain Not_found as the
             value for license ID, while the rest of the parameters will contain NULL values.
             However, if the user does not have READ privilege to any license or if there is any
             unexpected error while getting property information, the errors are returned in the
             ServiceData of GetLicenseDetailsResponse.
             

Use Cases:


             Use Case 1: Get properties of an ADA License

             You can get properties of an ADA_License business object of type ITAR/IP/Exclude
             using getLicenseDetails operation by providing
             license ID for the license.
             

             Use Case 2: Check the existence of an ADA License

             You can check if an ADA_License businesses object with given license ID exists
             using getLicenseDetails operation.
             


Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseIds: 
                         License IDs of the licenses to get properties for.
             
        :return: 
        """
        ...
    def GetLicenseIdsAndTypes(self, LicenseFilterInput: list[Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseTypeAndStatusFilter]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseIdsAndTypesResponse:
        """    
             This operation gets all the ADA_License business objects based on license
             type and license status specified in licenseFilterInput
             parameter. Licenses of a specific type can be queried for by specifying the license
             type as ITAR_License, IP_License or Exclude_License.
             A value of  ALL for the license type returns
             all types of ADA licenses. If the license status specified is ALL, all ADA licenses are returned, else only unlocked and unexpired
             licenses are returned. For the ADA_License business objects found, details
             like license IDs and license types are returned in LicenseIdAndType
             structures as part of LicenseIdsAndTypesResponse.
             If there is any unexpected error while getting licenses, the errors are returned
             in the serviceData of LicenseIdsAndTypesResponse.
             

Use Cases:

             Use Case 1: Get ADA Licenses based on type and status

             You can get ADA_License business objects using getLicenseIdsAndTypes
             operation based on specified license type and license status.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseFilterInput: 
                         Specifies the  type and  status of ADA licenses to get.
             
        :return: .
        """
        ...
    def RemoveLicenses(self, RemoveLicense: list[Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes/detaches ADA Licenses from WorkspaceObject business
             objects such as Item, ItemRevision, Dataset, etc. as specified
             in each LicenseInput. LicenseInput provides details of the licenses
             to be removed, and the WorkspaceObject business objects to remove the licenses
             from. Users performing this operation will need IP_ADMIN privilege to both
             the workspace objects and the licenses being removed, if the licenses are of type
             IP or Exclude, while the privilege specified in ADA_license_administration_privilege
             site preference is needed to both the workspace objects and the licenses being removed
             if the licenses are of ITAR license type. If the user does not have necessary
             privilege to remove any licenses, or if there is any other error while removing licenses,
             the errors are returned as partial errors in ServiceData.
             

Use Cases:

             Use case:
             
             You can remove ADA_License business objects from classified WorkspaceObject
             business objects to revoke access for users and/or groups listed on the licenses.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param RemoveLicense: 
                         Structures containing information of licenses to remove, and workspace objects from
                         which to remove.
             
        :return: 
        """
        ...
    @typing.overload
    def SetLicenseDetails(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2007_06.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetLicenseDetails(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2009_10.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def SetLicenseDetails(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2012_09.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetLicenseDetails2(self, LicenseIds: list[str]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2009_10.LicenseManagement.GetLicenseDetailsResponse:
        """    
             This operation gets the properties for each ADA_License business object specified
             in licenseIds and returns them in LicenseDetails structures as part of GetLicenseDetailsResponse.
             The LicenseDetails contains information for
             properties such as license type, license ID, expiry date, lock date, reason, in accordance
             with, and associated users and groups, for a given license. If there is no matching
             license for a given license ID, LicenseDetails structure for that license will contain
             Not_found as the value for license ID, while
             the rest of the parameters will contain NULL values. However, if the user does not
             have READ privilege to any license or if there is any unexpected error while getting
             property information, the errors are returned in the ServiceData
             of GetLicenseDetailsResponse.
             

Use Cases:

             Use Case 1: Get properties of an ADA License

             You can get properties of an ADA_License business object of type ITAR/IP/Exclude
             using getLicenseDetails2 operation by providing
             license ID for the license.
             

             Use Case 2: Check the existence of an ADA License

             You can check if an ADA_License businesses object with given license ID exists
             using getLicenseDetails2 operation.
             


Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseIds: 
                         License IDs of the licenses to get properties for.
             
        :return: 
        """
        ...
    def GetLicenseDetails3(self, LicenseIds: list[str]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2012_09.LicenseManagement.GetLicenseDetailsResponse:
        """    
             This operation gets the properties of anfor each ADA_License business object for
             each given specified in LicenseIds licenseIds parameter. The properties of the ADA_License
             business objects are supplied viareturned in LicenseDetails structures as part of
             LicenseDetailsResponse. The LicenseDetails contains information for properties such
             as license type, license ID, category, expiry date, lock date, reason, in accordance
             with, and associated users and groups, for a given license. If a the user does not
             have the sufficientREAD privilege to the any license,  if the a license ID does not
             exist or if there is any unexpected error of while getting property information,
             the errors are returned in the  ServiceData of LicenseDetailsResponse.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseIds: 
                         License IDs of the licenses to get properties for.
             
        :return: A list of LicenseDetails structures, one for each found ADA_License business object,
             and a ServiceData element as part of LicenseDetailsResponse. The properties of given
             ADA_License business objects are returned via LicenseDetails of LicenseDetailsResponse.
             If a the user does not have the sufficient READ privilege to the any license,  if
             the a license ID does not exist or if there is any unexpected error of while getting
             property information, the errors is are returned in ServiceData of LicenseDetailsResponse.
        """
        ...
    @typing.overload
    def CreateOrUpdateLicense(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2013_05.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    @typing.overload
    def CreateOrUpdateLicense(self, LicenseInfo: list[Teamcenter.Services.Strong.Authorizeddataaccess._2018_06.LicenseManagement.LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData: ...
    def GetLicenseDetails4(self, LicenseIds: list[str]) -> Teamcenter.Services.Strong.Authorizeddataaccess._2013_05.LicenseManagement.GetLicenseDetailsResponse:
        """    
             This operation gets the properties of  each ADA_License business object for each
             of the licenseIds parameter. The properties of the ADA_License business objects are
             returned in LicenseDetails structures as part of LicenseDetailsResponse. The LicenseDetails
             contains information for properties such as license type, license ID, category, citizenship,
             expiry date, lock date, reason, in accordance with, and associated users and groups,
             for a given license. If a the user does not have the sufficient READ privilege to
             the license,  if the a license ID does not exist or if there is any unexpected error
             of while getting property information, the errors are returned in the ServiceData
             of LicenseDetailsResponse.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseIds: 
                         License IDs of the licenses to get properties for.
             
        :return: A list of LicenseDetails structures, one for each found ADA_License business object,
             and a ServiceData element as part of LicenseDetailsResponse. The properties of given
             ADA_License business objects are returned via LicenseDetails of LicenseDetailsResponse.
             If a the user does not have the sufficient READ privilege to the any license,  if
             the a license ID does not exist or if there is any unexpected error of while getting
             property information, the errors is are returned in ServiceData of LicenseDetailsResponse.
             If the license cannot be found based on the licenseID given, partial error 10212
             is returned.  If the retrieve failed on any of the calls partial error 10220 is returned.
        """
        ...
    def AttachOrDetachLicensesFromObjects(self, LicenseAttachOrDetachInput: list[Teamcenter.Services.Strong.Authorizeddataaccess._2017_05.LicenseManagement.LicenseAttachOrDetachInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation attaches or detaches ADA_License objects to WorkspaceObject
             objects such as Item, ItemRevision, Dataset, etc. as specified
             in each LicenseAttachOrDetachInput. Optionally, this operation can set/update authorizing
             paragraph information for the ITAR licenses being attached. Users performing this
             operation will need IP_ADMIN privilege to both the workspace objects and the licenses
             being attached, if the licenses are of type IP or Exclude, while ITAR_ADMIN privilege
             is needed to both the workspace objects and the licenses being attached, if the licenses
             are of ITAR license type. If the user does not have necessary privilege to attach
             any licenses, or if there is any other error while attaching licenses, the errors
             are returned as partial errors in ServiceData.
             

Use Cases:


You can attach ADA_License business objects to classified
             WorkspaceObject business objects to grant access for users and/or groups listed on
             the licenses in context of structure configuration.
             
You can remove ADA_License business objects from classified
             WorkspaceObject business objects to revoke access for users and/or groups listed
             on the licenses in context of structure configuration.
             



Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseAttachOrDetachInput: 
                         A list containing attachOrDetachLicensesFromObjects.
             
        :return: 
        """
        ...

